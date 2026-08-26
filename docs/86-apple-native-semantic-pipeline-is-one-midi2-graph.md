# 86 — The Apple-Native Semantic Pipeline Is One MIDI2 Graph

This chapter is the governance refactoring slice for the Storify Source Auto pipeline described in Chapter 85. It
comes before runtime implementation. Its purpose is to make the boundary unambiguous enough that implementation can
be resumed without inventing a second contract in Swift, a scenario file, or a provider adapter.

## The decision

Storify is one semantic pipeline, not an exclusive choice between a local lane and a paid lane. The local Apple
frameworks establish a fast, source-addressed foundation. The paid lane extends that foundation when the governed
writer-facing policy selects it. Both participate in the same operation graph, carry the same source identity, and
produce receipts that the next operation must name.

The pipeline is:

```text
immutable source admission
  → Apple linguistic measurement
  → local semantic continuity
  → paid enrichment when selected
  → reconciliation
  → synthesis
  → grounded illustration prompt
```

Each arrow is a typed MIDI2 operation. A callback, model request, Store write, or UI progress line is not a substitute
for an operation boundary. The operation enters through the universal command plane in Chapter 81 and is proved by
the separate authorities required by Chapter 08.

Chapter 109, [NaturalLanguage Measurement Is a MIDI2 Instrument](109-natural-language-measurement-is-a-midi2-instrument.md), defines the measurement stage's host adapter, portable result, and terminal evidence boundary.

## The platform foundation

The local foundation may use Apple's Natural Language framework for language recognition, token and sentence
boundaries, lexical and name observations, and embeddings where available. It may use Foundation Models for
structured on-device generation and tool calls when the local model is the selected instrument. These frameworks are
instruments behind the contract; their callbacks and object lifetimes are not the contract.

The paid lane is the default extension for writer-facing semantic work when it is configured, authorised,
constructible, and healthy. Chapter 51 resolves that decision once for each declared operation that needs it. A later
stage receives the decision and its budget; it may not re-elect a provider, silently fall back, or interpret a missing
receipt as permission to start over.

## The seven operation identities

| Stage | MIDI2 operation | Required handoff |
| --- | --- | --- |
| Measure | `reframe/semantic.measure` | immutable source reference, range, framework revision, idempotency key |
| Embed | `reframe/semantic.embed` | source digest, measurement/range receipt, embedding revision, idempotency key |
| Interpret | `reframe/semantic.interpret` | source digest, semantic receipts, lane decision, model revision |
| Enrich | `reframe/semantic.enrich` | interpretation receipts, lane decision, model revision |
| Reconcile | `reframe/semantic.reconcile` | interpretation receipts, optional enrichment receipt, operation revision |
| Synthesize | `reframe/semantic.synthesize` | reconciled receipts, lane decision, model revision |
| Illustration prompt | `reframe/illustration.prompt` | synthesis receipt, grounded Movement/Question receipts, placement relation |

The exact request vocabulary is owned by the MIDI2 IDL and its generated facts. Large source and semantic payloads
remain in native FountainStore custody; MIDI2 carries references, digests, lifecycle, and terminal receipt identity.

## Rules

1. Source admission happens once. Every downstream operation names the admitted source document and content digest.
2. Measurement may establish boundaries and observations; it may not assign story meaning, Movements, Questions, or
   uncertainty.
3. Every stage enters through the universal MIDI2 command plane and emits the declared lifecycle and terminal result.
4. Every derived result names the receipts it used. A stage without source lineage is not an accepted semantic result.
5. Local measurement and paid enrichment are complementary stages. Neither is an alternate authority for the source.
6. A paid-capable stage receives one recorded lane decision, budget, model revision, and idempotency identity. It may
   not silently fall back or re-resolve because a later call is inconvenient.
7. Replayed requests with the same idempotency identity return the same admitted result or the same typed failure.
8. Reconciliation must preserve unresolved gaps. Synthesis may not fill a gap from memory, raw cloud text, or a prior
   uncited response.
9. Illustration prompting consumes only grounded Movement/Question packets and their source addresses. It does not
   consume raw source text or an unverified model synopsis as prompt authority.
10. A declared operation is not an implemented operation, and an implemented operation is not live-accepted. The
    registry, executor, Store receipt, AX surface, telemetry, and scenario evidence must agree before promotion.

## Portable kit boundary

The reusable seam may be released as an FCIS-KIT package. It may own stage identities, typed operation envelopes,
adapter protocols, provenance, idempotency, and reusable Apple instrument adapters. It must not own Reframe views,
consumer-domain semantic types, credentials, product Store projections, or independent AX/window-ID acceptance.

Until that package is released upstream, a tested local package is a development boundary only. Reframe remains the
owner of its product operation identities, Store projections, UI/AX projection, scenario composition, and acceptance.

## Acceptance order

Implementation proceeds in this order:

1. validate the IDL and regenerate facts and reasoning artifacts;
2. test the portable operation contract and its invalid-order, mixed-source, missing-lane, and replay cases;
3. implement one executor per operation with Store custody and lifecycle receipts;
4. express the complete dependency graph in the human/machine-readable scenario contract;
5. prove the composed lane decision and local/paid handoff through independent Store, MIDI2, AX, telemetry, and
   window-ID evidence; and
6. repeat the terminal scenario three times before calling the graph live-accepted.

## Current implementation boundary

This chapter is now the governing refactoring contract. The seven operation identities are declared in the MIDI2 IDL,
generated facts and reasoning manifests are regenerated, and `FountainSemanticPipelineKit` provides a tested local
pre-release contract for ordered handoffs. The complete executor graph, upstream FCIS-KIT release, scenario promotion,
and independent Live Drive acceptance remain implementation work. No published design mock or generated prompt is
evidence that those runtime stages have completed.

## Governing sentence

Storify's local Apple instruments and paid reasoning are one source-addressed, receipt-linked MIDI2 graph: every stage
enters the same command plane, preserves Store authority and lane provenance, and becomes true only when its own
terminal evidence agrees.
