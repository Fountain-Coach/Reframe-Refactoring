# Paid-First Copilot, and the Writer's Key — Quality-First Lane Selection

> Chapter summary: Copilot's conversational quality is a credibility requirement. Copilot silently chooses the best
> eligible route for the current work from live capability, credential, budget, and health facts. A reliable paid lane
> serves open-ended dialogue and Coaching Mode by default when available;
> on-device execution handles bounded, private, deterministic, and offline work wherever it preserves the experience.
> Delegation is internal: the writer sees one continuous Copilot, not provider handoffs or a weaker-mode offer. The
> writer still controls the route: paid is preferred when available, and an explicit local-only instruction keeps the
> current work on-device.

## Purpose — the failure this exists to end

A live, in-situ run of the Copilot on *Romeo and Juliet* exposed a coherent, damning failure of the lane model:

- **Cloud was the default the moment an account was signed in.** `reframeDefaultEngine()` returned the ChatGPT
  plan on sign-in; `ReframeLaneElection` treated on-device as a *fallback* via a hard-coded `benefitsFromCloud`
  table. So "signed in" silently meant "spend."
- **The on-device lane never actually ran.** The semantic read routed to a `403`/`429` OpenAI key that was out of
  quota, and reported **every passage as "Couldn't read this passage"** — while the opener told the writer it was
  running on-device. The local model, the free and always-available one, did no work at all.
- **The app lied about which model answered.** The opener was built from *configured* providers, not the elected
  lane; it announced "on-device … OpenAI API key" while the election had chosen something else. Asked directly,
  the Copilot stated the opposite of the truth.
- **The "fixes" were improvised as hard-coded lane tables** — forcing a lane, prepending a lane to a preference
  order, flipping `benefitsFromCloud`. Each was a static heuristic standing in for a decision that should be
  *reasoned*, and each was the wrong shape.

The through-line: the app decided the writer's spend by *configuration and guessing*, defaulted to cloud, failed
the free local lane it should have relied on, and misreported all of it. This chapter fixes the model.

## The principle — credibility is the floor; the writer's key governs spend

Reframe must feel as capable and fluent as the conversational standard the writer already knows. A reliable paid lane
is therefore the default for open-ended conversation and economically meaningful work whenever it is available.
On-device execution is a first-class optimization—private, fast, inexpensive, and useful for bounded work—selected
internally when it preserves the required experience and yields an economic benefit. The writer may explicitly say
"stay on device" or otherwise revoke paid use; that instruction is remembered as the local-only override. Paid
unavailability is a typed boundary, not a reason to discard the request.

## The decision (enforceable rules)

1. **Select the best eligible route for the task.** Open-ended conversation, situation-aware coaching, and turns whose
   quality depends on sustained context use the best available paid model when available. Bounded catalog lookup,
   deterministic controls, private preparation, and offline work may run on-device. The route is an internal quality
   decision; the writer is never asked to choose between providers or offered a weaker mode as a product experience.

2. **Paid is the default when available.** The best eligible paid model serves the writer-facing request by default
   when its capability, credential, account, transport, context budget, and health are available. The writer may **revoke** paid use in dialogue—
   "stay on device for this," "keep this local," or an equivalent meaning—and that instruction is remembered as the
   local-only override. There is no requirement that the writer learn a spend-specific phrase before Reframe can
   understand a direct request to use the paid lane. Paid unavailability remains a typed refusal and the app may use
   a local route only when it can preserve the requested outcome.

3. **The quality class is reasoned, never keyword-matched.** The mediator distinguishes open conversation from
   bounded operations using grounded intent and live state. It must not use a static phrase table or a provider
   preference to force dialogue onto the local lane. Cost-aware delegation happens after the quality class is known;
   consent remains a separate gate.

4. **Internal delegation preserves continuity.** A local mediator may classify a turn, but a local capacity failure
   must preserve the original turn, current situation, and conversation context while routing internally to the
   reliable paid lane when it is available. A provider retry or delegation is not a new writer-facing turn and must
   not execute an unrelated operation.

5. **The app states cost only where cost becomes relevant.** The opening conversation does not teach provider
   machinery. A paid route is disclosed at the consent boundary with its cost and purpose; the writer is not asked to
   approve an internal optimization or delegation. Any status disclosure names the route actually used, never a
   configured guess.

6. **The uncertainty substrate is inspectable.** UncertaintyScoreKit is **FCIS-AX compliant**, so the reasoning
   behind an escalation offer is machine-readable and provable, and the Copilot can **show the uncertainty map on
   request** (swapping it onto the surface and back) — the reasoning is made evident, not asserted.

7. **Recover internally, disclose only an actual boundary.** If a provider fails, Reframe preserves the turn and
   retries or delegates within the authorized route set. It must not fabricate a result, invoke an unrelated
   operation, or make the writer repeat herself. Only when no authorized route can complete the work may Copilot
   explain the service boundary and ask for the one consent or action that would change it.

## Where the key lives — custody, not only consent

Everything above governs WHEN the writer's key is used. It says nothing about where the key is kept, and that gap
had a measurable answer.

Measured 2026-08-06, the credential Reframe spends with:

```
-rw-r--r--  ~/.stage-native.config.json
             chat.openai.apiKey = <164 characters, plaintext>
```

World-readable, mode 644, on the same account this app charges. Reframe reads a key from three plaintext places —
that JSON file, `~/.codex/auth.json`, and the `OPENAI_API_KEY` environment variable — and from the Keychain never.

The organisation already owns the answer. `swift-secretstore` ships a `SecretStore` protocol with a `KeychainStore`
backend, it is used by `Fountain-Store`, `CILocal`, `SDLKit` and `the-fountainai` — and because Reframe depends on
Fountain-Store, **it is already in Reframe's resolved dependency graph.** The library is compiled into the build
today and never called. The one application in the estate that actually spends the writer's money is the one
keeping her credential in a file anything can read.

Consent without custody is a strong door on an open window. A grant the writer gives in dialogue means very little
if the key it authorises can be copied by any process on the machine — and worse, it makes the app's careful
account of *when* it spends into a false comfort, because the spending it governs is not the only spending the key
permits.

### The decision (enforceable rules, continued)

8. **The Keychain is the only place a key is read from.** `SecretStore` is the single custody path. There is no
   second supported way to supply a credential — not an environment variable, not a config file, not another
   application's auth file — because a fallback is a plaintext path that the writer believes is closed.

9. **A key found in plaintext is a defect the app reports and helps close.** Reframe does not silently keep using
   it and does not silently delete the writer's file. It names the file, offers to move the secret into the
   Keychain, and says what to remove afterwards. A migration the writer did not consent to is its own violation.

10. **A key is never logged, echoed, persisted to the store, or included in any report, telemetry or receipt** —
    including the diagnostic surfaces this repository is otherwise generous with. Its presence may be stated; its
    value never leaves the Keychain.

11. **The absence of a key is a lane fact, not an error.** With no credential the paid lane is simply not
    available, and the app says so with the on-device lane as its remedy
    ([ch.48](48-a-service-is-a-fact-not-a-symptom.md) rules 4-5) — never a prompt to paste a secret somewhere it
    would land in plaintext.

## Honesty (non-goals)

- **This is not "local is bad."** Local execution is an important efficiency, privacy, and offline path; the point
  is that it is selected internally only when it preserves the required experience.
- **The writer's local-only instruction is not a modal nag.** A local-only instruction is honored until revised; the
  Copilot does not re-ask what it has already been told. Rule 2 is a policy boundary, not an interruption pattern.
- **Delegation is not a writer-facing mode.** Bounded local work stays local without ceremony. Conversational work
  uses the reliable paid lane by default after consent, while internal local sub-work may reduce cost without changing
  the visible Copilot experience.
- **Quality-first is not a preference toggle.** It is the internal routing rule: use the reliable paid route when
  available, then optimize bounded sub-work locally without making the writer defend a provider choice.

## Relationship to other chapters

- **[The situated Copilot](15-the-situated-copilot.md)** — the opening names the true lane and cost before
  anything is spent; rule 5 is that requirement made specific to the elected lane.
- **[Grounding as a given](11-grounding-as-a-given.md)** / **[Animating truth](12-animating-truth.md)** — the
  local read is the substrate the whole surface is built from; it must work for the app to work.
- **[Apple's Human Interface Guidelines](19-apple-human-interface-guidelines.md)** — this chapter applies Apple's
  privacy and consent principles while making Reframe's separate quality requirement explicit: reliable dialogue
  must not be degraded merely to save a lane call.
- **FCIS-AX** — rule 6 requires the uncertainty substrate to satisfy it, so the reasoning is inspectable.
- **Feedback doctrine** — this chapter operationalizes *never spend without a yes*, *state cost at the consent
  boundary*, *reason don't keyword-match*, and *recover without exposing internal delegation* for the specific case
  of the lane.

## Acceptance

The doctrine is met when:

1. **A manuscript can be imported and composed on-device** when no paid route is authorized, while open-ended
   Coaching Mode uses the strongest authorized conversational lane by default; neither path may produce a dead-end
   capacity error or silently change the writer's request.
2. **A paid call uses the elected eligible paid route** when paid policy is available; with an explicit local-only
   instruction, the app runs local or fails visibly. A missing or unhealthy paid route is reported plainly.
3. **The writer can say "stay on device"** (or grant/revoke cloud) in conversation and the Copilot honors it,
   recognized by reasoning over meaning, not a keyword.
4. **Lane selection is quality-aware and grounded**, with no `benefitsFromCloud`-style table anywhere in the routing;
   conversational quality selects the strongest authorized route, while bounded work may be delegated on-device.
5. **Every cost-bearing surface names the elected lane**, updates on probe/demotion, and never announces a lane
   the work is not running on.
6. **The uncertainty map is FCIS-AX inspectable** and the Copilot can show it on request and switch back.
7. **The key is read from the Keychain and nowhere else.** With the credential in `SecretStore` and every
   plaintext path removed, the paid lane works; with the Keychain entry deleted, the paid lane is reported
   unavailable and the on-device lane carries the work. Searching the repository finds no code path that reads a
   credential from an environment variable or a configuration file.
8. **A plaintext key on the machine is reported, not consumed.** The app names the file, offers the move, and does
   not delete anything the writer did not ask it to.
9. **No log, receipt, telemetry event or store document contains a key value**, verified by searching the run's
   output and the store after a paid read.
