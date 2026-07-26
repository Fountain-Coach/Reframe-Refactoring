# No Preferences, Only Reasoning

> Chapter summary: Reframe has **no preferences** — no panel where the writer configures *how the app should
> decide*. A stored toggle for "which provider," "reasoning visibility," "command autonomy," or "guide policy" is a
> decision frozen into configuration, and this whole guide's axis — [ch.20](20-on-device-first-and-the-writers-key.md)
> (the lane is reasoned, granted in dialogue), [ch.21](21-training-perspectives.md) (training is authored by
> intent) — rejects exactly that. The app **reasons** its decisions and the writer **instructs it in dialogue**. The
> only settings that remain are **facts the app cannot reason into existence**: credentials, storage location,
> account state. Those are not preferences — they are a small *Accounts & Storage* surface. Everything that was a
> preference becomes either a reasoned decision or a spoken instruction; everything that was a fact stays a fact.

## Purpose — the failure this exists to end

The current Preferences window asks the writer to be the app's control system. It carries, among others:

- **Routing decisions** — `chat.planner.provider` / `semantic.provider` / `writer.provider` pickers, the default
  engine on sign-in. (Retired by [ch.20](20-on-device-first-and-the-writers-key.md): the lane is reasoned and
  granted in dialogue, not picked in a panel.)
- **Model and pipeline tuning** — `openai.model`, `backgroundModel`, `maxOutputTokens`, cache TTL,
  `beatMaxDecodeRetries`, `beatPromptStyle`, Storify Source presets, and a spread of `chain.*.enabled` flags.
- **Disclosure and autonomy toggles** — reasoning visibility, thought disclosure, command autonomy, operational-log
  surface mode, title canonicalization, guide policy / grounding-influence mode.
- **Training configuration** — trainer backend, dataset strategy, eval gate, memory caps. (Retired by
  [ch.21](21-training-perspectives.md): training is authored by intent, expert knobs behind disclosure.)

Every one of these is a **decision the writer is forced to freeze in advance**, globally, for work that has not
happened yet — the same anti-pattern the [no-determinism-gates] and [reason, don't keyword-match] doctrines name:
a static switch standing in for a judgment that should be made, in context, by reasoning. The panel is large
because the app offloaded its decisions onto the writer. It also drifts: a stored flag says one thing while the
runtime does another (the opener that announced the wrong lane — [ch.20](20-on-device-first-and-the-writers-key.md)
— was a preference disagreeing with reality). The fix is not a tidier panel. It is to stop having preferences.

## The principle — the app reasons; the writer instructs; facts are stored, decisions are not

A **preference** is a stored answer to "how should the app decide?" A **fact** is something true about the world
the app cannot derive — a secret, a location, an account. Reframe keeps facts and abolishes preferences. Where the
app faces a decision it **reasons** it, in context, from live state (the same way it reasons the lane and the
training plan). Where the writer wants a different decision, they **say so** — an instruction in dialogue the
Copilot understands by meaning, scoped or standing, revisable at any time. What the writer used to *set* once and
forget, they now either trust the app to reason, or tell it — and telling it is cheaper, clearer, and never drifts
out of sync with what actually happens.

## The decision (enforceable rules)

1. **No stored setting is a decision.** A value in configuration may only be a **fact the app cannot reason into
   existence** (rule 3). Any setting that answers "how should the app behave / route / disclose / tune" is retired.
   The test for a survivor: *if the app could figure this out, or the writer could just say it, it is not a
   setting.*

2. **Decisions are reasoned in context, not frozen in a panel.** Every behaviour a preference used to fix — the
   lane, the model, retries, disclosure, autonomy, the guide's influence, the Storify shape — is decided by the app
   **reasoning over live state** at the moment it matters, defaulting to the doctrine already written (on-device
   first; fail visibly; the act is the star). There is no global switch that pre-commits a per-work judgment.

3. **Facts, and only facts, are stored — on a lean surface, not a preferences panel.** The survivors are the things
   the app genuinely cannot derive: **credentials** (the OpenAI API key, Codex/ChatGPT sign-in, connector secrets),
   **storage** (the managed-library / store location), and **account/environment state**. They live on a small
   **Accounts & Storage** surface whose job is to *hold a fact and show its status*, never to tune behaviour. A
   credential is not permission to spend (that is the writer's key, [ch.20](20-on-device-first-and-the-writers-key.md))
   — it is only the fact that a lane *could* be reached.

4. **The writer changes a decision by instructing, in dialogue.** What a toggle used to do, the writer now says:
   "stay on device," "show me your reasoning for this," "don't touch the source without asking," "read this the
   short way." The Copilot understands the instruction by **meaning** ([reason, don't keyword-match]), applies it
   **scoped** (this work) or **standing** (until changed), and can state what instructions are currently in force
   and drop any of them. An instruction is a living decision the writer holds, not a dead flag.

5. **A standing instruction is remembered as an instruction, not re-frozen as a preference.** When the writer says
   "always show your reasoning," that is persisted as *a thing the writer told the Copilot* — legible in the
   writer's words, revisable in dialogue, and attributed to them — not silently converted back into a hidden
   boolean. Persistence of a spoken preference keeps its provenance (who said it, when) and stays inspectable.

6. **No behaviour hides behind an un-reachable or un-stated default.** Retiring a toggle never means burying its
   behaviour in a constant the writer can neither see nor change. Either the app reasons it (and can explain why),
   or the writer can instruct it. "It used to be a setting; now it's a hard-coded default nobody can reach" is a
   regression, not a simplification ([no-determinism-gates]).

7. **Expert machinery is demoted, not deleted.** Genuine power-user config that is neither a writer decision nor a
   fact (raw trainer knobs, deep pipeline flags, diagnostics) may remain reachable behind an explicit disclosure
   for the maintainer — never on the writer's front door, never mistaken for a preference the writer must set.

## Honesty (non-goals)

- **This is not removing the writer's control — it is relocating it.** The writer has *more* control, not less:
  every decision is instructable in dialogue and revisable, instead of a fixed switch set once. The key stays in
  the writer's hand ([ch.20](20-on-device-first-and-the-writers-key.md)); it just isn't a checkbox.
- **This is not "the app decides everything silently."** Reasoned decisions are explainable and the writer can
  override any of them by saying so. Reasoning replaces the *panel*, not the writer's authority.
- **This is not deleting credentials or storage.** Facts stay — they are simply not dressed as preferences. An API
  key still has to exist; where the store lives is still a fact. Rule 3 keeps them, on a lean surface.
- **This is not a prohibition on memory.** A standing instruction is remembered (rule 5); the ban is on the app
  *inventing* a decision-toggle, not on honouring what the writer told it.

## Relationship to other chapters

- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — the founding case: the
  lane was a preference (provider pickers, default-on-sign-in) and becomes a reasoned decision + a dialogue-held
  key. This chapter generalizes that move to the whole preferences system.
- **[Training Perspectives](21-training-perspectives.md)** — the second case: training config was the sharpest
  decisions-as-configuration cluster, converted to authoring-by-intent + evidence + stored facts (the adapter and
  its provenance). This chapter states the rule those two chapters both instance.
- **[The situated Copilot](15-the-situated-copilot.md)** — dialogue is where instructions are given and where the
  Copilot states what is in force; the Copilot is the surface of this chapter.
- **[The Stage Presents the Act](18-the-stage-presents-the-act.md)** — a wall of toggles is the console this guide
  rejects; the lean Accounts & Storage surface and progressive disclosure of expert machinery are rule 3 and 7 in
  visual terms.
- **Feedback doctrine** — [no-determinism-gates] (a stored decision-gate is the anti-pattern), [reason,
  don't keyword-match] (instructions understood by meaning), [ground claims in the store] (a preference that
  disagrees with the runtime is the drift this ends), [never spend without a yes] (a credential is a fact, not a
  grant).

## Acceptance

The doctrine is met when:

1. **There is no Preferences panel of behavioural toggles** — no provider picker, no reasoning-visibility /
   command-autonomy / guide-policy / disclosure switches, no model/retry/preset tuning on the writer's surface.
2. **What remains is a lean Accounts & Storage surface** holding only facts (credentials, sign-in, store location)
   and showing their status — never tuning behaviour.
3. **Every retired toggle's behaviour is either reasoned** (the app decides in context and can explain it) **or
   instructable in dialogue** — and none has become an unreachable hidden constant.
4. **The writer can change any such behaviour by telling the Copilot**, understood by meaning, scoped or standing,
   and can ask what instructions are currently in force and drop any of them.
5. **A standing instruction is stored as the writer's instruction** (legible, attributed, revisable), not
   re-frozen into a hidden boolean.
6. **Expert machinery, if kept, lives behind an explicit disclosure** for the maintainer, off the writer's front
   door.
