# Reframe Image Sources, Prompting, and Generation

> Chapter summary: Reframe treats images as authored, referenced, and generated material alongside Fountain text.
> Apple Photos/iCloud is accessed only through PhotoKit; Fountain remains portable text; and OpenAI image generation
> is a governed Copilot capability whose prompt, source references, result, cost, and lineage are all visible and
> recoverable.

## Purpose

Reframe's writing surface is text-first, but a writer may think through photographs, visual fragments, memories,
references, and generated images. The `.fountain` format is not a photo archive and must not be forced to become one.
The correct design is a compound boundary:

```text
Fountain text and image directives
        +
PhotoKit references selected by the writer
        +
writer-authored image prompt
        ↓
Reframe image operation
        ↓
OpenAI image generation or editing
        ↓
visual projection + durable lineage
```

This chapter governs the compound capability. It does not replace Chapter 60's Fountain editor contract, Chapter
64's durable draft custody, Chapter 65's Writing Coach role, or Chapter 20's provider and writer-key rules.

## The decision

1. **Reframe does not own the Photos archive.** Apple Photos/iCloud remains the canonical photo archive. Reframe
   stores references, selected working material, prompt text, generated results, and lineage. It does not duplicate
   the user's catalogue.
2. **PhotoKit is the Apple boundary.** Production code must use public PhotoKit authorization, fetch, thumbnail, and
   resource APIs. Reframe must not read or write `Photos.sqlite`, walk a `.photoslibrary` package, assume a library
   path, use private iCloud endpoints, or repair/reconfigure Photos.
3. **The probe precedes production integration.** A read-only native PhotoKit probe must establish authorization,
   catalogue scale, metadata, thumbnail retrieval, resource retrieval, and—where an appropriate asset exists—
   network-enabled retrieval of a cloud-resident original. A wrong or stale catalogue blocks integration; it does
   not authorize a filesystem workaround.
4. **The Fountain document remains text-first.** Images are represented by structured, portable directives or
   references. Image bytes do not enter the Fountain text document. The editor renders the directive as a visual
   projection while preserving the underlying text and metadata.
5. **The writer's prompt remains primary.** The prompt the writer types is preserved verbatim. Reframe may add
   explicit operational context—selected references, output medium, size, format, or safety-required preparation—
   but must distinguish writer text from generated or inferred instruction. It may not silently replace the prompt
   with an internal prompt.
6. **Image generation is a Copilot capability.** The writer may ask the Copilot to create, edit, vary, compare, or
   place an image. The Copilot mediates the turn, resolves the current selection and Fountain context, states what
   will be sent, and hands the operation to the existing provider executor. There is no second image command router.
7. **PhotoKit and OpenAI are separated by Reframe.** PhotoKit materializes only the selected representation into
   Reframe-owned temporary storage. Reframe then sends the minimum required image and prompt payload to the current
   OpenAI image API. PhotoKit never communicates with OpenAI directly.
8. **A generated image is not an edit of the source by default.** The original Photos asset remains unchanged. A
   generated result is a new Reframe object and may be saved as a new Photos asset only through a later explicit
   writer action.
9. **Every result carries lineage.** Reframe records the prompt, source references, selected resource form, provider
   operation, result identity, and relevant preparation facts. A result without source/prompt lineage is incomplete
   and must not be presented as publishable evidence.
10. **The visual projection is not the authority.** The left projection shows the selected source, prompt, progress,
    and result; the right Copilot mediates and explains. FountainStore and the durable Fountain project remain the
    behavioural authorities.

## The prompt contract

An image prompt is a first-class authored object, not an unstructured string hidden in a network request:

```text
ImagePrompt
-----------
id
writerText
operation: generate | edit | variation
sourcePhotoReferences[]
sourceFountainReferences[]
groundingIdentity?
medium?
constraints[]
providerParameters
createdAt
resultReferences[]
```

The contract has three distinguishable layers:

```text
writer text       = what the writer asked for
grounded context  = what Reframe can establish from selected work/material
transport options = size, format, quality, detail, and provider requirements
```

Only the first layer is the writer's authored prompt. The second must be evidenced; the third must be inspectable as
technical execution state. The system must not present provider parameters as if the writer authored them.

Natural language is the primary interface. For example:

> “Make a visual memory vector from these pictures, keeping the same person across the years.”

The Copilot resolves the selected references and asks only for a missing decision that materially changes the
result. A structured image directive may also be written into Fountain:

```fountain
.IMAGE PROMPT
Text: A visual memory vector made from these moments across several years.
Source: photokit://reframe/photo-123
Operation: generate
Result: reframe://generation-456
```

The exact directive grammar belongs to the Fountain parser contract and must be versioned. Unknown directives remain
preserved as text or are reported as unsupported; they must never be silently discarded.

## PhotoKit boundary and reference identity

The product abstraction is independent of Photos' physical storage:

```swift
protocol PhotoLibraryBackend {
    func authorizationStatus() async -> PhotoAuthorizationState
    func requestAuthorization() async -> PhotoAuthorizationState
    func fetchAssets(query: PhotoAssetQuery) async throws -> [ReframePhotoAsset]
    func fetchAsset(id: PhotoAssetReference) async throws -> ReframePhotoAsset?
    func requestThumbnail(for asset: PhotoAssetReference, targetSize: CGSize) async throws -> CGImage
    func materializeImageResource(
        for asset: PhotoAssetReference,
        preference: PhotoResourcePreference
    ) async throws -> MaterializedPhotoResource
}
```

`PHAsset.localIdentifier` is a PhotoKit resolution key, not Reframe's entire identity. A Reframe reference may carry
an internal UUID, PhotoKit identifier, media type, dimensions, creation date, resolution state, and an optional
fingerprint computed only when the selected resource is materialized. Reframe must tolerate an unresolved reference
without mass-downloading or duplicating the source archive.

Browsing is layered:

```text
metadata → thumbnail → selected high-quality resource → temporary provider material
```

Full originals are never fetched merely because the writer browses. Network-enabled retrieval is permitted only for
an explicit operation requiring the selected asset. Progress and cancellation must be surfaced where PhotoKit
supports them.

## OpenAI image boundary

Reframe's image capability may use the current OpenAI image-generation/editing API, including image inputs and
streamed partial image events where the selected integration supports them. The provider adapter must follow the
current official API contract at implementation time; model names, parameter limits, output formats, and transport
details must not be frozen in this chapter.

The governed operation is:

```text
resolve selected PhotoKit assets
  → materialize selected representation in Reframe temp storage
  → validate type, dimensions, and transport requirements
  → present/record composed prompt
  → invoke OpenAI image generation or editing
  → display result and progress
  → persist lineage and result
  → clean temporary source material
```

“Direct integration” means that Reframe owns this user-facing capability and its lifecycle. It does not mean that a
distributable client embeds an uncontrolled long-lived privileged key. Provider credentials remain governed by
Chapter 20 and the existing Reframe maintenance/SecretStore boundary. A cloud image call requires the same explicit
writer authority as any other paid or cloud operation.

## User-visible states

The image operation must expose truthful states through AX, the projection, and persisted lifecycle events:

```text
selecting source
preparing image
retrieving original from iCloud
preparing prompt
awaiting provider authority
generating
result available
cancelled
failed at PhotoKit / preparation / provider / result handling
```

No generic spinner or “nothing happened” message may hide which boundary is active. A PhotoKit failure must not be
reported as an OpenAI failure, and an OpenAI failure must not be described as a missing Photos asset.

## Privacy and custody

For one generation request, the default data boundary is:

```text
Leaves the Mac:
  selected image representation(s), writer prompt, required provider metadata

Does not leave the Mac by default:
  the entire Photos catalogue, unrelated originals, Photos database,
  Apple credentials, or the .photoslibrary package
```

Reframe retrieves only what the writer selected, does not index the full library, and does not retain temporary
source material beyond the bounded operation and its cleanup policy. Generated results and prompt lineage may be
persisted in Reframe's project store; source originals remain owned by Photos.

## Failure and cancellation contract

Photo and provider failures remain typed at their boundary:

```swift
enum PhotoBackendError: Error {
    case authorizationDenied
    case authorizationRestricted
    case assetNotFound
    case resourceNotAvailable
    case cloudDownloadFailed(underlying: Error)
    case requestCancelled
    case unsupportedAssetType
    case temporaryFileFailure(underlying: Error)
}

enum ImageGenerationBridgeError: Error {
    case sourceResolutionFailed(PhotoBackendError)
    case unsupportedInput
    case preparationFailed
    case uploadFailed
    case generationFailed
    case responseInvalid
    case cancelled
}
```

Cancellation must propagate through PhotoKit materialization, provider upload/generation, projection state, and
cleanup. Duplicate requests for the same asset and prompt must be coordinated rather than launched in parallel.

## Fountain and projection rules

1. Image directives are portable references, never embedded binary data.
2. The Fountain editor renders image blocks as visual cards or inline projections without changing the author's
   text unexpectedly.
3. The projection exposes source, prompt, result, lineage, and state through AX; a screenshot alone is not proof.
4. A generated result can be accepted, rejected, regenerated, or left provisional. It is never silently inserted
   into the manuscript as if it were writer-authored text.
5. Export preserves the directive and its references according to the declared Fountain grammar. A target that cannot
   resolve the image receives a clear placeholder or export error, never a fabricated image.
6. Reframe's image projection remains subordinate to the Fountain project surface; it does not create an unrelated
   media browser or second authoring surface.

## Phased implementation and acceptance

### Phase 1 — PhotoKit probe

Build a native, read-only probe with the correct Photos usage description. Record authorization, catalogue counts,
collections, representative metadata, thumbnail access, local-only retrieval, network-enabled retrieval, resource
inventory, progress, and repeated-launch stability. Do not create, move, repair, select, or modify a Photos library.

Phase 1 is a pass only when the visible catalogue is the expected one and selected resources can be retrieved through
PhotoKit. If no cloud-only asset can be identified, record a conditional pass rather than claiming cloud retrieval
proof.

### Phase 2 — Fountain image directives and Reframe adapter

Add versioned parser support for image references/prompts, implement the `PhotoLibraryBackend`, add bounded thumbnail
and temporary-resource services, and persist references without copying the archive. Verify parser round-trip,
unknown-directive preservation, AX projection, cancellation, relaunch, and cleanup.

### Phase 3 — one OpenAI image operation

Prove one selected PhotoKit asset plus one writer prompt through preparation, current OpenAI generation/editing,
result projection, Fountain reference, Store lineage, and cleanup. The original Photos asset must remain unchanged.

### Phase 4 — production breadth

Only after Phase 3 passes may Reframe add multiple references, edits and masks, Live Photo/RAW policies, result
collections, optional explicit “Save Result to Photos,” streaming partial results, and richer visual composition.

## Acceptance evidence

The capability is accepted only when all of the following are observed and attributed to their artifact:

- PhotoKit authorization and catalogue state from the native probe;
- selected asset identity and resource form from PhotoKit diagnostics;
- composed prompt and writer text through AX and the persisted prompt record;
- provider lifecycle and result identity through FountainStore;
- window-ID screenshot showing the source/prompt/result projection;
- Fountain parse/serialize round-trip preserving image directives;
- source Photos asset unchanged;
- temporary material cleaned up;
- no `.photoslibrary` filesystem access, Photos database access, library creation, or automatic Photos export;
- clear failure attribution for authorization, cloud retrieval, preparation, provider, cancellation, and result
  handling.

## Relationship to other chapters

- **Chapter 20 — On-device first, and the writer's key:** governs cloud/provider authority and credential custody.
- **Chapter 23 — One reasoning:** image requests enter through the single intent decision; no image-specific fast
  router may steal a turn.
- **Chapter 24 — The reasoning is an uncertainty map:** ambiguity about source, operation, or intended result is
  clarified rather than guessed.
- **Chapter 25 — The Copilot is the surface:** prompt teaching, selection, confirmation, and result explanation live
  in Copilot dialogue and its left projection.
- **Chapter 40/41 — Citation and retrieval:** external image references and evidence remain provenance-bearing and
  checkable; a generated image is not evidence merely because it looks plausible.
- **Chapter 60 — The Fountain editor is the project surface:** image directives extend the editor without replacing
  the text-first project surface.
- **Chapter 64 — FountainProjectKit durable custody:** prompt and directive edits are flushed immediately and survive
  interruption or relaunch.
- **Chapter 65 — Writing Coach:** the Coach helps the writer articulate visual intent without becoming an automatic
  author or silently rewriting the prompt.

## Governing sentence

Reframe lets a writer bring a remembered image into a Fountain project, describe what it should become, and receive a
traceable generated result—while Photos remains the archive, Fountain remains portable text, OpenAI remains a bounded
provider, and the writer remains the author.

## Implementation references

The implementation must consult the current primary documentation for [PhotoKit](https://developer.apple.com/documentation/photokit),
[`PHAssetResourceManager`](https://developer.apple.com/documentation/photos/phassetresourcemanager), and the
[OpenAI image generation API](https://platform.openai.com/docs/guides/image-generation) at implementation time.
