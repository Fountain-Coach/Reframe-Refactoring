# 73 — The Reframe Scenario Development Cycle

Chapters 68–72 establish the scenario as the publication unit, the public/maintainer projection boundary, and the
MIDI2 software-peer and projection surfaces. This chapter closes the loop: a Reframe scenario is the repeatable
development unit for writer journeys, governed capabilities, system boundaries, projections, and failure/recovery
paths.

Run ownership and non-interference are governed by [Chapter 75](75-scenario-run-ownership-and-non-interference.md),
which is part of this cycle rather than an optional operator convention.

It is a development contract, not merely a test script and not merely a Book-documentation artifact.

## The scenario has a wider scope than a command

A scenario may target one or more of these governed behaviors:

- a writer-facing command or alias;
- a registered Copilot capability;
- a prerequisite chain such as source acquisition → Storify → world report;
- a system boundary such as external MIDI2 control or a software peer;
- a projection that makes state legible through AX and rendered UI; or
- a refusal, failure, resume, reconnect, deduplication, or capacity outcome.

The command catalog remains the writer's entry point. A system scenario does not become a new command merely because it
exercises an existing operation through another transport or projection. Its contract names the operation it exercises
and the boundary it proves.

## Rules

1. Every scenario MUST have one stable identity, one declared target kind (`command`, `capability`, `system-boundary`,
   `projection`, or `failure-recovery`), and one explicit claim boundary.
2. The complete executable YAML scenario MUST be authored before implementation, Live Drive, or Book publication. Its
   JSON form is a checked runtime projection, never the authoring source.
3. The canonical executable scenario MUST live beside the implementation it tests in the integration repository's
   `apps/modernization-studio/LiveScenarios/` store. A Book record is a sanitized projection and must not become a
   second runtime contract.
4. A separate scenario repository MUST NOT be introduced merely to hold Reframe scenarios. It is justified only by a
   separately governed conformance program spanning products or independently owned runtimes; that decision requires a
   new authority, versioning, and synchronization contract before any move.
5. The scenario MUST declare its ordered prerequisites, actor roles, launch admission, typed actions, event-driven
   waits, terminal AX and FountainStore predicates, telemetry observations, evidence binding, cleanup, and failure or
   not-established outcomes.
6. A system-boundary scenario MUST name the actor that initiates intent and the authority that retains mediation,
   consent, lane/provider selection, execution, Store truth, and terminal completion. External peers may project
   lifecycle state but may not acquire those authorities by implication.
7. A projection scenario MUST prove semantic AX state and rendered visual state separately. A screenshot cannot supply
   semantic truth, and an AX tree cannot supply visual fidelity.
8. A failure or recovery scenario MUST be a first-class contract variant. Timeouts, refusal, unavailable capability,
   disconnect, duplicate, reconnect, and capacity outcomes must terminate explicitly; they may not be converted into a
   successful path by retrying until a timer expires or by changing the fixture silently.
9. The scenario work session MUST follow this order: resolve identity and current coverage; write or repair YAML;
   implement a bounded source slice; run focused validation; execute internally on an isolated managed Store; witness
   independently through AX/window-ID/VRT; reconcile observed evidence; then update the Book projection.
10. The internal scenario capability MAY produce behavioral receipts but MUST NOT self-approve `live-accepted`. Only
    the intersection of internal Store proof and independent surface evidence may promote a scenario.
11. The Book MUST keep command inventory, capability registry, system-capability projections, live acceptance, and
    release status distinct. A system-capability page must link to its scenario and evidence while leaving the command
    catalog unchanged when no writer-facing command exists.
12. Skills that enter scenario work MUST enforce scenario resolution first and MUST report the scenario kind, identity,
    prerequisite chain, expected terminal artifacts, source slice, coverage status, and next action before editing or
    driving.

## The single source, multiple projections

```text
integration YAML scenario + runtime implementation
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
   internal runner  Live Drive  Book projection
   Store receipt    AX/VRT      public/maintainer
          │         │         │
          └──────┬──┴─────────┘
                 ▼
          one bounded claim
```

The integration repository owns executable meaning. Reframe's internal scenario capability executes typed behavior and
records receipts. Live Drive independently witnesses the user-facing surface. The Book explains the sanitized
intersection for humans and, where authorized, provides a role-gated maintainer projection from the same reviewed
commit and digest.

## Completion condition

The cycle is complete for a scenario when the source slice, typed YAML contract, focused validation, internal receipt,
independent AX/window-ID/VRT evidence, Store read-back, provenance tuple, Book projection, and honest limitations all
agree. Completion of one scenario does not promote neighboring commands, transports, hardware claims, or release
allow-list entries.

## Governing sentence

Reframe develops by one versioned scenario at a time: executable meaning stays beside the implementation, independent
evidence stays independent, and the Book projects the resulting claim without becoming a second runtime authority.
