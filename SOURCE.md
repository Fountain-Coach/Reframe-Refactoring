# Source and Synchronization Contract

## Current synchronized change

- Change: **Chapter 51 — One Decision Decides the Lane.**
- Measured 2026-08-07 on a single page of one chapter: `[LANES] semantic -> codex`, `[WINDOW] budget 30000
  tokens`, `[READ-LANE] reading on openai`, and the call landing on Apple Foundation Models, which refused
  **25,025 tokens into a 4,096-token window**. Four subsystems, four answers, one act — and none of them lying.
- The same disagreement produced the rest of that day: credential PRESENCE read as permission, so a key that
  existed but could not be unlocked let the read fall silently to the on-device lane while three surfaces still
  said cloud; the Copilot's opening sentence constructed a paid client in order to NAME a lane, putting a
  password dialog in front of the manuscript to write a noun; and a per-window TIMEOUT recorded as a size ceiling
  ratcheted the budget 30,000 -> 21,929 -> 14,627, after an earlier turn of the same screw left 2,190 and capped
  every paid call at 261 tokens of manuscript.
- The ruling: a lane is resolved ONCE into a value, and the budget is a PROPERTY of that value — obtaining a
  client and obtaining the window it must fit are the same act, which makes the overflow unrepresentable rather
  than fixed. Gates are ordered and may only narrow; a refusal is a typed value with a reason, never a nil that
  composes into a silent fallback; a credential has four states and the writer's GRANT initialises a cloud lane;
  naming a lane may not read a secret; every surface prints the one recorded decision; a failure teaches only what
  it is evidence of; and the resolver is pure and lives in a kit.
- New acceptance cases: an exhaustive truth table over
  `permitted x credentialState x constructible x health x role`, and the property that a decision's budget belongs
  to its provider — one assertion that fails against the behaviour this chapter replaces.
- Direction: integration -> publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@50ed71d3` (on `main`)
- Publication pull request: recorded below once opened
- Governance first, per ch.07: no implementation accompanies this chapter.
- Synchronized: 2026-08-07

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
