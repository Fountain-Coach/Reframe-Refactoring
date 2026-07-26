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

## Governing sentence

Reframe shall read the source structurally once: Grounding determines the writer's declared intent, Storify reads the source under that intent, Cut Script owns authored output, and Continuity audits the result; no semantic indexing stage or index-derived authority remains in the final production path.
