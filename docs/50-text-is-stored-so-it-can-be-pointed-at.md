# 50. Text Is Stored So It Can Be Pointed At

> Chapter summary: A data store that can only return the whole work is not a data store for text — it is a file
> with extra steps. Reframe stores Ulysses as **one record of 1,519,413 characters and 32,694 lines**, so every
> client that wants Circe must fetch the entire book and slice it by line arithmetic in memory. That is why
> choosing a chapter opens the work at its beginning: the book is what was opened, and the chapter is a highlight
> drawn on top of it. The declaration already forbids this — `screenplay/lines.get` in `schema/idl.yaml` takes a
> `range: {startLine, endLine}` under `maxPayloadBytes: 65536`, and serving it from the blob overshoots that budget
> by 23×, every time. So: **local text content is stored in ordered, addressable units whose identifiers sort in
> reading order, and it is fetched by naming the span wanted.** Selection is a STORE operation — a range query over
> record ids, which FountainStore's declared API already serves — never a client-side slice of something larger.
> The units are the source; a whole-work rendering is a projection assembled on demand, never a second stored copy
> that can drift. The operation is declared once in the IDL and projected onto an OpenAPI route and a backplane
> topic by generation (ch.49), so no hand-rolled reader can quietly fetch more than it was commanded to select.

## Purpose — the failure this exists to end

Measured 2026-08-07, in the writer's own flagship store:

```
corpus reframe-ulysses
  screenplay:reframe-ulysses:source   →  text: 1,519,413 chars, 32,694 lines   (ONE record)
      line     1  Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of
      line 20,051  _(The Mabbot street entrance of nighttown, before which stretches an
```

The store is correct and the boundaries are correct: Circe genuinely begins at line 20,051 and ends at 25,573.
What is wrong is the **shape**. There is exactly one addressable thing — the book — so "open Circe" cannot be
expressed as a fetch. It can only be expressed as *fetch everything, then look at part of it*.

Everything the writer has been complaining about follows from that one fact:

- **Choosing a chapter opens the work at its beginning.** The reader is handed 32,694 lines; the chapter is a
  selection drawn over them. Three separate fixes to the library rail — showing chapters before the work is open,
  carrying the request through the switch, naming the work in the request — each made the *selection* correct and
  none of them changed what was *opened*, because the opening was never the rail's to decide.
- **The declared budget is unenforceable.** `screenplay/lines.get` promises a response inside 65,536 bytes. The
  only way to answer it today is to read 1,519,413 bytes and cut. The budget is not exceeded by accident; it is
  exceeded structurally, on every read, and nothing reports it.
- **Every reader must re-derive the structure.** Chapters are recovered by scanning the whole text for `[ N ]`
  markers — 233k characters re-measured per page during a read (measured: ~16s each) — because the store cannot be
  asked "what are the units?" It can only be asked for the blob.
- **Four hand-rolled corpus readers exist** (ch.49: `ReframeCorpusAPI`, `tools/corpus-api`, `tools/ovid-local-api`,
  `tools/ulysses-local-api`), none referencing the envelope, a QoS class, a capability or a budget. They exist
  *because* the store's shape does not answer the question, so each caller invented its own answer.

FountainStore is not the limitation. Its declared API (`docs/openapi-fountainstore.yaml`) already offers what is
needed: `GET /collections/{collection}/records/{id}` for a record, and `POST /collections/{collection}/query` for
**byId, index, and prefix/range scans** with `nextPageToken` paging. A range scan over ordered identifiers is
exactly "point at this span and nothing else." Reframe simply never stored text in a shape that scan can address.

## The rules

1. **Local text content is stored in ORDERED, ADDRESSABLE UNITS.** A work is never one record. The unit is the
   smallest span the writer navigates to — a chapter at minimum, and blocks within a chapter where the chapter is
   long enough that a chapter fetch would exceed the declared payload budget.

2. **Identifiers sort in reading order.** Numbers are zero-padded so lexical order is reading order
   (`…:unit:00015:0004`), because the store's range scan orders by identifier. An identifier scheme that sorts
   `10` before `2` is a defect, not a formatting preference.

3. **The units ADDRESS the source; they never hold a second copy of it.** A unit is a range — see §How this layers
   with chapters 13 and 29, which is binding on this rule. Two stored representations of one text can disagree,
   and the one nobody reads is the one that rots — the same category error as a `sourceVersion`. Partitioning is
   not materialisation: no derived content — no beats, no atoms, no annotations — may enter a unit either.

4. **Every fetch NAMES THE SPAN IT WANTS.** A client asks for a corpus, a document and a range. It does not ask
   for a work and then narrow. A reader that fetches more than it was commanded to select is defective even when
   the result it displays is correct — the overshoot is the defect.

5. **Selection is a store operation.** The span is resolved by a range query over unit identifiers. Slicing a
   larger payload in the client is forbidden: it moves a data-store responsibility into every caller, which is how
   four incompatible corpus readers came to exist.

6. **The declared payload budget is binding.** `maxPayloadBytes` is a promise to the caller. A fetch whose answer
   would exceed it MUST page — the store's `nextPageToken` is the mechanism — and MUST NOT answer with an
   oversized body. A read that cannot be served within budget is a paging decision, never a silent overshoot.

7. **The operation is declared once and projected, never hand-rolled.** `schema/idl.yaml` is the definition;
   the OpenAPI route and the backplane topic are generated from it (ch.49). Adding a new way to fetch text by
   writing an HTTP handler is forbidden. When a reader needs something the IDL does not declare, the IDL changes
   first.

8. **Each unit carries its own line span, and the work carries its hash.** A unit records the `startLine` and
   `endLine` it occupies in the work, so any span a reading claims can be verified against the source rather than
   trusted. The whole-work content hash remains the work's identity for provenance — an identity artifact, never
   the read path.

9. **Structure is asked for, not scanned for.** "What are this work's units?" is a query, answered by the store
   from stored identifiers and titles. No caller may recover chapter structure by scanning the text for markers.
   Re-deriving structure that the store holds is the re-derivation ch.42 forbids, and it is what costs ~16s per
   page today.

10. **Selection has an authority, and it is the store.** Where a typographic boundary exists it is recorded at
    import, once, by the importer that can see it. Where it does not exist — an unbroken stream with no paragraph
    or sentence boundaries — the store records that fact (`offersBoundaries: false`) rather than inventing a grid,
    and any mechanical cut made downstream is a recorded repair debt.

## How this layers with chapters 13 and 29 — the units are RANGES, not copies

This chapter was drafted as though the store were where text lives, and that was wrong twice over. Recorded here
rather than quietly corrected, because what was missing is the evidence that the draft was written on top of a
breach instead of noticing it.

[Chapter 13](13-storage-and-performance.md) already rules that the authored document is a **plain-text bundle
folder** — `source.fountain`, `chapters.json`, `beats.json` — that "the bundle folders are authoritative", and
that "the document layer is never stored as store documents". [Chapter 29](29-natural-language-measures-storify-interprets.md)
already rules that everything measured about the source is held "as ranges against the immutable source —
**offsets, never copies**".

Measured 2026-08-07: the source is a single STORE DOCUMENT (`screenplay:reframe-ulysses:source`), so chapter 13
was already violated before this chapter existed, and the first draft of this chapter proposed to deepen the
breach by splitting that document into many more.

The three chapters do not actually disagree once the layers are named:

11. **The authoritative source is the bundle folder** (ch.13). One file, one immutable text, one content hash.
    Partitioning never produces a second copy of the writer's words.
12. **A unit is a RANGE, not a payload** (ch.29). The unit index records `index`, `startLine`, `endLine`, byte
    offset and length, a title where the work names one, and whether the cut was mechanical — and no text. It is a
    **derived, rebuildable index**, exactly as `library-manifest.json` is derived over the folders (ch.13): on any
    disagreement the source wins, and the index is regenerated by scanning it.
13. **The pointed fetch reads only the bytes it names** (this chapter). Resolve the span against the index, read
    those byte ranges from the authoritative source, return exactly the requested lines, and report the bytes that
    actually crossed the boundary so the budget is proven rather than assumed.

So "the units are the source" means the units are how the source is ADDRESSED, never a second place it is kept.
A unit record containing text is a defect under ch.29 even when every other rule here is satisfied.

## What this forbids, stated plainly

- Storing a work as a single `text` field and calling the store a data store.
- Opening a work in order to reach a chapter.
- Reading a whole document to answer a request for part of it, in the app, in a tool, or in a test.
- Any HTTP route serving text that was not generated from the IDL.
- Recovering chapter boundaries by scanning text that the store could have named.

## Acceptance

A change lands under this chapter only with all five:

1. **A range fetch returns only the span.** Ask for Circe; measure the bytes that crossed the boundary. They must
   be Circe's, within the declared budget, and the response must name the span it is answering.
2. **The whole-work read path is gone.** No caller fetches the work to display a chapter. Proven by reading the
   callers, not by the screen looking right.
3. **The index resolves back to the whole.** The unit ranges, read in identifier order from the authoritative
   source, reproduce that source's content hash exactly, and the index records the hash it was built against. If
   they disagree the index is stale and is rebuilt by scanning — the source wins, never the index.
4. **No unit record contains text.** Checked, not assumed: a unit carrying a payload is a ch.29 defect even when
   every other rule here is satisfied.
5. **The route was generated.** The OpenAPI document and the backplane topic both trace to `schema/idl.yaml`, and
   regeneration produces no diff.

## Governing sentence

Text is stored in ordered addressable units and fetched by naming the span wanted, so that a client which is
commanded to select a chapter fetches that chapter and nothing else.
