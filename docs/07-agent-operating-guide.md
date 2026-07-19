# Operating Guide for `.claude` and `.codex`

> Chapter summary: This chapter tells coding agents how to interpret authority, plan work, retrieve evidence, implement phase-sized changes, and avoid the characteristic failure modes of this refactor.

This directory is written for both human maintainers and coding agents. `.claude` and `.codex` should treat it as the authoritative intent for the Grounding-first refactor, while still obeying the repository's higher operational precedence.

## Authority and reading order

Before acting, read the root `AGENTS.md` and `apps/modernization-studio/AGENTS.md` completely. Then read this suite's [abstract](00-abstract.md), the task-relevant chapter selected through the [reading index](01-reading-index.md), and the current phase in [the refactoring program](06-refactoring-program.md).

Operational reasoning follows the repository contract: IDL and facts, live FountainStore state, root and scoped agent guidance, generated reasoning orientation, then plans and prose documentation as citations. This guide defines the target refactor but cannot make unimplemented behavior true. When guide and code differ, describe code as current state and the guide as required migration.

Do not use `ClusterKnowledge`, old screenshots, historical README prose, or prior plan language to override current contract or store truth. The repository contains several generations of Reframe architecture; chronology is context, not authority.

## Planning discipline

Every implementation phase is multi-step and high risk. Create or update `PLANS.md` before editing code. State the phase goal, precise scope, non-goals, identities affected, migration behavior, risks, and validation commands. Do not combine direct Grounding, readiness replacement, UI deletion, runtime deletion, and manifest regeneration into an unreviewable sweep.

At the beginning of a phase, rediscover consumers with `rg`. Search symbols, document prefixes, user-facing language, capability gates, tests, config keys, and generated artifacts. The source tree may have moved since this guide was written. Prefer semantic ownership over filename familiarity.

## Replacement before deletion

Never delete an index producer merely because a new Storify path exists. First prove every consumer has a replacement. A valid deletion change includes negative evidence: searches showing no live callers, tests proving no store reads, and a no-index end-to-end path.

Do not preserve the old system behind an indefinite fallback. Temporary comparison seams are acceptable only while their removal phase and exit criteria are recorded. The final state has one structural source reader.

## Grounding implementation rules

Grounding fields express meaning, not token inventory. Do not clamp, cap, truncate, tail-drop, or rank them by numeric fit. Numeric observations may be telemetry only. When a provider's physical context cannot carry a safe relevant Grounding context, retrieve a more explicit phase field, mediate semantically, ask the writer, or fail visibly.

Do not infer natural-language Grounding meaning with regexes, phrase lists, or exact wording matches. Structured identifiers and explicit command grammar may be parsed deterministically; writer meaning must pass through grounded reasoning.

Persist confirmation and identity in FountainStore. Do not introduce a UI-only “confirmed” flag, a global singleton as authority, or HTTP access when native store access is available.

## Storify implementation rules

Source atoms remain factual authority. Grounding shapes salience and permitted transformation. A prompt or validator must never allow Grounding to invent events, characters, or source relationships.

Preserve window tracking, resume tokens, telemetry, provider provenance, budgets, retries, backfill, and visible unreadable results. Removing indexing is not permission to weaken runtime accountability.

Disable both index inputs when testing independence: derived beats and semantic-memory priors. A test that disables only `storifyReportFromReading` does not prove Storify is index-free.

## Editing and repository hygiene

Use `apply_patch` for hand-edited files. Preserve unrelated dirty-worktree changes. Do not destructively delete legacy store data, reset the repository, or rewrite historical plans. When removing source files, resolve exact targets and confirm they contain no shared types before deletion.

When the IDL, facts, roles, agent guidance, capability overlay, or reasoning-manifest sources change, regenerate the tracked reasoning artifacts before considering the repository consistent. MCP may assist, but repository correctness must not depend on MCP availability.

## Validation behavior

Use focused tests during a phase and the full Modernization Studio suite at phase closure. Run build-only proofreader validation when UI or executable surfaces change. For provider behavior, use explicit opt-in live tests and report whether a skip was expected. Never present an unrun live path as measured.

Document commands and outcomes in `PLANS.md`. A green suite does not replace semantic review of source authority, Grounding influence, or persisted identity. Conversely, a broad unrelated warning in a dirty worktree is not permission to rewrite adjacent systems.

## Review questions

Before handing off any phase, answer these questions from evidence:

1. Which persisted artifact is authoritative now?
2. What exact identity invalidates it?
3. Can the same behavior recover after relaunch?
4. Did any index document, reading state, or published semantic object influence the result?
5. Did Grounding reach the intended Storify request without numeric semantic loss?
6. Did source evidence remain authoritative?
7. Are failure, uncertainty, and stale state visibly distinct?
8. Do capabilities, generated reasoning orientation, UI language, and runtime agree?
9. What transition code remains, and in which recorded phase will it be removed?

An agent should not claim a phase complete until each applicable answer is explicit.
