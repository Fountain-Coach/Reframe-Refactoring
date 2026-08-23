# Credentialed Infrastructure Operations and Provider Adapters

> Governance chapter: 94. This chapter defines how Fountain Coach authorizes infrastructure operations through a
> writer-facing Copilot flow, SecretStore, and provider-specific deployment adapters. It does not claim that AWS,
> Hetzner, or any other provider is currently integrated or that a deployment has been performed.

## The decision

Fountain Coach treats cloud authorization and tool installation as a governed infrastructure operation. A writer or
agent may understand and approve the operation through Copilot, but credentials and provider authority remain outside
the local instrument, the reusable FCIS-KIT package, the conversation transcript, and public publication.

The reusable boundary is provider-neutral:

```text
fountain-coach.infrastructure-authorization
```

Provider adapters implement the provider-specific security and API rules:

```text
Hetzner Cloud adapter
AWS adapter
```

The abstraction governs intent, authorization, planning, confirmation, execution, evidence, rollback, and revocation.
It does not pretend that a Hetzner API token and an AWS IAM role have the same security properties.

## What this governs

This chapter applies when Fountain Coach needs to provision or update a host, install a released FCIS-KIT host
service, configure a deployment target, or connect that host to a provider such as the Book Library or Image Cloud.

It governs the infrastructure control plane, not the runtime provider operation itself. The distinction is essential:

| Boundary | Responsibility |
| --- | --- |
| Infrastructure provider | servers, DNS, networks, volumes, firewalls, identity, and deployment targets |
| FCIS-KIT host service | released instruments, host adapters, lifecycle, policy, and runtime evidence |
| Book Library or Image Cloud adapter | provider-specific content or asset operations |
| Local instrument | typed request and redacted result projection |
| Copilot | writer-facing explanation, consent, progress, refusal, and result summary |
| SecretStore | protected credential and secret-reference custody |
| FountainStore | durable operation, authorization, and release receipts |

No layer may silently take authority from another.

## The writer-facing authorization flow

Authorization must be visible to the writer or maintainer in Copilot. A hidden token lookup is not an adequate
operating explanation. Before asking for a credential, Copilot states:

- which provider is involved;
- which resource or host is affected;
- why authorization is required;
- which operations the credential can authorize;
- where the credential will be stored;
- what will not receive the credential; and
- whether the next step is read-only validation or a mutating deployment.

Copilot then follows this sequence:

```text
explain → look up SecretStore → request secure entry if absent → validate read-only
→ show safe authorization facts → present deployment plan → obtain confirmation
→ apply → verify → record receipt → offer rollback or revoke
```

Credential entry belongs in a secure field or native protected surface, never in ordinary chat text. Copilot may show
provider, project, scope, expiry state, resource names, and a non-secret fingerprint. It must never echo the token,
place it in a prompt, or repeat it in a result.

The writer must explicitly confirm a mutating operation. A valid credential does not constitute consent to install or
activate software.

## Provider-neutral operation contract

The capability exposes one governed intent surface with provider adapters behind it. Its operations are:

```text
secret.lookup
authorization.request
authorization.validate
deployment.plan
deployment.confirm
deployment.apply
deployment.verify
deployment.rollback
authorization.revoke
```

Each operation carries a stable capability identity, provider, operation version, target, session, idempotency key,
requested scope, and evidence requirement. Results are redacted and typed. A terminal result must distinguish at
least:

```text
authorized
not-authorized
credential-missing
scope-insufficient
provider-unavailable
plan-ready
confirmation-required
applied
verified
rolled-back
revoked
failed
```

The runtime contract remains the versioned MIDI2/FCIS contract and its generated projections. An OpenAPI document may
describe an HTTP-facing host service for human and tool discovery, but it does not replace the MIDI2 operation contract
or become a second operational vocabulary.

## SecretStore and provider credentials

SecretStore is the custody adapter. It is not the authorization authority and it does not decide what a credential may
do.

For Hetzner Cloud, the adapter may retrieve a narrowly scoped project token from SecretStore and use it only for the
declared infrastructure operation. The token remains in deployment automation and is never sent to a local
instrument or a runtime provider adapter.

For AWS, the preferred design is temporary, federated authorization or an IAM role established for the deployment
operation. Long-lived access keys are an explicit higher-risk exception requiring a separate policy decision, narrow
scope, rotation, and evidence. The AWS adapter must not inherit Hetzner assumptions merely because both providers are
behind the same abstraction.

Secret values MUST NOT appear in:

- MIDI2 requests or events;
- FCIS-KIT artifacts or manifests;
- Copilot prompts or transcripts;
- FountainStore receipts;
- logs, telemetry, screenshots, or AX values;
- Git history or public documentation; or
- deployment command arguments.

Only redacted references, safe metadata, digests, and authorization outcomes may cross those boundaries.

## Installation and promotion on a host

Infrastructure authorization does not itself install an instrument. The host installation is a separate promotion
path:

```text
candidate → signed → uploaded → verified → staged → scenario-tested
→ admitted → active → released
```

The deployment service MUST:

1. build the FCIS-KIT host artifact from a clean, pinned source revision;
2. record its semantic version, source revision, dependencies, permissions, and digest;
3. sign the release manifest and artifact;
4. authenticate the exact deployment target;
5. upload only to a non-active staging location;
6. verify signature, digest, version, permissions, and provider binding on the host;
7. run installation, mock-provider, refusal, replay, timeout, and rollback scenarios;
8. record an admission receipt before activation;
9. activate atomically while retaining the previous release;
10. perform a post-activation health and protocol check; and
11. publish the release result without exposing credentials or private host configuration.

The Hetzner Cloud API or AWS control plane authorizes infrastructure changes. A separate authenticated deployment
channel installs the verified software artifact. Neither provider API is allowed to silently install an arbitrary
working-tree copy.

## Local-to-host trust boundary

The local runtime must authenticate the already-admitted host service before sending an instrument request. The
connection must provide peer identity, protocol version, session binding, replay protection, expiry, and idempotency.
The local instrument receives only the operation result and its evidence reference.

The host service owns provider credentials, provider endpoints, host policy, release selection, and deployment state.
The reusable kit owns the typed contract, lifecycle semantics, tests, and host-neutral adapter boundary. Reframe owns
writer intent, Store selection, product policy, and AX projection.

## Evidence and claims

The following claims remain separate:

| Claim | Evidence required |
| --- | --- |
| authorization was requested | Copilot/Store request receipt with redacted scope |
| authorization was validated | provider response and typed validation receipt |
| release was installed | signed artifact, host verification, and activation receipt |
| host is operational | post-activation health and protocol result |
| provider operation succeeded | provider-specific terminal result and Store evidence |
| deployment is secure | independent security review, not merely a passing API call |

A token present in SecretStore, a reachable server, a successful API response, or a generated deployment plan does not
establish the stronger claims above.

Fixtures and mock providers establish contract and lifecycle behavior only. They do not prove access to a real account,
the security of a production deployment, or external service interoperability.

## Provider adapter admission

Each provider adapter must declare:

- provider identity and API version;
- supported authorization methods;
- required scopes or roles;
- secret-store keys or references;
- permitted infrastructure operations;
- data movement and residency boundary;
- refusal and rollback behavior;
- rate, cost, and expiry concerns;
- test and mock-provider scenarios; and
- the independent authority for security and production acceptance.

An adapter is not admitted because its API wrapper compiles. It becomes reusable only after a named, reproducible
release is promoted by its owning authority. Provider support remains proposed until its adapter, scenarios, and
acceptance evidence exist.

## Governance and publication boundary

This chapter governs the infrastructure authorization capability. The status domain may summarize its current state;
the FCIS-KIT documentation may describe the reusable contract; and the governance domain remains authoritative for the
rules and claim boundary.

Public pages may explain the workflow and supported states. They must not publish tokens, project identifiers that are
not intentionally public, host configuration, private deployment paths, or evidence that has not been independently
established.

## Governing sentence

Fountain Coach makes infrastructure authorization inspectable to writers and agents while keeping credentials,
provider authority, installation, and release promotion behind separate governed boundaries; a provider adapter is
reusable only when its named artifact, permissions, scenarios, evidence, and rollback path are explicit.
