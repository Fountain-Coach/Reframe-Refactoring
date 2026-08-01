# Copilot Capability Audit Skill — From Boundary to Empowerment

> Chapter summary: Chapter 37 records what the governed Copilot boundary means. This chapter defines the repeatable skill that audits that boundary, maintains one closure ledger, and plans the work required to widen Copilot toward the full capability registry without confusing code presence with empowerment.

## Why the skill exists

The application surface, capability registry, runtime adapters, teaching
surfaces, tests, and live evidence do not evolve at the same speed. A status
claim assembled from any one of them is incomplete. The repository-tracked
`copilot-capability-audit` skill makes the comparison repeatable and leaves
progress where the next agent can inspect it.

The skill is an audit and planning instrument. It does not grant capabilities,
replace the registry, or mark a row complete from a declaration-only validator.

## The authority chain

The skill reads the v2 registry first. It then checks the generated contract,
runtime owners, exposure declarations, focused tests, and the durable closure
ledger. Live-drive evidence remains the acceptance authority for behaviour:
FountainStore proves persisted effect, telemetry proves operational
correlation, and AX proves the writer-visible state and actions.

The skill therefore distinguishes:

- **executable-not-live-accepted** — the registry exposes an adapter, but the
  ledger has no complete live acceptance evidence;
- **unavailable-adapter-proof** — the registry deliberately blocks the row
  because its governed adapter and proof path are missing;
- **live-accepted** — the ledger records AX, FountainStore, telemetry, terminal
  proof, and the required origin/provider/consent scenarios; and
- **contract-drift** — registry, generated contract, exposure, or runtime
  binding disagrees and must be repaired before exposure.

## The repeatable run

From the repository root, run:

```sh
python3 .codex/skills/copilot-capability-audit/scripts/audit.py
```

The deterministic run reads `schema/modernization-studio-capabilities.json`
and writes:

- `docs/copilot-capability-audit.md`, a human-readable current empowerment and
  gap report; and
- `docs/copilot-capability-closure.json`, the durable per-capability ledger.

The ledger preserves manually recorded owner, next step, and evidence fields
on subsequent runs. It is the progress memory of the skill; the skill itself
contains procedure, not hidden project state.

## Closure row

Every capability row must eventually identify:

1. the native adapter and policy owner;
2. focused decoding, policy, and origin-parity tests;
3. natural-language, slash, and button scenarios where exposed;
4. provider, consent, failure, cancellation, and resume outcomes;
5. FountainStore proof/document IDs;
6. telemetry correlation IDs;
7. AX projection and terminal-result evidence; and
8. the owner and next implementation step.

The next implementation batch is selected from this ledger, not from a prompt
wish list. A batch should be reviewable, bounded, and ordered by dependencies:
adapter and policy first, proof and focused tests next, then live acceptance
and teaching exposure.

## Widening rule

Widening Copilot means moving a capability through evidence states, not merely
adding a slash alias or exposing a button. A capability becomes empowered only
when the runtime can execute it, policy can evaluate it, tests can constrain
it, the stores and telemetry can prove it, AX can expose it, and live acceptance
has exercised the required routes. Until then, the honest behaviour is an
explicit unavailable decision with no unverified mutation.

The skill is successful when it can answer, from tracked artifacts, three
questions without inference:

1. What can Copilot do now?
2. Why can it not do each remaining capability?
3. What exact implementation and acceptance work widens the next capability?
