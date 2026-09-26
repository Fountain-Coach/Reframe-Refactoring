# 150 — One MIDI2 Instrument Plane, Multiple Governed Transports

### Status

Governance proposal.

This chapter extends Chapters 81, 88, 108, 141, and 149.

It does not replace the universal MIDI2 command plane, the CodexKit boundary, joining-machine admission, or the remote Reframe–CodexKit peer relationship.

It clarifies the layer beneath them:

**the governed MIDI2 instrument plane is transport-neutral.**

RTP-MIDI2 is the currently implemented and proven Fountain Coach remote transport.

It is not the identity of the MIDI2 instrument plane itself.

---

## Chapter Summary

A Fountain Coach participant is a governed MIDI2 instrument independently of the network transport used to reach it.

Identity, MIDI-CI capability negotiation, UMP semantics, operation identity, authorization, lifecycle, durable evidence, and instrument admission belong to the MIDI2 instrument plane.

Network transport belongs beneath that plane.

The authoritative `midi2` implementation already exposes this separation through its common `MIDITransport` boundary.

The currently implemented remote network transport is `RTPMidiSession`, which carries Universal MIDI Packets between explicitly selected software peers over UDP using the Fountain Coach RTP-MIDI2 framing.

The estate SHALL preserve that implementation.

The estate SHALL NOT treat RTP-MIDI2 as the only admissible transport for MIDI2 instruments.

The next standards-facing transport target SHALL be an implementation of **Network MIDI 2.0 over UDP, M2-124-UM**, alongside rather than instead of `RTPMidiSession`.

Future transports MAY be admitted when their semantics, authority boundary, evidence model, and acceptance tests satisfy this chapter.

The resulting architecture is:

```text
                 governed MIDI2 instrument
                           │
                        MIDI-CI
                           │
                  typed UMP operations
                           │
                     MIDITransport
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    RTPMidiSession   NetworkMidi2Session   future
          │                │             transport
      RTP / UDP        M2-124-UM            │
          │                │                │
          └────────────────┴────────────────┘
                           │
                      IP network
```

The instrument remains the same instrument when the transport changes.

---

## 1. The Decision

Fountain Coach SHALL govern distributed participation at the **instrument layer**, not at the transport layer.

A participant does not become a different capability merely because it is reached through RTP, Network MIDI 2.0 UDP, an in-process transport, or a future admitted transport.

The stable contract is:

```text
identity
    ↓
MIDI-CI relationship
    ↓
registered MIDI2 capability
    ↓
typed UMP operation
    ↓
authorization and admission
    ↓
execution lifecycle
    ↓
durable evidence
```

Transport answers a narrower question:

> How are the MIDI2 messages moved between these two admitted endpoints?

Transport SHALL NOT answer:

> Who is this participant?

Transport SHALL NOT answer:

> What may this participant do?

Transport SHALL NOT grant authority.

Transport SHALL NOT redefine the operation vocabulary.

Transport SHALL NOT create a parallel lifecycle.

---

## 2. The Instrument Plane Is the Stable Architecture

The estate's architectural object is the **MIDI2 instrument**.

A governed MIDI2 instrument has, as applicable:

- a stable instrument identity;
- implementation and source provenance;
- MIDI-CI discovery and capability facts;
- registered operation identities;
- typed request, lifecycle, and result envelopes;
- authorization and role requirements;
- Store and evidence obligations;
- transport capabilities;
- lifecycle and revocation state.

Its transport capability is one property of the instrument, not its identity.

Conceptually:

```text
Instrument
├── identity
├── implementation revision
├── MIDI-CI capabilities
├── Profiles
├── Properties
├── operations
├── authority requirements
├── evidence requirements
└── transports
    ├── local
    ├── rtp-ump
    ├── network-midi2-udp
    └── future admitted transport
```

An instrument MAY expose more than one transport.

No transport acquires authority merely by being advertised.

---

## 3. `MIDITransport` Is the Implementation Boundary

The authoritative `Fountain-Coach/midi2` package already contains the correct architectural seam.

A transport implementation conforms to the common MIDI transport contract and delivers UMP between peers.

The existing implementation is conceptually:

```swift
RTPMidiSession : MIDITransport
```

The standards-facing addition SHALL follow the same boundary:

```swift
NetworkMidi2Session : MIDITransport
```

A consumer SHALL depend upon the transport contract where transport independence is required.

It SHALL NOT encode application semantics directly into a particular UDP or RTP implementation.

The intended topology is:

```text
                 MIDI2 / MIDI-CI runtime
                         │
                    MIDITransport
                    ╱          ╲
                   ╱            ╲
        RTPMidiSession      NetworkMidi2Session
               │                  │
        Fountain RTP/UMP      M2-124-UM
               │                  │
              UDP                UDP
```

Estate-specific policy remains above this boundary.

---

## 4. RTP-MIDI2 Remains an Admitted Fountain Transport

This chapter does not deprecate RTP-MIDI2.

The estate has an implemented cross-platform `RTPMidiSession` supporting governed software-peer communication, UMP delivery, explicit peer connection, UDP operation, and peer discovery.

That implementation remains a valid transport.

Its role is now stated precisely:

> RTP-MIDI2 is an implemented Fountain Coach transport profile for carrying the governed MIDI2 instrument plane between software peers.

It is not declared to be the universal definition of MIDI2 networking.

It is not required to masquerade as another transport standard.

It is not required to disappear when another transport becomes available.

The estate MAY continue to use RTP-MIDI2 where its semantics and deployment characteristics are appropriate.

---

## 5. Network MIDI 2.0 UDP Becomes the Standards-Facing Transport Target

The official MIDI Network transport, **M2-124-UM Network MIDI 2.0 over UDP**, SHALL be implemented as a separate transport adapter.

This transport SHALL NOT be introduced by modifying `RTPMidiSession` until it ceases to be recognizably the existing transport.

The implementations SHALL remain distinguishable:

```text
RTPMidiSession
    Fountain RTP/UMP transport

NetworkMidi2Session
    M2-124-UM Network MIDI 2.0 transport
```

`NetworkMidi2Session` SHALL implement the normative M2-124-UM wire contract required for its declared conformance, including the applicable:

- Network MIDI 2.0 discovery;
- session establishment;
- session termination;
- Network MIDI 2.0 command framing;
- UMP data transport;
- packet sequencing;
- loss detection;
- retransmission behavior where implemented by the standard profile;
- error handling;
- interoperability behavior; and
- conformance evidence.

The implementation SHALL make no M2-124-UM conformance claim until independent tests demonstrate the required behavior.

Existing UMP and MIDI-CI correctness SHALL be reused rather than reimplemented inside the transport.

---

## 6. Transport Discovery Is Not Instrument Admission

Network discovery and MIDI-CI discovery have distinct meanings.

Bonjour, DNS-SD, a host address, a UDP listener, an RTP peer, or a Network MIDI 2.0 session MAY make a transport endpoint visible.

That visibility SHALL NOT constitute estate admission.

Chapter 141 remains authoritative.

The sequence is:

```text
transport endpoint visible
          │
          ▼
candidate peer reachable
          │
          ▼
instrument identity established
          │
          ▼
MIDI-CI capability relationship
          │
          ▼
Fountain admission / authorization
          │
          ▼
registered operation available
```

A network session being open is transport evidence.

It is not authority evidence.

---

## 7. MIDI-CI Remains Above Transport Selection

MIDI-CI describes the participant and its MIDI capability relationship.

The transport delivers the messages.

The two SHALL NOT be conflated.

For a remote peer:

```text
transport connectivity
        ↓
instrument discovery
        ↓
MIDI-CI identity / capability exchange
        ↓
operation discovery
        ↓
authorization
        ↓
typed MIDI2 operation
```

Transport negotiation or selection MAY occur before or during this relationship where required by the relevant transport.

It SHALL NOT produce additional application authority.

---

## 8. Transport Capabilities Become Instrument Facts

A joining instrument MAY advertise or expose its supported transport capabilities through the appropriate governed discovery or Property Exchange surface.

Conceptually:

```text
instrument:
  id: fountain.host.ubuntu
  capabilities:
    midi2: true
    midi-ci: true

  transports:
    rtp-ump:
      supported: true

    network-midi2-udp:
      supported: true

    quic:
      supported: false
```

These declarations are capability facts.

They do not determine the selected transport by themselves.

Selection SHALL consider:

- mutual support;
- current network scope;
- security requirements;
- latency requirements;
- reliability semantics;
- interoperability requirements;
- policy;
- deployment context; and
- acceptance status.

A transport that is implemented but not accepted for a particular environment SHALL NOT be selected merely because both endpoints support it.

---

## 9. Transport Selection Must Not Change Operation Semantics

For a given governed operation, transport selection SHALL NOT alter:

- the operation identity;
- request meaning;
- authorization requirements;
- correlation identity;
- idempotency rules;
- lifecycle vocabulary;
- completion semantics;
- cancellation semantics;
- Store receipt requirements; or
- terminal evidence.

The desired invariant is:

```text
same instrument
+
same operation
+
same authority
+
different admitted transport
=
same governed behavior
```

Transport-specific metrics MAY differ.

Transport-specific connection state MAY differ.

Application semantics SHALL NOT.

---

## 10. Reliability Is an Operation Requirement, Not a Global Transport Myth

Not every MIDI2 message has the same delivery requirement.

The estate SHALL distinguish ephemeral realtime communication from durable state-changing operations.

Examples include:

```text
ephemeral
    controller movement
    monitoring telemetry
    transient timing/event traffic

correlated
    request / response
    operation lifecycle
    progress

durable
    authorization-changing operations
    Property Exchange state changes
    deployment mutation
    terminal receipts
```

A transport MAY provide reliability directly.

A higher layer MAY provide correlation, retry, idempotency, or durable settlement.

The estate SHALL NOT pretend that every message requires reliable ordered delivery.

It SHALL also not pretend that packet delivery alone proves completion of a durable operation.

The terminal Store/evidence contract remains authoritative.

---

## 11. CodexKit Demonstrates Why This Separation Matters

Chapter 88 establishes CodexKit as the governed boundary around the Codex app-server.

The app-server uses its native protocol behind CodexKit.

The governed estate-facing boundary is MIDI2.

The relationship remains:

```text
Reframe / MIDI2 peer
          │
          ▼
     CodexKit instrument
          │
          ▼
 JSON-RPC adapter / façade
          │
          ▼
   Codex app-server
```

JSON-RPC is therefore not a competing estate transport architecture.

It is the backend protocol spoken by CodexKit to the runtime it governs.

CodexKit translates between that runtime protocol and the estate's registered MIDI2 operation plane.

The remote path becomes:

```text
Reframe instrument
       │
       │ admitted MIDITransport
       ▼
CodexKit instrument
       │
       │ typed MIDI2 operation
       ▼
CodexKit adapter
       │
       │ JSON-RPC
       ▼
Codex app-server
```

Changing the network transport between Reframe and CodexKit SHALL NOT require changing Codex's JSON-RPC protocol.

Changing the Codex app-server protocol SHALL NOT require redefining the network transport.

This separation is intentional.

---

## 12. Amendment to Chapter 149

Chapter 149 establishes Reframe and a remote CodexKit execution environment as governed MIDI2 peer instruments.

That decision remains in force.

Its transport statement is refined by this chapter.

Where Chapter 149 describes RTP-MIDI2 as the normal remote transport, the normative interpretation after this chapter SHALL be:

> RTP-MIDI2 is the current implemented and accepted remote transport for that relationship. The peer relationship itself is defined at the governed MIDI2 instrument plane and MAY operate over another transport admitted under Chapter 150.

Thus:

```text
Chapter 149 implementation profile

Reframe
   │
   │ RTPMidiSession
   ▼
CodexKit
```

becomes a concrete instance of the more general governed relationship:

```text
Chapter 150 architecture

Reframe
   │
   │ admitted MIDITransport
   ▼
CodexKit
```

No Chapter 149 authority is lost.

Transport becomes explicitly replaceable.

---

## 13. Local Transport Remains a Valid Optimization

Transport neutrality applies locally as well as remotely.

A process-local or same-host adapter MAY avoid network serialization where useful.

It SHALL still converge on the same registered operation executor and lifecycle.

A local optimization SHALL NOT establish a privileged hidden command plane.

Conceptually:

```text
                MIDITransport
            ╱        │        ╲
           ╱         │         ╲
       local      RTP/UMP    M2-124
```

The observable governed operation remains equivalent.

---

## 14. Future Transports

Future transport adapters MAY include technologies such as QUIC or WebTransport if a governed requirement justifies them.

No speculative transport SHALL become architectural authority merely because it is technically attractive.

A new transport requires:

1. a named transport contract;
2. a threat and authority analysis;
3. explicit delivery semantics;
4. implementation beneath `MIDITransport`;
5. cross-peer tests;
6. failure and cancellation tests;
7. evidence that operation semantics remain unchanged;
8. declared scope;
9. acceptance scenarios; and
10. governance admission.

The transport SHALL solve a demonstrated transport problem.

It SHALL NOT create another command vocabulary.

---

## 15. Security Boundary

Transport security and instrument authority are separate but composable concerns.

Where a transport provides encryption, authentication, integrity, or peer identity, those properties SHALL be consumed as transport evidence.

They SHALL NOT silently replace:

- FountainAuthKit;
- machine admission;
- instrument admission;
- MIDI-CI identity;
- operation authorization;
- Store receipts; or
- deployment authority.

Likewise, an authorized instrument SHALL NOT cause an insecure transport to be considered secure.

Security claims SHALL name the layer they apply to.

---

## 16. Acceptance Matrix

Transport acceptance SHALL be explicit.

At minimum, governance SHALL be able to distinguish:

| State | Meaning |
|---|---|
| declared | transport contract exists |
| implemented | code exists |
| unit-tested | encoder/decoder and local behavior tested |
| peer-tested | two independent endpoints communicate |
| cross-platform-tested | required platforms interoperate |
| standards-tested | normative standard behavior demonstrated |
| instrument-integrated | MIDI-CI and operations cross the transport |
| live-accepted | a governed scenario proves terminal behavior |

A transport SHALL NOT be described as standards-conformant merely because UMP packets cross UDP.

A transport SHALL NOT be described as live-accepted because a socket opened.

---

## 17. Immediate Implementation Work Item

The next implementation work item is:

```text
NetworkMidi2Session : MIDITransport
```

within the authoritative Fountain Coach MIDI2 package.

Its first scope SHALL be intentionally narrow:

1. represent M2-124-UM session state;
2. implement Network MIDI 2.0 discovery;
3. establish two software-peer sessions;
4. encode and decode the required Network MIDI 2.0 commands;
5. transport existing UMP values without changing the MIDI2 core;
6. implement the required sequencing and recovery behavior;
7. expose received UMP through the existing transport callback boundary;
8. add deterministic loopback and two-peer tests;
9. add cross-platform tests where supported;
10. add M2-124-UM to the conformance ledger without claiming completion prematurely.

The existing `RTPMidiSession` SHALL remain operational throughout this work.

The implementation SHALL demonstrate coexistence rather than migration-by-destruction.

---

## 18. Required First Acceptance Scenario

The first governed acceptance scenario SHALL prove that the same MIDI2 operation can cross two different transports without semantic divergence.

Conceptually:

```text
Run A
Reframe peer
   ↓ RTPMidiSession
Instrument
   ↓
typed terminal result

Run B
Reframe peer
   ↓ NetworkMidi2Session
same Instrument
   ↓
same typed terminal result
```

The evidence SHALL compare:

- instrument identity;
- MIDI-CI capability result;
- operation identity;
- request payload;
- correlation identity class;
- lifecycle sequence;
- terminal semantic result;
- Store receipt shape; and
- transport-specific diagnostics.

The acceptance question is not:

> Did both transports move bytes?

It is:

> Did the same governed instrument operation remain the same operation across both admitted transports?

---

## 19. What This Chapter Does Not Claim

This chapter does not claim that:

- the current `midi2` repository already implements M2-124-UM;
- RTP-MIDI2 conforms to M2-124-UM;
- Network MIDI 2.0 replaces RTP-MIDI2;
- every MIDI2 transport is equally suitable for every network;
- MIDI-CI itself selects the correct transport automatically;
- transport encryption replaces Fountain authorization;
- UDP delivery proves application completion;
- QUIC or WebTransport is currently required;
- physical MIDI2 hardware interoperability follows from software-peer transport tests; or
- a future transport may bypass the universal MIDI2 command plane.

---

## 20. Relationship to Existing Governance

### Chapter 81 — The Universal MIDI2 Command Plane

Chapter 81 remains authoritative for operation semantics.

This chapter places multiple transports beneath that single plane.

### Chapter 88 — CodexKit Is a Governed Codex App-Server Boundary

Chapter 88 remains authoritative for the JSON-RPC boundary.

This chapter makes explicit that JSON-RPC translation and network transport selection are independent concerns.

### Chapter 91 — The FCIS-KIT Instrument Store Is the Capability Plane

Transport support becomes part of the capability facts exposed by an admitted instrument.

It does not become a second capability store.

### Chapter 93 — Instrument Creation Is a Governed Promotion Path

A transport implementation requires the same promotion discipline as other reusable infrastructure.

### Chapter 104 — MIDI2 Event Time, Jitter, and Asynchronous Completion Governance

Timing, completion, cancellation, and asynchronous lifecycle truth remain operation-level governance and SHALL survive transport substitution.

### Chapter 108 — Reframe Is a Swift-Native Cross-Platform Runtime

Transport neutrality makes the cross-host MIDI2 boundary explicit and allows platform-specific transport adapters beneath one portable instrument model.

### Chapter 140 — EstatePublisher Is Codex's Governed IP-Network Topology Mutator

EstatePublisher may configure or expose transport topology.

It does not define instrument semantics or manufacture authority from reachability.

### Chapter 141 — Each Joining Machine Is a Governed MIDI2 Instrument

Machine admission remains the precondition.

A reachable transport endpoint is still not an admitted machine.

### Chapter 142 — FountainAuthKit

Identity and authorization remain independent of transport.

Transport evidence may strengthen authentication but may not replace FountainAuthKit policy.

### Chapter 149 — Remote CodexKit: Reframe and Codex Meet as Governed MIDI2 Peer Instruments

The peer relationship remains.

RTP-MIDI2 becomes its current transport profile rather than its permanent architectural identity.

---

## 21. Architectural Consequence

The estate no longer needs to decide whether RTP, Network MIDI 2.0 UDP, QUIC, or another technology is **the** network.

That is the wrong architectural question.

The governed questions are:

```text
Who is the participant?
    → MIDI2 instrument identity

What can it do?
    → MIDI-CI + registered capability plane

May it do it?
    → admission + authorization

What operation is occurring?
    → typed MIDI2 operation

What became true?
    → lifecycle + FountainStore evidence

How are the packets moving right now?
    → selected MIDITransport
```

This ordering SHALL remain stable.

---

## Governing Sentence

**Fountain Coach governs the instrument, not the wire: MIDI2 identity, MIDI-CI capability, typed operations, authority, lifecycle, and evidence form one stable instrument plane, while RTP-MIDI2, Network MIDI 2.0 UDP, local transport, and future admitted transports remain replaceable carriers beneath the common `MIDITransport` boundary.**
