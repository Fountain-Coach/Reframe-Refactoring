# Chapter 96 — SwiftACMEKit Is a Provider-Neutral Certificate Automation Boundary

> Governance chapter: 96. This chapter governs the proposed standalone SwiftACMEKit repository and its use by
> Fountain Coach headless services. It defines a reusable certificate-automation boundary; it does not claim that
> the package, a production certificate, a CA account, or a public ACME deployment already exists.

## The decision

Fountain Coach may create and publish a standalone Swift package under the `Fountain-Coach` GitHub organisation to
automate certificates through the ACME protocol. The proposed repository and package name is:

```text
Fountain-Coach/SwiftACMEKit
```

The package is infrastructure, not an application-specific feature. A Swift server may use it to request, persist,
renew, rotate, and revoke TLS certificates without depending on Caddy, Certbot, shell scripts, OpenSSL command-line
tools, Docker, Python, or a separate certificate daemon.

The first supported authority is an RFC 8555-compatible ACME server, tested against the Let's Encrypt staging
directory before any production issuance. Let's Encrypt is a tested directory configuration, not the package's
protocol identity. The core API remains provider-neutral so another compatible ACME service can be selected through
an explicit directory configuration.

The governing sentence is:

> **SwiftACMEKit may automate certificate lifecycle operations only through an explicit, typed ACME directory,
> protected account and certificate custody, pluggable challenge handling, and independently evidenced issuance,
> renewal, rotation, or revocation; it is not a CA, a TLS server, or a substitute for host security policy.**

## What this chapter governs

This chapter applies to the proposed public Swift package, its platform profiles, host adapters, examples,
documentation, release manifests, and any Fountain Coach server that consumes it. It governs:

- Swift 6 concurrency and the macOS 13+ and Ubuntu/Linux support profiles;
- the portable ACME protocol model and typed lifecycle state machines;
- injected HTTP transport, persistence, cryptography, challenge, clock, and logging boundaries;
- account-key and certificate-key custody, permissions, redaction, rotation, and restart recovery;
- DNS identifier validation, HTTP-01 admission, CSR generation, certificate-chain handling, renewal, and atomic handoff;
- offline unit tests, deterministic mock-server scenarios, opt-in Let's Encrypt staging tests, and release evidence;
- public API compatibility, DocC documentation, SemVer, source licensing, security reporting, and publication claims.

It does not authorize a production CA account, public port binding, DNS changes, automatic firewall changes, a
background renewal daemon, a certificate claim for a domain, or the installation of a server runtime. Those are
separate host and deployment operations governed by Chapter 94 and the owning service's release policy.

## Boundary and package shape

The package must keep protocol authority separate from host facilities. A conforming implementation may use different
target names, but it must preserve these responsibilities:

```text
SwiftACMEKit
├── ACMECore                 directory, resources, identifiers, orders, states, errors
├── ACMEHTTP                 typed request/response and transport protocols
├── ACMEChallenges           challenge selection, presentation, and solver protocols
├── ACMECrypto               JWK, thumbprints, JWS, keys, CSR, and DER primitives
├── ACMECertificateStore     account/certificate persistence and atomic replacement
└── SwiftACMEKit             high-level actor facade and public composition surface
```

The exact decomposition is amendable; the dependency direction is not. Core logic must not depend on SwiftNIO
request/response types. SwiftNIO and `swift-nio-ssl` may be optional adapter targets for server integration and TLS
handoff. The core must remain usable from Foundation/URLSession-based or another injected transport.

The package is not FountainStore, FountainMaintenanceKit, Caddy, Reframe, or the host's TLS listener. A host owns
its scheduling, route binding, certificate activation, policy, and operational receipt. SwiftACMEKit owns the typed
ACME lifecycle it was asked to perform and returns a result that the host can verify and persist.

## Public composition contract

The high-level API must be simple for a server host while leaving lower-level operations available to maintainers. A
compatible shape is:

```swift
public actor ACMEClient {
    public init(
        directory: ACMEDirectoryConfiguration,
        transport: any ACMETransport,
        accountStore: any ACMEAccountStore,
        certificateStore: any ACMECertificateStore,
        challengeResponder: any ACMEChallengeResponder
    )

    public func ensureCertificate(
        for identifiers: [ACMEIdentifier],
        options: CertificateRequestOptions
    ) async throws -> CertificateBundle

    public func renewIfNeeded(
        certificateID: CertificateID,
        policy: RenewalPolicy
    ) async throws -> CertificateBundle?

    public func revokeCertificate(
        certificateID: CertificateID,
        reason: RevocationReason?
    ) async throws
}
```

The final API may improve these names, but it must preserve the separation of directory, transport, account custody,
certificate custody, and challenge response. Public types must be `Sendable` where appropriate and carry explicit
DocC explanations of security-relevant behavior.

## Directory and provider neutrality

`ACMEDirectoryConfiguration` is the provider boundary. It contains an explicit directory URL, terms-of-service
policy, supported algorithm policy, and any compatible metadata needed by the implementation. Built-in presets may
include:

```text
.letsEncryptStaging
.letsEncryptProduction
```

The implementation must discover and validate at least `newNonce`, `newAccount`, `newOrder`, `revokeCert`, and
`keyChange`. Required fields and URLs are validated before use; unknown directory metadata may be preserved without
being promoted to supported behavior.

Let's Encrypt URLs must not be scattered through the core. A different RFC 8555-compatible directory must be
selectable without rewriting order logic. Production selection is an explicit operator decision and is never inferred
from a successful staging test.

## ACME lifecycle authority

The normal issuance flow is a typed state transition, not a Boolean success flag:

```text
directory discovery
→ account load or registration
→ order creation
→ authorization retrieval
→ supported challenge selection
→ challenge presentation and validation
→ CSR generation
→ finalize
→ bounded polling with Retry-After
→ certificate download and chain preservation
→ atomic certificate persistence
→ host verification and optional TLS handoff
```

Order and authorization states must preserve protocol meaning, including `pending`, `ready`, `processing`, `valid`,
`invalid`, `deactivated`, `revoked`, `expired`, and an explicit representation for unknown future values. A protocol
problem is typed and retains RFC 7807/ACME fields (`type`, `detail`, `status`, `instance`, and subproblems) rather
than becoming an opaque string.

The client must honor replay nonces, consume response nonces, retry `badNonce` safely, respect `Retry-After`, bound
polling by a configurable policy, and terminate promptly on cancellation. It must not busy-loop or turn an
intermediate state into issuance success.

## Account, JWS, and key custody

The first account algorithm is ES256 with an EC P-256 key. The model must leave room for other algorithms without
pretending they are supported. New-account requests use a JWK header; existing-account requests use the account `kid`;
both preserve the ACME `nonce`, `url`, payload, and POST-as-GET rules.

JWK public coordinates and base64url encoding are protocol data, not ad-hoc string formatting. Base64url has no
padding and uses the URL-safe alphabet. JWS protected headers and signatures must be generated by tested typed
encoding, with known-vector verification where available. Cryptographic private material never appears in request
models, logs, telemetry, receipts, screenshots, DocC, examples, or errors.

The package receives account-key custody through an explicit `ACMEAccountStore` abstraction. A filesystem profile may
persist an account key and account metadata, but it must use restrictive permissions, atomic replacement, path
validation, and restart-safe recovery. A host may replace this with Keychain, SecretStore, HSM, or another protected
provider through an adapter. The package must not silently read environment variables, unrelated application auth
files, or guessed paths.

## Challenges and identifiers

The first complete challenge is HTTP-01 for normalized DNS identifiers. The package calculates:

```text
keyAuthorization = token + "." + base64url(SHA256(JWK thumbprint input))
```

`ACMEChallengeResponder` presents and removes a typed challenge. An in-memory `HTTP01ChallengeStore` may expose the
response for a host application's `/.well-known/acme-challenge/{token}` route, but the library does not bind port 80
or own the host's HTTP server.

Challenge handling is pluggable. The order state machine must accommodate future `dns-01` and `tls-alpn-01` solvers
without being rewritten, but those solvers remain unsupported until implemented and tested. Wildcards, external
account binding, alternate chains, ARI, OCSP helpers, and additional signing algorithms are future boundaries, not
implicit capabilities.

Malformed or unsafe DNS identifiers are rejected before order creation. Server-provided URLs are validated against the
expected ACME origin and security boundary before following them, unless an explicit protocol rule authorizes the
transition.

## CSR, certificate, and renewal custody

CSR generation is behind a replaceable protocol and initially supports EC P-256 certificate keys, DER encoding, and a
SAN extension containing every requested DNS identifier. The core must not shell out to OpenSSL. If the selected Swift
dependencies do not supply the required X.509/CSR primitives, only the minimal required ASN.1/DER structures may be
implemented, with focused encoding and signature tests.

The returned `CertificateBundle` preserves the leaf certificate, full chain, private key reference/material according
to the selected custody boundary, identifiers, and validity metadata. Account keys and certificate private keys are
separate authorities. A certificate store must support load, atomic save, and remove by typed `CertificateID`; an
interruption must never expose a partially written key, certificate, chain, or metadata file.

Renewal is an explicit API, not an internal timer. `RenewalPolicy` defines a renewal window and bounded jitter;
`needsRenewal` is deterministic for a supplied clock and stored certificate. The host owns scheduling through systemd,
server tasks, or another governed supervisor. Successful renewal exposes enough typed metadata for the host to perform
an atomic TLS identity handoff without coupling the core to `NIOSSLContext` or requiring a process restart.

## Security and operational boundaries

ACME automation is security-sensitive infrastructure. The implementation must use cryptographically secure key
generation, constant-time comparisons where relevant, content-type and response-size validation, timeouts, cancellation,
path-traversal protection, redirect restrictions, and explicit filesystem permissions. It must not overwrite unrelated
files or log secrets.

An ACME account key authorizes requests to a CA account; it is not a Fountain Coach deployment credential. A certificate
private key authorizes a TLS identity; it is not a provider token. Provider credentials remain in SecretStore under
Chapter 94. Host installation, systemd configuration, DNS ownership, firewall rules, and public edge exposure remain
host operations and require their own authorization and evidence.

Copilot-facing or agent-facing explanations must state the directory, identifiers, challenge, requested mutation,
credential custody, and whether the operation is staging or production. Credential presence never equals consent to
issue or install. A valid API response, reachable endpoint, or stored key does not establish secure deployment.

## Verification and evidence

The package must ship a deterministic in-process mock ACME server that can exercise directory discovery, nonces,
accounts, orders, authorizations, HTTP-01, finalization, certificate delivery, `badNonce`, invalid challenges,
`Retry-After`, cancellation, and typed problem responses. The offline suite must cover base64url, JWK thumbprints,
JWS modes and vectors, nonce concurrency, directory validation, order transitions, DNS validation, HTTP-01 cleanup,
CSR SANs and signatures, persistence/restart, atomic replacement, renewal, error documents, and cancellation.

Let's Encrypt staging integration is opt-in and must never be required for the normal offline suite. It must use explicit
environment/SecretStore inputs, avoid production rate limits, and report whether public DNS and account permissions made
the test executable. An unrun live path is not evidence.

The following claims remain separate:

| Claim | Required evidence |
| --- | --- |
| ACME protocol model exists | named package revision, API documentation, focused unit tests |
| mock issuance works | deterministic mock-server terminal receipt and test output |
| Linux support exists | clean Swift 6 Ubuntu build/test and profile evidence |
| macOS support exists | clean Swift 6 macOS build/test and profile evidence |
| Let's Encrypt interoperability exists | opt-in staging result with account, DNS/challenge, and certificate evidence |
| a domain certificate was issued | named production/staging order and certificate receipt for that domain |
| a server is securely deployed | host admission, independent security review, TLS verification, rollback evidence |

No lower row may be inferred from a higher row. In particular, mock issuance is not CA interoperability, a staging
certificate is not production security, and a compiled package is not a deployed server.

## Release and open-source boundary

The public repository must be a reusable SwiftPM product with a strong README, DocC-compatible public comments,
platform matrix, architecture diagram, security assumptions, examples without credentials, test instructions, and a
security policy. The first release target is `0.1.0` unless an existing repository has a reviewed versioning policy.
The package follows SemVer; protocol/API compatibility is treated as infrastructure compatibility.

The source repository may be MIT-licensed or use another explicitly reviewed Fountain-Coach license. Third-party
dependencies retain their own licenses. ACME CA terms, account policies, and certificate issuance policies are not
relicensed by Fountain Coach. Public documentation must not publish private account data, certificates that are not
intentionally public, private keys, or production host details.

The repository must carry the reusable-kit instruction and evidence surface (`AGENTS.md`, `PLANS.md`, `SOURCE.md`,
`README.md`, license, security policy, audit/compliance documents, release manifest, and generated artifacts where
applicable). A release is an implementation candidate until its declared platform, security, mock, and integration
gates pass.

## Rules

1. The core API MUST be provider-neutral; Let's Encrypt URLs MUST remain directory configuration.
2. The package MUST be usable on the declared macOS and Linux profiles without Apple-only security frameworks or
   shell-based certificate tooling.
3. Transport, storage, challenge handling, cryptography, clock, and logging MUST be replaceable protocols or adapters.
4. Account keys and certificate keys MUST remain separate, protected, restart-safe, redacted, and atomically persisted.
5. HTTP-01 is the first supported solver; unsupported challenge types MUST remain visibly unsupported.
6. The host owns scheduling, route binding, TLS activation, deployment, and operational policy; the kit MUST NOT
   silently take those authorities.
7. Offline mock evidence, staging interoperability, production issuance, and secure deployment MUST be reported as
   separate claims.
8. A release MUST NOT claim a feature, platform, or provider beyond its named implementation and acceptance evidence.

## Definition of done

This governance chapter is complete when it is published as a reviewed chapter with a reading-index entry and local
generated-site evidence. The SwiftACMEKit implementation is a subsequent phase and is complete only when the package
structure, public API, RFC 8555 lifecycle, HTTP-01, persistence, renewal, mock server, offline tests, platform builds,
staging path, documentation, security boundary, and release manifest satisfy the evidence table above.

Until then, the honest public status is **governed proposal** — not “ACME support”, not “Let's Encrypt integration”,
and not “secure certificate deployment”.

## Governing sentence

**SwiftACMEKit is Fountain Coach's provider-neutral Swift boundary for explicit ACME certificate lifecycle work; it
keeps protocol, credentials, host operations, and evidence separate, and it claims only the platform, challenge,
provider, and deployment behavior its named release has actually established.**
