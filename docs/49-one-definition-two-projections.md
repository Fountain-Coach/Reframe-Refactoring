# 49. One Definition, Two Projections

> Chapter summary: Reframe stands on the MIDI backplane — the IDL is where an operation is *defined*, with the
> things HTTP cannot express: quality of service, capability masks, latency and payload budgets, correlation,
> resume tokens, chunking. But **the web does not speak MIDI 2.0**, and Reframe offers real services to it —
> Ulysses-as-a-Service, Ovid-as-a-Service, the corpus API a self-hosted edition can replace. This chapter refuses
> the choice between them. An operation is **defined once, in the IDL**, and **projected twice**: onto a backplane
> topic, and onto an OpenAPI-described HTTP route. Neither projection is written by hand, so neither can drift
> from the other, and a third party binds to Reframe by publishing a document rather than by reading `main.swift`.

## Purpose — the failure this exists to end

Corpus retrieval is defined twice in this repository, and one of the definitions is invisible to everything that
matters.

The IDL already carries it. `schema/idl.yaml` holds `screenplay/get`, `screenplay/lines.get`, `screenplay/search`,
`screenplay/block.get`, `screenplay/beat.get`, `screenplay/beat.list` — each with `corpusId`, `documentId`, a QoS
class, a capability mask, latency/jitter/payload budgets, `correlationId`, `resumeToken` and chunking.

Beside it, the same operation exists **four more times**, hand-rolled: `ReframeCorpusAPI` (in-app, `NWListener`),
`tools/corpus-api`, `tools/ovid-local-api`, `tools/ulysses-local-api`. Measured 2026-08-06: **not one of them
references the envelope, a QoS class, a capability, a budget or a correlation id.** They are plain HTTP with no
description of any kind.

The cost is not aesthetic. The IDL is **generative** — `midi-schema-to-facts`, `midi-schema-to-reasoning` and
`generate-copilot-capabilities.mjs` all derive from it — so an operation defined there becomes a fact the app can
state, a manifest the reasoning can consult, and a capability identity Copilot can be told about truthfully
([ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md)). An operation defined in `main.swift` becomes none of
those. Copilot cannot know the corpus API exists, cannot say what it costs, and cannot report when it fails.

And it produced a concrete defect one chapter earlier. [ch.48](48-a-service-is-a-fact-not-a-symptom.md) rule 8
requires the register of services to be **generated from declarations** — and there is nowhere to declare a
service, because services are not IDL topics. The rule was unsatisfiable the day it was written, which is why the
register was written by hand, and why it omitted Ulysses-as-a-Service within the hour.

### The drift is already in the pillar

Two repositories carry the IDL: `midi-backplane/schema/idl.yaml` and this one. Both declare `version: 0.2.0`.
Their contents differ by roughly 1,300 lines — 78 topics against 172 — and this copy holds a capability bit,
`web.fetch`, that the backplane's does not.

**The same version number over different truth** is the hand-maintenance failure of ch.48's register, one level
down, in the architecture's foundation. A version is a promise that two things agree; where it is written by hand
it records only that someone typed the same digits twice.

## The principle — the web does not speak MIDI 2.0, and that is not a reason to define twice

The estate's history is not a mistake to correct. Fountain Coach did extensive OpenAPI work — eleven repositories
own an OpenAPI document today — and then **refactored to the IDL for the backplane**, because HTTP could not
express what an operation needs to travel: `qos`, `capabilities`, `budget.latencyMs`, `resumeToken`, `chunk`.
OpenAPI has no vocabulary for any of those. The refactor was right, and the IDL is the pillar Reframe stands on.

But the web is where Reframe's corpora are *offered*. A self-hosted edition replaces Ulysses-as-a-Service by
answering `/v1/episode/{n}` over plain HTTP; a browser can read it; nothing needs a backplane client. That
audience is real and it does not speak UMP.

So the two are not rivals and neither is the other's evolution. They are **projections of one definition**, which
is the move this repository already makes elsewhere: the score is the semantic model, and notation and MIDI 2.0
are projections of it — neither is the score. An operation is the same. Its definition is not its transport.

## The decision (enforceable rules)

1. **An operation is defined once, in the IDL.** Corpus retrieval, screenplay access, beat access — anything
   Reframe or a bound service performs — has exactly one definition, carrying what only the IDL can say: QoS,
   capability mask, budget, correlation, resume, chunking.

2. **Both projections are generated, never authored.** The backplane topic and the OpenAPI document are outputs.
   A hand-written OpenAPI file beside a hand-written server is two hand-maintained truths and will diverge; this
   repository has already proven that at schema level, with two copies of the IDL at the same version.

3. **The HTTP projection is a faithful projection, and says what it drops.** HTTP cannot carry a capability mask
   or a QoS class. The generated document states what the transport cannot express, so a third-party
   implementation knows what it is *not* being told rather than assuming parity.

4. **A service binds by publishing a document, not by being read.** ch.48 asks what a service must declare to be
   callable; the answer is **an OpenAPI document conforming to the generated projection**. Reframe derives the
   register entry, the capability identity and the failure vocabulary from it. "Anything speaking
   `/v1/episode/{n}` is a drop-in" becomes checkable instead of a claim about the current implementation.

5. **Copilot is told what it can do from the definition, never from prose.** Every projected operation becomes a
   capability identity with its lane and cost, so Copilot can offer it, price it, and report its failure —
   including operations belonging to a third-party service that bound this morning
   ([ch.39](39-a-model-cannot-be-told-what-it-cannot-do.md), [ch.37](37-copilot-capability-governance.md)).

6. **A version is a checked agreement, not a typed number.** Where a definition is carried in more than one place,
   agreement is verified mechanically and a mismatch fails. Two files reading `version: 0.2.0` with 1,300 lines
   between them is the defect this rule exists to make impossible.

7. **A bound endpoint is an outward act.** A substituted base URL may be remote, may cost money and may receive
   the writer's text. It runs under [ch.34](34-a-question-that-leaves-the-work.md) and
   [ch.20](20-on-device-first-and-the-writers-key.md) like any other outward act, and the writer is told when a
   non-default service answered — a substitution nobody notices cannot be reported
   ([ch.48](48-a-service-is-a-fact-not-a-symptom.md)).

## Honesty (non-goals)

- **Not "put the corpus API on the backplane".** The HTTP surface exists because the web is a real audience; the
  point is that it stops being a *second definition*.
- **Not a rewrite of the IDL into OpenAPI.** The refactor to the IDL was correct and is not being undone. OpenAPI
  is the projection for consumers that speak HTTP, nothing more and nothing less.
- **Not a plugin loader.** Nothing foreign is loaded into the process. A bound service is another process
  answering a documented contract, which is why it needs no ABI, no sandbox and no trust of foreign code.

## Acceptance

1. Corpus retrieval appears **once** in a definition, and the backplane topic and OpenAPI document are both
   produced from it by a generator, with no hand-edited copy of either in the tree.
2. `midi-schema-to-facts`, `midi-schema-to-reasoning` and the capability generator include the projected
   operations, so Copilot can name the corpus API, state its lane, and report a failure against it.
3. A third-party server implementing the published document is reachable via `ULYSSES_BASE_URL` with no change to
   Reframe, and Reframe reports that a non-default service answered.
4. A deliberate divergence between two copies of a definition **fails a check**, rather than being discoverable
   only by reading 1,300 lines of diff.
5. ch.48's generated register is produced from these declarations, and omitting a service becomes impossible
   rather than merely embarrassing.

## Governing sentence

An operation is defined once, where the definition can carry everything the operation needs; its transports are
projections of that definition, generated and never authored — so the backplane and the web can each be served
faithfully without either becoming a second, quieter truth.
