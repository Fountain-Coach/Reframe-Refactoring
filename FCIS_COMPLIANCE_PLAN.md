# FCIS Compliance Plan

## Goal and scope

Maintain compliance with FCIS RFC 0001 while publishing and synchronizing the Reframe refactoring guide. This repository has no application runtime; compliance focuses on governance layering, provenance, optional capabilities, and safe documentation maintenance.

## Required structure

The repository keeps behavioral invariants and routing in `AGENTS.md`, intent in `PLANS.md`, and synchronization procedure in `.codex/skills/docs-sync/SKILL.md`. `SOURCE.md` records the cross-repository authority relationship. The supporting script performs deterministic comparison or an explicitly directed transfer.

## Maintenance checklist

- Confirm `AGENTS.md` remains declarative.
- Confirm every multi-step change has a `PLANS.md` entry.
- Confirm procedures remain in skills and scripts.
- Compare `docs/` with the integration copy before publishing.
- Name counterpart commits or pull requests in both repositories.
- Keep MCP optional and avoid new dependencies.
- Keep prompts, manuscript content, semantic artifacts, and secrets out of the repository.
- Re-run the audit when repository structure or synchronization ownership changes.

## Status

Current status: COMPLIANT. See `FCIS_AUDIT.md` for evidence.
