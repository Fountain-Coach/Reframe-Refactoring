# Copilot Reading Surface and Typography — Situated, Legible, and Reframe-Native

> Chapter summary: Copilot belongs to Reframe's beat and uncertainty workspace. She is not a website sidebar, a book
> reader, or a diagnostic console. This chapter fixes the visual and interaction contract for a readable Copilot lane:
> the beat/uncertainty act remains primary, Copilot is a situated secondary inspector, typography is sans-serif and
> comfortable, source text keeps its monospaced treatment, and activity remains nested and quiet until it needs to be
> inspected.

## Purpose

The current Reframe surface already has a distinctive working object: uncertainty scoring above a horizontal set of
source-grounded beat cards. Copilot must make that object more useful without replacing it with a generic chat product.

Two design failures are explicitly excluded. First, a web-page composition — hero headings, navigation tabs, marketing
cards, and large empty regions — is not a Mac application. Second, literary book typography — serif display text,
chapter-title treatment, and parchment-like surfaces — is not the Reframe editor. Reframe is a working instrument for
reading, questioning, and structuring a manuscript.

## Design-review illustrations

These are generated concept illustrations, not implementation evidence. They establish the intended direction before
code changes:

![Copilot working beside the Reframe uncertainty and beat surface](illustrations/copilot-working-state.png)

*Working state: the beat/uncertainty surface remains the act; Copilot provides a readable situated proposal.*

![Copilot reduced while the Reframe beat surface remains in focus](illustrations/copilot-focused-state.png)

*Focused state: Copilot recedes to a compact inspector so the writer can stay with the beat structure.*

## The decision

1. **Reframe's beat and uncertainty surface is the act.** The score/ribbon and beat cards remain the largest and most
   central working object. Copilot may explain, propose, and act through that context; she may not visually displace it.

2. **Copilot is a situated inspector, not a web page.** Her lane is attached to the active Reframe arrangement and
   names the visible situation. It uses native macOS structure: a window toolbar, split panes, disclosure, keyboard
   access, and a dismissible or resizable inspector. No browser navigation, hero layout, or promotional framing.

3. **The interface uses sans-serif typography.** Copilot and all interface text use a clean system sans-serif in the
   SF Pro / iA Writer family of roles. Serif fonts are not used for headings, body copy, proposals, or labels. This is
   a writing instrument, not a book renderer.

4. **Source text keeps its source voice.** Fountain/manuscript excerpts remain monospaced where their source form is
   being inspected. The monospace role is not used for Copilot prose, controls, status, or explanatory text.

5. **The comfortable reading floor is a floor, not the target.** Copilot body text is at least 15 pt and is designed
   to read comfortably at approximately 17 pt with generous line spacing. Section titles are at least 15 pt; control
   labels are at least 12 pt; primary actions meet the 44 pt target. Near-black ink and high-contrast muted text are
   required in light and dark appearances.

6. **The conversation has a useful reading measure.** Copilot prose is constrained to a readable line length and uses
   paragraph spacing. A response begins near the top of the inspector and occupies only the space needed by its actual
   content. An empty white void is not a focus treatment.

7. **The proposal is conversational and situated.** When the UncertaintyScore justifies a reader-lens proposal,
   Copilot explains which visible threads produced it and offers a clear writer decision. The proposal is not a new
   baseline command surface and cannot silently mutate Grounding. Its actions are named, accessible, and governed by
   the same confirmation and persistence rules as any other capability.

8. **Activity is nested, asynchronous, and last in the Copilot lane.** Activity is the last persistent line in the
   Copilot surface, immediately above the composer or disclosure. It reports real state, can expand to details, and
   never floats as a permanent badge at the top of the writer's reading field. Long-running work may update it without
   taking over the conversation.

9. **Progressive disclosure protects focus.** The default Copilot lane exposes the two or three things the writer can
   do now: read the answer, inspect the proposal, and choose the next action. Telemetry, provider detail, lifecycle
   history, and secondary tools remain one obvious disclosure away.

10. **Reduced Copilot is a first-class state.** The writer can collapse or dismiss the inspector and return to the beat
    structure without losing the conversation or activity state. Reopening restores the same situated context from live
    application state; it does not invent context from transcript prose.

11. **AX and human legibility are both required.** Every Copilot heading, answer, proposal, button, status, disclosure,
    and composer is exposed with role, label, value, and action in the accessibility tree. AX presence does not prove
    readability: every change also requires a rendered light/dark screenshot reviewed at reading size.

12. **The illustration is not the proof.** Generated images communicate intent only. Acceptance requires the real
    Reframe window, the real beat/uncertainty state, AX semantics, window-ID capture, and persisted FountainStore
    evidence. No generated wording can be used to claim that a capability ran.

## Forbidden drift

- Serif “book” typography or literary chapter-title treatment in Copilot.
- Web navigation, hero copy, browser framing, promotional cards, or dashboard composition.
- A permanently empty Copilot pane, or a pane so dense that the beat act becomes secondary.
- Activity badges detached from the asynchronous work they describe.
- Tiny icon rows, unlabeled controls, grey-on-grey body text, or monospace Copilot prose.
- A visual redesign that changes beat identity, uncertainty meanings, source authority, or the situated Copilot contract.

## Relationship to other chapters

- **[The stage presents the act](18-the-stage-presents-the-act.md)** supplies the enforceable visual floor: glasses-test
  sizing, progressive disclosure, one act in focus, and verification by looking.
- **[The situated Copilot](15-the-situated-copilot.md)** supplies placement authority: Copilot speaks from the active
  arrangement and may not offer an object that the arrangement does not show.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** keeps beat anatomy and meaning invariant;
  this chapter changes presentation, not the beat object.
- **[Copilot capability governance](37-copilot-capability-governance.md)** binds proposals and actions to registry,
  runtime, FountainStore, telemetry, and AX evidence.
- **[Validation and acceptance](08-validation-and-acceptance.md)** governs real-window, AX, store, and visual evidence.

## Acceptance

The chapter is implemented only when a real Reframe build demonstrates:

1. the beat/uncertainty surface remains the dominant act in the working state;
2. Copilot body, headings, labels, and primary actions meet the type and contrast floors in light and dark;
3. Copilot uses sans-serif interface typography and reserves monospace for source excerpts/structured commands;
4. the proposal names visible uncertainty threads, is writer-confirmable, and does not silently alter Grounding;
5. activity remains the final nested asynchronous line and expands to real details;
6. collapsing and reopening Copilot preserves situated context without transcript inference;
7. AX exposes every visible Copilot state and action, while window-ID screenshots show human-readable presentation;
8. FountainStore and telemetry prove any claimed action, and the generated illustrations are clearly labeled as design
   references rather than runtime evidence.

## Governing sentence

Copilot is a situated Mac inspector beside Reframe's beat and uncertainty act: sans-serif, readable, progressively
disclosed, and quiet enough to preserve the writer's place; AX, rendered pixels, and persisted state must agree before
the surface or any action is claimed complete.
