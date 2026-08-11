# The Fountain-Coach Git Library and Reframe Project Flow

> Chapter summary: Reframe does not depend on GitHub to show, curate, or exchange projects. A Fountain-Coach-owned
> Git service is the repository authority; an owned Swift library makes Git a bounded capability; Reframe mediates the
> writer's intention; the Book Library publishes selected revisions; and FountainStore records the handoff.

This chapter replaces the former GitHub-specific repository curation design. There is no GitHub App, GitHub
installation token, GitHub rate limit, or GitHub-specific source class in the production path.

This chapter does not turn Reframe into a Git server. The managed Fountain-Coach service owns repositories and serves
their declared projections. Reframe is the writer-facing client and mediator. The hosted Book Library remains the
publication provider defined by [chapter 56](56-the-book-library-is-a-portable-source-provider.md).

## The decision

Fountain-Coach owns a managed Git project service whose repositories, refs, revisions, trees, blobs, ACLs, and
operation receipts are authoritative for Fountain-Coach projects. Reframe may inspect a project, request a selected
revision for publication, open a verified Library release, and explicitly export an authored result as a new commit.
No operation mutates a repository merely because a URL was pasted or a page was opened.

The initial product is a meaningful project surface, not a clone of every Git frontend feature. It must make these
writer actions possible through Copilot:

- “Show my projects” — list projects the current account may see, with health and last verified revision.
- “Open the project” — show its summary, branches, recent commits, tree, and bounded file content in Reframe.
- “Use this revision for the Library” — create a review-required candidate from an exact immutable revision and
  declared path scope.
- “Open the published release” — fetch the verified Library release into Reframe's normal source boundary.
- “Export this result to the project” — create an explicit, attributable commit job; never silently push.

Branches, commits, trees, and files are views of a project. They are not new manuscripts and do not pollute the
writer's manuscript history until a Library release is deliberately opened. A project can contain prose, governance,
code, or mixed material; the selected path scope and source manifest determine what is eligible for publication.

## The two directions

The source direction is:

```text
Copilot intention
  → Fountain-Coach Git service
  → exact project revision and path scope
  → review-required Library candidate
  → approved immutable Library release
  → Reframe source / FountainStore handoff
```

The authored direction is separate:

```text
Reframe authored result
  → explicit export preview and consent
  → Fountain-Coach Git commit job
  → new revision on a declared branch
  → receipt shown in Copilot and persisted in FountainStore
```

“Open” is read-only. “Publish” creates a candidate and requires the Library's review boundary. “Export” creates a
repository change and requires an explicit writer/account-owner decision. There is no automatic pull, push, merge,
promotion, or branch selection hidden behind a preference.

## The owned Swift library

The service and any local tooling use a Fountain-Coach-owned Swift package, provisionally named `FountainGitKit`.
It is the only boundary allowed to touch Git repository objects. A pinned, portable Git implementation such as
libgit2 behind a Swift package adapter may provide the mechanics, but libgit2 types and C calls do not cross the kit's
public API. The dependency is pinned by the committed manifest and revision, built and tested on every supported
server/client platform, and checked for dependency coherence before a live drive.

The kit exposes semantic operations rather than shell commands:

```text
Repository.open / Repository.createBare
Repository.refs
Repository.revision(id)
Revision.tree / Tree.entries / Blob.read(range)
Repository.diff(base, revision)
Repository.fetch(pack/source)      // managed service boundary only
Repository.commit(tree, parents, message, author)
Repository.updateRef(expected, next)
```

The kit enforces repository-root confinement, object and pack limits, immutable object IDs, expected-ref checks,
path-safe tree traversal, cancellation, and typed errors. It never receives a credential from chat, and it never
decides publication eligibility. A server adapter owns ACLs, jobs, receipts, and policy; the Library adapter owns
candidate and release semantics.

## Managed service surface

The managed service owns a registry of Fountain-Coach projects and exposes a read projection for the initial slice:

```text
git-projects/catalog.get
git-projects/project.get
git-projects/refs.get
git-projects/commits.get
git-projects/tree.get
git-projects/blob.get
git-projects/candidate.create
git-projects/export.commit
git-projects/job.get
```

These operation identities are defined once in the repository's reasoning/contract composition and projected to the
service transport. A hand-authored HTTP schema is not a second authority. The service may use an HTTP projection for
the remote managed host, while Reframe's native application operations remain governed by the MIDI backplane contract.
Read operations are bounded and deterministic. Candidate and commit operations are asynchronous, idempotent, and
return a job identity that remains inspectable until a typed terminal result exists.

The service stores bare repositories outside FountainStore. FountainStore stores sanitized operation events,
provenance, candidate/release handoff, and authored-export receipts; it does not store Git packs as a shadow database.

## Identity, custody, and policy

The service has a Fountain-Coach account and project identity, not a GitHub identity. Access is granted by the managed
service's own ACL and account/session protocol. Long-lived service credentials and signing keys stay in the server's
SecretStore. A client session credential stays in the platform Keychain/SecretStore. Neither credential enters Copilot
transcript, FountainStore content, telemetry, source manifests, or screenshots.

Accounts & Storage may show the factual connection state and endpoint health. It may not become a panel for default
branch, automatic export, publication, project routing, or merge policy. Those are reasoned per operation or stated by
the writer in Copilot; maintainer policy stays on the service.

The service must support migration by DNS and declared endpoint identity. Repository paths, IP addresses, machine names,
and deployment directories never become project identity. A host migration preserves project IDs, object IDs, release
manifests, and receipt references or records an explicit migration event.

## Provenance and accounting

Every operation carries an idempotency key, operation ID, account, project ID, exact revision, path scope, and current
state. The receipt chain records four ledgers:

1. **Repository provenance:** project, revision, refs before/after, tree/path scope, object and content digests, kit
   version, service revision, and source manifest.
2. **Rights and release:** license, attribution, jurisdiction, reviewer, approval actor, candidate ID, release ID,
   withdrawal or supersession state, and publication decision.
3. **Operations and resources:** bytes/objects, scan results, retries, queue time, duration, cancellation, and typed
   failure. A model lane is recorded only when one was actually used.
4. **Reframe handoff:** Library release, manifest digest, source units, FountainStore corpus/document identity, open
   result, export commit, and rollback target.

The writer sees a plain-language state and the operation identity through AX. The store and service receipt are the
behavioural proof. A screenshot, a branch name in chat, or a successful HTTP response alone is not proof.

## Acceptance boundary

The first implementation is complete only when a fixture-backed project can pass all of the following through the
current executable:

- list projects, open one, inspect refs/commits/tree, and read a bounded file through Copilot and AX;
- create an exact-revision, path-scoped review candidate without modifying the repository or Reframe manuscript list;
- approve/promote through the existing Library boundary and open the resulting release into Reframe;
- export a selected authored result through an explicit preview/consent and verify the new commit and receipt;
- prove wrong project, unknown revision, changed expected ref, path escape, missing manifest, rights unknown,
  secret detection, size limit, cancellation, retry, duplicate idempotency, and host-unavailable failures;
- expose current state, progress, cancel/resume, and terminal identity in AX without a spinner standing in for truth;
- reconcile service receipts, Library provenance, and FountainStore handoff with no credential or private source leak.

The fixture is not a substitute for the managed service: it proves the same kit and contract against a deterministic
repository. Production acceptance additionally requires HTTPS, DNS migration evidence, deployment provenance, and a
remote managed-server verification.

## Governing sentence

**Fountain-Coach owns the Git project authority and its Swift boundary; Reframe mediates what the writer means and
shows the bounded project flow; the Book Library decides publication; FountainStore proves the handoff; and every
repository mutation is explicit, attributable, idempotent, and reversible.**
