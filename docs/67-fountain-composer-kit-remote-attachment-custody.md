# FountainComposerKit — Remote Attachment Custody and the Composer Boundary

## The decision

Reframe's composer is the single admitted input surface for a writer's turn. That turn may contain text, an image,
or a file. It is not a beat control, a local-file import lane, or a second project editor.

Fountain-Coach therefore owns a reusable, product-neutral Swift contract:

```text
Fountain-Coach/FountainComposerKit
             │
             ├── text turn
             ├── image/file attachment manifest
             ├── intent mediation
             └── remote custody receipt
                         │
                         ▼
                 Fountain Attachment Cloud
                         │
                         ├── Copilot context
                         ├── FountainStore reference/evidence
                         └── Reframe pipeline admission
```

`ReframeComposerKit` is deliberately not the package name. Reframe is the product adapter and visual host;
`FountainComposerKit` is the portable contract that local Reframe, remote tooling, tests, and future Fountain-Coach
products can share. The kit does not own a model provider, a SwiftUI view, a FountainStore directory, or a cloud
deployment.

## Governing sentence

> Every image or file enters Reframe through the Copilot composer, is admitted to the remote Attachment Cloud before
> it can affect the reading or writing cycle, and is represented locally only by a typed reference, manifest, and
> receipt.

## Why this is a new boundary

Chapter 25 defines where the writer speaks. Chapter 64 protects the Fountain project draft. Chapter 66 governs image
publication. None of those chapters alone owns the complete transition from an arbitrary composer attachment to a
remote, inspectable, pipeline input. This chapter closes that seam without moving image rights or project custody into
the composer.

The boundaries remain separate:

- `FountainComposerKit` owns turn composition, attachment admission, and attachment receipts.
- `FountainImagePublicationKit` owns image provenance, rights, derivatives, disclosure, and publication readiness.
- `FountainProjectKit` owns Fountain text, project identity, revision, recovery, and explicit publication handoff.
- Reframe owns the Copilot adapter, projection, AX surface, and product routing.
- The Attachment Cloud owns remote bytes, manifests, retention, access control, and durable evidence.

## Rules

1. **One writer ingress.** Text, images, and files enter the cycle through the Copilot composer. Beat headers,
   beat menus, image icons, Fountain directives, and projection controls are not attachment intake surfaces.

2. **Remote admission precedes use.** Reframe reads selected bytes only transiently, submits them through the typed
   cloud client, and does not send the turn to a provider or pipeline stage until the cloud returns an admitted
   attachment reference or an explicit, typed failure.

3. **No local attachment authority.** A local path, security-scoped URL, temporary file, pasteboard object, thumbnail,
   or in-memory `Data` is transport material, never the durable attachment identity. Local cleanup is part of the
   successful and failed terminal paths.

4. **The local store keeps proof, not payload.** FountainStore may retain the turn identity, attachment ID, content
   digest, media type, byte length, provenance class, policy state, remote location identifier, and receipt. It must
   not retain attachment bytes, a local file path, a private prompt, a cookie, or an unrestricted transcript copy.

5. **A turn is not admitted by appearance.** A visible preview, a successful file read, or a provider response does
   not establish remote custody. Admission requires a cloud receipt bound to the turn, content digest, attachment
   identity, policy snapshot, and idempotency key.

6. **Images retain their specialised authority.** An image attachment enters through this composer contract, but
   image rights, AI provenance, disclosure, derivatives, and publication decisions remain governed by Chapter 66.
   A generic file is not silently treated as an image or as publishable manuscript source.

7. **The composer is semantically aware.** Copilot receives attachment metadata and remote references as structured
   context: filename, declared media type, digest, size, origin, custody state, and available operations. She may ask
   what the writer wants done with an attachment; she must not infer that every file is source text, evidence, or an
   instruction.

8. **Source admission is explicit.** A Fountain or text attachment may be proposed as a source only after mediation
   identifies the writer's intent and the existing source-admission contract accepts it. Uploading a file never
   silently starts a reading, replaces a project, or publishes a work.

9. **Remote failure is visible and reversible.** Offline, unauthorized, rejected, duplicate, too-large, unsupported,
   policy-blocked, and storage-failed states are distinct. The composer leaves the writer's text available for retry,
   but does not claim that the attachment entered the cycle.

9a. **The intake ceiling is explicit and generous.** One composer turn accepts at most 8 attachments, each up to
    50 MiB, with a 200 MiB total batch ceiling. Reframe validates the complete selected batch before making the first
    admission call, so a rejected batch cannot partially overfill the turn. The Attachment Cloud independently
    enforces the 50 MiB per-object ceiling and its transport allowance. These are intake limits, not model-context
    limits, and they must be exposed as a clear AX-visible terminal explanation when exceeded.

10. **No hidden lane election.** Attachment transport may use an authorized service lane, but composer custody does
    not elect a model provider or grant paid reasoning. Lane and consent rules remain those of Chapters 20 and 51.

11. **The writer sees the work, not infrastructure.** The Copilot explains “I have the image/file and can use it for
    this turn” or the exact blocker. It does not teach the writer about object storage, FountainStore, buckets,
    upload URLs, security-scoped bookmarks, or package internals.

12. **AX is the semantic surface.** The composer exposes attachment action, selected item, admission progress,
    custody state, error, retry/remove action, and terminal receipt through AX. A spinner or preview without semantic
    state is not acceptance evidence.

12a. **Copilot owns attachment introspection.** An admitted attachment is projected inside Copilot as a readable,
     self-aware representation of the current turn. It is not a left-pane attachment list, icon strip, or second
     staging surface. Copilot states what she received, how it is classified, its custody state, and what she may do.

12b. **Visual form follows media meaning.** Images appear as visual images or galleries; PDFs as readable page-shaped
     projections; Fountain text as screenplay-page text; Markdown as rendered document-page text; unsupported types
     as honest metadata/error projections. File icons alone are insufficient when readable projection is available.

12c. **Self-awareness is not ingestion.** A visual projection proves that Copilot can identify and inspect the
     admitted reference; it does not imply manuscript import, beat creation, publication, or provider use. Reference,
     evidence, source candidate, and promoted source remain visibly distinct.

13. **Evidence is bound across seams.** One attachment receipt binds the composer turn, cloud object, digest,
    policy/provenance decision, pipeline admission, and any later Fountain or publication effect. Reframe may project
    a human-readable summary, but cannot manufacture a success state from a partial event.

14. **Deletion is a governed operation.** Removing an attachment from a turn removes its local references and records
    the requested remote retention action. It does not silently erase evidence required for an already admitted
    pipeline operation or publication decision.

## Typed contract shape

The package defines dependency-light Swift contracts. The following is normative in meaning, not an instruction to
copy these names literally:

```swift
public struct ComposerTurn: Codable, Sendable, Equatable {
    public let turnID: UUID
    public let text: String
    public let attachments: [AttachmentReference]
}

public struct AttachmentReference: Codable, Sendable, Equatable {
    public let attachmentID: String
    public let mediaType: String
    public let filename: String
    public let contentDigest: String
    public let byteLength: Int64
    public let custody: AttachmentCustody
    public let receiptID: String
}

public protocol ComposerAttachmentClient: Sendable {
    func admit(_ input: AttachmentInput, idempotencyKey: String) async throws -> AttachmentReceipt
    func revoke(_ attachment: AttachmentReference) async throws -> RetentionReceipt
}
```

`AttachmentInput` carries transient bytes only inside the call boundary. The returned reference is the only value
allowed to cross into the durable turn, FountainStore, provider context, or pipeline request.

## Package boundary

The initial package should provide:

- `FountainComposerCore` — turn, attachment, custody, receipt, and typed failure contracts;
- `FountainComposerTransport` — injected remote Attachment Cloud client and idempotency behavior;
- `FountainComposerTestKit` — deterministic in-memory cloud, interruption, retry, duplicate, rejection, and cleanup
  fixtures;
- `FountainComposerPlatform` — optional AppKit/SwiftUI adapters for transient file/image selection and AX;
- `FountainComposerEvidence` — adapters for binding receipts to FountainStore evidence without storing payload bytes.

The core must not depend on Reframe views, Copilot phrase matching, OpenAI SDKs, PhotoKit, iCloud, a local archive,
or a particular server filesystem. Remote deployment, storage, authentication, retention, and migration are injected
through typed ports and are configured outside the package.

## Lifecycle

```text
writer selects/pastes
        ↓
transient inspect
        ↓
remote admit ── failure → visible retry/remove, no pipeline input
        ↓
receipt + reference
        ↓
composer turn context
        ↓
mediated source/image/file operation
        ↓
pipeline receipt and FountainStore evidence
```

The turn may remain a draft while admission is pending. The writer's text is protected by `FountainProjectKit`; the
attachment is not considered present in the cycle until remote custody succeeds. A crash or force quit after the
receipt but before the turn is sent is recoverable from the typed reference; a crash before the receipt is not falsely
reported as admitted.

## Acceptance

The chapter is implemented only when evidence proves:

1. The composer has one image/file attachment action and beat controls have none.
2. Image and generic-file selection are transient and leave no local attachment authority after success or failure.
3. Remote admission is idempotent and returns a durable reference and receipt before pipeline use.
4. Copilot receives structured attachment context and can distinguish image, file, source candidate, evidence, and
   unsupported intent without phrase-list authority.
5. Copilot renders each supported attachment class inside its conversation/projection surface as a readable visual
   form with metadata, custody, interpretation, and allowed operation available through AX. No separate left-pane
   attachment projection is presented.
6. FountainStore contains the turn/reference/receipt/evidence aggregate but no attachment bytes or local path.
7. Offline, unauthorized, rejected, duplicate, and interrupted flows are visible through AX and terminal receipts.
8. A relaunch resolves an admitted attachment from the remote reference without requiring the original local file.
9. Image-specific rights and provenance still pass Chapter 66's gates; generic files cannot bypass source admission.
10. The portable core, local adapter, remote service, and fixtures use the same typed contract and migration tests.
11. The exact package revisions, executable provenance, AX surface, and FountainStore proof are recorded for acceptance.

## Relationship to existing governance

- Chapter 25 remains the authority for the Copilot as the sole writer-facing composer and for in-context onboarding.
- Chapter 58 mediates what the writer means by attaching or using a file before any operation executes.
- Chapter 64 protects the Fountain project text and separates working custody from publication.
- Chapter 65 defines the Writing Coach's plain-language role; attachment infrastructure stays invisible plumbing.
- Chapter 66 governs image-specific rights, provenance, and publication after generic composer admission.

The former compact left-side attachment projection is retired. Copilot is the single writer-facing place for
attachment self-awareness and introspection; the manuscript/beat surface remains reserved for actual reading and
writing state.

**Governing sentence:** `FountainComposerKit` makes the Copilot composer the one typed ingress into Reframe's cycle;
remote Attachment Cloud custody is established before use, while Reframe retains only the minimum references and
evidence needed to continue and prove the work.
