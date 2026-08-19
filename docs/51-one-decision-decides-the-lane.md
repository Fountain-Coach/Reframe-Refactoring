# 51. One Decision Decides the Lane

> Chapter summary: "Which lane serves this?" is answered in four places in this app, and on 2026-08-07 all four
> disagreed about a single page: the election said `codex`, the window budget said 30,000 tokens, the read-lane
> log said `openai`, and the call landed on **Apple Foundation Models, which refused 25,025 tokens into a
> 4,096-token window**. Nobody was lying; nobody was asking the same question. So a lane is **resolved once, into
> a value**, and the **budget is a property of that value** — obtaining a client and obtaining the window it must
> fit are the same act, which makes the overflow above unrepresentable rather than merely fixed. Resolution is a
> pipeline of ordered gates — configured, permitted, credentialed, constructible, healthy — each of which may only
> NARROW, and each refusal is typed and carries its reason. A credential has four states, not two: absent,
> present-but-unverified, authorised, refused; **paid availability is the default election for writer-facing work**,
> while an explicit local-only instruction remains authoritative; presence never elects a lane, and naming a lane
> must never read a secret. Every surface prints the one recorded decision
> instead of re-deriving it. The resolver is pure — configuration, consent, credential state, health, clock in; a
> resolution out — so its small finite state space is tested exhaustively rather than by example, and it lives in
> a kit of its own.

## Purpose — the failure this exists to end

Measured 2026-08-07, on one page of one chapter, from one run:

```
[LANES]     semantic → codex — your ChatGPT plan is ready (team plan, 3% left)
[WINDOW]    grew 8 → 62 atoms (budget 30000 tokens, ours 2453)
[READ-LANE] reading on openai
actual:     Apple Foundation Models primary call failed —
            generable prompt input does not fit the context window (input 25025 of 4096 tokens)
```

Four subsystems, four answers, one act. `ReframeLaneAvailability` elected a lane; `semanticPrimaryRoute` built a
client by its own candidate order and fell through to Apple when a cloud client could not be constructed;
`storifyElectedSemanticProvider` sized the window from the election; a fourth logger reported something else
again. The window was sized for a lane with 30,000 tokens of headroom and the call executed against 4,096.

The same disagreement produced the rest of the day:

- **Presence was used where authorisation was meant.** `hasOpenAIAPIKey` answers an attributes-only Keychain
  question — *is there an item* — and it was read as *can this lane run*. A key existed, the client could not be
  built, and the read fell silently to the on-device lane while three surfaces still said cloud.
- **Naming a lane read a secret.** The Copilot's opening sentence wanted `route.provider` — a noun — and a route
  carries a client, so composing "I run on your ChatGPT plan" put a `SecurityAgent` password dialog in front of
  the manuscript. The app asked for the writer's password in order to write a sentence.
- **A failure taught the wrong thing.** A per-window TIMEOUT was recorded as `minOverflowTokens`, a statement
  about how much the lane can HOLD. A latency problem became a permanent size ceiling: 30,000 → 21,929 → 14,627,
  each retry ratcheting the next run smaller. An earlier turn of the same ratchet had left `2190` — an Apple
  on-device figure recorded against OpenAI — which capped every paid call at 261 tokens of manuscript and turned
  one chapter into ~1,470 calls.

None of these is a coding slip. They are all the same structural fault: **the question is asked repeatedly, by
parties who cannot see each other's answers.**

## The rules

1. **A lane is RESOLVED ONCE, into a value.** For a given role (semantic, planner, writer) at a given moment
   there is exactly one resolution. It is computed by one resolver and passed to everyone who needs it. No
   component may re-derive it, and "ask again later" is re-deriving.

2. **The budget is a property of the decision, not a lookup.** A decision carries the client AND the context
   window, output reserve and payload budget that client actually has. Obtaining one without the other is not an
   available operation. This is the rule that makes 25,025-into-4,096 unrepresentable rather than fixed.

3. **A refusal is a value with a reason, never a nil.** `nil` composes into a silent fallback — which is exactly
   how a failed cloud construction became an on-device read that nothing reported. A refusal names the role, the
   gate that refused, and what the writer could do about it.

4. **Gates are ordered and may only NARROW.** `configured → permitted → credentialed → constructible → healthy`.
   No stage may add a candidate a previous stage excluded. A lane already proven impossible — 401, 429, declined
   consent — cannot re-enter later in the pipeline.

5. **A credential has four states.** `absent`, `presentUnverified` (attributes only — no unlock, no prompt),
   `authorised` (the data was read), `refused` (the writer or the Keychain said no). Any code that treats this as
   a boolean is wrong by construction.

6. **Paid availability elects the paid lane by default.** For writer-facing work, a configured, credentialed,
   constructible and healthy paid lane is selected without requiring exact consent wording. An explicit local-only
   instruction is the only route override. `presentUnverified` may not elect a lane; it remains an unavailable gate.

7. **Naming a lane must not read a secret.** Any surface that states which lane will answer resolves the NAME
   through a path that unlocks nothing. A sentence is not a spend, and it must not cost the writer a password.

8. **Every surface prints the one decision.** The lane report, the read-lane line, the window ledger, the call
   record and the Copilot's own sentence render the same recorded value. Surfaces that each compute their own
   answer WILL drift, and the writer is the one who discovers it.

9. **A failure teaches only what it is evidence of.** A timeout is latency; a decode failure is schema or output
   length; an explicit overflow from the model is size. Narrowing a window for any of them is fair; only a size
   failure may write a size ceiling. A budget that learns from the wrong evidence ratchets, and a ratchet is
   invisible until someone measures the manuscript's share of a prompt.

10. **The resolver is pure, and it lives in a kit.** Inputs: configuration, consent, credential state, health,
    clock. Output: a resolution. No I/O, no Keychain, no network. It is a package of its own — nothing in the app
    resolves a lane, it asks the kit and receives a decision or a typed refusal.

11. **A composed pipeline carries one decision per declared role, not one accidental decision for the whole graph.**
    A local linguistic measurement may be followed by paid interpretation, enrichment, reconciliation, or synthesis,
    but each paid-capable operation receives its own recorded lane decision, budget, model revision, and idempotency
    identity. The downstream operation may not re-elect a lane or silently fall back. The decision is composed into the
    operation handoff before execution, so local processing is foundational and paid processing is the default
    extension when the governed writer-facing policy selects it.

## What this forbids, stated plainly

- Asking "which lane?" in more than one place.
- Computing a budget from anything but the decision that carries the client.
- Returning `nil` for an unavailable lane.
- Treating credential presence as permission, or permission as authorisation.
- Constructing a paid client in order to display a name, a version, a count or a status.
- Recording a ceiling from a timeout.
- A surface that renders lane state it computed itself.

## Acceptance

A change lands under this chapter only with all five:

1. **The truth table is exhaustive.** `permitted × credentialState × constructible × health × role` — every cell
   asserted against the expected resolution. The space is small and finite; example-based tests are not enough
   for a component whose failures are invisible.
2. **Budget belongs to provider.** A property test over every reachable decision:
   `decision.budget.contextWindow == decision.provider.contextWindow`. This one assertion fails today's defect.
3. **No gate widens.** A property test: the candidate set after each stage is a subset of the set before it.
4. **No prompt after a local-only instruction.** With consent `localOnly`, resolution never reaches `authorised` — proven with a
   fake credential store that RECORDS whether a data read was attempted, not merely what it returned.
5. **A regression per incident.** Presence falling silently to on-device; the window budgeted for one lane and
   executed on another; the timeout written as a size ceiling; the greeting that read the key to name a lane. Each
   is a named test, and each fails against the behaviour this chapter replaces.

Tests use fakes for the credential store and the clients: the suite never touches a Keychain and never prompts.

## Governing sentence

A lane shall be resolved once into a value that carries its own client and its own budget, obtained through
ordered gates that only narrow and refusals that always speak — so that no part of Reframe can size a window for
one lane and spend on another, and no sentence about a lane costs the writer their password.
