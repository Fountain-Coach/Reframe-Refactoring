# Reliable Copilot, and the Writer's Key — Quality-First Lane Selection

> Chapter summary: Copilot's conversational quality is a credibility requirement. When a reliable paid lane is
> available and the writer has authorized it, it is the default for open-ended dialogue and Coaching Mode. The
> on-device lane remains the preferred optimization for bounded, private, deterministic, and offline work. It is
> never a silent downgrade that makes a writer repeat herself or accept a visibly weaker conversation. The writer
> still holds the key: nothing spends her account without explicit grant, and every lane statement describes what
> actually happened.

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
is therefore the default for open-ended conversation once the writer has authorized it. On-device execution is a
first-class optimization—private, fast, inexpensive, and useful for bounded work—not a degraded conversational
fallback. The writer's key still governs spending: quality preference never becomes permission to charge. If the
paid lane is not authorized or unavailable, Reframe explains the boundary and offers the local mode without losing
the turn or pretending that the experience is equivalent.

## The decision (enforceable rules)

1. **Select the lane by the work's quality requirement.** Open-ended conversation, situation-aware coaching, and
   turns whose quality depends on sustained context default to the reliable paid lane when it is available and the
   writer has granted access. Bounded catalog lookup, deterministic controls, private preparation, and offline work
   may default on-device. No universal “on-device first” rule may force a weaker dialogue.

2. **The writer holds the key.** No operation spends the writer's cloud account without the writer's **explicit
   grant**. The grant is **given and revoked in dialogue** — "stay on device for this," "you may spend now,"
   "I'll tell you when you're allowed to spend my money." It may be **scoped** (this one work) or **standing**
   (until revoked). The default is **no spend until granted**; once a standing or work-scoped grant exists, the
   quality-first conversational route may use the paid lane by default. This gate sits in front of **every** cloud
   call; there is no path that reaches a paid lane around it.

3. **The quality class is reasoned, never keyword-matched.** The mediator distinguishes open conversation from
   bounded operations using grounded intent and live state. It must not use a static phrase table or a provider
   preference to force dialogue onto the local lane. A paid conversational default is a quality policy, not a license
   to charge: consent remains a separate gate.

4. **The route decision may not destroy the turn.** A local mediator may classify a turn, but a local capacity
   failure must preserve the original turn, current situation, and conversation context. It must hand off to the
   authorized paid lane or ask for authorization; it may not emit “try again,” silently downgrade, or execute an
   unrelated operation.

5. **The app states the lane it actually uses, before spending.** The opener and every cost-bearing surface name
   the **elected** lane — the one the work will truly run on — not a configured guess, and update the moment the
   availability probe or a runtime demotion changes it (chapter 15). It never announces a lane it is not using, and
   it never presents local output as equivalent to a failed or unavailable paid conversation. (This is the honesty
   half of [state the lane and cost up front].)

6. **The uncertainty substrate is inspectable.** UncertaintyScoreKit is **FCIS-AX compliant**, so the reasoning
   behind an escalation offer is machine-readable and provable, and the Copilot can **show the uncertainty map on
   request** (swapping it onto the surface and back) — the reasoning is made evident, not asserted.

7. **Recover visibly, never silently spend or fabricate.** If the selected paid lane fails, Reframe preserves the
   turn and offers an honest local continuation or retry. If local mediation fails, Reframe preserves the turn and
   offers the paid lane when available. Neither failure path may fabricate a result, invoke an unrelated operation,
   or make the writer repeat herself.

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

- **This is not "cloud is bad."** Cloud is a real widening and often the better read; the point is that it is the
  writer's to grant, on evidence, not the app's to assume.
- **The writer's key is not a modal nag.** A standing grant is honored until revoked; the Copilot does not re-ask
  what it has already been told. Rule 2 is a gate, not a interruption pattern.
- **Reasoned is not slow-by-default.** Bounded local work stays local without ceremony. Conversational work uses
  the reliable paid lane by default after consent; the route is not delayed by an unnecessary local probe.
- **Quality-first is not a preference toggle.** It is the conversational default once the writer has granted access;
  local execution remains an implementation optimization, not a weaker preference the writer must defend.

## Relationship to other chapters

- **[The situated Copilot](15-the-situated-copilot.md)** — the opening names the true lane and cost before
  anything is spent; rule 5 is that requirement made specific to the elected lane.
- **[Grounding as a given](11-grounding-as-a-given.md)** / **[Animating truth](12-animating-truth.md)** — the
  local read is the substrate the whole surface is built from; it must work for the app to work.
- **[Apple's Human Interface Guidelines](19-apple-human-interface-guidelines.md)** — this chapter applies Apple's
  privacy and consent principles while making Reframe's separate quality requirement explicit: reliable dialogue
  must not be degraded merely to save a lane call.
- **FCIS-AX** — rule 6 requires the uncertainty substrate to satisfy it, so the reasoning is inspectable.
- **Feedback doctrine** — this chapter operationalizes *never spend without a yes*, *state the lane and cost up
  front*, *reason don't keyword-match* (the grant is recognized by reasoning, not a keyword), and *no
  deterministic fallbacks* (rule 7), for the specific case of the lane.

## Acceptance

The doctrine is met when:

1. **A manuscript can be imported and composed on-device** when the paid lane is unavailable, while open-ended
   Coaching Mode uses the authorized paid lane by default when it is available; neither path may produce a dead-end
   capacity error or silently change the writer's request.
2. **No cloud call occurs without a writer grant** that the writer set in dialogue; with no grant, the app runs
   local or fails visibly, and never silently spends.
3. **The writer can say "stay on device"** (or grant/revoke cloud) in conversation and the Copilot honors it,
   recognized by reasoning over meaning, not a keyword.
4. **Lane selection is quality-aware and grounded**, with no `benefitsFromCloud`-style table anywhere in the routing;
   conversational quality selects the reliable paid lane after consent, while bounded work may remain on-device.
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
