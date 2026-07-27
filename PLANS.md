# PLANS.md

This file records intent for multi-step or high-risk changes to the Reframe refactoring guide. It is not a runbook. Procedures belong in `.codex/skills/`.

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
