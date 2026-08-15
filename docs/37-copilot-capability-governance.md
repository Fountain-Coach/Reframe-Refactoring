# Copilot Capability Governance — From Transport Contract to Trustworthy Action

> Chapter summary: As of 2026-08-15, Reframe has a checked v2 application capability boundary and the governing contract for one grounded mediation decision, paid-first lane selection, and typed handoff. The contract already exists; runtime adoption is incomplete. A mediation service exists, but workflow selection, reference resolution, and lane resolution still retain decision authority after mediation in some paths. The current registry contains 55 identities: 24 executable and 31 explicitly unavailable. This chapter records that distinction honestly and defines the path to an empowered Copilot: teach from the checked registry, act through existing application boundaries, and claim only what FountainStore, telemetry, and AX can prove.

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

This is a status report, not a claim of full completion. Boundary enforcement is
complete; capability closure is outstanding.

| Layer | Current position | Governance status |
| --- | --- | --- |
| MIDI backplane IDL | Defines topics, payloads, capability masks, QoS, budgets, acknowledgements, and telemetry. | Sound and authoritative for transport. |
| `schema/facts.json` | Generated from the IDL. | Sound when regenerated with the contract. |
| Reasoning manifest | Generated from IDL, facts, roles, app guidance, overlay, and capability declarations. | Useful orientation; not runtime truth. |
| Modernization capability file | `schema/modernization-studio-capabilities.json` describes user capabilities, IDL topics, stages, owners, gates, writes, and failure modes. | Authoritative v2 application boundary. The generated audit currently reports 55 identities, 24 executable, and 31 explicitly unavailable. |
| Copilot mediation | A typed model decision passes through a mediation service before planning/execution. | The contract is governed; runtime adoption is incomplete because later workflow/lane stages can still re-decide or discard the mediated route. |
| Writer-facing verbs | Generated and checked for the governed capabilities. | The exposed subset is registry-owned; unavailable rows must not be taught. |
| Runtime execution | Several operations reuse application-level handlers and FountainStore. | Real for selected actions; parity is incomplete. |
| Contextual availability | Situation and open-manuscript checks exist; route-specific prompt exposure also changes with model capacity. | Partially governed; capability should not disappear because a prompt is short. |
| Result proof | FountainStore persistence, telemetry, and AX evidence exist for governed execution. | Required for exposure, but not yet present for every registry identity. |

The practical conclusion is encouraging but firm: Reframe now has the join and an
honest boundary. It does not yet have adapters and evidence for the whole
application surface.

## Contract already pinned down; implementation not yet singular

The semantic-router contract is not a new design introduced by the implementation
phase. It is already distributed across the governing chapters:

- Chapter 23 requires one complete reasoning over the full intent taxonomy, with
  deterministic dispatch from that decision and no competing classifier.
- Chapter 24 defines the decision's uncertainty-map product and distinguishes
  settled, ambiguity, thin, and failure states.
- Chapter 20 requires the mediator to recognize the quality class, prefer the best
  eligible paid route when available, preserve the original turn during internal
  delegation, and expose only an actual service boundary.
- Chapter 51 requires lane resolution once into a value that carries its client
  and budget; no later surface may re-resolve it.
- Chapter 58 requires one open-turn handoff to a typed capability while existing
  executors retain mutation, persistence, and terminal-proof authority.

The current implementation contains pieces of this contract, but they are not yet
one runtime authority. `ManuscriptTurnIntentMediationService` performs a typed
mediation pass; downstream workflow selection, reference resolution, and lane
resolution can still make consequential choices or lose the original request.
Those are implementation seams, not additional governance authorities. The
required migration is therefore to make the mediated decision the sole semantic
route, then let deterministic planning and execution consume it without
reinterpreting writer meaning.

Until that migration is complete, the correct status is **contract governed,
implementation partial**. A passing mediation decode, a selected workflow, or a
provider call alone does not establish semantic-router completion.

## The executable boundary today

The available boundary is the generated registry, not a prose workflow. It currently includes maintenance and command
discovery, library/project operations, preparation and grounding, pipeline status, Storify source/run controls,
citations, and world/reference actions. The complete list and status are generated in `docs/copilot-capability-audit.md`.
The audit currently reports 24 executable identities and 31 unavailable identities. An executable identity is not a
live-accepted or released identity: each must still acquire its own adapter, policy, focused tests, persisted proof,
telemetry, AX result, and required live matrix.

The retired Manuscript Guide offer is not a current Copilot next step. After source import or preparation, writer-facing
offers use the current structural actions: confirm Grounding Inputs, map the manuscript into beats with Storify, read a
chapter, or make one focused draft change. Legacy guide artifacts may remain for migration and storage compatibility,
but they are not a current teaching surface.

An unavailable capability must be refused explicitly, remain absent from
teaching surfaces, produce no false started/completed message, and perform no
unverified mutation. Source import remains unavailable in the registry until its adapter and proof-gated acceptance are
recorded, even though the current isolated DraCor drive has demonstrated an execution path. Storify draft start remains
blocked until a proof-gated draft adapter exists.

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

Some capabilities are real today. Grounding confirmation, Storify Source Auto,
frame switching, library opening, and the governed preparation guide actions
have runtime paths and focused tests.

Some are only partially real. Natural-language continuation, cross-route action
parity across the entire application, contextual availability on every
placement, relaunch/resume through dialogue, successful terminal Storify proof,
and the full provider/high-risk matrix are not yet acceptance-complete.

Historical stale teaching such as `readInChapter`, `repairRead`, and indexed-passage promises has been retired from the governed teaching surfaces. Any future capability that is named but cannot resolve to a typed runtime owner is a governance defect, not an executable capability, and must not be taught.

The distinction matters. A Copilot that says “I cannot do that here because the current situation does not expose it” is trustworthy. A Copilot that describes an operation whose schema, executor, or evidence path does not exist is not.

## Live moment of truth

The Romeo-and-Juliet fixture drive demonstrated the governed portion of the
contract on the external full-screen display. It imported the manuscript,
answered a grounded question, exposed the generated command catalogue and
status, and drove `storify.source.start` through requested, accepted, running,
canceled, and resumed states. AX exposed the activity, cancel, and resume
controls. The fixture store contained the v2 aggregate and append-only event
records, with GUI telemetry correlated by execution ID.

The drive intentionally stopped the long on-device reading run after proving
the lifecycle and resume path. It does not claim a successful terminal Storify
proof, a paid-lane route, or ChatGPT/OpenAI-key provider acceptance. Those are
remaining acceptance work, not missing documentation.

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

Until those criteria are met, the registry's explicit unavailable rows are the
correct product behaviour, and this chapter is the authoritative status report.

## Governing sentence

The MIDI backplane tells Reframe how an operation travels; the capability registry tells Copilot what the writer means; the runtime and FountainStore prove what happened. Copilot may teach only the intersection of those three truths, and may claim no more than the evidence can show.
