# 71 — Reframe-to-Reframe Software-Peer Acceptance

Chapter 70 defines Reframe's negotiated MIDI2 boundary. This chapter defines the first conformance topology that can
prove that boundary without physical MIDI2 hardware: one Reframe process drives another Reframe process through the
MIDI2 software backplane.

This is a software-peer acceptance claim. It is not a hardware-interoperability claim, and it is not a new command
vocabulary. The capability, operation, lifecycle, consent, and terminal contracts remain those of the IDL, generated
capability registry, and the governing Reframe chapters.

## The topology

The acceptance run has three distinct authorities:

1. **Reframe A — target writer.** Reframe A owns the capability registry, semantic mediation, provider/lane election,
   consent, execution, FountainStore lifecycle, and the user-facing AX surface.
2. **Reframe B — software peer.** Reframe B performs MIDI-CI/Property Exchange discovery, invokes one typed
   capability, observes lifecycle events, handles consent and refusal, and reads the terminal result through the
   negotiated contract. It is an external peer, not a second Copilot and not a privileged test harness.
3. **Independent witness.** A third observer binds the run to both process identities, the target window ID, the
   target Store artifacts, the transport trace, the executable provenance, and the source commit. Reframe B cannot
   approve its own view of Reframe A.

Reframe A and Reframe B must be separate processes with separate PIDs and separate managed Store paths. A same-process
loopback, a second ViewModel, a direct method call, a shared Store, or a GUI script is not software-peer acceptance.

The transport may be a negotiated MIDI2 software or virtual endpoint backed by the owned MIDI2 implementation. The
transport must preserve the IDL topics and lifecycle semantics; an ad-hoc socket protocol or test-only JSON shortcut
does not establish MIDI2 conformance. No physical hardware is implied by this topology.

## Authority and routing

The peer may request a registered capability and supply the operation's typed arguments. It may not choose the model,
provider, or lane; bypass mediation, consent, or policy; write Reframe A's Store; invent completion; or treat an
acknowledgement as the result. Reframe A remains paid-first and selects the best available governed model for the task,
using local execution only where the capability policy and live availability make that appropriate.

The target's result is complete only when its FountainStore lifecycle and terminal receipt say so. MIDI2 events are the
peer-visible projection of that state, not a replacement for it. The target AX tree remains the machine-readable UI
authority, and the target window-ID capture remains the visual witness.

## Required journey

Every software-peer acceptance scenario must exercise this sequence:

```text
software-peer discovery
  → typed capability admission
  → one authorized operation
  → target mediation, lane election, and consent
  → target execution and Store lifecycle
  → MIDI2 progress/refusal/failure/terminal projection
  → peer resume or dedupe check
  → independent Store + AX + window-ID readback
```

The operation is correlated end to end. A valid run proves the happy path and the applicable refusal, failure, resume,
dedupe, and terminal cases. It must show that a peer reconnect does not duplicate the operation and that the peer can
recover the terminal state from the governed contract.

## Scenario-first gate

The first scenario is named `reframe-to-reframe-storify-source`. Its YAML contract must exist before runtime work for
the peer executor begins. The contract names both process roles, separate Store intents, transport and IDL topics,
prerequisites, consent expectations, correlation and idempotency rules, evidence paths, and the exact software-peer
claim boundary. A JSON projection is generated from that YAML; neither projection is a substitute for the other.

The implementation gates are:

1. read this chapter and Chapter 70 and synchronize both repository copies;
2. author and validate the scenario YAML/JSON pair;
3. implement the peer transport and process-level identity binding;
4. verify IDL, generated manifests, capability policy, and focused contract tests;
5. run Reframe B against a fresh Reframe A and capture the correlated MIDI2 lifecycle;
6. read back Reframe A's Store and independently witness its AX/window-ID state;
7. publish only the evidence-backed software-peer projection in the Book of Reframe.

Until gates 5 and 6 pass, the implementation may claim typed adapter readiness only. It may not claim full live
drivability or software-peer acceptance.

## Evidence and claim boundary

The acceptance tuple is:

```text
source commit
  + target executable and PID
  + peer executable and PID
  + target CoreGraphics window ID
  + separate managed Store paths and receipts
  + negotiated transport/session trace
  + IDL operation and correlation ID
  + target AX state
  + independent window-ID capture
```

The Book may publish the sanitized fact that two Reframe software processes completed a governed MIDI2 operation when
this tuple is complete. It must say “software-peer acceptance” and must not say “hardware interoperable” unless a
separate physical-device acceptance supplies that evidence.

## Governing rule

Two Reframe processes may exercise one composed MIDI2 capability contract as peer and target. The target mediates and
executes; FountainStore proves behavior; MIDI2 projects lifecycle; AX and the target window witness the writer surface;
an independent observer binds the evidence. The claim stops at the strongest topology actually observed.
