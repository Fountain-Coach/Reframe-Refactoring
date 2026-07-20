# Refactoring Program

> Chapter summary: This chapter gives the ordered, replacement-first implementation program, identifies current code seams, and defines the exit criteria that must be met before indexing code can be deleted.

This refactor is too cross-cutting for a single deletion commit. It changes product stages, persisted authority, prompts, readiness, UI, capabilities, tests, and generated reasoning orientation. Work must proceed in the phases below. Each phase requires an updated `PLANS.md` entry before implementation and ends only when its persisted behavior is proven.

## Phase 0 — Establish evidence and freeze the boundary

Record an end-to-end baseline for the current Grounding → index/Guide → Storify → Cut Script → Continuity path. Capture total latency, provider calls by purpose, Storify window count, derived-from-reading versus independent Storify decisions, beat coverage, uncertainties, and downstream continuity usability. This evidence is a migration comparator, not a gate that preserves indexing indefinitely.

Inventory all index producers and consumers with repository search. Begin with `indexSemanticMemoryInternal`, `startPrepManuscriptGuideGenerationTask`, `semantic_index_fresh`, `prepPublishedSemantic`, `semantic.readingStates`, `storifyReportFromReading`, `storifySemanticMemoryContext`, index commands, index UI labels, and semantic repair/readiness tests. Record the inventory in the phase plan so later deletion can prove each consumer was replaced rather than merely made unreachable.

Exit when the baseline and consumer inventory are durable and reviewable.

## Phase 1 — Persist the extended Grounding Profile

Introduce the Grounding Profile and history model described in [the Grounding contract](05-grounding-contract.md). Reuse existing author baseline, reader lens, language, and destination-medium data without inventing a second authority. Add the missing structural intent, preservation duties, and transformation boundaries through a migration that makes legacy confirmed baselines visible but incomplete until their new downstream policy is explicitly confirmed.

Update the Grounding UI so the writer can see the complete contract, edit draft values, understand which fields affect Storify, and confirm one coherent version. Persist a semantic identity and provenance. Do not make UI state or in-memory flags the source of confirmation.

Exit when a clean launch and relaunch recover exactly the same confirmed Grounding identity from FountainStore, and editing any semantic field makes the draft visibly newer than the confirmed profile.

## Phase 2 — Make Storify directly Grounding-aware

Extend `StorifyPass.semanticPrompt` and its call site in `ReframeViewModel+BodyB.swift` to receive the current confirmed Grounding context. Record its identity on the run, window, report, synopsis, and arc artifacts. Ensure writer steering remains a current-run overlay rather than mutating the confirmed profile.

Disable both index integrations in the experimental path: do not call `storifyReportFromReading`, and do not load or inject `storifySemanticMemoryContext`. Add negative instrumentation proving no reading state or semantic-memory document was consulted. Keep Source Auto's independent atom extraction, chapter seams, model validation, provider recovery, backfill, resume, and persistence behavior.

Exit when Source Auto succeeds in a store that contains confirmed Grounding and source text but no semantic-index documents, every semantic window records the same current Grounding identity, and prompt inspection tests prove the author baseline, reader lens, language, structural intent, and transformation boundaries are represented without index content.

## Phase 3 — Make Storify artifacts the downstream structural authority

Bind beat-board, synopsis, arc, Cut Script, and story-context consumers to source + Grounding + Storify identities. Where a consumer currently reads a published semantic object or index-derived sequence, replace it with the corresponding Storify artifact or a targeted source retrieval.

If a human-readable Manuscript Guide remains in the product, convert it into a deterministic projection over confirmed Grounding and completed Storify synthesis. Rename internal types where necessary so a projection cannot be mistaken for an inference job. Publishing this view must not trigger a provider call.

Exit when Cut Script can be produced from a clean no-index store and every downstream artifact can identify the exact Storify and Grounding lineage it consumed.

## Phase 4 — Replace readiness, journey, and capability contracts

Rewrite `pipelineReadinessSnapshotForStorifySource` or replace it with a name that reflects the full pipeline rather than a former Storify gate. Grounding readiness comes from the confirmed profile. Storify readiness comes from settled, identity-matching windows. Annotation authority, editor state, Cut Script, synopsis, compose, and publish no longer consult semantic readiness or a published semantic object.

Remove `semantic_index_fresh` from `schema/modernization-studio-capabilities.json` and every generated reasoning-manifest projection. Update command help, journey readers, Truth Center, load gates, status copy, operator guidance, and empty states. Do not leave a compatibility boolean that is always forced true; remove the concept.

Because capability and workflow orientation change here, regenerate all tracked reasoning-manifest artifacts before declaring the phase consistent.

Exit when an empty index is not a blocker or warning anywhere in the current journey, and a stale Grounding or Storify identity is described accurately from persisted state.

## Phase 5 — Replace index-backed retrieval and product surfaces

Route story and workflow questions through targeted retrieval from canonical source, confirmed Grounding, Storify windows/synthesis, Cut Script, and Continuity. Retire index read tools from model-facing capability sets. Preserve the mediation boundary: natural-language questions are resolved by grounded reasoning, not by matching phrases to a replacement command.

Remove the Index tab, passage read-in controls, Reading Laboratory presentation, index uncertainty surfaces, semantic repair queue UI, index activity copy, and settings that configure only the retired reader. Preserve reusable generic components only when they have a real non-index consumer and are renamed to that responsibility.

Exit when product navigation contains no index task and chat can answer supported story questions from targeted current artifacts without consulting index documents.

## Phase 6 — Delete the indexing runtime

Deletion begins only after phases 1–5 pass. Remove index entry points, chunk orchestration, staged passage reading, reading-state persistence, index repair debt, learned Apple split memory, index-only economic plans, provider timing ledgers that have no remaining consumer, index eval harnesses, and index-specific test shims. Remove `ReframeBeatDerivation` only after proving no non-index feature uses it; retain domain-neutral turn types only if Storify itself produces and consumes them under a new explicit owner.

Delete imports, settings, configuration keys, telemetry names, store document writers, and UI bindings that became dead. Use compiler errors and repository-wide searches as a consumer audit, but do not treat compilation alone as proof: dynamically named FountainStore prefixes, generated manifests, help text, snapshots, and tests must also be searched.

Legacy index documents remain untouched in existing stores. The runtime simply stops listing or consuming them operationally.

Exit when repository search finds no production reference to index entry points, index readiness, index-derived Storify input, or published semantic-object gating; all packages build; and the complete no-index acceptance journey passes.

## Phase 7 — Consolidate and remove transition machinery

Temporary comparison flags may exist while phases are evaluated, but the final architecture must not ship dual readers or a permanent “legacy index mode.” Remove the flags, old config keys, transition-only adapters, and migration diagnostics after the no-index path becomes authoritative.

Update app README material, operator playbooks, pipeline documentation, screenshots, demo stores, seeded expectations, and proofreader checklists. Older design notes may remain as dated historical records, but they must carry a superseded notice and link to this guide when they could otherwise misdirect implementation.

Exit when documentation, generated orientation, UI, tests, and runtime describe the same pipeline.

## Primary code seams

The following locations are starting points, not an exhaustive deletion list:

- `ReframeViewModel+BodyA.swift`: readiness, Guide generation, journey transitions, and background index calls.
- `ReframeViewModel+BodyB.swift`: Source Auto, direct Storify prompt construction, old memory injection, and auto orchestration.
- `ReframeViewModel+BodyC.swift`: Storify projections, source compatibility helpers, continuity reporting, and annotation authority.
- `ReframeViewModel+BodyD.swift`: semantic index orchestration, passage persistence, Guide-related semantic products, and repair behavior.
- `ReframeViewModel+BodyE.swift`: semantic helpers, memory context, learned split memory, prompts, and commands.
- `AppleStagedReadingModel.swift` and `ReframeViewModel+ReadingLaboratory.swift`: index-specific source reading and its Storify shortcut.
- `StudioSemanticCoordinator.swift`: index state and passage quality.
- `ReframeBeatDerivation.swift`: turns derived from index reading states.
- `BaselineWorkbenchPanel.swift`, `PrepCopilotWorkspaceView.swift`, `SemanticIndexView.swift`, and related shell views: product language and surfaces.
- `schema/modernization-studio-capabilities.json` and generated reasoning manifests: model-facing workflow truth.

Agents must rediscover exact consumers with `rg` at the start of each phase. This list describes known architecture; it is not permission to ignore code added later.

## Copilot extension to this program

This program governs the visible editorial pipeline. The conversational Copilot is migrated onto the same post-indexing authority model by a parallel, evidence-first program defined in the [Copilot implementation extension](10-copilot-implementation-extension.md). That chapter adds its own ordered phases — implementation map and parity matrix, Grounding-first perception, retrieval parity, action migration, action parity, and behavioural acceptance — and its own deletion obligation for indexing-era Copilot behaviour. Its phases are a deliberate addition to this program, not a rewrite of it: the Copilot must reuse the authoritative application operations these phases produce, never reconstruct them. Begin that work from the extension's mandatory discovery procedure, not from a presumed conversational flow.
