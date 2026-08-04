# Dynamic Grounding: From Default Reading to Writer-Accepted Lens

> Chapter summary: Grounding is not a workspace or a configuration panel. It is the living reading flow by which Reframe starts from a default non-integrational stance, observes what the first Storify reading leaves unresolved, and offers a writer-controlled change in lens.

## The decision

Grounding is a process, not a place.

Reframe begins a manuscript with a default non-integrational stance: the source remains authoritative, and the system does not silently reconcile, explain away, or merge tensions that the source has not resolved. The first Storify Source Auto pass is the first structural observation of that manuscript. It produces beats, questions, and an UncertaintyScore from the source and the confirmed Grounding policy.

After that reading, the UncertaintyScore may reveal a more useful way to attend to the manuscript. Reframe may propose a new grounding lens derived from the observed pattern. The proposal is a reading offer, not a hidden preference, a new baseline, or a manuscript edit.

The writer remains the authority for accepting the change. `/ground` is the explicit acceptance operation. When accepted, the new lens receives a new Grounding identity, invalidates the policy-dependent Storify results, and starts a new reading lineage. The source text and author baseline remain unchanged.

## Rules

1. **Grounding is a flow.** Do not present it as a standing workspace, editor, settings panel, or separate place the writer must visit. The user-facing vocabulary is Grounding, grounding lens, grounding proposal, and grounding change.
2. **The default stance is non-integrational.** Source contradictions, absences, and unresolved tensions remain visible. Grounding may change salience; it may not manufacture a resolution.
3. **Storify Source Auto is the first observation.** Dynamic grounding begins from the first source reading and its persisted UncertaintyScore. It must not depend on a retired index, semantic-memory shortcut, or an unobserved chat impression.
4. **The score may produce a proposal, not an automatic mutation.** A score-derived lens is an offer until the writer explicitly accepts it. Proposal text must identify the observed uncertainty and state that the author baseline is unchanged.
5. **`/ground` is the acceptance boundary.** The operation must be bound to the active reading run, the proposed lens, and the confirmed Grounding identity from which the proposal was derived. A stale, missing, or mismatched proposal fails visibly.
6. **A grounding change creates a new lineage.** The new identity must be persisted before downstream work is presented as current. Policy-dependent beats, kept/noise decisions, summaries, synopsis, and arcs become stale or are restarted according to the runtime contract.
7. **Grounding never edits the manuscript.** It changes the policy of attention, not the canonical source, author baseline, or writer-authored draft. Source evidence remains the authority for facts.
8. **The transition is inspectable.** Copilot text, AX state, the UncertaintyScore/lane projection, and FountainStore lifecycle/effect documents must agree about the proposal, acceptance, previous identity, new identity, and restart/invalidation effect.
9. **Grounding remains local by default.** A grounding proposal and acceptance run on the on-device lane unless the writer explicitly widens the lane under the provider governance chapters.
10. **The old static metaphor is retired.** No help item, alias, command catalogue entry, generated manifest, or AX label may describe Grounding as a legacy product workspace. Internal migration identifiers may remain only where they cannot reach writer-facing output.

## The live sequence

```text
canonical source
  → default non-integrational reading
  → first Storify Source Auto
  → persisted UncertaintyScore and dynamic lanes
  → proposed grounding lens
  → writer accepts / rejects
  → new Grounding identity if accepted
  → Storify re-forms its policy-dependent reading
```

The sequence is consequential. A successful command is not proved by the words “grounded” or “reading again.” Acceptance requires the AX-visible result, the changed reading projection, and persisted FountainStore evidence.

## The governing sentence

Grounding is Reframe’s living, source-authoritative flow of attention: the UncertaintyScore may propose how the reading should change, but only the writer may accept that change, and every accepted lens must leave a persisted, inspectable lineage.

## Acceptance

A revised grounding flow is accepted only when a fresh owned-source drive proves all of the following:

- the first Storify reading exposes the UncertaintyScore and its lanes;
- the default non-integrational stance remains visible in the absence of a proposal;
- the proposal is derived from the observed score and does not mutate the baseline;
- `/ground` is blocked without the proposal-bound acceptance state;
- accepted `/ground` persists a new identity and requests the downstream restart;
- the before/after score or lane projection is captured by window ID and readable in the AX tree;
- FountainStore lifecycle and effect documents show the accepted terminal result;
- no retired static Grounding label appears in the transcript, help, AX tree, or generated capability projection.

The Book may describe this as a live-accepted development command only after those authorities agree. It must not imply that the command belongs to a named released App build unless the release manifest says so.
