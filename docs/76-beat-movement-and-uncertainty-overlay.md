# Beat Movement and the Uncertainty Overlay

> Chapter summary: Questions and movements are separate semantic records. A question is a source-grounded uncertainty
> with a span and lifecycle. A movement is a source-grounded change, whether settled or unresolved. The projection
> keeps both lanes, plus read coverage; neither is renamed or counted as the other.

## Purpose

Chapter 28 defines the open-question span that this projection previously called a beat. Pyramus and Thisbe exposed
the need to keep that semantic object separate from a grounded dramatic movement: a meeting, reversal, revelation,
decision, or consequence can be settled while still being an important movement. It must remain visible without being
promoted to a question.

## Governing rules

1. **Questions and movements are distinct.** A question is the span over which the reading holds one story question
   open. A movement is an action, encounter, escalation, reversal, revelation, decision, consequence, or other
   source-grounded change. A movement is not automatically a question.

2. **Questions are not a movement gate.** A missing question never authorizes deleting a grounded movement; a
   movement never authorizes inventing a question without source evidence.

3. **Question lifecycle remains explicit.** A question records `questionMovement`: raised, carried, transformed,
   answered-by-the-text, deferred, or still-open-at-end. A movement records its own source evidence. “Resolved” is a
   question state, never a synonym for movement.

4. **Every semantic field keeps its evidence.** Each movement and each question movement carry source anchors,
   provenance, the reading/lens identity, and the operation version. Absence of an anchor is preserved as unknown; no
   span is borrowed merely to make an illustration or score mark look complete.

5. **The projection has separate lanes.** `Questions` shows question spans and lifecycle; `Movements` shows grounded
   changes, including settled changes with no question; `Read coverage` shows what was read. Participants, including
   illustrations, attach to a grounded movement and may reference a related question.

6. **UncertaintyScoreKit projects, it does not redefine.** Its lanes may be empty independently: no questions does not
   mean no movements, and movements do not count as questions.

7. **Storify must emit both contracts.** The semantic reading may return structural ordering/movement and optional
   uncertainties. Persistence, reconstruction, carry-forward, and projections must preserve both, including legacy
   and anchored question representations.

8. **Illustration eligibility is semantic, not numeric.** A movement is illustratable when it has grounded source
   evidence. A related question enriches the prompt when present; image generation must not require a question unless
   a scenario explicitly targets questions.

9. **Scenario acceptance names the intended shape.** A structural illustration scenario requires a persisted movement
   with source evidence. A question-led scenario additionally requires a question overlay and its lifecycle
   state. Neither scenario may pass from an image receipt alone.

## Naming

Use **Questions** for source-grounded question spans. Use **Movements** for source-grounded changes. Use **question
movement** for the question lifecycle (`raised`, `carried`, `transformed`, `answered-by-the-text`, `deferred`, or
`still-open-at-end`). Do not use “beat” as a label for either lane; retain old identifiers only as compatibility
aliases during migration.

## Acceptance

- A resolved myth still produces grounded movements, even when `Questions` is empty.
- A question appears only when its source-grounded question evidence exists.
- Store readback contains both movement and question evidence; reconstruction preserves structured and
  legacy questions.
- UncertaintyScoreKit, Score, and image projection agree on movement identity and source provenance.
- The Teatro myth scenario cannot reach image generation without a grounded movement; it requires a question only when
  the scenario declares uncertainty as its target.

## Governing sentence

Reframe shall project Questions and Movements as separate, source-grounded lanes, with Read coverage as a third
authority. They may be related, but they are never substituted for one another.
