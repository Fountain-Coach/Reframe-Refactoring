# Public Publication and Private Source Policy

The Fountain Coach public publications are evidence-backed projections, not mirrors of private implementation
repositories. This policy governs what may be published, what remains private, and how a reader follows the authority
chain without encountering a misleading access failure.

## The decision

1. **Public documentation may publish reviewed projections.** A publication may contain human-readable command and
   capability descriptions, sanitized release manifests, AX/VRT evidence, provenance, and links to public governance.
2. **Private implementation remains private by default.** Runtime source, private dependencies, private fixtures,
   manuscript material, FountainStore records, credentials, deployment details, and unreleased product machinery are
   not publication material.
3. **A private repository is never presented as a public source.** If GitHub access is restricted, the publication
   must say so plainly rather than give a public reader a link that resolves to a 404.
4. **Governance is the public explanation of the boundary.** Public publications link to this governance repository
   for architectural and release doctrine. Governance does not replace runtime truth, the capability registry, live
   evidence, or the release manifest.
5. **Sanitized contract projections are allowed.** A separate public contract or evidence projection may publish
   generated schemas, capability identities, release boundaries, and sanitized proof, provided it contains no private
   source, secrets, personal data, manuscript text, or unaudited claim.
6. **Making implementation public is a separate decision.** It requires an explicit repository-visibility decision,
   license review, secret and dependency scan, fixture/data scrub, and maintainer review. Documentation publication
   must never silently make that decision.

## The authority chain

```text
private runtime and live state  → current behaviour
checked capability registry     → capability identity and policy
live acceptance ledger           → what has been proven
named release manifest           → what has shipped
public Book projection           → what readers can inspect
public governance                → why these boundaries exist
```

The Book may publish development evidence only when it labels it as development evidence. A command catalog is not a
release promise, a screenshot is not a capability contract, and governance prose cannot override live runtime state.

## FCIS publication requirements

- `AGENTS.md` states the private/public boundary as an invariant.
- `PLANS.md` records the publication scope, exclusions, validation, and rollback for a policy change.
- A maintenance skill performs the sanitized projection and fail-closed validation.
- FCIS-AX and FCIS-VRT evidence remain separate authorities.
- `SOURCE.md` identifies the private runtime, the public governance source, the sanitized projection, and access status.
- Public links must resolve for their intended audience or carry an explicit access note.

## Governing sentence

Fountain Coach publishes what a reader can check, keeps implementation private unless it is deliberately released, and
never uses a public publication to imply access to a private runtime.
