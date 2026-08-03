# The Released Surface Is a Named Build

> Chapter summary: The runtime command inventory, governed capability registry, live-accepted capability set, and
> shipped App surface are different projections. A release claim requires a named build, a source commit, an explicit
> capability allow-list, and release evidence. Until those exist, Reframe is a development snapshot, not a released
> capability surface.

## The problem — a command list is not a release

Reframe has accumulated slash commands across architectural eras. The current catalog is valuable: it reveals the
runtime's command spellings, aliases, compatibility routes, maintainer tools, help surfaces, and contextual
availability. It is not a product promise. A command may be historical, an alias, a local orchestration, unavailable
under current preconditions, or present only for development.

The capability registry is narrower and more meaningful. It names the writer-facing actions that have an application
owner, policy, state gates, persistence effect, and proof contract. Even an executable registry row is not necessarily
released: live acceptance, provider and consent policy, failure/resume coverage, and a named build still matter.

## The decision (enforceable rules)

1. **The release surface is a named build.** A release claim MUST identify a release ID or version, source commit,
   build/distribution identity, and the date and environment in which it was accepted.
2. **The release surface is an allow-list.** It MUST enumerate the capability identities included in that build. The
   absence of a capability from the allow-list means it is not released, even if a command, handler, or registry row
   exists in the development checkout.
3. **Commands are an inventory, not a promise.** The slash catalog MUST be labeled as a runtime/development inventory
   and MUST distinguish aliases, help, maintainer-only entries, compatibility routes, and contextual or unavailable
   commands.
4. **Only governed identities enter the release surface.** A command may be linked to a release capability only through
   the checked capability registry and its owning runtime operation. Names, prompts, screenshots, and historical docs
   cannot promote it.
5. **Live acceptance is necessary but not sufficient.** A capability enters a release allow-list only after the
   required AX, FountainStore, telemetry, terminal, provider, consent, failure, cancellation, and resume evidence for
   its declared matrix is recorded.
6. **No release means no release promise.** If no named build and manifest exist, the publication MUST say
   “no released App surface recorded” and may publish development evidence only as such.
7. **Every projection names its authority.** Runtime state owns current behavior; the registry owns capability
   identity; the live ledger owns acceptance; the release manifest owns what is shipped. Historical governance prose is
   cited as history and cannot override those records.

## The four projections

```text
runtime command catalog
  → command/development inventory (spellings, aliases, conditions)
capability registry
  → governed capability boundary (executable or unavailable)
live acceptance ledger
  → evidence-backed empowerment (AX + store + telemetry + terminal matrix)
release manifest for a named build
  → shipped capability allow-list
```

These projections may overlap, but they must not be collapsed. A release can include a capability with several command
spellings, expose a capability through natural language without a slash command, or keep a development command out of
the shipped surface entirely.

## Release manifest contract

The integration repository owns the machine-readable manifest under `releases/`. Its minimum shape is:

```json
{
  "schemaVersion": 1,
  "product": "Reframe",
  "releaseId": "<named-release-or-development-snapshot>",
  "status": "released | development-snapshot | no-released-build",
  "source": { "repository": "...", "commit": "...", "build": "..." },
  "acceptedAt": "<ISO-8601 or null>",
  "capabilityAllowList": [],
  "evidence": [],
  "excludedReason": "<why this is not a shipped release, when applicable>"
}
```

The Book publishes a sanitized projection. It MUST NOT infer a release from `main`, a screenshot, or a green build.

## Acceptance

The doctrine is met when a reviewer can answer, from repository records alone:

- Which named build is being described?
- Which capability identities are allowed in it?
- Which of those are only executable, and which are live-accepted?
- Which command entries are historical, aliases, maintainer-only, or unavailable?
- What evidence proves the release surface, and what remains explicitly outside it?

## Governing sentence

The command catalog tells us what the development runtime knows; the capability registry tells us what Reframe means;
the live ledger tells us what has been proven; only a named release manifest tells us what has shipped.
