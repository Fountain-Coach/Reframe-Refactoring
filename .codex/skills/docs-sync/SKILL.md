---
name: docs-sync
description: Compare or explicitly synchronize the Reframe refactoring guide between this publication repository and its midi2-gpu-fabric integration copy.
---

# Reframe Refactoring Documentation Sync

## Purpose

Maintain exact guide parity between this repository's `docs/` directory and `apps/modernization-studio/docs/reframe-grounding-first-refactor/` in a local `midi2-gpu-fabric` checkout while preserving reciprocal Git provenance.

## When to use

Use this skill whenever a guide chapter changes, source provenance is updated, or a release/PR claims that the publication and integration copies agree.

## Preconditions

- Read `AGENTS.md`, `PLANS.md`, and `SOURCE.md`.
- Resolve a local `midi2-gpu-fabric` checkout and its current branch/commit.
- Inspect both worktrees. Never overwrite unrelated changes.
- Add or update a `PLANS.md` entry for a multi-file synchronization.

## Procedure

1. Run the sync script in its default read-only comparison mode against the integration checkout.
2. Review every reported difference and decide which repository contains the intended content. Do not infer direction from timestamps.
3. Use `--pull` only to copy the integration guide into this repository. Use `--push` only to copy this repository's guide into the integration checkout. Both modes are explicit and replace the destination chapter set.
4. Run the read-only comparison again; it must report parity.
5. Validate relative Markdown links and repository formatting.
6. Commit changes separately in each repository. Record the counterpart repository, commit, or pull request in the PR description and update `SOURCE.md` when the publication baseline changes.

## Commands

```sh
Scripts/sync-integration-copy --check /path/to/midi2-gpu-fabric
Scripts/sync-integration-copy --pull /path/to/midi2-gpu-fabric
Scripts/sync-integration-copy --push /path/to/midi2-gpu-fabric
```

## Output contract

Report the synchronization direction, publication commit, integration commit or pull request, parity result, link validation, and any intentional divergence. Do not claim synchronization when either repository still has uncommitted guide differences.
