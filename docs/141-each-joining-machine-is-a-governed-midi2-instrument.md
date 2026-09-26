# Each Joining Machine Is a Governed MIDI2 Instrument

## The decision

MIDI2 is a precondition for admitting a machine to the Fountain Coach local developer cloud. A machine is not an
eligible participant because it answers on an IP address, appears in Bonjour, accepts SSH, or has a familiar name in a
local configuration file. It becomes eligible only when a named, native MIDI2 instrument on that machine has been
created or admitted, started, and proven ready through the governed peer boundary.

This chapter supplies the missing machine-side step before Chapter 140's EstatePublisher joining sequence. It does not
make EstatePublisher guess an installer for an unknown bridge. EstatePublisher is empowered to resolve an unprepared
machine by presenting a typed remediation proposal, asking for consent, and injecting the exact signed artifact declared
by that proposal. It may not silently decide which bridge to install, copy an undeclared executable, or promote a
reachable host by guessing. The machine remains the authority for its own identity and MIDI-CI capability response.

Chapter 143 governs the human-facing security boundary for this promotion. The owner authorizes one bounded bootstrap
session for the declared target, purpose, capabilities, effects, rollback, and expiry. Ordinary operation within that
session produces no repeated Keychain prompt, phone approval, broker approval, or second human authority. A new owner
decision is required only when the trust boundary changes: expiry, revocation, rotation, recovery, scope expansion, or
new-device enrollment. This simplifies the ceremony without weakening artifact signing, identity, target binding,
MIDI-CI readiness, least privilege, or Store evidence.

The governing sequence is:

```text
machine selected by human intent
  → one bounded owner bootstrap/session
  → named MIDI2 instrument contract
  → signed/pinned native instrument artifact
  → device-side installation and launch through its declared host adapter
  → authenticated MIDI2 peer readiness + MIDI-CI capability exchange
  → signed instrument identity and capability receipt in FountainStore
  → EstatePublisher discovery and exact binding
  → enrollment and local-cloud reconciliation
  → estate publication, client, restart, and rollback proof
```

The bootstrap/session is the only recurring human-facing trust decision. The first five machine-side stages are the
admission of the machine as a MIDI2 instrument. The remaining stages are EstatePublisher
operations over that admitted participant. They are related, but they are not one authority and must not be collapsed.

## What “make this machine a MIDI2 instrument” means

The phrase names a governed promotion, not a software metaphor. The machine must expose a device-side instrument with:

- a stable instrument identity and versioned capability contract;
- a signed or otherwise declared release artifact with a digest and source revision;
- an authenticated MIDI2 peer endpoint reachable on the selected network;
- a completed MIDI-CI capability exchange, including the instrument's declared operations;
- a device key or equivalent signed identity that binds the endpoint to the machine-side instrument;
- a typed readiness record persisted in the managed FountainStore; and
- a host-adapter record describing how the instrument starts, stops, survives restart, and is revoked.

The endpoint may be native to the machine or supplied by a separately admitted companion bridge. In the latter case the
bridge is itself the named instrument and carries its own artifact, identity, capabilities, lifecycle, and evidence.
“Bridge” is not a permission to add an ungoverned helper.

## Authority boundaries

| Concern | Authority | Boundary |
| --- | --- | --- |
| Instrument contract and artifact | The declared Swift FCIS/MIDI2 kit and named host adapter | Defines what the machine-side instrument is and how it is versioned. |
| Device readiness | The instrument's MIDI2 peer and MIDI-CI exchange | Proves authenticated reachability and declared capability; it does not authorize cloud enrollment. |
| Durable readiness evidence | FountainStore | Records the signed identity, digest, source revision, endpoint, capabilities, and lifecycle receipts. |
| Network topology and cloud joining | EstatePublisher | Discovers the admitted instrument, binds one exact target, enrolls it, and runs the declared scenario. |
| Credentials and owner approval | SecretStore and one bounded owner bootstrap/session | Supplies references and authorization; secret values never enter requests or public records, and ordinary in-scope operation adds no human prompt. |
| Human intent | The human operator | Names the outcome and approves the exact operation when required; does not invent machine facts. |

Codex reasons over these authorities and submits one typed request. It is not the MIDI2 instrument, the device owner, or
the deployment authority.

## The machine-side promotion path

1. **Select the instrument contract.** Resolve the live kit and host-adapter catalog. The contract must name the MIDI2
   identity, operations, readiness predicates, artifact source, lifecycle, and revocation path. If no named adapter can
   create the instrument on the target platform, stop with `capability-seam-missing`.
2. **Prepare the artifact.** Build or retrieve the exact signed/pinned release through the native Swift release path.
   Record its digest, source revision, kit identity, and target scope. Do not use an ad-hoc shell installer, copied
   binary, guessed URL, or direct SSH mutation as a substitute.
3. **Install through the declared host adapter.** The adapter owns the device-side install, identity custody, service
   registration, and rollback. The canonical remote chain remains `ReframeLaunch → ReframeScenarioRunner →
   ReframePeer → fountainstore.remote.install → FountainCoachMaintenanceKit`; a different path is valid only when a
   separately named native adapter declares it.
4. **Start and admit the peer.** The machine-side instrument binds its governed MIDI2 endpoint, presents its signed
   identity, and completes MIDI-CI capability exchange. A port number, socket, process, or packet is not readiness by
   itself; the typed readiness record must bind the endpoint to the instrument PID/process, artifact, Store, and source
   revision where those fields apply.
5. **Persist readiness.** Write and read back one correlated FountainStore receipt containing instrument identity,
   endpoint, MIDI-CI capabilities, artifact digest, source revision, host lifecycle, and revocation information. This
   receipt is the input to EstatePublisher discovery; a scan cannot manufacture it.
6. **Hand off to Chapter 140.** EstatePublisher scans the network, correlates the discovered endpoint with the admitted
   MIDI2 identity, binds exactly one target, and only then proceeds to enrollment, gateway reconciliation, publication,
   client verification, restart persistence, and rollback.

## Admission predicates and refusal states

The machine-side promotion is admitted only when all of these predicates are observed in one correlated run:

| Predicate | Required proof | Refusal |
| --- | --- | --- |
| Consent | One bounded owner bootstrap binds artifact, capabilities, effects, rollback, expiry, target scope, and idempotency; retries within that session do not prompt again | `consent-unproven` |
| Named instrument | Live catalog entry and matching kit/adapter contract | `command-surface-insufficient` or `capability-seam-missing` |
| Artifact | Signed/pinned release, digest, and source revision | `artifact-unproven` |
| Identity | Signed device/instrument identity bound to the target | `identity-unproven` or `identity-mismatch` |
| MIDI2 peer | Authenticated endpoint and typed readiness | `midi2-not-ready` |
| MIDI-CI | Required capability exchange and declared operations | `midi-ci-incomplete` |
| Store | Correlated FountainStore readiness receipt and read-back | `readiness-unpersisted` |
| Lifecycle | Start/restart/revoke behavior owned by the host adapter | `lifecycle-unproven` |

Any refusal is terminal for that attempt, not terminal for the joining effort. EstatePublisher must not bind, enroll, or
mutate the network after a missing, stale, ambiguous, unsigned, unauthenticated, or mismatched instrument result. It
must instead emit the exact missing predicate as a typed remediation request, offer the signed component or host-adapter
action that can satisfy it, and retry under the existing bounded session. A new owner decision is required only when
the remediation changes the trust boundary; an ordinary retry reuses the existing correlation and idempotency identity
without a password or approval loop. The intended outcome is a prepared and admitted MIDI2 participant, not a polite
refusal report.

## What does not establish instrument admission

The following are observations that may help discovery but are not admission proof: an IP address, TCP/22, SSH config,
DNS or mDNS, a host name, a process list, a listening socket, a Keychain item, a screenshot, an HTTP response, a shell
exit status, or a MIDI packet without authenticated identity and MIDI-CI correlation. These facts must never be promoted
into a host identity or enrollment authorization by reasoning alone.

## Machine-to-machine welcome contract

The machine-to-machine welcome is a bounded bootstrap and conformance sequence. EstatePublisher treats the joining
machine as a black box: it injects only a signed instrument artifact and a typed launch contract; it does not inspect,
pre-seed, or infer the machine's internal Store, MUID, software revision, or device key. The bootstrap decision is made
once for the declared scope; the machine's runtime session carries that authorization until expiry or revocation.

The conceptual state machine is:

```text
PROPOSED → CONSENTED → INSTALLED → IDENTIFIED → ADMITTED → ACTIVE
    ↑          │             │           │
    └─ REMEDIATE ← REFUSED ──┴───────────┴→ REVOKED
```

The bootstrap binds the artifact digest, source revision, requested capabilities, resource/install effects, rollback
identity, target scope, expiry, and idempotency key. The machine's own MIDI-CI instrument owns identity and answers
discovery, profile inquiry, and readiness property exchange. EstatePublisher verifies that response against the signed
artifact, then records and reads back one correlated FountainStore receipt. No SSH reachability, process presence, HTTP
response, or pre-existing Store record is a substitute for that handshake.

This is the governing contract shape, not live acceptance evidence. The current integration has the signed release,
EstatePublisher installation operation, MIDI-CI responder, lifecycle runtime, and typed receipt models. The consent
proposal, black-box bootstrap, real target handshake, and terminal receipt remain acceptance gates; an unmet gate drives
the typed remediation loop rather than ending the membership effort. The loop ends only when the owner explicitly stops,
the target is revoked, or the native adapter proves that the requested participant cannot be made ready.

## Distribution and bootstrap source

The private Fountain Coach GitHub `midi2-gpu-fabric` repository is the distribution source for this joining-machine
implementation. The public `Fountain-Coach/midi2` repository remains the reusable MIDI2/MIDI-CI protocol dependency.
EstatePublisher must consume a signed, immutable release tuple from `midi2-gpu-fabric`: tag and commit, platform
artifact, release manifest, public verification material, artifact digest, service entrypoint, and rollback metadata.
The target needs only the authorized bootstrap channel to fetch and verify that tuple; it does not need to be a MIDI2
participant before installation.

The current GitHub verification is deliberately explicit. `Fountain-Coach/midi2-gpu-fabric` has no published GitHub
release yet. The working tree contains the native joining daemon, signed release manifest, SecretStore-backed release
signer, and EstatePublisher installation verifier, but the release tuple has not yet been promoted to a GitHub release.
The public `Fountain-Coach/midi2` release `v0.11.0` supplies the reusable protocol foundation; it is not the joining
machine release and must not be relabeled as one.

The missing release surface is the smallest next implementation slice: publish the signed joining-machine artifact and
manifest from `midi2-gpu-fabric`, then have EstatePublisher fetch the pinned release, verify the tag/commit, signature,
and digest, install through the declared host adapter, and continue to the machine-owned MIDI2 readiness receipt.
GitHub distributes this implementation; EstatePublisher authorizes installation; MIDI2 proves the running participant.
No live branch, unsigned download, or package-name guess is admissible.

## Acceptance proof

The chapter is implemented when the repository has a native scenario or kit contract that names the machine-side
instrument promotion and its terminal predicates, and one bounded acceptance run can correlate:

1. the exact instrument contract, artifact digest, source revision, and host adapter;
2. authenticated MIDI2 readiness, signed identity, and MIDI-CI capabilities;
3. FountainStore readiness write/read-back;
4. EstatePublisher discovery-to-binding correlation against that identity; and
5. downstream enrollment, cloud reconciliation, publication, client, restart, and rollback receipts.

Until that proof exists, the machine is **discovered** or **prepared**, never **admitted**, and no local developer cloud
installation claim may be made. The EstatePublisher path remains active: it diagnoses the missing predicate, proposes the
smallest consented remediation, retries, and continues toward admission. This chapter itself records the governance
boundary; it does not claim that the current machine has been promoted or that a live host has been enrolled. Chapter
143 supplies the human-facing bootstrap/session rule; this chapter supplies the machine identity and readiness proof.

## Relationship to existing governance

Chapter 70 governs external MIDI2 control. Chapters 71 and 72 govern software-peer acceptance and capacity admission.
Chapter 77 governs the Swift/MIDI2 scenario runtime. Chapter 81 governs the universal MIDI2 command plane. Chapter 93
governs instrument creation and promotion, Chapter 97 governs provider-neutral bootstrap and enrollment, Chapter 112
governs kit ownership, and Chapter 121 governs the dynamic instrument factory. Chapter 139 governs owner trust-root
custody and recovery. Chapter 140 governs EstatePublisher's discovery, binding, topology mutation, publication, and
proof after this machine-side precondition has passed.

## Governing sentence

**A machine joins the Fountain Coach estate only after a named native MIDI2 instrument on that machine proves its signed
identity, authenticated peer readiness, MIDI-CI capabilities, and durable FountainStore lifecycle; EstatePublisher may
then bind and operate that admitted instrument, but it may never turn network presence into admission.**
