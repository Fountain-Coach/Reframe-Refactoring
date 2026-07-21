# Reading Index

> Chapter summary: This index offers role-based reading paths, chapter descriptions, and a vocabulary map so humans and agents can retrieve only the material relevant to the task at hand.

The suite is intentionally divided into short, stable chapters. Agents should not load the whole directory into every prompt. Select the chapters whose authority is necessary for the current phase, then retrieve live code and state for implementation detail.

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

### Copilot implementation

Read the [target architecture](04-target-architecture.md), [Grounding contract](05-grounding-contract.md), and the [Copilot implementation extension](10-copilot-implementation-extension.md), then follow its mandatory discovery procedure before editing. The Copilot must reuse existing application operations and the same authority chain; it is not a second workflow engine. The behavioural, relaunch, and no-index acceptance cases in [validation and acceptance](08-validation-and-acceptance.md) apply.

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
| [Animating truth](12-animating-truth.md) | Perceived performance: never sign a wait with a spinner. Render the frame and cheap/cached truth instantly; foreshadow the unknown as honest, animated structure whose motion maps to real work. Applied first to loading. |
| [App-flow record](reframe-app-flow-governance.md) | The complete prose account of how the app must flow end to end — the single continuous narrative these numbered chapters refine. |
| [Storage and performance](13-storage-and-performance.md) | Locks the storage layering — document layer = plain-text bundle + single manifest; musical layer = MIDI 2.0 — and the performance doctrine: reads are fast architecturally (cache-first, one manifest, no serial fan-out), not by encoding. |

## Vocabulary

**Canonical source** means the imported manuscript stored under the source document identity. It is evidence, not a work surface for generated analysis.

**Grounding Profile** means the writer-confirmed policy document that directly governs downstream interpretation. It is not a summary of the source.

**Storify Source Auto** means the chapter-aware structural reading that converts source atoms into kept/noise decisions, beats, uncertainty, synopsis, and arcs.

**Cut Script** means the mutable, authored draft product assembled from chosen Storify units and later composition.

**Continuity** means the audit over Cut Script or other explicitly selected units. It is not a substitute source reader.

**Legacy semantic artifacts** means index passages, reading states, semantic memory, published semantic objects, repair debt, and index performance memory created before this refactor. They may remain inspectable, but they have no authority in the final pipeline.
