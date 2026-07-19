# FCIS Audit

## Executive summary

Status: COMPLIANT

The repository separates declarative agent policy, implementation intent, and synchronization procedure. It introduces no runtime or MCP dependency and contains no application data.

## Repository inventory

- Invariants and routing: `AGENTS.md`
- Intent protocol and active history: `PLANS.md`
- Procedures: `.codex/skills/docs-sync/SKILL.md`
- Procedure implementation: `Scripts/sync-integration-copy`
- Publication guide: `docs/*.md`
- Provenance: `SOURCE.md`

## Compliance matrix

| Requirement | Status | Evidence | Maintenance rule |
| --- | --- | --- | --- |
| FCIS-AGENTS-1 | PASS | `AGENTS.md` contains scope, invariants, authority, and routing without command procedures. | Keep procedures in skills. |
| FCIS-PLANS-1 | PASS | `PLANS.md` exists and records goal, scope, risks, phases, and validation. | Update it before multi-step or high-risk changes. |
| FCIS-SKILLS-1 | PASS | `.codex/skills/docs-sync/SKILL.md` owns the synchronization runbook. | Extend or add skills when procedures change. |
| FCIS-LAYERS-1 | PASS | Policy, intent, and procedure are stored in distinct layers. | Reject duplicated runbooks in AGENTS or PLANS. |
| FCIS-MCP-1 | PASS | Comparison and synchronization use local Git and a repository script. | Keep MCP optional. |
| FCIS-PROVENANCE-1 | PASS | `SOURCE.md` records exact source repository, path, branch, commit, PR, and import date. | Update counterpart provenance with every publication. |
| FCIS-CONTENT-1 | PASS | Repository contains architectural documentation only; no prompts, manuscripts, or semantic artifacts. | Never add user content or inference logs. |

## Drift vectors

- A guide update lands in only one repository.
- Procedural synchronization commands move into `AGENTS.md`.
- A runtime implementation plan is mistaken for current operational truth.
- Historical architecture is silently rewritten instead of being superseded explicitly.

The sync skill, source contract, and pull-request counterpart rule mitigate these risks.
