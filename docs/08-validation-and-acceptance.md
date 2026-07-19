# Validation and Acceptance

> Chapter summary: This chapter defines the evidence required to accept the Grounding-first architecture, including positive journeys, negative index-dependency checks, identity tests, live quality comparison, and final deletion criteria.

The refactor changes the application's epistemic chain, so compilation and snapshot updates are necessary but insufficient. Acceptance must prove that the right stage produced each artifact from the right persisted inputs and that the application does not quietly consult the retired system.

## Grounding contract tests

Tests must prove that all policy-bearing fields participate in Grounding identity, while timestamps and UI-only state do not. Confirmation must survive relaunch from FountainStore. Editing a confirmed semantic field must create a stale downstream relationship without destroying the prior confirmed profile. Legacy baseline and lens documents must migrate into an inspectable draft state without being falsely labeled fully confirmed under the extended contract.

Prompt-context tests must prove that author baseline, reader lens, source language, destination medium where relevant, structural intent, preservation duties, and transformation boundaries reach Storify. Tests must reject numeric truncation or positional dropping as context-selection behavior.

## Storify independence tests

Construct a store containing source and confirmed Grounding but no semantic index, reading states, semantic memory, published semantic object, or index activity documents. Source Auto must extract atoms, invoke its configured semantic route, validate and persist windows, complete synopsis behavior required by the selected policy, and restore its settled state after relaunch.

Instrument the store client or use a strict test double to fail if Storify lists or fetches retired semantic prefixes. The result must not call `storifyReportFromReading`, `storifySemanticMemoryContext`, or an indirect replacement that merely renames the same data.

Source-authority tests must present a deliberate disagreement between Grounding preference and atom evidence. The output may flag tension or adapt structural emphasis, but it may not invent facts or suppress the contradictory atom without an explicit source-grounded classification.

## Identity and invalidation tests

An unchanged source and Grounding pair may reuse validated Storify artifacts. A source semantic change invalidates affected source-derived and structural artifacts. A Grounding change preserves deterministic atom extraction when source text is unchanged but invalidates kept/noise decisions, beat ordering, summaries, synopsis, and arcs. A steering-only change belongs to its run lineage and does not mutate the confirmed Grounding identity.

All stale decisions must be reproducible after relaunch. Tests that mutate in-memory flags without persisting the corresponding artifact are invalid evidence.

## Downstream journey tests

The canonical acceptance journey is:

```text
import source
→ complete and confirm Grounding
→ run Storify Source Auto
→ inspect and settle structure
→ produce Cut Script
→ run Continuity
→ relaunch
→ recover the same current stage and identities
```

Run this journey with a clean store and assert that no Manuscript Guide generation, index task, staged passage read, or index repair activity occurs. Cut Script must cite current Storify lineage. Continuity must cite current Cut Script identity. Publish readiness must obey current continuity policy without consulting an index.

UI tests must show no Index tab, Read In action, Generate Manuscript Guide action that triggers inference, semantic repair queue, or index readiness blocker. Grounding should present the next structural action. Truth Center, command help, launcher recommendations, dedicated shells, and empty states must name the same stage order.

## Legacy-store tests

Open a store that contains historical semantic passages, reading states, published Guides, repair debts, and learned split facts. The application may expose them through an explicitly archival inspector, but readiness and prompts must ignore them. No migration should delete or rewrite them automatically.

Open a store with legacy baselines but no extended Grounding Profile. The application should preserve the baseline content, explain which new fields require confirmation, and avoid falsely treating old semantic artifacts as a substitute.

## Live Apple evaluation

Use representative screenplay and prose chapters. Compare the former chain with the Grounding-direct Storify chain while the comparison seam still exists. Record total elapsed time, provider calls by purpose, completed and unreadable windows, atom coverage, beat coverage, uncertainty, structural coherence, source fidelity, and usefulness of the resulting Cut Script and Continuity report.

Quality review must inspect the actual outputs; counts alone cannot establish that a beat boundary is meaningful. The comparison should include at least one case where Grounding materially changes structural salience and one where the source contradicts a Grounding preference.

The final architecture does not require the new path to reproduce old index wording. It must equal or improve source-grounded structural usefulness while removing the duplicate read and preserving honest uncertainty.

## Repository validation

During implementation, use focused filters for the changed subsystem. At phase closure run:

```sh
Scripts/modernization-studio-test
MODERNIZATION_STUDIO_BUILD_ONLY=1 Scripts/modernization-studio-proofread-all-apps
git diff --check
```

When capability or reasoning sources change, run the repository's reasoning-manifest regeneration and verification commands required by current skills and `AGENTS.md`, then confirm tracked generated artifacts are updated.

## Final negative evidence

Before deleting the transition flag and declaring completion, repository-wide searches must find no production dependency on:

```text
indexSemanticMemoryInternal
semantic_index_fresh
storifyReportFromReading
storifySemanticMemoryContext
semantic.readingStates
Generate Manuscript Guide   (as an inference action)
Read In                     (as semantic indexing)
```

Matches in explicitly dated historical documents or archival decoders are acceptable only when they cannot influence current runtime behavior and are labeled accordingly. Test fixtures should not keep dead production APIs alive merely to preserve old coverage.

## Acceptance statement

The refactor is accepted only when a reviewer can truthfully state: “Reframe has no semantic indexing stage; confirmed Grounding directly governs Storify; Storify alone reads source structure; downstream artifacts carry exact lineage; old index data is archival; and the full journey works from an index-free store.”
