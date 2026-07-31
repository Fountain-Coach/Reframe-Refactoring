# Reading Index

> Chapter summary: This index offers role-based reading paths, chapter descriptions, and a vocabulary map so humans and agents can retrieve only the material relevant to the task at hand. It covers the founding Grounding-first transition (00–11) and the working-surface, reasoning, knowledge, retrieval, and uncertainty-representation doctrine that grew from it (12–36). See the [root README](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/README.md) for the genesis and full arc.

The suite is intentionally divided into short, stable chapters. Agents should not load the whole directory into every prompt. Select the chapters whose authority is necessary for the current task, then retrieve live code and state for implementation detail. A UI claim is not settled by an accessibility-tree query alone — chapter 18 requires *looking* at the rendered view.

## Reading paths

### Product and architecture review

Read the [abstract](00-abstract.md), [development history](02-development-history.md), and [target architecture](04-target-architecture.md). These chapters explain why the older index-centered design existed, why its lessons remain valuable, and why authority moves to Grounding and Storify now.

### Grounding implementation

Read the [target architecture](04-target-architecture.md), [Grounding contract](05-grounding-contract.md), and phases 1–3 of the [refactoring program](06-refactoring-program.md). Finish with the relevant tests in [validation and acceptance](08-validation-and-acceptance.md).

### Storify implementation

Read the [current-state analysis](03-current-state-and-problem.md), [Grounding contract](05-grounding-contract.md), and phases 2–4 of the [refactoring program](06-refactoring-program.md). The source-authority and no-index acceptance cases in [validation and acceptance](08-validation-and-acceptance.md) are mandatory.

### Readiness, journey, or UI implementation

Read the [target architecture](04-target-architecture.md), phase 4 of the [refactoring program](06-refactoring-program.md), and [compatibility and future evolution](09-compatibility-and-future-evolution.md). These changes are incomplete until generated capabilities and reasoning artifacts agree with the UI.

### Index deletion

Read the entire [refactoring program](06-refactoring-program.md), especially its deletion gate, followed by the [agent operating guide](07-agent-operating-guide.md) and [validation and acceptance](08-validation-and-acceptance.md). Do not begin from a filename search and delete outward; prove replacement consumption first.

### The Score, and composing a cut

Read [the Score](17-the-score.md) (the one working surface; the timeline and Cut as lenses; the Cut composes a *take*; every projection reads it — "has one cut"), then [the beat and its arrangements](14-the-beat-and-its-arrangements.md) (the beat anatomy and the take it fires) and [animating truth](12-animating-truth.md) (how the read is felt). Anything the writer sees or operates is also governed by [the stage presents the act](18-the-stage-presents-the-act.md). The Cut is not a return of the retired patch-graph canvas — it is a lens and a second lane of the one surface.

### Visual, UI, or design work

Read [the stage presents the act](18-the-stage-presents-the-act.md) first — it is the enforceable floor (the act is the star; the glasses test for type and hit targets; progressive disclosure; one act in focus; relationships drawn, not implied; verify by *looking* in light and dark). Then [animating truth](12-animating-truth.md), [the Score](17-the-score.md), and the specific surface's chapter. A machine-readable accessibility tree is the necessary but never sufficient half of accessibility; passing it is not passing legibility.

### Copilot implementation

Read the [target architecture](04-target-architecture.md), [Grounding contract](05-grounding-contract.md), the [Copilot implementation extension](10-copilot-implementation-extension.md), and [the situated Copilot](15-the-situated-copilot.md), then follow chapter 10's mandatory discovery procedure before editing. Work that places the Copilot on a surface, or changes what she says when she arrives, is governed by chapter 15 and must satisfy its acceptance as well. The Copilot must reuse existing application operations and the same authority chain; it is not a second workflow engine. The behavioural, relaunch, and no-index acceptance cases in [validation and acceptance](08-validation-and-acceptance.md) apply.

### Model lanes, cost, and cloud escalation

Read [on-device first, and the writer's key](20-on-device-first-and-the-writers-key.md) — the on-device model is the default that must work on its own; cloud is a widening the **writer grants in dialogue**, never the app's automatic default; the escalation offer is **reasoned on-device over the uncertainty map**, never a hard-coded lane table. It is governed together with [the situated Copilot](15-the-situated-copilot.md) (the opener names the true elected lane and cost before spending).

### Training the on-device model to the writer's work

Read [training perspectives](21-training-perspectives.md) — a trained LoRA adapter is a **perspective** (a lens learned from the writer's material), authored by intent, adopted only on evidence (shadow comparison + eval gate), legible, and reversible; it is the **on-device path to quality**, the sibling axis to [on-device first, and the writer's key](20-on-device-first-and-the-writers-key.md) (which governs the lane and cloud escalation).

### Preferences, settings, and configuration

Read [no preferences, only reasoning](22-no-preferences-only-reasoning.md) — Reframe has no panel where the writer configures *how the app decides*; the app **reasons** decisions in context and the writer **instructs it in dialogue**. The only stored settings are **facts** the app cannot reason into existence (credentials, storage location, account state), on a lean Accounts & Storage surface. It generalizes [ch.20](20-on-device-first-and-the-writers-key.md) (the lane) and [ch.21](21-training-perspectives.md) (training) into the rule both instance.

### Turn routing, intent classification, the Copilot's understanding of a turn

Read [one reasoning](23-one-reasoning.md) — a turn is understood by ONE reasoning over ONE complete taxonomy, and everything routes from that single decision; no speculative "fast" pre-classifier with a smaller vocabulary that fires first and misroutes, no cascade of `reflect*` passes racing to grab the turn. It is what makes [ch.20](20-on-device-first-and-the-writers-key.md)'s writer's-key recognition reachable and the sibling of [ch.22](22-no-preferences-only-reasoning.md) (no stored toggle for a decision; here, no fast pre-guess for the reasoning).

### Intent uncertainty, clarification, escalation signal

Read [the reasoning is an uncertainty map](24-the-reasoning-is-an-uncertainty-map.md) — the one reasoning ([ch.23](23-one-reasoning.md)) produces an **uncertainty map** over what the writer could want (settled / ambiguity / thin / failure + why + what would resolve it), not a scalar confidence; the app routes from it (settled→dispatch, ambiguity→clarify, failure→fail visibly), it is the signal the writer's-key escalation ([ch.20](20-on-device-first-and-the-writers-key.md)) reads, and it is inspectable/showable (UncertaintyScoreKit / FCIS-AX). This is also *why* the one reasoning can run lean.

### UncertaintyScoreKit UX, arbitrary ledger lanes, and Reframe binding

Read [a want is a gap in a ledger](33-a-want-is-a-gap-in-a-ledger.md) first — it makes the ledger collection open-ended and explains why a lane is only a ledger's drawing, never a fixed kind of doubt. Then read [every gap keeps its address](36-every-gap-keeps-its-address.md): the arbitrary-lane rack, shared-spine map, composite lane/note selection, stable selected-thread account, generic-kit/Reframe boundary, and the rule that chat records collaboration around the map rather than becoming its only state surface. Visual implementation is also governed by [the stage presents the act](18-the-stage-presents-the-act.md), [Apple's Human Interface Guidelines](19-apple-human-interface-guidelines.md), and FCIS-AX.

### Code review

Read [current state and refactoring problem](03-current-state-and-problem.md), the relevant target contract, and the phase exit criteria in the [refactoring program](06-refactoring-program.md). A review should reject dual authority, hidden index reads, numeric context shaping, or readiness claims that are not persisted.

### `.claude` and `.codex`

Read the [agent operating guide](07-agent-operating-guide.md) first, then follow the task-specific path above. The guide explains authority precedence, planning discipline, evidence expectations, and the rule that historical documentation is never operational state.

## Chapter catalogue

| Chapter | Purpose |
| --- | --- |
| [Abstract](00-abstract.md) | Compact statement of the decision and completion condition. |
| [Development history](02-development-history.md) | The architectural eras, retained lessons, and superseded assumptions. |
| [Current state and problem](03-current-state-and-problem.md) | What the runtime does now and where index authority still leaks through. |
| [Target architecture](04-target-architecture.md) | Stage ownership, data flow, authority boundaries, and final invariants. |
| [Grounding contract](05-grounding-contract.md) | The persisted profile, identity rules, prompt relationship, and invalidation semantics. |
| [Refactoring program](06-refactoring-program.md) | Ordered implementation phases, affected seams, deletion gate, and exit criteria. |
| [Agent operating guide](07-agent-operating-guide.md) | Instructions for `.claude`, `.codex`, and human collaborators. |
| [Validation and acceptance](08-validation-and-acceptance.md) | Required unit, integration, store, UI, live-provider, and negative evidence. |
| [Compatibility and evolution](09-compatibility-and-future-evolution.md) | Legacy-store policy, archival behavior, rollback, and rules for future extensions. |
| [Copilot implementation extension](10-copilot-implementation-extension.md) | Extends the refactor to the conversational Copilot: perception, retrieval, action parity, discovery procedure, and acceptance. |
| [Grounding as a given](11-grounding-as-a-given.md) | Refines the Grounding authoring model: a canonical manifesto shipped as the default given, auto-confirmed on import, edited centrally as prose, never model-dissected. |
| [Animating truth](12-animating-truth.md) | Perceived performance: never sign a wait with a spinner. Render the frame and cheap/cached truth instantly; foreshadow the unknown as honest, animated structure whose motion maps to real work. Nothing that is not the manuscript may delay the manuscript; absence may not overwrite a truth already held; a click lands in its destination. |
| [App-flow record](reframe-app-flow-governance.md) | The complete prose account of how the app must flow end to end — the single continuous narrative these numbered chapters refine. |
| [Storage and performance](13-storage-and-performance.md) | Locks the storage layering — document layer = plain-text bundle + single manifest; musical layer = MIDI 2.0 — and the performance doctrine: reads are fast architecturally (cache-first, one manifest, no serial fan-out), not by encoding. |
| [The beat and its arrangements](14-the-beat-and-its-arrangements.md) | One beat, three arrangements: a single widget anatomy whose only differing part is its measure; the take — one firing that renders the document and musical layers as siblings. **Its patch-graph canvas (rules 7–9) is superseded by chapter 17;** the beat anatomy and take are retained. |
| [The situated Copilot](15-the-situated-copilot.md) | One Copilot, differently placed: she perceives the arrangement hosting her and what is wired into the conversation there, opens in words that fit the place, offers nothing whose object the surface does not show, and states an empty situation rather than filling it. |
| [The timeline is the machine room](16-the-timeline-is-the-machine-room.md) | Making beats IS the machinery and the timeline is where it is seen: one machinery, one surface. No machine room, factory gate, engine view, run report, or heartbeat line; diagnostics may drive behaviour but never become a surface; unreachable surface is deleted, not kept. |
| [The Score](17-the-score.md) | The performance space of the work, and the ONE working surface: the timeline and Cut become lenses of it (the patch-graph canvas is retired); a lane is a participant, not a track; the beat/arc is the structural spine every participant is grounded to; protocol state (MIDI 2.0) is composition. Defines the minimum honest Score — grounded spine + one Text participant from the source — with the distributed multi-participant stage named as horizon, not increment. |
| [The Stage Presents the Act](18-the-stage-presents-the-act.md) | Legibility over density: a surface presents the ACT the writer is performing, not a console. Enforceable floor — the act is the largest/central element; the glasses test (min type + hit-target sizes); progressive disclosure of per-object machinery (no permanent hieroglyph rows); one act in focus at a time; relationships are DRAWN, not implied by a glyph; and every visual change is verified by LOOKING at the rendered view (light + dark), never by the accessibility tree alone (the machine-readable half is necessary, never sufficient). |
| [Apple Human Interface Guidelines](19-apple-human-interface-guidelines.md) | The HIG is Reframe's baseline visual/interaction standard — the floor beneath chapters 12/14/17/18, not an alternative. Adopts the specifics our chapters implied: system text styles (macOS Body = 13pt), contrast ratios (4.5:1 text / 3:1 controls / aim 7:1, verified in light, dark, AND Increase Contrast), 44pt hit targets where touch/accessibility reach, semantic system colours (never colour-alone, never hard-coded), the 8pt grid, system materials, purposeful motion that honours Reduce Motion, SF Symbols, VoiceOver. Reconciles each against our chapters, notes where Reframe is deliberately stricter (the no-spinner rule), and records the gaps to close (Reduce Motion, contrast audit, migrate hard-coded sizes/colours). |
| [On-Device First, and the Writer's Key](20-on-device-first-and-the-writers-key.md) | The on-device model is the FIRST lane — the default that must work on its own (a manuscript read, discussed, composed with no cloud at all). Cloud is a widening of perspective and the writer's money, so the **writer holds the key**: no cloud call without an explicit grant the writer gives/revokes **in dialogue** (default local-only). When on-device leaves real uncertainty, the Copilot may OFFER to escalate — a decision **reasoned on-device over the UncertaintyScoreKit map**, never a hard-coded `benefitsFromCloud`/preference-order table. Apple's on-device→Private Cloud Compute escalation, with the key in the writer's hand. Every surface names the ELECTED lane before spending; fail visibly, never silently spend or fabricate. |
| [Training Perspectives](21-training-perspectives.md) | A trained LoRA adapter is a **perspective** — a lens the on-device model wears, learned from the writer's own material, to read/write THEIR work better. The sibling axis to ch.20: not *which lane*, but *how the on-device lane gets better*, and the on-device path to quality (the alternative to cloud escalation). Authored **by intent** ("learn my voice from these scenes"; the app reasons the training plan, expert knobs behind disclosure), adopted **only on evidence** (readable shadow comparison + passed eval gate; a perspective that doesn't beat the base is rejected), **legible** (provenance: what it learned, from what, how it compared), and **reversible** (worn per role, base never mutated). Cloud training is gated by the writer's key (ch.20); fail visibly, never silently fall back to base as success. |
| [No Preferences, Only Reasoning](22-no-preferences-only-reasoning.md) | Reframe has **no preferences** — no panel where the writer configures *how the app decides*. A stored toggle for provider / reasoning-visibility / command-autonomy / guide-policy / model-tuning is a decision frozen into config, the anti-pattern ch.20/21 reject. The app **reasons** decisions in context; the writer **instructs in dialogue** (understood by meaning, scoped or standing, revisable, remembered *as* an instruction with provenance). The only stored settings are **facts** the app cannot reason into existence — credentials, storage location, account state — on a lean **Accounts & Storage** surface (a credential is a fact, not permission to spend — that is the writer's key, ch.20). No retired toggle becomes an unreachable hidden default; expert machinery is demoted behind disclosure, not deleted. Generalizes ch.20 (lane) + ch.21 (training) into the rule both instance. |
| [One Reasoning](23-one-reasoning.md) | A turn is understood by **one** reasoning over **one complete taxonomy** of what the writer can want, and **everything routes from that single decision**. No speculative "fast" pre-classifier with a smaller vocabulary (`FastRouteTargetG`) that fires first and grabs the turn; no cascade of standalone `reflect*` passes racing to be first. Multiple reasoners with divergent vocabularies disagree, and first-to-grab wins — which is how "stay on device" (turning the writer's key) became a segmentation, and content questions / "fix it" became reads. Retire the fast pre-pass and the competing reflections into one decision; the key-turn (`cloudGrant`) is a case in the one taxonomy, so it becomes reachable by construction. Cheap preconditions (deterministic guards) are fine; a second *model reasoning* over intent is not. If the one reasoning is too slow, make IT lean — never front it with a lossy guesser. Sibling of ch.22 (no stored toggle for a decision; here, no fast pre-guess for the reasoning). |
| [The Reasoning Is an Uncertainty Map](24-the-reasoning-is-an-uncertainty-map.md) | The product of the one reasoning (ch.23) is an **uncertainty map** over what the writer could want — per-intent state (**settled / ambiguity / thin / failure**) + reason + `resolvedBy` — not an opaque verdict or scalar confidence. Route from it: settled→dispatch, ambiguity→**clarify** (ask, don't guess), thin→proceed/offer, failure→**fail visibly** (a window overflow is a loud failure, never a segmentation). Ambiguity (a real two-way split) and failure (a breakdown) are different in kind. This is *why* the reasoning can run lean — it needs only the taxonomy + message + minimal state, never the execution manifest (that loads in the dispatched producer). The map is the signal ch.20's writer's-key escalation reads (thin/failure whose resolution is a stronger model → offer to widen), and it is inspectable/showable via UncertaintyScoreKit + FCIS-AX so the writer decides on real evidence. Fuses ch.23 (one reasoning) + ch.20 (the key) + UncertaintyScoreKit into one law: the reasoning's product is an inspectable map of doubt, and the app acts from it. |
| [The CoPilot Is the Surface](25-the-copilot-is-the-surface.md) | Every capability that was a panel, editor, or toggle **lives in the CoPilot as dialogue**: the CoPilot **teaches** the writer the capability (they don't arrive knowing "grounding," a "reader lens," a "trained perspective"), **states** its current value in plain language, is **instructed** to change it by meaning (scoped/standing, revisable), and **shows the effect** on the work. The constructive half of ch.22: retiring a panel is not enough — the capability must *re-appear in conversation*, taught and held there, or it's a lost capability. Persistence is **invisible plumbing** — the writer never hears "saved," "stored," "Preferences," or "confirm." Instances: the key (ch.20), perspectives/LoRA (ch.21), preferences (ch.22), and **grounding/lenses (new — retire the baseline/grounding editor; the writer changes the lens by asking and the beats re-form)**. Onboarding is mandatory and in-context; expert machinery is demoted behind maintainer disclosure, never taught to the writer. |
| [Internals Tune Themselves](26-internals-tune-themselves.md) | The default disposition of any internal is **reasoned** — Reframe decides it **dynamically, in context, at the moment it matters** (output caps, routing, storify window, retries, budgets, reading shape) and can explain it; there is no setting. The writer meets a control **only when their judgment is genuinely needed** (a stance, a spend, a voice, a training intent), and then the **CoPilot surfaces it contextually**, teaches it, and asks — never a standing toggle. Turns ch.22 (no preferences) + ch.25 (CoPilot is the surface) into a **disposition procedure** (fact → reasoned → dialogic → maintainer → plumbing) and applies it to an audit of all **73** persisted settings. End state: Preferences collapses to a lean Accounts & Storage + Integrations surface plus a maintainer-only Developer disclosure — no routing panel, no tuning, no LoRA knob wall on the writer's path. Facts stay; reasoned values self-tune + stay explainable; genuine decisions go dialogic; maintainer machinery hides behind disclosure; runtime/learned state is never dressed as config. |
| [Parse Before You Ask](27-parse-before-you-ask.md) | Structure is parsed, meaning is read, and local non-generative tools measure what they can establish without invention; a higher reasoning is never asked what a lower tier can answer. |
| [A Beat Is the Question It Raises](28-a-beat-is-the-question-it-raises.md) | A beat is the span over which one story question remains open; atoms are local reading units and never promoted into named beats. |
| [NaturalLanguage Measures, Storify Interprets](29-natural-language-measures-storify-interprets.md) | Measurement supplies candidates, coordinates and contradictions; only the reading interprets meaning or assigns uncertainty state. |
| [The Living Gazetteer](30-the-living-gazetteer.md) | The evidenced, revisable account of what the source has established to exist; it remembers the world without routing, judging, or silently filling its holes. |
| [Compiled Knowledge](31-compiled-knowledge.md) | Hard, durable reasoning is compiled into evidenced project memory so the local lane improves for this work without pretending the model itself learned the world. |
| [Referenced Knowledge](32-referenced-knowledge.md) | Knowledge outside the manuscript is retrieved rather than recalled, cited with the source's own words, and promoted only by the writer. |
| [A Want Is a Gap in a Ledger](33-a-want-is-a-gap-in-a-ledger.md) | Uncertainty is collected from arbitrary registered ledgers; every gap carries a typed want naming who can close it, and a missing ledger reports failure rather than disappearing. |
| [A Question That Leaves the Work](34-a-question-that-leaves-the-work.md) | An outward question carries its work, measured doubt and bounded source passages; generated prose is discarded while fetched documents remain auditable. |
| [Deep Search](35-deep-search.md) | A cited page begins the source reading; justified local reasoning follows source-internal links, records every reason, and states exactly why the search stopped. |
| [Every Gap Keeps Its Address](36-every-gap-keeps-its-address.md) | The UI consequence of arbitrary ledgers: every gap keeps a composite lane/note address across an arbitrary-lane rack, shared-spine map, manuscript, typed want, evidence and decision. The kit remains generic; Reframe supplies domain context; complexity is represented at synchronized scales rather than flattened into fixed lanes or expanding chat cards. |

## Vocabulary

**Canonical source** means the imported manuscript stored under the source document identity. It is evidence, not a work surface for generated analysis.

**Grounding Profile** means the writer-confirmed policy document that directly governs downstream interpretation. It is not a summary of the source.

**Storify Source Auto** means the chapter-aware structural reading that converts source atoms into kept/noise decisions, beats, uncertainty, synopsis, and arcs.

**Cut Script** means the mutable, authored draft product assembled from chosen Storify units and later composition.

**Continuity** means the audit over Cut Script or other explicitly selected units. It is not a substitute source reader.

**Legacy semantic artifacts** means index passages, reading states, semantic memory, published semantic objects, repair debt, and index performance memory created before this refactor. They may remain inspectable, but they have no authority in the final pipeline.
