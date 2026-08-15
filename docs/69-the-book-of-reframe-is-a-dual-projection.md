# The Book of Reframe Is a Dual Projection

The Book of Reframe has two legitimate audiences: the public human reader and the Reframe maintainer. They share one
reviewed scenario model, but they do not receive the same projection or the same authority.

The public subdomain is the human reference. It explains what scenarios exist, why they matter, what evidence a claim
requires, which journeys are draft or live-accepted, and how a maintainer can ask Reframe to work on the next one. It
must remain useful without access to the private runtime repository.

Reframe's maintainer context is a separate, role-gated projection generated from the same reviewed Book commit. It may
contain internal procedure references needed to inspect, author, validate, and run a scenario. It is not a writer
manuscript, a public runtime contract, or an execution authorization.

## Rules

1. The public Book MUST remain published at its canonical human-facing subdomain as a sanitized, evidence-backed
   reference. Making a maintainer projection does not reduce the public documentation obligation.
2. The public Book and maintainer snapshot MUST identify the same source Book commit and content digest. A maintainer
   snapshot from an unreviewed working tree is invalid.
3. The runtime IDL, generated capability facts, live FountainStore state, and typed runtime contracts remain
   operational authority. The Book, public or maintainer, is a projection and cannot authorize execution or change
   capability status.
4. The public projection MAY contain scenario IDs, capability identities, prerequisites, sanitized predicates,
   evidence vocabulary, statuses, provenance, governance links, and maintainer request instructions.
5. The public projection MUST NOT contain private Store records, credentials, deployment secrets, unpublished
   manuscript material, raw runtime internals, or procedures that would expose a private control boundary.
6. The maintainer projection MUST be role-gated, content-addressed, provenance-bound, and excluded from writer-facing
   retrieval and normal manuscript context. It may add internal procedure references, but not new behavioral claims.
7. Reframe MUST consume the maintainer projection through an explicit maintainer knowledge boundary. It MUST NOT fetch
   the public website during execution and MUST NOT treat retrieved Book prose as a tool or capability decision.
8. Scenario discovery, authoring, validation, execution, and promotion remain typed maintainer operations. A Book
   entry or knowledge result may select a scenario identity, but only the scenario capability may execute it.
9. Only the intersection of internal behavioral proof and independent Live Drive AX/CoreGraphics/VRT evidence may
   become `live-accepted` or enter a completed public command claim.
10. Every generated or published projection MUST fail closed when its source commit, digest, role boundary, or
    sanitization review is missing.

## The projections

```text
governed scenario registry + reviewed Book commit
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
 public Book reference   maintainer knowledge snapshot
 humans / public web     Reframe / role-gated context
          │                   │
          └───────┬───────────┘
                  ▼
       runtime contract + independent witness
```

The public site is for human inspection and shared vocabulary. The maintainer snapshot is for efficient scenario
research and planning. Neither projection replaces FountainStore behavioral proof, the runtime capability registry,
or independent Live Drive evidence.

## Maintainer request loop

When a maintainer asks, “Add the next scenario for `/world`,” Reframe follows one governed loop:

1. resolve the public scenario identity and coverage status;
2. report the prerequisite chain and expected terminal artifacts;
3. author or repair the private scenario contract when it is absent or stale;
4. validate the contract against runtime and governance;
5. execute through `reframe.e2e.scenario.run` on an isolated managed Store;
6. invoke independent Live Drive for AX, window-ID, and visual evidence;
7. update the sanitized public projection only from the resulting evidence bundle.

The public Book should make this loop understandable to another human. The maintainer snapshot should make it
efficient for Reframe. The two surfaces are complementary, not duplicate authorities.

## Governing sentence

The Book is public reference for humans and a reviewed maintainer projection for Reframe; one source commit and digest
bind them, while runtime state and independent evidence remain the authorities for what may run and what actually
happened.
