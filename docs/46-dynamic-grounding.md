# Dynamic Grounding: From Default Reading to Writer-Accepted Lens

> Chapter summary: Grounding is not a workspace or a configuration panel. It is the living reading flow by which Reframe starts from a default non-integrational stance, observes what the first Storify reading leaves unresolved, and offers a writer-controlled change in lens.

## The decision

Grounding is a process, not a place.

Reframe begins a manuscript with a default non-integrational stance: the source remains authoritative, and the system does not silently reconcile, explain away, or merge tensions that the source has not resolved. The first Storify Source Auto pass is the first structural observation of that manuscript. It produces beats, questions, and an UncertaintyScore from the source and the confirmed Grounding policy.

After that reading, the UncertaintyScore may reveal a more useful way to attend to the manuscript. Reframe may propose a new grounding lens derived from the observed pattern. The proposal is a reading offer, not a hidden preference, a new baseline, or a manuscript edit.

The writer remains the authority for accepting the change. `/ground` is the explicit acceptance operation. When accepted, the new lens receives a new Grounding identity, invalidates the policy-dependent Storify results, and starts a new reading lineage. The source text and author baseline remain unchanged.

## Rules

1. **Grounding is a flow.** Do not present it as a standing workspace, editor, settings panel, or separate place the writer must visit. The user-facing vocabulary is Grounding, grounding lens, grounding proposal, and grounding change.
2. **The default stance is non-integrational.** Source contradictions, absences, and unresolved tensions remain visible. Grounding may change salience; it may not manufacture a resolution.
3. **Storify Source Auto is the first observation.** Dynamic grounding begins from the first source reading and its persisted UncertaintyScore. It must not depend on a retired index, semantic-memory shortcut, or an unobserved chat impression.
4. **The score may produce a proposal, not an automatic mutation.** A score-derived lens is an offer until the writer explicitly accepts it. Proposal text must identify the observed uncertainty and state that the author baseline is unchanged.
5. **`/ground` is the acceptance boundary.** The operation must be bound to the active reading run, the proposed lens, and the confirmed Grounding identity from which the proposal was derived. A stale, missing, or mismatched proposal fails visibly.
6. **A grounding change creates a new lineage.** The new identity must be persisted before downstream work is presented as current. Policy-dependent beats, kept/noise decisions, summaries, synopsis, and arcs become stale or are restarted according to the runtime contract.
7. **Grounding never edits the manuscript.** It changes the policy of attention, not the canonical source, author baseline, or writer-authored draft. Source evidence remains the authority for facts.
8. **The transition is inspectable.** Copilot text, AX state, the UncertaintyScore/lane projection, and FountainStore lifecycle/effect documents must agree about the proposal, acceptance, previous identity, new identity, and restart/invalidation effect.
9. **Grounding remains local by default.** A grounding proposal and acceptance run on the on-device lane unless the writer explicitly widens the lane under the provider governance chapters.
10. **The old static metaphor is retired.** No help item, alias, command catalogue entry, generated manifest, or AX label may describe Grounding as a legacy product workspace. Internal migration identifiers may remain only where they cannot reach writer-facing output.

## The live sequence

```text
canonical source
  → default non-integrational reading
  → first Storify Source Auto
  → persisted UncertaintyScore and dynamic lanes
  → proposed grounding lens
  → writer accepts / rejects
  → new Grounding identity if accepted
  → Storify re-forms its policy-dependent reading
```

The sequence is consequential. A successful command is not proved by the words “grounded” or “reading again.” Acceptance requires the AX-visible result, the changed reading projection, and persisted FountainStore evidence.

## Amendment (2026-08-05) — a lens is a hypothesis about the reader, not a description of the work

The chapter said the score "may reveal a more useful way to attend to the manuscript" and left *how* to the
implementation. What the implementation built instead was a summary: the first four open questions concatenated,
offered back as the lens. Driven live it produced, for a manuscript of associative material, this —

> holding the tension of unresolved uncertainty open against the potential for resolution through the
> protagonist's actions and the story's outcome

— which is not a way of reading anyone can adopt. It is a restatement of the fact that there is uncertainty. No
test caught it, because a test can check that a lens is *derived* and cannot check that it is *usable*.

### The uncertainty has two origins, and the map cannot tell them apart

A first reading is naive by design ([rule 2](#rules), the non-integrational stance): it does not resolve what the
source has not resolved, and what it cannot close becomes the UncertaintyScore. But that residue has two entirely
different origins, and they are drawn identically:

- **the work's** — the piece genuinely holds it open. That is the art, and no reading closes it;
- **the reading's** — the reader attended to the wrong thing, and the questions are artifacts of that stance.

Separating them is the whole value of the flow. ch.24 already distinguishes `ambiguity` from `thin` from
`failure`, but no state distinguishes *whose* uncertainty a note is, because nothing in a single reading can.

### What a lens is

**A lens is a hypothesis about the reader's blind spot.** It answers one question: *what would I have to be
attending to for this not-knowing to stop being not-knowing?* It is not a description of the work, not a summary
of the open questions, and not a mood.

The standing case is the Polyx Supershow. Its first reading produced fourteen questions of the form *"Will Dad's
desire for adventure lead to a dangerous situation?"* — causal-narrative questions. The writer's own account of
the work is that it is associative material, deliberately not coherent in the ordinary sense, "a Schnippel, the
work of a collecting mind that finds its curiosity in changing things — and every piece is here because of how it
looks."

Those fourteen questions are not the work's uncertainty. They are the residue of reading associative material as
though it were plot; a reader looking for causality in a Schnippel will generate that pattern indefinitely. The
writer's lens does not *resolve* those tensions. It dissolves the question of them, because they were never the
work's questions.

So the pattern of open questions is **evidence of a stance**, not a set of findings. Fourteen causal questions
over associative material is a diagnosis of the reader.

### Rules (extending the rules above)

11. **A lens names a way of attending, and must be adoptable.** It has to complete "read it for …" as something a
    reader could actually do. A phrase that only restates that uncertainty exists, or that names a mood, a theme,
    or a tension, is not a lens and may not be offered as one.
12. **The proposal states the reader's suspected blind spot, and cites the pattern as its evidence.** It says what
    the reading was attending to, what that left it holding, and what it suspects it should have been attending to
    instead — not what the open questions were.
13. **The writer's own lens is authoritative and is recorded verbatim.** A writer correcting the reading's stance
    is the highest-value turn in this flow, because they know their work's mode and no reading can derive it. Their
    words are the lens; they are never paraphrased into system language, and never merged with the proposed one.
14. **A lens is proved by a change in the KIND of uncertainty, not its amount.** After an accepted re-read, the
    honest question is whether the reader's artifacts fell away and the work's own ambiguity remained — which is a
    comparison between two readings of the same lines (the `/readings` command already exists for exactly this),
    not a count. A lens that
    only reduces the number of open questions has not been shown to be right.
15. **A hole is not a lens problem.** A stretch with no reading behind it is a `failure` gap whose want is the
    manuscript's ([ch.33](33-a-want-is-a-gap-in-a-ledger.md) rule 5). Re-reading it through a different stance
    reads the same hole through a new frame and calls the result grounded. When the score carries holes, Grounding
    says so and proposes nothing.

### Why this also governs the conversation

A lens that is a real proposition is one a writer can refuse. Measured: while the proposal was abstract, a
refusal carrying the writer's own lens did not reach the Grounding decision at all — there was nothing concrete
for the mediated turn to relate it to. Vagueness in the offer and misrouting of the answer are the same defect,
which is why rule 11 is a conversational requirement and not a matter of taste.

## The governing sentence

Grounding is Reframe’s living, source-authoritative flow of attention: the UncertaintyScore may propose how the reading should change, but only the writer may accept that change, and every accepted lens must leave a persisted, inspectable lineage.

## Acceptance

A revised grounding flow is accepted only when a fresh owned-source drive proves all of the following:

- the first Storify reading exposes the UncertaintyScore and its lanes;
- the default non-integrational stance remains visible in the absence of a proposal;
- the proposal is derived from the observed score and does not mutate the baseline;
- `/ground` is blocked without the proposal-bound acceptance state;
- accepted `/ground` persists a new identity and requests the downstream restart;
- the before/after score or lane projection is captured by window ID and readable in the AX tree;
- FountainStore lifecycle and effect documents show the accepted terminal result;
- no retired static Grounding label appears in the transcript, help, AX tree, or generated capability projection.

### Amendment (2026-08-05b) — the lens is answerable, and Reframe answers it

Rule 14 makes a lens provable by comparing two readings of the same lines. As written, the writer performs that
comparison: `/readings` diffs the pair and reflects on the difference, but nothing carries the result back to the
proposal that caused the re-read. A hypothesis nobody returns to is not a hypothesis; it is a claim.

16. **Reframe closes the loop it opened.** When an accepted lens has produced its re-read, Reframe returns to the
    proposal on its own — without being asked — and states what changed: which of the earlier reading's open
    questions did not recur, which persisted, and what that suggests about the blind spot the proposal named. The
    comparison is drawn from the two persisted readings of the same lines, never from the transcript.

17. **It must be able to say the hypothesis did not hold.** *"The questions I expected to dissolve are still
    here"* is a successful outcome of rule 16 and the honest one. A report that confirms the lens whatever the
    readings show is the laundering [ch.24](24-the-reasoning-is-an-uncertainty-map.md) rule 3 forbids, and a lens
    whose count merely fell has not been shown to be right (rule 14).

18. **It reports; it does not revert.** A lens whose hypothesis failed stays confirmed until the writer decides
    otherwise ([ch.47](47-situated-mixed-initiative-interaction.md) rule 9 — the human remains the mutation
    authority). Reframe may offer to read differently again; it may not undo the writer's accepted lens because
    its own hypothesis disappointed it.

19. **A missing comparison is stated, not inferred.** When no second reading covers the same span, the report says
    so. It may not reason about what would have changed ([ch.30](30-the-living-gazetteer.md) rule 10 —
    incompleteness is stated, never filled).

### Amendment (2026-08-05c) — the report says what it cannot tell, and ends in the writer's hands

Rule 14 made a lens provable by comparing two readings of the same lines, and rules 16–19 made Reframe deliver
that comparison unasked. The comparison was then calibrated, which is what rule 14 implies and what
`ReframeReadingDiff`'s own header warns of — *"the same lens twice mostly measures the model's noise"*:

| | held by both | dissolved | newly opened |
| --- | --- | --- | --- |
| **same lens, read twice** | 5 | 19 | 23 |
| lens changed to the writer's | 1 | 23 | 27 |

The same magnitude. And the control dissolved the very questions the changed-lens report had offered as its
evidence. The reading also held 28 questions open on one pass and 24 on the next, through an identical lens.

A single pair of readings therefore cannot separate what the lens did from what the reader does differently on a
second pass. Both surfaces were nonetheless asserting that it could: `/readings` prints its shared questions under
the heading *"the work's own ambiguity — these survived a change of reading"*, and printed exactly that for two
readings through an identical lens, where no reading had changed at all.

20. **A reading comparison states what it cannot tell, and attributes nothing it cannot establish.** It may say
    what differs between two readings. It may not say whose the uncertainty is — the work's or the reader's — on
    the strength of one pair, and it may not call a difference a survival of "a change of reading" when the lens
    did not change. The readings carry their own lens identity; the report reads it and says which case it is.

21. **"I cannot tell" is the third honest outcome.** Rule 17 required the report to be able to say the lens did
    not hold. It must equally be able to say that the evidence does not separate the lens from the instrument.
    Presenting a noise-level difference as a finding is [ch.24](24-the-reasoning-is-an-uncertainty-map.md) rule 3's
    laundering, one level up.

22. **The report ends in the writer's action, grounded.** Its product is not a verdict but a call: the questions
    that survived, named and addressed to their lines, are the material only the writer can judge. It hands them
    that material and asks, rather than telling them what it means. Every number and every question it shows is
    traceable to the two persisted readings.

23. **Both surfaces obey this.** The unasked report after an accepted lens and the writer-invoked `/readings` are
    two triggers over one comparison. A change to how a comparison is narrated belongs where it is narrated, once,
    so neither surface can drift into claiming more than the other.

### Acceptance for rules 20–23

- **a comparison of two readings through the SAME lens says so**, and describes the difference as the instrument's
  own variance rather than as anything surviving a change of reading;
- **no report attributes uncertainty to the work or to the reader** on the strength of a single pair;
- **a report whose difference is within what the same lens produces says it cannot tell**, in the writer's terms;
- **every report ends with the surviving questions, addressed to their lines**, and a question to the writer
  rather than a conclusion about their manuscript;
- **a drive in which `/readings` and the unasked report describe the same pair differently has failed** rule 23.

### Acceptance for the 2026-08-05 amendment (rules 11–15)

The criterion above — *the proposal is derived from the observed score* — is the one that let an unusable lens
through, because derivation is a fact about provenance and says nothing about whether a reader could adopt the
result. These are read from the offer itself, on a live drive:

- **the offered lens completes "read it for …" as something a reader could do.** A phrase naming only a mood, a
  theme, a tension, or the fact that the work is uncertain fails this, however faithfully it was derived;
- **the proposal names what the reading was attending to and what it suspects it should attend to instead**, and
  cites the shared pattern of the open questions as its evidence rather than listing them;
- **a writer's counter-lens is persisted verbatim** as the lens, neither paraphrased into system language nor
  merged with the proposed one;
- **the offer is refusable** — a refusal carrying the writer's own lens reaches the Grounding decision, leaves
  confirmed Grounding unchanged, and returns an offer of the writer's frame. An offer no writer can disagree with
  has failed rule 11 whatever it says;
- **a score carrying `failure` gaps produces no proposal at all**: each hole is named with its span and its want,
  and no pending proposal is persisted;
- **an accepted re-read is judged by the change in the KIND of uncertainty**, shown by comparing the two readings
  of the same lines. A smaller number of open questions is not acceptance, and neither is a larger one a failure.

### Acceptance for rules 16–19

- **the proposal is answered without the writer asking.** After an accepted lens produces its re-read, Reframe
  returns to it and reports, in the same conversation, what the comparison shows;
- **the report names which earlier open questions did not recur and which persisted**, and each is traceable to
  both persisted readings — not to the transcript;
- **a lens that did not change the kind of uncertainty is reported as not having held**, and the reading is left
  confirmed; a drive in which every accepted lens is reported as a success has failed this;
- **no revert happens on Reframe's judgement.** Grounding identity after the report is the one the writer
  accepted, unless the writer changes it in a new turn;
- **when no comparable pair exists the report says so** rather than describing a change it cannot see.

### Amendment (2026-08-15) — a reading remembers what it found

The comparison rules correctly reject two isolated same-lens passes as proof of a lens effect. That does not mean a
human rereading begins with an empty mind. An iterative reading returns to the source with what the previous reading
left open. The remembered material changes the act of attention without changing the writer's confirmed lens.

24. **A continuation reading carries semantic history.** When Storify rereads the same source under the same
    confirmed Grounding identity, the runtime must provide the prior reading's persisted findings, unresolved
    questions, and source evidence anchors as semantically selected continuation context. It must not reconstruct
    that context from transcript prose or from an in-memory snapshot.

25. **Remembered findings are not a lens change.** Carry-forward context may cause a question to be revisited,
    resolved, replaced, or deepened, but it must preserve the confirmed lens identity. A new lens identity requires
    the explicit writer-controlled Grounding acceptance boundary in rules 4–6.

26. **Lineage names the kind of second reading.** Every persisted continuation run records its parent reading run,
    the confirmed Grounding identity, and the carried semantic artifacts. A comparison must distinguish a
    history-aware continuation from an independent control pass; neither may be presented as the other.

27. **No difference is manufactured.** A continuation may produce the same questions when the source warrants that
    result. The acceptance result is the honest semantic account—confirmed, resolved, newly opened, or still
    indeterminate—not a requirement that wording or uncertainty counts change.

### Acceptance for the 2026-08-15 amendment (rules 24–27)

- **the second run is visibly and durably linked to the first** by a FountainStore parent-reading identity;
- **the second run keeps the same confirmed Grounding identity** unless the writer explicitly accepts `/ground`;
- **the carried context consists of persisted findings, unresolved questions, and evidence anchors**, selected for
  the current reading, and no prompt or transcript is persisted as a substitute;
- **the comparison states whether it is comparing a continuation or an independent control**, and reports semantic
  development without requiring artificial divergence;
- **a fresh owned-source drive can read back the lineage and carried-context proof from FountainStore**, while AX and
  the window-ID capture expose the corresponding reading state.

The Book may describe this as a live-accepted development command only after those authorities agree. It must not imply that the command belongs to a named released App build unless the release manifest says so.
