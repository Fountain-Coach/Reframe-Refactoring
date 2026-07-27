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
