# Reading Index

> Chapter summary: This index offers role-based reading paths, chapter descriptions, and a vocabulary map so humans and agents can retrieve only the material relevant to the task at hand. It covers both halves of the guide: the founding Grounding-first transition (00–11) and the working-surface doctrine that grew from it — the Score, the beat and its cut, the situated Copilot, and how the surface must read (12–18). See the [root README](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/README.md) for the genesis and full arc.

The suite is intentionally divided into short, stable chapters. Agents should not load the whole directory into every prompt. Select the chapters whose authority is necessary for the current task, then retrieve live code and state for implementation detail. A UI claim is not settled by an accessibility-tree query alone — chapter 18 requires *looking* at the rendered view.

## Reading paths

### Product and architecture review

Read the [abstract](00-abstract.md), [development history](02-development-history.md), and [target architecture](04-target-architecture.md). These chapters explain why the older index-centered design existed, why its lessons remain valuable, and why authority moves to Grounding and Storify now.

### Grounding implementation

Read the [target architecture](04-target-architecture.md), [Grounding contract](05-grounding-contract.md), and phases 1–3 of the [refactoring program](06-refactoring-program.md). Finish with the relevant tests in [validation and acceptance](08-validation-and-acceptance.md).

### Storify implementation

Read the [current-state analysis](03-current-state-and-problem.md), [Grounding contract](05-grounding-contract.md), and phases 2–4 of the [refactoring program](06-refactoring-program.md). The source-authority and no-index acceptance cases in [validation and acceptance](08-validation-and-acceptance.md) are mandatory.

### Readiness, journey, or UI implementation

Read the [target architecture](04-target-architecture.md), phase 4 of the [refactoring program](06-refactoring-program.md), and [compatibility and future evolution](09-compatibility-and-future-evolution.md). These changes are incomplete until generated capabilities and reasoning artifacts agree with the UI.

### Index deletion

Read the entire [refactoring program](06-refactoring-program.md), especially its deletion gate, followed by the [agent operating guide](07-agent-operating-guide.md) and [validation and acceptance](08-validation-and-acceptance.md). Do not begin from a filename search and delete outward; prove replacement consumption first.

### The Score, and composing a cut

Read [the Score](17-the-score.md) (the one working surface; the timeline and Cut as lenses; the Cut composes a *take*; every projection reads it — "has one cut"), then [the beat and its arrangements](14-the-beat-and-its-arrangements.md) (the beat anatomy and the take it fires) and [animating truth](12-animating-truth.md) (how the read is felt). Anything the writer sees or operates is also governed by [the stage presents the act](18-the-stage-presents-the-act.md). The Cut is not a return of the retired patch-graph canvas — it is a lens and a second lane of the one surface.

### Visual, UI, or design work

Read [the stage presents the act](18-the-stage-presents-the-act.md) first — it is the enforceable floor (the act is the star; the glasses test for type and hit targets; progressive disclosure; one act in focus; relationships drawn, not implied; verify by *looking* in light and dark). Then [animating truth](12-animating-truth.md), [the Score](17-the-score.md), and the specific surface's chapter. A machine-readable accessibility tree is the necessary but never sufficient half of accessibility; passing it is not passing legibility.

### Copilot implementation

Read the [target architecture](04-target-architecture.md), [Grounding contract](05-grounding-contract.md), the [Copilot implementation extension](10-copilot-implementation-extension.md), and [the situated Copilot](15-the-situated-copilot.md), then follow chapter 10's mandatory discovery procedure before editing. Work that places the Copilot on a surface, or changes what she says when she arrives, is governed by chapter 15 and must satisfy its acceptance as well. The Copilot must reuse existing application operations and the same authority chain; it is not a second workflow engine. The behavioural, relaunch, and no-index acceptance cases in [validation and acceptance](08-validation-and-acceptance.md) apply.

### Code review

Read [current state and refactoring problem](03-current-state-and-problem.md), the relevant target contract, and the phase exit criteria in the [refactoring program](06-refactoring-program.md). A review should reject dual authority, hidden index reads, numeric context shaping, or readiness claims that are not persisted.

### `.claude` and `.codex`

Read the [agent operating guide](07-agent-operating-guide.md) first, then follow the task-specific path above. The guide explains authority precedence, planning discipline, evidence expectations, and the rule that historical documentation is never operational state.

## Chapter catalogue

| Chapter | Purpose |
| --- | --- |
| [Abstract](00-abstract.md) | Compact statement of the decision and completion condition. |
| [Development history](02-development-history.md) | The architectural eras, retained lessons, and superseded assumptions. |
| [Current state and problem](03-current-state-and-problem.md) | What the runtime does now and where index authority still leaks through. |
| [Target architecture](04-target-architecture.md) | Stage ownership, data flow, authority boundaries, and final invariants. |
| [Grounding contract](05-grounding-contract.md) | The persisted profile, identity rules, prompt relationship, and invalidation semantics. |
| [Refactoring program](06-refactoring-program.md) | Ordered implementation phases, affected seams, deletion gate, and exit criteria. |
| [Agent operating guide](07-agent-operating-guide.md) | Instructions for `.claude`, `.codex`, and human collaborators. |
| [Validation and acceptance](08-validation-and-acceptance.md) | Required unit, integration, store, UI, live-provider, and negative evidence. |
| [Compatibility and evolution](09-compatibility-and-future-evolution.md) | Legacy-store policy, archival behavior, rollback, and rules for future extensions. |
| [Copilot implementation extension](10-copilot-implementation-extension.md) | Extends the refactor to the conversational Copilot: perception, retrieval, action parity, discovery procedure, and acceptance. |
| [Grounding as a given](11-grounding-as-a-given.md) | Refines the Grounding authoring model: a canonical manifesto shipped as the default given, auto-confirmed on import, edited centrally as prose, never model-dissected. |
| [Animating truth](12-animating-truth.md) | Perceived performance: never sign a wait with a spinner. Render the frame and cheap/cached truth instantly; foreshadow the unknown as honest, animated structure whose motion maps to real work. Nothing that is not the manuscript may delay the manuscript; absence may not overwrite a truth already held; a click lands in its destination. |
| [App-flow record](reframe-app-flow-governance.md) | The complete prose account of how the app must flow end to end — the single continuous narrative these numbered chapters refine. |
| [Storage and performance](13-storage-and-performance.md) | Locks the storage layering — document layer = plain-text bundle + single manifest; musical layer = MIDI 2.0 — and the performance doctrine: reads are fast architecturally (cache-first, one manifest, no serial fan-out), not by encoding. |
| [The beat and its arrangements](14-the-beat-and-its-arrangements.md) | One beat, three arrangements: a single widget anatomy whose only differing part is its measure; the take — one firing that renders the document and musical layers as siblings. **Its patch-graph canvas (rules 7–9) is superseded by chapter 17;** the beat anatomy and take are retained. |
| [The situated Copilot](15-the-situated-copilot.md) | One Copilot, differently placed: she perceives the arrangement hosting her and what is wired into the conversation there, opens in words that fit the place, offers nothing whose object the surface does not show, and states an empty situation rather than filling it. |
| [The timeline is the machine room](16-the-timeline-is-the-machine-room.md) | Making beats IS the machinery and the timeline is where it is seen: one machinery, one surface. No machine room, factory gate, engine view, run report, or heartbeat line; diagnostics may drive behaviour but never become a surface; unreachable surface is deleted, not kept. |
| [The Score](17-the-score.md) | The performance space of the work, and the ONE working surface: the timeline and Cut become lenses of it (the patch-graph canvas is retired); a lane is a participant, not a track; the beat/arc is the structural spine every participant is grounded to; protocol state (MIDI 2.0) is composition. Defines the minimum honest Score — grounded spine + one Text participant from the source — with the distributed multi-participant stage named as horizon, not increment. |
| [The Stage Presents the Act](18-the-stage-presents-the-act.md) | Legibility over density: a surface presents the ACT the writer is performing, not a console. Enforceable floor — the act is the largest/central element; the glasses test (min type + hit-target sizes); progressive disclosure of per-object machinery (no permanent hieroglyph rows); one act in focus at a time; relationships are DRAWN, not implied by a glyph; and every visual change is verified by LOOKING at the rendered view (light + dark), never by the accessibility tree alone (the machine-readable half is necessary, never sufficient). |

## Vocabulary

**Canonical source** means the imported manuscript stored under the source document identity. It is evidence, not a work surface for generated analysis.

**Grounding Profile** means the writer-confirmed policy document that directly governs downstream interpretation. It is not a summary of the source.

**Storify Source Auto** means the chapter-aware structural reading that converts source atoms into kept/noise decisions, beats, uncertainty, synopsis, and arcs.

**Cut Script** means the mutable, authored draft product assembled from chosen Storify units and later composition.

**Continuity** means the audit over Cut Script or other explicitly selected units. It is not a substitute source reader.

**Legacy semantic artifacts** means index passages, reading states, semantic memory, published semantic objects, repair debt, and index performance memory created before this refactor. They may remain inspectable, but they have no authority in the final pipeline.
