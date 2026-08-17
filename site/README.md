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
or Store data.
