# Reframe Refactoring — Agent Guide

Scope: the authoritative Grounding-first Reframe refactoring guide and its synchronization with the Reframe integration repository.

## Invariants

- The guide under `docs/` is the publication copy; the integration copy lives at `apps/modernization-studio/docs/reframe-grounding-first-refactor/` in `Fountain-Coach/midi2-gpu-fabric`.
- The publication and integration copies must not drift silently. Every content change names its counterpart commit or pull request.
- Historical behavior, current runtime behavior, and target architecture must remain explicitly distinguished.
- The canonical Reframe source remains factual authority; confirmed Grounding owns writer policy; Storify owns structural reading; Cut Script owns authored output; Continuity owns cross-unit audit.
- Numeric measurements may be telemetry only. They must not select, clamp, truncate, or rank semantic context.
- Repository correctness must not depend on MCP or another optional external capability.
- No secrets, prompts, manuscript content, or semantic artifacts belong in logs or repository telemetry.

## FCIS routing

- `AGENTS.md` contains invariants and routing only.
- Multi-step or high-risk changes require an entry in `PLANS.md` before edits.
- Synchronization procedures belong in `.codex/skills/docs-sync/SKILL.md` and supporting scripts.
- Runtime implementation work is routed to `Fountain-Coach/midi2-gpu-fabric` and its root and scoped `AGENTS.md` files.

## Authority

This repository is authoritative for refactoring intent and guide publication. It does not override the MIDI backplane IDL, live FountainStore state, or unimplemented runtime truth in the integration repository.
