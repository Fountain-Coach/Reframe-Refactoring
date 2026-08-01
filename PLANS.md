# PLANS.md

This file records intent for multi-step or high-risk changes to the Reframe refactoring guide. It is not a runbook. Procedures belong in `.codex/skills/`.

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
