# Internals Tune Themselves — the Disposition of the Preferences Panel

> Chapter summary: The default disposition of any internal is **reasoned** — Reframe decides it **dynamically, in
> context, at the moment it matters** (output caps, routing, the storify window, retries, budgets, the reading
> shape), and can explain the decision. The writer meets a setting **only when their judgment is genuinely needed**
> — a stance, a spend, a voice, a training intent — and then the **CoPilot surfaces it contextually** (at the
> relevant moment, in the writer's words), teaches what it is, and asks; it is never a standing toggle. Facts the
> app cannot derive (credentials, storage, account) stay on a lean surface. Raw maintainer machinery lives behind an
> explicit disclosure, off the writer's path. Runtime/learned state (last-opened, drawer widths, learned budgets) is
> not a preference at all. This chapter turns [ch.22](22-no-preferences-only-reasoning.md) (no preferences) and
> [ch.25](25-the-copilot-is-the-surface.md) (the CoPilot is the surface) into a **disposition procedure** and applies
> it to every setting Reframe currently persists.

## Purpose — the failure this exists to end

An audit of the live Preferences window found **73 persisted settings** across six tabs — General, Providers,
Writing, Integrations, LoRA, Developer. The great majority are decisions the app has offloaded onto the writer:
routing (Planner/Semantic/Writer engine pickers), model tuning (per-lane max output tokens), reading shape (Storify
source presets, structural-alignment presets, title canonicalization), disclosure/autonomy (reasoning visibility,
command autonomy, thought disclosure, pipeline-log surface), grounding defaults (author/reader preset ids, the
manifesto override — already retired), persona, and a large block of LoRA trainer knobs. A writer should never have
to know what a "max output token", a "structural-alignment preset", or a "trainer backend" is — and if a genuine
choice hides in there (spend, voice, stance), a **panel is the wrong place to meet it**: it is out of context, set
once for work that hasn't happened, and it drifts out of sync with the runtime ([ch.22](22-no-preferences-only-reasoning.md)).

The deeper failure a panel encodes: it treats every internal as a **standing decision the writer must pre-freeze**.
But most internals are not decisions at all — they are things Reframe can **work out in context** better than a
frozen switch can (how big a read window fits *this* chapter on *this* lane; whether to retry; which lane is
reachable now). And the few that are genuine writer decisions are best met **when they arise**, in conversation, not
hunted for in a tab.

## The principle — reasoned by default; contextual when the writer's judgment is needed

1. **Internals tune themselves.** Where Reframe can reason a value from live state, measurement, or doctrine, it
   **does so dynamically, at the moment it matters**, and can explain why. There is no setting. This is the default
   for routing, tuning, retries, budgets, and reading shape.

2. **The writer is asked only when their judgment is genuinely needed — and then in context.** A stance ("read it
   as…"), a spend (the cloud key), a voice/persona, a training intent — these need the writer. They are **surfaced
   by the CoPilot at the relevant moment**, taught in plain language, and asked, then held as a spoken instruction
   (scoped or standing, revisable — [ch.25](25-the-copilot-is-the-surface.md)). Never a standing toggle the writer
   must find.

3. **Facts, and only facts, are stored — on a lean surface.** Credentials, storage location, account/environment
   state (ch.22 rule 3). A lean *Accounts & Storage* surface holds a fact and shows its status; it never tunes
   behaviour.

4. **Maintainer machinery is demoted behind an explicit disclosure.** Diagnostics, trace retention, raw trainer
   internals — reachable for the maintainer, never on the writer's path, never mistaken for a writer decision.

5. **Runtime and learned state is not a preference.** Last-opened ids, drawer widths, learned auto-sizing budgets,
   run ids — plumbing. Persisted for continuity, never surfaced as configuration.

## The disposition procedure (apply to every setting)

For each persisted setting, ask in order; the first match is its disposition:

1. **Is it a FACT the app cannot derive?** (a secret, a location, an account) → **Fact.** Lean Accounts & Storage
   surface.
2. **Can Reframe REASON it in context?** (from live state, a measurement, or a written doctrine) → **Reasoned.** No
   surface; decided dynamically at the moment it matters; explainable on request. *This is the default answer for
   anything that tunes, routes, sizes, retries, or shapes.*
3. **Does it need the WRITER's judgment?** (a stance, a spend, a voice, an intent) → **Dialogic.** The CoPilot
   surfaces it contextually, teaches it, asks; instructable, scoped/standing, revisable.
4. **Is it raw MAINTAINER machinery?** (diagnostics, trainer internals) → **Maintainer.** Behind an explicit
   disclosure, off the writer's path.
5. **Is it RUNTIME/LEARNED state?** (continuity, memory, a learned budget) → **Plumbing.** Not a preference; never
   surfaced as config.

"If Reframe could work it out, or the writer could just say it, it is not a setting." A value survives as a
writer-facing control only if it is a **fact** (rule 1). Everything else is reasoned (2), dialogic (3), maintainer
(4), or plumbing (5).

## Applied audit — the 73 settings, disposed

**Reasoned (no surface; Reframe decides in context, explainable):**
- Routing: `plannerProvider`, `semanticProvider`, `writerProvider` — the lane is elected from probed facts + the
  writer's key ([ch.20](20-on-device-first-and-the-writers-key.md)), not picked.
- Model tuning: `plannerAppleMaxOutputTokens`, `semanticAppleMaxOutputTokens`, `writerAppleMaxOutputTokens` — output
  is bounded by the window/measurement, never a writer knob.
- Reading shape: `storifySourcePresetId`, `storifySourceCustomPresets`, `structuralAlignmentPresetId`,
  `structuralAlignmentCustomPresets`, `storifyTitleCanonicalizationMode`, `pipelineTransparencyPresetId`.
- Grounding influence: `groundingInfluenceModeDefault` (per-session override is state).

**Dialogic (CoPilot surfaces contextually, teaches, asks — never a standing toggle):**
- Disclosure/autonomy: `reasoningVisibilityMode`, `manuscriptThoughtDisclosureMode`, `commandAutonomyMode`,
  `pipelineLogSurfaceMode` — "show me your reasoning", "don't touch the source without asking".
- Grounding: `defaultAuthorBaselinePresetId`, `defaultReaderLensPresetId` (the shipped-preset choice — the lens
  itself is dialogic, [ch.25](25-the-copilot-is-the-surface.md)); `defaultProjectLanguageCode` (confirmed in
  dialogue when detection is uncertain).
- Voice: `modernizePersona`, `modernizePersonaPresetId`.
- Training intent: `loraShadowTrainingEnabled`, `loraRole`, `loraTrainingProfile`, `loraCorpora`, `loraAdapterId` —
  authored by intent ([ch.21](21-training-perspectives.md)).

**Fact (lean Accounts & Storage / Integrations surface):**
- Credentials: `openAIApiKey`, `facebookAppId`, `facebookAppSecret`, `facebookRedirectURI`, `facebookStoredToken`.
- Storage/env: `storePath`, `managedStoreResolvedLegacyPath`, `managedStoreLegacySourceManifest`,
  `appleAdapterLoadCommand`, `loraAppleToolkitPath`, `loraTrainerCommand`, `loraManifestPath`, `loraEnvironment`.

**Maintainer (behind an explicit disclosure, off the writer's path):**
- Diagnostics: `analyticsFullCaptureEnabled`, `analyticsJSONLPreset`, `storifyTraceExhaustiveEnabled`,
  `storifyTracePersistFullRun`, `storifyTraceRetentionPolicy`.
- Raw trainer knobs: `loraAdvancedModeEnabled`, `loraTrainerBackend`, `loraSwiftMode`, `loraSwiftRank`,
  `loraSwiftSteps`, `loraSwiftLearningRate`, `loraSwiftVocabularyCap`, `loraSwiftMemorySoftCapMB`,
  `loraDatasetMode`, `loraDatasetMaxDocs`, `loraEvalMode`, `loraPairMinNovelty`.

**Plumbing (runtime/learned state — not a preference):**
- Continuity: `lastCorpusId`, `lastSceneId`, `loraRunId`, `loraLastDecision`, `loraLastDecisionReason`,
  `loraWizardSessionState`, `beatAdaptiveResetToken`.
- UI memory: `mainStorifyMemoryDrawerOpen`, `mainStorifyMemoryDrawerWidth`, `storifyRunMemoryDrawerOpen`,
  `storifyRunMemoryDrawerWidth`.
- Learned budgets: `semanticAutoSizingSummary`, `semanticAutoSizingUpdatedAt`, `storifySourceAutoSizingSummary`,
  `storifySourceAutoSizingUpdatedAt` — learned by observation, not set.
- Already retired: `groundingInfluenceModeBySession` (session state, not config); the grounding manifesto override
  (cd30bd96).

## What "getting rid of it" looks like

For each non-fact tab section: replace the control with either **nothing** (the value is now reasoned, and the
CoPilot can explain it if asked) or a **dialogic hand-off** (the CoPilot surfaces and teaches it when relevant).
The end state of the Preferences window is a **lean Accounts & Storage + Integrations surface** plus a
maintainer-only Developer disclosure — no Providers routing panel, no Writing tuning, no LoRA knob wall on the
writer's path. The retirement order follows impact: Providers routing (the writer's key already replaces it) →
Writing tuning/shape → LoRA (intent + maintainer split) → the disclosure/autonomy toggles → collapse what remains
to Accounts & Storage.

## Retirement log (what has actually been executed)

1. **Providers routing** (dd7ef5a8) — the Planner/Semantic/Writer engine pickers. The lane is elected from the
   engines reachable now and governed by the writer's key ([ch.20](20-on-device-first-and-the-writers-key.md)).
2. **Writing tuning/shape** — the *Storify Source Preset* knob wall (extraction chunking, page sizing, prompt
   budgets, retries, fallback toggles, memory weights) and the never-instantiated structural-alignment twin
   deleted outright (~2,200 lines); the *pipeline transparency* preset, the *title canonicalization* picker (it
   offered exactly one mode — a menu with a single choice is not a decision), and the *Guide policy* picker
   (publish-required vs strict) retired. The Storify trace knobs moved to a **Developer → Diagnostics**
   disclosure. What remains on the tab: grounding pointers, the manuscript-guide defaults, the Composer Persona,
   and a *Disclosure & Autonomy* section holding the four toggles that are dialogic work (step 4).
   - **Retired means the value no longer governs, not merely that the control is hidden.** `ReframePreferences.load()`
     stopped reading the routing picks, the storify/structural preset picks, and title canonicalization back into
     the runtime; the transparency preset and grounding-influence default resolve to doctrine. Otherwise a pick made
     months ago keeps steering work it knows nothing about — the drift ch.22 exists to end. A maintainer can still
     pin any of these in the config file (rule 4).

3. **LoRA** — the raw trainer knobs were already behind an "Advanced" disclosure plus a "Show technical fields"
   toggle, so the maintainer half of [ch.21](21-training-perspectives.md) was structurally done. What was wrong was
   what sat *outside* it and what was *misfiled inside* it:
   - The tab opened on **Environment / Role / Corpora** pickers — overrides on values the wizard already derives
     from the manuscript. A writer asked to choose "planner | semantic | writer" is being asked to be an ML
     engineer (ch.21 rule 1), and an override left from a previous run silently retargets the next one. The front
     door now *reports* what was derived — "Learning from", "Teaches" — and names an override only when one
     actually differs. The controls moved into the maintainer disclosure as "Retarget this run".
   - The **shadow comparison** toggle was buried among the expert knobs. Evidence is how a perspective earns
     adoption (ch.21 rule 2) — burying it puts the machinery in front of the judgment. It now sits in the Decide
     step in the writer's terms: "Compare against the current model before adopting."

4. **The disclosure/autonomy toggles** — operational logs, reasoning visibility, thought disclosure, command
   autonomy. The first step that was not subtractive: these four *are* genuine writer decisions, which is why the
   panel was the wrong place for them (set once, out of context, for work that had not happened). They are now
   instruction, held in dialogue — the CoPilot states the stance on request and moves it when told, mirroring
   ch.25's grounding. The stored values still govern; nothing sets them from a standing toggle.
   - **One taxonomy case, not two.** `setDisclosure` and `describeDisclosure` began as separate targets in the one
     reasoning and **oscillated**: strengthening either bullet broke the other, because "show me your reasoning" is
     genuinely both a question and an instruction. They collapsed into a single `disclosureStance` case, with a
     focused second call deciding ask-vs-tell, which dimension, and which way — the same shape as ch.20's isolated
     spend guard, and for the same reason: the small model is reliable on one narrow question, not on a crowded one.
   - **Direction, not mode names.** The writer says "show me more of your thinking", never "set thought disclosure
     to expanded". Each stance is an ordered scale and an instruction moves it one step; at the end of a scale the
     CoPilot says so rather than claiming a change that did not happen.
   - **An autonomy increase is double-guarded.** Letting the app act on the writer's work without asking is the one
     move here that is hard to take back, and negation is exactly what the small model mis-reads. A proposed
     increase is re-checked in isolation; the safe default is to ask.
   - **Measured limit, recorded not hidden.** Across four live revisions on the real on-device model, the two
     behaviour-CHANGING cases pass reliably — including the negation trap "don't touch the source without asking".
     A conduct QUESTION ("will you act on my work without asking me?") still routes to `answerQuestion` and gets a
     generic answer instead of the stance. The miss **rotates** between neighbouring bullets depending on which was
     strengthened last — the 4K crowding ceiling, where every capability crowds out the one beside it. Shipped
     because the failure is benign (a weak answer, never a wrong action) and marked `XCTExpectFailure` in
     `LiveDialogicDisclosureTests`. The fix is structural, not more prompt text: put the current stance into the
     manifest the answer producer reads, so a conduct question answers truthfully wherever it routes.

5. **The collapse.** Two reasoned leftovers were still on the writer's path and went first: the **Apple Foundation
   Models** card (per-lane max output tokens — a stored number can only be wrong later; too low silently truncates
   a guided generation, which is what blocked the launcher health probe) and the **Manuscript Guide Defaults**
   section (default author-baseline and reader-lens presets, default language, and a "Use Current Manuscript as
   Defaults" button that wrote one manuscript's lens out as the global default for every future one — the exact
   drift cd30bd96 retired the manifesto override for, now that the lens is dialogic). Both stopped being read back
   into the runtime; a fresh manuscript inherits the shipped default.
   Then the **Providers tab** was retired outright: routing went in step 1 and the token overrides here, leaving
   only facts and a status readout. The OpenAI credential and the connection check moved to **Accounts & Storage**
   (General, renamed — it now holds only facts: where the library lives, the credential that pays for cloud); the
   raw codex `/status` moved to the **Developer** disclosure.

**End state reached.** The window is Accounts & Storage · Writing · Integrations · LoRA · Developer.

**What is left, and it is not a retirement.** Two writer-facing surfaces remain that ch.26 files as *dialogic*, and
each needs a capability built before its control can go — the same shape as step 4, not more deleting:
- the **Composer Persona** (voice) — the CoPilot must be able to hold and revise a persona in dialogue;
- **training intent** on the LoRA tab (ch.21 rule 1) — the writer says "learn how I write the Nurse" and the app
  reasons role, corpora and plan from it.

Neither should be faked by keyword-matching an instruction to a preset — that is the anti-pattern [reason, don't
keyword-match] exists to stop. Still open from ch.21: the writer authors a perspective **by intent** ("learn how I write the
Nurse") and the app reasons role/corpora/plan from it. That is an authoring build needing a reasoned pass, not a
retirement — the derived values are honest today, but the writer still cannot state the intent in their own words.

> Retiring a surface is not finished until its **tests** move with it. The ch.25 grounding-editor retirements left
> `BaselineWorkbenchPanel` tests and a manifesto-key test behind, and the whole test target stopped compiling for
> several commits without anyone noticing — a retirement that silently disables the suite buys the drift it was
> meant to remove. Those tests now render the live Prep surface. Pixels for each step come from
> `PreferencesPaneRenderHarness` (light + dark, full scrolled height).

**Open debt — three Preferences goldens cannot be promoted.** `settings-writing` and `settings-developer` were
refreshed with this step. `settings-general`, `settings-providers` and `settings-lora` still mismatch for reasons
that are not doctrine — each renders **machine state**, and a golden that encodes one machine cannot fail honestly:

| pane | what leaks into the golden |
| --- | --- |
| `settings-general` | the accumulating list of detected legacy libraries under `/var/folders/…`, one row per past test run |
| `settings-lora` | the Foundation-chat availability banner — the recorded golden says "requires macOS 26.4 or newer", a machine with Apple FM says "Ready" ([ch.20](20-on-device-first-and-the-writers-key.md)'s floor showing through) |

`settings-providers` is gone with its tab. `settings-writing`, `settings-developer` and `settings-integrations` are
promoted and stable. The LoRA pane's own content is otherwise deterministic; it is only that banner that blocks it.
These two need the availability/environment state injected as a fixture before their VRT means anything.

One caution learned in step 5: moving the codex `/status` readout to Developer briefly made *that* golden
machine-dependent too (it renders the local account and working directory). Putting it behind the disclosure —
where maintainer machinery belongs anyway — fixed both the doctrine and the golden. Watch for this whenever a card
moves: a pane is only VRT-able while everything it renders inline is deterministic.

## Relationship to other chapters

- **[No Preferences, Only Reasoning](22-no-preferences-only-reasoning.md)** — the prohibition; this is its
  disposition procedure and applied audit.
- **[The CoPilot Is the Surface](25-the-copilot-is-the-surface.md)** — where a genuine writer decision re-appears
  (dialogic, taught, contextual); this chapter adds "reasoned by default, surfaced only when judgment is needed."
- **[On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md)** — routing is reasoned +
  keyed, the founding "reasoned away a picker" case.
- **[Training Perspectives](21-training-perspectives.md)** — the LoRA split: intent is dialogic, raw knobs are
  maintainer.
- **Feedback doctrine** — [no-determinism-gates] (a stored decision-gate is the anti-pattern; a reasoned value must
  not become an unreachable constant either — it must be explainable/instructable), [reason, don't keyword-match],
  [ground claims in the store] (the drift a panel causes), [never spend without a yes] (spend is dialogic, not a
  checkbox).

## Acceptance

The doctrine is met when:

1. **Every persisted setting has a recorded disposition** — fact, reasoned, dialogic, maintainer, or plumbing —
   and nothing is a standing writer-facing behavioural toggle.
2. **Reasoned values decide in context and can be explained** — the writer can ask "why did you read it that way /
   use that lane / stop there?" and get an answer; the value is never a hidden unreachable constant.
3. **Genuine writer decisions are met in dialogue, contextually** — surfaced by the CoPilot at the relevant moment,
   taught, asked, held as instruction (scoped/standing, revisable).
4. **Facts live on a lean Accounts & Storage / Integrations surface** and only hold + show status.
5. **Maintainer machinery is behind an explicit disclosure**, off the writer's path.
6. **Runtime/learned state is never dressed as configuration.**
