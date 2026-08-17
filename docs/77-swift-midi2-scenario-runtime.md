# 77 — The Scenario Runtime Is Swift and MIDI2-Native

Chapters 68 and 73 make the E2E scenario Reframe's development and publication unit. Chapters 70, 71, and 75 define
the MIDI2 operation boundary, software-peer topology, and owned-run evidence rules. This chapter closes the missing
implementation boundary: the scenario contract and the application it proves must be executable by the owned Swift
and MIDI2 stack, without a Python interpreter in the acceptance path.

This is an architectural decision, not a claim that every witness action is a MIDI2 message. MIDI2 carries the typed
scenario operation and its lifecycle between scenario actors and Reframe. AX and CoreGraphics remain independent
witness interfaces because they prove what the writer could operate and see. FountainStore remains the durable
behavioral authority.

## The decision

Reframe's governed scenario runtime MUST be implemented in Swift and MUST use the owned MIDI2 backplane for scenario
execution. The runtime is a product capability and a development tool at once: Reframe can exercise a Reframe
capability through the same typed operation boundary that an external MIDI2 peer uses.

The scenario contract remains the authoring and publication unit. Its executor, lifecycle, event subscription,
evidence binding, and terminal classifier belong to the Swift stack. Python may remain temporarily as a migration or
documentation utility, but it is not an acceptance authority, a required runtime dependency, or a valid substitute for
the MIDI2 operation path.

## Rules

1. Every executable scenario MUST have a Swift executor that loads the checked scenario projection, validates its
   launch and actor bindings, and owns preparation, execution, waiting, evidence, and terminal classification.
2. Scenario execution MUST enter through one registered typed MIDI2 operation. The operation identity, payload,
   correlation, idempotency, consent, lane policy, lifecycle, resume, and failure vocabulary MUST be declared in the
   IDL/reasoning manifest and generated facts before the runtime is marked executable.
3. The scenario executor MUST NOT call a ViewModel method, write a target FountainStore directly, inject a fake
   completion, or introduce a test-only socket/JSON command path. A local scenario actor may be in-process, but it
   must use the same MIDI2 operation adapter and lifecycle as an external peer.
4. The MIDI2 event stream and FountainStore `changes()` feed MUST be armed before the associated action. A Store wait
   is event-driven and followed by an authoritative read-back; a watchdog may detect a hang but cannot establish
   semantic success or failure.
5. AX probes, CoreGraphics window capture, VRT, and telemetry are witness operations. They may observe and record a
   run, but they may not drive semantic completion or mutate the run's authority. The scenario cannot claim that
   MIDI2 made the UI correct without matching AX and window evidence.
6. The Swift runtime MUST preserve one uninterrupted run identity from preparation through terminal classification:
   scenario, source commit, executable, target PID, window ID, managed Store, launch intent, corpus, scene, and
   evidence root. A process replacement, Store replacement, or unrecorded intervention invalidates the run.
7. The runtime MUST support terminal success, typed failure, refusal, unavailable capability, disconnect, duplicate,
   reconnect, resume, and capacity outcomes as declared scenario predicates. “Not observed yet” is never a terminal
   result.
8. Scenario setup MUST be Swift-owned as well as scenario execution. Fresh Store admission, fixture seeding, MIDI2
   endpoint creation, and run-record creation may not depend on a Python script that silently selects a different
   corpus, scene, or Store intent.
9. The executor MUST optimize for event-driven latency: subscribe before acting, perform independent preparation in
   parallel where the contract permits it, reuse only verified build artifacts, and report immediate admitted
   progress through the MIDI2 lifecycle. It MUST NOT trade semantic correctness for numeric truncation, timer-driven
   success, or hidden retries.
10. A Python runner or shell harness may be used during migration only when it is explicitly labelled diagnostic or
    transitional. It cannot produce `live-accepted`, cannot be required by the Book command, and cannot be the only
    implementation of a scenario contract.
11. The Book may describe “MIDI2-native scenario-driven development” only after a Swift executor has completed the
    declared scenario and the independent AX, window-ID, FountainStore, telemetry, and provenance evidence agree.
    The claim means software-stack ownership and MIDI2 operation conformance; it does not imply physical hardware
    interoperability.

## Required topology

```text
Swift scenario actor
        │ typed MIDI2 operation + lifecycle
        ▼
Reframe target / external software peer
        │
        ├── FountainStore changes() + authoritative receipt
        ├── AX semantic witness
        └── CoreGraphics window-ID / VRT witness
```

The scenario actor and target may be separate Swift processes for peer acceptance or may use an in-process adapter for
local development. In both cases the operation identity and lifecycle are the same. A direct function call is a unit
test, not a MIDI2 scenario acceptance.

## Migration gate

The existing Python scenario tools are transitional evidence infrastructure. Before any scenario is promoted or
published under this chapter, the migration must:

1. add the Swift scenario contract/runtime target and its generated MIDI2 operation facts;
2. move Store preparation, event waits, AX action sequencing, and terminal classification into Swift;
3. run the canonical Book Library → Storify → downstream capability scenario through that runtime;
4. run the Reframe-to-Reframe software-peer scenario through the same operation boundary;
5. compare the Swift evidence bundle with the YAML terminal predicates and independent surface evidence; and
6. retire Python from the acceptance path, retaining it only if a separate governance decision preserves it for
   offline publication tooling.

Until this gate passes, existing Python-driven runs are diagnostic or transitional and must not be presented as proof
that the owned MIDI2 scenario stack is complete.

## Why this is a product distinction

Most E2E systems describe behavior in one language and test it through a separate automation layer. Reframe's stronger
claim is that the development scenario is itself a governed MIDI2 participant: it invokes the same typed capabilities,
observes the same correlated lifecycle, and is judged by the same Store and surface authorities as a real software peer.
That makes the development loop a conformance exercise rather than an imitation of one.

The claim remains bounded. MIDI2-native scenario execution proves owned software interoperability and lifecycle
truthfulness. Physical-device interoperability still requires a separate hardware witness.

## Governing sentence

Reframe scenarios are developed and accepted by an owned Swift runtime that drives the same typed MIDI2 operation
boundary as production peers; FountainStore proves behavior, AX and CoreGraphics witness the writer surface, and no
Python harness may stand in for that contract.
