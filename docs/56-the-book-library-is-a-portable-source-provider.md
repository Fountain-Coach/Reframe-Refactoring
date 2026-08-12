# The Book Library Is a Portable Source Provider

> Chapter summary: Reframe may read a curated Book of Reframe library from a separately hosted service, just as it
> reads DraCor. The library owns its publication and delivery boundary; FountainStore owns persistence; Reframe owns
> the writer-facing choice and import. The service is a portable source authority, not an accidental server attached to
> one machine.

## The decision

The Book of Reframe may publish a selectable subset of eligible works through a separately versioned Swift service.
Reframe treats that service as one source provider alongside DraCor and local-file input.

The provider is a curated, provenance-preserving fork. It may select, normalize, structure, version, and withdraw a
work, but it may not erase the upstream source, edition, license, jurisdiction, or transformation record. “Our terms”
govern the service, API, availability, and derived presentation; they do not silently replace the legal terms attached
to an individual work.

The provider is outside Fountain-Store. Fountain-Store remains the native persistence authority for the imported source,
its versions, receipts, and downstream artifacts. Reframe remains the writer-facing application and does not become the
library's publisher or server administrator.

## Rules

1. **A hosted library is a source provider, not a hidden importer.** It has a declared identity, endpoint, version,
   lane, cost class, reachability, health, and terminal outcome. Reframe reports those facts where the writer works.

2. **The provider is a separate repository and package.** Its Swift server, source manifest, fixtures, OpenAPI
   projection, deployment scripts, and migration documentation live outside Fountain-Store. Fountain-Store must not
   fetch or curate books, and the provider must not implement FountainStore persistence semantics.

3. **The library has two records for every work.** The immutable upstream record contains the source URL or identifier,
   retrieval time, edition, checksum, copyright/jurisdiction review, license, attribution, and any required notices.
   The Reframe publication record contains the selected work ID, normalized representation, chapter/unit map, content
   hash, transformation version, publication state, and provider release. Neither record may substitute for the other.
   A published work also has a validated navigation manifest. Its nodes have stable IDs, human-readable labels, valid
   source ranges, and optional provider-defined `kind` and `parentID` fields. The vocabulary is open: a provider may
   publish episodes, books, myths, scenes, sections, movements, or another structure without Reframe learning a new
   literary taxonomy.

4. **Eligibility is item-specific and jurisdiction-aware.** “Available from Gutenberg” is not by itself a sufficient
   publication decision. A work may be published only after its upstream notice and the intended audience's relevant
   jurisdiction have been reviewed. Copyrighted or restricted works require an explicit permission or compatible
   license. The publication manifest records the decision and its reviewer or review artifact.

5. **A source switch is authoritative and reversible.** Each work has an explicit state such as `published`,
   `withdrawn`, `superseded`, `review-required`, or `unavailable`. A withdrawn work disappears from selection and fetch
   results at the provider; existing Reframe/FountainStore copies retain their provenance and are marked with the
   provider state on the next catalog refresh. No client infers availability from a cached file or a stale catalog.

6. **Publication is reproducible.** A release is identified by a provider revision and a manifest digest. The same
   manifest and source inputs produce the same normalized content hashes, unit boundaries, metadata, and API results.
   A correction creates a new release; it does not rewrite an earlier release without a recorded supersession.

7. **The content API is a projection, not a second definition.** The provider's operation meaning, request/response
   shape, errors, read/write status, budgets, and version are defined once in the governed contract and projected to
   OpenAPI. A hand-maintained OpenAPI document and server implementation are not independent authorities.

8. **The minimum read surface is small and addressable.** The provider exposes the equivalent of:

   ```text
   GET /v1/catalog
   GET /v1/works/{work}
   GET /v1/works/{work}/manifest
   GET /v1/works/{work}/chapters
   GET /v1/works/{work}/source
   GET /v1/health
   ```

   Source responses name the work, provider release, content hash, unit/range, and provenance. The navigation
   response is a publication acceptance artifact, not an optional hint: it must be non-empty, have unique IDs, valid
   ranges, resolvable parents, and no parent cycle. A whole-work response may not silently replace a requested unit
   or range, and a client must refuse or clarify when the published navigation manifest cannot be verified.

9. **Import follows one honest lifecycle.** Reframe selects a work, fetches a declared representation, validates its
   manifest and hash, normalizes only according to the declared transformation, persists the source through native
   FountainStore access, verifies the persisted artifact, and only then reports success. A network response or server
   log is not proof that the manuscript landed in FountainStore.

10. **Failures are typed and visible.** Unreachable, unauthorized, unavailable, withdrawn, invalid, hash-mismatch,
    incompatible, too-slow, and persistence-failed are distinct outcomes. Reframe names the provider, what happened,
    and the remedies that actually exist. It never reports a successful import when persistence was not verified.

11. **The provider is portable by construction.** Reframe refers to a DNS name or configured service identity, never
    a literal IP. The service has no machine-local assumptions in its content, manifest, or runtime contract. A
    migration package includes source data, publication manifests, checksums, configuration, deployment scripts,
    secrets-handling instructions, and restore verification.

12. **Migration does not change content silently.** Moving to another IP, host, or provider preserves the provider
    identity, release manifest, work IDs, content hashes, publication states, API compatibility, and provenance. A
    changed host is a deployment event; a changed content hash is a publication event and requires a new release.

13. **Cutover is staged and reversible.** A new host is built and verified behind a non-public or temporary endpoint,
    then DNS is switched only after health, catalog, manifest, content-hash, TLS, and representative Reframe import
    checks pass. The previous host remains available for rollback until the new host is accepted.

14. **The public Book publishes projections, not private infrastructure.** Public documentation may expose the
    provider contract, work manifests, sanitized provenance, release IDs, and evidence. It must not expose private
    source repositories, credentials, deployment access, private store records, or unpublished manuscript material.

15. **The provider is independently testable.** Its fixture suite must prove catalog consistency, manifest integrity,
    normalized-content determinism, withdrawal, hash mismatch, migration restore, API compatibility, and failure
    reporting without requiring Reframe or a live FountainStore.

16. **Acquisition and publication are separate operations.** A remote importer may retrieve an explicitly selected
    upstream edition and create a candidate release, but it may not make that candidate visible in the published
    catalog. Publication requires a local, governed release action, human approval, a manifest digest, and a recorded
    rollback target. Reframe is never an acquisition or deployment client.

17. **The local publisher is the deployment authority.** The repository-local `book-library-publish` skill validates
    the exact provider commit, importer output, provenance, hashes, tests, and host identity before it asks the remote
    service to promote a candidate. Credentials remain in the approved local/host secret mechanism; no credential or
    arbitrary upstream URL enters Reframe or a public manifest.

18. **The remote importer is a controlled staging service.** It accepts only an explicit upstream identifier and
    declared edition metadata, writes into an isolated candidate area, is idempotent for the same upstream and source
    hash, and emits a candidate receipt. It must not fetch arbitrary URLs supplied by a writer, overwrite `current`,
    mutate an existing release, or publish content without the promotion protocol.

19. **Promotion is atomic and reversible.** A promoted release is immutable and addressed by its release ID and
    manifest digest. The service switches `current` only after validation, restarts or reloads the reader safely, and
    retains the previous release as the rollback target until HTTPS health, catalog, manifest, source, hash, and
    representative Reframe import checks pass. A rollback is itself recorded as a deployment event.

20. **Upstream adapters are explicit and bounded.** A Gutenberg adapter may use the official mirror/metadata routes
    and a selected eBook identifier, preserving the Gutenberg license and attribution requirements. It must record
    the item-level rights and jurisdiction review; availability from Gutenberg alone is not an eligibility decision.
    Private Ulysses material remains private or authenticated, and a translation/edition of Ovid is a distinct source
    item—not an implicit canonical work.

21. **Automatic refresh may prepare, never publish.** Scheduled acquisition may produce a candidate and notify the
    release owner, but only the governed promotion action can widen the public catalog. Content changes, withdrawals,
    and rights decisions therefore have a visible release boundary and can be reproduced or reversed.

## Ownership boundary

```text
upstream source / edition
          ↓ provenance-preserving curation
Book Library service — catalog, manifests, normalized projection, switch, API, deployment
          ↓ declared source provider contract
Reframe — selection, progress, validation, import, writer-facing explanation
          ↓ native persistence
FountainStore — source document, versions, receipts, downstream artifacts
```

The hosted service does not become a second FountainStore. Reframe does not become a second publisher. The Book site
does not become an operational dashboard. Each layer reports only the truth it owns.

## Publication control plane

```text
local repository + book-library-publish skill
       │ validate exact commit, candidate, approval, rollback
       ▼
remote book-library importer
       │ acquire explicit upstream edition → isolated candidate receipt
       ▼
remote promotion endpoint/script
       │ atomic immutable release → current
       ▼
library.fountain.coach
       │ read-only published catalog and source API
       ▼
Reframe → FountainStore
```

The importer and publisher may run on the same host, but they remain separate authorities and directories. The
publisher is not a blind deployment wrapper: it verifies the candidate that the importer produced. The minimum
receipts are the upstream identifier and edition, source and normalized hashes, candidate/release IDs, provider
commit, approver, promotion time, previous release, and post-promotion probes.

## Migration package

Every production release must be exportable into a machine-readable migration package containing:

- provider identity and release manifest;
- catalog and per-work publication manifests;
- source and normalized content hashes;
- unit/chapter metadata;
- deployment configuration with endpoint indirection;
- TLS and secret-rotation procedure, without secrets themselves;
- backup, restore, and verification commands;
- compatibility and rollback notes.

The migration package is sufficient to rebuild the service on a clean host and verify that the new host answers the
same catalog and content requests. A migration is not complete because the process starts; it is complete when the
content, manifest, API, and Reframe import evidence agree.

## Acceptance

The chapter is implemented only when all of the following are observed:

1. Reframe lists the Book Library as a source beside DraCor and local file, with no hidden flagship corpus.
2. A published work imports through the provider, persists in FountainStore, and is reopened after relaunch with the
   same source identity and content hash.
3. A published work exposes its provider-defined navigation manifest; Reframe can resolve a named unit without
   assuming that the unit is a chapter, book, or myth.
4. A withdrawn work is absent from fresh selection and produces a typed, writer-visible terminal outcome.
5. A deliberate navigation, manifest, or content-hash mismatch prevents import and leaves no false success artifact.
6. The provider's OpenAPI projection and Swift implementation pass contract parity checks from one definition.
7. A fresh-host restore reproduces catalog, manifests, hashes, publication switches, and representative API responses.
8. DNS cutover to the fresh host requires no Reframe code change and preserves the provider's identity and release
   evidence.
9. The old host remains a tested rollback target until the new host passes health, TLS, catalog, content, and Reframe
   live-drive checks.
10. The Book publication exposes only the sanitized contract and evidence permitted by Chapter 44.

## Relationship to other chapters

Chapter 44 governs what may be published. Chapter 48 governs service identity, failure, and persisted outcomes. Chapter
49 governs the one definition and generated OpenAPI projection. Chapter 55 governs FountainStore selection and native
persistence. Chapter 50 governs addressable source units. This chapter adds the public source-provider and migration
boundary; it does not replace those authorities.

## Governing sentence

**The Book Library is a portable, provenance-preserving source provider: it may curate and publish a work under a
legible service contract, but Reframe reports only what the provider declares and FountainStore proves, and a host may
change without the source, identity, or evidence changing silently.**
