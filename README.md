# Reframe Refactoring

Reframe Refactoring is the dedicated Fountain Coach publication and governance repository for the Grounding-first architectural transition in the Reframe application. The guide directs Reframe to remove semantic indexing, extend confirmed Grounding into the direct downstream policy contract, and make Storify Source Auto the sole structural reader of canonical source text.

Start with the [abstract](docs/00-abstract.md), then use the [reading index](docs/01-reading-index.md) to select a role-specific route through the guide.

## Documentation

- [Guide landing page](docs/README.md)
- [Development history](docs/02-development-history.md)
- [Current state and refactoring problem](docs/03-current-state-and-problem.md)
- [Target architecture](docs/04-target-architecture.md)
- [Extended Grounding contract](docs/05-grounding-contract.md)
- [Refactoring program](docs/06-refactoring-program.md)
- [Operating guide for `.claude` and `.codex`](docs/07-agent-operating-guide.md)
- [Validation and acceptance](docs/08-validation-and-acceptance.md)
- [Compatibility and future evolution](docs/09-compatibility-and-future-evolution.md)
- [Copilot implementation extension](docs/10-copilot-implementation-extension.md)
- [Grounding as a given — the canonical manifesto](docs/11-grounding-as-a-given.md)

## Source relationship

The guide is integrated beside the Reframe implementation in [`Fountain-Coach/midi2-gpu-fabric`](https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor). This repository is its dedicated publication and FCIS-governance home. The two copies are maintained as one document set; [SOURCE.md](SOURCE.md) records provenance and the synchronization contract.

The initial publication was sourced from `midi2-gpu-fabric` commit [`da22ba0c`](https://github.com/Fountain-Coach/midi2-gpu-fabric/commit/da22ba0c54e0fff6fb44f66182cecab0dd18759e) and is proposed for `main` through [midi2-gpu-fabric PR #8](https://github.com/Fountain-Coach/midi2-gpu-fabric/pull/8).

## FCIS compliance

This repository follows FCIS RFC 0001 layering:

- `AGENTS.md` contains scope, invariants, and routing.
- `PLANS.md` records intent for multi-step or high-risk changes.
- `.codex/skills/docs-sync/SKILL.md` contains the synchronization procedure.
- MCP is optional; repository correctness and synchronization do not depend on it.

See [FCIS_AUDIT.md](FCIS_AUDIT.md) and [FCIS_COMPLIANCE_PLAN.md](FCIS_COMPLIANCE_PLAN.md) for the compliance evidence and maintenance checklist.
