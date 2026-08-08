# Source and Synchronization Contract

## Current synchronized change

- Change: **Chapter 52 — The Pencil Belongs to the Writer.**
- A reader underlining marks FORWARD, IN IGNORANCE: the pencil moves before she can say why, flagging salience
  rather than asserting a conclusion, carrying no caption (and often unreconstructable later, which is normal),
  costing nothing to be wrong about, and layering across readings.
- The mark Reframe began emitting on 2026-08-08 is the exact inverse in every respect — made backward from a
  window the model has already finished, asserting "these words raised this question", captioned by that
  question, and expensive to be wrong about because a machine's mark is read as a finding. It is therefore not an
  underline but a CITATION (ch.40), and the app was one design review away from drawing it as a pencil stroke,
  which would have laundered retrospection as attention.
- The collision this ends: an underline already meant three things here — evidence that a recorded claim cites a
  line (producer removed with the semantic-index runtime; `BaselineViews.evidenceTint` survives with nothing
  mounting the view), read-through progress during a run, and the new anchor — and the CoPilot's own help text
  spent a paragraph warning the writer not to confuse them.
- Measured on a live on-device Circe run, 2026-08-08: 13 of 15 windows anchored; threads run 20608 -> 20815 while
  their anchors are 15 to 86 lines; one thread opens 95 lines into its own passage. So the citation marks a
  beat's HEAD and never its body — marking the body would stripe the chapter three deep and say nothing.
- The ruling: the two marks have different owners and never share a visual language. The machine's citation is
  backward-looking, captioned, answerable and bound to its question's lane. The PENCIL IS THE WRITER'S: her mark
  cites nothing, it says "this matters to me, I do not yet know why" — an instruction with an address (ch.46)
  that the app may notice and ask about in dialogue, but may never interpret, rank, score, or feed to a prompt as
  evidence. Absence stays absent; progress leaves nothing behind.
- New acceptance cases: every drawn citation resolves to a question and back to the same span; unanchored
  questions draw nothing (the Circe run's 2 unanchored windows are the fixture); and the writer's marks and the
  app's marks are distinguishable in a rendered image by someone who is not told which is which — pixel evidence
  in both themes, not a flag.
- Direction: integration -> publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@532922df` (on `main`)
- Publication pull request: `https://github.com/Fountain-Coach/Reframe-Refactoring/pull/21` (merged as `2d12f6f`)
- Governance first, per ch.07: no implementation accompanies this chapter.
- Synchronized: 2026-08-08

## Roles

This repository is the publication and FCIS-governance home of the Reframe Grounding-first refactoring guide.

The integration copy lives beside the application implementation at:

```text
Fountain-Coach/midi2-gpu-fabric
apps/modernization-studio/docs/reframe-grounding-first-refactor/
```

The publication copy lives here under `docs/`. Neither copy is permitted to drift silently. A guide change is maintained only when both repositories contain the same chapter set and content.

## Initial provenance

- Source repository: `Fountain-Coach/midi2-gpu-fabric`
- Source branch: `perf/model-response-cache`
- Source commit: `da22ba0c54e0fff6fb44f66182cecab0dd18759e`
- Source pull request: `https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/8`
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Imported: 2026-07-19

## Maintenance rule

## Previous synchronized changes

Newest first. Every entry below was `Current` when it was written; they are kept as the record of what
crossed between the repositories and under which commits and pull requests.

### 1.

- Change: Chapter 46 amendment, `a lens is a hypothesis about the reader, not a description of the work` — states
  that a first reading's residue has two origins (the work's and the reading's), that a lens names the reader's
  suspected blind spot rather than summarizing the open questions, and adds rules 11–15 (adoptable lens; the
  proposal cites the pattern as evidence; the writer's own lens is verbatim and authoritative; a lens is proved by
  a change in the kind of uncertainty across two readings; a hole is not a lens problem).
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commits: `Fountain-Coach/midi2-gpu-fabric@169e1adf` (amendment),
  `Fountain-Coach/midi2-gpu-fabric@7db89198` (acceptance for rules 11–15 + reading-index entry)
- Integration pull request: `https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/24`
- Publication pull request: `https://github.com/Fountain-Coach/Reframe-Refactoring/pull/10`
- Synchronized: 2026-08-05

### 2.

- Change: Chapter 45, `Copilot Reading Surface and Typography`
- Direction: integration → publication (manual exact transfer; the documented sync helper was absent in this checkout)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/45-copilot-reading-surface-and-typography.md`
- Publication path: `docs/45-copilot-reading-surface-and-typography.md`
- Illustrations: `docs/illustrations/copilot-working-state.png`, `docs/illustrations/copilot-focused-state.png`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@74d84a75`
- Synchronized: 2026-08-03

Changes may begin in either repository, but the pull request that publishes them must name the corresponding commit or pull request in the other repository. The documentation sync skill performs comparison and explicit transfer. Its default action is read-only comparison; transfer requires an explicit direction.

Runtime implementation, tests, generated reasoning manifests, and application-specific plans remain in `midi2-gpu-fabric`. This repository owns the refactoring guide and its FCIS governance, not the Reframe runtime.

- Release-surface chapter: `docs/43-the-released-surface-is-a-named-build.md`, synchronized with the integration guide and added 2026-08-03.
- Publication-boundary chapter: `docs/44-publication-and-source-policy.md`, synchronized with the integration guide;
  it governs the public Book projection, the private runtime boundary, and the org FCIS publication policy.
- Policy PRs: org FCIS `Fountain-Coach/.github#4`, governance `Fountain-Coach/Reframe-Refactoring#7`, runtime
  `Fountain-Coach/midi2-gpu-fabric#21`, and Book `Fountain-Coach/book-of-reframe#9`.

### 3.

- Change: Chapter 46, `Dynamic Grounding: From Default Reading to Writer-Accepted Lens`, plus the reading-index entry
  and synchronized chapters 44/45.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@aeb03ce3`
- Integration pull request: `https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/22`
- Publication pull request: `https://github.com/Fountain-Coach/Reframe-Refactoring/pull/8`
- Synchronized: 2026-08-04

### 4.

- Change: Refactored Chapter 38, `Copilot Capability Audit Skill`
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@633d110c`
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Synchronized: 2026-08-01

### 5.

- Change: Chapter 38 current audit update for the first `pipeline.status` widening slice
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@77c62a45`
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Synchronized: 2026-08-01

### 6.

- Change: Chapter 38, `Copilot Capability Audit Skill`, and the Chapter 37 reading-index entry
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@37231c2e`
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Synchronized: 2026-08-01

### 7.

- Change: chapter 36, `Every Gap Keeps Its Address`
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@cfeaa2c1`
- Integration pull request: `https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/9`
- Publication branch: `codex/ch36-every-gap-keeps-address`
- Synchronized: 2026-07-31

### 8.

- Change: Chapter 47, `Situated, Mixed-Initiative Interaction`, and its Chapter 47 reading-index entry
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@c33615ad`
- Publication commit: `Fountain-Coach/Reframe-Refactoring@688a200`
- Draft publication PR: `https://github.com/Fountain-Coach/Reframe-Refactoring/pull/9`
- Draft integration PR: `https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/23`
- Synchronized: 2026-08-04 (working tree; commits to be recorded reciprocally before publication)
