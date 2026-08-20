# Source and Synchronization Contract

## Current planned change — Chapter 87 MIDI2 Monitor foundational boundary (2026-08-20)

- Change: Chapter 87 defines the Swift-owned MIDI2 Monitor as the live event boundary between negotiated transport,
  durable FountainStore proof, the AX-visible peer mirror, and independent scenario witnesses.
- Direction: publication → integration through `Scripts/sync-integration-copy --push`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@e7194ed`.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@e04d312d`.
- Claim boundary: governance and deterministic design mock only; no runtime monitor implementation, hardware
  interoperability, or live-acceptance claim is made.
- Local validation: 89 generated routes, SVG render, guide parity, and independent light/dark/mobile AX/VRT acceptance.

## Current synchronized change — Chapter 86 Apple-native semantic pipeline refactoring (2026-08-19)

- Change: Chapter 86 defines Storify's local Apple measurement plus paid extension as one source-addressed MIDI2
  graph, with seven typed stage identities, portable FCIS-KIT boundary, and implementation acceptance order.
- Direction: publication → integration through `Scripts/sync-integration-copy --push`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@862f036`.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@1248ed54`; the synchronized integration tree also contains the typed IDL, generated contracts,
  and tested pre-release `FountainSemanticPipelineKit` implementation boundary.
- Claim boundary: governance and contract publication only; no complete semantic executor graph or live scenario
  acceptance is claimed.
- Production result: release `release-20260819T100116Z` is live at `governance.fountain.coach`; overview, status-quo,
  Chapters 85 and 86 return HTTPS 200 and DNS resolves to `65.109.14.71`.

## Current planned change — Correct Facebook link versus preview image (2026-08-18)

- Finding: the prior Facebook handoff linked the image-only `/social/<asset>/` route instead of the chapter site.
- Fix: generated illustrated chapters now have a cache-safe full-content `/chapters/<slug>/share/<asset>/` route; social
  packages use that route as `publicUrl` while retaining the 1200×630 card as `og:image`.
- Claim boundary: publication/social packaging only; no external post is claimed until Facebook returns a post record.
- Result: Chapter 84 packages now use `https://governance.fountain.coach/chapters/84-governed-reframe-design-mock/share/84-governed-reframe-design-mock-0132f2b1aae8/` as the Facebook `publicUrl`. That route serves the full chapter and declares the 1200×630 card as `og:image`; the image-only `/social/` route is no longer an allowed Facebook target. Integration skill commit `Fountain-Coach/midi2-gpu-fabric@ad19f054`; publication commit `Fountain-Coach/Reframe-Refactoring@fd24cde`.
- Production result: release `release-20260818T060312Z` is promoted; the full share route, stable chapter route, and card return HTTPS 200, and the share HTML contains the expected chapter title plus `og:image` dimensions.

## Current planned change — Improve governance table readability (2026-08-18)

- Change: publication tables now use readable spacing, restrained header hierarchy, alternating row surfaces, safe prose
  wrapping, and mobile-only horizontal scrolling for tables wider than the viewport.
- Claim boundary: CSS projection only; Markdown meaning, runtime behavior, scenario evidence, and navigation semantics are
  unchanged.
- Validation: desktop/mobile visual review, browser AX table semantics, overflow measurement, and governance acceptance
  passed: one table, 84 rows, two column headers, and zero desktop body overflow.
- Production result: publication commit `Fountain-Coach/Reframe-Refactoring@5be704e` is live as release
  `release-20260818T055902Z`; overview and Chapter 01 return HTTPS 200.

## Current planned change — Repair broken Reading Index table rendering (2026-08-18)

- Finding: blank lines between Markdown table rows in Chapter 01 caused Pandoc to terminate the table and emit the
  remaining catalogue entries as detached paragraphs, creating the split visible in the browser.
- Fix: removed the four blank separators within that table only; chapter wording and navigation semantics are unchanged.
- Validation: generated output contains one 84-row table, zero stray pipe paragraphs, no body overflow at 1200px, and
  local governance AX/VRT acceptance passed. The publication copy was synchronized to integration with `--push`.
- Claim boundary: publication rendering repair only; no runtime, scenario, Store, or capability claim changes.
- Production result: publication commit `Fountain-Coach/Reframe-Refactoring@a6785a5` is live as release
  `release-20260818T054618Z`; Chapter 01 returns HTTPS 200 with the repaired table.

## Current planned change — Chapter navigation and desktop arrow reading (2026-08-18)

- Change: generated chapter pages now expose explicit previous/next links, chapter position, and desktop Left/Right
  keyboard navigation; the active chapter rail entry is brought into view on load.
- Claim boundary: publication navigation only; no runtime, scenario, Store, or capability claim is changed.
- Validation: local generated route/link checks, browser AX/keyboard drive, desktop/mobile VRT, and prepublish scan are
  required before deployment. Governance-specific checks passed: 86 pager routes, AX names for both navigation regions,
  ArrowRight/ArrowLeft round trip between Chapters 83 and 84, and 1440×1000 visual review. The separate Book scan is
  blocked by missing PyYAML for `compliance/register.yaml` and reports its existing canonical-host warning.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@203feb2`.
- Production result: release `release-20260818T054125Z` is live at `governance.fountain.coach`; overview, Chapter 83,
  and Chapter 84 return HTTPS 200.

## Current planned change — Mandatory illustration social-post template (2026-08-18)

- Change: the publication generator now creates deterministic 1200×630 social-post derivatives for every chapter with
  a reviewed illustration, and emits matching Open Graph/Twitter metadata plus an accessible page link.
- Integration governance skill commit: `Fountain-Coach/midi2-gpu-fabric@87ebf934`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@951bf9c`.
- Claim boundary: social derivative and metadata are publication projections only; no external post was created and no
  scenario, AX, Store, image-generation, or placement evidence is implied.
- Production result: release `release-20260818T050939Z-43273` is promoted; Chapter 84 metadata and its 1200×630 card
  return HTTPS 200.
- Visual correction commit: `Fountain-Coach/Reframe-Refactoring@a9f4fee` and integration skill commit
  `Fountain-Coach/midi2-gpu-fabric@b7fb34a7` establish the white Fountain Coach/Courier visual system.
- Corrected release: `release-20260818T051717Z-44014`; Chapter 84 social image returns HTTPS 200 and matches the
  committed digest `0132f2b1aae884fee414f97e00af6f2a8a2ad631100d8ef9d1d2b50ca3462a9f`.

## Current planned change — Cache-safe social share routes (2026-08-18)

- Change: every generated social illustration receives a digest-named image and a matching `/social/<asset>/` page
  whose canonical and Open Graph URL is the new share URL.
- Claim boundary: this changes publication URL identity only; it does not claim that Facebook has fetched or published
  the preview, and no external post was created by the publisher.
- Validation: local generator build, route metadata, 1200×630 image dimensions, link checks, and independent AX/VRT
  acceptance passed.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@eaf1ddb`.
- Production result: release `release-20260818T052802Z-44948` is live; the cache-safe Chapter 84 route and its 1200×630
  image return HTTPS 200.

## Current planned change — Chapter 84 governed Reframe design mock (2026-08-18)

- Change: **Chapter 84 — The Reframe Design Mock Is a Governed Projection**, defining a deterministic default design
  reference that shows current Reframe layout plus proposed semantic illustration rollout without fabricating runtime,
  Store, AX, MIDI2, or Image Cloud evidence.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@a59b69b4`.
- Publication governance commits: `Fountain-Coach/Reframe-Refactoring@c622ab6` (chapter, generator, and site) and
  `Fountain-Coach/Reframe-Refactoring@0f8133f` (published illustration asset).
- Claim boundary: design reference only; `teatro-score-myth-illustrations` remains executable-not-live-accepted.
- The governance publisher and generator now exclude macOS AppleDouble metadata without rejecting valid generated
  content; local design-mock render and governance AX/VRT passed.
- Production result: release `release-20260818T045623Z-41188` was promoted to
  `/var/www/reframe-governance/current`; HTTPS returned 200 for Chapter 84 and the deployed asset is present.
- Live-derived correction: integration commit `Fountain-Coach/midi2-gpu-fabric@51b7be1c` and publication commit
  `Fountain-Coach/Reframe-Refactoring@4cc121d` replace the prior invented dark composition with the measured light
  Reframe shell and a proposed Copilot-region feature.
- Corrected production result: release `release-20260818T050417Z-42416` is promoted; Chapter 84 and its SVG asset
  return HTTPS 200, with rollback retained.

## Current planned change — Chapter 83 conversational scenario authoring (2026-08-18)

- Change: **Chapter 83 — Conversational Scenario Authoring Is the Development Surface**, defining scenarios as
  executable prompt-contracts authored conversationally and compiled to YAML/JSON, with semantic movement/question
  dependencies, typed execution, evidence lineage, and a clear boundary between governance and implementation.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@9c8fb561`.
- Publication governance commit: `Fountain-Coach/Reframe-Refactoring@04f258d`.
- Synchronized: 2026-08-18; guide parity, local governance build, and independent local AX/VRT acceptance passed.
- Claim boundary: governance only; the conversational authoring surface and compiler are not yet implemented or
  live-accepted by this chapter.
- Deployment repair: guarded publisher added at `Scripts/publish_governance_site.sh`; dry-run passed against the
  fixed host/root tuple.
- Production result: release `release-20260818T044627Z-40492` was promoted to
  `/var/www/reframe-governance/current`; HTTPS returned 200 for the overview, status-quo route, and Chapter 83.

## Current synchronized change — Chapter 79 default semantic manuscript projection (2026-08-17)

- Change: **Chapter 79 — The Default Semantic Manuscript Projection**, defining the continuous Courier/Fountain
  manuscript, semantic Questions/Movements/Read coverage navigation, right Copilot, bottom MIDI2 peers, and the
  boundary between a design illustration and acceptance evidence.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@48a46501`.
- Publication governance commit: `Fountain-Coach/Reframe-Refactoring@2b91e87`.
- Claim boundary: the chapter and signature image govern presentation intent only; no runtime or live-acceptance claim
  is promoted by publication.
- Synchronized: 2026-08-17; guide parity passed after transfer.

## Current synchronized change — Questions / Movements vocabulary (2026-08-17)

- Change: Chapters 28 and 76 now distinguish the `Questions`, `Movements`, and `Read coverage` lanes. The historical
  `beat` term remains a compatibility alias only; writer-facing projections must not use it for either lane.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@47df9e44`.
- Publication content/provenance commit: `Fountain-Coach/Reframe-Refactoring@ad6ce7b`.
- Synchronized: 2026-08-17; parity check passed after transfer.

## Current synchronized change — Chapter 78 (2026-08-17)

- Change: **Chapter 78 — Scenario-Driven Development Is Org Infrastructure**, naming the portable scenario contract,
  the Swift/MIDI2 event-driven seam, independent evidence authorities, historical context, and future negotiated-peer
  infrastructure.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@9fef1e66`.
- Publication content commit: `Fountain-Coach/book-of-reframe@9946725`.
- Claim boundary: governance and public method only; the public `FountainScenarioKit` package is reusable infrastructure,
  while Reframe-specific runtime, Store, AX, and live-acceptance claims remain separately governed.
- Synchronized: 2026-08-17.

## Current synchronized change — Chapter 77 (2026-08-17)

- Change: **Chapter 77 — The Scenario Runtime Is Swift and MIDI2-Native**, making scenario preparation, execution,
  lifecycle waits, evidence binding, and terminal classification an owned Swift capability using the production MIDI2
  operation boundary.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@53a07e78`.
- Publication content commit: pending this commit.
- Claim boundary: governance only; the Swift executor and scenario MIDI2 operation remain unimplemented and
  unaccepted. Python is transitional, and no hardware-interoperability claim is made.
- Synchronized: 2026-08-17.

## Current synchronized change

- Change: **Chapter 76 — Beat Movement and the Uncertainty Overlay**, reconciling grounded dramatic beats with the
  optional uncertainty-question lifecycle across Storify, UncertaintyScoreKit, Score projections, and image
  participants.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@10692fef`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@f97e590`.
- Synchronized: 2026-08-16.

## Current synchronized change

- Change: **Chapter 75 — Scenario Run Ownership and Non-Interference**, defining single-run ownership, event-driven
  waiting, intervention invalidation, and the terminal evidence boundary for truthful scenario acceptance.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`; this checkout has no sync helper, so
  the three governed files were transferred explicitly).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@b6f510a9`.
- Publication content/provenance commit: this synchronization commit; see `git log` for its immutable hash.
- Synchronized: 2026-08-16.

## Current planned change

- Change: **Chapter 72 — MIDI2 Peer Projections and Capacity Admission**, defining the generic peer projection surface,
  clonable endpoint identity, Reframe's default software-peer fixture, capacity-governed admission, and AX/Store/MIDI2
  evidence requirements.
- Direction: publication → integration (`Scripts/sync-integration-copy --push`).
- Publication content commit: pending.
- Integration content/provenance commit: `Fountain-Coach/midi2-gpu-fabric@7a8fe4d5`.
- Synchronized: 2026-08-16.

## Current planned change

- Change: **Chapter 71 — Reframe-to-Reframe Software-Peer Acceptance**, defining the two-process software-peer
  conformance topology, independent witness, separate Store authority, scenario-first gates, and the boundary between
  software-peer acceptance and hardware interoperability.
- Direction: publication → integration (`Scripts/sync-integration-copy --push`).
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@a168353`.
- Integration content/provenance commit: `Fountain-Coach/midi2-gpu-fabric@dee3d52a`.
- Synchronized: pending.

## Current synchronized change

- Change: **Chapter 70 — External MIDI2 Control of Reframe**, defining negotiated external operation ingress, internal
  mediation and lane policy, FountainStore lifecycle authority, MIDI2 event projection, AX/window-ID evidence, and
  scenario-first gates for claiming full live drivability.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@49e96076`.
- Publication content/provenance commit: this synchronization commit; see `git log` for its immutable hash.
- Synchronized: 2026-08-16.

## Current planned change

- Change: **Chapter 46 amendment — semantic carry-forward for iterative readings**, requiring a second Storify run to
  remember persisted findings and evidence under the same confirmed lens, with explicit lineage and no manufactured
  divergence.
- Direction: publication → integration (`Scripts/sync-integration-copy --push`).
- Publication content commit: pending.
- Integration content/provenance commit: pending synchronization.
- Synchronized: pending.

## Current planned change

- Change: **Chapter 68 — Governed Reframe E2E scenarios and Book publication**, making a versioned, prerequisite-
  complete scenario the first artifact for every Book command and binding AX, window-ID, FountainStore, paid-lane,
  and provenance evidence to one run.
- Direction: publication → integration (`Scripts/sync-integration-copy --push`).
- Integration content/provenance commit: `Fountain-Coach/midi2-gpu-fabric@706d022a`.
- Publication content/provenance commit: `Fountain-Coach/Reframe-Refactoring@acff230`.
- Synchronized: 2026-08-15.

## Current synchronized change

- Change: **Semantic turn-router governance status correction**, making explicit that the one-reasoning, paid-first,
  typed-handoff contract already exists in Chapters 20, 23, 24, 37, 51, and 58, while runtime adoption remains
  partial because downstream workflow, reference, and lane stages can still re-decide or discard a mediated turn.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@9aaeb347`.
- Publication content/provenance commit: this synchronization commit; see `git log` for its immutable hash.
- Synchronized: 2026-08-15.

## Current synchronized change

- Change: **Paid-first, task-based model selection**, amending Chapters 20 and 51 and the reading index so Reframe
  selects the best eligible model from live facts, keeps bounded local delegation internal, and honors explicit
  local-only instructions without requiring exact wording.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@73bd20c7`.
- Publication content commit: this synchronization commit; see `git log` for its immutable hash.
- Synchronized: 2026-08-15.

## Current synchronized change

- Change: **Chapter 67 amendment — Copilot-native attachment visual introspection**, moving attachment self-awareness
  into Copilot with media-specific image, PDF, Fountain, and Markdown projections; retiring the left-side attachment
  projection while keeping reference custody distinct from source ingestion.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@46407e56` (content `d8a60e23`).
- Publication mirror commit: `Fountain-Coach/Reframe-Refactoring@5571dab`.
- Synchronized: 2026-08-14.

## Current synchronized change

- Change: **Chapter 67 amendment — explicit composer upload ceiling**, defining the 8-attachment, 50 MiB-per-file,
  200 MiB-per-turn limit, complete-batch preflight, AX-visible rejection, and independent Attachment Cloud guard.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@c90da666`.
- FountainComposerKit contract/deployment: `Fountain-Coach/FountainComposerKit@4178190` (v0.3.5), deployed to
  `library.fountain.coach` from the same revision.
- Publication mirror commit: the publication commit containing this synchronization record; see `git log` for its
  immutable hash.
- Synchronized: 2026-08-14.

## Current synchronized change

- Change: **Chapter 67 — FountainComposerKit — Remote Attachment Custody**, defining the Copilot composer as the one
  typed ingress for text, images, and files; remote Attachment Cloud admission before pipeline use; minimal local
  references; structured Copilot context; and typed evidence across the cycle.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@29032509`.
- Publication mirror commit: `Fountain-Coach/Reframe-Refactoring@45c24a8`.
- Publication provenance commit: `Fountain-Coach/Reframe-Refactoring@e785b93`.
- Synchronized: 2026-08-13.

## Current synchronized change

- Change: **Chapter 66 amendment — official ReframeICloudKit seam**, distinguishing native PhotoKit placement from the
  embedded iCloud Photos WebKit handoff, typed placement receipts, generation/staging/placement states, package
  provenance, and Apple credential custody.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@11b1237e` (content `bb38aeed`).
- Publication content/provenance commit: `Fountain-Coach/Reframe-Refactoring@7a1a517`.
- Synchronized: 2026-08-13.

## Current synchronized change

- Change: **Chapter 66 — Reframe Image Sources, Prompting, and Generation**, defining the compound PhotoKit/iCloud →
  Fountain image directive → writer prompt → OpenAI generation/editing boundary, including privacy, provider
  custody, visual projection, and source-to-result lineage.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@f044d3c4`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@be743e4`.
- Synchronized: 2026-08-13.

## Current synchronized change

- Change: **Chapter 65 — The Copilot as Writing Coach**, defining the writer-facing Copilot persona that carries the
  default Grounding stance and invokes the internal Dramaturg realization discipline without exposing Dramaturg as a
  writer-facing control.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@bb27ec70`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@3dac8f9`.
- Synchronized: 2026-08-13.

## Current synchronized change

- Change: **Internal quality routing and invisible delegation**, amending Chapters 20 and 57 so Copilot silently
  chooses the strongest authorized route and uses efficient local sub-work without exposing provider handoff.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@60d268f6`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@0caad01`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Conversational credibility and quality-first lane policy**, amending Chapters 20 and 57 so reliable
  conversational quality takes precedence over cost-saving local execution while consent remains mandatory.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@5a9e8f93`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@5d3fea9`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Chapter 64 — FountainProjectKit — Durable Fountain Project Custody**, defining the reusable Swift
  custody boundary around FountainEditorKit: immediate creation persistence, edit flush, interruption and relaunch
  recovery, AX save truth, and the separation of working drafts from Git and Book Library publication.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@af60fca8`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@80e718d`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Library-rooted reading boundary and citation evidence bundle**, making the Book Library Reframe's sole
  reading provider, prohibiting generic web/DraCor/local-file reading, and binding textual citation evidence to its
  matching WebKit snapshot through one retrieval identity.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@71136ea2`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@20375e8e`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Copilot projection/conversation split amendment**, defining the Copilot-controlled projection on the left,
  Copilot mediation and commands on the right, and the two-pane seam across reading, Fountain editing, and round-trip
  handoff.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@02a50b0a`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@120787e`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Chapter 57 amendment — Copilot as semantic Book Library agent**, defining on-device semantic metadata
  discovery, provider retrieval versus Copilot interpretation, ambiguity preservation, and scale without catalog dumps.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`.
- Publication path: `docs/`.
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@27fba919`.
- Publication content/provenance commit: `Fountain-Coach/Reframe-Refactoring@eee0829`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Chapter 56 amendment — provider-defined publication navigation**, requiring validated, extensible
  navigation manifests with stable IDs, source ranges, optional kinds/parents, and no silent whole-work fallback.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`.
- Publication path: `docs/`.
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@9f46f862`.
- Book Library implementation: `Fountain-Coach/book-library@8054cf9`.
- Synchronized: 2026-08-12.

## Current synchronized change

- Change: **Chapter 61 — The Fountain Project Round Trip**, closing the explicit Library → Reframe → Compose →
  Fountain Project → managed Git → Library lifecycle with separate identities, provenance, transformation records,
  and no automatic feedback loop.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`.
- Publication path: `docs/`.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@6e352a82`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@64d7bcb8`.
- Synchronized: 2026-08-11.

## Current synchronized change

- Change: **Chapter 60 — The Fountain Editor Is the Project Surface**, defining Reframe as the writer-facing Fountain
  editor and Copilot project mediator, with managed Git as versioned transport, governed Fountain front matter, and
  the Book Library as publication authority.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`.
- Publication path: `docs/`.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@f72483e8`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@9bf5b972`.
- Synchronized: 2026-08-11.

## Current synchronized change

- Change: **Chapter 59 — The Fountain-Coach Git Library and Reframe Project Flow**, replacing the former GitHub-specific
  curation design with a Fountain-Coach-owned Git project service, an owned Swift Git boundary, Copilot-first project
  views, explicit Library candidate/release flow, authored export, custody, accounting, and migration.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`.
- Publication path: `docs/`.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@93c654f0`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@d694251`.
- Synchronized: 2026-08-11.

## Current synchronized change

- Change: **Chapter 58 — Open-Turn Mediation Protocol**, defining the single reusable mediation boundary for first
  contact, interruption, nonsense, correction, ambiguity, and spontaneous change of mind before an existing
  capability or lane executor acts.
- Direction: integration → publication (manual exact transfer; the documented sync helper is absent in this checkout).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@3ac6a135`.
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@57ca370`.
- Synchronized: 2026-08-11

## Current synchronized change

- Change: **Chapter 57 — The Writer Enters by Intention.**
- The ruling: Reframe opens on the writer's intention; on-device Copilot resolves that intention against the live
  published Book Library; provider IDs remain internal; retired visible controls retain structured accessibility
  paths; and AX semantic proof plus rendered visual proof are both mandatory.
- Direction: integration → publication (exact transfer of Chapter 57 and the reading-index row).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@3271f90f`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@074cfed` (content); this provenance correction is the
  following commit.
- Synchronized: 2026-08-10

## Current synchronized change

- Change: **Chapter 56 — The Book Library Is a Portable Source Provider.**
- The ruling: a separately hosted, provenance-preserving Book Library is a first-class Reframe source beside DraCor
  and local file; it owns curation, publication, OpenAPI delivery, withdrawal, and migration, while Reframe owns the
  writer-facing import and FountainStore owns native persistence. Acquisition is a remote candidate operation;
  governed promotion is a local publisher operation with explicit approval and rollback evidence.
- Direction: integration → publication (exact transfer of Chapter 56 and the reading-index row).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@fc40c88c`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@da992f7`.
- Synchronized: 2026-08-10

## Current synchronized change

- Change: **Chapter 54 — The Writer Does Not Manage the Projection.**
- The ruling: Reframe contains ledgers, providers, consent, batches, and rendering detail so the writer navigates
  manuscript questions rather than managing implementation machinery. `/readings`, `/ground`, and `/world` are
  sibling domains; outside investigation is an offered `/reference` act. Durable uncertainty evidence remains
  complete while every visual projection is bounded, explicit about its slice, stable under selection, and exposed
  through AX.
- Direction: integration → publication (limited transfer; the sync check also found an unrelated Chapter 08
  integration amendment, which was preserved and not overwritten).
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@fbfa6920`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@353d7c0`.
- Synchronized: 2026-08-10

## Previous synchronized change

- Change: **Chapter 53 — A Selection Snaps to Meaning.**
- The writer's report, on first using the pencil ch.52 introduced: her eyesight is not what it was and marking
  text is sometimes difficult. Not a preference and not an edge case — the surface asking a person to perform a
  fine motor task in order to express something coarse (*this bit matters*), then storing the fine motor task as
  though it were the meaning.
- The ruling: a selection that becomes a durable act is GROWN outward to the smallest unit of MEANING containing
  what she indicated — whole words always, the speech or stage direction or sentence when she has barely
  selected anything — chosen by what the text IS at that point rather than by generic punctuation, which is what
  makes it contextual rather than mechanical.
- The naive rule dies on this app's own shipped corpus. Measured over the last 400 lines of Ulysses: **27,287
  characters, one full stop, no question marks.** Penelope is unpunctuated by design, so "snap to the sentence"
  there selects the entire episode. So: grow to the nearest boundary the text DECLARES, parse it rather than ask
  a model (ch.27), measure it rather than conclude it (ch.29), and where the writing declares no boundary, stop
  at words and SAY SO rather than manufacture a grid (ch.50).
- The snap only ever grows, never shrinks and never moves off what she touched; it is shown before it is
  committed; a deliberate precise selection is honoured exactly; and no surface tells the writer her selection
  was wrong.
- New acceptance cases: Penelope is the fixture; a partial word never survives (property-tested); the snapped
  range always contains the raw range; dialogue, stage direction and verse each take their own unit; and
  evidence that seeds the store instead of performing the gesture does not satisfy the chapter.
- **Also in this sync, and not to be missed: chapter 45's amendment.** The reading column was set exactly as the
  specimen — a serif book face, 16.3pt, `line-height: 1.72`, a 64-character measure — built, rendered in the
  running app and looked at beside the Courier it replaced. The decision on seeing both was that the INSTRUMENT
  keeps its register: the writer is not consuming the manuscript on that page, she is marking it, selecting lines
  that become beats, composing against it, and monospace is what makes a manuscript legible AS MATERIAL. ch.45
  rule 4 stands; the amendment records where the book setting DOES belong — the export path, what leaves the
  workspace, where there is no editing, no Writing Tools and no accessibility drive to satisfy.
- Direction: integration -> publication (`Scripts/sync-integration-copy --pull`)
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/`
- Publication path: `docs/`
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@c147cc7d` (on `main`)
- Publication pull request: `https://github.com/Fountain-Coach/Reframe-Refactoring/pull/22` (merged)
- Governance first, per ch.07: the implementation follows this chapter, not the other way round.
- Synchronized: 2026-08-09

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

### 9.

- Change: Chapter 62, `Reframe Maintenance Control Plane`, plus its reading-index entry
- Direction: publication → integration (`Scripts/sync-integration-copy --push`)
- Publication path: `docs/62-reframe-maintenance-control-plane.md`
- Integration path: `apps/modernization-studio/docs/reframe-grounding-first-refactor/62-reframe-maintenance-control-plane.md`
- Status: synchronized working trees; counterpart commits will be recorded after both main-branch commits

### 10.

- Change: Chapter 62, `Reframe Maintenance Control Plane`, plus its reading-index entry
- Direction: publication → integration (`Scripts/sync-integration-copy --push`)
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@e2a1f6b`
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@d047292b`
- Synchronized: 2026-08-12

### 13.

- Change: Chapter 37 capability census and paid-first publication reconciliation
- Direction: integration → publication (`midi2-gpu-fabric` runtime copy → `docs/37-copilot-capability-governance.md`)
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@767f75ec0d969313586c55a75b6b9c10a054af9d`
- Publication projection commit: `Fountain-Coach/book-of-reframe@6c78d8d`
- Status: synchronized and pushed to the three main branches

### 11.

- Change: Chapter 62 amendment, `FountainMaintenanceKit — Portable Swift Maintenance Contract` (Chapter 63), and
  the Chapter 63 reading-index entry
- Direction: publication → integration (`Scripts/sync-integration-copy --push`)
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@92fa0e7`
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@60de3ed9`
- Synchronized: 2026-08-12

### 12.

- Change: Chapter 63 implementation-status correction: published `FountainMaintenanceKit@0.1.0` core/client/test-kit
  exists; hosted maintenance capability and adapters remain governed targets
- Direction: publication → integration (`Scripts/sync-integration-copy --push`)
- Publication content commit: `Fountain-Coach/Reframe-Refactoring@7f0a771`
- Integration content commit: `Fountain-Coach/midi2-gpu-fabric@3481ac4d`
- Synchronized: 2026-08-12
## Current planned change — Chapter 82 Remote MIDI2 Reading Room (2026-08-17)

- Change: **Chapter 82 — Remote MIDI2 Reading Rooms**, defining the useful multi-user product boundary over the
  existing MIDI2 peer infrastructure: shared semantic projections, human roles, writer authority, secure web
  transport, privacy, reconnect, and the first read-only acceptance gate.
- Direction: publication → integration (`Scripts/sync-integration-copy --push`).
- Publication content commit: pending.
- Integration content/provenance commit: pending synchronization.
- Claim boundary: governance and design reference only; no remote transport, authentication, or live multi-user
  acceptance is claimed by this chapter.
## Current planned change — Chapter 70 local AX/MIDI2 coordinator clarification (2026-08-18)

- Change: Chapter 70 now makes the Swift-owned local AX/MIDI2 coordinator explicit: one operation identity,
  execution identity, lifecycle projection, Store proof, and scenario evidence binding across local and external
  entry points.
- Claim boundary: governance clarification only. Reframe remains partially MIDI2-drivable; no runtime coordinator,
  full capability migration, or live acceptance is claimed.
- Direction: integration → publication (`Scripts/sync-integration-copy --pull`).
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@32e68292`.
- Publication commits: `Fountain-Coach/Reframe-Refactoring@3b4043a` and `Fountain-Coach/Reframe-Refactoring@11bd280`.
- Production result: release `release-20260818T153714Z` is live at `governance.fountain.coach`; the root,
  `/status-quo/`, Chapter 70, and Chapter 83 returned HTTPS 200 and Chapter 70 contains the coordinator section.
