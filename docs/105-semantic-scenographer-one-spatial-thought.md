# Semantic Scenographer — One Spatial Thought in Reading Order

> Chapter summary: Reframe may mark the moment when a source-addressed reading produces a spatial proposition. The
> writer-facing surface exposes one quiet spatial-thought marker, while the structured semantic scene, its variants,
> and its projections remain inside Semantic Scenographer and TeatroStageEngine.

![Principal illustration: a reading-order marker opens a source passage into a structured spatial thought](illustrations/105-semantic-scenographer-one-spatial-thought.png)

*Principal illustration — a design reference for the reading-order marker and its spatial consequence. It is not live
acceptance evidence and does not claim that a persisted scene, AX action, or Teatro runtime exists.*

## Purpose

Chapter 100 established Semantic Scenographer as a downstream Reframe instrument. Chapter 101 placed its stage
realization inside TeatroStageEngine. The supplied implementation brief resolves the remaining product question:
what should the writer actually see?

Reframe is not an illustration application. It should not teach a new icon alphabet for fields, trajectories,
thresholds, projections, or semantic roles. It should mark one thing only: at this exact point in reading order,
Reframe has a spatial thought that the writer may inspect.

The governing distinction is:

```text
reading order and source address
              ↓
      spatial thought exists
              ↓
structured semantic 3D scene
              ↓
  TeatroStageEngine projection
```

The marker is a reading-order fact about an available proposal. It is not a miniature stage, a tool picker, a quality
score, or a claim that the source literally contains the geometry proposed by the scene.

## The decision

The writer-facing reading surface exposes one stable spatial-thought marker at the exact semantic address where an
admitted scenographic proposition exists. Its label and surrounding text must make the address and status available
through AX; the glyph alone is never semantic authority.

The internal system may choose a plan, perspective, section, temporal score, storyboard, memory-vector, or another
projection. That choice belongs to Semantic Scenographer and TeatroStageEngine. It does not become a permanent
writer-facing grammar unless a later governed scenario proves that a new control is necessary.

### What the marker means

| State | Writer-facing behavior |
| --- | --- |
| Absent | No marker: no admitted spatial thought exists at this address. |
| Available | One marker appears at the exact reading-order address. |
| Focused | Activating it opens or focuses the linked spatial thought without changing source truth. |
| Revising | Ordinary activity text may show that a separate proposal is being revised. |
| Failed or stale | The state is exposed textually and accessibly; a stale thought is not shown as current. |

The marker refers to a `SpatialThoughtReference`, not directly to a renderer:

```text
SpatialThoughtReference {
    id
    sourceDocumentID
    sourceDigest
    sourceRange
    semanticAddress?
    compositionID
    proposalVersion
    createdInReadingOrder
    status
}
```

The exact type belongs to the owning FCIS-KIT contract. The invariant is identity: a marker opens a structured,
source-addressed thought, and that thought can return to its source address.

## Spatial thinking is relation, not decoration

The scenographer must not merely draw labels such as `DISTANCE`, `THRESHOLD`, or `FIELD` over a picture. A spatial
relation is meaningful only when it changes the scene's state or can be inspected as a relation.

```text
weak:   a label says “distance”
strong: positions and geometry produce a measurable distance

weak:   a circle is labelled “threshold”
strong: a boundary has a passage state and can be traversable or blocked
```

The structured scene may contain figures, objects, fields, zones, boundaries, thresholds, voids, axes, trajectories,
visibility relations, and temporal states. These are internal compositional primitives. They are not a new global icon
language for the writer.

## Authority and persistence

Source View remains exact source authority. Reading Navigation establishes the starting address. UncertaintyScoreKit
remains uncertainty authority. Semantic Scenographer proposes spatial relations; it may not invent, close, or conceal
uncertainty. TeatroStageEngine realizes the structured stage; it does not infer source meaning.

Persist the structured composition separately from the manuscript and uncertainty state. At minimum, persistence must
retain composition identity, source digest and range, proposal and instrument versions, engine revision, variant
identity, and sufficient renderer/view parameters for deterministic inspection.

The scene may have multiple projections and revisions, but those are not multiple source authorities. A linked stage
object without an unambiguous source address remains explicitly unlinked proposal material; it must not attach itself
to a nearby passage by visual or geometric proximity.

## Blank-page coaching guardrail

The marker may teach the writer what spatial consequence became available in a passage. It must never become a reward
signal or a proxy for writing quality.

Reframe must not show counts, streaks, density targets, badges, rankings, praise loops, or recommendations designed to
produce more or earlier markers. Some writing is interior, sonic, discursive, suspended, or deliberately
indeterminate. The absence of a marker is not a deficiency.

The valid coaching question is:

> What changed in the space because I wrote this?

The answer may describe occupancy, distance, orientation, entrance, exit, obstruction, visibility, withheld movement,
territory, absence, or a changed spatial condition. It may not grade the writer for generating the marker.

## Acceptance order

The first bounded acceptance scenario must:

1. select one exact source range during the normal governed reading flow;
2. resolve the same source and semantic address used by Reframe;
3. create one scenographic proposal from that address;
4. persist one structured TeatroStageEngine-backed composition;
5. expose exactly one spatial-thought marker at that reading-order moment;
6. activate the marker and open a suitable projection;
7. select a linked scene element and navigate back to the exact source range;
8. revise the spatial proposition as a distinct proposal without mutating source or uncertainty state;
9. reopen the persisted thought and prove stable identity and provenance; and
10. capture AX, window-ID, MIDI2, and FountainStore evidence separately.

The proof is not that Reframe can draw a stage. The proof is that, at one exact moment in reading order, Reframe can
create, preserve, reopen, and interrogate a source-addressed spatial thought.

## Explicit non-goals

- no generic screenplay-editor redesign around Teatro;
- no permanent Plan, Section, Perspective, Field, or Trajectory toolbar;
- no writer-facing icon alphabet for Teatro semantics;
- no flattened image as the only persisted result;
- no competing scene, physics, or source authority outside TeatroStageEngine and Reframe's existing authorities;
- no silent source mutation caused by a scenographic revision;
- no reward loop equating marker frequency with better writing.

## Relationship to existing governance

This chapter refines [Chapter 100](100-semantic-scenographer.md)'s writer-facing boundary and depends on [Chapter
101](101-teatro-stage-engine-semantic-scenography.md)'s stage authority. It retains [Chapter
99](99-decoupled-manuscript-instruments.md)'s separation of Reading Navigation, Source View, and uncertainty
projection, and [Chapter 98](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md)'s text
authority. [Chapter 93](93-instrument-creation-is-a-governed-promotion-path.md) governs creation and promotion of the
instrument. [Chapter 08](08-validation-and-acceptance.md) governs evidence and claim boundaries.

## Governing sentence

Reframe reads in order; when that reading produces a scenographic proposition, it marks the exact semantic address
with one spatial-thought marker, whose activation opens a source-addressed semantic scene realized by TeatroStageEngine;
the marker may teach spatial consequence, but it is never a tool grammar, reward signal, or proxy for writing quality.
