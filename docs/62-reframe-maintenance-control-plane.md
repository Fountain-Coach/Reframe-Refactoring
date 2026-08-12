# Reframe Maintenance Control Plane

> Chapter status: governing target. This chapter defines the authenticated maintenance boundary between Reframe,
> the Book Library host, and the deployment tools. It does not claim that the control plane is implemented.

The Book Library is a source provider for the writer. Its public API answers questions about published works and
returns declared source material. Deployment, promotion, rollback, service health, provenance, and migration are
different operations. They belong to an authenticated maintenance control plane and must not be smuggled through the
writer's source API, a shell session, or an agent's private deployment skill.

The current operational failure is therefore architectural, not merely credentialal: Reframe can describe and locally
prepare the full Library round trip, while the remote host has no Reframe-addressable, governed maintenance boundary.
This chapter closes that seam.

## The decision

Reframe owns a writer-facing Maintenance API client and Preferences surface. The Book Library host owns a separate,
authenticated Maintenance API. SecretStore owns credentials. Reframe Copilot and the local maintenance skill are two
clients of the same control plane; neither is allowed to invent a second SSH, filesystem, or deployment grammar.

```text
Reframe Preferences
  endpoint + account + SecretStore reference + disclosure state
                 │
                 ▼
          SecretStore resolves credential
                 │
Reframe Copilot ──┼── local maintenance skill
                 ▼
   authenticated Book Library maintenance API
                 │
       deploy / promote / rollback / verify
                 │
       immutable release + receipt + audit record
                 │
                 ▼
     public read-only library.fountain.coach API
```

The public source API remains read-only from Reframe's perspective. The maintenance API is a separate origin or
explicit control-plane route with separate authentication, authorization, logging, rate limits, and migration rules.
It is not a MIDI backplane topic and does not replace native FountainStore access for Reframe's local behavioral state.

## Rules

1. **Preferences never stores the secret.** Reframe Preferences may store the maintenance endpoint, selected account
   or project, TLS/host identity policy, operation defaults, and an opaque SecretStore item reference. The API key,
   bearer token, private key, certificate, and refresh credential live only in the approved platform SecretStore.
   Preferences, FountainStore, Copilot transcripts, logs, screenshots, and exported manuscripts never contain them.

2. **SecretStore access is explicit and inspectable.** A maintenance operation resolves its credential through the
   configured SecretStore service/key reference. The Preferences UI shows configured, unavailable, denied, expired,
   and rotated states without revealing the value. A Keychain or SecretStore authorization dialog is a first-class
   writer-visible state; Reframe must not treat its absence as success or silently retry with another secret.

3. **The control plane is not the public source API.** Public routes may expose health, catalog, manifests, chapters,
   and published source. Maintenance routes require authenticated, scoped authorization and are never advertised as
   writer source discovery. CORS, caching, robots, and public deployment must not turn a maintenance response into a
   public catalog or credential oracle.

4. **Every operation has a typed contract.** Deployment, candidate promotion, rollback, health verification,
   provenance inspection, migration export, and migration restore each declare arguments, actor, authorization scope,
   confirmation policy, idempotency key, progress phases, cancellation behavior, retry rules, terminal receipt, and
   rollback target. A pasted URL or a successful HTTP status is not an operation result.

5. **Reframe is confirmation-gated.** Copilot may explain the current maintenance state and prepare a proposal on
   device. It may start deployment, promotion, rollback, or migration only after the writer or authorized operator
   confirms the exact target, release/candidate identity, scope, and irreversible consequence. A maintenance
   preference is not standing permission to mutate a remote host.

6. **Authorization is server-owned.** Reframe supplies a credential and requested operation; the server decides
   whether that account may perform it. Promotion requires an authorized approver identity, not merely a non-empty
   text field. The server rejects unknown, expired, over-scoped, or revoked credentials and records the authorization
   decision without storing the credential.

7. **The skill is an adapter, not an authority.** A local publishing or deployment skill may validate provenance,
   call the Maintenance API, poll receipts, and collect evidence. It must use the same endpoint, SecretStore item,
   typed operation, and authorization rules as Reframe. It must not SSH by guess, read a remote repository path as
   authority, mutate Caddy or systemd ad hoc, or bypass an unavailable Reframe capability.

8. **No raw SSH in the writer workflow.** SSH may remain an operator recovery channel outside the writer-facing
   workflow, with host-key verification and a separately governed emergency procedure. Normal Reframe maintenance
   uses the authenticated API so endpoint indirection, audit, authorization, rollback, and migration remain stable
   when the host IP changes.

9. **Release transitions are atomic and reversible.** A deployment or promotion stages an immutable release, verifies
   its manifests, content hashes, executable provenance, configuration, and health, then switches the active release
   atomically. The previous release remains a named rollback target until its retention policy permits removal. A
   failed post-switch probe restores the previous release and returns a failed receipt; it never reports success from
   a partially switched host.

10. **Receipts cross the boundary; secrets do not.** A terminal receipt records operation ID, request and idempotency
    identity, target host alias, provider/repository commit, candidate and release IDs, approver, previous release,
    current release, verification probes, timestamps, and failure/rollback detail. It contains no token, private key,
    certificate, prompt, manuscript text, or unrestricted server output. Reframe persists its sanitized handoff proof
    in FountainStore; the server remains authoritative for deployment state.

11. **The API is host-independent.** Project IDs, candidate IDs, release IDs, content digests, and receipt identities
    never embed an IP address, hostname, absolute path, or machine-specific lease. Endpoint configuration is a
    preference and deployment concern. A migration changes DNS and SecretStore bindings, not the identities in the
    release ledger.

12. **Maintenance is observable through AX.** Preferences exposes endpoint identity, credential reference label,
    authorization state, last verified release, and last error. Copilot activity exposes the target, operation phase,
    confirmation, progress, cancellation/resume state, terminal receipt, and rollback result. AX is the semantic
    authority; a spinner, green HTTP response, or hidden log is not maintenance evidence.

13. **The public source boundary remains deliberate.** A successful deployment does not publish a work. A successful
    candidate promotion does not import a release into Reframe. A health probe does not prove content integrity. Each
    boundary reports its own receipt, and the writer or authorized operator chooses the next transition.

14. **Migration is a first-class operation.** The control plane can produce and verify a migration package containing
    release manifests, source and normalized hashes, Git bundles/refs where applicable, configuration templates,
    endpoint indirection, rollback metadata, and SecretStore re-binding instructions—but never secret values. Restore
    must prove catalog, manifest, source hash, active release, and maintenance health before cutover.

15. **Failure is fail-closed and resumable.** Missing SecretStore access, denied authorization, endpoint mismatch,
    stale candidate, digest mismatch, release collision, failed health probe, or unavailable rollback target stops the
    operation at its owning boundary. The writer sees the precise next action. A retry reuses the idempotency identity
    and polls the existing receipt; it does not create a second deployment by default.

## The minimum maintenance surface

The control plane must provide a typed, versioned surface for at least:

- `health.verify` — service, release, executable, dependency, and content probes;
- `candidate.promote` — explicit approver, candidate identity, new release identity, and rollback target;
- `release.deploy` — reviewed package, target alias, expected provider commit, and post-switch probes;
- `release.rollback` — named previous release and confirmation of the rollback consequence;
- `migration.export` and `migration.restore` — portable package creation and verified restore;
- `receipts.get` — sanitized terminal state for a known operation ID.

This is a contract inventory, not a claim that these capabilities already exist. The generated Reframe capability
registry and server contract become the current member list once implementation begins; this chapter defines what every
member must declare. A new operation is incomplete until its server adapter, SecretStore policy, Reframe capability,
FountainStore receipt, telemetry, AX projection, focused tests, and live acceptance evidence exist together.

## The governing boundary

The maintenance API is a control plane for the service, not a second manuscript surface. Reframe remains the writer's
editor and mediator; the Book Library remains publication authority; FountainStore remains Reframe's behavioral proof;
SecretStore remains credential authority; the remote host remains deployment authority. The control plane joins those
authorities through explicit, authenticated, reversible receipts.

## Acceptance

The chapter is implemented only when a reviewer can observe all of the following:

1. Preferences stores endpoint and SecretStore reference but no credential value.
2. A denied or missing SecretStore authorization remains visibly denied and leaves no successful operation receipt.
3. An authorized promotion reaches a new immutable release through Reframe and the maintenance API, with AX and
   FountainStore evidence agreeing with the server receipt.
4. An unauthorized approver is rejected by the server and surfaced distinctly in Reframe.
5. A failed post-switch verification rolls back to the named previous release.
6. The same release identities survive a host/IP migration and the public source API remains read-only.
7. The local skill and Reframe use the same API contract and cannot silently fall back to guessed SSH or filesystem
   operations.

**Governing sentence:** Preferences selects a maintenance endpoint and SecretStore reference; SecretStore supplies
the credential; the authenticated control plane authorizes and receipts reversible service operations; Reframe and its
skills are equal clients; and no deployment, promotion, rollback, or migration is real until the owning server and
FountainStore both prove it.
