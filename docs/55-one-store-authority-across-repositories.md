# One Store Authority Across Repositories

> Chapter summary: A FountainStore is an identified authority with a lifecycle, not a directory Reframe happens to
> open. Every process must receive the same explicit, verified store receipt from the shared Swift authority.

Reframe has had several names for the place where its state lives: the managed library, a working store, a fixture,
a temporary drive, and sometimes simply a path in the environment. Those names were useful locally and dangerous
together. A directory can exist without a FountainStore being ready. A previous build can be resumed from the right
store or accidentally paired with a different one. A test can create a fresh store while the GUI opens the writer's
library. A shell can print one path while the application resolves another.

This chapter establishes one boundary across repositories. Fountain-Store owns the generic authority for store
identity, readiness, leasing, recovery, and receipts. Reframe owns the meaning of a store selection in its product:
writer library, fresh live drive, named manuscript fixture, or resume of a prior run. Neither layer guesses among
directories.

## The decision

The store-selection authority is a Swift API in the Fountain-Store package. The Reframe launcher, the Reframe app,
tests, live-drive tools, and future clients use that authority rather than independently interpreting paths,
environment variables, configuration files, or filesystem recency.

The shared API is generic. It does not know what Circe, a paid lane, or a Reframe corpus means. Reframe supplies an
explicit intent and its product-specific readiness requirements. The shared API returns a receipt that both the
launcher and the application validate before a process may open the store.

## Rules

1. **A store choice is an intent, not an inferred path.** A caller must name `fresh`, `resume`, `explicit`, or the
   protected writer library. No automated or live-drive caller may omit the intent and receive a guessed store.

2. **The shared Swift authority is the only selector.** Shell launchers may adapt command-line arguments into the
   API, but they may not independently canonicalize, initialize, lease, or select a store.

3. **The generic library never scans for a likely store.** It accepts an explicit URL or an application-owned alias
   resolution. It must not choose the newest directory, the largest directory, a directory found by `find`, or a
   path remembered only in a log.

4. **Fresh means isolated and unambiguous.** A fresh request creates a unique store identity, refuses to reuse an
   existing path, initializes the required store metadata, and returns a receipt before the client opens it.

5. **Resume means the same identity.** A resume request resolves an explicit registered alias or path, validates
   its manifest and compatibility, and preserves its documents, corpus scope, run lineage, and receipts. A newer
   executable does not by itself justify a new store.

6. **A writer library is protected.** The writer's canonical library is never a disposable fixture. Opening it
   requires an explicit product-level intent and must be visible in the receipt. Fresh-drive cleanup must never
   target it.

7. **A directory is not readiness.** The authority distinguishes `fresh`, `ready`, `incomplete`, `incompatible`,
   `corrupt`, and `leased`. Control-corpus creation, manifest validity, schema compatibility, and recovery outcome
   are evidence; directory existence is not.

8. **Canonical identity is persisted.** Symlinks, relative paths, and aliases resolve to one canonical URL and one
   stable store identity. The receipt records both the caller's request and the canonical result.

9. **Leasing is part of opening.** A store cannot be admitted while another live owner holds its lease. A stale
   lease may be reclaimed only after the recorded owner is proven gone, and cleanup is conditional on the original
   lease token.

10. **Preflight precedes process admission.** The launcher obtains and persists a successful receipt before starting
    Reframe. Reframe validates that receipt, its executable identity, its parent/owner relationship, and its store
    path before starting store-backed services.

11. **Previous compiles reuse stores safely.** Store identity is independent of the Swift executable path and source
    commit. A changed build may resume an existing compatible store; incompatible migration is explicit, recorded,
    and never silently replaced by a fresh store.

12. **Failure is fail-closed and writer-facing.** Ambiguous selection, missing metadata, incompatible schema,
    active lease, failed recovery, and failed initialization stop the launch with a reason that names the requested
    intent and exact canonical path when one exists.

13. **Evidence names its authority.** The receipt proves selection and preflight. FountainStore proves persisted
    behavior. AX proves the available interaction and state. CoreGraphics window identity proves visual placement.
    Logs are telemetry and cannot substitute for any of these.

14. **The API is versioned and documented.** Public types, state transitions, errors, migration rules, and examples
    live in Fountain-Store's Swift documentation and repository docs. Reframe's launcher and agent skills point to
    that API; undocumented environment conventions are not supported interfaces.

## The public shape

The first public shape is intentionally small:

```swift
public enum FountainStoreIntent: Sendable, Codable {
    case fresh(label: String)
    case resume(alias: String)
    case explicit(path: URL)
    case writerLibrary
}

public struct FountainStoreSelectionRequest: Sendable, Codable {
    public let intent: FountainStoreIntent
    public let purpose: String
}

public enum FountainStoreState: String, Sendable, Codable {
    case fresh, ready, incomplete, incompatible, corrupt, leased
}

public struct FountainStoreSelectionReceipt: Sendable, Codable {
    public let requestedIntent: FountainStoreIntent
    public let canonicalPath: URL
    public let identity: String
    public let state: FountainStoreState
    public let sourceRevision: String?
    public let preflightPassed: Bool
}
```

The exact names may evolve during implementation, but the semantic fields may not disappear: requested intent,
canonical path, stable identity, state, provenance, and preflight result are the minimum needed to stop a client
from claiming that it opened one store while actually opening another.

## State transitions

```text
request
  ├─ fresh ───────────────→ initialized → ready → leased → opened
  ├─ resume / explicit ───→ inspected ───→ ready → leased → opened
  ├─ writerLibrary ───────→ confirmed ───→ ready → leased → opened
  └─ ambiguous / invalid ─→ rejected

existing store
  ├─ compatible ──────────→ ready
  ├─ incomplete ───────────→ recover or reject explicitly
  ├─ incompatible ────────→ migrate or reject explicitly
  ├─ corrupt ──────────────→ recovery failure / reject
  └─ live lease ───────────→ reject with owner evidence
```

No transition from `rejected`, `incomplete`, `incompatible`, or `corrupt` to `opened` may be hidden in a fallback.

## Repository boundary

Fountain-Store owns:

- canonicalization and stable identity;
- manifest and readiness inspection;
- initialization and recovery primitives;
- atomic leases and owner-safe release;
- selection receipts and public errors;
- crash and relaunch tests.

Reframe owns:

- product intents and aliases such as `writer`, `fresh live drive`, and a named Circe fixture;
- required Reframe control corpora and application schema checks;
- launcher/app admission and AX wording;
- live-drive and publication evidence.

Fountain-Store must not depend on Reframe. Reframe must not duplicate Fountain-Store's selection or lease logic.

## Acceptance

The chapter is implemented only when all of the following are demonstrated:

1. a fresh request creates and receipts one isolated store;
2. a resume request reopens the exact same identity after a new Reframe compile;
3. an explicit path never selects a neighboring store or follows an unreported alias;
4. the writer library is rejected unless its protected intent is explicit;
5. an empty directory, incomplete store, incompatible store, corrupt store, active lease, and stale lease each have
   distinct observed outcomes;
6. two simultaneous callers cannot open one store;
7. a crash/relaunch preserves the receipt and store identity;
8. the launcher and Reframe validate the same receipt;
9. the Swift API documentation, Reframe agent guidance, and live-drive skill show the same supported flow;
10. Fountain-Store and Reframe pin and report the same released library revision.

## Relationship to other chapters

Chapter 13 governs persistence and relaunch layering; this chapter makes the store boundary executable. Chapter 43
governs named-build release claims; a store receipt is evidence of the runtime's selected authority, not proof that a
capability is released. Chapter 48 governs service facts; a store authority is a native dependency, not an HTTP
service to be discovered. Chapter 54 keeps internal projections from becoming writer obligations; this chapter keeps
store mechanics out of the writer's head while making them explicit to the runtime and its agents.

## Governing sentence

**A FountainStore is an identified authority with a lifecycle, not a directory Reframe happens to open; every process
must receive the same explicit, verified store receipt from the shared Swift authority.**
