# 146 — Local FountainStore, Remote Caddy: The Production Static Estate

> Governance chapter: 146. This chapter establishes a named production profile for the Fountain Coach static estate.
> It does not claim that the Caddy capability, migration, or remote release is already implemented.

![Local Store to remote Caddy production estate](illustrations/146-local-store-remote-caddy-production-estate.svg)

*Principal illustration — a deterministic authority projection. It explains the intended release path; it is not a
publication receipt, a Caddy health witness, a TLS proof, or a live remote read-back.*

## The production decision

The production estate serves static routes from remote Caddy. The writer does not publish by making the remote
FountainStore answer every public page request.

The local, explicit FountainStore remains the authoring and preflight authority. EstatePublisher is the sole publication
authority. Its FCIS-KIT-owned operation compares the admitted local Store state, builds a deterministic immutable static
release, signs and records its manifest, transfers it to the remote host, atomically promotes one release root, and
reads the public route back through HTTPS. Caddy serves the active release as a read-only projection.

```text
checked-in estate + local FountainStore
                 │ typed preflight and semantic diff
                 ▼
       EstatePublisher / FCIS-KIT
       package · sign · admit · receipt
                 │ atomic release promotion
                 ▼
       remote Caddy active root
                 │ HTTPS static projection
                 ▼
       public estate · SVG · assets · Teatro embeds
                 ▲
       digest · HTTPS · rollback receipt
```

Remote FountainStore is not required in the public request path for this profile. It may remain as a separately governed
Store service for another capability or as a migration/recovery option, but it is not silently the authority of this
static release. Caddy is not an authoring surface, a semantic interpreter, or a second Store.

## What remains one authority

There is still one publication authority and one publication identity. The topology changes the destination projection,
not the ownership model:

| Concern | Production authority | Projection or witness |
| --- | --- | --- |
| authored estate | checked-in `estate/` plus local FountainStore | local preview |
| semantic diff and admission | EstatePublisher through FCIS-KIT | typed operation state |
| release bytes | deterministic immutable release manifest | remote Caddy root |
| public serving | Caddy active root | HTTPS response |
| trust, DNS, TLS, host mutation | named FCIS-KIT capabilities under Chapters 94/139–143 | typed receipts |
| observation and explanation | Reframe Semantic Browser and Copilot | estate-wide logo/report |
| publication proof | correlated manifest, digest, receipt, and read-back | never a logo, screenshot, or HTTP 200 alone |

The remote edge is deliberately boring: it serves the admitted bytes and does not decide what they mean.

## Release and rollback contract

Each release has a release ID, source revision, template revision, route manifest digest, asset digest, creation
correlation, authorization-session identity, and previous-release pointer. The remote host retains the previous immutable
root until the new release has passed validation and public read-back. Promotion is one atomic active-root change.

The operation must validate the Caddy configuration, reload only after the new root is complete, check the selected
HTTPS routes and certificate identity, and persist a typed receipt. A failed transfer, validation, reload, or read-back
leaves the previous release active. Recovery is a release-root rollback, not an ad-hoc file edit.

The local authoring machine may be offline after a release is established; the remote Caddy projection continues to
serve the last accepted release. Conversely, no new release may be claimed while local Store preflight, authorization,
or the typed remote witnesses are unavailable.

## Perspective on the existing governance

This chapter is a production-profile amendment and crosswalk. It does not erase earlier chapters.

| Existing chapter | Perspective under this production profile |
| --- | --- |
| 91, 93, 112 | FCIS-KIT ownership and mechanical constraints remain normative. Caddy administration must become a named kit capability; no host adapter or shell fallback becomes authority. |
| 92 | The connected estate remains one semantic domain. Its domains now project one admitted release rather than independently publishing. |
| 94, 96–97 | Provider-neutral infrastructure, DNS, TLS, and host enrollment remain separate witnessed capabilities. They are prerequisites, not hidden side effects of copying files. |
| 115 | Reframe remains a governed Semantic Browser and MIDI2/FountainStore observer; it does not become a static deployer. |
| 116 | Its Store-native edge is the existing production profile and remains valid where selected. For Chapter 146, local Store authority and remote Caddy projection replace remote Store serving; remote Store read-back is replaced by release-root and HTTPS read-back. |
| 117–118 | Snapshot, recovery, continuity, and risk evidence still apply. The immutable Caddy release is a projection, never a second authoring Store. |
| 125, 127–129 | Typed route mapping, the estate template, read-only mirror semantics, and deterministic SVG/static bundles carry forward unchanged. |
| 130–131 | Stable scenario identity and one bounded credential/session boundary apply to release promotion; repeated prompts are not a deployment protocol. |
| 134–138 | EstatePublisher remains the publication authority; Web, Native, Headless, Teatro, and Ear remain projection/runtime boundaries, not publication authorities. |
| 139–143 | Owner trust, joining-machine admission, FountainAuthKit, one bootstrap/one trusted session, rotation, and recovery govern the release operation. |
| 144 | The Media Service still owns media compilation and verified derivatives. Caddy may serve admitted static derivatives but does not compile media or carry media control state. |
| 145 | The estate-wide signal and Reframe/Copilot observation model remain. Its publication identity must report the Caddy release digest and receipt for this profile instead of implying remote Store read-back. |

The result is a coherent choice between two explicitly named profiles:

1. **Store-native profile:** local FountainStore → remote FountainStore → native Store edge, governed by Chapter 116.
2. **Static production profile:** local FountainStore → EstatePublisher/FCIS-KIT → immutable remote Caddy release, governed
   by this chapter.

Neither profile may be inferred from a URL, a running process, or a successful HTTP response. The selected profile must
be declared by the scenario and established by its typed terminal proof.

## Implementation boundary

The next implementation work is not “copy the website to Caddy.” It is one named FCIS-KIT instrument and scenario:

1. declare the static-release identity, inputs, predicates, refusal states, and terminal receipt;
2. reuse local Store preflight and EstatePublisher semantic diff;
3. package a deterministic release with an immutable manifest and previous-root pointer;
4. perform authenticated, bounded Caddy installation and atomic promotion through the kit-owned capability;
5. verify Caddy configuration, HTTPS/DNS/TLS, selected routes, digest, and rollback; and
6. expose the same typed state to Reframe, Copilot, and every estate logo.

Until that scenario is admitted and passes, the static production profile is a governed target and the Store-native path
must not be silently removed.

## Acceptance boundary

This chapter becomes operationally established only when one correlated proof shows:

1. the local Store snapshot and semantic diff were admitted;
2. the release manifest and bytes are deterministic and immutable;
3. FCIS-KIT, not a host adapter or shell script, owns authorization and remote mutation;
4. Caddy activates exactly one release root atomically;
5. HTTPS/DNS/TLS and selected route read-back match the release digest;
6. failure leaves the prior root active and rollback is witnessed; and
7. Reframe observes the same receipt without becoming a second publisher.

## Rules

1. Chapter 146 is the governing production profile for static public routes served by remote Caddy.
2. The local explicit FountainStore is the authoring, preflight, and semantic-diff source.
3. EstatePublisher is the sole publication authority; its Caddy release operation is FCIS-KIT-owned.
4. Remote Caddy serves immutable admitted bytes and has no semantic or authoring authority.
5. Remote FountainStore is not a dependency of the static public request path in this profile.
6. Every promotion is atomic, digest-addressed, receipt-backed, and reversible to the previous release.
7. DNS, TLS, host enrollment, and cloud-provider operations remain separate typed capabilities with separate evidence.
8. Reframe/Copilot observes and explains the release state; it does not copy, reload, or publish the estate.
9. A screenshot, HTTP 200, logo animation, or Caddy process alone never establishes publication.
10. The Store-native Chapter-116 profile remains available until a separately accepted migration retires it.

## Governing sentence

**The local FountainStore authors; EstatePublisher and FCIS-KIT admit and promote one immutable release; remote Caddy
serves it; Reframe explains it; no edge, adapter, or page becomes a second authority.**
