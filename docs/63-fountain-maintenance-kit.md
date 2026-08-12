# FountainMaintenanceKit — Portable Swift Maintenance Contract

> Chapter status: package boundary and Reframe client-side SecretStore transport are implemented; hosted maintenance
> remains incomplete. The published `Fountain-Coach/FountainMaintenanceKit` `v0.2.0` release provides the core, typed
> client, ephemeral secret-provider boundary, and offline test kit. Reframe's macOS adapter reads the configured
> maintenance credential through `swift-secretstore` and releases it only while the authenticated request is sent.
> The Book Library now has a digest-backed server verifier; production deployment binding, native Git, and remote
> rollout evidence remain open gates.

The maintenance seam must not be reimplemented separately in Reframe, a publishing skill, and the Book Library host.
Those clients need one typed contract, one authority chain, one receipt vocabulary, and one portability boundary. This
chapter therefore establishes the proposed Swift package repository:

```text
Fountain-Coach/FountainMaintenanceKit
```

The package is the reusable control-plane core. It is not FountainStore, not the Book Library catalog, not Reframe's
Copilot, and not a replacement for the MIDI backplane IDL. It connects those authorities without making any of them
secretly responsible for deployment.

## Decision and claim

`FountainMaintenanceKit` is a Swift Package Manager repository governed by FCIS. Its supported portability claim is
the intersection of its declared Swift toolchain, platform profiles, and adapter implementations. The initial profiles
are macOS for Reframe and Linux for the hosted Book Library. A container or another host is a new profile with explicit
build, security, migration, and acceptance evidence.

“Pure Swift” means that the authority and domain contract are implemented in portable Swift. It does not mean that a
kernel, TLS stack, filesystem, process supervisor, DNS provider, or cloud host disappears. Those are injected platform
adapters. An adapter may use a host facility; it may not redefine the contract, identity, authorization, or receipt.

## Package boundary

The published repository contains these independently testable layers:

- `FountainMaintenanceCore` — operation IDs, target and scope types, authorization decisions, confirmation policy,
  idempotency, progress phases, terminal receipts, release/candidate identities, rollback state, and migration
  manifests.
- `FountainMaintenanceClient` — the versioned typed client used by Reframe and the local maintenance skill. It
  carries no deployment authority and exposes no raw credential value to callers. Its `MaintenanceSecretProvider`
  releases a value only inside the transport closure; the request model and receipt remain reference-only.
- `FountainMaintenanceServer` — portable request validation, authorization handoff, operation lifecycle, receipt
  handling, and capability/telemetry projection for a host implementation.
- `FountainMaintenanceSecretStore` — protocols for opaque SecretStore references, explicit resolution, denial,
  expiry, rotation, and redaction. The package never persists the resolved secret.
- `FountainMaintenanceAdapters` — protocols and implementations for persistence, network/TLS, process supervision,
  filesystem layout, DNS/edge publication, and Git. Host-specific code stays behind these seams.
- `FountainMaintenanceTestKit` — deterministic fixtures for authorization, idempotency, promotion, rollback,
  migration, secret redaction, failure, and resume.

The exact module names may change during implementation only through a governed amendment. The layering must not:
portable core above replaceable host facilities is the architectural invariant.

## Git and release custody

The package owns the typed repository and release operations needed by the maintenance contract. The preferred backend
is a native Swift Git library with explicit clone, fetch, object verification, ref inspection, bundle/export, and
atomic promotion capabilities. A process invocation of the host `git` executable is a transitional compatibility
adapter only; it must be labeled, observable, test-covered, and excluded from the authority claim. It must not be
silently selected when a native backend is required by the active platform profile.

The package never guesses a repository from a directory scan. Repository identity, provider, commit, candidate,
release, and migration identities are explicit and host-independent. The Book Library host remains publication
authority; Reframe remains writer/editor and mediator; FountainStore remains Reframe behavioral proof.

## Maintenance operation contract

Every operation request declares operation identity, actor, target alias, requested scope, expected provider/repository
revision, SecretStore reference label where required, confirmation state, idempotency key, and requested capability.
Every receipt declares the same operation identity, authorization decision, release transition, verification probes,
failure or rollback detail, and terminal state. No request, receipt, telemetry event, fixture, or AX projection may
contain a token, private key, certificate, prompt, manuscript text, or unrestricted host output.

The server is the authorization authority. A client can prepare and submit a request; it cannot self-approve it. The
server must reject scope mismatch, stale revision, duplicate release, expired or revoked credential, and failed
post-switch verification. Repeating an idempotency key retrieves or resumes the existing operation rather than creating
an accidental second mutation.

## SecretStore and Preferences

Reframe's Accounts & Storage surface stores only facts: endpoint, account/project identity, platform profile, TLS
identity policy, and an opaque SecretStore item reference. It does not store a key, token, private key, or standing
permission. A SecretStore prompt, denial, expiry, or rotation is a visible state and a valid terminal boundary.

`FountainMaintenanceKit` receives a `MaintenanceSecretProvider`, not a platform Keychain object. Reframe now supplies
the macOS implementation through `swift-secretstore`; tests supply a deterministic denial/redaction fixture. The Book
Library now supplies a host-side digest verifier: production configuration provides the SHA-256 digest, while the
incoming bearer value is compared in constant time and never persisted. The server labels an absent verifier as
fixture-only mode; hosted deployment must configure it. The same operation contract and redaction rules apply in every
profile.

## FCIS and repository requirements

The repository must ship the FCIS instruction and evidence surface appropriate to a reusable library: `AGENTS.md`,
`PLANS.md`, `SOURCE.md`, `README.md`, license and security policy, `FCIS_AUDIT.md`, `FCIS_COMPLIANCE_PLAN.md`,
generated contract/reasoning artifacts where applicable, and a release manifest. Changes to contract inputs regenerate
tracked artifacts before implementation is considered consistent. Telemetry follows the governed schema; operation
events, chunk/resume rules, budgets, and terminal receipts remain enabled where the host runtime requires them.

The MIDI backplane IDL remains the sole MIDI contract and is not replaced by an OpenAPI document. A maintenance HTTP
or native transport is a service-owned typed boundary. Reframe's consumer-side capability registry, FountainStore
effects, AX labels/actions, and live-drive evidence remain governed in the consuming repository.

AX is not a requirement for the headless package itself. It is mandatory at the Reframe Preferences, Copilot, and
activity surfaces that consume this package: every operation state offered to a writer or agent must be exposed with
role, label, value, actions, progress, cancellation/resume, and terminal result.

## Platform profiles and migration

Each profile declares:

- Swift toolchain and supported OS/runtime versions;
- network and TLS implementation;
- persistent receipt/release store;
- filesystem and supervisor adapter;
- DNS/edge publication adapter, if applicable;
- Git backend and its verification evidence;
- build, test, security, migration, and rollback evidence.

The portable migration package contains release manifests, source and normalized digests, repository refs or Git
bundles, configuration templates, endpoint indirection, rollback metadata, and instructions for rebinding SecretStore
references. It never contains secret values. Moving from Hetzner to another host changes profile bindings and endpoint
configuration, not operation, candidate, release, or receipt identities.

## Remaining implementation and acceptance gates

The package and client-side SecretStore boundary are ready for integration. The full maintenance capability is not ready until
all of the following exist:

1. Core codec and state-machine tests prove typed validation, idempotency, authorization, redaction, cancellation,
   resume, rollback, and migration behavior.
2. macOS and Linux profile builds run the same core fixture suite; adapter-specific differences are explicit.
3. Native Swift Git or the explicitly named transitional adapter proves commit/ref/object verification and atomic
   release transitions without directory guessing.
4. A local fixture server and the hosted Book Library server return the same typed receipts for the same scenario.
5. Reframe and the maintenance skill consume the same client contract; Reframe's provider and the Book Library
   verifier do not leak the secret;
   no normal path uses guessed SSH, shell, or
   filesystem mutation.
6. Reframe acceptance proves Preferences/SecretStore denial, confirmation, AX activity, FountainStore proof,
   successful promotion, failed verification with rollback, and host migration.
7. Release provenance names the package revision, platform profile, adapter set, and test evidence. Until these gates
   are met, Chapter 62's hosted maintenance API remains a governance target rather than a shipped capability.

**Governing sentence:** `FountainMaintenanceKit` is the portable Swift contract and receipt authority for Reframe's
authenticated maintenance seam; SecretStore supplies opaque credentials, host facilities are replaceable adapters,
Reframe and skills are equal clients, and no platform or “pure Swift” claim exceeds its declared profile evidence.
