# One Reasoning — The Single Front Door of a Turn

> Chapter summary: A turn is understood by **one** reasoning, over **one** complete taxonomy of what the writer can
> want, and **everything routes from that single decision**. There is no speculative "fast" pre-classifier with its
> own smaller vocabulary that fires first and can grab a turn before the real reasoning runs; there is no cascade of
> independent `reflect*` passes each re-asking a slice of the same question and racing to be first. Multiple
> reasoners with divergent vocabularies **disagree**, and whichever grabs the turn first wins — which is how a
> content question became a segmentation, "fix it" became a whole read, and "stay on device" (turning the writer's
> key, [ch.20](20-on-device-first-and-the-writers-key.md)) became a segmentation. One reasoning, the right one, over
> the whole space of intents; route from it.

## Purpose — the failure this exists to end

A single manuscript turn was being decided by **five** separate model-reasoned passes, in order, first-to-grab
wins:

1. `fastTurnDecision` — a one-shot "fast" reasoner over `FastRouteTargetG` (9 cases: answerQuestion, segmentBeats,
   groundInputsOrGuide, …).
2. `reflectWriterAsksAboutStoryContent` — a separate reflection.
3. `reflectWriterWantsToReviewBeats` — another reflection.
4. the staged intent-mediation classifier over `StudioReasoningIntentCategory` (12 cases) — the *complete* one,
   where speech-act, disposition, and (per [ch.20](20-on-device-first-and-the-writers-key.md)) the writer's-key
   `cloudGrant` recognition live.
5. `reflectWriterIntendsToActOnNextStep` — yet another reflection.

The taxonomies **differ** (`FastRouteTargetG` has no `cloudGrant`, no notion of a key-turn; the reflections each
model a single yes/no), and the earliest pass to claim the turn decides it. So:

- **"Stay on device — don't spend my cloud account"** (the writer turning their key) reached pass 1, which has no
  key-turn in its vocabulary, mapped it to `segmentBeats`, and ran a manuscript read. The complete classifier in
  pass 4 — which *does* recognize a `cloudGrant` — was never reached.
- The same mechanism sent content questions ("what is the through-line?") and referent-less commands ("fix it") to
  a read: a fast reasoner with a coarse vocabulary guessed an action, and the turn never reached the reasoning that
  would have understood it.

The defect is not any one pass being wrong. It is that **there are several**, with different vocabularies, in a
race. A turn's meaning cannot be decided twice; a second reasoner with a smaller taxonomy is not an optimization,
it is a source of disagreement that silently overrides the right answer.

## The principle — one reasoning, complete, and everything routes from it

A turn has one meaning. It is reasoned **once**, over **one taxonomy that spans everything the writer can want** —
to be answered, to have an operation performed, to turn the writer's key, to be asked a clarifying question, to
just converse. That single decision is what the rest of the turn routes from. There is no faster, smaller reasoner
in front of it, because a smaller vocabulary can only be *wrong more often* about the cases it does not contain,
and being first lets it impose that wrongness. Reasoning is where correctness lives; duplicating it fractures the
correctness.

## The decision (enforceable rules)

1. **One reasoning boundary per turn.** A turn is classified once, by one model-reasoned decision, before it is
   routed. No second classifier runs ahead of it, beside it, or after it to re-decide the same question. The
   `fastTurnDecision` / `FastRouteTargetG` pre-pass and the standalone `reflect*` re-classifications are retired
   into this one decision.

2. **One complete taxonomy.** The single decision reasons over a taxonomy that covers **every** thing a writer can
   want in a turn — including answering, each real operation, turning the writer's key (`cloudGrant`), clarifying,
   and conversing. There is no case a turn can fall into that this taxonomy cannot name, and therefore no need for
   a second vocabulary to "catch" anything. A missing case is a gap in the one taxonomy, closed there — never a
   reason to add a competing reasoner.

3. **Everything routes from that one decision.** Answering, performing an operation, turning the key, opening a
   reader, clarifying — all are dispatched from the single classification result. Routing is deterministic code
   over that result; it never re-reasons. ([Reason, don't keyword-match] governs the *classification*; routing
   *from* it is plain dispatch, not a second interpretation.)

4. **No speculative shortcut may pre-empt the reasoning.** A performance shortcut that answers before the one
   reasoning has run is forbidden when it can decide the turn. If the single reasoning is too expensive, make *it*
   cheaper (fewer tokens, a leaner manifest — the on-device window work); do not bolt a coarse guesser in front of
   it. Speed is not worth a wrong front door. (This is the turn-level twin of [ch.22](22-no-preferences-only-reasoning.md):
   there, no stored toggle stands in for a decision; here, no fast pre-guess stands in for the reasoning.)

5. **Reason over meaning, once.** The one decision is made by the model reasoning over the writer's meaning against
   the complete taxonomy — never by keyword or verb matching, and never by a chain of narrow yes/no reflections
   that each re-read the turn. If a distinction matters (act vs. ask, grant vs. revoke, answer vs. perform), it is
   a facet the one reasoning returns, not another reasoner.

6. **The reasoning is inspectable.** The single decision — the chosen intent, its confidence, and the facets that
   route it — is legible (loggable, testable) so a turn's routing can always be explained by "the one reasoning
   decided X," never by "whichever pass grabbed it." One decision to point at, not five to reconstruct.

## Honesty (non-goals)

- **This is not "always run the heaviest pipeline."** One reasoning can be one cheap call; the point is that it is
  *one*, and *complete*, not that it is large. Cost is addressed by making the single reasoning lean, not by
  fronting it with a lossy guesser.
- **This is not banning cheap preconditions.** A non-reasoning, deterministic guard ("there are no beats, so the
  beat-reader cannot open") is fine and encouraged — it is not a *reasoning* pass and cannot misclassify meaning.
  What is banned is a second *model reasoning* over the turn's intent with a different vocabulary.
- **This is not forbidding facets.** The one decision may carry many fields (speech act, disposition, key
  direction/scope, target operation). Those are outputs of the single reasoning, not separate reasoners.
- **This is not a rewrite of what the operations are.** The capabilities are unchanged; only the number of places
  that decide *which* capability a turn wants collapses to one.

## Relationship to other chapters

- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — the `cloudGrant`
  key-turn is recognized only because it is a case in the one taxonomy every turn flows through; the fast pre-pass
  is exactly what hid it. This chapter is what makes ch.20's dialogue recognition reachable.
- **[No Preferences, Only Reasoning](22-no-preferences-only-reasoning.md)** — the sibling law: there, no stored
  toggle substitutes for a decision; here, no speculative fast pass substitutes for the reasoning. Both say: the
  app decides by reasoning, in one place, over meaning.
- **[The situated Copilot](15-the-situated-copilot.md)** — the one reasoning is the Copilot's understanding of the
  turn; its result is what she acts or speaks from.
- **Feedback doctrine** — [reason, don't keyword-match] (the one decision is reasoned over meaning),
  [ground claims in the store] and the self-reflection work (reflection informs the *one* decision, it is not a
  second router), [no-determinism-gates] (a fast pre-classifier is a gate that pre-empts reasoning).

## Acceptance

The doctrine is met when:

1. **A manuscript turn is classified exactly once** before routing — one model-reasoned decision, no fast
   pre-classifier and no standalone `reflect*` re-classification racing it.
2. **The one taxonomy is complete** — every routable outcome (answer, each operation, `cloudGrant`, clarify,
   converse) is a case in it; there is no second vocabulary anywhere in the turn path.
3. **"Stay on device" turns the writer's key** (and "use the cloud for this" grants it) because the key-turn is a
   case in the one taxonomy the turn flows through — verified live, not only unit-tested.
4. **A content question is answered and a referent-less command is clarified** — because the one reasoning sees the
   whole space and is not pre-empted by a coarse guesser mapping them to an action.
5. **Routing is deterministic dispatch over the single decision** — no code path re-reasons the turn's intent after
   it is classified.
6. **The decision is inspectable** — a turn's route can be explained by the one reasoning's logged result.
