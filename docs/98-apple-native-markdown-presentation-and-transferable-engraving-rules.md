# Apple-Native Markdown Presentation and Transferable Engraving Rules

> Chapter summary: Reframe's Copilot output is a semantic Markdown stream presented by an Apple-native text surface.
> The reusable policy is an injectable FCIS-KIT boundary. General rules learned from musical engraving may govern
> spacing, wrapping, collision avoidance, and optical hierarchy; musical ScoreKit notation and Teatro SVG remain
> separate projections and never become the authority for readable text.

## Purpose

Reframe is judged at the point where a writer reads the Copilot response. A typed result that is correct in a Store but
arrives as a wall of literal markers is not a finished instrument. The needed contract is not a cosmetic card pass and
not a second semantic parser hidden in the view. It is a complete path:

```text
typed mediation result
  → deterministic Markdown stream
  → Markdown/Fountain semantic document
  → presentation roles and layout decisions
  → Apple-native text rendering
  → AX and rendered window
```

The source Markdown stream remains inspectable and preservable. The rendered surface may improve measure, grouping,
spacing, and hierarchy, but it may not rewrite the content or invent a meaning that the stream did not contain.

## The decision

1. **Markdown is the content interchange.** A command result emits a properly formatted Markdown stream. The supported
   Markdown subset is parsed into typed blocks and inline spans before presentation. Literal Markdown markers are not a
   successful rendering of headings, emphasis, lists, quotes, links, code, or thematic breaks.

2. **Fountain is a supported semantic subset, not a competing text universe.** `.fountain` screenplay constructs,
   notes, sections, dialogue, action, and preformatted regions remain parseable and preservable. A Fountain block that
   has no safe rich-text projection is shown as an explicit preformatted block; it is never silently flattened or
   discarded.

3. **Apple-native text is the WYSIWYG authority.** SwiftUI/AppKit text, their named semantic styles, measurement,
   wrapping, selection, Dynamic Type/accessibility behaviour, and platform shaping render the readable surface. A
   screenshot is visual evidence of that surface; it is not a parser, a source of meaning, or a replacement for AX.

4. **The Composer is the input instrument.** The bottom text input field is the writer's Composer. It accepts the same
   governed turn surface and AX contract as the canonical Reframe Composer. It is not the assistant's output and it is
   not permitted to parse or reinterpret the assistant's response as a second authority.

5. **Presentation policy is injectable, not preference-driven.** A role-based policy may select font register, size,
   leading, measure, grouping, block spacing, list indentation, and code treatment for a destination. Reframe reasons
   these values from the active surface and accessibility state; the writer does not maintain a typography preference
   panel. Export destinations may use a book or print policy; the working Copilot surface remains governed by Chapter
   45's screenplay instrument register.

6. **Engraving principles transfer only where they are domain-independent.** A text surface may reuse rules for
   measured line breaking, keep-together constraints, collision priority, optical scaling, baseline/leading rhythm,
   and overfull diagnostics. The transfer is a layout policy, not a claim that prose is music.

7. **ScoreKit remains a score instrument.** Musical notation models, staff geometry, beams, accidentals, SMuFL glyphs,
   note spacing, and score-specific vertical alignment belong to ScoreKit and its renderer. They may produce a score or
   uncertainty projection when explicitly requested, but they must not be imported into the Copilot Markdown renderer.

8. **Teatro SVG remains a geometric projection.** Teatro may decorate or illustrate a presentation surface. It does not
   replace Apple text shaping, selection, AX exposure, copy/paste, accessibility scaling, or Markdown semantics.

9. **No model call decides ordinary line breaks.** Semantic reasoning may author or structure content when the governed
   operation calls for it. Wrapping, sentence grouping, block spacing, and overflow are deterministic layout concerns;
   they must not be delegated to a model merely to repair a renderer.

## Ownership and kit boundary

| Boundary | Owns | Must not own |
| --- | --- | --- |
| `FountainMarkdownPresentationKit` | Markdown/Fountain subset parsing, typed blocks/spans, source-preserving serialization, deterministic stream projection, fixtures | SwiftUI views, Reframe session state, provider choice, window evidence |
| Future `FountainTextLayoutKit` | Role tokens, measured layout policy, line/group decisions, keep-together and overflow diagnostics, injectable policy protocols | Markdown meaning, Copilot transcript authority, AppKit/SwiftUI view ownership |
| Apple presentation adapter | Native text styles, font/metric resolution, shaping, selection, accessibility scaling, platform text controls | Content mutation, semantic inference, provider/lane selection |
| Reframe | Mediation, command identity, Composer, Copilot placement, AX identifiers, FountainStore, live acceptance | A private duplicate of the released parser or layout contract |
| ScoreKit / RulesKit | Musical domain model and general engraving rule sources | Copilot prose rendering or Reframe product state |
| Teatro | Geometric/SVG visual projections | Primary text, selection, Markdown parsing, or AX truth |

The first three boundaries may be released as separate FCIS-KIT libraries or as a deliberately versioned family. The
package names, repository ownership, semantic version, and MIDI2 operation identities are implementation decisions to
be recorded before extraction. Until a release exists, a local package is a candidate boundary only; it is not a
published kit claim.

## Rules for the transferable layout policy

The policy must operate on typed semantic blocks and measured platform metrics. It may declare:

- block roles and hierarchy, including headings, labels, prose, quotes, lists, code, notes, and Fountain regions;
- sentence-aware grouping where the source has no stronger block boundary;
- line measure, leading, paragraph separation, list indentation, and code/preformatted treatment;
- keep-together and widow/orphan decisions where the destination supports them;
- collision priority and visible overflow/overfull diagnostics;
- optical-size adjustments that preserve the selected role and remain accessible;
- deterministic fallback behaviour for malformed or unsupported input.

It must not:

- inspect rendered pixels to recover semantics;
- merge blocks solely because a view is short of space;
- silently drop content, truncate by byte/token count, or hide overflow;
- use a musical glyph, staff, note, or score alignment rule as a prose meaning rule;
- turn a layout decision into a provider, lane, command, or Store mutation;
- replace the source stream with a generated “pretty” transcript.

## Apple implementation contract

The production adapter uses Apple's semantic text system rather than a hand-drawn glyph surface. It resolves named
roles against platform text styles and preserves the working register required by Chapter 45. Courier or its documented
system-monospace fallback is used for Copilot prose, Composer text, structured command text, and Fountain material where
that chapter applies; system labels and surrounding application chrome retain their system roles. Hard-coded font sizes
may not bypass the platform's accessibility scaling or role hierarchy.

The adapter must expose the same semantic blocks that it renders. Headings, labels, list items, code, notes, links,
Composer content, status, and overflow are individually reachable through AX with role, label/value, and action where
applicable. Copy, selection, keyboard navigation, contrast, light/dark appearance, and readable measure are part of the
surface, not optional polish.

## Acceptance order

1. Declare the supported Markdown/Fountain grammar and malformed-input fixtures in the owning presentation kit.
2. Prove that the parser produces typed blocks/spans while preserving the exact source stream.
3. Extract only domain-independent layout rules into a versioned, rendering-neutral kit boundary.
4. Implement the Apple adapter and keep all Reframe-specific mediation, Store, and AX ownership in Reframe.
5. Test headings, emphasis, code, links, quotes, ordered/unordered lists, thematic breaks, Fountain notes/sections,
   preformatted regions, sentence grouping, long lines, malformed input, and accessibility-size variants.
6. Drive the real Reframe surface through AX, inspect the window-ID capture at reading size in light and dark, and read
   the matching FountainStore round. The exact Markdown stream, semantic block identity, AX state, pixels, and Store
   receipt must agree.
7. Repeat consequential acceptance three times before calling the presentation capability live-accepted. A formatted
   screenshot alone cannot establish parser correctness, kit release, or command execution.

## Forbidden drift

- Treating assistant prose, screenshots, or a view's attributed string as the semantic source.
- Calling the Composer the Copilot output, or making a dedicated command composer diverge from the canonical Composer.
- Solving Markdown readability with rounded cards while literal markers or block identity remain unresolved.
- Making Teatro SVG, Core Graphics drawing, or custom glyph placement the primary text path.
- Pulling unstable, unreleased musical RulesKit/ScoreKit APIs into the Copilot presentation boundary.
- Introducing a typography preference that makes the writer manage an internal rendering decision.
- Claiming Apple, RulesKit, ScoreKit, Teatro, or a future FCIS-KIT adapter is implemented or live-accepted merely
  because this chapter names its boundary.

## Relationship to other chapters

- **[Copilot Reading Surface and Typography](45-copilot-reading-surface-and-typography.md)** fixes the Reframe
  working register, placement, hierarchy, measure, and human-legibility floor.
- **[Parse Before You Ask](27-parse-before-you-ask.md)** supplies the rule that declared text boundaries are parsed
  and measured before semantic reasoning is asked to infer anything.
- **[The Stage Presents the Act](18-the-stage-presents-the-act.md)** supplies the visual review and progressive-
  disclosure floor.
- **[The Apple-Native Semantic Pipeline Is One MIDI2 Graph](86-apple-native-semantic-pipeline-is-one-midi2-graph.md)**
  supplies Apple measurement, typed handoff, portable kit ownership, and receipt lineage.
- **[The FCIS-KIT Instrument Store Is the Capability Plane](91-fcis-kit-instrument-store-is-the-capability-plane.md)**
  supplies kit identity, admission, release, and consumption boundaries.
- **[Validation and Acceptance](08-validation-and-acceptance.md)** supplies AX, window-ID, Store, and claim-specific
  evidence authority.
- **[Decoupled Manuscript Instruments](99-decoupled-manuscript-instruments.md)** applies this text boundary to the
  Source View and separates it from Reading Navigation and the independent SVG Lane View.

## Current implementation boundary

`FountainMarkdownPresentationKit` is the current released parser/presentation-stream boundary used by Reframe. Its
NaturalLanguage sentence grouping and the Courier-Land Copilot surface are implementation evidence for the problem
this chapter governs, not evidence that a generalized text-layout kit, ScoreKit integration, Teatro adapter, or complete
WYSIWYG acceptance exists. Those remain explicitly bounded implementation slices.

## Governing sentence

Reframe emits semantic Markdown, parses it into source-preserving blocks, lays those blocks out by transferable rules,
and renders them through Apple's accessible text system; ScoreKit and Teatro may project their own domains, but neither
may become the Copilot's text authority.
