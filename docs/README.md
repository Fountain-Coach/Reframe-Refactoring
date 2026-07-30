# Reframe Grounding-First Refactoring Guide

> Chapter summary: This landing page identifies the authority, purpose, and safe reading order of the documentation set that governs Reframe's working surface — a set that began as the move away from semantic indexing (chapters 00–11) and grew, through implementation, into the doctrine of the one surface it left behind: the Score and how it must read (chapters 12–18).

Status: authoritative design and refactoring directive (a living guide)
Published: 2026-07-19 · continuously extended as chapters are earned in the code
Applies to: `apps/modernization-studio` (the Reframe application)
Audience: Reframe maintainers, product engineers, reviewers, designers, `.claude`, and `.codex`

Dedicated GitHub repository: [Fountain-Coach/Reframe-Refactoring](https://github.com/Fountain-Coach/Reframe-Refactoring)
Integration source: [`Fountain-Coach/midi2-gpu-fabric/apps/modernization-studio/docs/reframe-grounding-first-refactor`](https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor)

This directory began as the guide for one architectural transition — semantic indexing and the index-built Manuscript Guide leave the production pipeline, confirmed Grounding becomes the direct downstream policy contract, and Storify Source Auto becomes the sole structural reader of the canonical source (chapters 00–11). That founding decision still holds. Implementing it surfaced the deeper doctrine of the surface that remains — one performance space (the Score), the beat and its take, the situated Copilot, and how the surface must read to a human — stated in chapters 12–18. The [root README](https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/README.md) tells the full genesis and arc.

The dedicated repository is the publication and FCIS-governance home for this guide. This directory is its integration copy beside the Reframe implementation. A documentation change is maintained only when the two copies agree; the dedicated repository contains the synchronization procedure and provenance record.

The guide is authoritative about the intended design. It does not pretend the work has already happened. Until a chapter's doctrine is implemented and validated, live code, live FountainStore state, the MIDI backplane contract, and the generated reasoning manifest remain the truth about current behavior. The precedence rules in the root and app-scoped `AGENTS.md` files always apply.

## Start here

Read the [abstract](00-abstract.md) for the founding decision in compact form, then use the [reading index](01-reading-index.md) to choose a route — it carries role-based paths for both humans and agents, and now covers the working-surface chapters (Score, cut, visual) as well as the original transition.

For the Grounding-first transition, the minimum safe sequence is:

1. [Development history and retained lessons](02-development-history.md)
2. [Current state and refactoring problem](03-current-state-and-problem.md)
3. [Target architecture](04-target-architecture.md)
4. [Extended Grounding contract](05-grounding-contract.md)
5. [Refactoring program](06-refactoring-program.md)
6. [Agent operating guide](07-agent-operating-guide.md)
7. [Validation and acceptance](08-validation-and-acceptance.md)
8. [Compatibility and future evolution](09-compatibility-and-future-evolution.md)
9. [Copilot implementation extension](10-copilot-implementation-extension.md)
10. [Grounding as a given — the canonical manifesto](11-grounding-as-a-given.md)

For the working surface — the Score, composing a cut, and how it must look — read [the Score (17)](17-the-score.md), [the beat and its arrangements (14)](14-the-beat-and-its-arrangements.md), [animating truth (12)](12-animating-truth.md), [the stage presents the act (18)](18-the-stage-presents-the-act.md), and [Apple's Human Interface Guidelines (19)](19-apple-human-interface-guidelines.md) — the platform baseline (system text styles, contrast, hit targets, Reduce Motion) beneath our visual doctrine. The [reading index](01-reading-index.md) gives the task-specific routes.

For **model lanes, cost, and cloud escalation**, read [on-device first, and the writer's key (20)](20-on-device-first-and-the-writers-key.md): the on-device model is the default that must work on its own, cloud is a widening the writer grants in dialogue (never the app's automatic default), and the escalation offer is reasoned on-device over the uncertainty map — never a hard-coded lane table.

For **training the on-device model to the writer's work**, read [training perspectives (21)](21-training-perspectives.md): a trained LoRA adapter is a *perspective* (a lens learned from the writer's material), authored by intent, adopted only on evidence, legible, and reversible — the on-device path to quality, the sibling axis to ch.20's lane escalation.

For **preferences, settings, and configuration**, read [no preferences, only reasoning (22)](22-no-preferences-only-reasoning.md): Reframe has no panel where the writer configures how the app decides — the app reasons decisions in context and the writer instructs it in dialogue; the only stored settings are facts the app cannot reason into existence (credentials, storage, account state), on a lean Accounts & Storage surface. It generalizes ch.20 and ch.21 into the rule both instance.

For **turn routing and intent classification**, read [one reasoning (23)](23-one-reasoning.md): a turn is understood by one reasoning over one complete taxonomy, and everything routes from that single decision — no speculative "fast" pre-classifier with a smaller vocabulary that fires first and misroutes. It is what makes ch.20's writer's-key recognition reachable, and the sibling of ch.22.

For **intent uncertainty, clarification, and the escalation signal**, read [the reasoning is an uncertainty map (24)](24-the-reasoning-is-an-uncertainty-map.md): the one reasoning produces an uncertainty map (settled / ambiguity / thin / failure + why + what would resolve it), not a scalar guess; the app routes from it (dispatch / clarify / fail visibly), it is the signal ch.20's writer's-key escalation reads, and it is inspectable/showable via UncertaintyScoreKit — which is also why the reasoning can run lean.

For **what may be asked of a model at all**, read [parse before you ask (27)](27-parse-before-you-ask.md): structure is parsed, meaning is read, and between them sits local non-generative tooling (named entities, part of speech, sentence boundaries, sentence embeddings) that measures without being able to invent. A question a lower tier can answer is never put to a higher one — the manuscript's own declarations are shown before the reading starts, and what will not parse is marked rather than smoothed. It is the substrate beneath ch.23's one reasoning and ch.24's uncertainty map: both get cheaper and more honest as the parse grows.

For **what a beat IS**, read [a beat is the question it raises (28)](28-a-beat-is-the-question-it-raises.md): a beat is the stretch of story over which one question stays open, found in one forward pass and named by that question; an atom is the reader's local unit — a minute of performance cut at the text's own seam — and is never called a beat nor given a name. Measured on the whole of Telemachus. It fixes the identity ch.14 arranges and shows, and it is why ch.27's parse comes before any model is asked anything.

For **how far the measuring may go**, read [NaturalLanguage measures, Storify interprets (29)](29-natural-language-measures-storify-interprets.md): the framework answers where the text is, what literal form appears there, what resembles it, what changed, and which model claim the text does not support — and never what the story means. Its output is candidates and coordinates, confirmed by the reading or not at all; it may supply REASONS to ch.24's map but never a status, a lane or a turn's target. It is ch.27 read in the other direction: never ask a model what a measurement answers, and never let a measurement answer what only a reading can.

For **what the work's world remembers**, read [the Living Gazetteer (30)](30-the-living-gazetteer.md): the continuously accumulating record of what the source has established to EXIST — candidates observed by ch.29, confirmed by the reading, held with their provenance and their history, revisable by the writer in a sentence. It is consulted before every later reading and asked nothing: it routes no turn, sets no status, answers no story question, which is exactly what separates it from the semantic index this refactor removed. Measured on Telemachus: 28 names in and 28 identities out is a world nobody has worked out yet, and the state in which a reading invents a conflict between Stephen and Dedalus.

For **why any of it accumulates**, read [Compiled Knowledge (31)](31-compiled-knowledge.md): the on-device ambition is not a model problem. Frontier reasoning is demoted from RUNTIME to KNOWLEDGE COMPILER — asked the hard, durable questions rarely, and what it settles is compiled into evidenced, revisable project memory the local lane executes against forever after, so the app grows better at THIS manuscript without its model changing. Models learn language; projects remember worlds; the writer owns the world's memory. The Gazetteer (30) is the first artefact of the family and the bar for joining it: authored, evidenced, falsifiable, historied, removable, narrowly invalidated — and never routing a turn, gating a step, deciding meaning or authorising a spend. Measured: a name the reading confirmed was invisible to the instrument on the next read until the world was compiled back into it.

For **knowledge that is not in the book**, read [Referenced Knowledge (32)](32-referenced-knowledge.md): some things a manuscript needs known are not in it — measured, a full reading of Telemachus holds Kinch and Stephen Dedalus as two people, both correctly evidenced, and they are one man, because the chapter never says so and Gifford's annotations do. So a third kind of evidence is admitted and governed: a REFERENCE, cited well enough for a doubting reader to follow. Its first rule is the answer to the question every student asks about AI and citation — references are RETRIEVED, never RECALLED: a model may say what kind of source would settle a question, never produce the source from memory, because an invented citation states something false in the register of things that have been checked. A citation carries its work, its locator and the quotation that bears the claim; the text still wins about what the text contains; scholarship that disagrees is recorded beside, not instead; and the writer stops being the CURATOR of the world's knowledge and becomes its arbiter of last resort — asked to settle a presented disagreement, never to supply what could have been retrieved.

For **how the app knows it needs to look anything up at all**, read [A Want Is a Gap in a Ledger (33)](33-a-want-is-a-gap-in-a-ledger.md): uncertainty about the world is not a list of axes somebody enumerated — it is a function of the ledgers the work keeps and the gaps in them. Measured: the identity axis was designed, its data computed at real cost and passed in, and the projection dropped it on the floor, so the map reported no identity doubt at all — which renders identically to "identity is settled" over a reading that had Stephen and Kinch as two men in conflict. A design in which absence is unrepresentable keeps producing it, so a ledger now always answers, and one that is stale, broken or never built reports the loudest gap of all. Each gap carries a WANT, typed by who can answer it — the manuscript, a stronger reasoning, a source outside the work, or the writer — which is (32)'s order of resort made mechanical: a want of the third kind is the only thing that may reach for the web, and it authorises nothing without the writer's yes. This is what lets Kinch reach a source with no rule naming him, and it retires the resemblance detector that structurally never could.

## Governing sentence

Reframe shall read the source structurally once: Grounding determines the writer's declared intent, Storify reads the source under that intent, Cut Script owns authored output, and Continuity audits the result; no semantic indexing stage or index-derived authority remains in the final production path.
