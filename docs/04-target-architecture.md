# Target Architecture

> Chapter summary: This chapter defines the final stage model, artifact ownership, authority boundaries, and non-negotiable invariants of the Grounding-first Reframe application.

The final architecture has one source, one declared policy contract, one structural reader, one authored draft, and one continuity authority. Its simplicity is intentional: each stage owns a different kind of truth and may not silently claim another stage's authority.

```text
┌──────────────────────┐
│ Canonical source     │  factual manuscript evidence
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ Confirmed Grounding  │  writer-declared interpretive policy
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ Storify Source Auto  │  structural reading and synthesis
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ Cut Script           │  selected and authored output
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ Continuity           │  cross-unit audit and guidance
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│ Compose / Publish    │  user-authorized production actions
└──────────────────────┘
```

## Stage authority

The canonical source owns what the manuscript says. It is imported, line-addressable evidence. Storify and later stages may cite it, but generated analysis is persisted beside it rather than inserted into it.

The Grounding Profile owns what the writer has declared about interpretive posture. It names the authorial baseline, reader lens, source language, destination medium, structural priorities, preservation duties, and transformation boundaries. It does not assert what happens in the source.

Storify owns proposed dramatic structure. Its atoms, kept/noise classifications, beats, uncertainties, window summaries, synopsis, and arcs are source-bound, Grounding-bound derived artifacts. Storify is the only production stage that reads the canonical source for structural segmentation.

Cut Script owns mutable screenplay output. It may use Storify structure and Grounding policy, but the draft is never confused with the source.

Continuity owns cross-unit findings for an explicitly named basis and scope. A continuity report is true only of the Cut Script or unit identity it audited. It advises compose and blocks publish only where current policy explicitly requires complete, fresh coverage.

## Artifact identity

Every derived artifact must state enough identity to prove what it belongs to. At minimum, Storify artifacts carry the source document identity, operational source hash, confirmed Grounding identity, operation version, provider provenance when a provider was used, and current steering identity when steering changed the result. Cut Script artifacts add the selected Storify structure identity. Continuity reports add the exact Cut Script or unit dependency identity.

Identity is not a cache convenience. It is the reason a persisted artifact may be trusted after relaunch. A missing or mismatched identity produces stale or unavailable status; the runtime must not patch the gap with in-memory assumptions.

## Readiness

Readiness derives from persisted artifacts and current identities:

```text
Grounding ready  = required Grounding fields are confirmed for the current manuscript
Storify ready    = all required source windows are settled for source + Grounding
Cut Script ready = a current draft exists for the selected Storify structure
Continuity ready = required scope is freshly audited for the current Cut Script identity
```

There is no index readiness and no published semantic-object readiness. A human-readable Guide projection, if retained, reports existing Grounding and Storify truth and cannot block downstream work.

## Prompt authority

Storify prompt construction follows a strict hierarchy. Source atoms determine facts. Confirmed Grounding determines interpretive and adaptation policy. The Storify preset determines operational emphasis. Current writer steering narrows the immediate task. When these inputs conflict, source evidence wins on facts, current explicit steering wins over older operational preference, and conflicts are surfaced as uncertainty rather than silently reconciled.

Prompt context is selected by semantic relevance to the phase. Full transcript, full source, full Grounding history, all tools, and all runtime state are not default context. Numeric measurements may be emitted as telemetry but must not select, clamp, truncate, or rank semantic content. Provider context windows remain transport constraints; inability to form a safe relevant context is a visible request for clarification or a routed provider limitation, not permission to omit meaning by size.

## Final invariants

- No production action invokes semantic indexing or staged passage reading.
- No readiness, capability, or UI state depends on `semantic_index_fresh`.
- No Storify prompt reads index summaries, claims, patterns, reflection, or reading states.
- No beat is derived from an index turn.
- Every Storify semantic window receives current confirmed Grounding.
- The canonical source remains immutable under analysis.
- FountainStore native access remains authoritative when available.
- Telemetry, resume tokens, window tracking, budgets, and visible failures remain enabled.
- Freeform writer turns continue through intent mediation before execution routing.
- Generated reasoning artifacts are regenerated whenever their source contracts change.
