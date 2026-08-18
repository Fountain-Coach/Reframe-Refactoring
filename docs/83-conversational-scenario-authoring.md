# 83 — Conversational Scenario Authoring Is the Development Surface

Chapters 68 and 73 make the scenario the development and publication unit. Chapter 77 makes its execution Swift and
MIDI2-native. Chapter 78 names the organizational infrastructure. This chapter governs the missing authoring seam:
the scenario must be developed as a conversation with the maintainer, not as a hand-edited YAML file discovered in a
repository directory.

The scenario is an executable prompt-contract. It is readable as prose by a human and precise enough for a machine to
compile, validate, execute, and witness. YAML and JSON remain important artifacts, but they are projections of that
contract, not the maintainer's primary development experience.

## The decision

When a maintainer says what should happen — for example, “load this source, let Storify derive its movements and
questions, use those results to compose Teatro illustrations, and place each admitted image at its semantic text
location” — the scenario authoring surface MUST preserve that meaning as one governed contract.

The authoring flow resolves the request, exposes the proposed scenario in human-readable form, compiles it into the
checked integration representation, and only then offers execution. The compiled representation MUST retain the
relationships expressed in the prose. It may not replace them with a generic static prompt, a timer, an unrelated
identifier, or a runner-specific shortcut.

This is not a claim that the conversational authoring surface already exists. The current repository stores executable
scenario YAML beside the implementation and a checked JSON projection. That is the current artifact arrangement. The
authoring experience governed here is the required next development boundary.

## What a scenario prompt-contract contains

A scenario prompt-contract carries, in one readable meaning:

- the intended writer journey and the reason it matters;
- the actors, authorities, and consent boundaries;
- the source identity and the passages to be read;
- the semantic products the journey requires, including Storify movements and questions;
- the downstream consumers of those products;
- the transformations that compose prompts or other derived requests;
- the location relationship that attaches a result back to the text;
- the typed operation, lifecycle, and terminal predicates;
- the evidence required from FountainStore, AX, window-ID/VRT, telemetry, and provenance; and
- the honest failure, uncertainty, unavailable, resume, and not-established outcomes.

The machine projection may normalize names and types, but it MUST be lossless with respect to these dependencies.
If the author says that an illustration prompt depends on a movement, a question, and a source passage, the compiled
scenario must name those inputs and their lineage. If the author says that the image belongs at a semantic text
location, the compiled scenario must carry that placement relation. A field called `beatID` is not an acceptable
substitute merely because an older implementation happens to use that term.

## Semantic handoff is a dependency, not a wait

The scenario MUST express the actual data dependency:

```text
source passage
    → Storify reading
    → persisted movements and questions
    → movement/question/source context
    → composed illustration prompt
    → consented image generation
    → Image Cloud receipt
    → placement at the corresponding text location
```

“Storify finished” is therefore insufficient as a scenario description. The terminal Storify predicate must establish
that the required movements, questions, source spans, and uncertainty state were persisted and readable. The image
step must consume those artifacts rather than repeat the same information in a static prompt written beside the YAML.

An empty question set is a meaningful result and must remain distinguishable from a missing Questions artifact. A
movement with no source location is incomplete for placement and must not be presented as an image anchor. A generated
image without an admitted Image Cloud receipt is not an illustration participant. A receipt without a text-location
relationship is not correctly placed.

## The conversational authoring loop

The governed development experience is:

```text
maintainer prose
      ↓
grounded scenario interpretation
      ↓
human-readable scenario draft
      ↓ confirmation or correction
      ↓
compiled YAML + checked JSON projection
      ↓
validation and focused implementation
      ↓
owned MIDI2 scenario run and independent witnesses
      ↓
observed evidence, correction, and rerun
```

The authoring mediator MUST distinguish intent, clarification, and execution. It MUST not silently turn a vague turn
into a YAML action, infer a semantic anchor from a screenshot, or treat a runner error as a reason to rewrite the
scenario's meaning. When the prose does not establish which passage, movement, question, or placement relation is
intended, the authoring surface asks for that missing meaning or retrieves the governed state.

The maintainer may revise the scenario by saying what changed. The system recompiles the affected projection and
reports the semantic delta: prerequisites added or removed, outputs newly consumed, evidence changed, and claim
boundary changed. It does not require the maintainer to locate and manually synchronize multiple serialization files.

## Rules

1. The primary scenario authoring surface MUST accept and return human-readable prompt-contract prose.
2. The authoring surface MUST show the resolved scenario before execution and preserve the maintainer's ability to
   correct its meaning.
3. YAML beside the implementation is the canonical executable integration artifact until a separately governed
   scenario compiler is released; JSON is a checked runtime projection. Neither may silently become a second meaning.
4. Compilation MUST preserve semantic lineage between source passages, movements, questions, derived prompts, image
   receipts, and text locations. It MUST reject unresolved required relationships rather than inventing them.
5. Scenario language MUST use the domain's current semantic vocabulary. `Movements`, `Questions`, source passages,
   and text locations are distinct. Historical `beat` identifiers may remain compatibility aliases in storage only;
   they are not the authoring vocabulary for this contract.
6. A downstream action MUST consume the persisted output of its prerequisite. A static restatement in a later prompt,
   a screenshot, a log line, or a timer does not satisfy the dependency.
7. The generic runner MUST execute the compiled contract without deciding what the scenario “really means” from
   exact phrases, regexes, step names, or hardcoded scenario types.
8. A scenario compiler or authoring mediator MUST not bypass the governed MIDI2 operation, consent, lane policy,
   FountainStore, AX, or evidence authorities.
9. A scenario revision MUST produce a new source identity or explicit source diff. Existing run evidence cannot be
   silently relabeled as evidence for the revised contract.
10. Public publication MAY project the human-readable contract and sanitized evidence, but MUST NOT expose private
    prompts, manuscript material, Store data, credentials, runtime source, or an unearned implementation claim.
11. The authoring surface is not live-accepted merely because it can produce YAML, and a scenario is not accepted
    merely because its compiled projection validates. Both require the evidence gates of Chapters 08, 73, 75, and 77.

## Acceptance boundary

The authoring capability is implemented only when a maintainer can state a scenario in conversation, inspect and amend
the resolved contract, obtain a deterministic compiled projection, and run that projection through the owned Swift
and MIDI2 runtime without manual serialization edits. Acceptance must show that a semantic downstream action consumed
the persisted prerequisite artifacts and that its result was attached to the declared text location.

Until then, the repository's YAML/JSON scenarios remain valid implementation artifacts and diagnostic contracts, but
the conversational authoring experience is **not established**.

## Governing sentence

A scenario is a human-readable executable prompt-contract: conversation gives it meaning, compilation gives it a
checked runtime form, and only the declared semantic lineage and independent evidence may give it a result.
