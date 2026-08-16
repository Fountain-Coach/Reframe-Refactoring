# 72 — MIDI2 Peer Projections and Capacity Admission

Chapter 71 defines how two Reframe processes prove a governed MIDI2 software-peer operation. This chapter defines
how that relationship appears inside Reframe and how additional MIDI2 peers are admitted. The projections surface is
the place where peer communication is made visible; it is not a music placeholder, a second Copilot persona, or a
transcript of transport packets.

## The peer model

Reframe is one MIDI2 device implementation among potentially many. The UI therefore models a generic peer endpoint,
not a hard-coded “other Reframe” role. Reframe is the default software-peer fixture because it is the first peer that
can be built, driven, and independently witnessed. A future peer may be another Reframe instance, a software
instrument, a stage system, or a physical device, provided it declares the same negotiated MIDI2 roles and capability
contract.

Every peer instance has its own identity, session, negotiated capabilities, authorization state, lifecycle, transport
health, and resource admission. Instances are clonable at the contract level: a new instance is a new endpoint and
session, never a duplicate of another peer's Store, process identity, or lifecycle.

## The projections surface

The projections area presents the current peer graph and the operation flow crossing it. The default Reframe fixture
may be shown as “Reframe peer”; that label identifies the endpoint, not an actor who speaks to the writer.

For each peer, the accessibility tree exposes at least:

- peer identity and role;
- connection, discovery, authorization, and admission state;
- negotiated capability summary;
- active operation and correlation identity;
- lifecycle state: requested, mediated, awaiting consent, running, completed, refused, failed, or resumed;
- transport/resource health and the reason for any admission refusal.

The projection is derived from negotiated state and FountainStore-backed lifecycle facts. It does not invent progress
from elapsed time, replace the target's AX surface, expose private Store content, or turn internal mediation into an
“Interpreter” or provider ceremony. The writer sees the meaningful peer relationship and result, not the routing
machinery that produced it.

## Admission is capacity-governed

There is no arbitrary fixed instance count in the projection contract. The host admits a peer when the governed
runtime can provide the required process, Store, transport, authorization, provider, and telemetry resources. It
refuses or queues admission with a typed reason when those resources are unavailable. The refusal is a durable,
correlated state, not a silent disappearance from the projection.

An off-machine peer can move execution beyond the local host's CPU, memory, Store, or provider limits, but the remote
transport remains subject to pairing, authorization, bandwidth, latency, reliability, and peer capacity. “Potentially
unbounded off machine” is an architectural possibility, never a claim that any transport or deployment has unlimited
capacity.

Admission does not grant a peer authority to select Reframe's model or lane, bypass consent, write the target Store,
or assert completion. Reframe still performs the mediated capability decision and the target Store remains behavioral
authority.

## Scenario and acceptance gate

The `reframe-to-reframe-storify-source` scenario from Chapter 71 must include the projection contract before its runtime
acceptance is promoted. Its YAML/JSON evidence must identify the peer instance, target instance, projection state,
AX labels/actions, admission decision, resource reason when refused, correlation identity, and separate Store receipts.

The projection implementation is accepted only when:

1. a discovered Reframe peer appears as a generic endpoint with a stable identity;
2. a typed operation changes the projection through the governed lifecycle states;
3. a second peer instance receives a distinct identity and cannot alias the first session or Store;
4. admission refusal or queueing is visible with its typed reason;
5. the projection is truthful through AX and agrees with the target Store and MIDI2 lifecycle events; and
6. an independent window-ID witness confirms the visible projection without treating pixels as semantic authority.

The Book may document the projection contract and a software-peer result only from a complete evidence tuple. It must
not imply that the default Reframe fixture is the only possible peer or that off-machine transport removes capacity
and authorization limits.

## Governing rule

The projections surface is Reframe's visible peer boundary: generic MIDI2 endpoints are discovered and clonable by
contract, Reframe is the default software-peer fixture, and every instance is admitted by live governed capacity.
AX exposes the semantic projection, FountainStore proves behavior, MIDI2 carries the negotiated lifecycle, and no
projection may claim more peers, capacity, or interoperability than the evidence establishes.
