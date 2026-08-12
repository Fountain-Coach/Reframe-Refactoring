Title: Chapter 59 — The Fountain-Coach Git Library and Reframe Project Flow (2026-08-11)
Goal: Replace the GitHub-specific repository curation design with the Fountain-Coach-owned Git project service and
its Swift boundary, including Copilot project views, Library candidate/release flow, explicit authored export,
credential custody, accounting, migration, and acceptance.
Scope: `docs/59-copilot-initiated-library-curation.md`, `docs/01-reading-index.md`, exact integration mirror, and
reciprocal provenance.
Non-goals: GitHub App provisioning, GitHub credentials, runtime implementation, provider deployment, and live
acceptance; those follow the chapter.
Direction: integration → publication; exact transfer through `Scripts/sync-integration-copy --pull`.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@93c654f0`.
Validation: guide parity, relative-link review, and `git diff --check`.

Title: Open-Turn Mediation Protocol (2026-08-11)
Goal: Publish governance Chapter 58 and its reading-index entry from the integration repository.
Scope: `docs/58-open-turn-mediation-protocol.md`, `docs/01-reading-index.md`, exact integration mirror, reciprocal provenance.
Non-goals: runtime implementation, provider deployment, or live-acceptance claims.
Direction: integration → publication; manual exact transfer because `Scripts/sync-integration-copy` is absent in this checkout.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@3ac6a135`.
Validation: relative links, `git diff --check`, and byte parity for the transferred files.

Title: Chapter 57 — The writer enters by intention (2026-08-10)
Goal: Publish the governance contract for a new Reframe landing where writers begin with an intention and the
on-device Copilot discovers the live Book Library without requiring provider IDs.
Scope: `docs/57-the-writer-enters-by-intention.md`, `docs/01-reading-index.md`, exact integration mirror, and
reciprocal provenance.
Non-goals: landing implementation, catalog-search capability binding, AX implementation, visual redesign, and live
acceptance; those follow the chapter.
Plan:
- Step 1 (completed) - Read ch.07, ch.08, ch.15, ch.18, and ch.25 and record their binding rules in the integration
  plan.
- Step 2 (completed) - Draft Chapter 57 with the intention-led landing, on-device discovery, internal-ID boundary,
  and separate AX/VRT acceptance gates.
- Step 3 (completed) - Push integration commit `3271f90f` on `main`.
- Step 4 (completed) - Transfer the exact chapter and index entry to this publication repository; preserve unrelated
  guide content while synchronizing the previously identified integration drift.
- Step 5 (pending) - Commit and push the publication mirror, then record the reciprocal publication commit.

Title: Chapter 56 — The Book Library is a portable source provider (2026-08-10)
Goal: Publish the governance contract for a separately hosted curated source provider that Reframe can use beside
DraCor and local files, with item-level provenance, generated OpenAPI, withdrawal switches, and migration to another
IP or host without changing Reframe.
Scope: `docs/56-the-book-library-is-a-portable-source-provider.md`, `docs/01-reading-index.md`, exact integration
mirror, and reciprocal provenance.
Non-goals: the external repository, server implementation, content selection, DNS/HTTPS deployment, Reframe client,
and live acceptance; those follow the chapter.
Plan:
- Step 1 (completed) - Read the binding governance and record the rules in the integration plan.
- Step 2 (completed) - Draft Chapter 56 and its integration reading-index entry.
- Step 3 (completed) - Push integration commit `fc40c88c` on `main`.
- Step 4 (completed) - Transfer the exact chapter to this publication repository and record provenance.
- Step 5 (completed) - Publication commit `da992f7` pushed to `main`; importer/promotion control is now part of the
  governing chapter and remains an implementation obligation in the provider repository.

Title: The pencil belongs to the writer (2026-08-08)
Goal: Publish the governance contract for marks made ON the manuscript, so the app can never wear the appearance
of having attended to a page it has only finished reading, and so the writer's own pencil is not interpreted.
Scope: `docs/52-the-pencil-belongs-to-the-writer.md`, `docs/01-reading-index.md`, `docs/README.md`, exact
integration mirror, reciprocal provenance.
Non-goals: the two visual languages themselves, the writer-mark capture surface, drawing the citation in the text.
Plan:
- Step 1 (completed) - Measured the collision: an underline already meant three things here (claim evidence,
  read-through progress, the new anchor), with the CoPilot's own help text spending a paragraph warning writers
  not to confuse them, and `BaselineViews.evidenceTint` surviving with nothing mounting the view.
- Step 2 (completed) - Measured the anchor on a live on-device Circe run: 13 of 15 windows anchored, threads
  running 20608→20815 against anchors of 15–86 lines, one thread opening 95 lines into its own passage.
- Step 3 (completed) - Drafted chapter 52 with nine rules, seven prohibitions and six acceptance cases, naming
  the machine's mark a CITATION (ch.40) and leaving the pencil to the writer (ch.46).
- Step 4 (completed) - Pulled into publication; `--check` reports no differences.
---
Title: One decision decides the lane (2026-08-07)
Goal: Publish the governance contract for lane resolution, so no part of Reframe can size a window for one lane
and spend on another, and no sentence about a lane costs the writer their password.
Scope: `docs/51-one-decision-decides-the-lane.md`, `docs/01-reading-index.md`, `docs/README.md`, exact integration
mirror, reciprocal provenance.
Non-goals: the resolver implementation, the gating kit, migrating the four call sites that answer the question today.
Plan:
- Step 1 (completed) - Measured four disagreeing answers on one page, and three further incidents from the same fault.
- Step 2 (completed) - Drafted chapter 51 with ten rules and five acceptance cases.
- Step 3 (completed) - Pulled into publication; `--check` reports no differences.
- Step 4 (completed) - Opened publication pull request #20 and recorded it here and in SOURCE.md.
---
Title: Chapter 50 amended — a unit is a range, not a copy (2026-08-07)
Goal: Reconcile chapter 50 with chapters 13 and 29 so no chapter has to be wrong, and record that the first draft
was written on top of an existing breach rather than noticing it.
Scope: `docs/50-text-is-stored-so-it-can-be-pointed-at.md`, `docs/01-reading-index.md`, `docs/README.md`, exact
integration mirror, reciprocal provenance.
Non-goals: the partitioning implementation, moving the source out of the store, generating the OpenAPI projection.
Plan:
- Step 1 (completed) - `governance-read` resolved ch.13 and ch.29 alongside ch.50 and found them in conflict.
- Step 2 (completed) - Raised the conflict to the writer before implementing; resolution: layer them.
- Step 3 (completed) - Amended the chapter, rule 3, and the acceptance cases; corrected the index row and pointer.
- Step 4 (completed) - Pulled into publication; `--check` reports no differences.
---
Title: Text is stored so it can be pointed at (2026-08-07)
Goal: Publish the governance contract for how local text content is stored and fetched, so a client commanded to
select a chapter fetches that chapter and nothing else.
Scope: `docs/50-text-is-stored-so-it-can-be-pointed-at.md`, `docs/01-reading-index.md`, `docs/README.md`, the
carried chapter 20 custody section, exact integration mirror, and reciprocal provenance.
Non-goals: partitioning the stored source, changing FountainStore, generating the OpenAPI projection, or any
runtime read-path implementation.
Plan:
- Step 1 (completed) - Research the Fountain Coach OpenAPI history: the FountainStore declared API already serves
  prefix/range scans with paging, `schema/idl.yaml` already declares `screenplay/lines.get` with a range and a
  65,536-byte budget, and ch.49 already rules that an operation is defined once and projected by generation.
- Step 2 (completed) - Measure the defect in the writer's own store: one record, 1,519,413 characters, 32,694
  lines; Circe at 20,051-25,573 reachable only by fetching the whole book.
- Step 3 (completed) - Draft chapter 50 with ten rules and four acceptance cases, and its reading-index row.
- Step 4 (completed) - Pull the exact guide copy into publication; `--check` reports no differences.
- Step 5 (completed) - Opened publication pull request #18 and recorded it here and in SOURCE.md.
---
Title: Situated, mixed-initiative interaction (2026-08-04)
Goal: Publish the governance contract for Reframe as an open interaction space in which human turns may be corrective,
interrupted, out of sequence, or unrelated, while only grounded live state and one mediated meaning may authorize a
persisted transition.
Scope: `docs/47-situated-mixed-initiative-interaction.md`, `docs/01-reading-index.md`, exact integration mirror, and
reciprocal provenance.
Non-goals: runtime implementation, new capability identities, provider policy, or release promotion.
Plan:
- Step 1 (completed) - Read the binding chapters and record their rules in the integration plan.
- Step 2 (completed) - Draft Chapter 47 and its reading-index entry in the integration guide.
- Step 3 (completed) - Pull the exact guide copy into publication and resolve the pre-existing 01/45 merge drift
  toward the documented integration-side version.
- Step 4 (completed) - Record reciprocal commits, validate links/parity/provenance, and prepare reviewed publication
  commits.
Validation:
- Publication and integration chapter copies are byte-identical.
- `Scripts/sync-integration-copy --check <integration>` passes.
- Relative links, `git diff --check`, and repository-specific publication checks pass.
- This chapter does not claim runtime or live acceptance; those remain in the integration phase plan.
- Integration commit: `Fountain-Coach/midi2-gpu-fabric@c33615ad`.
- Publication commit: `Fountain-Coach/Reframe-Refactoring@688a200`.
- Draft publication PR: `Fountain-Coach/Reframe-Refactoring#9`.
- Draft integration PR: `Fountain-Coach/midi2-gpu-fabric#23`.

---

Title: Define the released Reframe surface (2026-08-03)
Goal: Separate development command inventory, governed capabilities, live acceptance, and the named-build release allow-list.
Scope: `docs/43-the-released-surface-is-a-named-build.md`, `docs/01-reading-index.md`, the exact integration mirror, and reciprocal provenance.
Non-goals: declaring a shipped version, promoting development capabilities, or changing runtime behavior.
Plan:
- Step 1 (status: completed) - Add chapter 43 and the release/publication reading path.
- Step 2 (status: pending) - Synchronize the exact chapter and index into the integration guide and record both counterparts.
Validation:

---

Title: Publish Chapter 46 — Dynamic Grounding (2026-08-04)
Goal: Publish the governance decision that Grounding is a dynamic, source-authoritative flow rather than a workspace.
Scope: `docs/46-dynamic-grounding.md`, `docs/01-reading-index.md`, and the synchronized publication copies of chapters
44/45.
Non-goals: runtime implementation or live acceptance of `/ground`.
Plan:
- Step 1 (status: completed) - Compare the integration and publication guide copies.
- Step 2 (status: completed) - Pull the intentional integration changes with `Scripts/sync-integration-copy --pull`.
- Step 3 (status: completed) - Record reciprocal provenance and validate parity and whitespace.
Validation:
- Integration governance PR: `Fountain-Coach/midi2-gpu-fabric#22`.
- Counterpart integration commit: `aeb03ce3`.
- `Scripts/sync-integration-copy --check` and `git diff --check` must pass before publication.
- The publication and integration chapter copies are byte-identical.
- Relative links, `git diff --check`, and the sync script pass.
- The release manifest explicitly says `no-released-build` until a named distribution build exists.

# PLANS.md

## Sync — Chapter 61: The Fountain Project Round Trip (2026-08-11)

Title: Synchronize the closing Fountain Project lifecycle chapter from the integration copy.
Goal: make the Library → Reframe → Compose → Fountain Project → Git → Library loop explicit without collapsing
authority boundaries or claiming a complete implementation.
Scope: `docs/61-the-fountain-project-round-trip.md`, `docs/01-reading-index.md`, and reciprocal provenance.
Direction: integration → publication, selected after `Scripts/sync-integration-copy --check` identified only these
two guide changes.
Non-goals: runtime round-trip implementation, repository provisioning, candidate promotion, or live acceptance.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@6e352a82`.
Validation: guide parity and `git diff --check` must pass in both repositories.

## Sync — Chapter 60: The Fountain Editor Is the Project Surface (2026-08-11)

Title: Synchronize the Fountain editor/project-surface governance chapter from the integration copy.
Goal: publish the decision that Reframe is the Fountain editor and Copilot mediator, while managed Git versions and
transports projects and the Book Library owns publication.
Scope: `docs/60-the-fountain-editor-is-the-project-surface.md`, `docs/01-reading-index.md`, and reciprocal provenance.
Direction: integration → publication, explicitly selected after `Scripts/sync-integration-copy --check` identified
only these two guide changes.
Non-goals: runtime implementation, repository provisioning, writable editor implementation, or live acceptance.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@f72483e8`.
Validation: guide parity and `git diff --check` must pass in both repositories; skill synchronization remains a
pre-existing integration-repository drift and is not part of this documentation transfer.

## Sync — Chapter 54: The Writer Does Not Manage the Projection

Title: Synchronize governance Chapter 54 from the integration copy.
Goal: publication `docs/` carries the exact writer-facing projection and command-seam contract authored beside the
implementation.
Scope: `docs/54-the-writer-does-not-manage-the-projection.md` and its `docs/01-reading-index.md` row.
Non-goals: do not overwrite the unrelated Chapter 08 integration drift; no runtime implementation or live-acceptance
claim.
Direction: integration → publication, limited to the two changed guide files.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@fbfa6920`.
Publication commit: `Fountain-Coach/Reframe-Refactoring@353d7c0`.
Validation: chapter links resolve, `git diff --check` passes, and the remaining parity difference is the pre-existing
integration-only Chapter 08 amendment, intentionally excluded from this sync.

Title: Public publication and private source policy (2026-08-03)
Goal: Establish the FCIS-governed boundary between public projections, public governance, and private runtime source.
Scope: `docs/44-publication-and-source-policy.md`, reading index, README, exact integration mirror, org FCIS policy,
the Book projection, and runtime links.
Non-goals: changing repository visibility, publishing runtime source, changing release status, or changing runtime
behaviour.
Plan:
- Step 1 (status: in progress) - Publish the governing policy and its reading path.
- Step 2 (status: pending) - Synchronize the integration copy and add the appropriate public/private projections.
- Step 3 (status: pending) - Validate links, parity, FCIS layers, and repository visibility statements; open reviewed PRs.
Validation:
- Publication and integration chapter copies are byte-identical.
- Public links resolve; the private runtime is named with an explicit access note rather than a misleading public link.
- `git diff --check` and repository-specific FCIS validation pass.
- PRs: org FCIS `#4`, governance `#7`, runtime `#21`, Book `#9`.
- Chapters read: 07 (plan and source authority), 08 (separate AX/VRT/store evidence), 43 (named-build release boundary),
  and 44 (public projections/private implementation).
- What they forbid here: treating a command catalog, screenshot, or public link as a release or as permission to expose
  runtime source; collapsing governance, runtime, acceptance, and release authorities.
- Conflicts: none; the user's request to publish the policy is consistent with keeping the runtime private by default.
- Excluded, and why: repository-visibility change, runtime implementation, and release allow-list changes are separate
  decisions governed by Chapter 44 and were not authorized by this publication task.

This file records intent for multi-step or high-risk changes to the Reframe refactoring guide. It is not a runbook. Procedures belong in `.codex/skills/`.

Title: Copilot reading surface and typography (2026-08-03)
Goal: Publish the approved governance chapter defining a situated, legible, Reframe-native Copilot surface and its
acceptance boundary.
Scope: `docs/45-copilot-reading-surface-and-typography.md`, its two design-review illustrations, the reading index,
the exact integration mirror, and reciprocal provenance.
Non-goals: publishing runtime source, declaring a released App surface, or changing capability policy.
Plan:
- Step 1 (status: completed) - Read the binding surface, Copilot, validation, and capability-governance chapters;
  generate and review the two illustrations before implementation.
- Step 2 (status: completed) - Implement the approved reading surface and repair the activity-disclosure crash in the
  integration repository; validate build, focused tests, AX disclosure, and window-ID evidence.
- Step 3 (status: completed) - Transfer the exact chapter and illustrations integration → publication, update the
  reading index, and record reciprocal commit provenance.
Validation:
- Publication and integration chapter copies are byte-identical; illustration assets are byte-identical.
- `StudioThemeContrastAuditTests` (2), `StudioChatPanelRenderingTests` (3), product build, and `git diff --check`
  pass.
- AX opened `copilot-activity-details`; the managed app remained alive and the bounded history surface appeared.
- The chapter remains governance/design guidance; it does not claim a released App capability.


---

Title: Chapter 36 — every gap keeps its address (2026-07-31)
Goal: Publish and synchronize the governance for representing an open-ended collection of uncertainty ledgers without flattening it into fixed lanes or detached chat cards.
Scope: `docs/36-every-gap-keeps-its-address.md`, `docs/README.md`, `docs/01-reading-index.md`, their exact integration mirror, reciprocal provenance, and documentation validation.
Non-goals: Reframe runtime implementation, a fixed ledger taxonomy, automatic lane ranking, changes to the MIDI/telemetry contract, or moving Reframe domain types into UncertaintyScoreKit.
Constraints: every gap keeps composite lane/note identity; producer lane order and arbitrary cardinality survive presentation; the generic kit owns map navigation while Reframe owns typed wants and evidence; visual and AX truth agree; synchronization direction is integration to publication (`--pull`).
Risks: a polished mock can silently reinstate enumerated lanes, collapse detail into an executive summary, confuse uncertainty lanes with Score participants, or let chat become the state store; mitigate with explicit rules, generated large-lane acceptance, a generic-kit/host boundary, and parity checks.
Plan:
- Step 1 (status: completed) - Compare the publication and integration guide and review every difference.
- Step 2 (status: completed) - Pull the intended integration guide into publication, then create separate, narrowly scoped commits and draft PRs in both repositories.
- Step 3 (status: completed) - Recheck byte parity, relative links, shell syntax, whitespace, staged scope, and reciprocal PR provenance.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports parity.
- Every relative Markdown link in the guide resolves.
- `sh -n Scripts/sync-integration-copy` and `git diff --check` pass.
- Both PRs contain only the chapter-36 guide change and synchronization governance; unrelated Reframe implementation work remains unstaged.
Results:
- Integration counterpart: `Fountain-Coach/midi2-gpu-fabric@cfeaa2c1`, draft PR `#9`.
- The publication and integration worktrees contain the same 37-file guide; relative links, sync-script syntax and `git diff --check` pass.

---

Title: Chapter 32 store-native research compiler (2026-07-30)
Goal: Extend Referenced Knowledge so web retrieval and frontier reasoning enlarge the manuscript's durable corpus without creating a second knowledge plane beside FountainStore.
Scope: `docs/32-referenced-knowledge.md`, its exact integration mirror, reciprocal provenance, and documentation validation.
Non-goals: Reframe runtime implementation, provider selection, new IDL topics, automatic web access, or treating external material as authority over the manuscript.
Constraints: FountainStore remains the operational account of knowledge and uncertainty; retrieval is persisted before interpretation; frontier models compile stored evidence rather than supply citations from memory; all artefacts remain typed, evidenced, historied, removable, narrowly invalidated, and non-authoritative about meaning; numeric measurements remain telemetry only.
Risks: a broad "knowledge base" can launder transient web material into project truth, repeat paid research, or let an embedding/index become authority; mitigate with separately owned artefacts, persist-before-interpret, store-first lookup, typed promotion, conflict preservation, and removal/replay tests.
Plan:
- Step 1 (status: completed) - Recorded the doctrine and pragmatic artefact flow in chapter 32 without deleting or weakening its existing rules.
- Step 2 (status: completed) - Synchronized the exact chapter into `Fountain-Coach/midi2-gpu-fabric`.
- Step 3 (status: completed) - Validated byte parity, relative Markdown links, whitespace, file modes and staged scope; recorded the integration counterpart before publishing both `main` branches.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports parity.
- Every relative Markdown link in the guide resolves.
- `git diff --check` passes in both repositories.
- The integration commit contains only `PLANS.md` and the mirrored chapter; implementation work remains untouched.
Results:
- Integration counterpart commit: `Fountain-Coach/midi2-gpu-fabric@7ffd4166`.
- Chapter copies have SHA-256 `c34bd823e3bc16e731ab4b182ac0511326ed0357e19548721d310188dfe7fb93`.

---

Title: Live-drive display policy synchronization (2026-07-26)
Goal: Publish the operational evidence rules for a Reframe live drive, including full-screen launch on the attached display, and synchronize them to the integration guide.
Scope: `AGENTS.md`, validation guidance, and the exact integration guide mirror.
Non-goals: Reframe runtime changes, demo-store changes, or edits to unrelated integration worktree files.
Constraints: keep AGENTS declarative; preserve AX as interaction authority, window-ID screenshots as visual evidence, and FountainStore as behavioural truth; do not guess display numbers or coordinates.
Risks: a generic GUI-testing rule could hide the multi-display requirement; mitigate by making the display target, full-screen transition, and window-ID verification explicit.
Plan:
- Step 1 (status: completed) - Updated governance invariants and the validation chapter.
- Step 2 (status: completed) - Pushed the publication guide into the integration mirror and rechecked parity.
- Step 3 (status: completed) - Validated Markdown and Git hygiene, committed each repository separately, and pushed only the dedicated governance repository.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports parity.
- Relative Markdown links, `sh -n Scripts/sync-integration-copy`, and `git diff --check` pass.
- Staged paths exclude unrelated implementation edits in the integration worktree.

---

Title: Initial FCIS-compliant publication (2026-07-19)
Goal: Publish the complete Grounding-first Reframe refactoring guide in a dedicated Fountain Coach repository and establish reciprocal provenance with its integration copy.
Scope: guide chapters, repository landing page, source contract, FCIS layers, synchronization skill and script, validation, and GitHub publication.
Non-goals: implementing the Reframe runtime refactor, changing the MIDI backplane IDL, mutating FountainStore, or deleting legacy index artifacts.
Constraints: preserve exact guide content; keep AGENTS declarative, plans intentional, and procedures in skills; keep MCP optional; create no new dependency.
Risks: two copies can drift or claim conflicting authority; mitigate with explicit roles, exact provenance, a read-only default sync check, and counterpart links in every publication change.
Plan:
- Step 1 (status: done) - Import the committed integration guide into `docs/`.
- Step 2 (status: done) - Add FCIS-compliant repository layers and synchronization ownership.
- Step 3 (status: done) - Validate content parity, links, shell syntax, and repository hygiene.
- Step 4 (status: done) - Publish the private Fountain Coach repository and verify reciprocal links.
Validation:
- Every guide chapter exists under `docs/` and relative Markdown links resolve.
- `Scripts/sync-integration-copy --check <integration-checkout>` reports no difference.
- `sh -n Scripts/sync-integration-copy` passes.
- `git diff --check` passes.

Results:
- Published privately at `https://github.com/Fountain-Coach/Reframe-Refactoring` with `main` as the default branch.
- Recorded the integration source at `midi2-gpu-fabric` commit `da22ba0c54e0fff6fb44f66182cecab0dd18759e` and draft PR `#8`.
- Confirmed guide parity, relative links, synchronization-script syntax, and Git whitespace hygiene.

---

---

Title: Publish the Copilot Capability Audit skill (2026-08-01)
Goal: Synchronize Chapter 38 and its reading-index entry from the integration repository into the publication guide,
preserving the evidence-backed capability boundary and reciprocal provenance.
Scope: `docs/38-copilot-capability-audit-skill.md`, `docs/01-reading-index.md`, `SOURCE.md`.
Non-goals: runtime implementation, registry changes, or copying unrelated historical chapter drift.
Plan:
- Step 1 (status: completed) - Compare publication and integration guide copies with `Scripts/sync-integration-copy --check`.
- Step 2 (status: completed) - Pull the intended integration chapter set, retain only Chapter 38 and its index entry,
  and restore unrelated publication drift.
- Step 3 (status: completed) - Record reciprocal source provenance and verify guide parity.
Validation:
- `Scripts/sync-integration-copy --check /Volumes/NINJA2/Github-Desktop/midi2-gpu-fabric` reports synchronized copies.
- `git diff --check` passes.
- Integration counterpart: `Fountain-Coach/midi2-gpu-fabric@37231c2e`.

---

Title: Refactor Chapter 38 — complete Copilot capability skill suite (2026-08-01)
Goal: Publish the refactored governance chapter describing the complete skill suite, widening workflow, evidence contract,
and Codex↔Claude synchronization.
Scope: `docs/38-copilot-capability-audit-skill.md`, `SOURCE.md`.
Non-goals: runtime implementation or capability-registry changes.
Plan:
- Step 1 (status: completed) - Compare publication and integration copies with `Scripts/sync-integration-copy --check`.
- Step 2 (status: completed) - Pull the refactored integration Chapter 38 and restore unrelated historical guide drift.
- Step 3 (status: completed) - Record reciprocal provenance and verify parity and whitespace hygiene.
Validation:
- `Scripts/sync-integration-copy --check /Volumes/NINJA2/Github-Desktop/midi2-gpu-fabric` reports synchronized copies.
- `git diff --check` passes.
- Integration counterpart: `Fountain-Coach/midi2-gpu-fabric@633d110c`.

---

Title: Publish the pipeline status widening update (2026-08-01)
Goal: Keep Chapter 38 aligned with the first governed capability widening slice.
Scope: `docs/38-copilot-capability-audit-skill.md`, `SOURCE.md`.
Plan:
- Step 1 (status: completed) - Compare publication and integration guide copies.
- Step 2 (status: completed) - Pull the updated Chapter 38 and restore unrelated publication drift.
- Step 3 (status: completed) - Record reciprocal provenance and verify parity.
Validation:
- `Scripts/sync-integration-copy --check /Volumes/NINJA2/Github-Desktop/midi2-gpu-fabric` reports synchronized copies.
- `git diff --check` passes.
- Integration counterpart: `Fountain-Coach/midi2-gpu-fabric@77c62a45`.

---

Title: Publish the ch.26 execution record (2026-07-27)
Goal: Restore publication/integration parity for chapter 26 after its retirement log was written in the integration mirror only, and record what executing the chapter actually produced.
Scope: `docs/26-internals-tune-themselves.md`.
Non-goals: Reframe runtime changes, edits to other chapters, or re-litigating the ch.26 disposition procedure itself.
Constraints: preserve the chapter's existing doctrine sections unchanged — the added material is an execution log and an open-debt table, not a change of intent; name the counterpart commit in both repositories; keep the audit's drift-vector-1 closed by publishing in the same session the divergence was found.
Risks: an execution record can be mistaken for doctrine and then "maintained" as intent; mitigate by keeping it under an explicitly named retirement-log heading, separate from the decision and acceptance sections.
Plan:
- Step 1 (status: completed) - Detected the drift with `Scripts/sync-integration-copy --check` (chapter 26 only).
- Step 2 (status: completed) - Transferred the integration chapter into `docs/` with an explicit direction (--pull).
- Step 3 (status: completed) - Re-ran the parity check and committed in both repositories naming the counterpart.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports parity.
- `git diff --check` passes in both repositories.
- Counterpart integration commit: `31459df4a9acab9574fab5bbce35cadfa8ebb43e`.


## Plan template

Title:
Goal:
Scope:
Non-goals:
Constraints:
Risks:
Plan:
Validation:

## Sync — chapter 48 (a service is a fact, not a symptom)

Title: Synchronize governance chapter 48 from the integration copy
Goal: Publication `docs/` carries the chapter authored beside the implementation, with reciprocal provenance.
Scope: `docs/48-a-service-is-a-fact-not-a-symptom.md`, `docs/01-reading-index.md`, `SOURCE.md`.
Non-goals: No implementation. The chapter is governance first (ch.07); the code that satisfies it lands separately.
Plan:
- Step 1 (status: completed) - `Scripts/sync-integration-copy --check` reported exactly two differences, both new
  and both authored in the integration copy: the chapter file and its reading-index row. No unrelated drift.
- Step 2 (status: completed) - Transferred with an explicit direction (--pull), integration → publication.
- Step 3 (status: completed) - Re-ran the parity check and validated the chapter's six cross-references resolve.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports `guide copies are synchronized`.
- `git diff --check` passes in both repositories.
- All six relative links in chapter 48 resolve inside `docs/`.
- Counterpart integration commit: `200a431f` (merge of Fountain-Coach/midi2-gpu-fabric#34 to `main`).

## Sync — chapter 48 binding contract, chapter 40 reading surface

Plan:
- Step 1 (status: completed) - `--check` reported three differing files, all authored in the integration copy.
  Reviewed each: index and ch.40 purely additive; ch.48 additive plus a deliberate REMOVAL of the hand-written
  service register, confirmed line by line before transfer so the pull could not destroy unrelated work.
- Step 2 (status: completed) - Transferred with an explicit direction (--pull), integration → publication.
- Step 3 (status: completed) - Re-ran parity; validated every relative link in both amended chapters.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports `guide copies are synchronized`.
- `git diff --check` passes in both repositories.
- Counterpart integration commit: `a80916b2` (merge of Fountain-Coach/midi2-gpu-fabric#35 to `main`).

## Sync — chapter 49 (one definition, two projections)

Plan:
- Step 1 (status: completed) - `--check` reported the new chapter plus two amended files. Reviewed each: index
  purely additive; ch.48's single publication-only line was a line-split introducing the ch.49 cross-reference,
  confirmed before transfer so the pull could not discard prose.
- Step 2 (status: completed) - Transferred with an explicit direction (--pull), integration → publication.
- Step 3 (status: completed) - Re-ran parity; every relative link in ch.49 resolves; every chapter is indexed.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports `guide copies are synchronized`.
- `git diff --check` passes in both repositories.
- Counterpart integration commit: `d2fc4ea7` (merge of Fountain-Coach/midi2-gpu-fabric#36 to `main`).

## Sync — chapter 49 amendment (MIDI-CI binding; the web speaks midi2 by choice)

Plan:
- Step 1 (status: completed) - `--check` reported two amended files. Reviewed: the publication-only lines were
  exactly the superseded chapter summary and principle text, confirmed before transfer.
- Step 2 (status: completed) - Transferred with an explicit direction (--pull), integration → publication.
- Step 3 (status: completed) - Re-ran parity; links resolve; every chapter indexed.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports `guide copies are synchronized`.
- `git diff --check` passes in both repositories.
- Counterpart integration commit: `cfa49cfe` (merge of Fountain-Coach/midi2-gpu-fabric#37 to `main`).

## Sync — chapter 49 correction (the definition is the manifest)

Plan:
- Step 1 (status: completed) - `--check` reported ch.49 and the index. Reviewed: the 14 publication-only lines
  were exactly the superseded summary and rule 1, confirmed before transfer.
- Step 2 (status: completed) - Transferred with an explicit direction (--pull), integration → publication.
- Step 3 (status: completed) - Re-ran parity; links resolve.
Validation:
- `Scripts/sync-integration-copy --check <integration-checkout>` reports `guide copies are synchronized`.
- Counterpart integration commit: `393b15f8` (merge of Fountain-Coach/midi2-gpu-fabric#39 to `main`).

## Chapter 62 — Reframe Maintenance Control Plane

Plan:
- Step 1 (status: completed) - Resolve the maintenance/API, Preferences, SecretStore, deployment, promotion,
  rollback, migration, and remote-host boundary through Chapters 07, 08, 56, 59, and 61; record the implementation
  boundary before editing.
- Step 2 (status: completed) - Add the publication chapter and reading-index entry. The chapter defines the
  authenticated maintenance control plane without claiming runtime implementation.
- Step 3 (status: completed) - Synchronize the publication chapter and guide index into the integration repository
  with the explicit `Scripts/sync-integration-copy --push` direction.
- Step 4 (status: completed) - Commit and push the publication and integration repositories to their `main` branches;
  record both commits reciprocally (`Reframe-Refactoring@e2a1f6b`, `midi2-gpu-fabric@d047292b`).

Validation:
- `Scripts/sync-integration-copy --check /Volumes/NINJA2/Github-Desktop/midi2-gpu-fabric`
- `git diff --check` in both repositories.
- No implementation or live-acceptance claim belongs in this chapter change.

## Chapter 62 amendment and Chapter 63 — Portable Swift maintenance boundary

Plan:
- Step 1 (status: completed) - Resolve the portable maintenance boundary through Chapters 07, 08, 56, and 62:
  portable Swift owns the control-plane contract; SecretStore and host facilities remain explicit adapters.
- Step 2 (status: completed) - Amend Chapter 62 with the declared-profile portability doctrine and add Chapter 63,
  the proposed `Fountain-Coach/FountainMaintenanceKit` package contract. Update the reading index.
- Step 3 (status: completed) - Synchronize the publication chapter and index into the integration repository with the
  explicit `Scripts/sync-integration-copy --push` direction.
- Step 4 (status: completed) - Commit and push both repositories on `main`, then record reciprocal provenance and
  revalidate parity and clean worktrees.

Boundary:
- Governance only. No Swift package, server adapter, Reframe capability, SecretStore integration, or live-acceptance
  claim is included in this tranche.

Provenance:
- Publication content/provenance commit: `Reframe-Refactoring@92fa0e7`.
- Integration content/provenance commit: `midi2-gpu-fabric@60de3ed9`.

## Chapter 63 implementation-status correction (2026-08-12)

**Reason:** the first FCIS Kit release now exists and Reframe resolves it remotely, so Chapter 63's statement that the
package did not exist became stale.

**Change:** update Chapter 63 to distinguish the implemented `FountainMaintenanceKit@0.1.0` core/client/test-kit
release from the still-unimplemented native Git, hosted server, SecretStore adapter, and full acceptance gates.

**Validation:** synchronize publication → integration, run parity and link checks, and record the resulting commits.

**Provenance:** publication content commit `Reframe-Refactoring@7f0a771`; integration content commit
`midi2-gpu-fabric@3481ac4d`.
Title: Library-rooted reading boundary and citation evidence bundle (2026-08-12)
Goal: Publish the revised Chapter 56 reading boundary and Chapter 40 evidence-bundle rule: Book Library is the sole
Reframe reading provider; WebKit may render only the exact retrieved citation evidence, never an interactive browser.
Scope: `docs/01-reading-index.md`, chapters 40, 45, 56, and 58, exact integration mirror, reciprocal provenance.
Non-goals: runtime web-source removal, bounded research implementation, generated contract changes, and live acceptance;
those remain the next implementation tranche.
Direction: integration → publication; exact transfer through `Scripts/sync-integration-copy --pull`.
Integration commit: `Fountain-Coach/midi2-gpu-fabric@71136ea2`.
Publication commit: pending.
Validation: 93 focused Reframe tests, dependency coherence, deprecated reader-surface check, guide parity, and
`git diff --check`.
