# The Fountain Project Round Trip

> Chapter summary: The Book Library and Reframe form a closed, governed Fountain Project loop. A Library release
> enters Reframe as a declared source; Reframe reads, structures, audits, and composes it; an explicit export creates
> a versioned Fountain Project; and a reviewed candidate may return to the Library as a new release. The loop is
> closed by provenance and explicit handoffs, never by silent synchronization.

Chapters 56, 59, and 60 define the three authorities separately: the Book Library publishes source releases, the
managed Git service owns versioned projects, and Reframe presents the writer-facing Fountain editor. This chapter
defines the lifecycle that connects them without collapsing their boundaries.

## The decision

The natural export moment is after Reframe's current Cut Script has passed Continuity and the writer has applied the
final Compose result. The composed Fountain text is then eligible to be materialized as a Fountain Project. It is not
exported merely because a Cut Script exists, a background compose job has started, or a candidate was suggested.

The closed lifecycle is:

```text
Book Library release
        ↓ declared source import
Reframe / FountainStore working source
        ↓ Grounding → Storify → Cut Script
        ↓ Continuity audit
        ↓ Compose / Apply
composed Fountain Project export
        ↓ explicit managed Git operation
managed Git revision
        ↓ exact revision/path candidate
review-required Book Library candidate
        ↓ human review and atomic promotion
new Book Library release
```

This is a versioned round trip, not an automatic feedback loop. Every transition is explicit, attributable,
idempotent where appropriate, and recorded. A new release is never mistaken for the release from which the work
started.

## Rules

1. **Import and export are different operations.** Library import creates or reopens a Reframe working source.
   Fountain Project export creates an external authored artifact. Neither operation implies the other, and neither
   silently commits, publishes, or re-imports.

2. **Compose is the export gate.** Export requires a current Continuity audit, an applied Compose result, and a valid
   Fountain preflight. If the Cut Script changes after Continuity or Compose, the downstream identity is stale and
   export is blocked until the affected stage runs again.

3. **The writer approves the externalization.** Reframe may offer “Export this composed work as a Fountain Project,”
   but the writer explicitly chooses the project destination, branch or new branch, commit message, and whether to
   create a Library candidate afterward. No background operation externalizes the writer's work.

4. **A round trip creates new identities.** The imported Library release, Reframe source revision, Cut Script,
   composed export, Git commit, Library candidate, and promoted release each retain their own identity. A content
   digest may establish equality; an ID must never be reused merely because the text looks unchanged.

5. **Lineage travels with the handoff.** Every export records the originating provider/work/release, source digest,
   Grounding identity, Storify structure identity, Cut Script identity, Continuity audit identity, Compose identity,
   export profile, and resulting content digest. The managed service and Library store the appropriate sanitized
   projection; FountainStore stores the Reframe handoff evidence.

6. **Lossless and semantic round trips are named differently.** If the imported source is already Fountain and the
   export preserves its governed text, the handoff may be declared content-preserving after digest verification. If
   the source is converted, normalized, or composed into a new form, the result is a semantic transformation with a
   declared transformation version. Reframe never calls a semantic conversion byte-identical.

7. **Front matter is generated at the project boundary.** The export may create or repair governed Fountain front
   matter for work ID, title, author, language, and publication state. Front matter expresses the authored project
   declaration; it does not prove rights, provenance, attribution, jurisdiction, content digest, or publication.
   Those remain independently validated by the Book Library and managed service.

8. **Internal Reframe markers do not become accidental public contract.** Cut Script unit markers, editor hints,
   continuity annotations, and internal orchestration text are either represented through the declared export profile
   or kept in a provenance sidecar. They must not silently leak into writer-facing Fountain prose or be discarded
   without an explicit loss/transformation record.

9. **The Git commit is not the Library release.** A successful export or commit proves only that a versioned project
   exists. Candidate creation, rights review, approval, promotion, and publication create later states and receipts.
   Reframe reports each state separately.

10. **The Library candidate is isolated.** A candidate created from the exported project names the exact project,
    commit, path, front matter, source lineage, normalized digest, rights record, and idempotency key. It does not
    modify the Git project, the current published release, or the Reframe working manuscript.

11. **Promotion closes one cycle and starts another.** A promoted release is immutable and becomes a new source
    authority. Re-importing it into Reframe is a new operation with a new working-source identity, even when the
    content digest matches the exported project.

12. **No recursive automatic loop.** Reframe must not automatically import a release it just exported, and the
    Library must not automatically promote a candidate merely because it came from Reframe. The writer or authorized
    reviewer chooses when the next cycle begins.

13. **Failures stop at the owning boundary.** A stale Continuity audit blocks export; an invalid Fountain document
    blocks export; a Git custody or expected-ref failure blocks commit; a candidate provenance/rights/digest failure
    blocks Library review; and a promotion failure leaves the prior release as rollback target. No layer reports a
    downstream success from an upstream request alone.

14. **FountainStore proves the working handoff.** Store evidence must identify the imported source, downstream
    identities, export request, external operation, candidate/release handoff, and terminal result. Service receipts,
    Git logs, screenshots, and HTTP responses are useful corroboration but cannot replace persisted behavioural proof.

15. **AX tells the writer what can happen next.** The Copilot and editor expose source release, revision, dirty state,
    Continuity freshness, Compose freshness, export preview, destination, confirmation, operation phase, candidate
    state, and terminal result through the accessibility tree. A spinner or a green request response is not a loop
    state.

16. **Round-trip migration is host-independent.** Moving the managed Git service or Book Library to another host
    preserves project IDs, revision IDs, release IDs, content digests, transformation versions, and provenance. DNS
    and endpoint configuration change; the round-trip identities do not.

## Identity ledger

The minimum relationship is:

```text
sourceReleaseID
  → reframeSourceRevisionID
  → groundingIdentity
  → storifyStructureIdentity
  → cutScriptIdentity
  → continuityAuditIdentity
  → composeIdentity
  → fountainExportDigest / exportID
  → gitProjectID + gitRevisionID + path
  → libraryCandidateID
  → promotedReleaseID
```

These are references, not a demand that every layer copy every upstream payload. Each authority stores the fields it
owns and a stable reference to the others. A missing link is an incomplete handoff, not an invitation to infer one
from timestamps, filenames, branch names, or matching prose.

## Ownership boundary

```text
Book Library
  published source releases, provenance, rights, candidates, promotion, withdrawal

Reframe / FountainStore
  working source, Grounding, Storify, Cut Script, Continuity, Compose, export intent, handoff proof

Managed Git service
  project custody, refs, revisions, trees, blobs, commits, ACLs, operation receipts

Fountain Project
  portable composed Fountain text, governed front matter, and declared export profile
```

The Fountain Project is the portable authored artifact at the seam. It is not a FountainStore dump, not a Library
release by itself, and not a replacement for the managed Git repository that versions it.

## Acceptance boundary

This chapter is implemented only when the following are demonstrated:

1. A published Library work imports into Reframe with source release identity and provenance intact.
2. Grounding, Storify, Cut Script, Continuity, and Compose identities are persisted and freshness gates are enforced.
3. A composed Cut Script can be previewed and exported as a Fountain Project with governed front matter and a declared
   export profile.
4. A stale downstream identity blocks export with a writer-visible reason and a valid next action.
5. A Fountain Project can be committed explicitly to a managed Git project using expected-revision protection.
6. An exact exported revision/path creates an isolated, review-required Library candidate without mutating the project,
   Reframe manuscript, or published release.
7. A promoted candidate can be imported again as a new Library release, with a complete lineage ledger and no false
   claim of byte identity when transformation occurred.
8. Duplicate, cancelled, unavailable, rights-failed, digest-mismatch, stale-ref, invalid-front-matter, and failed-
   promotion cases each produce typed terminal evidence.
9. AX, window-ID visual capture, service receipts, and FountainStore artifacts agree for a positive round trip.
10. The same round trip survives managed-service migration without changing project or release identities.

Until then, the system may claim only the individually accepted slices. The existence of import, Git browsing, or
candidate types does not prove a complete round trip.

## Relationship to other chapters

Chapter 50 governs addressable text. Chapter 52 keeps authorship with the writer. Chapter 55 governs the single
FountainStore authority. Chapter 56 governs Library source, candidate, release, and migration. Chapter 59 governs
managed Git projects, custody, accounting, and explicit project flow. Chapter 60 governs the Fountain editor,
front-matter templates, and project surface. This chapter closes their lifecycle without replacing any authority.

## Governing sentence

**The Fountain Project loop is closed by explicit, versioned handoffs: every imported release, composed project, Git
revision, candidate, and promoted release keeps its own identity and provenance, and no loop transition is automatic
or falsely described as lossless.**
