# 79 — The Default Semantic Manuscript Projection

Chapters 45 and 76 define Reframe's two-pane writing instrument and the distinction between Questions, Movements, and
Read coverage. This chapter fixes how that meaning is presented by default: as a continuous, scrollable Fountain
manuscript with semantic navigation beside it, not as a page-card gallery or a horizontal timeline. The three-way
ownership and cross-focus contract is now refined by [Chapter 99](99-decoupled-manuscript-instruments.md).

## Purpose

Reframe is a manuscript instrument. The writer should be able to read the source in its own Courier/Fountain register,
scroll through it naturally, and see where the current reading found Questions, Movements, and Read coverage without
leaving the text. Copilot remains the right-hand conversational authority. The MIDI2 peer projection remains the
bottom system boundary. These surfaces compose one Reframe window; none is a second application shell.

![Signature illustration: Reframe's combined semantic manuscript workspace](illustrations/reframe-default-semantic-workspace.jpg)

*Design reference for the governed direction. This generated illustration is not runtime, AX, FountainStore, or visual
regression evidence.*

## Governing rules

1. **The manuscript is continuous.** The default left projection is one vertically scrollable Fountain reading field.
   It is not divided into A4 pages, cards, columns of passages, or artificial screen-sized units. Source line identity
   remains addressable even when the text wraps or the window is resized.

2. **Semantic navigation is adjacent, not ornamental.** A narrow navigation rail or inspector beside the manuscript
   lists the current reading's semantic units. It is a navigation projection over persisted findings, not a replacement
   for the source text and not an independent workflow.

3. **Questions and Movements remain separate.** The navigation groups source-grounded question spans and source-grounded
   changes independently. Read coverage is a third group. A question may relate to a movement, but neither is renamed,
   counted, or visually substituted for the other. The historical word `beat` may remain only as a compatibility identity;
   it is not a default UI label for either group.

4. **Units point to source spans.** Every navigable item carries its reading/lens identity, source document identity,
   start and end line, lifecycle or settlement state where applicable, provenance, and correlation identity. Selecting an
   item scrolls the manuscript to its source span and exposes its evidence in the inspector. A finding without an anchor
   stays unknown; the UI never invents one to complete a decoration.

5. **Overlap is represented by parallel semantic rows.** Questions and Movements can occupy related or overlapping source
   spans. They do not need to be forced into one timeline, one card, or one mutually exclusive lane. The navigation may
   show the two rows aligned to the same source range while preserving their distinct identities.

6. **Marks belong to the manuscript.** The left gutter and inline marks use restrained semantic colour and position to
   show source ranges. Suggested meanings are Questions in blue, Movements in green, references in amber, and unread or
   ungrounded material in red; colour is never the only signal. Marks are quiet until selected, then disclose the complete
   finding and its source evidence. No decorative bar or dense chart may replace readable text.

7. **The score is an overlay, not the default reading object.** UncertaintyScoreKit projects persisted Questions,
   Movements, and Read coverage over the manuscript. It does not redefine their semantics, create a scalar substitute,
   or require a question before a grounded Movement can appear. A diagnostic score/ribbon may be disclosed when useful,
   but it must not displace the continuous reading field or turn the default surface into a dashboard.

8. **The Reframe shell is not Slugline's shell.** Reframe does not reproduce Slugline's File, Edit, Format, Outline,
   View, Window, or Help header. The application retains its own minimal macOS title/window treatment and governed
   Reframe controls. The reference to Slugline is a visual register—quiet Courier manuscript, generous whitespace,
   stable reading column—not a dependency or an imitation of its menus.

9. **Copilot remains situated on the right.** The right pane is the sole conversational authority and retains the
   current response, composer, and nested activity state. It may explain or act on the selected semantic item, but it
   may not infer meaning from transcript prose or become a second left-side navigation authority.

10. **MIDI2 peers remain at the system boundary.** The bottom projections surface shows negotiated peer identity,
    capability, lifecycle, admission, and transport/resource state. It must not be turned into music decoration, an
    “Interpreter” persona, or a packet transcript. MIDI2 carries lifecycle; AX exposes the visible projection;
    FountainStore proves behavior.

11. **Accessibility follows the semantic projection.** The manuscript exposes readable text and source line identity.
    Each navigation group and item exposes role, label, value, identifier, source span, and actions. Selection, expand/
    collapse, scroll-to-source, and inspector state are AX-observable. A custom-drawn gutter or overlay is incomplete
    until its equivalent semantic content is in the accessibility tree.

12. **Visual and behavioral evidence stay separate.** A signature illustration communicates design intent. Acceptance of
    an implementation requires a real build, focused tests, AX observations, a CoreGraphics window-ID capture, and the
    matching FountainStore artifacts bound to one PID, executable, Store path, and source commit. A screenshot may prove
    appearance only; it never proves that a Question, Movement, peer operation, or Copilot action occurred.

## Non-goals and migration boundary

This chapter does not redefine Question or Movement identity, UncertaintyScoreKit persistence, MIDI2 contracts,
Copilot mediation, or FountainStore authority. Those remain governed by Chapters 45, 72, 73, and 76 and by the IDL and
facts. It does not require deleting historical `beat` identifiers in one change. It does require that new writer-facing
labels use Questions and Movements and that compatibility aliases cannot leak into the default presentation.

The following are not the default projection: A4 page thumbnails, source-passage cards, a horizontal time axis, a
single undifferentiated “Grounded dramatic movement” list, a permanent score dashboard, or Slugline's application
menus. They may exist only as explicitly named diagnostic or compatibility projections with their own contract and
acceptance evidence.

## Acceptance

The projection is ready to implement when a focused runtime slice can demonstrate all of the following:

- continuous Courier/Fountain text remains the dominant left-side reading surface while scrolling;
- Questions, Movements, and Read coverage are independently discoverable, collapsible, and selectable;
- selecting a semantic item moves to and highlights its persisted source span without changing its identity;
- overlapping spans remain distinct and readable;
- marks and colours have redundant labels and do not rely on colour alone;
- Copilot remains the right-hand conversational surface and MIDI2 peers remain the bottom system projection;
- AX exposes the visible semantic content and actions, while window-ID capture establishes rendered presentation;
- FountainStore read-back establishes behavior; and
- the live result matches the scenario and evidence boundary without promoting the generated illustration to proof.

## Governing sentence

Reframe's default projection is a quiet, continuous Courier manuscript with semantic navigation beside it, Copilot on
the right, and MIDI2 peers below: Questions, Movements, and Read coverage remain distinct, source-addressable, and
accessible, while design references never substitute for AX, rendered, or persisted evidence.
