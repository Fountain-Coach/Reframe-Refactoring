# Instrument Creation Is a Governed Promotion Path

> Governance chapter: 93. This chapter defines the reusable creation and promotion contract for Fountain Coach instruments. It is not the implementation of one instrument, a catalog entry, or a claim that a proposed capability has been released.

## The decision

Fountain Coach treats an instrument as a bounded capability that can be constructed, observed, admitted, reused, and published under named authorities. Instrument creation is therefore a governed promotion path, not an ad-hoc plugin exercise and not a visual catalog exercise.

The canonical lifecycle is:

```text
intent → scenario → contract → implementation → build → execution → evidence → admission → release → publication → reuse
```

Every arrow is a gate. A later state does not follow merely because an earlier artifact exists. A repository, a compiled binary, a responsive process, a passing unit test, a successful scenario run, and a public page are different facts.

The reusable agent workflow is the skill `fountain-coach-instrument-creation`. That skill operationalizes this chapter for any bounded instrument. A particular instrument—whether a login fixture, a MIDI2 peer, a local Apple capability, a remote service, or a composed instrument—is an input to the workflow, never the definition of the workflow.

## What an instrument is

An instrument is a named capability boundary that can be addressed through the Fountain Coach MIDI2 command plane and can report its lifecycle without taking ownership of the host application.

An instrument MUST declare, in machine-readable and human-readable form:

- a stable identity, version, owner, and implementation provenance;
- the MIDI2 operations, events, lifecycle states, and terminal receipts it supports;
- its input, output, permission, privacy, credential, and external-resource boundary;
- whether execution is local, remote, composed, simulated, or hardware-facing;
- progress, cancellation, retry, recovery, timeout, and failure semantics where applicable;
- resource, timing, latency, jitter, ordering, and capacity claims where applicable;
- the scenarios that exercise its declared behavior;
- the evidence authorities that can establish each claim;
- its FCIS-KIT contract version and build identity; and
- its distribution and admission state.

An instrument is not automatically an application, a model, a process, a provider account, a hardware device, or a web page. Those may be implementation participants or evidence authorities behind the declared boundary.

## The authority chain

No layer silently substitutes for another:

| Layer | Authority | Establishes |
| --- | --- | --- |
| MIDI2 contract | the versioned IDL and generated projections | operation names, fields, lifecycle vocabulary, and transport shape |
| FCIS-KIT package | the owned kit repository and release manifest | reusable package boundary, dependencies, version, and build identity |
| Host | Reframe and its product-local policy | intention mediation, permissions, lane selection, Store binding, and host authority |
| Instrument | the instrument runtime | its declared execution, lifecycle events, and terminal result |
| Scenario | the versioned executable scenario | preconditions, actions, terminal predicates, and required evidence |
| FountainStore | the persisted Store authority | durable lifecycle, receipts, leases, and effects |
| AX and window witness | independent UI evidence | what the user-facing surface exposed and what was visibly present |
| Security or interoperability witness | independent review or peer/hardware evidence | claims that local implementation tests cannot establish |
| Release authority | the owning maintainer or release process | promotion of a named build for reuse |
| Publication projection | the appropriate Fountain Coach domain | sanitized human and machine-readable public documentation |

Codex or another agent may implement and exercise a candidate. It is not the arbiter of its own admission, release, security, or interoperability claim.

## Scenario first

Creation begins with a versioned scenario, not with a guessed class, endpoint, screen, or logo. The scenario is the executable prompt-contract for the capability. It names:

1. the intended capability and stable identity;
2. the host and instrument preconditions;
3. the permitted resources, credentials, lanes, and data movement;
4. the MIDI2 operations and expected lifecycle events;
5. the success, cancellation, timeout, refusal, and failure predicates;
6. the evidence required from Store, AX, window identity, telemetry, security, peer, or hardware witnesses; and
7. the claim that may be made if—and only if—the predicates and evidence are present.

The scenario is not a prose promise. It must have a checked executable projection and a deterministic preparation path. A scenario that lacks a terminal predicate, an evidence requirement, or an ownership binding is not ready to drive implementation.

## The creation workflow

The named skill MUST perform these phases in order. It may delegate individual checks to narrower skills, but it may not omit or silently merge the phases.

### 1. Resolve governance and plan the slice

Read the task-specific governance chapters before editing. Record the scope, authorities, risks, exclusions, and validation plan in `PLANS.md`. Resolve whether the work is a new instrument, a revision, a kit extraction, a host adapter, a catalog projection, or a release-only change.

The skill must stop if the proposed boundary conflicts with the MIDI2 IDL, host authority, publication policy, or an existing released kit without an explicit migration decision.

### 2. Declare the identity and contract

Give the capability a stable namespace and version. Declare the owning repository, the FCIS-KIT contract version, the supported MIDI2 operations, and the distinction between standard MIDI2 semantics and Fountain Coach extensions.

The declaration must be sufficient for a machine to answer “what is this?” and “which exact build is this?” without reading implementation prose. Namespaces must not imply that a Fountain Coach extension is a MIDI Association standard operation.

### 3. Create or update the scenario

Author the scenario beside the implementation and generate its checked projection. Include the normal path and the relevant refusal, cancellation, timeout, invalid-input, recovery, and replay cases. For an instrument that touches credentials or an external provider, use a deterministic fixture or mock for repeatable local acceptance; never publish a fixture result as proof of real-provider authorization.

### 4. Implement inside the kit boundary

The FCIS-KIT repository owns the reusable contract, transport seam, lifecycle model, and instrument-local implementation. It must not absorb Reframe product policy, private Store schemas, UI ownership, credentials, manuscript data, or deployment secrets.

The host adapter owns mediation, permission, account, project, Store, AX, and publication decisions. The instrument reports what it did; it does not decide that its own report is accepted.

### 5. Build a named, reproducible release candidate

Resolve dependencies from the committed manifest and lockfile. Build from the current source revision, record the exact executable or package artifact, and run the repository’s negative deprecated-surface checks. No cached or path-dependent artifact may be treated as a released kit.

The candidate must expose its version, source revision, dependency revisions, and artifact digest. A build that cannot be reproduced or identified is not promotable.

### 6. Execute and collect independent evidence

Run focused unit, contract, negative, lifecycle, and scenario tests. For Reframe integration, use the governed Swift `ReframeLaunch` path, the prepared managed FountainStore, the declared MIDI2 ports, AX admission, and the bound CoreGraphics window identity. Bind evidence to one run, PID, executable, Store, scenario, ports, and source revision.

Separate evidence classes:

- tests establish code-level behavior;
- MIDI2 traces establish protocol exchange;
- FountainStore establishes durable lifecycle and receipts;
- AX establishes exposed user-facing semantics;
- window-ID capture establishes rendered visual state;
- security review establishes the separately reviewed security claim;
- software-peer evidence establishes software interoperability; and
- physical-device evidence establishes hardware interoperability.

One class must never be silently used as another.

### 7. Admit the instrument

Admission is a state transition with an authority and evidence record. The instrument moves through explicit states such as:

```text
candidate → organization instrument → locally tested → live-accepted → released
```

Discovery is not admission. A catalog tile is not admission. Compilation is not admission. A passing mock scenario is not proof of a real provider or physical device. If required evidence is missing, the instrument remains honestly pending or unresolved.

### 8. Release the owned kit

Release the standalone FCIS-KIT repository or package with semantic versioning, changelog, source revision, artifact digest, license boundary, dependency declaration, and migration notes. Release upstream before pinning a consumer to the new version. Do not leave a path dependency or an unpublished local copy as the integration contract.

The release record must identify what is included, what is not included, what is simulated, and which claims remain unestablished.

### 9. Integrate the consumer

The Reframe or other consumer must depend on the released kit boundary and preserve the universal MIDI2 command plane. The integration must declare its adapter, roles, capability registration, scenario projection, Store intent, AX labels/actions, and failure behavior.

The consumer integration is a separate change from kit release. It may prove that one host uses one released instrument; it does not redefine the reusable kit or promote unrelated capabilities.

### 10. Publish the projection

Publish only the sanitized instrument projection at `instruments.fountain.coach` after local validation. The public document must show identity, version, contract, lifecycle, intended use, implementation boundary, evidence state, limitations, and links to the released kit and relevant governance chapter.

The catalog is not an operational marketplace unless a separate governance and deployment decision establishes one. It must not expose credentials, private Store data, prompts, manuscript material, private source, deployment details, or unsupported runtime claims.

Cross-domain links are semantic edges:

- `governance.fountain.coach` explains why the instrument exists and what governs admission;
- `midi2.fountain.coach` documents the machine-readable MIDI2 contract;
- `instruments.fountain.coach` presents the admitted capability catalog;
- `book.fountain.coach` presents the development story and scenario evidence; and
- `status.fountain.coach` presents company, legal, and operational context.

The publication template must make those roles legible without making sibling links look like duplicated content or like evidence of sibling release.

## Claims and stop conditions

The workflow must report claims at the narrowest supported level:

| Claim | Minimum evidence |
| --- | --- |
| declared | machine-readable identity and contract exist |
| implemented | source, build, and focused tests exist |
| scenario-tested | the named scenario reaches its declared terminal predicate |
| live-accepted | independent AX, Store, window, and scenario evidence are bound to the same run where applicable |
| released | a named, reproducible version is promoted by its release authority |
| publicly documented | sanitized publication passes estate, metadata, accessibility, and link gates |
| software-peer interoperable | independent software-peer acceptance exists |
| hardware interoperable | physical-device evidence exists |

Stop rather than promote when the IDL identity is missing, the scenario has no terminal predicate, the candidate cannot be bound to one run, lifecycle or receipts are unobservable, credentials or private data would cross the boundary, a generic fallback hides missing provenance, the release is not reproducible, or the public projection would overstate evidence.

Hardware interoperability is always a separate claim. Its absence does not invalidate a machine-readable or software-only instrument, but it must not be implied.

## What the skill does not do

`fountain-coach-instrument-creation` does not:

- invent a MIDI2 operation outside the IDL;
- turn a catalog page into a runtime authority;
- treat a model response, log, screenshot, or process existence as proof by itself;
- silently grant production credentials or provider authority;
- replace independent security review;
- claim hardware interoperability without hardware evidence;
- publish private implementation or Store data;
- merge kit release and consumer integration into one opaque change; or
- narrow itself to a particular example such as login, authentication, image generation, or a single device class.

## Governing sentence

An instrument is created by making a bounded capability executable, observable, reproducible, and evidence-bound; it becomes reusable only when its owning release authority promotes a named build, and it becomes public only through a sanitized projection that says exactly what the evidence establishes and what it does not.
