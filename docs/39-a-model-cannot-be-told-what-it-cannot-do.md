# A Model Cannot Be Told What It Cannot Do

> Chapter summary: Asked to perform work Reframe has no capability for, the copilot invented a procedure for
> doing it. Told in its instructions to refuse instead, it invented a precondition — "grant your cloud account
> permission and the app will train the adapter" — a promise of completion attached to the writer's money.
> Given an explicit "beyond this app" class to choose, it chose it once in three identical requests. This is not
> a local defect and not a prompt that needs another sentence: **out-of-scope detection is a named, benchmarked,
> unsolved problem**, and the published numbers match what this app measured. This chapter records what is
> established, what was measured here, and the one line that does not move: a claim about what Reframe can do is
> a FACT THE APP OWNS, and never something a model composes.

## Purpose — the failure this exists to end

**An app that cannot do something, saying how to do it.**

Measured on live drives, 2026-08-01 and 2026-08-02, on the second display against a fresh store. Asked *"train a
LoRA adapter on this manuscript and lint the fountain file"* — neither of which Reframe has any adapter for — the
copilot answered:

> *"1. Load the manuscript into the semantic memory model. 2. Train the LoRA adapter on the loaded manuscript.
> 3. Use the semantic memory to lint the fountain file for any syntax errors or inconsistencies."*

Confident, fluent, plausible, and describing an app that does not exist. No capability was requested and no
lifecycle record was written: the turn never reached the capability boundary at all.

Three repairs were attempted, in the order a reasonable person would try them, and the order matters because each
failed differently:

1. **Remove the unavailable capabilities from the teaching surface** ([ch.37](37-copilot-capability-governance.md)
   already requires this). Necessary, and it changed nothing here — with the rows absent, a request outside the
   list simply had no defined answer, so the model supplied one.
2. **Instruct the model to refuse.** One sentence, in the classifier's own instructions. The answer became
   *"…require the use of cloud resources. To proceed, you would need to grant your cloud account permission…
   Once granted, the app will train the LoRA adapter."* This is WORSE than the fabrication it replaced: it is a
   false promise of completion, and it asks for the writer's money for work that will never happen
   ([ch.20](20-on-device-first-and-the-writers-key.md)). Reverted.
3. **Give the model an explicit out-of-scope class to choose.** It chose it on one of three identical requests.
   The other two produced honest uncertainty — "I couldn't confidently read that", and a two-way clarification —
   which is better than inventing, and is not a refusal.

## What is already known — this is a named problem with numbers

The mistake worth not repeating is treating this as a Reframe bug. It is
**out-of-scope (OOS) intent detection** in task-oriented dialogue, with a standard benchmark (CLINC150) built
because a system *"cannot assume that every query at inference time belongs to a supported intent class"*.

| finding | measured |
| --- | --- |
| Prompted models do not reliably notice they are out of scope: *"all models including LLMs struggle with OOS detection with poor OOS recall across datasets"* | OOS recall **0.0 – 0.615** |
| An explicit reject/OOS class performs **worse** than the alternatives; threshold- and confidence-based rejection is the established approach | EMNLP 2020 |
| Best reported shape: predict from IN-SCOPE labels only, then decide out-of-scope from a **second signal** | OOS recall 0.465 → 0.715; 0.205 → **0.950** |
| Detection *"significantly depends upon the scope of intent labels and the size of the label space"* — system design over prompting | — |

Sources: `arXiv:2410.01627`, `aclanthology.org/2020.emnlp-main.324`, `clinc_oos`.

Attempts 2 and 3 above are the first two rows of that table, reproduced in this app before the table was read.
**Reading first would have cost an hour and saved a day.**

## The principle — a fact about the app is not a thing to reason about

A model is a good judge of MEANING and a poor witness to FACT about the system it is running inside. It has no
access to the capability registry's contents as knowledge; it has only what the prompt says and what similar apps
in its training data could do. Asked what Reframe can do, it answers about apps in general.

So the line is drawn by KIND, not by confidence:

- **What the writer means** — is this a question or a direction, about the work or about the app — is a judgement,
  and the model makes it. Uncertainty here is legitimate and is already mapped
  ([ch.24](24-the-reasoning-is-an-uncertainty-map.md)).
- **What Reframe can do** is a fact, written in the registry ([ch.37](37-copilot-capability-governance.md)), and
  the app states it. Not because the model's prose is untrusted in general — it writes the answers everywhere
  else — but because this particular sentence has a source of truth, and prose is not it.

This is the same move [ch.28](28-a-beat-is-the-question-it-raises.md) makes when it refuses a model's beat title,
and the same one the "MADE BY" stamp makes when it records the resolved route rather than the configured provider.
Where a fact exists, the app speaks it.

## Detection is not the lever, and pretending otherwise is the trap

Measured after the redesign: three distinct out-of-scope requests, and the derived out-of-scope branch fired
**zero** times. The reading did not fail. It settled *confidently* on the nearest in-scope intent
(`semanticMemory`) with `wantsExecutionNow = false`.

That is the hard case in the literature and the reason a confidence threshold cannot close this: the model is not
uncertain, it is **confidently wrong**. A system whose safety depends on the model noticing its own ignorance has
no safety property at all.

What follows is uncomfortable and load-bearing: **Reframe does not currently detect out-of-scope requests
reliably, and this chapter does not claim it does.** What it claims is narrower and provable — that when such a
request IS recognised, nothing the app says about itself can be invented.

## What may be relied upon

- The refusal, when reached, is composed by the app from the registry. Two entirely different requests produce the
  same sentence except where the writer's own words appear, so no generated text can enter it.
- The offer inside the refusal names only capabilities that exist, because it is built from the same registry that
  gates execution.
- A request that is not recognised as out of scope still cannot silently ACT: it reaches no capability, writes no
  lifecycle record, and mutates nothing ([ch.37](37-copilot-capability-governance.md)). The residual harm is a
  wrong SENTENCE, not a wrong action.

## What is still open, and the shape of the work

Neither remaining step is more prompt text.

1. **Verify the prediction.** After an in-scope intent is predicted, check the request against known examples of
   that intent and reject a mismatch — the method with the largest reported gain (0.205 → 0.950). It needs
   exemplars or representations this app does not keep yet.
2. **Narrow the catch-all.** `semanticMemory` and `discussManuscript` are broad enough to absorb anything, and in
   measurement they absorbed everything. The published finding that detection depends on the scope of the labels
   and the size of the label space is a system-design instruction, and it is the cheaper of the two.

## Rules

1. **A claim about what this app can do is composed by the app**, from the registry — never by a model.
2. **An unavailable capability is never taught** ([ch.37](37-copilot-capability-governance.md)); and absence from
   the teaching surface is NOT a refusal mechanism, because it leaves the request with no defined answer.
3. **No instruction to a model is accepted as a safety property.** An instruction may improve behaviour; it may
   not be relied upon, and it must be measured before it is believed.
4. **Do not add an explicit out-of-scope class and call the problem solved.** It is the weaker published option
   and it measured 1-in-3 here.
5. **Out-of-scope is derived from a second signal**, over a prediction made from in-scope labels only — never
   asked for directly.
6. **A refusal names what was asked and offers only what exists.** No steps, no preconditions, no "once you have
   done X" — a promise of completion is worse than the fabrication it replaces, and worst when it asks for money.
7. **Failing to recognise a request may never cause an action.** The floor is a wrong sentence; a wrong ACT is a
   different failure and is governed elsewhere.
8. **Measure recall over repeated identical requests**, not once. A mechanism that fires sometimes reads as
   working, and the difference is only visible in repetition.
9. **Consult the published work before inventing a mechanism.** Two of the three attempts here are the first two
   rows of a table that already existed.

## Acceptance

The doctrine is met when:

1. No sentence describing Reframe's capabilities can contain generated text — provable by construction, not by
   inspection.
2. A refusal offers only capabilities with a runtime adapter, and this is enforced by test.
3. An unrecognised out-of-scope request produces no capability request, no lifecycle record and no mutation.
4. Out-of-scope recall is stated as a MEASURED number over repeated trials, not asserted, and is recorded where
   the next person will find it.
5. Neither of the two open steps is replaced by additional instructions to the model.

## Governing sentence

Reframe shall let a model judge what the writer means and never let it testify to what Reframe can do — and where
the app cannot yet tell that a request is beyond it, it shall say so plainly rather than let a confident sentence
stand in for a capability it does not have.
