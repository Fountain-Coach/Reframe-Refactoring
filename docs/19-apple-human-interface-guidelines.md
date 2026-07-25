# Apple's Human Interface Guidelines — the Baseline We Build On

> Chapter summary: Reframe is a native macOS application, and Apple's **Human Interface Guidelines (HIG)** are its baseline visual and interaction standard — not an alternative to our doctrine but the floor beneath it. This chapter adopts the HIG specifics our own chapters implied but never numbered (system text styles, contrast ratios, hit targets, the 8-point grid, semantic system colours, materials, purposeful motion that honours Reduce Motion, SF Symbols, VoiceOver), maps them onto chapters 12/14/17/18, states where Reframe deliberately goes *further* than the HIG, and records the gaps between the current app and the HIG that this adoption obliges us to close. It states enforceable rules; it does not restate the whole HIG.

## Purpose

Chapters 12–18 arrived at good visual doctrine by hitting walls in the code — "the act is the star", "the glasses test", "verify by looking". Much of what they found is exactly what Apple already publishes in the HIG, arrived at from the other direction. Rather than keep re-deriving it, Reframe **adopts the HIG as its baseline** and reconciles our earned doctrine with it: where they agree, the HIG supplies the numbers we were guessing; where we go further, we say so; and where the current app falls short of the HIG, we name the gap.

Adopting the HIG is also the honest completion of the accessibility work. FCIS-AX gave us the machine-readable half; chapter 18 gave us the human-legible half; the HIG is where Apple states both together, for the platform Reframe actually ships on.

## The principle — the HIG is the floor; our chapters are the extension

A native app that ignores the HIG fights the platform: it loses free Dark Mode, Dynamic Type, Increase Contrast, VoiceOver, Reduce Motion, and the muscle memory of every Mac user. So the HIG is the **baseline** — Reframe conforms by default and departs only deliberately, for a stated reason. Chapters 12 (animating truth), 14 (the beat's anatomy), 17 (the Score), and 18 (the stage presents the act) are Reframe's **extensions** of the HIG for the specific act of reading a manuscript into a story and composing from it — never contradictions of it.

## The decision (adopted HIG specifics, enforceable)

1. **Type comes from the system text styles, not hand-picked point sizes.** Use the built-in styles (Body, Title/Headline, Footnote, Caption) rendered in the system font (SF Pro; SF Pro Text ≤ 19 pt, Display ≥ 20 pt, dynamic optical sizing on macOS 11+). On macOS the **Body style is 13 pt Regular** — which is exactly chapter 18's body floor, arrived at independently. Chapter 18's floor is therefore restated as: **body = Body (13 pt), a beat/section title ≥ Headline/emphasized (~15 pt), a label ≥ Footnote/Caption (≥ 11–12 pt)** — and prefer the named style over a literal size so Dynamic Type and optical sizing come for free.

2. **Contrast meets the HIG ratios, verified in every appearance.** Text ≥ **4.5:1** against its background (the WCAG AA / App Store "Sufficient Contrast" floor), non-text controls and meaningful graphics ≥ **3:1**, and **aim for 7:1** on primary reading text. Verify in **light, dark, AND Increase Contrast** — chapter 18's "verify by looking" now explicitly includes the Increase-Contrast setting, not only the two themes.

3. **Hit targets honour 44 pt where touch or accessibility reach; macOS pointer may be finer, never cramped.** The HIG floor is **44 × 44 pt** for touch and for Full-Keyboard-Access / Switch-Control reach. macOS is pointer-first, so secondary controls may be smaller — but chapter 18's rule stands and is reconciled: **secondary controls ≥ 28 pt, a primary action ≥ 44 pt**, and nothing a writer must hit is a sub-12 px glyph.

4. **Colour is semantic and system-supplied; a colour meaning is never hard-coded.** Use the semantic system colours (`.primary`, `.secondary`, `.accentColor`, label/fill/background roles) so light/dark and Increase-Contrast adapt for free. Never hard-code a colour that carries meaning — the "Thinking… in red" defect (a working state painted as an error) is exactly this rule broken. And per the HIG, **never rely on colour alone** to convey state — pair it with text, shape, or a symbol (chapter 18 rule 5 is the same idea for relationships).

5. **Layout is an 8-point grid that defers to content.** Space in multiples of 8; give content generous margins and whitespace; establish hierarchy by size and weight; group related elements. "Defer to content" is the HIG's own phrasing of chapter 18's "the act is the star."

6. **Depth and grouping use system materials, not hand-rolled panels.** Prefer the platform's materials/vibrancy for sidebars, popovers, and layered surfaces so the app reads as native and adapts to appearance and Increase-Contrast automatically.

7. **Motion is purposeful AND honours Reduce Motion.** Chapter 12's animated truth — breathing ghosts, the read-head, the settle of a beat — is HIG-aligned *purposeful* motion, but the HIG also requires respecting the **Reduce Motion** accessibility setting. Every chapter-12 animation must have a reduced, non-animated (or cross-fade) form when Reduce Motion is on; the *information* the motion carried (progress, arrival) must survive without the movement.

8. **Icons are SF Symbols, scaling with the text.** Use SF Symbols for iconography; size and weight them to match the adjacent text style so they scale with Dynamic Type. A custom-drawn glyph (e.g. the noodle thread) is legitimate only where no symbol expresses the meaning.

9. **Accessibility is both halves, per the HIG.** VoiceOver labels and accessibility identifiers on every control (FCIS-AX); Dynamic Type honoured; contrast met; colour never the sole signal; Reduce Motion respected. The HIG is where Apple states the machine-readable and human-legible halves as one requirement.

## Reconciliation — our chapters against the HIG

| HIG topic | Reframe chapter | Relationship |
| --- | --- | --- |
| Defer to content | 18 (the act is the star) | Agreement — same idea, ours names the *act* specifically |
| Typography / text styles | 18 (glasses test) | HIG supplies the numbers; our floor == macOS Body 13 pt |
| Contrast ratios | 18 | HIG adds the ratios (4.5 / 3 / 7); we adopt + add Increase Contrast to "verify by looking" |
| Reduce clutter / prioritise | 18 (progressive disclosure), 16 (one surface) | Agreement |
| Colour (semantic, not colour-alone) | 18 rule 5, and the "Thinking-red" fix | HIG reinforces; we adopt semantic-only |
| Motion (purposeful, Reduce Motion) | 12 (animating truth) | Agreement on purposeful; HIG adds Reduce Motion — shared `StudioMotion` helper + Cut lane done, other ch.12 animations pending |
| Accessibility (VoiceOver) | FCIS-AX standard | Two halves of one requirement |
| Progress indicators | 12 (never sign a wait with a spinner) | **Deliberate departure** — Reframe is *stricter*: the wait is the show, not a spinner |

## Honesty (non-goals)

- **The HIG is a baseline, not a straitjacket.** Where Reframe deliberately exceeds it — the no-spinner rule (ch.12), "the act is the star" as a hard rule (ch.18), relationships drawn as lines (the noodle) — that is stricter conformance to the *spirit* (clarity, deference to content), stated as a departure, not an accident.
- **Adopting the HIG is not a reskin.** It is meeting the platform's floor for legibility, contrast, motion, and accessibility — function, not veneer.
- **Numbers are a floor, not a target.** 4.5:1 and 13 pt are minimums; primary reading text should sit comfortably above them.

## Relationship to other chapters

- **[The stage presents the act](18-the-stage-presents-the-act.md)** — the human-legibility floor; this chapter supplies its numbers from the HIG and adds contrast + Increase-Contrast.
- **[Animating truth](12-animating-truth.md)** — purposeful motion; this chapter binds it to Reduce Motion.
- **[The beat and its arrangements](14-the-beat-and-its-arrangements.md)** — the one beat spec now reads from system text styles at the HIG floor.
- **FCIS-AX standard** — the machine-readable half of the HIG's accessibility requirement; this chapter is where it meets the human half.

## Acceptance

The doctrine is met when:

1. **Text uses the system text styles** (or matches their sizes) and meets the chapter-18 floor, in the system font.
2. **Contrast meets 4.5:1 (text) / 3:1 (controls)**, verified in light, dark, and Increase Contrast; primary reading text aims for 7:1.
3. **Hit targets meet 44 pt where touch/accessibility reach**, and no writer-facing control is a sub-12 px glyph.
4. **Colours are semantic and adapt to appearance automatically;** no colour carries meaning alone, and none is hard-coded.
5. **Motion honours Reduce Motion** — every animation has a reduced form that preserves the information it carried.
6. **Every control has a VoiceOver label and an accessibility identifier** (FCIS-AX), and Dynamic Type is honoured.

## Known gaps this adoption obliges us to close

Stated honestly. The first round of compliance (the shared mechanisms + the Cut surface, the surface this chapter governs most directly) is done; the app-wide sweep remains.

**Closed:**

- **Reduce Motion has a shared, non-View-context-capable helper** (`StudioMotion` reads the process-wide setting via `NSWorkspace`, so a `DropDelegate` or plain method can honour it, not only a `View`). The Cut lane's reorder animations (drag and button) now drop the tween under Reduce Motion while keeping the state change. A named text-style vocabulary (`StudioTheme.beatTitle`/`readingBody`/`controlLabel`/`primaryAction`/`eyebrow`, backed by macOS system text styles) and a named **provenance** colour (the noodle's "moved" meaning, no longer hard-coded orange inline) exist and the Cut surface consumes them.
- **A contrast audit exists and is enforced** — `StudioThemeContrastAuditTests` computes the real WCAG ratio for the text/ground pairs Reframe owns, in light *and* dark, and fails the build below the 4.5:1 text (3:1 large/control) floor. It caught genuine defects (the status text-on-fill tokens — warning/success/accent/info — sat at ~3:1, worse in dark); their blends were deepened until every owned pair clears 4.5:1. Secondary/tertiary label tiers are measured and held to the 3:1 support floor (they are for supporting captions, never primary reading — Apple's own usage).
- **Materials** are used on the Cut lane's recessed background (`.regularMaterial`), so it reads as depth beneath the reading rather than a flat wash.

**Still open (app-wide, not the governed surface):**

- **Migrate the remaining hard-coded sizes and colours** on the other surfaces (~460 literal `.system(size:)` sites, a handful of raw colour literals) to the named text styles and semantic/`StudioTheme` colours. The vocabulary now exists; the sweep does not.
- **Honour Reduce Motion in the other chapter-12 animations** (breathing ghosts, settles, the read-head) using the `StudioMotion` helper — several views already read `accessibilityReduceMotion` piecemeal; converge them on the helper and cover the rest.
- **Extend the contrast audit** to Increase-Contrast resolution and to more composited pairs as surfaces migrate. Opt-in pixel goldens (`UI_SNAPSHOT=1`) that render status pills will need a one-time `UPDATE_GOLDEN=1` refresh to adopt the deepened status colours.

These remaining items are the backlog; they are not claimed as done.

## Sources

Apple Human Interface Guidelines and related developer documentation:

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines)
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Typography](https://developer.apple.com/design/human-interface-guidelines/typography)
- [Color](https://developer.apple.com/design/human-interface-guidelines/color)
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout)
- [Sufficient Contrast evaluation criteria — App Store Connect](https://developer.apple.com/help/app-store-connect/manage-app-accessibility/sufficient-contrast-evaluation-criteria/)
- [UI Design Dos and Don'ts](https://developer.apple.com/design/tips/)
