# Reframe Refactoring

The Fountain Coach publication and FCIS-governance home for the design and architectural doctrine of **Reframe** — the on-device screenwriting studio that reads a manuscript into a story structure and lets a writer compose from it.

This repository is a **living guide**, not a one-time spec. It is written to be read by both **humans** (maintainers, reviewers, designers) and **agents** (`.claude`, `.codex`): short, stable, numbered chapters, each stating enforceable doctrine for one part of the work, so a reader — of either kind — loads only what the task needs.

Start with the [abstract](docs/00-abstract.md), then use the [reading index](docs/01-reading-index.md) to pick a route.

## Genesis, and how the guide grew

The guide began (2026-07-19) as **one architectural transition**: remove semantic indexing from Reframe's production path, make confirmed **Grounding** the direct downstream policy contract, and make **Storify Source Auto** the sole structural reader of the canonical source. That founding decision still holds and is stated in chapters 00–11. Its governing sentence:

> Reframe shall read the source structurally once: Grounding determines the writer's declared intent, Storify reads the source under that intent, Cut Script owns authored output, and Continuity audits the result; no semantic indexing stage or index-derived authority remains in the final production path.

Implementing that transition surfaced deeper truths it *implied* but had not yet named — and the guide grew to state them, chapter by chapter, as they were earned in the code:

- **Grounding is a given** (11) — a settled manifesto edited as prose, never a gate.
- **Animating truth** (12) — never sign a wait with a spinner; the wait itself is the show.
- **Storage and performance** (13) — a plain-text document layer and a MIDI 2.0 musical layer; reads are fast by *architecture*, not by encoding.
- **The beat and its arrangements** (14) — one beat, three arrangements, and the *take* it fires.
- **The situated Copilot** (15) — one Copilot, differently placed, offering nothing whose object the surface does not show.
- **The timeline is the machine room** (16) — one machinery, one surface; no second-account diagnostics view.
- **The Score** (17) — the consolidated **performance space**: the ONE working surface, of which the timeline and the Cut are *lenses*; the Cut composes a **take**, and once fired that take is the root every projection reads ("has one cut").
- **The Stage Presents the Act** (18) — the enforceable **visual floor**: a surface presents the writer's act, large and legible (the *glasses test*), not a dense console — and UI is verified by *looking*, of which a machine-readable accessibility tree is the necessary but never sufficient half.
- **Apple's Human Interface Guidelines** (19) — the platform **baseline** beneath 12/14/17/18, not an alternative: it supplies the numbers our visual floor was guessing (system text styles — macOS Body = 13 pt; contrast 4.5:1 text / 3:1 controls / aim 7:1; 44 pt hit targets; semantic colours; the 8 pt grid; Reduce Motion) and records the gaps we still owe.

So the arc is legible: from **subtracting a stage** (remove indexing) → to naming the **one surface** that remains (the Score, a stage of participants grounded to a beat-spine) → to how that surface must **read to a human** (legibility over density) → to the **platform baseline** that legibility rests on (Apple's HIG). Reframe's working surface is now governed here as one architectural *and* design doctrine.

The guide is authoritative about the *intended* design. It never claims the work is already done: until a chapter's doctrine is implemented and validated, **live code, live FountainStore state, the MIDI backplane contract, and the generated manifest remain the truth about current behavior.** The precedence rules in the root and app-scoped `AGENTS.md` always apply.

## The chapters

**Foundations — the Grounding-first transition (00–11)**

- [Abstract](docs/00-abstract.md) · the decision and completion condition, compact
- [Reading index](docs/01-reading-index.md) · role-based routes, chapter catalogue, vocabulary
- [Development history](docs/02-development-history.md) · the eras, retained lessons, superseded assumptions
- [Current state and problem](docs/03-current-state-and-problem.md) · where index authority still leaks
- [Target architecture](docs/04-target-architecture.md) · stage ownership, data flow, invariants
- [Grounding contract](docs/05-grounding-contract.md) · the persisted profile, identity, invalidation
- [Refactoring program](docs/06-refactoring-program.md) · ordered phases, the deletion gate, exit criteria
- [Agent operating guide](docs/07-agent-operating-guide.md) · precedence, planning, evidence for `.claude`/`.codex`
- [Validation and acceptance](docs/08-validation-and-acceptance.md) · required tests and negative evidence
- [Compatibility and evolution](docs/09-compatibility-and-future-evolution.md) · legacy stores, rollback, extension rules
- [Copilot implementation extension](docs/10-copilot-implementation-extension.md) · perception, retrieval, action parity
- [Grounding as a given](docs/11-grounding-as-a-given.md) · the canonical manifesto, auto-confirmed, edited as prose

**The working surface and its doctrine (12–19)**

- [Animating truth](docs/12-animating-truth.md) · perceived performance; foreshadow the unknown honestly
- [Storage and performance](docs/13-storage-and-performance.md) · document + musical layers; fast by architecture
- [The beat and its arrangements](docs/14-the-beat-and-its-arrangements.md) · one beat, three arrangements, the take
- [The situated Copilot](docs/15-the-situated-copilot.md) · one Copilot, differently placed
- [The timeline is the machine room](docs/16-the-timeline-is-the-machine-room.md) · one machinery, one surface
- [The Score](docs/17-the-score.md) · the ONE surface; lenses; the Cut composes a take; "has one cut"
- [The Stage Presents the Act](docs/18-the-stage-presents-the-act.md) · legibility over density; verify by looking
- [Apple's Human Interface Guidelines](docs/19-apple-human-interface-guidelines.md) · the platform baseline — text styles, contrast, hit targets, Reduce Motion

**The continuous account**

- [App-flow record](docs/reframe-app-flow-governance.md) · the end-to-end prose narrative these chapters refine

## Reading paths

Pick the row for your task; read those chapters, then retrieve live code and state for detail. Do not load the whole directory.

| If you are… | Read |
| --- | --- |
| Reviewing the architecture (human) | 00 → 02 → 04 → 17 (the arc, then where it now stands) |
| Implementing Grounding | 04 → 05 → 06 (phases 1–3) → 08 |
| Implementing Storify (the read) | 03 → 05 → 06 (phases 2–4) → 08 |
| Working on the Score / composing a cut | 17 → 14 → 12, then 18 for how it must look |
| Doing UI / visual / design work | 18 (the floor) → 19 (the platform baseline) → 12 → 17 → the specific surface's chapter |
| Placing or changing the Copilot | 10 → 15 (and its discovery procedure) → 08 |
| Deleting the index | all of 06 (esp. the deletion gate) → 07 → 08 |
| Reviewing code | 03 → the relevant target contract → 06 exit criteria → 18 (does the writer see it?) |
| An agent picking up any task | 07 first (precedence, evidence, planning), then the row above |

**For agents specifically:** authority precedence and evidence discipline live in [chapter 07](docs/07-agent-operating-guide.md). The guide is doctrine, not runtime truth — verify current behavior against live code and store. UI claims require *looking* at the rendered view (chapter 18), not only an accessibility-tree query.

## Source relationship

This guide is maintained as **one document set in two places**: here (the publication and FCIS-governance home) and beside the Reframe implementation in [`Fountain-Coach/midi2-gpu-fabric`](https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor). A documentation change is maintained only when the two copies agree; [SOURCE.md](SOURCE.md) records provenance and the synchronization contract.

## FCIS compliance

This repository follows FCIS RFC 0001 layering:

- `AGENTS.md` — scope, invariants, routing.
- `PLANS.md` — intent for multi-step or high-risk changes.
- `.codex/skills/docs-sync/SKILL.md` — the synchronization procedure.
- MCP is optional; correctness and synchronization do not depend on it.

See [FCIS_AUDIT.md](FCIS_AUDIT.md) and [FCIS_COMPLIANCE_PLAN.md](FCIS_COMPLIANCE_PLAN.md) for evidence and the maintenance checklist.
