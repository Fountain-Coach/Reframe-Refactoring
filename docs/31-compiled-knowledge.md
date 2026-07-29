# Compiled Knowledge — the Cloud Teaches, the Device Remembers

> Chapter summary: Reframe's on-device ambition was read for a year as a model problem — *how does a local model
> compete with a frontier one?* It is not a model problem. A frontier model's value to a manuscript is not its
> presence at every turn but the **durable knowledge one expensive act of reasoning can leave behind**. So the
> frontier lane is demoted from runtime to **knowledge compiler**: it is asked hard questions rarely, and what it
> settles is compiled into inspectable, attributed, revisable project memory that the on-device lane executes
> against forever after. The runtime gets better at *this* manuscript without its model changing, because its
> memory improved. [The Living Gazetteer (ch.30)](30-the-living-gazetteer.md) is the first such artefact and the
> proof of the shape; this chapter governs the family. Its first-class rule: **separate learning from remembering.**
> Models learn language; projects remember worlds; the writer owns the world's memory.

## Purpose — the failure this exists to end

**Every act of reasoning was thrown away.** A reading settled that *Kinch*, *Stephen* and *Stephen Dedalus* are one
man, and the next pass over the same chapter began by not knowing it. Not because the knowledge was lost — it was
persisted, and [ch.30](30-the-living-gazetteer.md) had already given it a home — but because nothing downstream
consumed it. Measured, on the sentence the chapter opens with:

```
no world compiled in:      Buck Mulligan → OtherWord     Mulligan → OtherWord
the confirmed world in:    Buck Mulligan → PersonalName  Mulligan → PersonalName
```

The instrument could not see the man the reading had already confirmed twice. Every later passage paid, in tokens
and in error, to re-derive a fact the project already held — and a reading that cannot see who is present is
exactly the state in which it invents a quarrel with someone who is not.

**And the opposite temptation, which would be worse.** The obvious cure for a weak local lane is to send more to
the frontier: ask the big model each time, and the answers improve. That is a runtime that costs the writer money
per turn forever, gets no better at their manuscript on the hundredth read than on the first, and cannot explain a
single thing it concluded. It also violates the plainest constraint this app has: **cloud inference is the
writer's money** ([ch.26](26-internals-tune-themselves.md)), and on-device is the first lane, not the fallback.

Between the two sits the actual architecture. Expensive reasoning is worth paying for **once**, when it settles
something durable, and worthless to pay for repeatedly to rediscover it.

## The principle — separate learning from remembering

**Models learn language. Projects remember worlds. The writer owns the world's memory.**

Three mechanisms are routinely conflated in AI systems and must never be conflated here:

| | what changes | where it lives | who may change it |
|---|---|---|---|
| **Statistical learning** | model weights | the model vendor's artefacts | nobody here |
| **Project memory** | knowledge, with evidence | this manuscript's store | the reading, then the writer |
| **Interpretation** | nothing; it reasons | a turn | the one reasoning ([ch.12](12-animating-truth.md)) |

Reframe trains nothing. It has no LoRA, no fine-tune, no adapter, and this chapter is not a route to one. What it
accumulates is **remembered knowledge, not learned parameters** — explicit, addressable, inspectable, and wrong in
ways a writer can point at and correct in a sentence. That property is the whole reason it is allowed to exist:
weights cannot be argued with, and a world that cannot be argued with has authority over a manuscript, which
[ch.30](30-the-living-gazetteer.md) forbids.

## What a compiled artefact is

A compiled artefact is the **durable residue of an act of reasoning**: what was settled, by whom, from what
evidence, at what moment, and what would overturn it.

It is therefore, precisely:

- **Authored.** Every entry names the act that produced it — a reading, a measurement, or the writer.
- **Evidenced.** Every entry cites the passage that put it there. An entry with no evidence is a fabrication with
  provenance formatting ([ch.28](28-a-beat-is-the-question-it-raises.md)).
- **Falsifiable.** Every entry implies what would refute it. Knowledge that cannot be wrong is decoration.
- **Revisable, and historied.** Supersession, never silent rewriting: what the project believed last week stays
  readable beside what it believes now ([ch.30](30-the-living-gazetteer.md) rule 5).
- **Removable.** Delete every compiled artefact and the manuscript is whole and readable. Recognition degrades;
  nothing becomes inaccessible; no step is gated.

And it is **not a cache.** The proposal that prompted this chapter called it "a cache of understanding", and the
word has to be refused: a cache may be silently discarded and silently rebuilt, and its contents are nobody's
decision. These artefacts are decisions. They are discarded only where a writer or a reading can see it happen.
The app's standing rule that the store is the truth and nothing of consequence lives only in memory applies at
full strength — compiled knowledge is *stored*, not *cached*, and the distinction is authority, not durability.

## Two lanes, and the one that must never be required

**The cloud teaches. The device remembers.** Frontier reasoning is spent on what is genuinely hard and genuinely
durable — an ambiguity the text will not settle, an identity two passages apart, a continuity decision spanning a
chapter. What it settles is compiled. The on-device lane then does the enormous common work — recognition, lookup,
retrieval, continuity, the writer's editing turn — against compiled knowledge, at no cost and no latency.

Three constraints keep this from becoming an argument for spending:

1. **On-device is the first lane, always** ([ch.26](26-internals-tune-themselves.md)). Escalation is a reasoned
   widening over an uncertainty the local lane reported, never a default and never automatic.
2. **The writer's money is spent only with the writer's yes**, at the call site, per act. A design in which the
   architecture *needs* the cloud lane to function is a design that spends without asking, and is rejected here.
3. **The architecture must be complete with the cloud lane never used.** On-device reasoning compiles knowledge on
   exactly the same terms — the same evidence, the same provenance, the same durability. A frontier lane makes the
   compiled world better and faster to build; it is never what makes it possible.

What the cloud lane buys, then, is not capability. It is **compilation rate**: the same world, sooner.

## The ratchet, and what makes it pay

The economics only work if compiled knowledge is *narrowly invalidated*. An artefact that must be rebuilt whenever
anything changes is not infrastructure — it is a full recomputation with a filing cabinet attached, and this app
has already measured what that costs: three stalls in one day, 99% CPU with a frozen GUI, then 760%, each one a
consumer re-deriving what another consumer had just derived.

So every compiled artefact must **declare what invalidates it** and be keyed on exactly that. The Gazetteer's
recognition, built under this chapter, is the worked example: the measurement is keyed on the source, the analyzer
revision and the world's generation together, so confirming a person re-measures the chapter with that person
visible, while consulting the world a thousand times changes nothing. Measured on the next read after two
identities were confirmed:

```
[MEASURED] 40381 chars → 136 forms, 925 candidates, knowing 6 confirmed names
```

Six spellings the instrument was blind to on the previous read, seen for free on this one, because a reading had
settled who they were and the knowledge was compiled rather than re-derived.

The ratchet is the point: **the project's reasoning cost falls as its knowledge grows.** A frontier turn is
expensive once and its result is free forever; a local turn is cheap and its result is free forever. Neither is
paid twice for the same fact.

## The family, and the bar for joining it

The Living Gazetteer is the first compiled artefact, not the only intended one. Others that plainly fit the shape:
a **continuity ledger** (what has happened, and to whom, in the order the work establishes it), a **beat graph**
(the questions the work holds open and where they close — [ch.28](28-a-beat-is-the-question-it-raises.md)), an
**author-intent ledger** (what the writer has decided, and refused, about their own work), and a **retrieval
index** for resemblance ([ch.29](29-natural-language-measures-storify-interprets.md) rule 4).

None of them is admitted by being plausible. The bar, inherited from [ch.29](29-natural-language-measures-storify-interprets.md)
rule 11 and made general:

- it must **change what the writer sees or does** — not merely be computable, and not merely be interesting;
- it must **name what invalidates it**, narrowly;
- it must be **removable** without gating anything;
- it must be **wrong in an inspectable way**, with the evidence and the act that produced it attached;
- and it must **not overlap an existing artefact's authority.** Two artefacts that can disagree about the same
  fact will, and then the app has an oracle problem instead of a memory.

## What may never be compiled

The compiler's reach stops exactly where authority begins:

- **Meaning.** What a passage is about, what a beat is, what a character wants: read every time, by the one
  reasoning ([ch.12](12-animating-truth.md)). Compiled knowledge is what the reading reasons *from*,
  never what it concludes.
- **Verdicts.** "This beat is wrong", "this claim is false", "this reading is better" — not artefacts. Gradings
  are reported with their grounds ([ch.29](29-natural-language-measures-storify-interprets.md) rule 6).
- **Routing and spending.** No compiled artefact may pick a lane, target a turn, gate a step, or authorise a cost.
- **Confidence as a number.** The proposal behind this chapter asks each entry to carry a confidence; this app
  does not do that, for the reason [ch.24](24-the-reasoning-is-an-uncertainty-map.md) gives: 0.63 is not a
  reason and cannot be argued with. An entry carries a **status**, its **evidence** and its **history**, which is
  strictly more information and is legible to a writer.
- **The writer's judgment.** Where the writer and the compiled world disagree, the writer is right, and the
  correction is recorded as theirs ([ch.30](30-the-living-gazetteer.md) rule 9).

## Compiled knowledge is dated, and the surface says so

A compiled world moves. A reading made under an earlier world, an earlier instrument or an earlier build is not
wrong, but it is not what this app would produce now — and presenting it as current is the same lie as an
unattributed claim. So every reading carries the stamp of what made it, and the stage states it plainly:

> This is what the reading at 15:28 read, with an earlier version of Reframe. Reading again may find something else.

The old reading is not discarded and not hidden: it is named, and reading again is one action. Without this, an
accumulating architecture becomes indistinguishable from a broken one — every fix looks unlanded, and the writer
is left to guess which of the things on screen are still true.

## Rules

1. **Separate learning from remembering.** Reframe trains nothing. What accumulates is explicit, evidenced project
   memory — never weights, never a fine-tune, never an adapter that encodes this manuscript.
2. **Frontier reasoning is a compiler, not a runtime.** It is spent on what is hard and durable, and what it
   settles is compiled. Repeated frontier turns to rediscover project facts are a defect.
3. **On-device is the first lane, and the architecture is complete without the other one.** Escalation is reasoned,
   authorised per act, and never structurally required.
4. **A compiled artefact is authored, evidenced, falsifiable, revisable, historied and removable.** Anything
   missing one of these is not admitted.
5. **It is stored, not cached.** Nothing compiled is silently discarded or silently rebuilt.
6. **Every artefact declares what invalidates it, narrowly**, and consumers READ it rather than re-deriving it
   ([ch.29](29-natural-language-measures-storify-interprets.md) rule 10).
7. **No compiled artefact routes a turn, gates a step, sets a status, decides meaning, or authorises a spend.**
8. **No two artefacts may hold authority over the same fact.**
9. **A new artefact ships only when it changes what the writer sees or does**, and goes back in the drawer, with
   its tests, when it does not.
10. **The writer owns the world's memory.** Any entry is correctable in a sentence, the correction is recorded as
    theirs, and it wins.
11. **Anything shown from compiled knowledge is dated.** A reading, a map or a claim drawn from an earlier world or
    build says so on the surface, and offers the act that would refresh it.
12. **Name artefacts for what they hold, never for authority they lack** ([ch.29](29-natural-language-measures-storify-interprets.md)
    rule 12): `Gazetteer`, `ContinuityLedger` — never `TruthIndex`, `KnowledgeBase`, `WorldModel`.

## Acceptance

- A fact the project has settled is never re-derived by a later pass; the pass reads it, and can say where it came
  from.
- Deleting every compiled artefact leaves the manuscript whole, readable and fully navigable — only accumulated
  knowledge is lost, and the surface says it is gone.
- Every entry in every artefact traces to the passage and the act that produced it, and shows its revisions.
- A run with the cloud lane disabled produces the same kinds of artefacts, from on-device reasoning, at a lower
  rate.
- No spend occurs without an explicit authorisation at the call site, and no code path requires one to proceed.
- Re-measuring after a confirmation costs one measurement; consulting the world costs nothing.
- Any surface drawn from compiled knowledge shows when it was made, and offers the action that remakes it.

## Governing sentence

Reframe shall spend expensive reasoning to compile durable, evidenced, revisable knowledge of one manuscript's
world, and shall execute against that knowledge locally, forever after — so that the app grows better at the
writer's work without the writer paying again for what it has already understood.
