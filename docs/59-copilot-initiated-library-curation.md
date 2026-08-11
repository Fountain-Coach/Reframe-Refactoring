# Copilot-Initiated Library Curation

> Chapter summary: an explicit Copilot request may ask the hosted Fountain-Coach Book Library to acquire a GitHub
> repository as a reviewed source candidate and open its published release in Reframe. The repository is never
> silently moved, the GitHub secret never enters Reframe, and a candidate is never publication until a human-approved
> release has an auditable receipt.

## The decision

“Move this repo to the library and open it in Reframe” is a new, explicit capability: **curate a GitHub repository as a
Fountain-Coach Library project**. It is not a synonym for “open this URL”. The existing bare-URL behavior remains
display-only: Reframe may show the requested web page in its bounded WebKit source view, but it does not ingest it,
create a manuscript, or publish it.

The word *move* is writer language, not a destructive GitHub operation. The governed operation creates a provenance-
preserving Library candidate from a selected repository revision. The original GitHub repository remains where it is.
After candidate review and explicit promotion, Reframe may open the immutable Library release. A Library project is a
provider-side source work and release, not an empty Reframe manuscript and not a second local copy managed by the
writer.

This separation gives the Copilot a clear grammar:

```text
show this URL
→ render the page only

move this GitHub repository to the Library
→ mediate scope, rights, credentials, and destination
→ acquire a candidate
→ review and explicitly promote
→ optionally open the named release in Reframe
```

No phrase list is the authority for freeform meaning. The Open-Turn Mediation Protocol first determines whether the
writer has requested display, curation, or conversation. A structured GitHub repository URL, owner/name, commit, tag,
and path may be parsed deterministically after that meaning has been settled.

## What a GitHub source must provide

A repository is not automatically a publishable book. It may contain code, documentation, generated output, secrets,
dependencies, licenses, or unrelated private material. The first adapter therefore accepts a repository only as a
**candidate source**, with a declared scope and a source-owned publication manifest. The initial manifest should name:

- the Library work title, creator or owning organization, language, edition, and intended source type;
- the exact Git commit or tag, not only a mutable branch name;
- the admissible entry documents and chapter/section mapping;
- the license, attribution, jurisdiction, and rights contact;
- the transformation/importer version and any files deliberately excluded.

Without that declaration, the result is review-only and cannot be promoted. The importer must exclude `.git` internals,
credentials, private keys, deployment files, caches, generated artifacts, and binary or oversized content unless the
manifest and review policy explicitly admit them. It must defend against path traversal, archive bombs, unexpected
object counts, and embedded secrets before a candidate is exposed to the public Library.

GitHub access is an acquisition permission, not publication permission. GitHub's current guidance says GitHub Apps
should receive the minimum permissions required; for this feature the preferred installation grant is repository
metadata plus read-only contents, restricted to the selected repository. A fine-grained personal access token is a
fallback, scoped to the selected repository with read-only contents and metadata and an expiry. Neither mechanism
proves that the source may be republished in the writer's jurisdiction. The candidate still requires the Library's
rights and attribution review.

## The mediated operation

The writer may say:

> Move this repo to the Library and open it in Reframe.

The Copilot resolves the request on device and presents the consequential facts before any remote acquisition:

1. canonical GitHub repository and owner;
2. exact revision, or a request to resolve the default branch to a commit;
3. selected paths and the source manifest, if present;
4. proposed Library work identity and destination;
5. rights, license, attribution, and jurisdiction state;
6. whether a GitHub connection is needed and what read access it grants;
7. whether the writer wants the release opened after promotion.

“Yes” to opening is not “yes” to publication. The writer may authorize acquisition, review, promotion, and opening as
separate decisions. An unresolved repository, mutable revision, missing rights basis, private-repository connection,
or ambiguous scope produces a clarification or a typed block. The Copilot never proceeds by guessing.

The proposed capability identity is `book-library/curate.github-repository`. Its implementation must bind one meaning
to one declared operation, one responsible Library actor, one job identity, one FountainStore receipt, one AX-visible
state, and one terminal result. The hosted Library may expose its provider projection over HTTPS, but Reframe must keep
the MIDI backplane IDL as its native contract and must regenerate facts, reasoning orientation, and telemetry artifacts
if that contract changes. No hand-authored second operation definition is allowed.

## Lifecycle and ownership

The operation is asynchronous and auditable:

```text
requested → validated → acquiring → candidate → review-required
          → approved → promoted → verified → opened
```

Typed terminal failures include `not-found`, `unauthorized`, `rate-limited`, `rights-unknown`, `manifest-invalid`,
`scope-invalid`, `secret-detected`, `parse-invalid`, `hash-mismatch`, `promotion-failed`, and `open-failed`. A retry
keeps the same operation identity when the source revision, scope, importer version, and destination are unchanged.
It must not create a second release or double-count the same acquisition. A changed commit or transform is a new
candidate lineage.

The ownership split is deliberately narrow:

- **Reframe Copilot:** mediate meaning, show the proposed scope and consequences, request the Library job, show live
  progress through AX, ask for approval at the governed boundary, and open only the verified release.
- **Hosted Book Library/importer:** fetch GitHub content, validate the manifest and scope, scan and normalize the
  candidate, preserve provenance, hold the review state, promote atomically, retain rollback evidence, and publish
  the catalog/release.
- **FountainStore:** persist Reframe's operation reference, approval/instruction events, handoff, and terminal receipt;
  it is not a blob store for the repository and not a credential vault.
- **Maintainer/deployment operator:** configure the GitHub App, importer policy, server, DNS, TLS, quotas, and rollback.

The existing `book-library-upload` and `book-library-publish` skills already describe candidate staging, rights,
digests, approval, atomic promotion, HTTPS verification, and Reframe verification. `secure-publishing` governs the
host and its credentials. Those are maintainer/agent procedures, not writer-facing server controls. The missing work is
the Library-side GitHub adapter and the Copilot capability binding; this chapter does not pretend either exists yet.

## SecretStore: exact custody boundary

Public repositories need no GitHub secret. The importer may use an unauthenticated public fetch, subject to GitHub's
rate limits, and must record that the acquisition was public and unauthenticated.

Private repositories require a server-side GitHub connection. The preferred production shape is a GitHub App with a
read-only `contents` permission, read-only metadata, and repository selection restricted to the requested repository.
The importer mints a short-lived installation token for the job. If a personal token is temporarily required, it must
be fine-grained, repository-scoped, read-only, expiring, and treated as a migration exception—not pasted into
Copilot. The GitHub token is never sent to Reframe.

SecretStore holds only secret values, under the hosted Library service identity. The exact names are an implementation
contract to be finalized in the Library repository, but the custody classes are fixed:

- GitHub App private key and client secret, if the App is used;
- Library importer service credential used by Reframe's server adapter;
- deployment/SSH/DNS/TLS credentials used by the publishing operator;
- Reframe's separately governed model credentials, never reused as Library credentials.

Installation IDs, repository allow-lists, endpoint URLs, and account names are facts/configuration and may be exposed as
non-secret account state; private keys, tokens, and bearer values may not. FountainStore records a secret reference,
issuer, scope, key version, and fingerprint where needed for audit—not the value. Telemetry, chat, screenshots,
candidate manifests, public Book projections, and error messages must redact secret material. Presence of a secret is
not consent to use it. A private-repository acquisition requires an explicit writer or account-owner authorization
event, and the server must report `unauthorized` or `approval-required` rather than silently falling back.

## Preferences are the wrong interface

Nothing about GitHub access, server selection, auto-promotion, default branch, path inclusion, or cloud lane belongs in
Reframe Preferences. Those are decisions that depend on the current repository and publication risk. Chapter 22's
rule applies directly:

- **Facts** belong in Accounts & Storage or Integrations: Library endpoint identity and health, connected GitHub
  account, installation scope, credential state, and selected publishing tenant.
- **Instructions** belong in Copilot dialogue: “use this repository,” “include the docs folder,” “open the release
  when it is published.” If an instruction is remembered, it is stored with author, scope, provenance, and revision;
  it does not become a hidden routing toggle.
- **Maintainer policy** belongs on the Library service: allowed organizations, file classes, size/object limits, review
  requirements, queue limits, retention, and deployment environment. It is not a writer preference.

The only useful “setting” is a factual connection state and the account owner may revoke it. Every publication still
gets a visible, attributable operation and a release decision. The server may offer a maintainer policy such as
“promotion always requires approval”; Reframe must not expose an “auto-publish” switch to bypass it.

## Accounting and evidence

Every request receives an idempotency key and an operation ID. The receipt chain must distinguish four ledgers:

1. **Provenance:** canonical repository URL, owner, exact commit, GitHub provider, acquisition mode, source manifest,
   upstream hash, normalized hash, excluded paths, importer version, and Library service commit.
2. **Rights and approval:** license/attribution/jurisdiction evidence, reviewer, approval actor, timestamps, scope,
   private-source authorization, and any expiry or withdrawal.
3. **Operations and resources:** candidate ID, bytes/objects, scan results, retries, queue/compute/network usage,
   GitHub rate-limit observations, lane/provider if reasoning was used, and an estimate/actual cost record where a
   billable service was involved.
4. **Release and handoff:** release ID, manifest digest, previous release, atomic promotion time, HTTPS/catalog
   verification, Reframe operation reference, open result, and rollback target.

These are facts, not a claim assembled from chat prose. A public fetch may consume quota without incurring a monetary
charge; a paid model lane is chargeable only when the writer explicitly grants it and a provider receipt proves the
call. The system must never say “the writer paid” merely because a credential exists. A retry points to the existing
operation and release identity; it does not create a second charge or publication.

Reframe persists a sanitized handoff and terminal receipt in FountainStore immediately as state appears: requested,
candidate, approval-required, promoted, verified, opened, or typed failure. The hosted service remains authoritative
for source bytes and release state. AX must expose the same operation ID, current state, progress meaning, cancel/resume
actions, and terminal result that the receipt records. A screenshot alone is not proof.

## Acceptance gate before implementation is called complete

The capability is not live because the Copilot knows the sentence. It must pass:

- public-repository positive path from explicit Copilot request through candidate, human approval, atomic release,
  HTTPS/catalog verification, and opening the exact release in Reframe;
- private-repository path with the GitHub connection absent, refused, expired, and authorized, proving no token enters
  chat, FountainStore, telemetry, or public output;
- wrong repository, wrong revision, mutable-branch ambiguity, missing manifest, rights unknown, secret detected,
  parse failure, hash mismatch, rate limit, promotion failure, cancellation, resume, and rollback paths;
- duplicate request/idempotency proof and changed-commit/new-release proof;
- bare URL regression proof: it still opens the page only and never starts an importer job;
- AX and rendered acceptance of every state, with operation/release identity visible and no spinner standing in for
  unknown work;
- provider receipt, FountainStore handoff, and accounting reconciliation proving that every claim names its artifact.

## Governing sentence

Reframe may ask the hosted Fountain-Coach Library to curate a GitHub repository only through an explicit, mediated,
reviewable operation: GitHub grants the importer the narrowest read access, SecretStore keeps every credential outside
Reframe, the Library owns candidate and release truth, FountainStore records the handoff and receipt, and Reframe opens
only the verified release a human has authorized.

### External provider references

The implementation should re-check GitHub's current primary documentation when provisioning the adapter:

- [Choosing permissions for a GitHub App](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app)
- [Generating an installation access token](https://docs.github.com/en/enterprise-cloud@latest/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app)
- [Managing personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
- [REST API rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
