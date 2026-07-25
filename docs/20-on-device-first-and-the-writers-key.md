# On-Device First, and the Writer's Key — Reasoned Cloud Escalation

> Chapter summary: The on-device (Apple Foundation Models) lane is the **first lane** — the default that does the
> work, and it must plainly work on its own. The larger cloud model is a **widening of perspective**, never the
> automatic default, and it is the **writer's money**. So the writer **holds the key**: nothing spends their cloud
> account without their explicit grant, which they give and revoke **in dialogue**. When cloud would help, the
> Copilot may *offer* — a decision **reasoned on-device over the uncertainty map** (UncertaintyScoreKit), never a
> hard-coded lane table. This is the same shape as Apple's on-device → Private Cloud Compute escalation, with the
> escalation key in the writer's hand.

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

## The principle — local is the floor; cloud is the writer's to grant

Reframe stands on the on-device model. It is free, private, always present, and it is the lane the writer's work
runs on by default. A larger cloud model is a **deliberate widening** — more perspective when a specific piece of
work genuinely needs it — and it is spent from the **writer's own account**. Therefore the escalation to cloud is
**the writer's decision**, held on a key only they turn. This is Apple's own pattern — on-device first, escalate
to Private Cloud Compute only when the task exceeds on-device capacity — with one addition that the platform makes
implicit and Reframe makes explicit: **the escalation is gated by the person whose money pays for it.**

## The decision (enforceable rules)

1. **On-device is the first lane, for every role.** Planner, semantic read, and writer all default to the
   on-device model. The local experience must be **100% coherent on its own** — a manuscript can be imported,
   read into real beats, discussed, and composed with **no cloud lane at all**. "The on-device read failed" is a
   defect to fix in the read, never an excuse to reach for cloud.

2. **The writer holds the key.** No operation spends the writer's cloud account without the writer's **explicit
   grant**. The grant is **given and revoked in dialogue** — "stay on device for this," "you may spend now,"
   "I'll tell you when you're allowed to spend my money." It may be **scoped** (this one work) or **standing**
   (until revoked). The default is **local-only**. This gate sits in front of **every** cloud call; there is no
   path that reaches a paid lane around it.

3. **The escalation decision is reasoned, never tabled.** There is **no** static policy that says a role or a
   task "benefits from cloud." When the on-device pass leaves real uncertainty, the **local model reasons over the
   uncertainty map** ([UncertaintyScoreKit](https://github.com/Fountain-Coach/UncertaintyScoreKit)) — which lanes
   are `.thin` or `.failure`, what each note's `resolvedBy` says would close it — and only then may the Copilot
   **offer** to widen, naming *what cloud would resolve* and *what it costs*. Delete `benefitsFromCloud` and
   every preference-order heuristic that stands in for this reasoning.

4. **The reasoning runs on-device.** You cannot spend a cloud call to decide whether to spend a cloud call. The
   judgment "is this beyond what I can do locally?" is, by construction, a local-model judgment.

5. **The app states the lane it actually uses, before spending.** The opener and every cost-bearing surface name
   the **elected** lane — the one the work will truly run on — not a configured guess, and update the moment the
   availability probe or a runtime demotion changes it (chapter 15). When on-device, it says so and states the
   on-device-first stance: it stays local and will ask before ever widening. It never announces a lane it is not
   using. (This is the honesty half of [state the lane and cost up front].)

6. **The uncertainty substrate is inspectable.** UncertaintyScoreKit is **FCIS-AX compliant**, so the reasoning
   behind an escalation offer is machine-readable and provable, and the Copilot can **show the uncertainty map on
   request** (swapping it onto the surface and back) — the reasoning is made evident, not asserted.

7. **Fail visibly, never silently spend or fabricate.** If the on-device lane cannot do a piece of work and the
   writer has not granted cloud, the app says so plainly and stops — it does **not** silently route to a paid
   lane, and it does **not** fabricate a result. (This is [no deterministic fallbacks] and [never spend without a
   yes], applied to the lane.)

## Honesty (non-goals)

- **This is not "cloud is bad."** Cloud is a real widening and often the better read; the point is that it is the
  writer's to grant, on evidence, not the app's to assume.
- **The writer's key is not a modal nag.** A standing grant is honored until revoked; the Copilot does not re-ask
  what it has already been told. Rule 2 is a gate, not a interruption pattern.
- **Reasoned is not slow-by-default.** The escalation *offer* is reasoned only when the on-device pass surfaced
  uncertainty worth widening for — not on every turn. A confident local result is delivered locally, in silence.
- **On-device-first is not a preference toggle.** It is the architecture. There is no "prefer cloud" setting that
  reintroduces rule-1 as a checkbox; cloud is reached only through the writer's key (rule 2).

## Relationship to other chapters

- **[The situated Copilot](15-the-situated-copilot.md)** — the opening names the true lane and cost before
  anything is spent; rule 5 is that requirement made specific to the elected lane.
- **[Grounding as a given](11-grounding-as-a-given.md)** / **[Animating truth](12-animating-truth.md)** — the
  local read is the substrate the whole surface is built from; it must work for the app to work.
- **[Apple's Human Interface Guidelines](19-apple-human-interface-guidelines.md)** — this chapter is Reframe's
  application of Apple's own on-device-first / Private Cloud Compute escalation model to the writer's account.
- **FCIS-AX** — rule 6 requires the uncertainty substrate to satisfy it, so the reasoning is inspectable.
- **Feedback doctrine** — this chapter operationalizes *never spend without a yes*, *state the lane and cost up
  front*, *reason don't keyword-match* (the grant is recognized by reasoning, not a keyword), and *no
  deterministic fallbacks* (rule 7), for the specific case of the lane.

## Acceptance

The doctrine is met when:

1. **A manuscript can be imported, read into real beats, discussed, and composed entirely on-device**, with every
   cloud lane unavailable — and the result is coherent, not a wall of "couldn't read."
2. **No cloud call occurs without a writer grant** that the writer set in dialogue; with no grant, the app runs
   local or fails visibly, and never silently spends.
3. **The writer can say "stay on device"** (or grant/revoke cloud) in conversation and the Copilot honors it,
   recognized by reasoning over meaning, not a keyword.
4. **Escalation offers are reasoned over the uncertainty map**, name what cloud would resolve and its cost, and
   appear only when the on-device pass left uncertainty worth widening for — with no `benefitsFromCloud`-style
   table anywhere in the routing.
5. **Every cost-bearing surface names the elected lane**, updates on probe/demotion, and never announces a lane
   the work is not running on.
6. **The uncertainty map is FCIS-AX inspectable** and the Copilot can show it on request and switch back.
