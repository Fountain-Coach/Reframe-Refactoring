# FountainImagePublicationKit — Reframe Image Cloud and Publication Boundary

> Status: governing proposal for the replacement of the retired Apple Photos handoff. This chapter describes the
> target contract; it does not claim that the package, server, policy bundles, or publication adapters already exist.

## Genesis and turning point

Reframe first approached images through the machine's Photos boundary. The implementation tried to compensate for
PhotoKit's dependence on the configured System Photo Library by adding an iCloud Photos WebKit session, staging a
generated file, and asking the writer to complete an Apple upload. The result was technically honest in its receipts,
but product-wise wrong: a writer met a browser-like handoff, an external-library problem, and a second custody model
instead of an integrated Reframe image operation. The live drive exposed the seam: generation completed, but the
writer was left at “placement pending” and had to operate an external page.

That route is retired. `ReframeICloudKit`, PhotoKit gallery selection, iCloud WebKit handoff, Apple sign-in custody,
and iCloud placement are not Reframe's image-publication path. Existing references remain readable only as an
explicit migration concern; no new feature may depend on them.

The turning point is the legal and publishing requirement to make image origin, rights, AI contribution, disclosure,
and destination terms inspectable. Reframe therefore owns a clear Image Cloud boundary: the writer pastes or chooses
an image in Reframe, Reframe uploads a governed source or derivative to the Fountain Image Cloud, and the Fountain
project stores a durable cloud reference and lineage—not a local image path and not image bytes. Local Swift tooling
and remote Swift services implement the same typed contract and can run on every platform supported by Swift.

## Governing sentence

> Reframe never treats an image as publishable because it can display or generate it; a named destination receives only
> an admitted derivative whose source, rights, AI provenance, disclosure, terms, recipe, and human or policy decision
> are bound to an auditable Image Cloud receipt.

## Scope and non-goals

This chapter governs:

- image paste, selection, generation, editing, and variation in Reframe;
- the Fountain Image Cloud source and derivative service;
- the cross-platform Swift package used by local and remote tooling;
- Fountain references and image projections in the editor;
- rights, consent, provenance, EU transparency, preflight, delivery, retention, and evidence.

Image bytes entering through the Copilot composer are admitted first by [Chapter 67](67-fountain-composer-kit-remote-attachment-custody.md).
This chapter begins where the admitted attachment is treated as an image asset and governs its image-specific rights,
provenance, derivatives, disclosure, and publication state.

It does not create an Apple Photos integration, an iCloud API, a general web browser, a local image archive, or a
legal guarantee. Reframe may later import from an external source through an explicitly admitted adapter, but that
adapter ends at Image Cloud intake and never becomes the publication authority.

## Product boundary

```text
paste / choose / generate in Reframe
                 |
                 v
       FountainImagePublicationKit
    inspect -> admit -> edit -> preflight
                 |
                 v
          Fountain Image Cloud
     originals and derivatives, governed
                 |
                 v
   web / print / archive / Book publication
```

The local client performs immediate inspection, preview, recipe construction, and upload preparation. The remote
service stores content-addressed objects, manifests, policy snapshots, and terminal receipts. A server may perform
heavy transformations, but it receives only an authenticated typed request and the minimum admitted material.

Fountain text remains portable. A Fountain image directive contains a stable Image Cloud reference, caption/alt text,
lineage identity, and projection hints. It never contains a Photos path, local filesystem path, credential, cookie,
private prompt, or image bytes.

## The writer's path

The normal path is deliberately short and Copilot-mediated:

1. The writer describes an image need or attaches an image in the Copilot composer. The prompt, semantic search,
   generation request, gallery choice, and attachment admission belong to that conversation—not to a beat header,
   beat editor, or image form.
2. Chapter 67 admits the attachment to remote custody. Copilot then reasons over the active manuscript state and the
   managed Image Cloud, requesting a semantic image projection or an image-specific publication operation.
3. Reframe shows the resulting gallery inline in the Copilot projection and, when assigned to a beat, as a passive beat
   projection. A beat never becomes an image intake surface.
4. Reframe shows each image with its current state: private, rights incomplete, generated, review required, ready, or
   published. The writer may ask Copilot to caption, credit, replace, or remove an assignment.
5. A named destination is selected through the Copilot or publication surface. Preflight either admits the exact
   derivative or explains the missing decision.
6. Reframe returns a terminal Image Cloud receipt. “Uploaded”, “admitted”, “accepted”, and “published” are distinct.

The beat has no image-generation, paste, upload, or prompt control. An image icon or gallery mark on a beat is a passive
projection affordance only: it opens or focuses the images Copilot has already assigned. Private preview is never
silently promoted to public delivery.

## Typed core contract

The public package begins with dependency-light contracts. Names below are normative shapes; implementation may refine
them without weakening their semantics.

```swift
public struct ImageAssetDescriptor: Codable, Sendable, Equatable {
    public let assetID: AssetID
    public let lineageID: LineageID
    public let contentHash: SHA256Digest
    public let byteLength: Int64
    public let origin: ImageOrigin
    public let rights: RightsDeclaration
    public let consent: ConsentState
    public let aiProvenance: AIContentProvenance
    public let allowedPurposes: Set<PublicationPurpose>
}

public enum RightsAdmission: Codable, Sendable, Equatable {
    case admitted(PublicationGrant)
    case previewOnly(AdmissionReason)
    case needsReview(ReviewRequirement)
    case prohibited(AdmissionReason)
}

public enum PublicationDecision: Codable, Sendable, Equatable {
    case admitted(PublicationGrant)
    case admittedWithDisclosure(PublicationGrant, DisclosurePlan)
    case editorialReviewRequired(ReviewCase)
    case consentRequired(ConsentRequirement)
    case termsReviewRequired(TermsRequirement)
    case prohibited(ProhibitionReason)
}

public protocol ImageCloudClient: Sendable {
    func intake(_ request: ImageIntakeRequest) async throws -> ImageCloudReceipt
    func inspect(_ asset: CloudAssetReference) async throws -> ImageInspection
    func execute(_ recipe: ImageEditRecipe, for asset: CloudAssetReference) async throws -> DerivativeReceipt
    func preflight(_ derivative: CloudDerivativeReference,
                   for profile: PublicationProfile) async throws -> PublicationDecision
    func deliver(_ derivative: CloudDerivativeReference,
                 to destination: PublicationDestination) async throws -> DeliveryReceipt
}
```

The client and server share Codable contracts, deterministic identities, idempotency keys, capability declarations,
error taxonomy, and receipt verification. The package does not depend on Reframe, FountainStore, Photos, iCloud, or a
particular AI provider. Reframe owns the adapter that persists references and receipts in FountainStore.

## Image Cloud custody

The Image Cloud is the canonical Reframe image store. It is not a mounted drive and not an implicit local cache.

- Originals and derivatives are content-addressed and immutable after admission.
- Working objects are access-controlled and have explicit retention and cleanup.
- The manifest records source hash, recipe hash, tool identity/version, output hash, rights grant, AI provenance,
  disclosure, policy versions, destination, and terminal receipts.
- Reframe may retain a bounded preview cache for responsiveness; a cache is disposable and never authority.
- FountainStore persists references, manifests, decisions, and receipts, never image bytes. Exact authored image prompts
  remain excluded from those records except for the private, access-controlled `image.prompt.history` artifact governed
  by [Chapter 74](74-private-image-prompt-history.md); lifecycle receipts and public projections remain digest-only.
- Server storage, queues, databases, policy bundles, and object stores are configured by deployment identity, not baked
  into the client. Migration to another host changes an endpoint and authenticated deployment identity, not the data
  model or evidence rules.
- Logs contain no image bytes, private prompts, manuscripts, credentials, personal data, or confidential rights
  evidence.

Uploads and delivery are idempotent. A retry must converge on one asset/derivative identity and must never create a
second publication merely because the first receipt was delayed.

## Rights, consent, and AI provenance

Unknown rights, unavailable evidence, unresolved consent, expired licences, or unresolved DRM/protection state fail
closed for public delivery. Reframe does not decrypt, bypass, scrape, or defeat access control.

Every asset records:

- origin: camera/scan, human digital work, standard edit, AI-assisted edit, partial synthetic, fully generated,
  manipulated existing image, or unknown;
- owner or licence declaration, evidence reference, purposes, territory, expiry, attribution, modification,
  derivative, and redistribution terms;
- consent/model-release state where people are identifiable;
- provider, model, generation date, generation reference, input lineage, and synthetic contribution;
- whether the asset may appear authentic, depicts an existing subject, or needs editorial assessment.

Pixel inspection cannot establish ownership, authenticity, consent, or lawful publication. Recorded provenance and
human review are the authorities.

## EU and publication compliance

The first release treats EU and national requirements as a product capability, not a disclaimer. Policy profiles must
cover, at minimum, Regulation (EU) 2024/1689 including Article 50 transparency obligations, Directive (EU) 2019/790,
GDPR where personal data is involved, personality/image rights, advertising and consumer rules, provider terms, and
destination licences. This is implementation guidance, not legal advice; qualified review owns the production policy
baseline.

The kit keeps two disclosure layers:

1. **Machine-readable:** preserve trustworthy provider marks where possible; support an optional signed C2PA/Content
   Credentials adapter; record transformations and report when a destination strips or cannot preserve a mark.
2. **Human-visible:** caption, adjacent label, credit, colophon, watermark, or print notice as appropriate. Embedded
   metadata never substitutes for a required visible disclosure.

AI-generated or manipulated content that could appear authentic requires clear disclosure at first exposure. Artistic,
fictional, and satirical work receives context-appropriate disclosure. Public-interest material requires substantive
human editorial review where the applicable policy requires it. Uncertain cases remain visibly in review.

Provider and destination terms are separate, signed, versioned snapshots. A decision binds the exact source and
derivative hashes, recipe, purpose, destination, territory, disclosure, terms, policy versions, review receipt, and
expiry. Any change makes the prior decision stale.

## Editing and preflight

The initial recipe vocabulary covers orientation, crop, resize, rotate, flip, canvas and safe-area placement, colour
conversion, bit depth, alpha, permitted formats, compression, metadata inspection/redaction, thumbnails, responsive
renditions, print masters, proofs, hashes, dimensions, DPI, bleed, trim, gamut, and accessibility text.

`PublicationProfile` names the destination requirements. Preflight checks rights, consent, territory, expiry, AI
origin, disclosure, editorial review, provider/destination terms, identity, metadata leakage, provenance preservation,
format, dimensions, DPI, colour, transparency, accessibility text, and file size. Outcomes are `ready`,
`readyWithWarnings`, `needsRightsReview`, `needsUserAction`, `unsupported`, or `failed`. A warning may not hide a
mandatory condition.

## Swift cross-platform architecture

The project is a separate public Fountain-Coach FCIS-Kit repository, tentatively named `FountainImagePublicationKit`.
It is released and pinned like every other owned kit. The repository must contain `AGENTS.md`, `PLANS.md`,
`FCIS_AUDIT.md`, `FCIS_COMPLIANCE_PLAN.md`, `SOURCE.md`, package documentation, deterministic fixtures, and a README
written for both Swift engineers and publishing operators.

```text
FountainImageCore              identities, recipes, profiles, manifests, receipts
FountainImageRights             licences, consent, admission
FountainImageComplianceCore     jurisdiction-neutral evaluation
FountainImageEuropeanPolicy     reviewed EU disclosure profiles
FountainImageProviderTerms      signed terms snapshots
FountainImageProvenance         lineage and optional C2PA seam
FountainImageEditorialReview    evidence-bound review receipts
FountainImageCloudClient         typed transport, auth, retries, idempotency
FountainImageCloudServer        portable service handlers and storage ports
FountainImageApple               optional ImageIO/Core Image adapter, never iCloud authority
FountainImageHost                safe executable/tool adapters
FountainImageTestKit             deterministic providers, fixtures, policy bundles
```

The core, policy, client, server, and test-kit products are Foundation/Swift where possible. Platform adapters are
optional. The server owns no macOS assumptions; object storage, database, queue, and image-processing providers are
ports with explicit implementations. Executable adapters use argument arrays, resolved identities, restricted working
directories, timeouts, output limits, and sanitised diagnostics. No shell fragments or arbitrary executable paths
cross the public API.

The local and remote tools use the same package contracts and test fixtures. A remote deployment can move to another
IP, provider, or Swift-supported host by changing signed deployment configuration and endpoint discovery. It must not
require a Reframe binary rewrite or a data migration that changes identities.

## Reframe integration

Reframe's adapter owns only product integration:

- Copilot's composer creates the semantic image request or selects a managed gallery;
- the Image Cloud client uploads and returns a durable cloud reference;
- Copilot renders the gallery in its projection and may assign a reference to a beat;
- the Fountain editor renders an assigned reference as a passive inline visual projection;
- Copilot mediates generation, editing, captioning, review, and publication intent;
- FountainStore records the request, identity, lineage, state, decision, and receipt;
- the UI exposes the exact state through AX and does not present server success until the receipt says so.

The current iCloud handoff controls, PhotoKit picker as an image destination, WebKit upload surface, Apple Account
session, and `placement pending` language are removed from the writer-facing path. An optional Apple adapter may later
use PhotoKit as an *intake source*, but it terminates at Image Cloud intake and cannot publish directly.

## Delivery bundles

Delivery is explicit:

- **Web:** responsive renditions, dimensions, integrity hashes, alt text, disclosure, attribution, and provenance
  status.
- **Print:** press master, ICC profile, trim/bleed, DPI/gamut report, credit/disclosure placement, proof, and receipt.
- **Server/Book:** admitted derivative only, signed sanitised manifest, authenticated typed transport, idempotency key,
  and terminal accepted/published/rejected/failed receipt.
- **Archive:** source-evidence references, recipe, derivative manifest, policy and terms snapshots, disclosure, review,
  and validation result without confidential source material.

## Acceptance gates

The first release is accepted only when evidence shows:

1. No protected input is bypassed and unknown rights cannot reach public delivery.
2. Paste → Image Cloud intake → Fountain reference survives relaunch and never depends on local image storage.
3. A changed source, recipe, destination, disclosure, terms snapshot, or policy invalidates the prior decision.
4. AI origin, synthetic contribution, and required human-visible disclosure remain traceable.
5. Provider and destination terms are evaluated separately.
6. Server outage, retry, and duplicate submission remain truthful and idempotent.
7. `staged`, `uploaded`, `admitted`, `accepted`, `published`, `rejected`, and `failed` are distinct AX-visible and
   persisted states.
8. Public manifests and logs contain no private images, prompts, manuscripts, credentials, or personal data. The
   private prompt-history exception is governed separately by Chapter 74 and is never promoted into these artifacts.
9. Reframe's AX tree exposes image state, review requirements, disclosure, and terminal delivery results.
10. Local and remote Swift implementations pass the same contract, fixture, receipt, and migration tests.
11. Qualified legal review has approved the initial policy profiles and user-facing claims.

## Phased implementation

1. **Governance and policy baseline:** counsel, EU profiles, terms snapshots, non-goals, and public claims.
2. **Core contracts:** identities, lineage, recipes, profiles, manifests, receipts, rights, provenance, and fixtures.
3. **Image Cloud service:** authenticated intake, content addressing, storage ports, idempotency, retention, and
   migration-safe deployment configuration.
4. **Reframe intake:** paste/selection, inline projection, Fountain directive, Store custody, AX, and relaunch.
5. **Generation and editing:** OpenAI or another admitted provider through a typed adapter; no provider key in the
   client payload or Image Cloud browser surface.
6. **Compliance admission:** policy evaluator, disclosure, editorial review, signed terms, and fail-closed delivery.
7. **Web/print/Book delivery:** profiles, derivatives, signed manifests, publication receipts, rollback, and archive.
8. **Optional adapters:** Apple-native intake, ImageMagick, libvips, ExifTool, C2PA, and remote transforms, each with
   its own capability, licence, and acceptance gate.

## Public README and business-facing promise

The kit README must explain the writer journey, the operator deployment journey, the Swift package products, the
security and rights model, the EU disclosure posture, migration, pricing/cost boundaries, support expectations,
failure states, and exact evidence produced. It must distinguish shipped behaviour, target architecture, and legal
policy requiring review.

The product promise is precise: Reframe gives writers a simple image path and gives publishers an auditable route
from image intake to named delivery. It does not promise that an image is lawful; it makes the conditions for release
visible, reviewable, reproducible, and portable.

## Supersession

This chapter supersedes the previous Chapter 66 title and all governance text that made PhotoKit or iCloud WebKit an
image-publication destination. Historical live-drive records may retain the genesis story and observed receipts, but
they are not current runtime authority. The implementation must remove the retired controls before the Image Cloud
intake path is declared complete.

## Normative references

- Fountain-Coach Reframe Refactoring: <https://github.com/Fountain-Coach/Reframe-Refactoring>
- Fountain-Coach ReframeICloudKit: historical Apple-boundary package; not the Reframe publication path
- Regulation (EU) 2024/1689 (AI Act): <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng>
- European Commission Article 50 guidance: <https://digital-strategy.ec.europa.eu/en/policies/guidelines-ai-transparency-obligations>
- Directive (EU) 2019/790: <https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng>
- Regulation (EU) 2016/679 (GDPR): <https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng>
- C2PA Content Credentials: <https://spec.c2pa.org/specifications/specifications/2.4/specs/ContentCredentials.html>
