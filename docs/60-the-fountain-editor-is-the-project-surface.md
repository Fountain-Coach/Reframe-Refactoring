# The Fountain Editor Is the Project Surface

> Chapter summary: Reframe is a Fountain editor with Copilot as its conversational project steward. Git is the
> managed versioning and transport layer behind the editor; the Book Library is the publication authority. A
> repository may be imported or cloned into Fountain-Coach infrastructure, but a writer works with Fountain text,
> metadata, revisions, and publication choices—not with Git internals as the primary interface.

Chapter 59 establishes the Fountain-Coach Git project authority and its two directions: source material may become a
review-required Library candidate, and an authored result may become an explicit repository commit. This chapter
defines the writer-facing object at that boundary: the Fountain project.

## The decision

Reframe's project surface is a Fountain document and its governed project context. The document is editable in
Reframe, addressable by path and revision, and accompanied by publication metadata. Copilot mediates the writer's
intentions—open, inspect, edit, import, commit, candidate, publish, or return to the work—without requiring the
writer to know repository IDs, object storage, service paths, or transport details.

The managed Git service owns repository objects, refs, revisions, access, import jobs, commit jobs, and operation
receipts. The Book Library owns candidate review, publication, release identity, withdrawal, and promotion. FountainStore
owns the Reframe working document, source identity, versions, and handoff evidence. These authorities remain distinct.

The intended flow is:

```text
writer / Copilot
       ↓
Fountain editor + publication front matter
       ↓ explicit import or commit operation
managed Fountain-Coach Git project
       ↓ exact revision and path scope
review-required Book Library candidate
       ↓ human approval and atomic promotion
published Book Library work
       ↓ declared source provider import
Reframe / FountainStore
```

## Rules

1. **Fountain is the writer's primary object.** Reframe presents editable Fountain text, structure, metadata, source
   identity, and current revision. Git branches, object IDs, pack files, and server paths are implementation details
   unless the writer asks for project information.

2. **Copilot is the project mediator.** A writer may say “open this project,” “show the README,” “make this a Library
   candidate,” “save this revision,” or “publish this.” Copilot resolves the intention against live project and
   Library state, explains the next governed step, and never invents a project, revision, path, or publication result.

3. **Repository provisioning is a separate operation.** “Move this repository to Fountain-Coach” means an explicit
   managed-project import or clone operation. It is not implied by opening a URL, pasting a repository path, or
   creating a Library candidate. The operation must identify the source, account, destination project ID, expected
   revision/ref, and custody policy before it runs.

4. **Only approved source forms may provision a project.** A server may accept a verified Git bundle, a permitted
   HTTPS Git source, or an operator-approved migration package. A writer-provided URL is not automatically cloned.
   Remote acquisition is allowlisted, authenticated by the server's SecretStore, bounded, auditable, and isolated.

5. **A managed project is a repository authority, not a manuscript.** Import creates or registers a bare repository
   under the server's declared Git root and assigns a stable project ID. It does not create a Reframe manuscript,
   publish a work, or alter the writer's FountainStore.

6. **The editor works from an explicit revision.** Every opened or imported Fountain document records the project ID,
   immutable revision, path, content digest, and source state. A moving branch is a discovery reference; it is not the
   source identity for a reading or candidate.

7. **Front matter is a declaration, not the whole publication contract.** A Fountain document may begin with a
   governed metadata block:

   ```fountain
   ---
   work_id: reframe-git-demo
   title: Fountain Coach Git Library
   author: Fountain Coach
   language: en
   publication: review-required
   ---
   ```

   The editor and Copilot may generate, repair, and validate this block. The server independently validates its
   schema, path scope, source revision, content digest, attribution, rights, jurisdiction, and publication state.
   Front matter may express author intent; it cannot grant rights, prove provenance, or promote a release.

8. **Templates are governed and versioned.** A project template declares the required metadata fields, permitted
   values, default publication state, and validation version. Templates are not arbitrary model output. A changed
   template creates a recorded format revision and does not silently rewrite an existing published work.

9. **Fountain parsing is bounded and loss-aware.** The editor preserves source text, front matter, line identity,
   chapter/unit boundaries, and unrecognized metadata according to the Fountain contract. Invalid or ambiguous front
   matter is shown as a repairable state; the editor does not silently reinterpret prose as metadata.

10. **Editing is local to the selected project context.** A writer edits a working document associated with one
    project, revision, and path. A commit requires an explicit target branch or new branch, expected base revision,
    commit message, author identity, and confirmation. A stale expected revision fails safely; it never overwrites a
    newer server revision.

11. **Commit and publication are different verbs.** Commit records authored text in Git. Candidate creates a
    review-required Library artifact. Publish promotes an approved immutable Library release. Opening a document,
    saving an edit, committing, creating a candidate, and publishing must remain visibly distinct operations.

12. **A candidate is built from exact content.** Candidate creation names project, revision, path scope, Fountain
    metadata, upstream provenance, normalized digest, and idempotency key. It copies or derives the selected content
    into an isolated review-required candidate area; it never changes the source repository or published `current`.

13. **The Library validates independently.** A candidate is rejected when the revision is missing, the path escapes
    the repository, the content is oversized or truncated, front matter is invalid, the digest does not match, rights
    are unknown where review is required, or required attribution is absent. A successful HTTP response is not a
    publication result.

14. **Git custody is explicit.** Repository acquisition, server-side cloning, bundle import, commit, and export have
    separate receipts. Credentials stay in the server or platform SecretStore. Copilot never receives credentials,
    and FountainStore never stores secrets, Git packs, or private repository content outside the writer's selected
    working document.

15. **The project surface is portable.** Project IDs, revision IDs, Fountain work IDs, content hashes, and release
    IDs do not contain hostnames, IP addresses, or deployment paths. A server migration moves repository bundles,
    refs, receipts, templates, and configuration through a verified migration package; DNS/HTTPS is the endpoint
    indirection.

16. **No hidden synchronization.** Reframe does not silently pull, clone, fetch, commit, push, merge, or promote.
    Automatic refresh may inspect availability or prepare a candidate only when separately governed. Any repository
    mutation is explicit, attributable, idempotent, cancellable where possible, and recoverable.

17. **The user sees the state they can act on.** AX exposes project identity, document path, revision, dirty state,
    front-matter validation, operation phase, confirmation, progress, cancellation/resume, and terminal receipt.
    Visual state and FountainStore events must agree. A spinner cannot stand in for an unknown repository or
    publication state.

## Ownership boundary

```text
Fountain editor / Copilot
  meaning, text editing, metadata templates, confirmations, AX

FountainGitKit + managed Git service
  repository provisioning, refs, revisions, trees, blobs, commits, ACLs, operation receipts

Book Library
  provenance review, candidate isolation, rights, publication, release, withdrawal, promotion

FountainStore
  Reframe working document, source identity, versions, handoff, and behavioural proof
```

The Git service may clone or import arbitrary permitted repositories into its own custody, but it does not decide
which files are publishable. The Fountain editor may author and validate metadata, but it does not decide legal
eligibility. The Book Library may publish a reviewed candidate, but it does not become Reframe's working store.

## Required operations

The capability contract must distinguish at least:

```text
git.library.project.catalog
git.library.project.import
git.library.project.open
git.library.project.revision.open
git.library.project.commit
git.library.candidate.create
library.release.open
```

Each operation declares its origin, account, project, revision or expected base, path scope, idempotency key,
confirmation policy, provider endpoint, and terminal receipt. The generated capability registry remains the current
inventory; this list defines the semantic membership required of the project surface.

## Acceptance boundary

This chapter is implemented only when the following are proven:

1. A permitted Git source can be imported into a managed server repository with a stable project ID and verified
   refs, without creating a Reframe manuscript or publishing content.
2. Reframe can open a project revision and edit a Fountain document with AX-visible path, revision, dirty state, and
   front-matter validation.
3. Copilot can generate and repair the governed front matter without inventing provenance or rights claims.
4. An explicit commit creates a new revision only when the expected base is current; stale-base writes fail safely.
5. A selected exact revision/path creates an isolated review-required Library candidate and leaves the repository and
   published release unchanged.
6. Candidate validation rejects malformed front matter, path escapes, digest mismatch, missing rights/attribution,
   truncation, and duplicate or conflicting idempotency keys.
7. Approval and promotion remain Library operations, and the promoted release opens through Reframe's normal source
   boundary into FountainStore.
8. All import, edit, commit, candidate, and release states are visible through AX and reconciled with service and
   FountainStore receipts.
9. A migration to another host preserves project IDs, revision IDs, metadata-template versions, hashes, release
   manifests, and rollback evidence without a Reframe code change.

Until these conditions are met, Reframe may claim only the implemented subset: managed-project browsing and
exact-revision candidate request where the project already exists on the configured service. It may not claim
repository provisioning, writable Fountain editing, or successful remote publication merely because the types or
endpoint names exist.

## Relationship to other chapters

Chapter 52 keeps the pencil with the writer. Chapter 55 governs the single FountainStore authority. Chapter 56
governs the portable Book Library and its candidate/promotion boundary. Chapter 57 governs intention-led entry.
Chapter 58 requires open-turn mediation before any project operation. Chapter 59 governs the managed Git authority,
Swift boundary, custody, accounting, and two-direction project flow. This chapter makes the Fountain editor the
writer-facing project surface without collapsing those authorities.

## Governing sentence

**Reframe is a Fountain editor with Copilot as its project mediator; Git versions and transports the project, the Book
Library decides publication, and FountainStore proves the writer's working handoff—no repository operation or
publication state may be inferred from a URL, a template, or a successful request alone.**
