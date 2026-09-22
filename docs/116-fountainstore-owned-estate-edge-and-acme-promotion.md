# 116 — FountainStore Authority and MIDI2 Estate Edge Projection

> Chapter summary: One local FountainStore owns durable estate publication state. Governed publication freezes an immutable projection and sends it to an enrolled remote MIDI2 machine instrument; the edge admits that projection atomically and serves it without becoming a second Store. ACME, TLS, and external DNS remain explicit production operations with their own credentials, evidence, and rollback.

![Principal illustration: a local FountainStore authority promotes an immutable estate projection to an enrolled remote MIDI2 edge instrument](illustrations/116-fountainstore-estate-edge.svg)

*Principal illustration — a deterministic vector architecture projection. It is not a live deployment screenshot and does not claim that every estate domain, certificate, or route has already been promoted.*

The [Fountain Coach Publication Estate](92-fountain-coach-publication-estate.md) defines one identity expressed through specialized domains. This chapter defines the missing operational seam: how those domains become a browsable local, staging, or published projection without introducing a second web authority.

## The decision

FountainStore is the estate's **single durable publication-state authority**. The writer's Mac or the admitted local Ubuntu machine may host that authority; moving compute between those local machines does not create another publication authority. A remote public host is an enrolled MIDI2 instrument that receives, validates, activates, serves, and reports an immutable estate projection.

The remote edge does **not** need a second authoritative FountainStore. Its restart continuity is provided by a distinct subordinate **MIDI2 cache instrument** that durably retains only the last projection already admitted by the edge. That cache instrument may restore and report the admitted revision, but it cannot create, edit, promote, reinterpret, or independently authorize publication state.

```text
local FountainStore authority
        │ freeze typed revision + digest + predecessor
        ▼
local publication / projection instrument
        │ MIDI-CI identity + governed MIDI2 lifecycle
        │ immutable projection transfer + receipt
        ▼
remote edge machine = enrolled MIDI2 instrument
        │ validate → atomically admit → serve
        │
        ├── active in-memory projection
        │
        └── subordinate MIDI2 cache instrument
              │ persist last admitted revision only
              │ report revision / digest / predecessor
              └── restore exact cached projection after restart
        ▼
HTTPS projection
        ├── fountain.coach
        ├── book.fountain.coach
        ├── governance.fountain.coach
        ├── midi2.fountain.coach
        ├── instruments.fountain.coach
        └── status.fountain.coach
```

The machines share one publication graph and one typed contract. They do not share publication authority. MIDI-CI establishes who the participating instrument is and what projection capabilities it declares; the local Store establishes what revision exists.

## Store-owned publication manifest

Every admitted domain is represented by a typed manifest record. The record names the host, publication role, route root or Store projection, template revision, content digest, environment, and promotion state. A route is not admitted because a server happens to have a directory with that name.

The manifest MUST preserve:

1. the canonical domain and its declared role from Chapter 92;
2. the local, staging, or published environment;
3. the source projection and template identity;
4. the content and asset digests;
5. the Store receipt and source revision that established the projection;
6. the route and certificate identities where applicable; and
7. the rollback predecessor.

The route registry is a Store projection. A checked-in JSON file may bootstrap a development server, but it is not the durable authority and must not silently diverge from the Store.

## One estate, three environments

The same estate graph may be projected in three environments:

| Environment | Meaning | Authority |
| --- | --- | --- |
| `local` | editable candidate and writer-facing preview | local FountainStore |
| `staging` | reviewable immutable projection on an enrolled staging instrument | local FountainStore; staging edge is projection only |
| `published` | immutable projection serving the canonical host | local FountainStore; public edge is projection only |

Every environment MUST expose its state to the machine-readable surface and, where it is visible to a writer, to AX and the rendered page. A local page may retain the canonical public URL as provenance, but it must visibly identify itself as local and pre-published. A remote instrument may report which revision it has admitted, but that receipt is not a competing publication manifest.

## Promotion and synchronization

The promotion path is a typed, receipt-producing instrument operation:

```text
candidate in local FountainStore
  → validate estate manifest and shared template contract
  → freeze immutable projection revision + digest + predecessor
  → discover/verify target machine by MIDI-CI
  → transfer projection to the enrolled edge instrument
  → edge validates complete content before activation
  → atomically replace active edge projection
  → edge returns correlated admission receipt
  → verify HTTPS and semantic estate graph
```

The transfer is not Store replication and not a blind filesystem copy. It MUST be idempotent, revision-addressed, digest-checked, target-bound, and rollback-capable. The old projection remains active until the replacement has completely validated. If transfer or validation fails, the remote instrument continues to serve its previously admitted revision.

MIDI2 is the operation and lifecycle plane. Bulk projection bytes may use a negotiated content transport when that is more appropriate than UMP payloads, but the transfer still belongs to the same MIDI-CI-discovered instrument operation and correlation identity; an incidental HTTP upload, SSH session, or mounted filesystem MUST NOT become a parallel authority.

### Bounded route publication

A publication request that names one chapter, page, or route is a bounded route publication. The publisher MUST identify that unit by canonical host and normalized path prefix, freeze only the selected route files plus the metadata needed to verify their graph position, and send that route patch to the selected edge instrument. Whole-estate synchronization is a separate, explicit intent.

Before mutation, the publisher MUST establish that the route exists in the current local Store snapshot, that the remote MIDI2 instrument is the enrolled target, that its declared capabilities include the required projection operation, and that the destination can admit the candidate revision. Credentials remain in their owning SecretStore/host adapter; they are not MIDI2 payload fields.

The operation is complete only when one correlated local Store receipt establishes all of the following:

1. the intended remote instrument identity was discovered and verified;
2. the edge admitted the expected revision/predecessor and content digest;
3. typed edge read-back reports the selected host/path as active; and
4. the canonical public HTTPS route returns that same content digest.

A remote process exit code, transport success, or HTTP 200 without matching instrument/revision evidence cannot satisfy this proof. The operation enters Reframe through the governed MIDI2 plane described in [Chapter 81](81-universal-midi2-command-plane.md), uses the capability boundary in [Chapter 91](91-fcis-kit-instrument-store-is-the-capability-plane.md), and records lifecycle evidence under [Chapter 104](104-midi2-event-time-jitter-and-asynchronous-completion-governance.md).

## MIDI2 instrument edge projection

The HTTP/HTTPS process on a remote host is a projection surface of an enrolled machine instrument. At startup or explicit promotion it admits one complete immutable revision. Public GET/HEAD requests are then served from that admitted projection rather than performing authoritative Store reads.

A replacement projection becomes visible as one atomic change. Existing requests may complete against the previous revision while new requests see the replacement. Uploading candidate files alone MUST NOT evict or mutate the active projection.

If the local authority is temporarily unreachable, the edge MAY continue serving the last admitted revision and its existing certificate. It MUST refuse new promotion, route mutation, authority claims, or guessed recovery. This availability rule is precisely why the edge projection is distinct from the authority.

The machine identity is a MIDI2 instrument identity. MIDI-CI Discovery and Property Exchange expose the bounded capabilities and revision/protocol metadata needed to decide whether it may participate. HTTP health endpoints, SSH reachability, an IP address, or possession of cached files do not enroll the machine and do not establish publication authority.

## Durable subordinate cache instrument

Restart continuity is owned by a distinct MIDI2 instrument, not by an opaque filesystem cache and not by a second FountainStore.

The cache instrument:

- has its own stable instrument identity, MIDI-CI Discovery descriptor, Property Exchange state resource, enrollment binding, and revocation path;
- is subordinate to exactly one enrolled edge instrument;
- may persist only a projection that the parent edge has already admitted successfully;
- records the admitted revision, predecessor, source revision, content digest, file count, and immutable files needed to restore that exact projection;
- answers authenticated MIDI2 state queries about the cached revision;
- may restore the parent edge after process or machine restart only after validating its own cache identity and content digests; and
- MUST NOT author, merge, promote, reinterpret, or independently advance publication state.

Cache replacement MUST be atomic on the host filesystem. The canonical cache file remains either the previous complete revision or the new complete revision; a partial temporary file cannot become serving state.

Publication admission and cache persistence form one acceptance boundary. If persistence of a newly admitted revision fails, the edge MUST roll back its active in-memory projection to the previously admitted revision before returning failure. An acknowledged state of “active but not durable” is forbidden.

A restart therefore follows this bounded sequence:

```text
cache instrument starts / remains available
  → identifies itself by MIDI-CI
  → reports cached revision + digest + predecessor
edge instrument starts
  → loads and validates the cache instrument's last-admitted projection
  → restores exactly that projection into memory
  → emits restore evidence
  → becomes READY
```

The cache's durable bytes are availability state, not publication authority. The remote FountainStore publication snapshot MUST remain absent; possession of the cached projection does not grant mutation or promotion rights.

## ACME, TLS, and external DNS

ACME is a separate but connected production operation. [Chapter 96](96-swiftacmekit-is-a-provider-neutral-certificate-automation-boundary.md) owns the provider-neutral certificate lifecycle; [Chapter 94](94-credentialed-infrastructure-operations-and-provider-adapters.md) owns credential custody and provider-specific authorization.

The estate publisher MUST:

- request or renew certificates only for manifest-admitted domains;
- keep ACME account material and provider credentials in SecretStore-backed adapters;
- record challenge, certificate, route, and digest evidence without publishing secrets;
- activate TLS only after certificate identity matches the promoted host set;
- keep the previous certificate and route snapshot available for rollback; and
- distinguish certificate readiness from public DNS readiness.

External DNS is not silently changed by projection transfer. A DNS mutation is a separately authorized operation against the selected provider, with an exact target, receipt, and rollback or reversal evidence. Where DNS-01 is used, the challenge mutation remains within that explicit boundary. Where HTTP-01 or TLS-ALPN-01 is used, the enrolled edge instrument must own the required public edge ports for the challenge period. Removing Caddy does not remove these requirements; it transfers the edge responsibility to FountainStore.

## Local browsing and semantic equivalence

The local mirror is accepted as equivalent only when the Semantic Browser can traverse the same estate graph and observe the same page identities, headings, links, metadata, template semantics, and accessibility landmarks as the corresponding published projection. Its environment banner, Store receipt, and local source provenance are additional state—not a replacement semantic model.

The local browser may use a loopback origin when system DNS is intentionally untouched. In that case the DNS instrument records the intended estate host and environment, while the projection makes the difference explicit. A machine-wide resolver change is never a prerequisite for local editing and must not be used as an implicit mirror mechanism.

## Acceptance and release boundary

Acceptance requires, at minimum:

1. one named local FountainStore authority with a complete manifest, revision, and digest;
2. MIDI-CI discovery of the exact staging/public edge machine instrument and its projection capability;
3. a correlated projection transfer and admission receipt bound to that instrument identity;
4. an atomic edge projection that serves every admitted domain in the scenario without per-request Store authority reads;
5. continuity proof that the previous projection remains active until replacement validation succeeds, and that cache-persistence failure rolls the edge back before acknowledgement;
6. rejection of unknown hosts, conflicting revisions, wrong predecessors, and wrong instrument identities;
7. a separately enrolled subordinate MIDI2 cache instrument whose authenticated state query reports the admitted revision/digest/predecessor, plus a restart proof that restores that exact revision while the remote Store publication snapshot remains absent;
8. certificate identity and TLS evidence for the active host set;
9. external DNS evidence where a public route is claimed; and
10. Semantic Browser, AX, visual, edge, MIDI2, and FountainStore witnesses that agree about the same source revision.

The following claims remain separate:

```text
local manifest validates          publication authority
MIDI-CI peer verifies             machine/instrument identity
projection transfer completes     delivery witness
edge admits revision              serving-state witness
HTTP edge responds                HTTP witness
ACME certificate is valid         TLS witness
DNS points to the edge            public routing witness
semantic graph matches            browser/AX equivalence witness
```

No one row proves another.

## Rules

1. Exactly one declared local FountainStore MUST own the durable estate publication manifest for a publication lineage.
2. A remote staging or public machine MUST participate as an enrolled MIDI2 instrument and MUST NOT silently become a second Store authority.
3. Edge projection activation MUST be complete, digest-verified, predecessor-aware, atomic, rollback-capable, and coupled to durable cache persistence before acknowledgement.
4. Candidate transfer MUST leave the currently active edge projection untouched until replacement admission succeeds.
5. The last admitted projection MAY remain servable while the local authority is unreachable. Restart continuity MUST come from a separately enrolled subordinate MIDI2 cache instrument; mutation and promotion MUST fail closed.
6. Host-aware routing MUST select only an admitted manifest record and MUST reject unknown or conflicting hosts.
7. MIDI-CI identity/capability evidence and FountainStore publication evidence MUST remain distinct and correlated.
8. Credentials remain in SecretStore/host adapters; MIDI2 messages and projection receipts MUST be redacted capability/evidence objects, not secret containers.
9. ACME, TLS activation, and external DNS mutation MUST remain explicit operations with independent evidence.
10. A chapter, page, or route publication MUST remain host-and-path scoped unless whole-estate intent is explicit.
11. HTTP, SSH, filesystem presence, or process reachability MUST NOT establish enrollment or publication authority.
12. Local, staging, and published projections MUST report their environment and source revision without inventing a second semantic model.
13. A cache instrument MUST persist only already-admitted projection state, MUST replace its canonical cache atomically, and MUST never expose publication-authority operations.
14. If cache persistence fails after tentative in-memory admission, the edge MUST restore the prior projection before returning failure.

## Governing sentence

The Fountain Coach estate has one durable local FountainStore publication authority; every remote serving machine joins as a MIDI2 edge instrument and may own a separately enrolled subordinate MIDI2 cache instrument that durably restores only the last admitted projection, while neither edge nor cache becomes another Store authority and TLS, DNS, rollback, and public verification remain explicit evidenced operations.

