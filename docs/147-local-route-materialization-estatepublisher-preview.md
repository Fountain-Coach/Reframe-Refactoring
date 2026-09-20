# 147 — Local Route Materialization: EstatePublisher Preview Before Check-In

> Governance chapter: 147. This chapter governs the existing local EstatePublisher draft lifecycle. It names no new
> CRUD or REST authority: the existing typed preview operations are the contract.

![Local route materialization through EstatePublisher](illustrations/147-local-route-materialization-estatepublisher-preview.svg)

## The decision

New estate content uses two existing local operations:

1. `estate.preview.draft-refresh` patches one selected route in the disposable preview Store and running native
   FountainStoreHTTPServer without restart, durable check-in, or remote publication.
2. `estate.preview.draft-check-in` requires the displayed digest, rejects drift, and writes the selected route into the
   explicit local FountainStore candidate. Remote publication remains separate.

The same typed route patch updates an existing host/path identity or creates an absent one. It receives explicit source,
host, normalized path, revision, template, and snapshot identity and returns a route/content digest. FountainStoreHTTP
is a read projection, not a CRUD or OpenAPI authority.

The current EstatePublisher catalog, scenarios, `EstatePublisherPreviewRefreshExecutor`, route materializer, route-patch
seam, and Store session are reused. No `estate.route.create/update/delete` parallel surface is introduced.

## Rules and proof

Draft refresh is disposable and non-publishing. Check-in is the only explicit local candidate write in this lifecycle.
The contract is established when refresh changes the selected route on the existing lease without changing its server
PID, check-in accepts the displayed digest exactly once and reads it back from the candidate Store, and remote
publication remains a separate explicit operation. HTTP status, screenshots, and file changes alone are not proof.

## Governing sentence

**EstatePublisher writes or creates one local route through the existing typed preview patch, FountainStoreHTTP shows it,
the writer explicitly checks it in, and remote publication remains a separate act.**
