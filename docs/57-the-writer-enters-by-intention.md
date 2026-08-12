# The Writer Enters by Intention

The writer does not begin Reframe by learning its provider menu, its internal IDs, or its lane vocabulary. She
begins with a want: a manuscript to open, a passage to read, a question to pursue, or work already in progress.
The landing surface is therefore a situated Copilot opening, not an empty canvas with a mysterious `+` control.

This chapter governs the Reframe landing experience and the discovery of the Book Library. It extends chapters 15,
18, 20, 22, 25, 47, and 56. It does not create a second workflow engine: the Copilot discovers and explains the
existing catalog and dispatches the existing import operation.

## The decision

1. **The landing asks for intention.** A fresh Reframe window presents a concise, writer-facing prompt such as
   “What would you like to read or work on?” It offers the Copilot as the primary entry point and does not require
   the writer to discover a provider menu before she can begin.
2. **The `+` is not the writer's library vocabulary.** The visible plus/import control may be retired from the
   primary landing when its operations have a dialogic home. The underlying structured actions remain available to
   accessibility, tests, and deliberate expert paths; retiring chrome never retires capability.
3. **The Copilot is grounded in live source state.** For Book Library discovery she receives the current published
   catalog, not a hand-written list, stale onboarding text, remembered IDs, or a model's general knowledge. Catalog
   entries expose human-readable title, author, language where available, edition/provenance, publication state, and
   the stable internal work address.
4. **The writer addresses works by meaning.** “Find Freud's German Vorlesungen” and “open Circe from Ulysses” are
   valid writer requests. The provider work ID is an implementation address resolved after catalog retrieval; it is
   not a prerequisite the writer must know or type.
5. **Ambiguity is clarified, never guessed.** If several editions or works match, the Copilot presents the candidates
   with the distinction that matters and asks the writer to choose. If no published work matches, it says so and may
   offer a governed curation request; it may not fetch arbitrary Gutenberg content or publish it from the dialogue.
6. **The introduction is writer-facing; lane selection protects credibility.** Catalog search, explanation of
   availability, source distinction, and import preparation may run on-device when that is sufficient. Open-ended
   Copilot conversation and Coaching Mode use the reliable paid lane by default once the writer has authorized it;
   the app must not force a visibly weaker local dialogue to save a call. Before any paid use, the reason, elected
   lane, and cost are stated and the writer's consent is recorded. If the local mediator cannot fit or decode a turn,
   it preserves the turn and offers the authorized paid route instead of exposing an internal capacity failure.
7. **The landing is situated.** With no manuscript open, the Copilot says that the workspace is empty and offers
   reading/import discovery. With a manuscript already open, she offers relevant continuation or navigation and never
   proposes opening the work that is already open. Her words and affordances are derived from live application state,
   as required by chapter 15.
8. **The act remains central.** Once a work or project is selected, the manuscript or reading act becomes the largest
   and most central element. Catalog metadata, lane facts, provenance, and import progress recede behind progressive
   disclosure. The landing is an invitation, not a dashboard.
9. **AX is semantic truth and operability.** Every landing state and library interaction must expose an accessibility
   role, stable identifier, label, value/state, and supported action. The AX tree must contain the prompt, current
   situation, catalog result identity, source/publication status, selection, import action, and failures. A writer or
   agent must be able to search, choose, clarify, cancel, and retry without coordinates or screenshot interpretation.
10. **AX readability is separate from visual proof.** AX presence does not prove visual legibility. The rendered
    landing and catalog must also pass the glasses test in light, dark, Increase Contrast, and Reduce Motion states:
    readable type, sufficient contrast, clear focus, generous spacing, and no colour-only meaning. Both proofs are
    required; neither substitutes for the other.
11. **The source seam stays visible but quiet.** After selection, Reframe identifies the source as Book Library,
    DraCor, local file, or another governed provider and shows the edition/provenance in a checkable disclosure. The
    writer is not asked to manage HTTP, releases, hashes, or deployment details.
12. **Failure teaches the next action.** A catalog outage, unavailable work, ambiguous result, rejected import, or
   lane refusal appears in the writer's dialogue and AX state with a bounded next step. An empty catalog is not
   silently treated as “nothing exists,” and a missing ID is not repaired by guessing.
13. **Copilot is a semantic library agent.** A writer may describe a work by subject, language, period, form, author,
   provenance, or a combination of those meanings. The Book Library supplies grounded metadata candidates; Copilot
   interprets the writer's intent using the lane that preserves the required conversational quality and explains why
   candidates fit. General model knowledge is never treated as proof that a work is published.
14. **Retrieval and interpretation are separate.** The provider may retrieve candidates through a searchable metadata
   surface, but it does not decide the writer's meaning. Copilot may ask for clarification, preserve ambiguity, or
   select one explicit candidate; it may not silently turn a relevance score into an import.
15. **Scale does not become a catalog dump.** Reframe must not load an ever-growing library into the left rail or into
   one prompt. Search returns compact, grounded candidate records; only the selected work's manifest and source are
   fetched. Candidate selection remains inspectable through title, author, edition, provenance, and stable AX state.

## The writer-facing grammar

The preferred grammar is natural language because the writer knows what she wants, not how the provider stores it:

> Find Freud's German Vorlesungen in the Book Library.

> Open Ulysses at Circe.

> Show me published works by Ovid.

> Find a German introduction to psychoanalysis by Freud.

> I want a short Greek tragedy about exile.

Structured commands may remain as deterministic accessibility and maintenance grammar, for example a catalog search
operation with an explicit result identity. They are projections of the same capability contract, not a second meaning
system. The Copilot's answer should return a short candidate card in plain language, with “Import” or “Choose” as the
action, never a raw ID as the headline. Search is on-device-first and does not require a paid lane merely because the
catalog is large.

## Acceptance

The landing/library change is not complete until all of the following are demonstrated:

- a fresh launch presents the intention-led landing and a truthful empty situation;
- the on-device Copilot retrieves the live Book Library catalog and can answer a title/author request without a paid
  lane;
- a semantic request by subject, language, period, form, or provenance returns grounded candidates without importing;
- a large-catalog request does not dump the catalog into the left rail or a single prompt;
- a catalog result exposes title, author, source, edition/status, and a stable AX identity, while the provider ID is
  available as inspectable detail rather than required writer input;
- an ambiguous request produces a clarification with distinct candidates;
- an unpublished Gutenberg work produces an honest unavailable/curation response and never auto-publishes;
- confirmation dispatches the existing import operation and persists the selected source and navigation metadata;
- AX inspection finds and operates the prompt, result cards, selection, import, cancel, retry, status, and failure
  controls without coordinates;
- VoiceOver/AX reads the current situation, result title, provenance, selection state, and action outcome in a useful
  order;
- rendered screenshots are reviewed at reading size in light, dark, Increase Contrast, and reduced-motion variants;
- the landing does not introduce a second app window, move the primary act off the external display, or resurrect
  retired uncertainty/structure panes;
- persisted FountainStore evidence proves the import and terminal outcome after relaunch; logs and screenshots alone
  do not count.

## Governing sentence

Reframe opens on the writer's intention, lets Copilot resolve that intention against live published source truth using
the lane that preserves conversational credibility, keeps provider IDs and lane machinery behind the dialogue, and
proves every state twice: semantically through AX and visibly through the rendered surface.
