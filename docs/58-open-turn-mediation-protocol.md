# Open-Turn Mediation Protocol

> Chapter summary: Reframe is entered through an open interaction, not a scripted command sequence. The Copilot
> receives noisy, incomplete, corrective, interrupted, or changing turns and settles each one against the live
> situation before any capability or provider route may act.

This protocol generalizes first contact. The empty landing is its first case, but the same boundary applies whenever
the writer interrupts, changes direction, says something nonsensical, corrects Reframe, or returns to an earlier task.
It extends chapters 15, 23, 24, 47, 51, and 57. It does not create a second workflow engine: it mediates meaning and
hands a settled request to an existing governed capability.

## The decision

1. **Every freeform turn crosses one open-turn boundary.** No manuscript, launcher, cloud-key, provider, or execution
   classifier may consume the turn before mediation has read the live situation and decided what the writer is doing.
2. **The situation is the first fact.** The mediator reads the current arrangement, open manuscript or empty state,
   available catalog, pending offer, running work, selected objects, provider authority, and relevant persisted
   identity. It never reconstructs state from transcript wording.
3. **Noise is not failure.** Provocation, absurdity, an off-topic remark, or a thin turn receives a coherent response
   or clarification. It does not accidentally become a cloud instruction, manuscript mutation, or unrelated action.
4. **A change of mind is authoritative.** “I know better now” replaces the writer's current intention for the new
   turn. A previous offer remains unchanged unless the writer explicitly accepts, replaces, abandons, or cancels it
   under that capability's policy.
5. **Retired vocabulary is translated, not obeyed literally.** A request such as “open Circe from Ulysses” carries a
   work reference and provenance context. The mediator resolves the work against the current Book Library, explains
   the current source boundary, and never routes the writer into a retired or direct-upstream implementation.
6. **Discovery precedes identity.** The writer addresses a work by meaning. The mediator retrieves the current
   catalog, presents the human distinction when several entries match, and keeps provider IDs behind the dialogue.
7. **No guessing across ambiguity.** One match may proceed to the existing importer. Several matches require a short
   clarification. No match produces an honest availability explanation and a bounded next action.
8. **The writer's lane authority is separate.** A source request is never a cloud-spend instruction merely because it
   mentions a provider, an old source, or a model. Cloud authority changes only through an explicit mediated key turn.
9. **The protocol preserves agency without losing coherence.** A side question may be answered and the active offer
   parked; a correction may replace it; a return may resume it. The Copilot does not force the writer through a lesson
   plan or demand command vocabulary.
10. **Handoff is explicit and typed.** The mediator returns one of: answer, clarify, offer, execute, decline, resume,
    or visible failure, with the grounded capability and target when execution is authorized. Existing executors own
    mutation, confirmation, persistence, cancellation, and terminal proof.
11. **The protocol is observable.** AX exposes the current situation, mediator state, question or offer, available
    choices, progress, and result. FountainStore records consequential transitions; screenshots establish rendered
    truth; logs remain telemetry.
12. **Mediation owns the split.** The right Copilot pane receives and settles the turn; the left pane shows the
    resulting projection. A turn that asks to open, read, research, ground, structure, compose, or export changes the
    left projection only through this mediated handoff. The projection never becomes a competing interpreter.

## The open-turn shape

```text
live situation
  → writer turn
  → one mediated meaning and uncertainty state
  → answer / clarify / offer / execute / decline / resume / fail
  → persisted result or unchanged pending state
```

This is a semantic boundary, not a phrase grammar. Meaning must come from grounded reasoning. Deterministic parsing
remains permissible for slash commands, stable IDs, and explicit accessibility selections only.

## First-contact behavior

When the workspace is empty, the mediator explains the available beginning in plain language and does not report
internal lanes, account state, or implementation history unless the writer asks. For a noisy first turn it settles the
likely task and the available route in one sentence before acting:

> “I understand that you want Joyce’s *Circe*. ‘Ulysses’ is the historical source reference; I’ll look for the
> published work in the Book Library.”

If the live catalog returns one entry, the existing Book Library import proceeds. If it returns several, the Copilot
asks which edition matters. If it returns none, she says that the current catalog did not resolve the request and
offers a bounded next step: refine the library search or explicitly ask for a research/citation lookup. She never
offers direct DraCor, web, or local-file reading, fabricates a provider ID, or silently publishes arbitrary source
material.

## Boundaries with neighboring commands

- `/ground`, `/readings`, `/world`, and `/research` remain capability grammars after mediation has established their
  target and scope; the protocol does not absorb their semantics. `/world` and `/research` may request bounded
  gazetteer/reference evidence, but they may not open generic web pages or turn evidence into a reading source.
- The launcher, manuscript planner, and cloud-key authority remain executors or specialized decision authorities;
  they do not compete to interpret the initial freeform turn.
- The transcript is conversational evidence, not project-state authority. Situation, pending offers, source identity,
  and terminal outcomes come from live state and FountainStore.

## Acceptance

The protocol is complete only when a clean-store drive demonstrates, through AX, window-ID capture, and FountainStore:

- an empty landing mediates “open Circe from Ulysses” toward the current Book Library rather than answering with lane
  or cloud-key copy;
- a single catalog match dispatches the existing importer and persists the selected source;
- multiple matches clarify without guessing, and no match explains the available next step;
- an interruption, nonsense turn, correction, and spontaneous change of mind do not mutate the prior offer silently;
- a parked task can be resumed after an unrelated turn and after relaunch;
- a request naming an old provider never invokes its retired implementation or direct-upstream reading path;
- an arbitrary URL is declined as a reading source, while an explicit research/citation request yields only bounded,
  provenance-bearing evidence;
- the same source request never changes cloud authority;
- AX exposes the mediator situation, result identity, import action, status, clarification, cancellation, and failure;
- the two-pane surface shows the mediated projection on the left and the same active situation, status, and next
  action in the right Copilot pane, with no independent left command authority;
- three consequential repetitions agree across AX semantics, rendered window-ID evidence, and persisted store records.

## Governing sentence

The Open-Turn Mediation Protocol lets the writer arrive, interrupt, wander, correct, or change her mind while one
grounded Copilot settles the current intention and hands it to the existing capability that can honestly do it.
