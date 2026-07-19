# Current State and Refactoring Problem

> Chapter summary: This chapter describes the live seams that still connect Grounding, indexing, the Manuscript Guide, Storify, and Continuity, and identifies the exact problems the refactor must remove.

The current runtime contains both the old pipeline and its successor. Understanding that overlap is essential because a deletion performed from product terminology alone would leave hidden consumers behind.

Grounding currently persists the author baseline, reader lens, language, and related manuscript settings. Its readiness is real, but its downstream semantic influence is largely mediated through index generation and the published semantic object called the Manuscript Guide. `startPrepManuscriptGuideGenerationTask` waits for or launches `indexSemanticMemoryInternal`, then persists a Guide candidate. UI, journey, and readiness language still describe this as the canonical handoff.

Indexing itself is a large runtime. It selects source or chapter chunks, calls Apple or another configured semantic route, validates results, persists passage feeds and reading state, records repair debt, resumes interrupted work, exposes uncertainty and activity, and contributes economic-inference artifacts. Apple-specific code now includes provider phase telemetry and learned exact-source recovery from context and safety failures. This behavior is extensively tested, but it remains a separate serial reading of the source.

Storify has two distinct index integrations. First, `storifyReportFromReading(atoms:)` attempts to derive beat boundaries from accepted, evidence-linked turns in persisted reading states. A successful derivation bypasses Storify's semantic model call. Second, `storifySemanticMemoryContext` can inject selected summaries, claims, patterns, and reflection as memory priors into the ordinary Storify prompt. These are independent integrations: disabling derived beats does not by itself make Storify index-free.

Storify also has a complete index-independent path. It reads the canonical source through `sourcePipelineText`, selects the active chapter when appropriate, analyzes prose or screenplay form, extracts candidate atoms, pages those atoms without crossing chapter seams, asks the configured provider for kept/noise decisions and beat ordering, validates returned identifiers, persists window artifacts, and runs later synopsis or arc synthesis. The source atoms are authoritative, and a failed semantic read produces an explicit unreadable or pending window rather than invented structure.

The active Source Auto loop no longer writes analysis into the canonical source. It persists Storify state and derived documents. Compatibility helpers can still render historical `STORIFY:AUTO` blocks for old projections, but they are not the target storage model and must not be mistaken for current write authority.

Continuity is downstream and structurally separate. Its Cut Script path derives units from the draft and records reports with the draft input identity. It does not require indexed passages to perform the audit. Its own future incremental invalidation work remains valuable, but it is not a reason to preserve indexing.

## The architectural defects

The first defect is duplicate authority. The application can describe the Manuscript Guide as canonical, derive beats from reading states, ask Storify to read atoms independently, and then synthesize another global story product. A maintainer cannot tell from product labels alone which artifact deserves trust.

The second defect is disconnected Grounding. If both index integrations are disabled today, Storify still works, but the author baseline and reader lens no longer reliably reach its semantic window. Storify receives generic instructions, a Storify preset, source atoms, and current steering. Removing indexing without replacing this handoff would improve latency by silently discarding writer intent.

The third defect is unsafe partial acceleration. The derived-beat seam requires an opening turn but does not establish that every atom in the requested window was read to an acceptable quality. A structurally valid turn can therefore stand in for a broader reading than the index actually earned.

The fourth defect is stale readiness. Capability definitions, reasoning manifests, UI copy, journey state, and tests still mention `semantic_index_fresh`, published semantic objects, or the Guide as prerequisites even though Source Auto's execution path treats readiness as status and proceeds independently.

The fifth defect is maintenance gravity. Index-specific provider tuning, repair, telemetry, UI, persistence, and tests consume engineering attention while Storify has become the stage that actually owns structural output. Continuing to optimize both readers makes the boundary less clear, not more reliable.

## Refactoring boundary

The refactor removes the semantic indexing product and runtime, not every use of the word “semantic,” every model call, or the Apple provider. Storify remains a semantic structural reader. Continuity remains a semantic audit. Chat may reason over retrieved source and derived artifacts. The deletion target is the independent passage-index authority and every downstream dependency on it.

Likewise, the refactor does not authorize a broad rewrite of Cut Script, Continuity, the MIDI backplane, or FountainStore. Those systems change only where they read readiness, Grounding identity, or former index artifacts.
