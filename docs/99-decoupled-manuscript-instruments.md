# Decoupled Manuscript Instruments — Navigation, Source, and Uncertainty

> Chapter summary: Reframe presents one manuscript through three cooperating instruments. Reading Navigation
> chooses an address, Source View renders the source faithfully, and Lane View renders the uncertainty score as an
> independent SVG canvas. They share semantic identity and source coordinates, but they do not share rendering
> authority.

## Purpose

The default manuscript surface has accumulated three different jobs in one visual area:

1. helping the writer move through the reading;
2. showing the source text; and
3. showing the uncertainty map produced by reading.

Those jobs are related, but they are not the same instrument. A navigation list must not become a second source
renderer. A source renderer must not become a score plot. A score canvas must not become a hidden text editor. The
surface becomes explainable when the relationship is explicit:

```text
persisted UncertaintyScore + source identity
             │
             ├── Reading Navigation: choose a semantic address
             │                         (lane, note, source span)
             │
             ├── Source View: render the addressed Markdown/.fountain source
             │                 with source-preserving Apple-native text
             │
             └── Lane View: render the same score as an independent SVG map
                            with animation, focus, and inspectable marks
```

This chapter extends [Chapter 79](79-default-semantic-manuscript-projection.md), [Chapter 98](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md), and the uncertainty ownership boundary in [Chapter 36](36-every-gap-keeps-its-address.md). It does not replace [Chapter 85](85-storify-source-auto-reads-a-defined-whole.md)'s
source authority or [Chapter 08](08-validation-and-acceptance.md)'s evidence authorities.

## The decision

### 1. Three instruments, one semantic spine

The instruments consume the same persisted source identity and score identity. The score's source coordinates are
the shared spine. A selection is an address, not a pixel:

```text
(sourceDocumentID, sourceDigest, laneID, noteID, startLine, endLine)
```

The exact composite identity is supplied by the current runtime contract. The important rule is that a note title,
colour, row position, or screen coordinate is never sufficient identity. This follows [Chapter 36](36-every-gap-keeps-its-address.md)'s composite-address rule and [Chapter 50](50-text-is-stored-so-it-can-be-pointed-at.md)'s
addressable text contract.

### 2. Reading Navigation owns movement through meaning

Reading Navigation is the semantic index of the visible instrument, not a second uncertainty producer. It may show:

- registered ledgers and their current states;
- lane titles and counts;
- note titles, states, details, and source ranges;
- selected-note context and the action that focuses its source span.

It must consume the complete ordered lane collection. It may not enumerate a fixed set of lane names, assume a
maximum number of lanes, or manufacture a finding because a section is empty. A missing, stale, or failed ledger
remains visible according to [Chapter 33](33-a-want-is-a-gap-in-a-ledger.md) and [Chapter 24](24-the-reasoning-is-an-uncertainty-map.md).

Navigation is allowed to request focus in Source View and Lane View. It is not allowed to draw their marks, rewrite
source text, or decide the meaning of a score state.

### 3. Source View owns readable source

Source View is the manuscript instrument. Its content authority is the admitted, source-preserving Markdown stream
with the supported `.fountain` subset described in [Chapter 98](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md). Source View may:

- render headings, prose, lists, quotes, code, notes, sections, dialogue, and other declared Fountain constructs;
- wrap and measure text using the Apple-native semantic text system;
- select, copy, scroll, and focus the exact source range named by an address;
- show line numbers and a compact source-linked indication that a score mark overlaps the line.

Source View must not:

- parse uncertainty from colour, layout, or assistant prose;
- replace source text with a summary or score label;
- change line measure because a lane has been added;
- use a lane count as a font, wrapping, or source-column multiplier;
- silently truncate source or score data to fit a visual row.

If the source has no safe rich-text projection, the declared preformatted treatment from Chapter 98 applies. Source
View remains a text view even when a score selection is active.

### 4. Lane View owns the uncertainty projection

Lane View is an independent UncertaintyScoreKit presentation. Its visual substrate is an animatable SVG canvas. SVG
is the rendering medium, not the semantic authority. The kit owns:

- ordered arbitrary lanes;
- note geometry on the shared source spine;
- state shapes, continuation, selection, focus, zoom, and animation;
- stable lane/note identity and composite selection;
- keyboard and accessibility projection of every visible mark.

The kit must not import Reframe types or learn about Copilot commands, FountainStore documents, providers, Grounding,
Storify, or paid lanes. Reframe supplies the score and the address binding; the kit supplies generic score geometry.
This is the same boundary established for UncertaintyScoreKit in [Chapter 36](36-every-gap-keeps-its-address.md).

SVG animation may express a real transition — arrival of a persisted note, focus movement, expansion, or a state
change that has been recorded. It may not manufacture progress, hide a failed reading, or imply a terminal result
that FountainStore does not contain. Reduce Motion and accessibility settings remain binding.

### 5. The relationship is semantic, not geometric

The canonical interaction is:

```text
Navigation selects (laneID, noteID)
    → Lane View focuses that address
    → Source View scrolls to startLine...endLine
    → selected context exposes the same address and state in AX
```

The reverse path is also allowed: selecting a source range may focus the corresponding score marks when the address
is unambiguous. When several lanes overlap, Source View must preserve the source range and Lane View must preserve
the composite selection; neither is permitted to collapse the overlap into one guessed meaning. If no score address
matches, Source View remains readable and Navigation reports that no finding is linked.

The instruments may be laid out side by side, stacked, overlaid, or placed in a responsive shell. Layout is not the
contract. The source address, score identity, state meaning, and focus behavior are.

## Ownership and kit boundary

| Instrument | Owns | Does not own |
| --- | --- | --- |
| Reading Navigation | semantic collection, disclosure, selection address, source-focus request | source parsing, score geometry, provider choice, Store mutation |
| Source View | source-preserving Markdown/Fountain rendering, Apple text measurement, selection and source focus | uncertainty interpretation, lane geometry, SVG animation, model routing |
| Lane View / UncertaintyScoreKit | arbitrary lanes, note geometry, state visuals, SVG animation, generic AX marks | Reframe domain wording, source custody, Copilot action, consent, persistence |
| Reframe host adapter | source/score identity binding, Store reads, domain labels, cross-instrument focus, AX composition | private duplicate score renderer, private parser, hidden second state |
| Teatro SVG projection | geometric/illustrative projections explicitly requested by a governed surface | primary source text, Markdown semantics, score authority, AX truth |

Teatro remains governed by [Chapter 98](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md):
it may project geometry, but it cannot become the readable source path. The Lane View SVG canvas is therefore not a
Teatro shortcut; it is a generic UncertaintyScoreKit surface that may later share a rendering family or host seam with
Teatro without sharing semantic ownership.

## Instrument contract

Every instrument exposes a typed, testable surface:

- stable accessibility identifier and human label;
- source identity and score generation identity where applicable;
- current selection address or explicit no-selection state;
- state and state meaning, never colour alone;
- actions for focus, expand/collapse, selection, zoom, animation pause, and reduced motion where applicable;
- a visible failure or stale state when the underlying Store evidence is missing or invalid.

The AX tree is the machine-readable UI layer. For Lane View, the SVG canvas must expose each rendered lane and note
as an accessible element or an equivalent accessible collection with role, label, value, and actions. Pixel geometry
alone is not evidence. Source View must expose source lines or semantic blocks with their exact source addresses.
Reading Navigation must expose the same composite addresses it uses to focus the other instruments.

## Acceptance order

1. Record the three-instrument scenario and its source/score identities before implementation.
2. Prove that Reading Navigation consumes arbitrary lanes and notes without fixed-name or maximum-count logic.
3. Prove that Source View renders the exact Markdown/.fountain source and that adding lanes does not change source
   measure except through the declared responsive layout policy.
4. Extract or consume the released UncertaintyScoreKit SVG boundary; do not build a Reframe-private lane canvas.
5. Prove that every score mark visible in SVG is reachable through AX and carries a composite address.
6. Prove Navigation → Lane View → Source View focus with overlapping notes, missing ledgers, failure states, and a
   source range with no matching score mark.
7. Capture AX semantics, window-ID/VRT evidence, and matching FountainStore documents separately as required by
   [Chapter 08](08-validation-and-acceptance.md). A local design mock or SVG snapshot is not live acceptance.
8. Repeat consequential focus and state transitions three times before declaring the projection live-accepted.

## Current implementation boundary

Reframe currently has a SwiftUI semantic manuscript projection with navigation beside source text and a score-backed
line-mark indication. The current diagnostic slice has shown that the source text wraps within a fixed pane and that
the compact visual braid limits painted marks; AX instrumentation is being added so omitted visual marks cannot be
mistaken for absent score data. This is implementation evidence, not a claim that the three independent instruments,
the released SVG Lane View, or the complete cross-focus contract is live.

## Related chapters

- [Chapter 18 — The Stage Presents the Act](18-the-stage-presents-the-act.md) governs legibility and progressive disclosure.
- [Chapter 24 — The Reasoning Is an Uncertainty Map](24-the-reasoning-is-an-uncertainty-map.md) governs state meaning.
- [Chapter 33 — A Want Is a Gap in a Ledger](33-a-want-is-a-gap-in-a-ledger.md) governs arbitrary ledger collection.
- [Chapter 36 — Every Gap Keeps Its Address](36-every-gap-keeps-its-address.md) governs kit ownership and composite identity.
- [Chapter 45 — Copilot Reading Surface and Typography](45-copilot-reading-surface-and-typography.md) governs the two-pane reading surface.
- [Chapter 79 — The Default Semantic Manuscript Projection](79-default-semantic-manuscript-projection.md) governs the current product projection.
- [Chapter 85 — Storify Source Auto Reads a Defined Whole](85-storify-source-auto-reads-a-defined-whole.md) governs source-reading authority.
- [Chapter 98 — Apple-Native Markdown Presentation and Transferable Engraving Rules](98-apple-native-markdown-presentation-and-transferable-engraving-rules.md) governs text parsing and Apple-native WYSIWYG rendering.

## Governing sentence

Reading Navigation chooses a source-addressed meaning, Source View renders the exact Markdown/Fountain source, and
Lane View renders the same UncertaintyScoreKit map as an independent accessible SVG instrument; they coordinate by
identity, never by duplicated authority or incidental geometry.
