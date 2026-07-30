# The Reasoning Is an Uncertainty Map

> Chapter summary: The product of the one reasoning ([ch.23](23-one-reasoning.md)) is not an opaque verdict — it is
> a small **uncertainty map** over what the writer could want: which readings are live, how sure the model is of
> each, and what would resolve the doubt. The app acts *from that map*. A confident (`settled`) reading dispatches;
> a genuinely torn (`ambiguity`) reading asks; an under-supported (`thin`) reading may offer to widen; a broken
> (`failure`) reading — including a turn that overflowed the window — is surfaced loud, never laundered into a calm
> answer. This is what lets the reasoning run **lean** ([ch.23](23-one-reasoning.md) rule 4): an unburdened first
> pass can honestly report what it does and does not know, which a clamped one cannot. The map is the shared
> substrate of three things at once — routing, escalation ([ch.20](20-on-device-first-and-the-writers-key.md), the
> writer's key), and transparency — expressed as [UncertaintyScoreKit](https://github.com/Fountain-Coach/UncertaintyScoreKit)
> and made inspectable (FCIS-AX), so the writer decides on real evidence.

## Purpose — the failure this exists to end

The one reasoning currently returns a target plus a scalar `confidence: "low|medium|high"` — an opaque guess. Two
failures follow:

- **It cannot be lean.** To answer inside the same call it hauls in the capability manifest, evidence, and view
  semantics — ~3,800 tokens — and on the on-device 4k window it *overflows* ("no room for output"). Forced into a
  smaller box, it emits a clamped guess or a breakdown. The very act of cramming destroys the reasoning's ability
  to report its own uncertainty.
- **It hides what it does not know.** A turn like "stay on device" that is genuinely between *turn the key* and
  *chat* is flattened to one guess with a confidence label; when the guess is wrong it silently misroutes (a
  content question becomes a segmentation). There is no honest signal "I am torn, and here is why" — so nothing can
  clarify, offer to widen, or be shown to the writer.

UncertaintyScoreKit already states the principle for the manuscript read: *a first pass is far more reliable at
reporting what it does and does not know than at producing settled answers; the deliverable is a multi-dimensional
map of uncertainty, not a confident index.* The same is true of reasoning about a **turn**. This chapter makes the
one reasoning's product that map.

## The principle — reason once, and the product is a map of doubt

The one reasoning's job is *"what does the writer want."* Its honest output is not a single answer but a small
**uncertainty map** over the intent taxonomy: for the live candidate intents, how settled or open each is, why, and
what would close the doubt. The app then acts *from the map* by deterministic dispatch. Because the map — not an
inline answer — is all the reasoning must produce, the call is lean by construction: it needs the writer's message,
the small taxonomy, and minimal situational state, never the execution manifest. Room to reason is what makes an
honest map possible; an honest map is what makes lean reasoning safe.

## The decision (enforceable rules)

1. **The one reasoning emits an uncertainty map, not a scalar confidence.** Its result is an `UncertaintyScore`
   over the intent taxonomy: each live candidate intent carries a state — `settled` / `ambiguity` / `thin` /
   `failure` — a short reason, and, where useful, `resolvedBy` (what would close it). A bare "confidence:
   low|medium|high" is retired.

2. **The states mean exactly what UncertaintyScoreKit says, and route accordingly.**
   - **`settled`** — one intent clearly wins → dispatch it (deterministic, [ch.23](23-one-reasoning.md) rule 3).
   - **`ambiguity`** — the message genuinely supports more than one intent → **ask** (this is ch.23's *clarify*):
     name the readings and let the writer choose. Never silently pick one.
   - **`thin`** — a leaning but under-supported reading → proceed with it, and it is a candidate for a widening
     offer (rule 4).
   - **`failure`** — the reasoning broke down (could not classify, or **overflowed the window**) → surface it
     **loud** and honest ("I couldn't read your turn"), never dispatch a guess and never launder it into a calm
     answer. A window overflow is a failure-axis note, not a segmentation.

3. **Ambiguity is a result; failure is a breakdown — keep them different.** `ambiguity` (the turn honestly supports
   two intents) and `failure` (the reasoning could not run) are different in kind and are rendered and routed
   differently. Never present a `failure` as a mild open question, and never treat a real `ambiguity` as an error.
   (This is UncertaintyScoreKit's founding line, applied to turn reasoning.)

4. **Because the product is a map, the reasoning is lean by construction.** The classification loads only the
   taxonomy + the writer's message + minimal state. The capability manifest, evidence, and view semantics are
   **execution** context, loaded only by the producer the map dispatches to, only when needed — never injected into
   the classification. Leanness is achieved by removing burden at its source (ch.23 rule 4), not by clamping
   evidence to fit.

5. **The map drives escalation — the writer's key reads it.** The widening-to-cloud decision
   ([ch.20](20-on-device-first-and-the-writers-key.md)) is reasoned over this uncertainty. A `settled` local
   reading stays local; a `thin`/`failure` reading whose `resolvedBy` is "a stronger model" is what may make the
   Copilot **offer** to widen — the writer's key still decides. The classification's uncertainty is the first place
   that escalation signal exists.

6. **The map is transparent — inspectable and showable.** The uncertainty map is machine-readable (FCIS-AX) and
   the Copilot can **show it on request** (the UncertaintyScoreKit surface) and state it in words ("most likely X,
   but possibly Y, because …"). The writer holds the key over *real evidence*, not a hidden guess. A route is
   always explainable by "the one reasoning read the turn as this map," never "a pass grabbed it."

## Honesty (non-goals)

- **This is not a probability theatre.** The map is the model's honest reading, in the four named states, with
  reasons — not a fabricated numeric distribution. `magnitude` exists but the states carry the meaning.
- **This is not "always ask."** `ambiguity` is for a genuine two-way split, not for every turn; a `settled` read is
  acted on without a clarifying question. Over-asking is its own failure.
- **This is not a second reasoner.** The map is the *output* of the one reasoning ([ch.23](23-one-reasoning.md)),
  not another pass. Routing, escalation, and display all read the *same* map.
- **This does not push execution context into the map.** Producers still load what they need at execution; the map
  stays lean. The map says *what* the writer wants and how sure; it does not carry *how* to do it.

## Relationship to other chapters

- **[One Reasoning](23-one-reasoning.md)** — this chapter says what that one reasoning *produces*: an uncertainty
  map, which is also why it can be lean (rule 4 realized).
- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — the map is the
  uncertainty the escalation offer is reasoned over; the writer's key decides on it.
- **UncertaintyScoreKit** — the reasoning's product is expressed in its model (`UncertaintyState`,
  `UncertaintyNote.resolvedBy`, `UncertaintyLane`, `UncertaintyScore`); it must be FCIS-AX so the map is inspectable
  and showable (rule 6).
- **[A Want Is a Gap in a Ledger](33-a-want-is-a-gap-in-a-ledger.md)** — this chapter maps a *turn*; that one maps
  the *world*, and says where its marks come from: collected from the ledgers the work keeps, never from an
  enumerated list of axes. It also types what this chapter left as prose — `resolvedBy` becomes a **want**, named
  by who can answer it, which is how rule 5's escalation reaches [ch.32](32-referenced-knowledge.md)'s reference
  lane and not only ch.20's stronger model.
- **[First read's product is uncertainty]** (the manuscript-read doctrine) — the same principle for reading a
  manuscript, now applied to reading a *turn*: the honest first-pass deliverable is a map of doubt, not a confident
  verdict.
- **Feedback doctrine** — [no deterministic fallbacks] (a `failure` fails visibly, never a canned guess),
  [reason, don't keyword-match] (the map is reasoned over meaning), [ground claims in the store] (the map is
  evidence, not decoration).

## Acceptance

The doctrine is met when:

1. **The one reasoning returns an uncertainty map** over the intent taxonomy (per-intent state + reason +
   `resolvedBy`), not a scalar confidence.
2. **Routing follows the states** — `settled`→dispatch, `ambiguity`→clarify, `thin`→proceed/offer,
   `failure`→fail visibly — verified on real turns, including that a window overflow renders as a loud failure, not
   a segmentation.
3. **The classification call is lean** — taxonomy + message + minimal state only; no capability manifest, evidence,
   or view-semantics injected into it; execution context loads in the dispatched producer.
4. **A genuinely ambiguous turn asks** rather than guessing, and a `settled` turn acts without asking.
5. **The escalation offer is reasoned over the map** — a `thin`/`failure` reading whose resolution is a stronger
   model is what surfaces a widening offer; the writer's key decides.
6. **The map is inspectable and showable** — machine-readable (FCIS-AX), stateable in words, and viewable via the
   UncertaintyScoreKit surface on request; every route is explainable by the one map.
