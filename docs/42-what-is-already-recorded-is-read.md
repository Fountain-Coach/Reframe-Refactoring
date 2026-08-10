# What Is Already Recorded Is Read, Never Re-Derived

> Chapter summary: On 2026-08-02 an agent with forty-one chapters of doctrine, a governed drive procedure, and a
> store holding every fact it needed produced a batch in which **every single defect was already governed**. It
> encoded records into chat messages that the store already held; it rebuilt in memory a capability history the
> store already persisted; it put a parser in a render path; it delivered accumulated status into the
> conversation, which [ch.16](16-the-timeline-is-the-machine-room.md) forbids in as many words; it added a cache
> to hide the round-trip; and it attributed the resulting hang by a bisect whose reproduction never exercised the
> reported symptom. Seven successive fixes improved the artifact and none reached the mechanism. The unifying
> failure is not ignorance — it is **re-derivation**: rebuilding from scratch what the store, the chapters, or the
> evidence procedure had already recorded. So: **what is already recorded is read, never re-derived** — records
> are referenced rather than copied, doctrine is read before the work rather than cited after it, and evidence is
> taken from the authority that owns it.

## Purpose — the failure this exists to end

**Everything needed already existed, in writing, and was rebuilt badly instead.**

The batch is on the record. Its defects, and where each was already governed:

| what was built | what already held it |
| --- | --- |
| `[OutgoingCitation]` encoded into a chat message as a `[[reframe:citations …]]` block, then parsed back out by the renderer | the store: `work:citations:<corpus>` |
| a capability history rebuilt as a `@Published` array | the store: `copilot:capability:<corpus>:<id>`, required by [ch.37](37-copilot-capability-governance.md) |
| accumulated act status delivered into the transcript | [ch.16](16-the-timeline-is-the-machine-room.md) rule 3 — *"a log bubbling into it is a category error"* |
| an in-memory layout cache to absorb the cost | [ch.13](13-storage-and-performance.md) — caches are permitted, but reconciled by refresh and never the sole authority |
| hand-rolled `11.5`/`10.5` pt fonts and mirrored RGB tints | [ch.19](19-apple-human-interface-guidelines.md) — system text styles, semantic system colours |
| a 17-file sweep with no plan | [ch.07](07-agent-operating-guide.md) §Planning discipline |
| "confirmed" from a single confounded run | [ch.08](08-validation-and-acceptance.md) — *"repeat consequential behaviour three times"*; *"never present an unrun live path as measured"* |
| a hang diagnosed from `count windows: 0` | [ch.08](08-validation-and-acceptance.md) — separate evidence authorities; the live-drive runbook names the zero-windows trap |

Three properties of this decide the chapter:

1. **No rule was missing.** Every item above had an owner before the work started. The reading index
   ([ch.01](01-reading-index.md)) exists precisely so the relevant chapter is cheap to find.
2. **Re-derivation looked like progress.** Each rebuilt thing compiled, rendered, and passed tests. Nothing
   announced that it was a second copy of something authoritative.
3. **The real defect was never touched.** The writer found it in one attempt — the beat filmstrip stalls on a
   main-thread fetch while scrolling — a surface that blocks while fetching, which
   [ch.12](12-animating-truth.md) already forbids. The agent spent a day on a symptom of its own measurement.

## The principle — reference the record, read the rule, take the evidence

Reframe already keeps three kinds of record: **state** in FountainStore, **doctrine** in these chapters, and
**evidence** under the authorities [ch.08](08-validation-and-acceptance.md) assigns. Each has exactly one home.
Re-deriving any of them produces a second copy that can disagree with the first, and the disagreement is silent.

So the discipline is the same in all three registers:

- **State**: a surface *references* a record and reads it back. It does not carry it, copy it, or encode it into
  something else on the way to the screen.
- **Doctrine**: the chapter is read *before* the work. A chapter cited after the fact is an epitaph.
- **Evidence**: the accessibility tree owns semantic UI state, the window capture owns layout and wording,
  FountainStore owns behaviour, and logs own nothing. A reading from the wrong authority is not weak evidence, it
  is a different claim.

## A turn carries references, not records

A conversation turn is what was *said*: a role, a moment, and a sentence a person can read. When the turn concerns
a record, it names the record; the surface reads that record back.

Encoding a record into the turn and parsing it out again is a round trip whose halves cancel and whose cost does
not. Measured in this batch: three `FountainExtensionParser` passes plus a full Fountain parse, per message, per
layout evaluation, from inside a view body, over a kilobyte of the app's own JSON.

This extends [ch.13](13-storage-and-performance.md) clause 8, which already places chat in the store as working
state, and it is the same instinct as [ch.36](36-every-gap-keeps-its-address.md): the address is what travels.

## Parsing is an ingest concern

[ch.27](27-parse-before-you-ask.md) governs *parse rather than ask a model*. It does not govern *where* parsing
happens, and the gap was load-bearing.

A parser reads text of unknown structure that someone else wrote — an imported manuscript, a pasted document, a
fetched source. That is an ingest act, performed once, at the boundary. A render path parses nothing: it receives
typed values and draws them. A parser called from a view body is a category error regardless of how fast it is,
because its cost is multiplied by every layout pass and its input is text the app itself produced.

## Which grammar owns which text

Three grammars meet in this application and they are not variants of each other:

- **Fountain** — the manuscript, imported documents, and explicitly marked screenplay regions. Owned by
  FountainEditorKit.
- **Prose markup** — what the copilot writes in conversation.
- **Typed values** — what the app computes: citations, capabilities, ledgers, threads. Not text at all.

**Fountain is not a subset of Markdown**, and treating it as one silently picks a loser: `>` is a blockquote in
one and a transition in the other, `===` a heading and a page break, `_x_` italic and underline, and an uppercase
line is a paragraph in one and a character cue in the other. This repository already runs two parsers that read
`[[ … ]]` differently on purpose — `ReframeCore.FountainParser` as a screenplay *note*, `FountainExtensionParser`
as a *typed block*. That overlap is tolerable only while it is stated.

The grammar of a region is therefore **declared by whatever emitted it**, never detected from its contents.
Sniffing — running a screenplay parser over a chat message to guess whether it "looks like" dialogue — is the same
error as keyword routing, and it is retired for the same reason.

## An instructed act is answered; machinery is not narrated

[ch.16](16-the-timeline-is-the-machine-room.md) rule 3 states that no run report, transcript of windows, or
accumulated status is delivered into the conversation. This chapter does not weaken it; it draws the line the
batch discovered:

- **An act the writer instructed is answered in the conversation** — once, in a sentence saying what happened and
  what changed. That is not a log; it is the reply to their instruction.
- **Machinery the writer did not ask about is not narrated at all.** Progress is structure
  ([ch.12](12-animating-truth.md)), and a diagnostic drives behaviour without becoming a surface.
- **The history of acts is not resident in the lane.** It is durable in the store already
  ([ch.37](37-copilot-capability-governance.md)) and is *retrieved on request*, like any other record.

Nothing is lost by this and nothing accumulates: the record is permanent, the conversation stays a conversation.

## A kit we own is changed upstream, with a version

Three of the five Fountain-Coach kits this application consumes are pinned to raw revisions with no recorded
reason, so a fix landing upstream is invisible here until someone re-pins by hand. The organisation's compliance
plans also state plainly that new dependencies are not to be introduced,[^fcisplan] which means a capability we
lack is built in a kit we own rather than imported.

The practice already exists and is recorded — the generic uncertainty seam was released upstream in
`UncertaintyScoreKit v0.8.3`, consumed here by version, and *"the kit receives none of those domain types"*.[^kitprecedent]
This chapter writes that down as the rule rather than leaving it as one worked example.

The resolved graph is part of that record. A SwiftPM cache can preserve a syntactically valid executable after the
consumer source or a transitive kit has moved. Therefore a current-source claim is not established until the exact
executable, committed lockfile revisions, upstream object existence, and negative retired-surface check have all been
read. The repository runbook `Scripts/verify-dependency-coherence` is the operational projection of FCIS-KIT-10A;
`Scripts/verify-reader-ui-surface.sh` is its reader-surface negative gate.

## What this does not license

- **Not a ban on caches.** [ch.13](13-storage-and-performance.md) requires one for the library. What is forbidden
  is a cache that reconciles with nothing, or one standing in for a round trip that should not exist.
- **Not a ban on parsing.** It is a ban on parsing in a render path, and on parsing text the app itself produced.
- **Not silence about work in progress.** [ch.12](12-animating-truth.md) governs that, and
  [ch.16](16-the-timeline-is-the-machine-room.md) rule 8 keeps failure loud.
- **Not a licence to skip a chapter because this one summarises it.** The table in *Purpose* is an index of what
  was broken, not a replacement for the chapters that own each rule.
- **Not a new process for its own sake.** Everything in the method rules below already existed in
  [ch.07](07-agent-operating-guide.md) and [ch.08](08-validation-and-acceptance.md); they are restated here only
  because the batch proved that existing is not the same as being read.

## Rules

1. **A turn carries a reference, never a record.** Role, moment, sentence, and the identity of any record it
   concerns. The surface reads that record back.
2. **The app never parses text it produced.** A round trip through a serialization the app wrote is a defect, not
   an optimisation target.
3. **Parsing happens at ingest, never in a render path.** A view receives typed values.
4. **A region's grammar is declared by its emitter, never detected from its contents.**
5. **Fountain, prose markup, and typed values are three grammars, not three dialects.** Where their sigils
   collide, the collision is documented at the boundary that owns it.
6. **A capability we lack is built in a kit we own and released upstream with a version**; consumers take it by
   semver. A revision pin is a temporary state that must record its reason and its exit. The executable actually
   driven must also be checked against the resolved graph; a cache is never its provenance.
7. **An instructed act is answered once in the conversation; accumulated status is not.** Act history is durable
   in the store and retrieved on request.
8. **Derived surfaces invalidate from the records they read**, never from a counter a view increments.
9. **Read the owning chapter before the work.** [ch.01](01-reading-index.md) resolves a task to its chapter; a
   chapter cited only in the commit message was not read.
10. **Evidence is taken from the authority that owns it** ([ch.08](08-validation-and-acceptance.md)), a
    reproduction must exercise the reported symptom before anything is attributed to a cause, and consequential
    behaviour is repeated three times before it is called measured.
11. **After the second fix to the same symptom, instrument rather than fix.** A third attempt at the artifact is
    evidence that the mechanism has not been found.

## Acceptance

The doctrine is met when:

1. No chat message contains a serialized application record, and no renderer decodes one.
2. No parser is invoked from a view body; the parsers appear only on ingest paths.
3. Every surface that presents a record re-reads it when that record changes, and survives relaunch unchanged.
4. Capability history is readable from the store on request and is not resident in the transcript.
5. No text region's grammar is inferred from its contents anywhere in the codebase.
6. Every dependency on an owned kit is a semver range, or a revision pin carrying its reason and its exit; the exact
   executable used for live/UI/publication evidence passes dependency-coherence and negative retired-surface gates.
7. A phase closes with [ch.07](07-agent-operating-guide.md)'s review questions answered from evidence, and a
   live-acceptance record that names its authorities and its three repetitions.

## Governing sentence

Reframe shall read what is already recorded — the state in its store, the doctrine in these chapters, the evidence
under its own authorities — and shall never rebuild any of them from scratch, so that no second copy of the truth
can exist to disagree with the first.

## Sources

[^fcisplan]: `FCIS_COMPLIANCE_PLAN.md`, this repository and `Fountain-Coach/FountainEditorKit` — *"Keep this
    repository compliant with FCIS RFC 0001 … with minimal changes and no new dependencies."* The organisation's
    standards themselves (FCIS-AX 1.0, FCIS-VRT 1.0, FCIS-AIC-Preflight 1.2) are published in
    `Fountain-Coach/.github/docs/` and cover accessibility, visual regression and Apple Intelligence preflight;
    none covers dependency versioning, which is the gap rule 6 closes.

[^kitprecedent]: `FCIS_COMPLIANCE_PLAN.md`, this repository — the generic address/rack/map/inspector seam
    *"released upstream in `UncertaintyScoreKit v0.8.3`"*, consumed here by version, with the kit receiving none
    of Reframe's domain types. Verified against the file and against `Package.swift`, which consumes the kit by
    semver range while three sibling kits carry undocumented revision pins.
