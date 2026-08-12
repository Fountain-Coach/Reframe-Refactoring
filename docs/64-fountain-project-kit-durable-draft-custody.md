# FountainProjectKit — Durable Fountain Project Custody

> Chapter status: governing contract. This chapter defines the reusable Swift package that makes a Fountain
> Project durable while it is being written. It does not claim that the package or its Reframe integration is
> implemented until the acceptance gates below have evidence.

Chapter 60 names the Fountain editor as the writer's project surface. Chapter 61 names the round trip from a
published source through composition and later export. The missing seam is the package that keeps the writer's
unfinished project safe between those two moments. That seam must not be hidden in a SwiftUI view, a Copilot
transcript, a debounce task, or a Git checkout.

## The decision

Fountain-Coach owns a reusable Swift package:

```text
Fountain-Coach/FountainProjectKit
```

`FountainEditorKit` remains the editor surface: Fountain text editing, syntax presentation, outline utilities, and
editor accessibility. `FountainProjectKit` is the custody boundary around that surface: project identity, document
revision, durable writes, recovery, and explicit handoff. Reframe is a thin product adapter and Copilot remains the
writer-facing mediator.

```text
FountainEditorKit
        │ text changes
        ▼
FountainProjectKit ── FountainStoreSessionKit ── managed FountainStore
        │
        ├── recoverable working draft
        └── explicit export handoff → FountainGitAdapter → Book Library candidate
```

The working project is durable before it is published. It may be incomplete, unnamed beyond a generated working
title, or not yet suitable for review; none of those states permit discarding its text.

## Rules

1. **Creation is a persistence event.** A jump-start creates a named project identity and its initial Fountain
   document in the admitted managed FountainStore before the editor is presented as ready. A conversation turn or
   an in-memory binding is never the project record.

2. **Every accepted edit has a custody path.** The kit may coalesce writes for responsiveness, but it must expose an
   explicit flush operation. A transition, project switch, application suspension, termination request, or editor
   disappearance flushes the latest accepted text before releasing the project session. Cancelling a debounce task
   without flushing is a data-loss defect.

3. **The editor never owns persistence policy.** `FountainEditorKit` reports exact text changes. It must not invent
   project IDs, choose a store, publish a candidate, invoke Git, or silently rewrite Fountain text. The project kit
   owns write ordering, optimistic revision checks, conflict reporting, and recovery.

4. **One explicit store admission.** The project kit receives a `FountainStoreSessionKit`-admitted session or typed
   store client. It must not scan directories, guess a FountainStore, create a second lease, or use a parallel
   filesystem cache as authority.

5. **Identity is explicit and host-independent.** A project identity includes a stable project ID, corpus ID, source
   document ID, working revision, and creation/update receipts. It must not embed an IP address, absolute path,
   temporary directory, process ID, or Git checkout location.

6. **Working draft and publication are separate states.** A durable Reframe project is not a Book Library work, a Git
   commit, or a release. Publication requires an explicit Copilot-mediated handoff with a named export, provenance,
   review state, and candidate receipt. Closing Reframe never publishes implicitly and never deletes an unpublished
   draft.

7. **Recovery is a capability, not a hope.** The kit persists enough project identity for a later session to resolve
   and continue the draft. A recovery pointer is verified against the project and source document before it is offered
   to the writer. A stale pointer is reported and cleared without touching the underlying draft.

8. **Interruption is an ordinary state.** A crash, force quit, window removal, provider interruption, failed store
   write, or network-independent local suspension must leave the last acknowledged revision readable. The kit reports
   the last durable revision and any unsent in-memory edit; it never claims the latter was saved.

9. **Revision conflicts fail visibly.** A stale expected version cannot overwrite newer text. The kit returns a typed
   conflict with both project identity and durable revision; Reframe offers recovery or merge according to a later
   governed policy. Silent last-writer-wins is forbidden.

10. **Copilot wording names custody truth.** After jump-start, Copilot says that the project is saved as a Reframe
    working draft and that Book Library submission is a separate later action. It must not say merely “opening the
    editor” when persistence has already happened, and it must not imply publication.

11. **AX exposes the custody state.** The Reframe adapter exposes project identity, durable revision, save state,
    pending flush, conflict/error state, recovery action, and publication boundary through AX. A visual “saved” mark
    without a corresponding semantic value and FountainStore proof is not acceptance evidence.

12. **Git is an explicit downstream adapter.** Git may package or version an authored Fountain export after the writer
    asks for that handoff. It is not required for jump-start, editor autosave, interruption safety, or relaunch
    recovery. A Git failure cannot make the working draft unavailable.

13. **The kit is portable by injected authority.** The portable Swift core contains identity, revision, state, and
    receipt contracts. FountainStore access, clocks, scheduling, and export are injected adapters. macOS AppKit/SwiftUI
    integration belongs in a platform adapter; the core must remain deterministic and offline-testable.

14. **No prompt or manuscript leakage.** The kit does not persist prompts, provider context, secrets, unrestricted
    logs, or hidden transcript copies. It persists the project text and the minimum typed custody metadata required to
    recover and prove it.

## Package boundary

The initial package should provide:

- `FountainProjectCore` — project IDs, document revisions, custody states, typed errors, flush decisions, and receipts;
- `FountainProjectStore` — a protocol over the admitted FountainStore session for put/get/revision/recovery records;
- `FountainProjectSession` — creation, edit acknowledgement, coalesced persistence, explicit flush, interruption,
  and recovery operations;
- `FountainProjectExport` — an explicit, read-only handoff description for a later Fountain/Git adapter;
- `FountainProjectTestKit` — deterministic in-memory store, failure, interruption, conflict, and relaunch fixtures.

The kit may depend on the released Fountain-Store session contract. It must not depend on Reframe product models,
Copilot phrase matching, Book Library transport, or a Git executable. If editor UI conveniences are shared, they remain
in `FountainEditorKit` and are consumed by the Reframe adapter.

## Acceptance

The chapter is implemented only when all of these are proven:

1. A jump-start creates a FountainStore-backed project before the editor reports ready.
2. Creation, successive edits, a forced flush, and a failed write each produce deterministic typed outcomes.
3. A final edit survives editor disappearance and application termination without waiting for a long process to finish.
4. A fresh client on the same admitted store resolves the project and exact last durable text/revision.
5. A stale revision is rejected without overwriting the newer document.
6. AX exposes the same project identity, revision, save state, and recovery action that FountainStore proves.
7. Copilot clearly distinguishes “saved working draft” from “Book Library candidate.”
8. Git/export is absent from the jump-start path and works only through a later explicit handoff contract.
9. The package core and fixtures run offline; platform adapters and Reframe integration identify their exact package
   revisions and pass dependency-coherence and deprecated-surface gates.

**Governing sentence:** `FountainProjectKit` makes every writer edit durable in the admitted FountainStore before any
Git or Book Library handoff; `FountainEditorKit` renders and edits, Reframe mediates and projects, and publication is
always an explicit later transition.
