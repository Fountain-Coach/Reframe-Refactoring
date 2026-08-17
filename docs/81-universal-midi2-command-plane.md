# 81 — The Universal MIDI2 Command Plane

Chapters 70 and 77 establish Reframe as a MIDI2-drivable software participant and make the scenario runtime
Swift-owned. This chapter closes the remaining architectural ambiguity: MIDI2 is not a special route for external
peers or for a small set of commands. It is Reframe's command plane. Every executable Reframe capability enters the
same typed MIDI2 operation boundary.

This is a governance target and migration rule. It does not claim that every capability is already migrated. A
capability is not universal-MIDI2 complete until its registry identity, IDL contract, executor, lifecycle, Store
receipt, AX surface, and acceptance scenario agree.

## Current implementation status

The first universal-ingress slice is implemented. `reframe/capability.invoke` is declared in the MIDI2 IDL; discovery
enumerates the generated `CopilotCapabilityID` registry; the Swift adapter resolves the requested identity through
that registry and enters the existing mediation, consent, lane, and capability executor; and the Swift scenario
runner can emit the generic topic. The scenario contract is `universal-midi2-capability-ingress`.

The focused contract suite passes and the scenario projection is executable. This establishes the generic transport
and dispatch boundary, not registry-wide capability availability or live acceptance. The remaining acceptance gate is
an independent software-peer run with matching FountainStore, AX, and window-ID evidence; the chapter remains honest
about that boundary until it exists.

## The decision

A Reframe command is a writer-facing expression of intent. A capability is the registered operation that can satisfy
that intent. MIDI2 is the common command and event boundary between the expression, the operation, and its durable
result. Copilot, slash commands, buttons, the Swift scenario actor, and a second Reframe instance are different
clients of the same operation plane; they are not different implementations of the command.

The governed path is:

```text
surface intent
  → one mediated capability identity
  → one typed MIDI2 operation envelope
  → admission, consent, lane election, and execution
  → correlated lifecycle events
  → FountainStore receipt and result
  → AX-visible projection and independent evidence
```

No surface may execute a capability by private ViewModel call, notification handoff, callback-only task, guessed
Store path, transcript matching, or a second command vocabulary. An in-process adapter is allowed for local
performance, but it must enter the same operation executor and emit the same lifecycle and terminal result.

## MIDI-CI and the operation plane are different layers

MIDI-CI is the peer handshake. It establishes identity, discovery, Property Exchange, supported profiles, and the
capability vocabulary a peer may use. It answers: “Who are you, and what can you speak?”

The MIDI2 command plane carries a particular operation after that capability relationship exists. It answers: “What
typed operation was admitted, what happened, and what durable result can I read?”

For an external peer the sequence is therefore:

```text
MIDI-CI discovery / Property Exchange
  → operation discovery and authorization
  → typed MIDI2 request
  → MIDI2 lifecycle and terminal result
```

For Copilot, the GUI, and the local Swift scenario actor, a fresh MIDI-CI exchange is not required on every turn.
They use the already-negotiated local endpoint and the same registered operation definition. Omitting a network or
device handshake locally does not permit them to bypass the MIDI2 operation contract.

## One envelope for every capability

The exact capability-specific arguments and result schema remain typed by the IDL. The transport and lifecycle
envelope is uniform and must carry, as applicable:

- operation identity and contract version;
- correlation, execution, idempotency, and resume identity;
- requesting role, peer/session identity, and authorization or consent facts;
- current corpus and source-document identity when the operation is manuscript-scoped;
- lane election and provider outcome without allowing a caller to select a provider by name;
- admitted, running, awaiting-confirmation, succeeded, failed, canceled, or unavailable state;
- progress and failure vocabulary defined by the backplane contract; and
- terminal result identity, receipt, and authoritative Store address.

The terminal event is not an acknowledgement. It names what became true. For an import it can name the resulting
corpus and source document. For a reading it can name the reading receipt and coverage. For image generation it can
name the asset-cloud receipt. For a project write it can name the durable revision. A consumer follows those returned
identities; it never guesses a fixture corpus, scans for the newest document, or waits on an unrelated default.

## The single router remains Reframe mediation

Making every command MIDI2 does not create a second semantic router. Mediation still reasons over the complete
capability taxonomy and live state before execution. It decides whether the request is actionable, needs clarification,
or remains conversational. It resolves the registered operation and lets the governed lane policy decide how the work
is served.

The MIDI2 peer or scenario actor may request an operation, but may not choose “paid”, “local”, a model, a fallback,
or a prompt rewrite. Paid availability remains the default election for writer-facing work; local execution is used
when the governed reasoning finds it suitable or the writer explicitly requests local-only execution. This decision
is recorded once and is visible in the lifecycle. Internal delegation is not presented as an “Interpreter” persona.

## FountainStore remains behavioural authority

MIDI2 is the command and event backplane, not a replacement for FountainStore. The operation boundary owns the
correlation and lifecycle; FountainStore owns durable state, receipts, and the native `changes()` event seam. The
required order for a mutating operation is:

```text
admitted → executing → durable Store apply and receipt → terminal MIDI2 projection
```

The event subscriber then reads the named Store artifact. A timeout, missing notification, or stale UI observation is
not proof that the operation failed. At-least-once delivery is handled by correlation and idempotency; resume and
duplicate rules come from the IDL and the Store-side operation boundary.

## All clients converge, all witnesses stay independent

The following are clients, not competing authorities:

| Client | Meaning entry | Required convergence |
| --- | --- | --- |
| Copilot | mediated natural language | registered MIDI2 operation |
| Slash command | explicit machine grammar | registered MIDI2 operation |
| GUI control | grounded deterministic action | registered MIDI2 operation |
| Swift scenario actor | checked scenario step | registered MIDI2 operation |
| Reframe software peer | MIDI-CI-negotiated request | registered MIDI2 operation |

MIDI2 proves control and lifecycle. FountainStore proves durable behavior. AX proves what the writer could operate
and read. CoreGraphics window-ID capture proves which rendered window was witnessed. Telemetry explains timing and
resources. None of these authorities may impersonate another.

## Migration rule

Existing direct paths are compatibility seams, not precedents. No new capability may bypass the universal plane. Each
migration batch must:

1. identify the capability in the generated registry;
2. declare or reuse its IDL operation and generate facts and reasoning artifacts;
3. bind mediation, consent, lane, authorization, idempotency, resume, Store, telemetry, and AX policy;
4. write the complete scenario YAML and JSON projection before runtime edits;
5. route every client through the typed MIDI2 executor;
6. prove terminal result identity rather than acknowledgement or inferred state; and
7. run focused contract tests, the Swift scenario, independent AX/window evidence, and Store read-back.

The migration ledger must distinguish `declared`, `implemented`, `transport-accepted`, `surface-accepted`, and
`live-accepted`. Chapter 70's Book Library import is the first compatibility seam. Its completion does not imply that
the rest of the registry has migrated.

## What this chapter does not claim

- MIDI-CI negotiation does not by itself prove that an operation executed.
- A MIDI2 envelope does not replace semantic mediation, consent, lane policy, Store authority, or AX.
- A software-peer test does not establish interoperability with physical MIDI2 hardware.
- A capability is not universal-MIDI2 complete merely because one adapter or scenario exists.
- The public governance book exposes the contract and evidence boundary, never private Store data, credentials,
  manuscript material, runtime source, or deployment secrets.

## Governing sentence

Every Reframe command is one mediated, typed MIDI2 operation: MIDI-CI establishes the peer relationship, the backplane
carries the correlated lifecycle, FountainStore proves the durable result, and AX independently proves the writer's
surface.
