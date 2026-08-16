# 75 — Scenario Run Ownership and Non-Interference

Chapter 73 defines the Reframe scenario as the executable development and publication unit. Chapter 08 defines the
separate authorities that establish live acceptance. This addendum closes the missing operational boundary: a scenario
run must remain owned by its runner from preparation through terminal classification, or its evidence is invalid.

## Rules

1. Every executable scenario run MUST have one run identity and one owner. The run identity binds the scenario ID,
   source commit, executable path, Reframe PID, managed Store path, launch corpus, launch scene, and evidence root.
2. The run state MUST be one of `prepared`, `running`, `terminal-success`, `terminal-failure`, `timed-out`, or
   `invalidated`. Only the runner may advance a run from `prepared` or `running` to a terminal state.
3. A Store wait is not a timer and an empty read is not a failure. While the runner is `running`, an intermediate AX
   observation, empty query, missing receipt, or conversational acknowledgement is only an observation. It may not
   terminate or downgrade the run.
4. The runner MUST arm declared Store waits before issuing their associated AX action and MUST use the durable Store
   change feed followed by an authoritative read-back. The root `watchdogSec` is only a hang guard; expiry produces
   `timed-out`, never success and never an inferred provider failure.
5. AX probes, CoreGraphics window-ID capture, Store read-back, and telemetry inspection MAY observe a running run but
   MUST NOT alter its state, process, Store, launch environment, or evidence binding.
6. Any process kill, interrupt, relaunch, Store replacement, launch-binding change, source/executable change, or
   unrecorded coordinate/action intervention during `running` MUST append an intervention record and transition the run
   to `invalidated`. An invalidated run cannot be promoted to `live-accepted`.
7. A runner interruption MUST be distinguishable from a scenario terminal failure. The evidence bundle MUST state the
   actor, timestamp, operation, prior run state, and affected binding for every intervention or attempted intervention.
8. A scenario is `terminal-success` only when its YAML terminal predicates pass and the same run identity has matching
   AX, window-ID/VRT, FountainStore, telemetry, and provenance evidence. No assistant report, screenshot, or internal
   receipt may create success on its own.
9. A scenario is `terminal-failure` only when a declared failure predicate is observed, or when the application emits a
   typed terminal failure for the declared capability. “Not seen yet” is not failure.
10. A run that ends without a terminal state, or whose ownership/audit record is incomplete, is `not accepted` and MUST
    be rerun from a fresh preparation boundary. Partial artifacts may be retained as diagnostic evidence but must not
    be reused as acceptance proof.
11. The scenario work-session command MUST own execution, waiting, evidence capture, and final classification as one
    lifecycle. An operator or agent MUST NOT replace an active runner with ad-hoc polling, manual retries, or a second
    launcher while preserving the original run's acceptance claim.
12. Skills and operator procedures MUST say whether an action is observation-only or run-controlling before issuing it.
    They MUST never send an interrupt or kill merely because an intermediate observation appears stalled.

## Required run record

The runner records a manifest before the first AX action:

```text
runID
scenario
sourceCommit
executable
pid
windowID (when resolved)
managedStore
storeIntent
corpus
scene
owner
state
```

The run record is append-only. A terminal verifier rejects a missing manifest, a changed binding, an unexplained
intervention, or evidence captured under another run ID. A read-only observation may be attached to the run, but it may
not replace the runner's declared wait or terminal predicate.

## Governing sentence

A Reframe scenario is truthfully tested only by an owned, uninterrupted run whose declared terminal predicates and
independent evidence agree; everything observed before that point is provisional, and every intervention invalidates the
claim rather than silently changing its meaning.
