# EstatePublisher Is Codex's Governed IP-Network Topology Mutator

> Normative scope: this chapter governs the interaction boundary between a human command, Codex, and EstatePublisher.
> It defines selection, admissibility, IP-network topology mutation, execution, refusal, and evidence. It does not redefine infrastructure
> authorization, publication, SecretStore custody, or host-adapter contracts owned by other chapters.

## The decision

EstatePublisher is the single native topology and deployment mutator that Codex may use when a human requests a governed
operational outcome. Codex is the reasoning client. The human supplies the desired outcome. EstatePublisher is the execution
authority for the admitted IP network: it discovers, binds, reconciles, connects, disconnects, extends, shrinks, and rolls
back declared network topology through typed host adapters. FountainStore is the durable operation and read-back authority. Its enrollment authority accepts or refuses
the signed device enrollment. No agent, conversation, script, or public page may become a parallel deployment
authority.

The governing interaction is:

```text
human outcome
  → Codex reads EstatePublisher's live command surface
  → Codex selects one matching existing operation
  → EstatePublisher validates and executes one typed request
  → EstatePublisher returns a typed terminal result and evidence references
  → Codex reports observed, inferred, and unestablished state
```

## The joining sequence

The machine-side precondition is governed by [Chapter 141](141-each-joining-machine-is-a-governed-midi2-instrument.md):
the target must already be a named, authenticated, signed MIDI2 instrument with a correlated FountainStore readiness
receipt. This chapter begins only after that precondition has passed. EstatePublisher discovers and operates the
instrument; it does not create an unknown bridge as a side effect of network discovery.

The principal interaction is temporal and uncomplicated:

1. The device announces: “I am here.”
2. EstatePublisher discovers that presence.
3. The device exposes its MIDI 2 capability and signed identity.
4. EstatePublisher binds one deterministic candidate.
5. The enrollment authority accepts or refuses that identified device.
6. EstatePublisher sends only admitted typed operations.
7. FountainStore records the result and read-back proof.

Discovery answers **which device is present**. MIDI 2 and MIDI-CI answer **what that device can speak**. Binding answers
**which discovered identity is the intended target**. Enrollment answers **whether that identified target may join**.
Operation answers **what the admitted target may do**. Proof answers **what actually happened**. No later answer is
silently assumed from an earlier one.

## Authority boundaries

| Participant | Authority | Prohibition |
| --- | --- | --- |
| Human | States the desired outcome and approves or rejects the exact named operation when required. | Must not provide guessed topology, credentials, host keys, release data, or DNS edits. |
| Codex or another capable agent | Grounds the request against the live EstatePublisher catalog and submits one typed request. | Must not invent commands, self-authorize, execute deployment steps directly, or claim proof from prose. |
| EstatePublisher | Validates, binds, dispatches, reconciles, records, and returns the operation result through native Swift adapters. | Must not guess targets, bypass strict host verification, expose secrets, or create a second authority. |
| FountainStore | Persists operation records, receipts, and typed read-back. | Must not be treated as live discovery merely because a record exists. |

## Human command contract

The human command is an outcome, not an infrastructure questionnaire:

> “Add the reachable device to the developer cloud and make the estate available to its browser clients.”

Codex MUST translate that outcome only through the current EstatePublisher command catalog. If no existing command
matches, Codex MUST report that the surface is insufficient. The human is never asked to author machine facts. If an
operation requires approval, EstatePublisher MUST present the exact target, scope, effect, and recovery path in plain
language; the human supplies only a yes/no decision.

## Capability selection

| Outcome requested by the human | Existing EstatePublisher surface | Required result |
| --- | --- | --- |
| Inspect the available command and adapter surface | `--inspect --strict`, `--commands` | Current catalog and conformance result. |
| Discover reachable deployment candidates | `--scan-local-developer-cloud` | In-memory enumeration followed by a redacted FountainStore scan record. |
| Read previously recorded deployment facts | `--collect-local-developer-cloud-from-store` | Explicit Store read-back, clearly separated from live discovery. |
| Enroll a discovered device | `--enroll-create`, `--enroll-authorize`, `--enroll-submit`, `--record-enrolled-connection` | Signed request, external admission result, and managed connection receipt. |
| Install or reconcile a managed local cloud | `--run-local-developer-cloud-supply-chain`, `--run-local-developer-cloud-from-store`, `--reconcile-local-developer-cloud` | Typed installation or reconciliation result with release, host, Store, and rollback evidence. |
| Publish a reviewed estate route | `--publish` / `estate.publication.sync` | Route-scoped signed publication and typed remote read-back. |
| Record the deployment situation in an FCIS repository | `--update-deployment-agents` | Bounded `AGENTS.md` update; Reframe and self-implementation are rejected as authorities. |

The catalog is authoritative. Command names, remembered history, implementation convenience, and similar operations
are not permission to select a different command.

## Implementation contract

This chapter gives an implementing agent a bounded order of work. It does not require the agent to guess runtime
facts, and it does not turn an absent fact into a policy choice.

1. Read the current `EstatePublisher --inspect --strict` and `EstatePublisher --commands` output. If the selected
   operation is absent, stop with `command-surface-insufficient`; do not add a command merely because this chapter
   names an outcome.
2. Resolve the operation's declared Swift kit contract and host adapter. The implementation seam is the existing
   typed adapter; a missing kit contract or adapter is `capability-seam-missing`, not an invitation to create a
   script, generic server, or second authority.
3. Select the matching compiled scenario by exact capability, operation, scope, and terminal predicates. The
   scenario is the acceptance source. A scenario with a different identity, stale platform assumptions, or missing
   predicates is `scenario-mismatch` and must be repaired before mutation.
4. Read the explicit FountainStore intent and current records. A stored record may be reused only when its identity,
   target, authorization, source revision, and evidence binding match the request. Store state is read-back, not live
   discovery.
5. Invoke discovery through the native collector when live facts are required. Keep the enumeration in memory until
   EstatePublisher writes the redacted observation. Bind only deterministically identified candidates; zero or more
   candidates is a normal typed result, while ambiguity is a terminal refusal for that attempt.
6. Compose one typed request and run the existing authorization, SecretStore, release, host, and publication adapters
   in their governed order. Each phase must return its own typed receipt before the next phase can mutate state.
7. Verify the scenario's terminal predicates by correlated FountainStore read-back and the named external witnesses.
   Report each predicate as `observed`, `inferred`, or `unestablished`; do not infer installation from a process exit,
   network packet, screenshot, or generated plan.

The implementation is therefore knowable without pretending that the target is known in advance: the chapter fixes
the authority, order, refusal states, and evidence contract; the live command catalog, typed kit contracts, scenario,
Store records, and admitted host supply the target-specific values.

## Agent execution record

An implementing agent uses the following existing scenario and operation for this capability:

- scenario: `estate-local-wlan-turnkey-access`;
- capability: `fountaincoach.estate-domain-publication@0.1.0`;
- operation: `estate.publication.sync`;
- native workflow entry point: `--install-local-developer-cloud --request <file> --output <file>`;
- active discovery entry point: `--scan-local-developer-cloud --request <file> --output <file>`.

These identifiers are a routing contract, not permission to bypass the live catalog. The agent first verifies them
with `EstatePublisher --inspect --strict` and `EstatePublisher --commands`, then validates the scenario YAML and its
checked JSON projection. If the catalog, scenario identity, or projection does not agree, the agent stops with a
typed `command-surface-insufficient` or `scenario-mismatch` result before mutation.

The typed installation request is complete only when it carries these references and values:

| Request member | Required meaning | Source of truth |
| --- | --- | --- |
| operation, scenario, correlation, and idempotency identity | One named operation and one resumable run | EstatePublisher catalog and compiled scenario |
| domain pattern/prefix and complete manifest identity | The configurable private namespace and the current estate to serve | Request plus `estate/projection-manifest.json` digest |
| discovered candidate and interface inventory | The bound device, host, uplink, management, access, and standby facts | The same-run in-memory scan and its typed Store receipt |
| enrollment and authorization references | Proof that this exact target may join and be operated | FountainStore enrollment authority and owner authorization |
| host-key, SecretStore, release, and source-revision references | Custodied credentials, strict SSH identity, signed artifact, and exact release | Named native adapters; secret values never enter the request |
| gateway policy and recovery identity | Persistent WLAN, DHCP, DNS, NAT, routing, preserved management/internet access, and rollback target | Typed host-adapter contract and prior known-good receipt |

No request member may contain a guessed IP address, device or operating-system name, SSID, interface, router, client,
per-device DNS edit, credential value, host-key value, or hardcoded domain. The collector creates the live inventory in
memory; EstatePublisher validates and binds it; only then is the redacted observation persisted and made an input to
the installation request.

## Phase gates for implementation

The workflow is one EstatePublisher authority with ordered gates. A failed gate is terminal for that attempt; later
phases are not called and the previous known-good state remains available for rollback.

| Phase | EstatePublisher action | Gate before the next phase |
| --- | --- | --- |
| Surface | Inspect commands, kit contracts, and the compiled scenario | Exact operation and scenario agree |
| Discover | Scan reachable presence, MIDI 2/MIDI-CI capability, signed identity, and all policy-relevant interfaces | Complete typed enumeration exists in memory; ambiguity is refused |
| Bind and enroll | Bind one deterministic candidate and submit its signed enrollment request | Enrollment authority returns acceptance for that identity |
| Prepare | Resolve SecretStore references, strict host key, signed release, source revision, domain pattern, and manifest | Every reference is present and exact-target validation passes |
| Reconcile | Invoke the native host adapter for persistent WLAN, DHCP, DNS, NAT, routing, management, and internet access | Typed host read-back proves the declared gateway state |
| Publish | Reuse signed `estate.publication.sync` for the complete current manifest | Store-to-Store receipt, typed remote read-back, and domain/certificate read-back agree |
| Prove | Verify browser-client routes, restart persistence, and rollback | Every scenario terminal predicate is correlated to the same run |

The agent must not treat a plan, process exit, packet, screenshot, or HTTP response as a phase gate. Each gate is a
typed result tied to the correlation identity, target binding, source revision, Store path, and scenario identity.

## Acceptance matrix

The implementation is complete only when the compiled scenario reports `scenario-validation: PASS` and
`scenario-preparation: COMPLETE`, and one correlated run proves all of the following:

| Predicate | Required evidence | Failure classification |
| --- | --- | --- |
| Configuration | Domain pattern/prefix is request-derived and the complete manifest digest is served | `configuration-mismatch` |
| Discovery and binding | Every admitted interface is classified and exactly one target binding is read back | `discovery-incomplete` or `binding-ambiguous` |
| Admission and custody | Signed enrollment, owner authorization, strict host-key verification, and SecretStore references are accepted | `admission-failed` or `credential-invalid` |
| Gateway | WLAN, DHCP, DNS, NAT, estate routing, internet, and management survive host read-back | `host-reconcile-failed` |
| Publication | Native `estate.publication.sync` receipt and typed remote manifest read-back match the source | `publication-unproven` |
| Clients | Browser matrix reaches the estate root and selected subdomains without router or per-device DNS edits | `client-readback-failed` |
| Recovery | Restart restores the gateway and publication; rollback restores the previous known-good release | `persistence-unproven` or `rollback-unproven` |

If any predicate lacks correlated evidence, the result is `BLOCKED`, not a partial installation claim. Invalid
credentials produce one typed refusal and a resumable recovery path; they never start a password retry loop.

## IP-network topology mutation

“Local developer cloud” names the requested deployment profile, not a localhost-only implementation and not a fixed LAN
topology. The governed object is an admitted IP network topology. EstatePublisher may mutate that topology only through
the declared host adapter: it may connect or disconnect an admitted node, extend or shrink an admitted segment, reconcile
uplink, management, access, and standby paths, and publish the resulting estate routes. The adapter discovers actual
interfaces and addresses and applies the declared policy; Chapter 140 never names a router, subnet, interface, SSID,
device, client, or address.

Every topology mutation has a before-state, an intended after-state, an exact target binding, an idempotency identity,
and a rollback state. A mutation is not admitted merely because a host responds on an IP address. EstatePublisher must
prove the resulting routes, preserved management and internet access, and recovery to the prior known-good topology.
The same contract applies whether the admitted network is a private WLAN, another IP segment, or a future provider-neutral
IP transport declared by a host adapter.

## What this chapter supplies and what it does not

This chapter supplies the Codex-facing selection rule, the single-authority rule, the phase order, the refusal
taxonomy, and the evidence vocabulary. It does not supply an IP address, device identity, interface role, WLAN
credential, host key, certificate, source revision, domain value, or approval. Those are facts or authorizations that
must be discovered or resolved through the named native contracts.

The implementation agent closes this boundary by wiring those reads and collectors to the declared typed contracts.
After closure, one EstatePublisher workflow owns the complete sequence: it discovers the reachable device and host
interfaces, binds one deterministic target, composes the authorized request, mutates the admitted IP topology, activates
the persistent gateway, publishes the complete estate, and records every phase in FountainStore. A missing, invalid, ambiguous, or stale
result produces its typed refusal and recovery path; no prose default fills the value.

## Closure state

The implementation is closed when the compiled scenario and the live command surface describe the same operation and
the following state is true for one correlated run:

- the target is a device-neutral, deterministically bound participant with signed identity, a reachable authenticated
  MIDI 2 peer endpoint, and declared capabilities;
- EstatePublisher has discovered and classified every admitted uplink, management, access, and standby interface;
- SecretStore custody, owner authorization, strict host-key verification, signed release, and source revision are
  bound to that target without exposing secret values;
- the native host adapter has activated persistent WLAN, DHCP, DNS, NAT, and estate routing while preserving internet
  and management access;
- the complete current estate manifest is served through the selected configurable domain pattern, without router or
  per-device DNS edits;
- browser clients can reach the estate and selected subdomains, and typed read-back proves the route and certificate;
- restart read-back proves persistence, and rollback read-back proves recovery to the previous known-good release;
- FountainStore contains the correlated receipts, while EstatePublisher remains the only native publication/deployment
  authority.

The closure state is the implementation target, not a claim that a particular live target has already reached it.
Once these predicates pass, the implementing agent reports the correlated result and does not reopen this chapter as a
questionnaire or invent a second workflow.

## Admissibility and refusal

An operation is admissible only when its operation identity, target, scope, source revision, authorization references,
idempotency identity, and evidence requirements are explicit and consistent. EstatePublisher MUST fail closed for an
ambiguous target or device, missing Store authority, invalid credential, stale binding, unverified host key, unsigned
release, incomplete capability data, or failed read-back.

Every refusal is typed, terminal for that attempt, and recoverable without a password loop. The previous known-good
state remains intact. A retry or resume uses the existing idempotency identity; it does not create an overlapping
operation.

## Device and transport neutrality

The joining participant is a device, not a named operating system or vendor. Discovery MAY use Bonjour/mDNS or another
declared provider-neutral transport, but presence alone never makes a device joinable. MIDI 2 is a mandatory joining
capability: the device MUST expose a reachable, authenticated MIDI 2 peer endpoint and answer the required MIDI-CI
capability exchange before EstatePublisher may bind or operate it. The endpoint may be native to the device or supplied
by a separately admitted companion/bridge; EstatePublisher must not silently install one. Neither the discovery
transport nor MIDI-CI is admission, host-key proof, authorization, or Store proof. A target adapter may impose a
declared platform requirement; that rule belongs to the adapter contract and is not hardcoded into this interaction
chapter.

## Evidence and reporting

Codex MUST distinguish:

- **Observed:** present in a typed EstatePublisher result, host read-back, or correlated FountainStore receipt.
- **Inferred:** a reasoned interpretation that is not itself an operational receipt.
- **Unestablished:** required evidence that has not been obtained.

A process exit, screenshot, HTTP response, Bonjour packet, MIDI-CI exchange, generated plan, or command description
alone cannot establish installation, publication, admission, restart persistence, or rollback.

## Concrete enrollment authority

The principal sequence above is the contract. In the current FountainStore implementation, its enrollment step is
provided by the `/enroll/{deviceKeyID}` endpoint. The endpoint is implemented by
`FountainStoreTrustedDeviceEnrollmentService`, verifies the signed request through `MaintenanceEnrollmentAuthority`,
and persists the admitted public key in `maintenance.trusted-devices`. These names identify the current adapter; they
do not change the sequence or make enrollment precede discovery.

## Non-overlap with existing governance

Chapter 94 governs provider-neutral infrastructure authorization and SecretStore-backed credentials. Chapter 92 governs
the publication estate and domain roles. Chapter 112 governs kit ownership. Chapter 134 governs EstatePublisher as the
publication authority. Chapter 139 governs owner trust-root and SecretStore custody. This chapter governs only the
Codex-facing command boundary and implementation order; it delegates those concerns to their own authorities.

## Governing sentence

**On a human command, Codex selects one existing EstatePublisher operation; EstatePublisher alone validates, executes,
records, and reports the governed deployment result, while every infrastructure, credential, publication, and host
authority remains owned by its declared contract.**
