# Copilot Implementation Extension

> Chapter summary: This chapter extends the Grounding-first Reframe refactor to the application Copilot. It defines the required product behaviour, authority boundaries, implementation-discovery procedure, migration rules, and acceptance evidence. It does not prescribe unverified types, files, protocols, or call paths.

## Purpose

Reframe contains a conversational Copilot intended to operate with the same legitimate access to the active Reframe workspace that the writer has through the application.

The Grounding-first refactor must therefore extend beyond the visible editorial pipeline. The Copilot must be migrated onto the same post-indexing authority model as the rest of Reframe.

The Copilot is not a separate source of truth, a second workflow engine, or an independent interpretation layer. It is the conversational means by which the writer may inspect, understand, direct, and operate the existing Reframe application.

The implementation objective is:

Every Reframe operation that the writer may legitimately perform through the application should be available to the Copilot through the same authoritative application behaviour, subject to explicit safety, cost, confirmation, and identity rules.

This does not mean that the Copilot may silently act without limits. It means that the Copilot must no longer be artificially weaker because it lacks access to application state or because its action vocabulary reflects obsolete architecture.

## Relationship to the Grounding-first refactor

All authority rules defined by the Grounding-first refactor apply equally when an operation is initiated conversationally.

The Copilot must respect the same authority chain:

1. canonical source text remains factual authority;
2. confirmed Grounding provides the writer-confirmed interpretive and policy contract;
3. Storify Source Auto is the sole structural reader of canonical source text;
4. downstream artifacts remain derived artifacts with explicit identity and readiness;
5. FountainStore persistence remains authoritative over transient UI state;
6. source evidence must remain distinguishable from Grounding, derived interpretation, and model inference;
7. removed semantic-index artifacts must not remain hidden Copilot dependencies.

A Copilot request must not bypass these contracts merely because it originates in natural language.

## Required end state

After this extension is complete, the Copilot must be able to:

* inspect the active Reframe project and explain its current state;
* retrieve the same canonical source and persisted Reframe artifacts available through the application;
* distinguish current, stale, missing, failed, incomplete, and unreadable artifacts;
* explain what operations are currently available and why;
* invoke legitimate Reframe operations through the application's existing operational boundaries;
* request confirmation where the corresponding user operation requires confirmation;
* expose cost-bearing or provider-bearing work before execution;
* report the persisted result of an operation rather than merely claiming that it ran;
* recover its understanding of the workspace after application relaunch;
* refuse or visibly fail when required authority, evidence, readiness, provider access, or writer confirmation is absent.

The Copilot must not depend on semantic indexing, published semantic-memory objects, historical reading state, or obsolete index-derived readiness.

## Non-goals

This extension does not authorize the coding agent to:

* invent a new Copilot architecture before inspecting the existing one;
* replace the application workflow with a generic agent framework;
* create a second store beside FountainStore;
* introduce a parallel command bus solely for the Copilot;
* make conversation history authoritative application state;
* infer writer confirmation from conversational tone;
* expose every internal function directly to the model;
* preserve semantic indexing as a private Copilot-only subsystem;
* redesign unrelated UI, model-provider, or persistence systems;
* assume that filenames or currently documented symbols still identify the implementation.

## Implementation discovery is mandatory

Before proposing or editing the Copilot implementation, inspect the current Reframe source tree.

Do not begin from a presumed flow such as:

```
chat view
→ planner
→ interpreter
→ command
→ view model
→ store
```

That flow may or may not describe the current implementation.

Instead, establish the real implementation from evidence.

### Required discovery questions

The coding agent must determine:

1. Where does a writer's conversational turn enter the application?
2. Which component constructs model context?
3. Which persisted sources are available to that context?
4. Which source or artifact retrieval paths already exist?
5. How is intent represented after model inference?
6. Is intent typed, textual, enumerated, generated, or interpreted dynamically?
7. Which component decides whether an action may execute?
8. Which component requests confirmation?
9. Which component performs the operation?
10. Which component persists the resulting state?
11. How is success verified?
12. How are failure and uncertainty returned to the conversation?
13. Which Copilot operations still invoke indexing-era behaviour?
14. Which application operations are currently unavailable to the Copilot?
15. Which Copilot-specific paths duplicate behaviour already implemented elsewhere?
16. Which generated manifests, capability declarations, IDL definitions, facts, or reasoning artifacts describe Copilot access?
17. Which tests currently exercise the live conversational path?
18. Which state survives relaunch, and which state exists only in memory?

Record the answers in PLANS.md with symbol names, source paths, and evidence.

### Required searches

Search by behaviour and symbols, not only by guessed filenames.

At minimum, search for:

* Copilot
* chat
* conversation
* planner
* intent
* command
* capability
* operation
* confirmation
* approval
* inference cost
* provider
* Grounding
* Storify
* Continuity
* Cut Script
* publish
* FountainStore
* semantic index
* reading state
* semantic memory
* readiness
* resume
* failure
* relaunch
* generated reasoning
* manifest
* IDL
* facts

Also search for user-facing strings corresponding to currently visible Copilot actions.

## Implementation principle: reuse before extension

The Copilot must operate Reframe through the application's existing authoritative use cases wherever those use cases already exist.

For every Copilot action, determine whether Reframe already has an application-level operation used by the visible UI or another legitimate caller.

If it exists:

* reuse it;
* expose it through the existing intent or capability mechanism;
* preserve its validation, persistence, telemetry, provider, cost, and failure behaviour;
* do not reconstruct the operation inside the Copilot layer.

If it does not exist:

* first determine whether the missing boundary is an application defect independent of the Copilot;
* add the smallest reusable application-level operation;
* use that operation from both the normal interface and the Copilot where appropriate;
* do not create an operation callable only through model-generated text unless the behaviour is genuinely conversational.

The Copilot should add conversational access, not duplicate business logic.

## Copilot perception contract

The Copilot requires a truthful representation of the current Reframe workspace.

This representation must be assembled from authoritative application and persisted state. It must not be reconstructed from prior assistant messages.

The coding agent must identify the current mechanism by which workspace state enters Copilot context and extend or replace that mechanism only as necessary.

The resulting perception contract must allow the Copilot to determine, where relevant:

* active project identity;
* canonical source identity;
* source availability;
* confirmed Grounding identity and status;
* Storify identity, progress, readiness, and failure;
* Cut Script identity and readiness;
* Continuity identity, readiness, and findings;
* publication state;
* provider availability and provenance;
* incomplete or resumable operations;
* stale derived artifacts;
* operations currently available;
* operations currently blocked;
* reasons for blocking;
* whether confirmation is required;
* whether an operation may incur inference cost.

Do not prescribe a new aggregate type merely to satisfy this document. First inspect whether the application already has snapshots, projections, manifests, readiness structures, or store queries that provide these facts.

Any new representation must be derived from existing authority rather than becoming authority itself.

## Retrieval parity

The Copilot must have legitimate read access to the same project materials the writer can access through Reframe.

This includes, where applicable:

* canonical source text;
* source chapters, scenes, or line ranges;
* confirmed Grounding;
* Storify results and progress;
* Cut Script artifacts;
* Continuity findings;
* publication state;
* operational failures;
* provider and telemetry information exposed by the application.

Retrieval must use current native application and FountainStore access.

Do not inject the entire project into every prompt merely to claim parity. Retrieval may remain scoped, selective, resumable, or mediated according to the existing model architecture.

Parity means that the Copilot can obtain the relevant material when needed, not that all material must always occupy model context.

The retrieval implementation must preserve distinctions between:

* canonical source evidence;
* writer-confirmed Grounding;
* derived artifacts;
* operational metadata;
* model inference.

The Copilot must not report an inference as source fact.

## Action parity

The coding agent must compare:

1. operations the writer can initiate through Reframe;
2. operations currently available to the Copilot;
3. operations that should remain unavailable conversationally for safety or product reasons.

Create an evidence-based parity matrix in PLANS.md.

For each operation, record:

* user-visible name;
* current UI entry point;
* current application operation;
* current Copilot entry point, if any;
* required persisted artifacts;
* readiness conditions;
* confirmation behaviour;
* cost behaviour;
* provider behaviour;
* persistence effect;
* telemetry effect;
* failure result;
* relaunch behaviour;
* migration requirement.

Do not automatically expose low-level internal functions. Expose legitimate application operations at the level of writer intent.

## Intent mediation

Natural-language requests must pass through Reframe's existing grounded intent-mediation architecture.

The coding agent must first inspect how Reframe currently converts a writer turn into executable application behaviour.

Extend that system rather than adding an unrelated model-to-function mechanism.

The final implementation must ensure:

* model prose is not executed directly;
* ambiguous intent remains ambiguous until resolved;
* unavailable actions are not fabricated;
* required targets are grounded in the active project;
* destructive or expensive actions cannot be smuggled through descriptive language;
* writer confirmation remains explicit where required;
* the same writer wording produces behaviour consistent with current application state;
* unsupported requests receive an accurate explanation rather than a false success response.

If the current implementation uses generated intents, capabilities, IDL, facts, manifests, command schemas, or interpreters, update the authoritative source and regenerate all tracked derivatives.

Do not manually patch generated artifacts as though they were source.

## Confirmation and cost

The Copilot must not invent its own cost or confirmation policy.

For every operation initiated by the Copilot, preserve the application's existing rules for:

* confirmation;
* destructive effects;
* model-provider invocation;
* inference cost;
* retries;
* cancellation;
* resume;
* visible failure.

Where equivalent UI behaviour currently lacks an explicit reusable policy boundary, introduce the smallest shared boundary necessary so that UI and Copilot cannot diverge.

The model may explain known cost or provider information supplied by the application. It must not estimate, waive, or authorize application cost by itself.

Writer confirmation must be persisted or represented according to the existing Reframe authority contract. A transient sentence in conversation must not become a hidden global permission.

## Execution and verification

A Copilot-initiated action is not complete when a model emits an intent.

Completion requires the same application evidence required for a user-initiated action.

The implementation must distinguish:

* intent recognized;
* action available;
* confirmation requested;
* confirmation accepted;
* execution started;
* execution progressing;
* execution resumable;
* execution succeeded;
* execution failed;
* persisted result verified;
* resulting artifact stale or current.

The conversational response must be generated from the observed result, not from the requested result.

For persisted operations, verify the resulting artifact or state through the same store authority used after relaunch.

Do not report "completed" merely because an asynchronous task was launched.

## Removal of indexing-era Copilot behaviour

The Copilot migration must explicitly discover and remove dependencies on the architecture eliminated by this refactor.

Search for Copilot-accessible operations, context fields, readiness rules, prompts, tests, user-facing strings, and generated capabilities related to:

* semantic indexing;
* chapter read-in as an index-building operation;
* repair of semantic reading state;
* index-derived beats;
* semantic-memory priors;
* published semantic objects used as structural authority;
* index-derived manuscript guides;
* legacy reading completion;
* index-based readiness.

For each dependency:

1. identify the current Copilot behaviour;
2. identify the legitimate writer intention behind it;
3. map that intention to the Grounding-first architecture;
4. implement the replacement;
5. migrate or remove the visible Copilot operation;
6. prove no live Copilot caller remains;
7. remove temporary transition code in the recorded phase.

Do not merely rename indexing-era actions.

A conversational command such as "read this chapter" may still represent a legitimate writer intention, but it must be reinterpreted through the new architecture rather than routed to a removed index producer.

## Writer steering

Conversation may contain project direction, corrections, preferences, or decisions.

The implementation must distinguish conversational steering from persisted Grounding and other authoritative project state.

The Copilot may:

* propose a Grounding change;
* help formulate a Grounding change;
* show the effect a proposed change would have;
* invoke the application's legitimate Grounding confirmation flow.

The Copilot must not silently promote ordinary conversation into confirmed Grounding.

Where Reframe already supports persisted writer instructions outside Grounding, use that mechanism according to its authority. Do not invent a new steering artifact without first establishing that no suitable current mechanism exists.

## Relaunch parity

The Copilot must not depend on unrecoverable session memory for its understanding of project state.

After application relaunch, the Copilot must be able to reconstruct:

* the active persisted project state;
* confirmed Grounding;
* available and blocked operations;
* resumable work;
* completed artifacts;
* failures that remain relevant;
* current artifact identity.

Conversation history may improve continuity, but it must not be the sole source for operational truth.

Acceptance tests must include at least one relaunch boundary.

## Implementation phases

The exact source files and symbols must be determined during discovery. Do not convert these phases into guessed file edits.

### Phase 1 — Current Copilot implementation map

Produce an implementation map and parity matrix.

No architectural rewrite is permitted in this phase.

Deliver:

* actual conversational entry path;
* actual context-construction path;
* actual intent representation;
* actual execution path;
* actual persistence path;
* actual confirmation path;
* actual result-reporting path;
* all indexing-era dependencies;
* operation parity matrix;
* relevant tests;
* affected generated artifacts.

Update PLANS.md.

### Phase 2 — Grounding-first Copilot perception

Make the current authoritative Grounding-first workspace state available to the existing Copilot reasoning path.

Do not add mutation capability in this phase unless required to preserve an already working operation.

Prove that the Copilot can correctly distinguish:

* source;
* confirmed Grounding;
* derived artifacts;
* stale state;
* missing state;
* failed state;
* blocked operations.

### Phase 3 — Retrieval parity

Connect the Copilot's existing retrieval mechanism to current canonical source and persisted Grounding-first artifacts.

Remove retrieval dependence on semantic indexes and historical reading state.

Prove source attribution and identity handling.

### Phase 4 — Existing action migration

Migrate currently exposed Copilot actions away from indexing-era operations.

For each action:

* preserve the writer intention;
* route through the current application operation;
* preserve confirmation and cost policy;
* verify persisted effects;
* update user-facing language;
* update generated capabilities or manifests;
* add focused tests.

### Phase 5 — Legitimate action parity

Add missing conversational access to legitimate Reframe operations identified by the parity matrix.

Reuse existing application operations.

Do not expose arbitrary internal functions.

### Phase 6 — Relaunch, failure, and behavioural acceptance

Add end-to-end tests covering natural writer language, persisted effects, failure, stale state, confirmation, cost, and relaunch.

Remove remaining transition seams whose exit criteria are satisfied.

## Behavioural acceptance scenarios

Tests must assert application behaviour and persisted state, not exact assistant phrasing.

At minimum, cover scenarios equivalent to the following.

### Inspect current state

The writer asks:

> Where are we?

The Copilot reports the actual current project state, including incomplete, stale, failed, or blocked work, without using conversation history as authority.

### Explain readiness

The writer asks:

> Why can't I continue?

The Copilot identifies the actual blocking condition from application state and does not invent a missing index requirement.

### Retrieve source evidence

The writer asks about a source passage.

The Copilot retrieves canonical source evidence and distinguishes it from Grounding and derived interpretation.

### Inspect Grounding

The writer asks what Reframe has been told to preserve or prioritize.

The Copilot reports confirmed Grounding and does not silently include unconfirmed conversational suggestions.

### Run a legitimate operation

The writer asks to run a currently available Reframe operation.

The Copilot resolves the target, exposes confirmation or cost where required, invokes the existing application operation, and reports the verified result.

### Block an unavailable operation

The writer asks for an operation whose prerequisites are absent.

The Copilot explains the real missing prerequisite and does not claim execution.

### Handle stale identity

A source or Grounding identity changes after a derived artifact exists.

The Copilot identifies the derived artifact as stale and does not present it as current.

### Survive relaunch

An operation completes or pauses, the application relaunches, and the writer asks to continue.

The Copilot reconstructs state from persisted authority and resumes only where the application contract permits.

### No-index proof

Run the Copilot path with semantic-index inputs, semantic-memory priors, and legacy reading-state inputs unavailable.

The supported Grounding-first inspection, retrieval, and action scenarios must still work.

## Validation requirements

Each phase must document exact commands and outcomes in PLANS.md.

Validation must include, as applicable:

* focused unit tests;
* application-operation tests;
* FountainStore persistence tests;
* intent-mediation tests;
* generated-artifact consistency;
* UI or executable build validation;
* behavioural Copilot tests;
* relaunch tests;
* explicit no-index tests;
* opt-in live-provider tests where provider behaviour itself is under test.

Do not claim live model behaviour from mocks alone.

Do not require live-provider tests for deterministic authority, persistence, identity, or routing behaviour that can be tested without inference.

## Required negative evidence

Before declaring the Copilot migration complete, provide searches showing that no production Copilot path still depends on:

* semantic-index documents;
* index-derived reading completion;
* semantic-memory priors;
* index-derived Storify input;
* deprecated Copilot action names;
* removed readiness concepts;
* UI-only confirmation authority;
* conversation-only project state;
* duplicate Copilot persistence.

Negative search evidence must be recorded with the exact searched symbols and paths.

## Documentation updates

When implementation changes are complete, update:

* the reading index;
* the current-state chapter;
* the target-architecture chapter where Copilot behaviour materially affects it;
* the refactoring program;
* validation and acceptance;
* compatibility and migration notes;
* the operating guide for `.claude` and `.codex`;
* generated reasoning orientation and capability documentation where applicable.

Do not modify historical claims to pretend the Copilot migration always existed. Record the extension as a deliberate addition to the program.

## Completion criteria

The Copilot implementation extension is complete only when all of the following are true:

1. The real Copilot implementation path is documented from source evidence.
2. The Copilot receives current Grounding-first workspace state.
3. The Copilot can retrieve canonical source and current persisted artifacts without semantic indexing.
4. Existing Copilot actions no longer route to removed indexing-era behaviour.
5. Legitimate conversational operations reuse authoritative application behaviour.
6. Confirmation, provider, cost, retry, resume, telemetry, and failure behaviour remain consistent with direct application use.
7. Copilot responses report verified results rather than requested outcomes.
8. Confirmed Grounding cannot be created implicitly from ordinary conversation.
9. State and operational understanding recover after relaunch.
10. Generated capability, IDL, fact, role, manifest, and reasoning artifacts agree with runtime behaviour.
11. No production semantic-index dependency remains in the Copilot path.
12. Behavioural acceptance tests pass through the actual conversational integration surface.
13. Remaining transition code, if any, has a recorded removal phase and explicit exit criteria.

## Instruction to the implementing agent

Do not begin by designing a generic Copilot framework.

Begin by reading the repository authority files, then map the implementation that exists.

Do not infer architecture from this chapter's conceptual language. This chapter defines required behaviour and migration constraints, not unverified source structure.

Where current code and this extension differ:

* describe the code as current state;
* describe this chapter as required migration;
* identify the smallest phase-sized change;
* implement through existing Reframe authority and application boundaries;
* prove the result from persisted state and tests.

The desired result is not a Copilot adjacent to Reframe.

The desired result is that the existing Reframe Copilot can truthfully perceive and legitimately operate the Grounding-first Reframe application.
