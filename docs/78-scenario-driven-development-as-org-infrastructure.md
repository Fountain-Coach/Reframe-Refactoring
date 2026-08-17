# 78 — Scenario-Driven Development Is Org Infrastructure

Chapter 68 made the E2E scenario Reframe's publication unit. Chapter 73 made that scenario the reusable development
unit. Chapter 77 made its executor Swift- and MIDI2-native. This chapter names the larger consequence: the scenario is
not merely a test artifact inside Reframe. It is a portable development contract that an organization can share,
release, execute, inspect, and use to explain how software becomes trustworthy.

## The decision

Fountain Coach treats Scenario-Driven Development as infrastructure. A scenario contract is authored before the source
slice it exercises, executed through a typed operation boundary, and judged by the authorities that own each kind of
truth. The generic lifecycle and MIDI2 transport seam may be released as an org-owned kit; product meaning, Store
adapters, UI witnesses, and publication claims remain with the consuming product.

This is a development system, not a claim that a scenario can approve itself. A green package suite proves the generic
seam. A product run proves behavior. AX, CoreGraphics/VRT, FountainStore, telemetry, and provenance prove different
parts of the product claim. Only their declared intersection can promote a result to `live-accepted`.

## Why this relieves the development cycle

Before a governed scenario exists, a development request tends to be reconstructed from prose: one person remembers
the setup, another writes a harness, a third reads a screenshot, and a fourth infers success from timing or logs.
Every handoff can silently change the prerequisite chain, the target process, the state being observed, or the meaning
of completion. The burden is not only test maintenance. It is repeatedly re-deciding what the system is supposed to do.

Scenario-Driven Development moves that decision into a versioned, inspectable contract. The contract names the actor,
launch admission, prerequisites, typed actions, lifecycle, terminal predicates, evidence binding, failure states,
cleanup, and claim boundary. The development loop then becomes a bounded cycle:

```text
contract → focused source slice → typed execution → independent evidence → correction → public projection
```

The loop is shorter because it carries identity and proof forward. A maintainer does not have to babysit a sequence,
guess which process is visible, or translate a timeout into a success claim. A failure remains attached to the exact
scenario, source commit, executable, process, Store, window, and evidence root that produced it.

## What MIDI2 changes

End-to-end systems historically separated the language of a specification from the automation that drove it. Early
test scripts were valuable but often imperative and timing-shaped: launch, sleep, click, poll, and inspect. Message
buses and CI systems improved repeatability, but a test runner could still speak a private command language that the
product itself did not understand.

For Fountain Coach systems, MIDI 2.0 provides an owned event-driven peer protocol for this class of system. Its
Universal MIDI Packet transport, negotiated peer model, typed operation vocabulary, correlation, and event-oriented
exchange let the scenario actor participate as a software peer. The scenario invokes the same governed operation
boundary as an external device or Reframe process; the target emits a correlated lifecycle instead of forcing the
runner to infer progress from delay or console text. This complements BDD/ATDD, contract testing, and CI; it does not
replace them or claim to be a universal test-orchestration standard.

The architectural gain is therefore not “MIDI2 makes tests pass.” It is that development communication becomes an
owned protocol surface. Admission, running, terminal success, typed refusal, failure, reconnect, duplicate, resume,
and capacity outcomes can be represented and observed explicitly. MIDI-CI discovery and Property Exchange can extend
that boundary when peers need to negotiate capabilities, profiles, or transport details.

MIDI2 does not remove the need for independent witnesses. AX proves what a human or agent could operate and what the
surface exposed; CoreGraphics and VRT prove rendered appearance; FountainStore proves durable behavior; telemetry
explains timing and resource conditions. A MIDI2 lifecycle event alone is never visual or behavioral proof.

## Rules

1. Every scenario used for development, acceptance, or publication MUST have one stable identity and one complete
   executable contract authored before implementation or driving.
2. The generic scenario seam MUST remain product-neutral. Product operation identities, fixtures, Store adapters, UI
   semantics, and publication claims belong to the consumer or to a separately governed product contract.
3. A reusable generic seam SHOULD be factored into an org-owned kit when more than one consumer needs it. The kit MUST
   follow FCIS-KIT: generic boundary, own tests, immutable semantic version, upstream-first release, and semver
   consumption. A moved copy inside a consumer is not a kit.
4. Scenario execution MUST enter through the same typed MIDI2 operation boundary used by a production software peer.
   A direct function call is a unit test; a private socket, JSON shortcut, or ViewModel call is not scenario acceptance.
5. Lifecycle and state waits MUST be event-driven and correlated. Timers may detect a hang, but neither a timer nor a
   missing event may establish semantic success.
6. One run MUST retain its binding tuple from preparation through terminal classification: scenario, source commit,
   executable, target PID, window ID, managed Store, launch intent, corpus, scene, and evidence root.
7. Independent witnesses MUST remain independent. MIDI2 cannot substitute for AX, visual evidence, Store read-back,
   telemetry, or provenance; each claim must name the artifact that establishes it.
8. A public Book projection MAY explain the method, history, and bounded product evidence. It MUST NOT publish private
   runtime source, Store data, credentials, unpublished manuscript material, or an unearned interoperability claim.
9. The method's future portability MUST be preserved: a new consumer may bind the generic kit to another typed
   operation, transport, Store, UI, or peer without teaching the kit about Reframe's domain.
10. Physical MIDI2 interoperability remains a separate claim requiring a hardware witness. Software-peer acceptance is
    valuable and publishable, but it is not hardware conformance.

## Historical perspective and future infrastructure

Scenario-Driven Development stands in a line from unit tests, acceptance-test-driven development, CI pipelines,
contract testing, and message-oriented integration. Its distinct step is to make the scenario itself a first-class,
versioned participant: not only a list of steps, and not only a test result, but a protocol-bound development object
with durable evidence and a public projection.

The immediate future is a shared Fountain Coach scenario ecosystem: released Swift kits for generic lifecycle,
transport, fixture, and evidence seams; product repositories that bind those seams to their own IDL and Store; MIDI-CI
discovery between software peers; and Book projections that teach humans what a scenario proves without exposing private
implementation. Scenario repositories remain unnecessary unless an independently governed cross-product conformance
authority is created.

The longer-term direction is an ecosystem of cooperating development peers. A Reframe instance, a stage, a service, or
a future physical MIDI2 device could advertise a typed role, negotiate capabilities, exchange correlated lifecycle
events, and retain independent witnesses. The organization gains a reusable conformance vocabulary while each product
keeps authority over its own behavior and user surface.

## Governing sentence

Scenario-Driven Development is Fountain Coach's governed extension of BDD/ATDD for event-driven, stateful systems: a
versioned scenario enters through a typed MIDI2 boundary, carries its identity and lifecycle through the run, is judged
by independent evidence, and becomes public only as a sanitized projection of what the owning product actually proved.

## Evidence and terminology boundary

BDD and ATDD are neighboring established practices, not claims invented by Fountain Coach. The BDD research literature
is still developing: a 2023 systematic mapping study identified 166 papers but reported limited industry insight and a
shortage of process and artifact metrics ([Journal of Systems and Software](https://doi.org/10.1016/j.jss.2023.111749)).
Research on TDD likewise reports context-dependent and often small effects rather than a universal productivity law
([Information and Software Technology](https://doi.org/10.1016/j.infsof.2011.02.002)). Cucumber is a tool for executing
BDD specifications, not a scientific authority ([Cucumber documentation](https://cucumber.io/docs/bdd/)).

Accordingly, Fountain Coach may claim a governed Scenario-Driven Development architecture and report its own measured
results, but MUST NOT imply that BDD, ATDD, TDD, Cucumber, or MIDI2 has been scientifically superseded. Comparative
claims require named measures, a defined baseline, and reproducible evidence.
