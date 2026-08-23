# FountainStore Is the Headless Linux Persistence Authority

> Governance chapter: 95. This chapter governs the promotion of the existing FountainStore HTTP server to a
> supported headless Linux deployment profile. It does not create a second database product and it does not make
> the server public-facing by default.

## The decision

FountainStore remains Fountain Coach's persistence authority: a pure-Swift engine with WAL, transactional replay,
MVCC, SSTables, indexes, FTS, vector support, backups, restores, and session/lease APIs. The private
`Fountain-Coach/Fountain-Store` repository may additionally ship that authority as a supported headless Ubuntu/Linux
service through its existing `FountainStoreHTTPServer`.

The server is an access and lifecycle boundary around FountainStore. It is not a replacement engine, a new storage
model, or a public internet database.

```text
Internet
  │
 Caddy / Fountain Coach application service
  │  localhost or private network
 FountainStoreHTTPServer
  │
 FountainStore
  │
 /var/lib/fountain-store
```

The governing sentence is:

> **FountainStore may serve as a headless Linux persistence authority only when its configured Store has opened,
> recovered, obtained its owner-safe lease, and is reported ready through a typed, authenticated server surface.**

## What this chapter governs

This chapter applies to the FountainStore 0.4 workstream in the private FountainStore repository. It governs:

- release-mode Linux build and installation;
- typed server configuration and deterministic precedence;
- filesystem and Store identity handling;
- startup, recovery, readiness, liveness, and shutdown;
- authentication and SecretStore-backed credentials;
- diagnostics, metrics, backups, restore transitions, and disk pressure;
- systemd operation and service hardening;
- OpenAPI, documentation, CI, versioning, and release evidence.

The chapter does not authorize a new persistence engine, a mandatory container runtime, a Caddy dependency, public
unauthenticated binding, automatic data deletion, or silent creation of a replacement Store.

## Authority boundaries

| Boundary | Authority |
| --- | --- |
| Persistence semantics | FountainStore engine |
| Session, identity, lease, and durable Store selection | FountainStoreSessionKit and Store APIs |
| HTTP access and authentication | FountainStoreHTTP / FountainStoreHTTPServer |
| HTTP contract | `docs/openapi-fountainstore.yaml` |
| Process lifecycle and readiness | Headless server runtime |
| Credential custody | SecretStore / FileKeystore / supported Linux secret provider |
| Reverse proxy and public TLS | Caddy or another Fountain Coach application service |
| Deployment supervision | systemd or an equivalent supervisor |

No HTTP handler may duplicate storage logic or infer authority from process reachability alone. A successful HTTP
response is not, by itself, proof that the requested Store is the authoritative Store.

## Configuration is typed and deterministic

The server exposes a small typed configuration model. It must support, at minimum:

```text
--bind
--port
--store-path
--cache-bytes
--wal-segment-bytes
--default-scan-limit
--log-level
--config
--version
--help
```

Configuration precedence is fixed and documented:

```text
CLI → environment → config file → defaults
```

Existing environment variables remain supported where practical, including `FS_PATH`, `FS_API_KEY`,
`FS_SECRETSTORE_PATH`, and `FS_SECRETSTORE_PASSWORD`.

The safe defaults are:

- bind address `127.0.0.1`;
- authenticated access;
- no silent path substitution;
- no secret values in logs, errors, metrics, status, or readiness responses.

Binding to a non-loopback address without authentication must produce a clear warning and, by default, fail closed.
Any development override must be unmistakable, such as `--allow-unauthenticated-remote`; it must never be inferred
from a missing key.

## Filesystem and Store identity

The supported Linux layout is:

```text
/usr/local/bin/fountain-store-server
/etc/fountain-store/fountain-store.env
/etc/fountain-store/fountain-store.conf
/var/lib/fountain-store/store/
/var/lib/fountain-store/backups/
/var/log/fountain-store/        # only when journald is not used
```

The service must resolve and report the canonical Store path and Store identity explicitly. It may create permitted
child directories, but it must fail clearly when the configured path is inaccessible, incompatible, or not writable.
Opening failure must never fall back to a fresh unrelated Store.

## Startup, readiness, and failure

The process lifecycle has distinct states:

```text
starting → opening → recovering → ready → stopping → stopped
                         └──────→ fatal
```

`GET /health/live` answers only whether the process can answer HTTP requests. It must not perform expensive storage
work.

`GET /health/ready` answers whether this instance is safe to use as the persistence authority. It returns success only
after configuration validation, Store path and identity resolution, manifest/open validation, WAL recovery, required
reconstruction, writability checks, owner-safe lease acquisition, and routing initialization. It returns `503` while
starting or when authority is unavailable, with machine-readable safe reasons.

`GET /health` remains for backward compatibility and must have documented semantics distinct from the new probes.

Fatal startup conditions include inaccessible paths, invalid manifests, unrecoverable WAL corruption, unsupported
formats, failed leases, unusable authentication/SecretStore configuration, and an unbindable port. Fatal conditions
exit non-zero and are not represented as healthy-but-not-ready operation.

On `SIGTERM` or `SIGINT`, the service stops accepting new work, gives in-flight operations a bounded opportunity to
finish, flushes the Store as required, closes the Store, shuts down NIO event loops, and exits with a meaningful
status. Abrupt process destruction is a recovery test, not the normal shutdown path.

## Authentication and SecretStore

The server retains its existing authentication forms:

- `FS_API_KEY`;
- `x-api-key`;
- `Authorization: Bearer …`;
- SecretStore-backed credentials, including the documented FileKeystore path on headless Linux.

Secret values remain outside the HTTP contract. Constant-time comparison is required for API-key validation. The
server may expose authentication state and safe configuration diagnostics, never the key, keystore password, or
secret-bearing path contents.

## Operational diagnostics and observability

The server retains `/status`, `/metrics`, and Prometheus output. Safe metadata should allow an operator to determine
server version, Store readiness and identity, sequence, uptime, collection count, compaction state, and backup state
where inexpensive. It must not disclose unnecessary filesystem details or credentials.

The headless distribution includes a non-destructive diagnostic command:

```text
fountain-store-server doctor
fountain-store-server doctor --json
```

Doctor checks configuration, path permissions, Store opening, manifest compatibility, WAL/recovery state, disk space,
backup accessibility, authentication/keystore accessibility, bind safety, and persisted-format compatibility. It
returns zero only when the installation is healthy. Doctor diagnoses; it does not repair or mutate persistence.

Structured lifecycle logs should cover startup, configuration, Store opening, WAL recovery, readiness changes, HTTP
listening, backup/restore transitions, shutdown, Store closure, and fatal startup. Per-record logging is not the
default.

## Backups, restore, and disk pressure

Backups remain an explicit Store operation and must work while the service is running. Backup metadata must survive a
restart and enumeration must remain deterministic.

Restore is a lifecycle transition, not an ordinary write. Readiness becomes false during an unsafe restore transition;
restore cannot race normal writes; failure remains diagnosable; and successful restore reopens and verifies a valid
Store authority. A simple external systemd-timer-compatible invocation is sufficient; a mandatory scheduler is not.

Obvious disk exhaustion must be detected before large operations where feasible. `ENOSPC` and related write failures
must be surfaced clearly and must affect readiness when durable writes can no longer be trusted. The service must not
delete user data speculatively.

## systemd and release installation

The supported native deployment includes a small, audited systemd unit with the actual runtime requirements tested.
The unit should use a dedicated `fountain-store` user/group, an explicit `EnvironmentFile`, a working directory,
`Restart=on-failure`, `KillSignal=SIGTERM`, `TimeoutStopSec`, and compatible hardening such as
`NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectSystem=strict`, `ProtectHome=true`, and a narrowly declared
`ReadWritePaths`.

The primary build is:

```text
swift build -c release
```

The resulting executable must run without a Swift toolchain installed. A documented, idempotent installation path
places it at `/usr/local/bin/fountain-store-server`. Docker is optional and never the primary support claim.

## OpenAPI and compatibility

`docs/openapi-fountainstore.yaml` remains the authoritative HTTP contract. Every public HTTP change must update it,
including `/health/live`, `/health/ready`, legacy `/health`, readiness schemas, authentication behavior, version
metadata, and RFC7807 error responses.

The 0.4 release is additive. Existing routes should remain available. If API and product versioning differ, the policy
must be explicit; stale current metadata must not remain unexplained. Historical release references remain historical
and are not rewritten as part of the version bump.

## Evidence and acceptance

Headless Linux support is not established by a macOS test suite or by a successful compilation alone. The release
evidence must include:

1. Linux debug and release build evidence;
2. configuration defaults, precedence, invalid-value, and loopback tests;
3. liveness/readiness tests during startup, ready operation, and persistence failure;
4. authentication tests for API key, bearer, missing, invalid, and remote-bind cases;
5. clean termination, restart persistence, and intentionally unclean WAL recovery;
6. backup/list/restart/restore verification;
7. doctor success and meaningful failure statuses;
8. systemd installation and restart evidence;
9. OpenAPI/implementation parity;
10. no-secret inspection of logs, responses, fixtures, and release artifacts.

The claim “headless Linux persistence authority” is permitted only after these authorities agree: the running Linux
process, the reopened Store, the health probes, the authenticated HTTP contract, and the persisted records. A passing
unit test alone cannot establish the claim.

## Definition of done

FountainStore 0.4 is ready for release when the private repository has the implementation, tests, Linux CI, release
build, systemd unit, doctor, documentation, OpenAPI parity, coherent current-version metadata, and release notes,
and the acceptance evidence above passes. The expected release is `v0.4.0`.

Until then, the correct status is an implementation candidate, not a production-ready authority. A tag may be created
only after all required evidence passes and the repository workflow permits release publication.

## Governing sentence

> **FountainStore is embedded first and headless second: the Linux server is trusted only when it exposes the existing
> Store authority through explicit configuration, authenticated access, truthful readiness, durable recovery, and
> independently tested lifecycle evidence.**
