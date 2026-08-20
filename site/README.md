# Reframe Governance publication template

This directory is the public publication projection of `Reframe-Refactoring`. It is deliberately distinct from the
source repository's GitHub presentation and from the human-facing Book of Reframe:

- the Book is a light, writer-facing product reference;
- this site is an OS-aware, source-oriented maintainer/governance reader with a chapter rail;
- both projections use the Fountain Coach logo; this site uses a transparent dark-surface derivative of the reviewed
  logo asset from the Book publication;
- `docs/` remains the governance source of truth; `site/` is generated output;
- deployment target: `governance.fountain.coach` → `/var/www/reframe-governance`.

Build locally with:

```sh
python3 site/build-governance-site.py
```

The generator uses the installed `pandoc` executable, copies reviewed chapter illustrations, creates a chapter route
for every top-level governance Markdown file, includes the reviewed Fountain Coach identity asset, and emits no runtime
or Store data. The homepage and stable `/status-quo/` route are generated from `content/status-quo.md`; the
machine-readable `chapter-status.json` labels current orientation chapters without deleting or silently rewriting
historical material. Every page emits canonical metadata, JSON-LD, keyboard navigation, and an accessible chapter rail.
A chapter with a reviewed principal illustration emits a deterministic 1200×630 social illustration derived from that
artwork: the principal illustration itself is the Facebook/OG post image, fitted to the social canvas without a
competing title card. The semantic `/chapters/<slug>/` URL is both the reading page and the Facebook link; the image
URL is metadata/post media only and is never used as the link destination.
