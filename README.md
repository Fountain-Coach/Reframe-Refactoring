# Reframe Refactoring

The Fountain Coach publication and FCIS-governance home for the design and architectural doctrine of **Reframe** — the on-device screenwriting studio that reads a manuscript into a story structure and lets a writer compose from it.

This repository is a **living guide**, not a one-time spec. It is written to be read by both **humans** (maintainers, reviewers, designers) and **agents** (`.claude`, `.codex`): short, stable, numbered chapters, each stating enforceable doctrine for one part of the work, so a reader — of either kind — loads only what the task needs.

Start with the [abstract](docs/00-abstract.md), then use the [reading index](docs/01-reading-index.md) to pick a route.

## Genesis, and how the guide grew

The guide began (2026-07-19) as **one architectural transition**: remove semantic indexing from Reframe's production path, make confirmed **Grounding** the direct downstream policy contract, and make **Storify Source Auto** the sole structural reader of the canonical source. That founding decision still holds and is stated in chapters 00–11. Its governing sentence:

> Reframe shall read the source structurally once: Grounding determines the writer's declared intent, Storify reads the source under that intent, Cut Script owns authored output, and Continuity audits the result; no semantic indexing stage or index-derived authority remains in the final production path.

Implementing that transition surfaced deeper truths it *implied* but had not yet named — and the guide grew to state them, chapter by chapter, as they were earned in the code:

- **Grounding is a given** (11) — a settled manifesto edited as prose, never a gate.
- **Animating truth** (12) — never sign a wait with a spinner; the wait itself is the show.
- **Storage and performance** (13) — a plain-text document layer and a MIDI 2.0 musical layer; reads are fast by *architecture*, not by encoding.
- **The beat and its arrangements** (14) — one beat, three arrangements, and the *take* it fires.
- **The situated Copilot** (15) — one Copilot, differently placed, offering nothing whose object the surface does not show.
- **The timeline is the machine room** (16) — one machinery, one surface; no second-account diagnostics view.
- **The Score** (17) — the consolidated **performance space**: the ONE working surface, of which the timeline and the Cut are *lenses*; the Cut composes a **take**, and once fired that take is the root every projection reads ("has one cut").
- **The Stage Presents the Act** (18) — the enforceable **visual floor**: a surface presents the writer's act, large and legible (the *glasses test*), not a dense console — and UI is verified by *looking*, of which a machine-readable accessibility tree is the necessary but never sufficient half.
- **Apple's Human Interface Guidelines** (19) — the platform **baseline** beneath 12/14/17/18, not an alternative: it supplies the numbers our visual floor was guessing (system text styles — macOS Body = 13 pt; contrast 4.5:1 text / 3:1 controls / aim 7:1; 44 pt hit targets; semantic colours; the 8 pt grid; Reduce Motion) and records the gaps we still owe.
- **On-Device First, and the Writer's Key** (20) — the model-lane doctrine: the on-device model is the **first lane** (the default that must work on its own); cloud is a **widening of perspective** and the writer's money, so the **writer holds the key** (no cloud call without an explicit grant given/revoked *in dialogue*, default local-only); and the escalation *offer* is **reasoned on-device over the uncertainty map** ([UncertaintyScoreKit](https://github.com/Fountain-Coach/UncertaintyScoreKit)), never a hard-coded lane table. Apple's on-device→Private Cloud Compute escalation, with the key in the writer's hand.
- **Training Perspectives** (21) — the sibling axis to 20: not *which lane*, but *how the on-device lane gets better at this writer's work*. A trained LoRA adapter is a **perspective** — a lens the on-device model wears, learned from the writer's material — authored **by intent**, adopted **only on evidence** (shadow comparison + eval gate), **legible** (provenance), and **reversible** (base never mutated). The on-device path to quality; the alternative to escalating the lane.
- **No Preferences, Only Reasoning** (22) — the rule 20 and 21 both instance: Reframe has **no preferences panel** where the writer configures *how the app decides*. The app **reasons** decisions in context; the writer **instructs in dialogue** (understood by meaning, scoped or standing, revisable, remembered *as* an instruction). The only stored settings are **facts** the app cannot reason into existence — credentials, storage location, account state — on a lean Accounts & Storage surface. A credential is a fact, not permission to spend (that is the writer's key, ch.20).
- **One Reasoning** (23) — a turn is understood by **one** reasoning over **one complete taxonomy** of what the writer can want, and **everything routes from that single decision**. No speculative "fast" pre-classifier with a smaller vocabulary that fires first and grabs the turn; no cascade of standalone reflections racing to be first. Multiple reasoners disagree and first-to-grab wins — which is how "stay on device" (turning the writer's key) became a segmentation. Sibling of 22 (no stored toggle for a decision; here, no fast pre-guess for the reasoning); it makes ch.20's key-turn reachable by construction.
- **The Reasoning Is an Uncertainty Map** (24) — the *product* of the one reasoning (23) is an **uncertainty map** over what the writer could want — per-intent **settled / ambiguity / thin / failure** + reason + what would resolve it — not an opaque verdict. Route from it (dispatch / clarify / fail visibly; an overflow is a loud failure, never a segmentation). This is *why* the reasoning runs lean — a map needs only the taxonomy + message + minimal state, not the execution manifest. The map is the signal ch.20's writer's-key escalation reads, and it is inspectable/showable via [UncertaintyScoreKit](https://github.com/Fountain-Coach/UncertaintyScoreKit) + FCIS-AX, so the writer decides on real evidence. Fuses 23 + 20 + UncertaintyScoreKit into one law.

So the arc is legible: from **subtracting a stage** (remove indexing) → to naming the **one surface** that remains (the Score, a stage of participants grounded to a beat-spine) → to how that surface must **read to a human** (legibility over density) → to the **platform baseline** that legibility rests on (Apple's HIG) → to **which model does the work and who pays** (on-device first; the writer holds the escalation key) → to **how the on-device model gets better** at this writer's work (trained perspectives, authored and worn) → to abolishing the **preferences panel** entirely (the app reasons, the writer instructs; only facts are stored) → to reasoning about a turn **once**, over the whole space, with no fast pre-guess that can misroute it → to that one reasoning's product being an **inspectable map of doubt** the app acts from (routing, escalation, and transparency read the same map). Reframe's working surface is now governed here as one architectural *and* design doctrine.

The guide is authoritative about the *intended* design. It never claims the work is already done: until a chapter's doctrine is implemented and validated, **live code, live FountainStore state, the MIDI backplane contract, and the generated manifest remain the truth about current behavior.** The precedence rules in the root and app-scoped `AGENTS.md` always apply.

## The chapters

**Foundations — the Grounding-first transition (00–11)**

- [Abstract](docs/00-abstract.md) · the decision and completion condition, compact
- [Reading index](docs/01-reading-index.md) · role-based routes, chapter catalogue, vocabulary
- [Development history](docs/02-development-history.md) · the eras, retained lessons, superseded assumptions
- [Current state and problem](docs/03-current-state-and-problem.md) · where index authority still leaks
- [Target architecture](docs/04-target-architecture.md) · stage ownership, data flow, invariants
- [Grounding contract](docs/05-grounding-contract.md) · the persisted profile, identity, invalidation
- [Refactoring program](docs/06-refactoring-program.md) · ordered phases, the deletion gate, exit criteria
- [Agent operating guide](docs/07-agent-operating-guide.md) · precedence, planning, evidence for `.claude`/`.codex`
- [Validation and acceptance](docs/08-validation-and-acceptance.md) · required tests and negative evidence
- [Compatibility and evolution](docs/09-compatibility-and-future-evolution.md) · legacy stores, rollback, extension rules
- [Copilot implementation extension](docs/10-copilot-implementation-extension.md) · perception, retrieval, action parity
- [Grounding as a given](docs/11-grounding-as-a-given.md) · the canonical manifesto, auto-confirmed, edited as prose

**The working surface and its doctrine (12–19)**

- [Animating truth](docs/12-animating-truth.md) · perceived performance; foreshadow the unknown honestly
- [Storage and performance](docs/13-storage-and-performance.md) · document + musical layers; fast by architecture
- [The beat and its arrangements](docs/14-the-beat-and-its-arrangements.md) · one beat, three arrangements, the take
- [The situated Copilot](docs/15-the-situated-copilot.md) · one Copilot, differently placed
- [The timeline is the machine room](docs/16-the-timeline-is-the-machine-room.md) · one machinery, one surface
- [The Score](docs/17-the-score.md) · the ONE surface; lenses; the Cut composes a take; "has one cut"
- [The Stage Presents the Act](docs/18-the-stage-presents-the-act.md) · legibility over density; verify by looking
- [Apple's Human Interface Guidelines](docs/19-apple-human-interface-guidelines.md) · the platform baseline — text styles, contrast, hit targets, Reduce Motion

**Model lanes, cost, and cloud escalation (20)**

- [On-Device First, and the Writer's Key](docs/20-on-device-first-and-the-writers-key.md) · on-device is the default that must work alone; cloud is a widening the writer grants in dialogue; the escalation offer is reasoned on-device over the uncertainty map, never a hard-coded lane table
- [Training Perspectives](docs/21-training-perspectives.md) · a trained LoRA adapter is a *perspective* — a lens learned from the writer's material — authored by intent, adopted only on evidence, legible, reversible; the on-device path to quality
- [No Preferences, Only Reasoning](docs/22-no-preferences-only-reasoning.md) · no panel of behavioural toggles; the app reasons decisions and the writer instructs in dialogue; only facts (credentials, storage, account state) are stored, on a lean Accounts & Storage surface
- [One Reasoning](docs/23-one-reasoning.md) · a turn is understood by one reasoning over one complete taxonomy, and everything routes from that single decision; no fast pre-classifier that fires first and misroutes
- [The Reasoning Is an Uncertainty Map](docs/24-the-reasoning-is-an-uncertainty-map.md) · the one reasoning's product is an uncertainty map (settled/ambiguity/thin/failure + why + resolvedBy), not a verdict; route from it, escalate from it, show it — which is also why it runs lean

**The continuous account**

- [App-flow record](docs/reframe-app-flow-governance.md) · the end-to-end prose narrative these chapters refine

## Reading paths

Pick the row for your task; read those chapters, then retrieve live code and state for detail. Do not load the whole directory.

| If you are… | Read |
| --- | --- |
| Reviewing the architecture (human) | 00 → 02 → 04 → 17 (the arc, then where it now stands) |
| Implementing Grounding | 04 → 05 → 06 (phases 1–3) → 08 |
| Implementing Storify (the read) | 03 → 05 → 06 (phases 2–4) → 08 |
| Working on the Score / composing a cut | 17 → 14 → 12, then 18 for how it must look |
| Doing UI / visual / design work | 18 (the floor) → 19 (the platform baseline) → 12 → 17 → the specific surface's chapter |
| Placing or changing the Copilot | 10 → 15 (and its discovery procedure) → 08 |
| Working on model lanes / cost / cloud escalation | 20 (on-device first, the writer's key) → 15 (the opener names the lane) |
| Working on training / LoRA / adapters (perspectives) | 21 (training perspectives) → 20 (the sibling lane axis) → 17 (perspectives are lenses) |
| Working on preferences / settings / configuration | 22 (no preferences, only reasoning) → 20 + 21 (the cases it generalizes) |
| Working on turn routing / intent classification | 23 (one reasoning) → 24 (its product is an uncertainty map) → 20 (the key-turn it makes reachable) → 15 (the Copilot's understanding) |
| Working on intent uncertainty / clarification / escalation signal | 24 (the reasoning is an uncertainty map) → 23 (one reasoning) → 20 (the writer's key reads the map) |
| Deleting the index | all of 06 (esp. the deletion gate) → 07 → 08 |
| Reviewing code | 03 → the relevant target contract → 06 exit criteria → 18 (does the writer see it?) |
| An agent picking up any task | 07 first (precedence, evidence, planning), then the row above |

**For agents specifically:** authority precedence and evidence discipline live in [chapter 07](docs/07-agent-operating-guide.md). The guide is doctrine, not runtime truth — verify current behavior against live code and store. UI claims require *looking* at the rendered view (chapter 18), not only an accessibility-tree query.

## Source relationship

This guide is maintained as **one document set in two places**: here (the publication and FCIS-governance home) and beside the Reframe implementation in [`Fountain-Coach/midi2-gpu-fabric`](https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor). A documentation change is maintained only when the two copies agree; [SOURCE.md](SOURCE.md) records provenance and the synchronization contract.

## FCIS compliance

This repository follows FCIS RFC 0001 layering:

- `AGENTS.md` — scope, invariants, routing.
- `PLANS.md` — intent for multi-step or high-risk changes.
- `.codex/skills/docs-sync/SKILL.md` — the synchronization procedure.
- MCP is optional; correctness and synchronization do not depend on it.

See [FCIS_AUDIT.md](FCIS_AUDIT.md) and [FCIS_COMPLIANCE_PLAN.md](FCIS_COMPLIANCE_PLAN.md) for evidence and the maintenance checklist.
