# The Writer Does Not Manage the Projection

> Chapter summary: Reframe may hold more evidence than one view can show, but it must never make the writer manage the ledgers, provider lanes, consent, batches, or renderer limits that make the evidence possible.

## Purpose — the failure this exists to end

The writer comes to Reframe with manuscript questions. She should be able to ask what the reading established,
what changed between readings, what deserves attention, and whether an unanswered world question needs a reference.
She should not have to learn that `/world` is also a gazetteer reset, a research state machine, a provider switch,
or a queue maintenance tool.

The same leakage appears visually. An uncertainty score can contain many durable notes, lanes, and addresses. A
view that grows once for every note can push the rest of the workspace out of reach or destabilize the window. The
answer is not to throw away notes, hide them behind an unexplained cap, or ask the writer to close panels until the
application becomes usable. Evidence completeness and viewport completeness are different obligations.

This chapter binds the command grammar and the visual projection to one writer-facing rule: internal complexity is
contained by the application, while manuscript meaning remains visible, honest, and actionable.

## The decision — the writer navigates questions, not machinery

The writer's conceptual path is not a mandatory command pipeline. It is a set of neighboring questions:

```text
/readings   what changed between readings?
/ground     what should the next reading attend to?
/world      what has the manuscript established about its world?
/reference  what outside evidence could answer a world gap?
```

`/readings`, `/ground`, and `/world` are sibling manuscript-facing domains. A reading may reveal a world gap, and
that gap may offer `/reference`; the writer is never required to visit each command or understand the order of the
system's internal producers.

The namespace rule is therefore:

1. A public command names a writer problem, not an internal ledger or provider.
2. `/world` reports and revises what the manuscript has established. It does not expose research consent,
   provider widening, queue selection, or storage maintenance as primary concepts.
3. Outside investigation is a distinct reference act. Its card states the unresolved world question, the reason
   the manuscript cannot settle it, the proposed source, and the writer's available decision in plain language.
4. Internal transitions may retain deterministic slash aliases for compatibility, but the visible action is named
   by its manuscript consequence: retrieve this source, add this identity, leave it unresolved, or try a wider
   source.
5. A destructive command declares exactly the records it changes. If it changes several ledgers, it names them and
   leaves a durable receipt. If it changes one, its promise is narrow.

## The projection rule — complete evidence, bounded presentation

Every durable uncertainty note remains stored with its address, state, reason, provenance, and relevant evidence.
The view may show a slice, but a slice is a projection and must say that it is one.

1. **No evidence is discarded for visual fit.** Numeric limits may control a viewport, a page, or a materialized
   row set; they may not decide which semantic notes survive or which evidence is considered relevant.
2. **Every expanding surface has containment before it ships.** The surface uses a bounded viewport, scrolling,
   virtualization, paging, disclosure, or another explicit containment mechanism. A raw collection must never
   determine the height of the whole workspace.
3. **A bounded projection reports its extent.** The writer can tell how many notes exist, which portion is visible,
   and how to reach the rest. “More” is a navigable state, not silent omission.
4. **Selection is semantic and stable.** Paging, scrolling, filtering, or disclosure does not change the selected
   note's identity or move the writer to an unrelated item. The selected item opens its manuscript address and
   evidence.
5. **AX and sight agree.** The accessibility tree exposes the same count, states, selection, actions, and navigation
   that the visual surface claims. A screenshot cannot establish that hidden evidence is reachable, and an AX count
   cannot excuse a surface that is visually unusable.
6. **The default view triages attention.** It shows a compact account of where uncertainty is, what kind it is, and
   how much there is. Detail expands around the writer's selected question; the writer never has to tune the
   renderer to keep the manuscript workspace alive.
7. **A failure is not a quiet slice.** If the application cannot contain or expose the projection, it reports a
   visible failure and preserves the durable score. It must not present a partial result as the whole score.
8. **Projection and conversation share one state.** Changing the active work, section, reading phase, or Fountain
   document through Copilot updates the left projection and right-hand status as one typed transition. A screenshot
   showing two panes is not sufficient if AX or FountainStore identifies different active objects.

## The two-pane projection arrangement

The writer-facing window has two coordinated panes:

- **Left — projection:** the current source, publication/web page, publication-defined section, reading result,
  grounding/uncertainty view, or Fountain editor selected by Copilot.
- **Right — Copilot:** open-turn mediation, conversation, status, offers, confirmations, and composer.

The left pane is not a second command surface. Its visible selection, editing state, and evidence are projections of
the live state that Copilot has resolved. A left-pane control may support ordinary reading or text editing, but it must
not independently import, search the library, commit, publish, or choose a provider. Those intentions return through
the right pane so the same mediation, accounting, AX state, and persistence rules apply.

## The seam between manuscript and implementation

The application may need a ledger identity, a provider lane, an authorization state, a continuation token, or a
rendering window. Those are valid implementation facts. They become a governance defect when the writer must use
them to understand what the manuscript says or to keep the workspace operational.

The boundary is crossed when:

- `/world yes` or `/world no` requires the writer to remember which hidden transition is pending;
- `/world ask` silently means a positional subset of unresolved names;
- “widen” names a generic paid lane while the operation actually depends on one fixed provider;
- “clear world” promises to remove records that remain in another ledger;
- a dense uncertainty map forces the writer to close, mute, or manually paginate the rest of the application;
- `/readings` turns a difference into a claim about the work or the lens without evidence that can establish that
  cause.

The repair in each case is the same shape: state the manuscript question, expose the evidence that answers it,
offer only the writer's meaningful decision, and keep the implementation state behind the result.

## Acceptance

1. **Grammar seam.** A writer can move among `/readings`, `/ground`, `/world`, and an offered `/reference` act
   without being taught ledger names, provider names, or internal transition names. The same journey remains
   understandable when interrupted or resumed out of order.
2. **World/reference boundary.** A manuscript world report distinguishes what the text establishes from what an
   outside source may add. A reference offer carries its unresolved question, source, provenance, and promotion
   decision; retrieval is not silently treated as manuscript fact.
3. **Destructive scope.** A clear operation's persisted post-state matches its wording. The drive reads every
   affected document and its terminal receipt; no allegedly cleared unresolved or reference record remains hidden.
4. **Batch honesty.** Any bounded unresolved-name operation states its batch and continuation. A positional prefix is
   never presented as the complete queue, and no semantic batch is selected merely because it fits a number.
5. **Provider honesty.** A widening offer names the lane that will actually be used, its cost and consent state, and
   its refusal path. The capability, adapter, UI, telemetry, and persisted result agree.
6. **Dense score containment.** A fixture with many overlapping uncertainty notes leaves the window usable. The
   complete score remains durable; the visible projection reports total and current slice; selection remains stable;
   the full set is reachable through AX; and a containment failure is loud rather than silently partial.
7. **Manuscript return.** After inspecting uncertainty, the writer can open the relevant manuscript address and take
   a next action. The result does not require her to operate a renderer, ledger, or provider control surface.
8. **Evidence discipline.** A reading comparison may say that two readings differ, but when the evidence cannot
   establish whether the work or the lens caused the difference it says “I cannot tell” and offers a manuscript-facing
   next action.
9. **Two-pane agreement.** Live acceptance proves the left projection, right Copilot, AX tree, window-ID capture, and
   FountainStore identity agree; no retired Manuscripts rail, independent left command surface, or blank substitute
   pane is present.

## Governing sentence

Reframe shall contain its own ledgers, providers, consent, batches, and rendering detail so that the writer can
navigate manuscript questions and reach the complete durable evidence without managing the machinery that projects it.
