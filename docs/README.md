# Reframe Grounding-First Refactoring Guide

> Chapter summary: This landing page identifies the authority, purpose, and safe reading order of the documentation set that directs Reframe away from semantic indexing and toward a Grounding-first Storify pipeline.

Status: authoritative refactoring directive
Published: 2026-07-19
Applies to: `apps/modernization-studio` (the Reframe application)
Audience: Reframe maintainers, product engineers, reviewers, `.claude`, and `.codex`

Dedicated GitHub repository: [Fountain-Coach/Reframe-Refactoring](https://github.com/Fountain-Coach/Reframe-Refactoring)
Integration source: [`Fountain-Coach/midi2-gpu-fabric/apps/modernization-studio/docs/reframe-grounding-first-refactor`](https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor)

This directory is the authoritative design and execution guide for one specific architectural transition: semantic indexing and the index-built Manuscript Guide are to leave the Reframe production pipeline, confirmed Grounding is to become the direct downstream policy contract, and Storify Source Auto is to become the sole structural reader of the canonical source.

The dedicated repository is the publication and FCIS-governance home for this guide. This directory is its integration copy beside the Reframe implementation. A documentation change is maintained only when the two copies agree; the dedicated repository contains the synchronization procedure and provenance record.

The guide is authoritative about the intended refactor. It does not pretend that the refactor has already happened. Until a migration phase is implemented and validated, live code, live FountainStore state, the MIDI backplane contract, and the generated reasoning manifest remain the truth about current behavior. The precedence rules in the root and app-scoped `AGENTS.md` files always apply.

## Start here

Read the [abstract](00-abstract.md) for the decision in compact form, then use the [reading index](01-reading-index.md) to choose a route through the remaining chapters.

For implementation work, the minimum safe sequence is:

1. [Development history and retained lessons](02-development-history.md)
2. [Current state and refactoring problem](03-current-state-and-problem.md)
3. [Target architecture](04-target-architecture.md)
4. [Extended Grounding contract](05-grounding-contract.md)
5. [Refactoring program](06-refactoring-program.md)
6. [Agent operating guide](07-agent-operating-guide.md)
7. [Validation and acceptance](08-validation-and-acceptance.md)
8. [Compatibility and future evolution](09-compatibility-and-future-evolution.md)
9. [Copilot implementation extension](10-copilot-implementation-extension.md)

## Governing sentence

Reframe shall read the source structurally once: Grounding determines the writer's declared intent, Storify reads the source under that intent, Cut Script owns authored output, and Continuity audits the result; no semantic indexing stage or index-derived authority remains in the final production path.
