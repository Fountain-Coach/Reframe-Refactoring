# Copilot Capability Audit Skill — From Boundary to Empowerment

> Chapter summary: Chapter 37 defines the honest Copilot boundary. This chapter defines the repository-tracked skill system that audits that boundary, implements the next capability, proves it in the running application, and publishes the evidence without confusing code presence with empowerment.

## The decision

Copilot widening is a governed loop, not a sequence of prompt edits. The
registry remains authoritative for identity and declared exposure; live runtime
state, FountainStore, telemetry, AX, focused tests, and live acceptance supply
the evidence. The skill suite makes that loop repeatable for both Codex and
Claude.

`.codex/skills` is the canonical repository-local skill source. `.claude/skills`
is its synchronized mirror. Global user installation is outside this contract.
`Scripts/sync-agent-skills --check` must pass before a skill is described as
available to both agents.

## The complete skill suite

The skills are deliberately complementary rather than capability-specific:

| Skill | Responsibility |
| --- | --- |
| `copilot-capability-audit` | Read the v2 registry and maintain the empowerment and gap ledger. |
| `copilot-capability-implement` | Build one unavailable capability through adapter, policy, tests, proof, telemetry, AX, and exposure. |
| `copilot-capability-live-acceptance` | Drive the full origin × provider × consent × outcome matrix. |
| `fountainstore-proof-audit` | Verify lifecycle records, persisted effects, and terminal proof. |
| `copilot-provider-acceptance` | Prove provider routing, paid consent, refusal, failure, retry, and correlation. |
| `generated-contract-regeneration` | Regenerate and byte-compare Swift, manifest, facts, and capability projections. |
| `swift-failure-triage` | Separate capability regressions from fixture, provider, AX, and baseline failures. |
| `ax-surface-audit` | Verify semantic accessibility state, actions, progress, cancellation, resume, and result. |
| `docs-sync` | Keep the publication guide and integration counterpart identical with explicit direction. |
| `governance-publish` | Run validation, provenance, commit, push, and review publication. |

Existing domain skills (`live-drive`, `modernization-studio-ops`, `repo-ops`,
and related build/evaluation skills) remain the execution primitives. The new
suite composes them; it does not replace them.

## The authority and status model

The audit skill reads `schema/modernization-studio-capabilities.json` first,
then checks generated contract, runtime owners, exposure, tests, and the
closure ledger. It derives only these statuses:

- **executable-not-live-accepted** — an adapter and policy exist, but required
  live evidence is absent;
- **unavailable-adapter-proof** — the registry intentionally blocks the row
  because its governed adapter and proof path are missing;
- **live-accepted** — AX, FountainStore, telemetry, terminal proof, and all
  required origin/provider/consent scenarios are recorded; and
- **contract-drift** — registry, generated contract, exposure, or runtime
  binding disagrees and must be repaired before exposure.

The current audit reports 43 registry identities: 9 executable, 34
unavailable, 0 live-accepted, and 0 drift findings. Those counts describe the
evidenced boundary, not the full application surface.

## The widening workflow

1. **Audit.** Run `python3 .codex/skills/copilot-capability-audit/scripts/audit.py`.
   Review `docs/copilot-capability-audit.md` and
   `docs/copilot-capability-closure.json`.
2. **Select.** Choose one bounded unavailable row, record its dependency and
   owner, and create a plan entry. Do not select by prompt demand alone.
3. **Implement.** Use `copilot-capability-implement` to add the typed adapter,
   centralized policy, exhaustive operation mapping, and focused tests.
4. **Regenerate.** Use `generated-contract-regeneration`; byte-compare tracked
   Swift and manifest artifacts and check parity in both directions.
5. **Prove persistence.** Use `fountainstore-proof-audit` to verify ordered
   v2 lifecycle events, observed effects, terminal proof, and telemetry
   correlation. v1 receipts remain historical dispatch records.
6. **Audit AX.** Use `ax-surface-audit` to verify identifiers, roles, labels,
   values, progress, cancel/resume, Reduce Motion, and terminal result.
7. **Drive live.** Use `copilot-capability-live-acceptance` and
   `copilot-provider-acceptance` for every applicable origin, placement,
   provider, consent, failure, cancellation, and resume case. Use `live-drive`
   for the external-display AX/window-ID procedure.
8. **Record.** Update the closure ledger with adapter, test, store, telemetry,
   AX, provider, and live evidence. Only now may the row become
   `live-accepted` and teaching be exposed.
9. **Publish.** Use `docs-sync` for publication/integration parity and
   `governance-publish` for clean provenance, review, and release.

## Closure row and evidence contract

Every capability row must identify:

1. native adapter and policy owner;
2. decoding, policy, origin-parity, failure, and proof-gating tests;
3. natural-language, slash, and button scenarios where exposed;
4. provider, consent, cost, failure, cancellation, and resume outcomes;
5. FountainStore proof/document IDs and verified effects;
6. telemetry correlation IDs;
7. AX projection and terminal-result evidence; and
8. owner, implementation commit, live scenario, and next step.

A request is not a start until `running` is persisted. A result is not a
success until terminal proof is verified. An unavailable request must refuse
explicitly, remain absent from teaching, and perform no unverified mutation.

## Cross-agent synchronization

The synchronizer mirrors every Codex skill package, including `SKILL.md`,
metadata, and resources, while preserving Claude-only skills:

```sh
Scripts/sync-agent-skills --sync
Scripts/sync-agent-skills --check
```

Matching packages are canonical mirrors, so drift is a failure rather than an
implicit choice. A skill is available to both agents only when the check is
green and both copies pass structural validation.

## Completion rule

The suite is successful when it can answer from tracked artifacts, without
inference:

1. What can Copilot do now?
2. Why is each remaining capability unavailable or unaccepted?
3. What exact implementation and acceptance work widens the next capability?

Full governance closure requires every exposed capability to be live-accepted
and every remaining identity to be accepted or explicitly unavailable with a
current reason. Until then, the audit ledger and this chapter are the honest
status record.
