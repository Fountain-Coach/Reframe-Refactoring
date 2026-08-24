# TeatroStageEngine Is the Stage — Semantic Scenography Extends It

> Chapter summary: Teatro is the broader composition and rendering ecosystem. TeatroStageEngine is its canonical
> physical stage runtime. Reframe's Semantic Scenographer must extend that stage-engine boundary where semantic
> scenography requires new stage concepts; it must not create a parallel RealityKit scene authority, a private SVG
> renderer, or a second Teatro-like engine.

## Purpose

Chapter 100 established Semantic Scenographer as a downstream Reframe instrument: Reframe establishes what is there;
the scenographer proposes how relations might exist in space; Teatro scores and renders that proposition. This chapter
resolves the implementation boundary that Chapter 100 left open.

The answer is not to assemble unrelated rendering stacks. The answer is to use the Teatro system we own and extend its
canonical stage runtime where the current stage model does not yet express the scenographer's needs.

The governing distinction is:

```text
Teatro                 = composition, rendering, animation, and host ecosystem
TeatroStageEngine      = canonical physical stage runtime
Semantic Scenographer  = Reframe interpretation and source-addressed stage proposal
```

## What Teatro means

Teatro is the wider Fountain Coach composition and rendering family. Its existing responsibilities include:

- composable view and layout structures;
- Fountain and Markdown-adjacent parsing and projection;
- storyboard and animation models;
- SVG, HTML, Markdown, Fountain, and other renderer surfaces;
- MIDI2 and audio integration;
- GUI, CLI, and renderer-plugin hosts;
- related vector, layout, animation, and stage packages.

Teatro is therefore an ecosystem and integration boundary, not one monolithic engine and not one mandatory visual
surface. A Teatro projection may be text, vector, animated SVG, a stage, or another governed renderer.

## What TeatroStageEngine means

TeatroStageEngine is the concrete domain engine for the Teatro stage. It owns the physical and geometric semantics of
the stage, including:

- a deterministic world and timestep;
- bodies, gravity, damping, constraints, and floor contact;
- the Fadenpuppe rig and its topology;
- stage-room geometry, including floor, walls, and door;
- the canonical camera model and input bounds;
- the paper-stage visual constants that hosts are expected to respect;
- snapshots, replay/interchange shape, and engine-level invariants.

The stage engine is renderer-agnostic. It does not own Reframe source meaning, Copilot mediation, uncertainty
interpretation, provider selection, or publication. It supplies a stable stage world to hosts such as a web renderer,
an SVG view, or a future native host.

The distinction matters because the current Teatro package and the current TeatroStageEngine package solve different
problems. Teatro's generic `Stage`, `Renderable`, and renderer types do not constitute a semantic 3D scene graph.
TeatroStageEngine's puppet world does not constitute a source-addressed semantic score. Neither may be treated as if it
already supplied the missing boundary.

## The decision

### 1. TeatroStageEngine remains the stage authority

Semantic Scenographer does not introduce a parallel scene authority. When a proposal requires a stage entity, world
position, camera state, trajectory, field, threshold, or temporal stage state, the proposal is expressed through a
versioned TeatroStageEngine extension or a thin adapter to an admitted engine capability.

The engine specifications remain first: a change to stage semantics begins in the relevant TeatroStageEngine spec,
then the engine implementation, tests, hosts, and instrument projections are aligned.

### 2. Semantic Scenographer remains the interpretation authority

Reframe remains responsible for resolving the exact source address and admitted context, asking the scenographic
question, and recording that the result is a proposal. TeatroStageEngine must not infer source meaning from labels,
colours, layout, or assistant prose.

The chain is:

```text
source / beat / uncertainty address
            ↓
Reframe semantic context
            ↓
Semantic Scenographer proposal
            ↓
TeatroStageEngine composition/state
            ↓
Teatro renderer or host
```

### 3. No competing RealityKit authority

Apple frameworks may be used by a host where they provide a useful native projection. RealityKit, SpriteKit, SwiftUI,
Metal, Core Graphics, or another renderer may not become a second semantic or physical authority merely because it
offers entities, nodes, animation, or physics.

If RealityKit is used, it is an adapter-backed projection of a stored TeatroStageEngine composition. RealityKit entity
state is not the persisted score, and RealityKit physics is not silently substituted for the canonical stage physics.
Any future backend substitution requires an explicit engine contract, parity evidence, and a governed migration.

### 4. Semantic extensions belong at the engine boundary

The first implementation question is not “which graphics API should draw this?” It is “what stage concept is missing?”
Possible extensions include a generic stage entity, a field or zone, a boundary or threshold, a path or trajectory,
an annotation, a composition variant, and a deterministic temporal state. Each extension must be specified before it is
added and must remain useful to more than one renderer or host where practical.

### 5. Source provenance travels with the proposal

TeatroStageEngine may receive provenance-bearing composition metadata, but it does not become the authority for that
metadata. A stage object that originates in Reframe carries a stable relationship to:

- source document identity and source digest;
- exact source range;
- beat, movement, lane, note, or composite address where applicable;
- proposal and instrument versions;
- engine composition version and renderer parameters.

An object without an unambiguous source address remains explicitly unlinked proposal material. It must not attach itself
to a nearby passage by visual or geometric proximity.

## The extension boundary

The proposed contract is a structured, serializable stage composition. It is not a flattened image and not a private
SwiftUI view tree.

```text
ScenographicComposition
 ├── stage configuration
 ├── entities and semantic roles
 ├── relations and constraints
 ├── trajectories and temporal states
 ├── source/provenance references
 ├── variant identity
 └── engine and renderer parameters
```

The initial vocabulary may include:

```text
figure · object · field · zone · distance · threshold · boundary · axis
entry · exit · void · density · isolation · cluster · witness
foreground · background · trajectory · pause · repetition · overlap
containment · exposure · concealment
```

These are declared compositional roles. They are not new uncertainty states, source facts, or hidden classifications.

The stage engine should expose only the operations needed to create, inspect, update, compare, sequence, and replay a
composition. A large general-purpose graphics API is not a scenographer contract.

## Ownership

| Boundary | Owns | Must not own |
| --- | --- | --- |
| Reframe | source address, semantic context, Copilot mediation, proposal identity, Store lineage | engine physics, renderer internals, source mutation through a projection |
| Semantic Scenographer Kit | structured proposal, roles, relations, variants, provenance references | source authority, uncertainty authority, host UI, provider policy |
| TeatroStageEngine | stage entities, geometry, constraints, physics, camera, snapshots, deterministic stage state | source interpretation, Copilot routing, uncertainty meaning |
| Teatro host/renderer | visual projection, interaction bridge, animation presentation | semantic authority, hidden source rewriting, invented evidence |
| Apple/native adapter | platform rendering, input, and host integration | a second persisted scene or physics authority |

This keeps Chapter 99's three manuscript instruments intact. Reading Navigation chooses the address; Source View keeps
the exact source readable; UncertaintyScoreKit remains the internal uncertainty model projection. TeatroStageEngine is
downstream of those authorities and does not become a second navigation surface.

## Composition and physics

Not every scenographic relation is physical. A “distance” may be a stage-engine distance, a symbolic separation, or an
unresolved relation represented by a declared field. The composition must state which kind it is.

- Physical entities use TeatroStageEngine world coordinates and constraints.
- Symbolic entities use a declared projection grammar and do not masquerade as bodies in the physics world.
- Temporal changes use the engine's deterministic stepping or an admitted animation contract.
- A renderer may exaggerate a relation for legibility only when that transformation is declared as presentation, not
  persisted as physical fact.

The Fadenpuppe rig remains the first canonical physical stage, not the universal semantic ontology. New generic stage
objects must not destabilize existing rig invariants merely to make a diagram convenient.

## Determinism and persistence

The interpretive act and the stage projection remain separate artifacts:

```text
semantic interpretation
        → stored structured composition
        → deterministic engine state / snapshot
        → deterministic render
```

Replaying the same composition with the same source identity, instrument version, engine revision, timestep, and
renderer parameters must produce the same stage state within the declared backend tolerance. A changed interpretation
creates a distinct proposal or variant; it does not overwrite source truth or uncertainty truth.

The Store records the composition and its provenance separately from the manuscript. A screenshot, animation frame, or
RealityKit entity tree is not sufficient persistence or acceptance evidence.

## Initial implementation scope

The first engine extension should remain narrow:

1. Define the composition and provenance schema in the owning TeatroStageEngine specification.
2. Add the smallest engine model for source-addressed stage entities and declared spatial relations.
3. Preserve existing puppet, room, camera, physics, and snapshot invariants.
4. Provide one deterministic host projection, preferably the existing Teatro stage host.
5. Make each linked object selectable and return the same address to Reframe.
6. Support one alternative composition without promoting it to a canonical reading.
7. Persist the score, engine revision, renderer parameters, and digest separately from source and uncertainty data.

The first proof is not an attractive stage. It is one exact passage becoming one inspectable, traceable, replayable
stage proposal without changing the passage or uncertainty state.

## Explicit non-goals

This chapter does not authorize:

- a parallel RealityKit or SpriteKit semantic engine;
- replacing TeatroStageEngine physics with a host's default physics;
- treating generic Teatro text views as a semantic spatial model;
- inventing source facts, uncertainty states, or dramatic conclusions;
- making Lane View a scenographic surface;
- flattening proposals into image generation before storing the structured composition;
- publishing a live capability or claiming that the engine extension already exists.

## Acceptance order

Acceptance must prove, in order:

1. the TeatroStageEngine specification names the new composition boundary;
2. the engine and tests preserve existing stage and rig invariants;
3. a stored composition contains exact source identity and declared roles/relations;
4. the same composition replays deterministically;
5. every linked stage object exposes stable identity and can focus the corresponding Reframe address;
6. missing or ambiguous source context is visible and does not produce a guessed object;
7. variants remain distinct and do not mutate source or uncertainty authority;
8. AX, window-ID/VRT, and FountainStore evidence agree for the live host;
9. any native Apple renderer is proven as an adapter and not as a second authority.

A design illustration, a four-field placeholder, a renderer snapshot, or a successful model response cannot establish
this acceptance.

## Relationship to existing governance

This chapter extends [Chapter 100](100-semantic-scenographer.md) by fixing the Teatro/TeatroStageEngine boundary. It
retains [Chapter 99](99-decoupled-manuscript-instruments.md)'s source and uncertainty separation and [Chapter 98](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md)'s
prohibition on making a geometric renderer the text authority. [Chapter 93](93-instrument-creation-is-a-governed-promotion-path.md)
governs the instrument's scenario-first creation and release. [Chapter 08](08-validation-and-acceptance.md) governs
the evidence required before any live claim.

## Governing sentence

Reframe proposes source-addressed spatial relations, TeatroStageEngine remains the canonical stage runtime, and Teatro
hosts render the resulting composition; no Apple framework, generic renderer, or projection may become a competing
semantic or physical authority.
