# One Retrieval, Two Directions

> Chapter summary: [ch.32](32-referenced-knowledge.md) governs a source coming IN, [ch.40](40-a-citation-is-a-promise-someone-can-check.md)
> a claim going OUT. Built separately, they grew near-identical shapes — a work, a locator, a quotation, a receipt
> — and three different receipt types for the same act. The visible consequence is a writer being asked to retype
> a source Reframe has *already fetched, quoted and receipted*, and a reader having no way to tell which of the
> two systems is authoritative. This chapter rules that **there is one retrieval, recorded once, and two
> directions of use.** A retrieval receipt is a fact about what the app fetched; it does not know which direction
> it will be used in. An accepted reference is therefore a citation candidate that already carries its check, and
> the writer's act is to decide the claim it supports — never to re-key the evidence.

## Purpose — the failure this exists to end

**The same fetch, recorded three times, in three shapes, with no path between them.**

Reframe currently holds three receipt types for one act — the app went and got something, and here is what came
back:

| type | records | lives in |
| --- | --- | --- |
| `GazetteerRetrieval` ([ch.32](32-referenced-knowledge.md)) | why the app believes a world fact | the Gazetteer |
| `ReferenceRetrievalReceipt` ([ch.34](34-a-question-that-leaves-the-work.md)) | a question that left the work and what came back | the reference ledger |
| `CitationCheck` ([ch.40](40-a-citation-is-a-promise-someone-can-check.md)) | the source was fetched and the quotation found in it | the work's citations |

And two near-identical carriers: `GazetteerCitation` (work · locator · url · quotation · retrieval) and
`OutgoingCitation` (claim · claimAddress · work · quotation · verification). Both say: *here is a source, here are
its own words, here is proof someone actually looked.*

Three properties of this decide the chapter:

1. **The duplication is invisible to the writer and expensive to them.** Driven on Romeo and Juliet, recording a
   citation meant typing a URL and pasting a quotation by hand — for a class of source the app already knows how
   to fetch, quote and receipt. The work was done and then thrown away.
2. **Authority is genuinely unclear from the outside.** Two things named "citation" with overlapping fields, and
   a third (`CopilotCitationLink`, a wire between a beat and a sentence) sharing the word for something that is
   not a source at all. A reader of this repository cannot tell which is the record.
3. **It will get worse under its own rules, not better.** Each chapter correctly forbade the others' shortcuts —
   ch.32 forbids recalled sources, ch.40 forbids asserted verification — so each grew its own honest machinery.
   Nothing in the existing doctrine says they are the same act.

## The principle — a retrieval does not know what it is for

When Reframe fetches a source and finds words in it, that event is a fact about the world: *at this moment, this
URL returned this text, and this quotation was at this offset.* It is true regardless of whether the app is about
to believe something with it, or the writer is about to cite it.

Direction is a property of **use**, not of retrieval:

- **Incoming** — the app uses the retrieval to justify what it believes about the world. Governed by
  [ch.32](32-referenced-knowledge.md): retrieved, never recalled; the writer judges the inference.
- **Outgoing** — the work uses the retrieval to support a claim a reader may follow. Governed by
  [ch.40](40-a-citation-is-a-promise-someone-can-check.md): checked, or visibly not checked.

One record, two readings of it. The obligations differ and both remain in force; what may not differ is the
evidence, because it is the same evidence.

## What follows: an accepted reference is a citation candidate

If a reference has been retrieved, quoted and receipted for the incoming lane, then everything
[ch.40](40-a-citation-is-a-promise-someone-can-check.md) requires of a *checked* citation has already happened —
the source was fetched, the quotation is the source's own words, and a receipt records it. Making the writer
retype it is not caution; it is discarding evidence and asking them to reproduce it less reliably.

So the writer's act at the citation boundary is **to choose the claim it supports** — the one judgement that is
irreducibly theirs ([ch.32](32-referenced-knowledge.md) rule 7). The evidence travels; the judgement does not.

This does not weaken ch.40 rule 2. Verification remains an act, and the act is the one already performed and
receipted. What is forbidden is a citation reaching `checked` with **no** receipt — not a citation reaching it
with a receipt written by the reference lane.

## Naming, because the confusion is partly ours

"Citation" currently names three different things, one of which is not a source. A wire between a beat the writer
picked up and the sentence they wrote about it is a *link* on a screen; calling it a citation costs this
repository the word it needs for the thing a reader can follow. The wire keeps its behaviour and loses the name.

## What this does not license

- **Not merging the ledgers.** The Gazetteer answers "why does the app believe this about the world"; the work's
  citations answer "what is this sentence standing on". Different questions, different lifetimes, different
  owners. They share evidence, not storage.
- **Not automatic citation.** A retrieved reference becoming *available* as a citation is not it becoming one. No
  claim acquires a source without the writer attaching it to that claim.
- **Not a weaker receipt.** Unifying the three types means the strictest of them wins: a receipt must name where
  the text came from and what was found in it, or it is not evidence
  ([ch.40](40-a-citation-is-a-promise-someone-can-check.md) rule 2).
- **Not retiring ch.32 or ch.40.** Both stand. This chapter governs only what they share.
- **Not a migration mandate for stored records.** Existing Gazetteer and citation documents remain readable; the
  unification is of the type, and old records are read forward, never silently rewritten
  ([ch.04](04-target-architecture.md): the canonical source remains immutable under analysis).

## Rules

1. **One retrieval receipt type** records the act of fetching a source and locating text in it: when, from where,
   what was sought, what was found, and how much was read. The three current types converge on it.
2. **A retrieval receipt is directionless.** It records what happened, never what it will be used for.
3. **The incoming and outgoing obligations both stand** ([ch.32](32-referenced-knowledge.md),
   [ch.40](40-a-citation-is-a-promise-someone-can-check.md)); this chapter unifies their evidence, not their duties.
4. **An accepted reference is offered as a citation candidate** carrying its existing receipt. The writer supplies
   the claim; the app never supplies it ([ch.32](32-referenced-knowledge.md) rule 7).
5. **A citation created from an accepted reference is checked from the first moment**, because the check already
   happened and is receipted. A citation with no receipt is never checked, whatever created it.
6. **No source may be re-keyed by hand when the app already holds its receipt.** Manual entry remains available
   for a source the app has never fetched.
7. **"Citation" names a source a reader can follow.** A wire between a beat and a sentence is a link and is named
   as one.
8. **Every citation keeps its address in both directions** ([ch.36](36-every-gap-keeps-its-address.md)): claim ↔
   receipt ↔ source, and from the uncertainty score to all three.
9. **Re-checking is always available and always recorded.** A receipt is evidence that the source said this
   *then*; the web is not immutable, and a re-check writes a new receipt rather than editing the old one.
10. **A withdrawn or contradicted citation keeps its receipt** ([ch.40](40-a-citation-is-a-promise-someone-can-check.md)
    rule 7) — the evidence of what was actually fetched is what makes the withdrawal auditable.

## Acceptance

The doctrine is met when:

1. One receipt type is used by the Gazetteer, the reference ledger and the work's citations, and no second type
   records the same act.
2. A writer can turn an accepted reference into a citation on a claim without typing the source, the identifier
   or the quotation.
3. A citation so created reports `checked` and names the receipt that checked it — the same receipt the reference
   lane recorded.
4. A citation with no receipt cannot report `checked` by any path, including decoding a hand-edited document
   ([ch.40](40-a-citation-is-a-promise-someone-can-check.md) rule 2).
5. Following a citation reaches its receipt, and following the receipt reaches the fetched source; following the
   uncertainty note reaches the claim.
6. No type or identifier in the codebase uses "citation" for an on-screen wire.
7. Existing stored Gazetteer and citation records are read successfully after the unification.

## Governing sentence

Reframe shall record a retrieval once and use it in either direction, so that evidence the app has already
gathered is never discarded, never re-keyed by the writer, and never in two shapes that disagree about what was
actually fetched.
