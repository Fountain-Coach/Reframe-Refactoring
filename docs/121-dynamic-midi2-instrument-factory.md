# 121 — The Dynamic MIDI2 Instrument Factory

> Chapter summary: Reframe discovers and uses admitted MIDI2 instruments through a generic host boundary. A Swift
> Instrument Factory creates new instruments in a governed build environment; it does not turn every new instrument
> into a compiled switch case in Reframe.

![Principal illustration: Reframe discovers admitted MIDI2 instruments through a generic boundary while a Swift factory builds new instruments in a pinned Linux image and records evidence in FountainStore](illustrations/121-dynamic-midi2-instrument-factory.svg)

*Principal illustration — a deterministic vector governance projection. It explains the intended boundary; it is not a
build receipt, an admission result, or proof that the dynamic registry is already complete.*

## The decision

Reframe SHALL host one generic MIDI2 instrument boundary. New admitted instruments SHALL be discoverable by their
typed MIDI2 profiles and invocable through the shared operation contract. Reframe MUST NOT require a new compiled
per-instrument dispatch switch merely because the estate gains another instrument.

The Instrument Factory SHALL be a separate FountainCoachMaintenanceKit-owned MIDI2 instrument. It SHALL create,
validate, build, test, admit, and record instruments in batches. It is a creation and promotion boundary, not a second
runtime or an authority that can self-admit its output.

```text
human intent → Reframe Composer → MIDI2 discovery/invocation → admitted profiles
                                      │
                                      └── generic Reframe dispatch

factory request → pinned Swift Linux image → artifact + tests + Store evidence
```

## Runtime use without a Reframe rebuild

An admitted profile declares stable identity, operation, inputs, outputs, lifecycle, terminal predicates, evidence
authorities, and claim boundary. The Composer reasons over that profile and invokes the shared operation boundary.
Reframe does not import the instrument source or learn a private command vocabulary.

Runtime use requires the generic host, an admitted discoverable profile, IDL-conforming operations, Composer-visible
traits, and shared lifecycle/Store evidence. This is runtime composability, not compiler magic: a genuinely new Swift
implementation still needs compilation and promotion somewhere, but not a new Reframe switch case.

## The speed factory

The factory accepts a batch of named instrument intents. It resolves contracts once, reuses unchanged artifacts from a
content-addressed local cache, validates independent work in parallel, builds shared Swift products once, runs one
consolidated acceptance matrix, and persists per-instrument results in FountainStore.

Caching may optimize unchanged work, but never substitutes for changed-contract validation, admission, or evidence.
The human result explains requested intent, reuse, performed work, observed predicates, unresolved claims, and the next
bounded action.

## Swift and Linux

The factory core SHALL be portable Swift on macOS and Linux. A pinned Linux Swift image is the preferred headless build
lane for portable instruments. Toolchain, source revision, dependency resolution, artifact digests, tests, and
admission belong in the receipt. The portable core does not import AppKit, SwiftUI, Accessibility, CoreGraphics,
Metal, WebKit, Foundation Models, Keychain, or assume a graphical session.

No Node, npm, GitHub Actions, hosted runner, or network-only service may be required for factory correctness. macOS
AX, window-ID, and visual acceptance remain host-specific witnesses for writer-facing surfaces.

## MIDI2 and FountainStore

MIDI2 carries discovery, operation requests, lifecycle, correlation, and compact result references. Large artifacts are
addressed by digest through the governed Store/artifact boundary. FountainStore is authoritative for factory plans,
identities, lifecycle, terminal evidence, admission, release provenance, and resumable failures.

A remote instrument becomes usable when its MIDI2 profile is admitted and its Store receipt establishes the matching
contract and artifact identity. Reframe then discovers and invokes it through the generic host boundary.

## Migration from the compiled switch

The current per-instrument switch is a migration seam. The migration order is:

1. define generic MIDI2 discovery and invocation;
2. expose current instruments through it without changing identity or evidence;
3. add registry resolution, compatibility checks, and missing-instrument requests;
4. move instrument-specific dispatch behind host adapters or admitted profiles;
5. prove a newly admitted instrument can be discovered and invoked without changing Reframe source; and
6. remove obsolete switch branches only after negative search, focused tests, and live Store/MIDI2 evidence.

The migration MUST NOT create a “run anything” escape hatch, infer an instrument from a filename, or make a chat
proposal executable by assertion.

## Current boundary

This chapter defines the target architecture. The first estate publication-data instrument is admitted through a
typed Swift adapter and live-proven through MIDI2 and FountainStore. The generic dynamic registry and batch factory
still require their own implementation and acceptance. This chapter therefore makes no claim that arbitrary new
instruments are already usable without a Reframe rebuild.

## Governing rules

1. Reframe uses one generic MIDI2 instrument boundary and does not grow a per-instrument switch indefinitely.
2. The Instrument Factory is a governed FountainCoachMaintenanceKit instrument with durable evidence.
3. Runtime use of an admitted conforming instrument does not require recompiling Reframe.
4. New Swift implementations still require a compiler, preferably in a pinned portable Linux build image.
5. MIDI2 carries discovery, commands, lifecycle, and references; FountainStore carries durable proof.
6. Node, npm, GitHub services, hosted CI, and network-only dependencies are excluded from factory correctness.
7. Caching may remove unchanged work, never changed-work validation or evidence.
8. Missing profiles become explicit missing-instrument requests; behavior is never silently substituted.
9. macOS AX and visual acceptance remain host-specific witnesses.

## Governing sentence

Reframe remains stable while a portable Swift factory creates and promotes new MIDI2 instruments with evidence, and
the Composer discovers and uses those admitted instruments through one generic boundary.
