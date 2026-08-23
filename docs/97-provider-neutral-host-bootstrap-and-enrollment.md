# Provider-Neutral Host Bootstrap and Enrollment

> Governance chapter: 97. This chapter defines how an Ubuntu host becomes a managed Fountain Coach host without
> making SSH a writer-facing dependency. It governs the bootstrap and enrollment boundary; it does not claim that a
> Hetzner or AWS host, host agent, enrollment service, or production deployment is currently implemented.

## The decision

Fountain Coach separates initial host bootstrap from ordinary host operation. A new or rebuilt Linux host may be
initialized by its infrastructure provider through a first-boot mechanism such as cloud-init. The resulting host
agent then enrolls with Fountain Coach and exposes a narrowly scoped, authenticated operation surface.

The normal writer-facing path is:

```text
provider provisioning API → first-boot bootstrap → host identity verification
→ one-time enrollment → scoped host credential in SecretStore
→ HTTPS host-agent operation → FountainStore receipt
```

SSH may remain an owner-only emergency or recovery channel, but it is not the normal Reframe operation path and is
never required of a writer. A provider API token is not a substitute for the host-agent credential: the provider
creates or configures infrastructure, while the host agent admits and operates the FountainStore release.

## What this governs

This chapter applies to:

- first-boot installation of the FountainStore host agent;
- provider-neutral host identity and enrollment;
- scoped host-agent credentials, rotation, expiry, and revocation;
- provider adapters for Hetzner Cloud, AWS, and later providers;
- migration of an existing host into the enrolled model;
- the Copilot and SecretStore projection of host authorization; and
- bootstrap, enrollment, readiness, rollback, and recovery evidence.

It does not authorize arbitrary host discovery, provider-wide scanning, a new persistence engine, public unauthenticated
host APIs, automatic Store replacement, or the placement of long-lived credentials in cloud-init user data.

## Authority boundaries

| Boundary | Authority |
| --- | --- |
| Infrastructure creation and network attachment | Named provider adapter |
| First-boot delivery | Provider launch template, image, or cloud-init boundary |
| Host identity and agent lifecycle | FountainStore host agent |
| Enrollment authority | Fountain Coach enrollment service and owner-controlled registry |
| Credential custody | SecretStore / Keychain-backed host adapter |
| Installation and rollback | Enrolled host agent plus named release authority |
| Writer explanation and confirmation | Reframe Copilot |
| Durable operation and enrollment evidence | FountainStore |
| TLS and public ingress | Host/TLS boundary governed separately by Chapters 94–96 |

No provider adapter may silently become the enrollment authority. No host agent may enroll itself merely because it can
reach an endpoint. No local instrument may infer enrollment from a successful process connection.

## Bootstrap is not enrollment

Bootstrap installs the candidate agent and supplies enough information for it to request enrollment. Enrollment is the
explicit trust transition that records the host identity, permitted scope, release channel, and revocation authority.

The bootstrap artifact MUST be reproducible, signed or otherwise pinned, and bound to:

- the provider and exact target identity;
- the FountainStore host-agent version and digest;
- the enrollment endpoint and protocol version;
- a short-lived, one-time enrollment transaction;
- the requested operation scope; and
- the owner or release authority that may revoke it.

Cloud-init user data, launch-template data, and provider metadata are bootstrap inputs, not durable secret stores.
They MUST NOT contain a long-lived SSH private key, provider master token, host-agent bearer token, or unrelated
application credential. A one-time enrollment value may be delivered only when it is scoped, expiring, single-use,
redacted from logs, and invalidated after successful enrollment or timeout.

## Provider adapters

The reusable host contract is provider-neutral. Provider adapters implement only the infrastructure-specific work:

```text
provider account → instance/image/network → bootstrap input → provider receipt
```

For Hetzner Cloud, the adapter may create an Ubuntu server and attach cloud-init user data. For AWS, the adapter may
use EC2 launch configuration, user data, launch templates, an instance profile, or an equivalent first-boot boundary.
The adapter must not assume that a Hetzner project token and an AWS IAM role have the same custody or scope.

Provider credentials remain in SecretStore-backed adapters. They never cross into cloud-init as reusable credentials,
MIDI2 envelopes, Copilot prompts, FountainStore documents, logs, or public publication.

## Existing-host migration without SSH

An existing host that was not bootstrapped with an enrollment contract cannot be declared enrolled from a health
response alone. Its supported migration choices are:

1. a provider-controlled console or recovery boundary that runs the signed bootstrap once; or
2. replacement from a verified image with the existing Store preserved through an explicitly checked volume/backup
   migration.

The migration scenario MUST bind the old and new Store identities, prove the release and backup lineage, and retain a
rollback path. It MUST NOT silently reinitialize the Store or copy credentials through a Mac user account.

## Enrollment lifecycle

The host registry and Store receipts use explicit states:

```text
candidate → bootstrapped → identity-pending → enrollment-pending
→ enrolled → ready → revoked | expired | refused | failed
```

Enrollment is terminal only when the registry and FountainStore contain matching identities and the host agent proves:

- the exact target identity;
- the enrolled agent build and digest;
- the protocol and capability version;
- the allowed operation scope;
- credential expiry and rotation state;
- TLS/transport identity where applicable; and
- the revocation and rollback authority.

Reachability, a provider API success, a cloud-init completion marker, or a live health endpoint is not enrollment proof.

## Host-agent operation contract

After enrollment, Reframe uses the named host-agent contract for bounded operations such as:

```text
host.status
fountainstore.remote.install
host.rollback
host.revoke
```

Every request carries the enrolled host identity, operation version, exact target, artifact version, source revision,
digest, scope, idempotency key, expiry, and evidence requirement. Credentials are presented by the host adapter and
are never request fields. The host agent verifies the signed artifact and target before mutation, stages into a
non-active location, reports authenticated readiness, and retains the previous release for rollback.

The host API MUST reject replayed, expired, wrong-target, wrong-scope, unsigned, or digest-mismatched requests. A
provider API response cannot stand in for the host-agent receipt.

## Copilot and SecretStore surface

Copilot teaches the writer only the safe state:

- “The staging host is enrolled and ready.”
- “The staging host authorization is missing or expired.”
- “The host identity changed; operation refused.”
- “The host is ready for a pinned release.”

When enrollment or credential setup is required, Copilot opens a protected native setup surface. It may show host
name, provider, scope, expiry, public-key or certificate fingerprint, and readiness state. It must not ask the writer
to paste a private key or token into chat, reveal Keychain internals as a manual procedure, or expose cloud-init user
data as an operational instruction.

SecretStore stores the scoped host credential and enrollment metadata. Rotation replaces the credential atomically;
revocation makes the old credential unusable and records the reason and authority. Possession of a valid credential is
not consent to mutate a host; mutating installation still requires explicit confirmation.

## Evidence and claims

| Claim | Required evidence |
| --- | --- |
| bootstrap was requested | provider plan and pinned bootstrap descriptor |
| agent was installed | signed artifact, target identity, and first-boot receipt |
| host was enrolled | registry receipt plus Store identity and agent identity match |
| host is ready | authenticated host-agent readiness and Store/lease proof |
| release was installed | signed artifact, digest, staging, activation, and rollback receipt |
| credential was rotated or revoked | SecretStore outcome and host-agent refusal of the old credential |
| owner-controlled operational production | Chapter 94 requirements plus enrolled-host live acceptance |
| security-reviewed/public production | operational evidence plus independent external review; not implied by enrollment |

Each finding is marked observed, inferred, or not established. A cloud-init log, provider response, screenshot, or
process listing alone cannot establish enrollment, readiness, release activation, or rollback.

## Governing sentence

**A host becomes a managed Fountain Coach host through a signed, provider-delivered bootstrap followed by an explicit,
scoped, revocable enrollment; after that transition, Copilot uses the enrolled host-agent contract and SecretStore—not
writer-managed SSH—to operate FountainStore.**
