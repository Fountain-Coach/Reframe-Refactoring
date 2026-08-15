# 68 — The Reframe E2E Scenario Is the Publication Unit

The Book of Reframe does not publish a command because a prompt was written, a route exists, or an assistant sentence
sounds right. It publishes a command only after a named end-to-end scenario has driven that command through the real
Reframe surface and read the result back from the authorities that own it.

This chapter governs the reusable acceptance seam between Reframe runtime truth and the public Book projection. It
does not define a second command contract, a prompt library, or a visual-demo checklist. The command and capability
contracts remain those compiled from the IDL, facts, generated reasoning manifest, registry, and live Store state.
The scenario binds those contracts into a repeatable writer journey.

## The scenario comes first

For every command proposed for the Book, maintenance begins by resolving its scenario identity:

1. Find the command and capability in the Book scenario coverage manifest.
2. Check that the scenario's prerequisites and terminal assertions still match the current registry, AX surface,
   governance, and runtime implementation.
3. If no scenario exists or the existing one is stale, author or amend the scenario before launching Reframe.
4. Report the scenario ID, prerequisite chain, expected terminal artifacts, and current coverage status before driving.
5. Do not improvise a live sequence from a prompt, a screenshot, or remembered operator procedure.

An absent or imprecise scenario is a publication blocker. The remedy is to make the journey precise, not to weaken the
evidence requirement.

## The scenario is the first implementation artifact

The complete scenario contract is written before implementation begins. It is not a post-hoc test script, a prompt
to be tried against the application, or a record reconstructed from a successful drive. The contract declares the
ordered setup and dependent steps, the executor for each prerequisite, the AX and FountainStore terminal predicates
that permit the next step, the paid-lane decision where applicable, the failure and unavailable outcomes, and the
evidence binding tuple. A scenario whose setup is represented only by prose is not executable and remains `draft` or
`blocked`.

The checked-in serialization may be YAML or a lossless machine-readable projection of the YAML-shaped contract, but it
must pass the repository's scenario validator before source implementation or Live Drive. The validator and internal
scenario capability are the enforcement seam: they reject missing executors, missing terminal predicates, unbound
Stores, and dependent steps that have no established predecessor. The external Live Drive remains a separate witness;
it does not supply missing scenario semantics by operator improvisation.

### Launch admission is part of the contract

An executable scenario MUST also declare a machine-readable `launch` object with exactly the admission values that the
external launcher must inherit: `storeIntent`, `corpus`, and `scene`. `launch.corpus` MUST equal the prepared corpus
(the single `managed-store-seed` corpus when one exists, otherwise `store.corpus`). Preparation emits these values in
its proof; the scenario runner verifies the same values in the target PID's inherited environment before it performs
the first AX action. A prepared fresh Store may therefore be admitted as `explicit`, but that transition is declared
in YAML rather than chosen interactively. Missing, conflicting, or manually substituted launch values fail the
scenario before execution; a validator pass cannot be claimed if this binding is absent.

## What a scenario means

A scenario is a versioned acceptance specification for one writer-facing outcome. It names:

- the command and governed capability identity;
- the source, fixture, or library prerequisite and its identity;
- the managed Store intent, corpus, and isolation boundary;
- the launch and external-display setup;
- the semantic AX actions and identifiers used to interact;
- state-based waits and the state that permits each next step;
- the writer's decision points, including paid-lane confirmation or explicit local-only instruction;
- the terminal AX result and the persisted FountainStore effect;
- the telemetry observation required to explain the run, without using logs as behavioral proof;
- the CoreGraphics window-ID capture for visual evidence;
- the PID, window ID, Store path, executable, and source commit binding;
- cleanup, timeout, refusal, unavailable, and not-established outcomes; and
- the sanitized public projection and reciprocal source links.

Prompt text may be stored as scenario input. It is never the success authority. AX establishes what the writer-facing
surface exposed and accepted. FountainStore establishes what happened. The window-ID capture establishes what the
surface looked like. Telemetry explains the run but cannot substitute for either AX or Store evidence.

## Prerequisites are part of the command

A command is not tested in an empty state when its meaning depends on prior work. The scenario declares the complete
chain and cannot advance until each predecessor has reached its own terminal proof. For example, the honest sequence
for a world report is:

```text
source acquisition → source read-back → Storify source reading → writer confirmation →
Storify terminal Store proof → /world report → world/ledger Store proof
```

`/world` is therefore not accepted by sending `/world` to a newly launched empty workspace. A failed source import is
not silently bypassed, and a confirmation prompt is not a terminal reading result. Each step has its own identity and
evidence.

## Interaction and waiting

AX is the interaction authority. Scenarios address controls by semantic identifier and assert values, roles, states,
and actions. Coordinates may exist only as a separately recorded temporary bridge for a demonstrated AX gap; they are
never the scenario's meaning or acceptance authority.

Waiting is state-based. A scenario waits for a declared AX or Store predicate, with a bounded timeout and a typed
failure. Arbitrary sleeps, visual guesses, and operator intervention are not evidence. If the predicate does not
arrive, the scenario is failed, blocked, unavailable, or not-established according to the observed artifact; it does
not continue by assumption.

## Lane and consent

The scenario records the lane decision visible at the relevant step. Paid availability remains the default election for
writer-facing work under Chapter 51, while an explicit local-only instruction remains authoritative. Internal
delegation is invisible to the writer and is not a separate scenario actor.

Where the operation spends against a paid plan, the scenario must reach and record the writer's explicit confirmation.
A refusal, missing credential, provider failure, or unavailable lane is a terminal outcome of that scenario variant,
not permission to silently use another provider or to publish success.

## Evidence binding and result vocabulary

One run has one binding tuple:

```text
(Reframe PID, CoreGraphics window ID, managed FountainStore path,
 executable path, source commit)
```

AX observations, window capture, Store read-back, and provenance must be attributable to that tuple. An isolated fresh
run is an isolated run; it must never be described as the writer's current UI.

Every assertion is classified:

- **observed** — the named AX element, Store document/event, or image sidecar was opened and checked;
- **inferred** — a conclusion derived from observed facts, never used as sole acceptance proof; or
- **not established** — the required artifact was absent, ambiguous, stale, or unavailable.

Only observed terminal evidence can promote a scenario to `live-accepted`. A screenshot without AX and Store proof is
visual context, not behavioral acceptance. Assistant prose without a persisted artifact is not acceptance.

## Reframe owns the scenario semantics; the witness stays independent

The scenario system is also an internal maintainer capability of Reframe. Its registry and typed contract are not
writer-facing commands. They let Reframe inspect a scenario, validate its prerequisites, execute the application's
typed behavioral path, persist a run receipt, and report the result without re-deriving the journey from prompt prose.

The internal capability is deliberately not a self-approval loop. Reframe may prove behavioral facts from its own
runtime and FountainStore, but an independent Live Drive witness must still prove the accessibility tree, the
CoreGraphics window-ID capture, and rendered visual fidelity. The two authorities meet in one bound evidence bundle:

```text
Reframe internal capability:
  registry → prerequisites → typed execution → Store receipt

Independent witness:
  AX interaction/state → CoreGraphics window ID → VRT capture

Publication:
  only the intersection of both evidence sets
```

The internal capability has a maintainer-only audience, uses a fresh or explicitly named managed Store, cannot target
the writer's current Store by default, and cannot mark itself `live-accepted`. Its machine-readable contract records
the external-witness requirement and the prohibition on circular proof. The external runner is therefore reduced to an
independent witness adapter over a reusable internal scenario definition, not a second source of scenario meaning.

This is the governed development loop: author once, validate once, execute repeatedly, retain receipts, and publish
only after independent surface evidence agrees with internal behavioral proof. It simplifies repetition and drift
control without weakening the distinction between runtime truth and visual acceptance.

## Scenario statuses

The scenario manifest uses these statuses:

- `draft`: the journey is being designed and cannot be driven as publication evidence;
- `executable`: the contract is precise and the runner can attempt it, but no complete live proof exists;
- `live-accepted`: the declared terminal path and evidence bundle passed on the named source/build;
- `blocked`: a specific external or product prerequisite prevents the declared journey, recorded with the artifact;
- `retired`: the command or scenario is no longer a current publication path.

`available`, `executable`, `live-accepted`, and `released` remain distinct. A command page may describe an unavailable
or pending command honestly, but it may not present it as completed live behavior.

## The Book projection

The Book stores sanitized scenario contracts and coverage records. A command page links to its scenario ID; the
scenario links to its governing chapter, runtime source, capability identity, and evidence record. The public record may
include predicates, dates, source commits, window dimensions, and evidence links. It must not include private Store
data, credentials, deployment secrets, raw internal identifiers, or unowned manuscript material.

The Book's scenario section explains the method and shows the coverage matrix. It is not a second runtime contract and
does not turn a development snapshot into a released App. Chapter 43 remains the authority for release status, and
Chapter 44 remains the authority for public/private boundaries.

## Publication rule

No new command page, refreshed command snapshot, or live-accepted capability claim enters the Book until:

1. its scenario is resolved or authored;
2. its prerequisites are explicit and executable;
3. its current run reaches the declared command result;
4. AX, window-ID, FountainStore, and provenance evidence are bound to one run;
5. the result status and limitations are recorded honestly; and
6. the Book projection passes its own AX/VRT and strict prepublication gates.

The scenario is the smallest reusable unit that makes a publication claim checkable. The Book publishes the projection;
Reframe and FountainStore remain the authorities for what the scenario actually proves.
