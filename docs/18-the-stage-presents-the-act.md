# The Stage Presents the Act — Legibility Over Density

> Chapter summary: A Reframe surface is a **presentation of the act the writer is performing** — reading, segmenting, composing a cut — not a control console that happens to hold the data. This chapter fixes the visual doctrine that keeps being violated: the act being performed must be the **largest, most central thing on screen**; type and hit targets must pass the **glasses test**; per-object machinery is **progressively disclosed**, never a permanent row of hieroglyphs; only **one act is in focus at a time**; a relationship the writer reasons about is **drawn, not implied**; and every UI change is **verified by looking** at the rendered view, in light and dark, at reading size. It states enforceable rules, not decoration.

## Purpose — the failure this exists to end

The Cut lens was built correctly and verified wrongly. Every capability had a handle, each handle passed an accessibility-tree check (`find` / `press` / `count`), and the whole thing was **illegible**: 9–10px icon rows in every beat-card header, miniature cut chips with sub-10px controls, the story arc, the beats chart, four dense monospace cards, a cut strip, a music lane, a transport, and the Copilot all on screen at once — with the *thing being composed* the smallest element present. The writer's verdict was exact: *"tiny, crowded, suffocated — nothing for somebody who may need a pair of glasses."*

Two mistakes produced it. First, the surface was built as a **console** (everything, always, small) rather than a **stage** (the act, large, central) — the very thing [chapter 17](17-the-score.md) decision 8 forbids ("the Score opens simple… never an eight-lane console the writer did not ask for"). Second, verification checked that a control **existed in the accessibility tree**, which proves a machine can find it and proves nothing about whether a human can see or use it. Accessibility has two halves; the agent half passed while the human half — legibility — failed.

## The principle — the surface is the act, presented

A writer opening Reframe is not operating a mixing desk; they are **doing something to their story** and need to see it happen. The surface's job is to present that act with enough size, space, and focus that it reads at a glance and is operable by someone who wears glasses. Density is not sophistication; it is the failure mode. Space and size are not waste; they are the presentation.

## The decision (enforceable rules)

1. **The act is the star.** Whatever the writer is performing right now — the beats they are reading, the cut they are composing — is the **largest and most central** element on the surface. Chrome, meters, and secondary lanes are peripheral by size and position. If the thing being composed is smaller than the tools that act on it, the surface is wrong.

2. **The glasses test — a legibility floor.** Anything a writer **reads or acts on** meets a minimum:
   - source/body text a writer reads: **≥ 13 pt**;
   - a beat/section **title**: **≥ 15 pt**;
   - a control's **label**: **≥ 12 pt** (icon-only controls carry a real label in the accessibility tree AND a visible tooltip);
   - a control's **hit target**: **≥ 28 × 28 pt** (a primary action **≥ 44 pt** tall).
   A row of sub-12px glyphs is a defect, not a toolbar. If a control cannot meet the floor where it is, it does not belong there — it belongs behind progressive disclosure (rule 3).

3. **Progressive disclosure — never a console.** Per-object machinery (reframe/compose, social export, writing tools, provenance details, …) is **not** shown always-on. Each object surfaces at most its **two or three primary affordances**; the rest live behind a single, obvious "more" (a "…" / disclosure) and appear on intent. Lanes and inspectors **accrue when the work calls them** (chapter 17 decision 8; chapter 12's progressive-disclosure ethic), never as a permanent wall.

4. **One act in focus at a time.** The surface presents the **current** act at full size; other surfaces recede, collapse, or wait. "Everything visible at once" is not a feature — it is the absence of a decision about what the writer is doing now.

5. **A relationship is drawn, not implied.** When the writer is reasoning about a relationship — a beat's placement against its source (the provenance noodle), a beat against its grounding — that relationship is a **visible mark that connects the two things** (a line, a thread), legible at reading size. A glyph that merely *asserts* "moved" is not the relationship; the relationship is the line you can see.

6. **Verify by looking.** Every visual change is verified by **rendering the real view and looking at the image**, in **light and dark**, at **reading size** — the same view a writer sees. The accessibility tree (`axprobe`, FCIS-AX) proves a handle exists and is machine-operable; it is necessary and **never sufficient** for a claim about legibility or presentation. "The probe found it" is not "the writer can see it."

7. **Space is the presentation.** Generous whitespace, real type scale, and breathing room are how the act is presented. When a surface feels crowded, the fix is **fewer things larger**, not **more things smaller**.

## Honesty (non-goals)

- **This is not decoration.** Legibility and focus are function: a surface the writer cannot read is not working, however complete its data model. Prettiness for its own sake is not the goal; being able to *do the act* is.
- **Progressive disclosure is not hidden capability.** Nothing is removed; the machinery is one gesture away, named and reachable (including in the accessibility tree). Rule 3 declutters the *default*, it does not amputate.
- **Familiarity is not the goal.** DAW/IDE density is the habit being broken, not the target. Resembling a console is precisely the failure.
- **The glasses test is a floor, not a ceiling.** Meeting the minimums is the baseline; the act should read comfortably well above them.

## Relationship to other chapters

- **[The Score](17-the-score.md)** — decision 8 ("opens simple… never an eight-lane console") is the specific case; this chapter generalizes it into an enforceable visual floor for every surface, and the Score is the first surface it is applied to.
- **[Animating truth](12-animating-truth.md)** — progressive disclosure and "show what is true now" are the same ethic in time; this chapter is that ethic in space.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — the beat's anatomy (HEADER · TITLE · BODY · MEASURE) is honored at a size a writer can read; this chapter sets that size.
- **FCIS-AX (accessibility standard)** — the machine-readable half of accessibility. This chapter is the **human-readable** half: both are required, and passing one never substitutes for the other.
- **[Apple's Human Interface Guidelines](19-apple-human-interface-guidelines.md)** — the platform baseline beneath this chapter. It supplies the numbers this chapter's floor was guessing (the system text styles — macOS Body is 13 pt; contrast 4.5:1 / 3:1; 44 pt hit targets) and adds Increase-Contrast to "verify by looking". This chapter's rules are Reframe's extension of the HIG for the act of composing; where they meet, the HIG's numbers govern.

## Acceptance

The doctrine is met when:

1. **A screenshot of the surface at reading size, viewed by someone who wears glasses, reads at a glance** — the act being performed is immediately the most prominent thing.
2. **No surface shows a row of sub-12px, label-less controls;** every object's default shows two or three primary affordances, the rest behind a disclosure.
3. **Text and controls meet the glasses-test floor** (rule 2), in light and dark.
4. **Exactly one act is at full focus;** secondary lanes/panes are recessed, collapsed, or absent until called.
5. **Every relationship the writer reasons about is a visible mark connecting its two ends,** not a glyph asserting it.
6. **Every visual change in the change set was verified by looking at the rendered view** (light and dark), and the reviewer can point to that image — not only to an accessibility-tree query.
