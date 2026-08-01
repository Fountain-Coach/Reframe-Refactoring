# Copilot Capability Governance — From Transport Contract to Trustworthy Action

> Chapter summary: As of 2026-08-01, Reframe has a strong transport and persistence contract, a real intent-mediation path, and several working Copilot actions. It does not yet have one authoritative, executable capability contract joining the MIDI backplane IDL, writer-facing verbs, runtime actors, contextual availability, and persisted evidence. This chapter records that status honestly and defines the pragmatic path to an empowered Copilot: teach from a checked capability registry, act through existing application boundaries, and claim only what FountainStore, telemetry, and AX can prove.

## The decision

The MIDI 2.0 backplane IDL remains the sole contract for transportable operations, payloads, capabilities, QoS, budgets, resume, and telemetry. It is not replaced by OpenAPI, and it is not expanded into a writer-facing vocabulary it was never designed to contain.

The Copilot needs one governed layer above that transport contract: the **application capability contract**. A capability is the smallest writer-meaningful action Reframe can honestly teach and perform. It joins:

- the writer-facing verb and explanation;
- the intent it satisfies;
- the IDL topics or native application operation it uses;
- the responsible runtime actor;
- the visible situations in which it is available;
- its state and readiness gates;
- confirmation, provider, and cost rules;
- its persistence effect and failure modes;
- the AX and FountainStore evidence that proves its result.

The Copilot is taught from that capability contract. It is never taught from a prompt paragraph, a stale slash-command list, or an enum that has no runtime owner.

## Current status — what exists and what does not

This is a status report, not a claim of completion.

| Layer | Current position | Governance status |
| --- | --- | --- |
| MIDI backplane IDL | Defines topics, payloads, capability masks, QoS, budgets, acknowledgements, and telemetry. | Sound and authoritative for transport. |
| `schema/facts.json` | Generated from the IDL. | Sound when regenerated with the contract. |
| Reasoning manifest | Generated from IDL, facts, roles, app guidance, overlay, and capability declarations. | Useful orientation; not runtime truth. |
| Modernization capability file | `schema/modernization-studio-capabilities.json` describes user capabilities, IDL topics, stages, owners, gates, writes, and failure modes. | Closest existing registry, but currently descriptive rather than executable. |
| Copilot mediation | A typed model decision passes through a mediation service before planning/execution. | Real boundary; still vulnerable when the model chooses an answer route against resumable live work. |
| Writer-facing verbs | Distributed across capability JSON, prompts, Swift enums, slash parsers, and runtime switches. | Split authority; the main source of capability drift. |
| Runtime execution | Several operations reuse application-level handlers and FountainStore. | Real for selected actions; parity is incomplete. |
| Contextual availability | Situation and open-manuscript checks exist; route-specific prompt exposure also changes with model capacity. | Partially governed; capability should not disappear because a prompt is short. |
| Result proof | FountainStore persistence, telemetry, and AX evidence exist in the architecture. | Not yet required uniformly for every Copilot action. |

The practical conclusion is encouraging but firm: Reframe does not lack a foundation. It lacks a single join between foundations that already exist.

## The source-of-truth chain

The intended chain is:

```text
MIDI backplane IDL
    ↓ generated
facts and transport operation catalogue
    ↓ declared by the app
Modernization Studio capability registry
    ↓ generated/validated
Copilot intent vocabulary, slash catalogue, and runtime bindings
    ↓ selected by grounded mediation
typed application operation
    ↓ executed
FountainStore / native runtime / telemetry
    ↓ verified
AX-visible and writer-facing result
```

Each layer has a distinct authority:

1. `schema/idl.yaml` is authoritative for transportable operations and their protocol obligations.
2. Generated facts are authoritative projections of that IDL, never a second contract.
3. The Modernization Studio capability registry is authoritative for the application meaning of an operation: what the writer can ask for and what Reframe promises to do.
4. Live FountainStore and runtime state are authoritative for whether a capability is currently ready, blocked, incomplete, stale, running, or resumable.
5. The runtime executor is authoritative for whether an action actually ran.
6. FountainStore, telemetry, and AX together are the evidence authorities for completion: persisted behaviour, operational trace, and perceivable UI state.
7. The prompt is a generated or selected teaching surface. It has no authority to create a capability.

This is why the old OpenAPI instinct was understandable. An operation catalogue is necessary. The missing fact is that transport operations are not yet writer capabilities. `screenplay/patch` is a protocol operation; “rewrite this passage” is a capability with a target, policy, confirmation rule, actor, and result proof. The second must be bound to the first without pretending they are the same thing.

## Actors and responsibility

The system becomes legible when responsibility is explicit:

| Actor | Responsibility | May not do |
| --- | --- | --- |
| Writer | Supplies intent, chooses scope, and confirms guarded or costly work. | Cannot be replaced by model confidence. |
| Copilot mediator | Resolves freeform meaning into a typed capability request using live context. | Cannot execute model prose or invent an action. |
| Planner | Selects an available capability and resolves grounded references. | Cannot bypass readiness, confirmation, or target checks. |
| Application runtime | Owns the reusable operation and its policy boundary. | Cannot report success from task launch alone. |
| MIDI/FountainStore boundary | Carries validated operations and persists the resulting state. | Cannot become a substitute for application meaning. |
| Telemetry | Records errors, timing, resource, and lifecycle facts. | Cannot serve as behavioural proof by itself. |
| AX projection | Exposes the state and actions the writer and driver can reach. | Cannot claim a result absent from runtime/state authority. |
| Capability registry owner | Keeps the writer verb, actor, IDL mapping, gates, and evidence contract coherent. | Cannot mark a capability implemented without executable and tested ownership. |

The current mess is therefore not the fault of the MIDI backplane. It is an integration-governance failure: the application capability registry, Copilot teaching surface, and runtime executor were allowed to evolve as parallel lists.

## Honest examples from the current build

Some capabilities are real today. Grounding confirmation, Storify Source Auto, frame switching, library opening, selected preparation actions, and several screenplay read/write invocations have runtime paths and focused tests.

Some are only partially real. Natural-language continuation, cross-route action parity, contextual availability on every placement, relaunch/resume through dialogue, and uniform persisted-result verification are not yet acceptance-complete.

Some are stale or misleading. The prompt still describes `readInChapter` and `repairRead`, while the current operation enum and executor do not provide those operations. The on-device prompt also omits important hands when its context is tight and directs the writer toward the retired Index model. A capability that is named but cannot resolve to a typed runtime owner is not an unavailable capability; it is a governance defect and must not be taught.

The distinction matters. A Copilot that says “I cannot do that here because the current situation does not expose it” is trustworthy. A Copilot that describes an operation whose schema, executor, or evidence path does not exist is not.

## The empowering vision

The goal is not to turn Copilot into a generic autonomous agent. The goal is to make her a clear conversational front door to the operations Reframe already owns.

When the writer says “continue reading,” Copilot should:

1. inspect the live Storify state;
2. recognize whether there is incomplete or resumable work;
3. resolve the current source and reading scope;
4. state what will happen and who pays, if applicable;
5. request confirmation when required;
6. call the same application operation as the visible UI or structured command;
7. expose real progress without inventing completion;
8. verify the persisted result;
9. answer from that result, including failure or partial completion.

The same pattern should govern opening a manuscript, importing a source, confirming Grounding, running review, revising a beat, patching a draft, or asking for source evidence. Copilot becomes empowered not by having more prose, but by having fewer ambiguous seams.

## Concrete implementation perspective

The existing `schema/modernization-studio-capabilities.json` should become the starting point for the executable capability registry, rather than introducing a competing framework.

Each entry needs a checked binding with at least:

```json
{
  "capabilityId": "storify.source.auto",
  "writerVerb": "read the manuscript into beats",
  "idlTopics": ["screenplay/beat.put", "fountainstore/document.put"],
  "nativeOperation": "ReframeViewModel.startCopilotStorifySourceAuto",
  "actors": ["writer", "copilot.mediator", "runtime"],
  "allowedStages": ["source", "storify"],
  "requiresConfirmation": true,
  "cost": "may use the writer's configured reading lane",
  "reads": ["live Storify run state", "canonical source"],
  "writes": ["persisted beats and run state"],
  "evidence": ["FountainStore run result", "AX activity and result state"]
}
```

The implementation sequence is deliberately modest:

1. Inventory every current writer verb, slash command, `PrepIntentOperationKind`, planner executor, and IDL topic.
2. Promote the capability JSON into the reviewed registry and remove entries that have no runtime owner.
3. Add a parity validator: every registry entry must resolve to an IDL topic or explicitly named native operation, an executor, a policy, and tests; every prompt or slash verb must resolve back to a registry entry.
4. Generate or derive the Copilot teaching vocabulary and command catalogue from the registry. Keep natural-language interpretation model-mediated; only structured slash grammar remains deterministic.
5. Make contextual availability a runtime projection of live state, not a prompt-size decision.
6. Make every guarded operation use the same confirmation and cost policy whether invoked by button, slash command, or natural language.
7. Require persisted-result verification before the Copilot can say an action completed.
8. Add acceptance by capability × placement × provider route × failure/resume state, with FountainStore and AX evidence.

This does not require changing the MIDI backplane IDL for every new writer phrase. It requires binding each meaningful writer capability to the IDL and to the existing application operation that owns its semantics.

## Completion criteria

Copilot capability governance is complete when:

- every taught capability has exactly one registry identity;
- every registry identity has an executable owner or is explicitly unavailable;
- every transport operation is IDL-valid and carries the required telemetry/persistence obligations;
- every writer-facing verb resolves by grounded mediation to a typed capability;
- current state, placement, readiness, cost, and confirmation are supplied by live authority;
- the model cannot create a new operation through prose or JSON alone;
- every action has focused tests and at least one integration or live acceptance path;
- completion claims are based on persisted state and AX-visible result, not requested intent;
- stale index-era capabilities are removed or marked historical and unreachable;
- the manifest, prompts, slash catalogue, runtime bindings, and tests pass parity validation.

## Governing sentence

The MIDI backplane tells Reframe how an operation travels; the capability registry tells Copilot what the writer means; the runtime and FountainStore prove what happened. Copilot may teach only the intersection of those three truths, and may claim no more than the evidence can show.
