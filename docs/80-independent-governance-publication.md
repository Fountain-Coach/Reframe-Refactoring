# 80 — Independent Governance Publication

The governance book is a public projection of the reviewed Reframe refactoring doctrine. It must be readable as a
book by humans and resolvable as a source-bound reference by maintainers and implementation agents. GitHub remains a
source and provenance mirror; it is not the public delivery surface.

## Two projections, two jobs

The [Book of Reframe](https://book.fountain.coach/) is the light, writer-facing product reference. The governance
book at [governance.fountain.coach](https://governance.fountain.coach/) is the OS-aware, source-oriented maintainer
projection: it exposes the chapter rail, source-oriented typography, chapter provenance, and the boundary between
public doctrine and private implementation evidence. Its light and dark palettes follow the reader's operating-system
appearance preference. The two sites may link to one another, but one must not silently
inherit the other's shell or claim its evidence.

## Publication contract

1. `Reframe-Refactoring/docs/` is the reviewed governance source. The generated `site/` projection is built by
   `site/build-governance-site.py`; hand-edited generated HTML is not authoritative.
2. The canonical public host is `governance.fountain.coach`. Its deployment root is a dedicated, rollback-capable
   document root and must not share the Book or manifesto root.
3. The deployment host keeps clean source clones for provenance and reproducibility. A source clone is not permission
   to publish private Store data, credentials, runtime source, or unpublished manuscript material.
4. Every publication records the source commit, generated-site checks, host/root tuple, HTTPS response checks, and the
   independent AX/VRT result. If AX or VRT cannot be run, that gap is reported rather than inferred from curl or a
   static screenshot.
5. A release is not complete until the overview, a representative chapter, its reviewed illustration assets, and
   canonical links return successfully over HTTPS.
6. GitHub publication delivery may be retired only after the independent host passes the complete gate above. GitHub
   history, source links, and repository provenance remain preserved.

## Why this boundary exists

A repository renderer is useful for source review but is not a stable publication design. The independent projection
lets governance evolve its own navigation, responsive behavior, metadata, accessibility evidence, and rollback
discipline without confusing source browsing with a released public book. The separation also makes the deployment
target explicit: humans read the governed projection, while maintainers can always trace each chapter back to a named
source commit.
