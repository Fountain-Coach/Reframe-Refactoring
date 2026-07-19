# Compatibility and Future Evolution

> Chapter summary: This chapter defines how legacy stores and documents survive the transition, how rollback remains recoverable, and how future features may extend the new architecture without recreating an index under another name.

Removing indexing from production does not require erasing its history. Legacy semantic artifacts are evidence of earlier runs and may matter for audit, support, or research. They should remain readable as archival data, but the application must make their status unmistakable and must not allow them to satisfy current readiness.

## Legacy data policy

The migration is non-destructive. Existing index passages, reading states, published semantic objects, repair debts, learning ledgers, and Apple split-memory facts stay in FountainStore unless the user later chooses an explicit cleanup operation. New code stops creating them and current prompts stop retrieving them.

If archival inspection remains in the app, it belongs behind a clearly labeled legacy surface. It must not share controls or status language with current Grounding, Storify, or Continuity. An old Guide may be exported or compared, but opening it cannot mark Grounding or Storify ready.

Legacy baseline and reader-lens content are different: they remain semantically relevant and should migrate into the extended Grounding draft. Migration preserves exact content and provenance, then asks the writer to complete and confirm fields that did not previously exist. It must not invent structural intent from old index output.

## Rollback during development

Implementation should remain recoverable through source control and store copies, not through destructive resets. Temporary comparison flags may select old or new behavior in development builds while evidence is gathered. Each flag must have an owner, removal phase, and test proving the intended default.

The production end state has no dual authority and no permanent fallback to indexing. A provider failure in Storify is handled by Storify recovery, routing, backfill, or an honest unreadable result—not by secretly reactivating an index reader.

## Evolving Grounding

Future Grounding fields must express writer policy that a downstream phase genuinely consumes. New fields require explicit ownership, UI meaning, identity participation, persistence, and invalidation tests. A field must not be added merely to carry internal prompt tuning or model telemetry.

When a new phase needs only part of Grounding, it should retrieve a reasoned, inspectable phase projection. It must not create an opaque compressed profile selected by token fit. If the projection itself becomes durable authority, it needs provenance, a parent Grounding identity, and writer-visible meaning.

## Evolving Storify

Storify may gain stronger structural schemas, multi-pass critique, provider specialization, or deterministic transformations over validated artifacts. Such extensions remain inside Storify ownership as long as they operate on source atoms and persisted Storify results under confirmed Grounding.

A proposed feature recreates the retired index if it independently rereads every passage into a general-purpose semantic memory before Storify can run. That design requires an explicit architectural review against this guide. Targeted retrieval for a question, a scoped repair of an unreadable Storify window, or a provider-specific Storify pass is not an index when it remains owned by the requested structural task and does not become a parallel readiness authority.

## Evolving Continuity

Continuity remains downstream. It may adopt content-addressed unit reuse or dependency-aware invalidation, but a cached report must retain the exact Cut Script and incoming continuity-state identities that make it trustworthy. Continuity must not become a covert source index or claim authority over source facts it did not audit.

## Documentation lifecycle

This guide should be revised when the target contract changes, not edited to disguise incomplete implementation. Phase results belong in `PLANS.md`; current operational changes belong in generated capabilities and reasoning orientation; historical rationale stays in the history chapter.

When the refactor completes, update the status on the landing page from “authoritative refactoring directive” to “implemented architecture,” add the completion evidence, and mark older index-centered pipeline documents as superseded with links here. Preserve their dates and content so future maintainers can understand why durable persistence, evidence validation, uncertainty, and provider telemetry still exist after the index that introduced them is gone.

## Future-proof test

Any proposed Reframe feature should be explainable through the final authority chain:

```text
What source evidence does it use?
Which confirmed Grounding policy governs it?
Which stage owns the derived artifact?
What exact identity makes that artifact current?
Which downstream consumer is allowed to trust it?
```

If those questions cannot be answered without saying “the semantic index knows,” the feature has either found a missing targeted artifact or is attempting to recreate the architecture this refactor removes.
