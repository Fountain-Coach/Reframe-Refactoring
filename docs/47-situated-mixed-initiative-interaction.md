# Situated, Mixed-Initiative Interaction

> Chapter summary: Reframe is an open interaction space, not a finite dialogue script. A human may arrive early,
> late, sideways, interrupted, corrective, or with an unrelated question. The Copilot must understand each turn
> against the live application situation and the current governed exchange, then preserve state authority when the
> expected next turn does not arrive.

## The decision

Reframe treats conversation as situated, mixed-initiative interaction.

The human is not a test harness moving through a prescribed sequence. Reframe may offer a next step, but the writer
may accept it, correct it, ask about it, interrupt it, change the subject, or return to it after another turn. A turn
has meaning only in relation to the live application situation, the persisted records that make that situation true,
and the writer's current meaning. The transcript is a record of the exchange, not the authority for project state.

This is an open interaction space: the set of possible human turns cannot be reduced to the vocabulary of the last
assistant sentence or to a finite list of expected replies. Reframe must remain safe and useful when the human does
not follow the anticipated adjacency pair.

## Rules

1. **The situation comes first.** Before a turn can mutate anything, Reframe reads the current application and
   FountainStore state that governs the possible action: active manuscript, arrangement, selected objects, pending
   proposal, run, identity, and lifecycle. A missing situation is an honest absence, not an invitation to invent one.

2. **The human may take the initiative.** A writer may answer an offer, correct it, ask a side question, interrupt a
   running task, return to an earlier proposal, or say something unrelated. The mediator must classify the meaning of
   that turn in its current situation; it may not assume that every turn answers the last assistant sentence.

3. **Expected replies are not grammars.** “Yes”, “no”, “that is wrong”, “do it”, or any other wording has no fixed
   operational meaning outside the persisted situation and the writer's grounded meaning. A response to `/ground`
   is a Grounding decision only after a proposal-bound pending state exists; the same words after a greeting remain
   conversation or require clarification.

4. **One turn, one reasoning boundary.** Freeform meaning passes through the single complete mediation decision of
   chapter 23. State gates may make an operation ineligible or require clarification, but no phrase list, regex,
   response-position rule, or second intent classifier may decide what the writer meant.

5. **Offers are reversible until accepted.** An assistant proposal is not an instruction, confirmation, or mutation.
   A writer's correction produces a restatement or replacement offer; a decline leaves the governed artifact unchanged;
   an explicit agreement is the only path to the proposal's executor. The response must be persisted before any result
   is presented as complete.

6. **Repair is a first-class outcome.** When a turn is thin, ambiguous, out of sequence, stale, or unrelated to a
   pending operation, Reframe asks or answers without mutating the pending artifact. It must distinguish a missing
   situation, an uncertain meaning, a provider failure, and a rejected operation rather than collapsing them into a
   generic success or routing them to an unrelated capability.

7. **Interruption does not erase state.** A side question, relaunch, process restart, or temporary provider failure
   does not turn a persisted proposal or running operation into transcript-only state. On return, Reframe rehydrates
   the current record, states what is pending, and lets the writer continue, replace, decline, or abandon it by a new
   mediated turn.

8. **Context is selected by semantic relevance.** The front door retrieves the smallest context that explains the
   current situation and turn. It does not assemble the full transcript, manifest, toolset, or runtime state by
   default, and it never drops semantic material by position, byte count, or token fit. If relevant context cannot be
   selected safely, Reframe retrieves more targeted state, asks, or fails visibly.

9. **The human remains the mutation authority.** Situated perception is not consent, an offer is not acceptance, and
   a successful model response is not persisted behaviour. Grounding, source, draft, provider, cost, and other
   governed state change only through their existing confirmation, executor, persistence, and telemetry contracts.

10. **Every consequential path is observable.** AX exposes the current situation, proposal, pending/working/failed
    state, available actions, and terminal result. FountainStore records the behavioural transition and identity.
    Window-ID capture establishes visual truth. Logs explain the decision but never prove that it happened.

## The interaction states

```text
live situation
  → writer turn (expected, corrective, interrupting, or unrelated)
  → one mediated meaning + uncertainty map
  → answer / clarify / offer / execute / decline / resume / fail visibly
  → persisted result or unchanged pending state
```

The arrows are not a script. Any writer turn may arrive at any point. The invariant is that Reframe must not advance
the governed state merely because the turn resembles an expected next sentence.

## Non-goals

- This chapter does not create a second conversation engine, a persona per surface, or a transcript-backed project
  state store.
- It does not require Reframe to answer every turn without clarification; honest clarification and visible failure are
  successful outcomes when the situation or meaning is insufficient.
- It does not make every interruption cancel work. Cancellation, resume, and abandonment remain capability-specific
  policies, but they must be visible and persisted where governed.
- It does not permit arbitrary model autonomy. Mixed initiative widens the possible human turns; it does not widen
  mutation authority.

## Relationship to other chapters

- **[The situated Copilot](15-the-situated-copilot.md)** defines where the Copilot is and what that arrangement shows;
  this chapter defines how she behaves when the human does not follow a scripted exchange there.
- **[One Reasoning](23-one-reasoning.md)** supplies the single mediation boundary and forbids competing phrase or
  reflection classifiers.
- **[The Reasoning Is an Uncertainty Map](24-the-reasoning-is-an-uncertainty-map.md)** supplies settled,
  ambiguity, thin, and failure outcomes for open turns.
- **[Dynamic Grounding](46-dynamic-grounding.md)** supplies the concrete proposal/acceptance boundary: `/ground`
  becomes meaningful only when its persisted proposal situation exists, and only acceptance creates a new lineage.
- **[Validation and acceptance](08-validation-and-acceptance.md)** supplies AX, FountainStore, window-ID, and
  three-repetition evidence; this chapter expands the scenarios that must be repeated.

## The governing sentence

Reframe is a situated, mixed-initiative interaction space: the human may take the conversation anywhere, but only
grounded live state and one mediated meaning may authorize a persisted transition.

## Acceptance

The doctrine is met when a clean-store drive proves, through AX and FountainStore, that:

1. a greeting before `/ground` does not create a Grounding response state;
2. `/ground` creates a persisted proposal before any acceptance, decline, or correction is interpreted;
3. the same correction is safe with and without an explicit “no” and does not reach answer, citation, or unrelated
   capability routes;
4. a side question, interruption, relaunch, stale proposal, and provider failure leave the pending artifact unchanged
   or produce the governed visible failure;
5. a replacement is restated and persisted as a new offer without changing confirmed Grounding;
6. only a later explicit agreement changes Grounding identity and starts the downstream reading lineage;
7. three repetitions of the consequential transitions agree across AX semantics, window-ID capture, and FountainStore;
8. no acceptance claim depends on exact assistant wording, a phrase list, transcript reconstruction, or logs alone.

The Book may describe this as a development governance contract only after these authorities agree. It must not imply
that the interaction space is a named released App capability without the release manifest and live evidence.
