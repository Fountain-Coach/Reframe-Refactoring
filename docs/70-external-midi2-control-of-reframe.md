# 70 — External MIDI2 Control of Reframe

Reframe is intended to be a first-class MIDI2 participant: an external MIDI2 entity may discover what Reframe can
do, authorize an operation, invoke it, receive progress and terminal events, and read the resulting state without
driving the app by guessed text, screen coordinates, or private process hooks.

This chapter defines that target. It does not claim that the target is implemented. Until the capability registry,
IDL, runtime, FountainStore receipts, and an external-device Live Drive agree, Reframe remains only partially
MIDI2-drivable.

## The decision

The external MIDI2 entity is a peer driver, not a second Copilot and not a privileged test harness. It communicates
with Reframe through the negotiated MIDI2 backplane contract. Reframe remains responsible for semantic mediation,
capability policy, lane election, consent, execution, persistence, and terminal proof.

The governed path is:

```text
MIDI-CI discovery and Property Exchange
  → capability admission and authorization
  → one Reframe capability operation
  → mediated meaning and deterministic execution
  → FountainStore durable lifecycle and result
  → MIDI2 progress/terminal projection
  → AX/window-ID independent surface witness
```

The external entity may initiate the operation, but it may not manufacture Reframe meaning, bypass the capability
registry, select a provider by name, assert completion from an acknowledgement, or write directly to FountainStore.

## What “full MIDI2 live-drivable” means

The phrase has a precise acceptance boundary. Reframe is fully MIDI2 live-drivable only when an external MIDI2
driver can, for every released driver-capable Reframe capability:

1. discover the capability and its version, role, required authorization, input schema, result schema, QoS, budget,
   correlation, resume, and failure vocabulary;
2. submit a typed operation through the IDL without depending on a writer-facing phrase or slash command;
3. receive mediation, admission, progress, refusal, failure, and terminal events using the same correlation identity;
4. recover or resume according to the operation's declared policy without duplicating a durable effect;
5. read the authoritative FountainStore lifecycle and result documents after the event;
6. observe the corresponding Reframe surface state through AX, with window-ID capture when visual proof is required;
   and
7. produce one evidence bundle binding the external driver, Reframe PID, window ID, Store path, executable, and
   source commit.

An operation that merely accepts a MIDI message, returns an acknowledgement, or emits telemetry is not thereby
MIDI2 live-accepted.

## One operation, three synchronized representations

The operation is defined once in the composition governed by Chapter 49:

| Representation | Responsibility | Authority |
| --- | --- | --- |
| IDL | topic, payload, capability mask, QoS, budget, correlation, chunking, resume, response topic | MIDI2 transport contract |
| Generated reasoning/capability manifest | writer meaning, when to use, never use, mutability, owner, gates, cost, policy, evidence | Reframe reasoning and capability contract |
| Scenario YAML | one executable journey, prerequisites, driver actions, terminal predicates, evidence binding, status | E2E acceptance and Book projection input |

The Book is a sanitized projection of the scenario and capability contract. It is never a fourth authored operation
definition. A mismatch between these representations fails validation and blocks implementation or publication.

## External driver roles

An external MIDI2 device or peer may have one or more declared roles:

- **discovery client** — reads Reframe's negotiated capability declaration;
- **operation client** — requests a governed capability;
- **event subscriber** — receives progress and terminal projections;
- **resume client** — continues an admitted operation using its declared resume token;
- **evidence client** — reads a permitted result or receipt, never private Store internals.

Role admission is explicit. A device does not gain write authority merely because it can receive telemetry, and a
telemetry subscriber cannot be treated as an operation executor. Capability masks and authorization are checked at
the operation boundary, not inferred from device presence.

## Mediation and lane policy remain inside Reframe

MIDI2 supplies the external operation identity and typed intent payload. Reframe still performs the one governed
mediation decision required by Chapters 23, 24, 37, and 51. The external driver does not choose “paid”, “local”, a
model name, a prompt window, or a fallback chain.

For writer-facing work, paid availability remains the default election. Local execution may be used when the
governed lane decision finds it economically suitable or when the writer explicitly requests local-only execution.
The selected lane is recorded once and carried through execution. A provider failure is a typed terminal outcome; it
does not silently turn an external MIDI2 request into a different operation.

Internal delegation is not exposed as a second MIDI2 actor. The driver sees Reframe's capability lifecycle, not an
“Interpreter” ceremony, prompt rewrite, or provider-specific persona.

## Event and state authority

MIDI2 events describe transport and lifecycle transitions. FountainStore proves durable behavior. The canonical
ordering for a mutating operation is:

```text
admitted → started/progressing → WAL fsync and in-memory apply → StoreChange
  → lifecycle/result document → MIDI2 terminal projection
```

The MIDI2 terminal event is not sufficient on its own. A consumer reads the named Store artifact at or after the
announced sequence. The Store's native cross-process `changes()` feed is the event seam; Reframe must not reintroduce
WAL parsing, filesystem watching, transcript matching, or snapshot polling as a substitute.

At-least-once delivery requires de-duplication by correlation and execution identity. Exactly-once effects require
the IDL's resume/receipt semantics and an idempotent Store-side operation boundary. “No event received” means only
that no event was observed; it never proves that the operation did not happen.

## Surface and evidence authority

An external MIDI2 driver does not replace the independent Live Drive witness. For a user-facing capability:

- MIDI2 proves the external control path and transport lifecycle;
- FountainStore proves durable behavioral effect;
- AX proves the semantic writer-facing surface;
- CoreGraphics window-ID capture proves which rendered window was observed;
- telemetry explains timing, provider, QoS, and resource behavior but cannot prove completion alone.

The evidence tuple remains:

```text
(external driver identity/session, Reframe PID, CoreGraphics window ID,
 managed FountainStore path, executable path, source commit)
```

An isolated external-device run may not be reported as the writer's current UI. A MIDI2-only test may establish
transport acceptance, but it cannot establish writer-surface or public-command acceptance without AX and Store proof.

## Security, custody, and failure

The external boundary must not expose credentials, raw private Store paths, unpublished manuscript material, or
deployment secrets. Authorization and consent are facts carried by the governed operation and its receipt, not by a
device naming itself as trusted.

Every refusal is typed and visible to the driver and, where the operation is writer-facing, to the writer. Required
failure classes include malformed envelope, schema mismatch, unknown capability, denied capability, stale or invalid
resume, unavailable lane, provider failure, Store admission failure, and surface-not-established. A transport timeout
is a transport observation, not a semantic success or failure until the authoritative Store state is read.

## Every command enters the same operation boundary

MIDI2 is not an optional second route reserved for external peers. A Reframe command is a request for one registered
operation, whether initiated through Copilot, a slash grammar, a button, an internal scenario actor, or an external
MIDI2 peer. These surfaces may differ in how intent is expressed, but they MUST converge before execution on the same
typed operation identity, admission policy, correlation identity, and lifecycle.

The local implementation MUST NOT use a notification handoff, callback-only task, or Store-document polling loop as a
substitute for that operation boundary. A local surface may use an in-process adapter to the same MIDI2 executor, but
it must receive the same admitted, progress, terminal-success, and terminal-failure events. FountainStore persists
those events and results; it is not the command bus.

This does not require an external MIDI-CI exchange for every local turn. MIDI-CI discovers and negotiates the operation
when a peer is external. Local surfaces use the already-registered operation definition while preserving the same
payload, lifecycle, correlation, idempotency, and failure vocabulary.

## The local AX/MIDI2 coordinator

The local adapter is a Swift-owned coordinator, not a second command router. Its job is to bind the machine-readable
AX surface to the same registered MIDI2 operation that an external peer would invoke. AX does not become a transport
implementation, and MIDI2 does not become a replacement for accessibility semantics. The coordinator owns the join:

```text
AX action or local intent
  → typed operation admission
  → one execution identity
  → MIDI2 lifecycle events
  → AX state/progress/result projection
  → FountainStore lifecycle and terminal proof
```

Every admitted execution MUST carry one stable binding containing, at minimum, `scenarioId` when applicable,
operation identity and version, `executionId`, `correlationId`, source commit, Store intent/path identity, and the
selected capability policy. The same `executionId` and lifecycle sequence MUST be observable in the MIDI2 event
projection, the AX activity surface, and the persisted FountainStore lifecycle/result documents. A surface may expose
different labels or controls, but it may not create a private lifecycle, infer progress from elapsed time, or call an
executor directly while presenting itself as the MIDI2 operation.

The coordinator MUST admit before an AX action can claim that work is running, publish explicit admitted/running/
progress/terminal states, route cancellation and resume through the same operation boundary, and fail closed when
the MIDI2 readiness or Store binding is absent. The scenario runner may drive AX and observe the independent surface,
but it must use MIDI2 for the operation handoff and must reconcile the same execution identity across MIDI2, AX, and
Store evidence. Subprocesses may collect evidence; they may not coordinate runtime execution.

This rule applies equally to Copilot, slash commands, buttons, internal scenario actors, Book Library operations,
Storify, semantic search, image generation, and external MIDI2 peers. The first implementation target remains one
complete capability; naming the coordinator does not establish that every capability has migrated.

The first migration target is Book Library import. Its current notification handoff is a compatibility seam only until
`library.import` has a declared IDL topic, generated facts/manifest entry, typed executor, correlated lifecycle, and an
event-driven scenario proving both success and provider failure.

## Implementation gates

No capability becomes externally driver-capable by editing this chapter. The implementation gate is:

1. declare or reuse the operation in the IDL and regenerate facts;
2. add its single manifest/capability identity and owning runtime actor;
3. define authorization, lane, consent, idempotency, resume, Store, telemetry, and AX policy;
4. author the complete external-driver scenario YAML before runtime edits;
5. validate YAML/JSON parity and focused contract tests;
6. implement the MIDI2 adapter without a second operation vocabulary;
7. run an external-driver integration test and an independent Live Drive;
8. read the matching Store artifacts and bind all evidence to one tuple; and
9. only then mark the capability `live-accepted` and project it into the Book.

The first implementation slice must be one small, meaningful capability with a complete lifecycle, not a broad
adapter that claims the whole app. Each additional capability repeats the same scenario-first gate.

## What this chapter does not permit

- MIDI notes, controller numbers, or device-specific gestures as an undocumented Reframe API;
- direct mutation of FountainStore by an external device;
- a second router that competes with Reframe mediation;
- external selection of a model, paid lane, fallback, or prompt wording;
- an acknowledgement presented as completion;
- a Book page claiming “MIDI2 capable” without external-driver and independent surface evidence;
- treating the existence of a MIDI2 implementation as proof that Reframe has implemented every adapter.

## Governing sentence

An external MIDI2 entity may drive Reframe only through the one composed capability contract; MIDI2 carries the
negotiated operation and lifecycle, Reframe mediates and executes, FountainStore proves what happened, and AX proves
what the writer could see.
