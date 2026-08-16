# Private Image Prompt History

> Status: governing contract for the private `image.prompt.history` capability. This chapter narrows the general
> prompt-retention prohibition only for the exact authored prompt required by this capability.

## Governing sentence

> Reframe may retain an exact image-generation prompt only as a private, access-controlled history artifact whose
> purpose is writer recovery and lineage; no other surface may treat that text as public, telemetry, manuscript, or
> publication material.

## Rules

1. **The exception is capability-scoped.** Only the registered `image.prompt.history` capability may write or read
   exact image-generation prompt text. Other image lifecycle receipts remain digest-only.
2. **The artifact is private by construction.** Prompt history is stored under a protected FountainStore document
   identity and private retention policy. It is not Fountain text, a beat, a public project export, a Book projection,
   a reasoning-manifest fact, or a general conversation-history substitute.
3. **The record is lineage-bound.** Each entry carries execution identity, lineage identity, operation, provider/model,
   creation time, terminal state, Image Cloud reference when available, and prompt digest. The exact prompt is useful
   only when those identities remain readable and the entry is not stale or deleted.
4. **The writer's access is explicit.** The writer can request, inspect, and remove her prompt history through the
   governed Reframe surface. Copilot may use a selected history entry only when the active image operation declares
   that lineage as context; prompt history never silently becomes general model context.
5. **No leakage.** Exact prompt text must not appear in logs, telemetry, error strings, screenshots used as public
   evidence, lifecycle receipts, cloud manifests, Fountain text, Book content, or diagnostic exports. Redaction tests
   must inspect both successful and failed paths.
6. **Provider and cloud custody stay separate.** The prompt-history artifact may record provider/model identity and
   the Image Cloud reference, but it does not replace Image Cloud rights, provenance, disclosure, or publication
   receipts and does not authorize a provider call.
7. **Retention is reversible.** Deleting history removes the exact prompt while retaining only the minimum digest and
   terminal lineage evidence required by the applicable audit policy. Export and relaunch must preserve the private
   access boundary.
8. **AX is truthful.** The private history list and detail view expose their privacy state, lineage, and terminal
   outcome through FCIS-AX. A Copilot response may say that history is unavailable, redacted, stale, or deleted; it may
   not reconstruct missing prompt text from a digest.

## Acceptance

The contract is met only when focused tests and a fresh isolated Live Drive prove:

- an exact prompt is recoverable from the private history surface after a successful generation;
- the same prompt is absent from the lifecycle receipt, telemetry, logs, cloud manifest, and public projection;
- failed, cancelled, duplicate, relaunch, and deletion paths preserve the same boundary;
- a selected history entry is not silently injected into unrelated Copilot turns; and
- the FountainStore artifact, AX state, window-ID evidence, executable, PID, source commit, and managed Store agree.

The capability remains `draft` or `blocked` until the private Store authorization and retention implementation exist.

## Relationship to image governance

Chapter 66 still governs image custody, AI provenance, rights, disclosure, and publication. Chapters 20 and 51 still
govern paid-lane election and credential custody. This chapter changes only exact prompt retention for the named
private history capability; it does not loosen any provider, publication, or public-safety boundary.
