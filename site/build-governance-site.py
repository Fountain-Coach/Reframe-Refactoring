#!/usr/bin/env python3
"""Build the public governance projection from the repository's reviewed Markdown chapters."""

from __future__ import annotations

import html
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
DOCS = REPO / "docs"
CHAPTERS = ROOT / "chapters"
ASSETS = ROOT / "assets"
LOGO = ASSETS / "fountain-coach-logo-transparent.png"


def title_for(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()
    for line in first:
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def chapter_files() -> list[Path]:
    return sorted(
        (path for path in DOCS.glob("*.md") if path.name not in {"README.md"}),
        key=lambda path: (int(path.name[:2]) if path.name[:2].isdigit() else 999, path.name),
    )


def slug(path: Path) -> str:
    return path.stem


def markdown_html(path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html", "--wrap=none", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    result = re.sub(r'href="(?!https?://)(?:\.\./)?(?:docs/)?([^\"]+?)\.md(#[^\"]+)?"',
                    lambda m: f'href="/chapters/{m.group(1)}/{m.group(2) or ""}"', result)
    result = result.replace('src="illustrations/', 'src="/assets/illustrations/')
    result = result.replace('src="assets/', 'src="/assets/')
    return result


def shell(page_title: str, content: str, active: str = "") -> str:
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{html.escape(page_title)} — Reframe Governance</title>
  <meta name="description" content="The public Reframe Governance book: reviewed architectural doctrine, validation rules, and publication boundaries.">
  <link rel="icon" type="image/png" href="/assets/fountain-coach-logo-transparent.png">
  <link rel="apple-touch-icon" href="/assets/fountain-coach-logo-transparent.png">
  <link rel="canonical" href="https://governance.fountain.coach{active}">
  <link rel="stylesheet" href="/assets/governance.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to chapter</a>
  <header class="topbar"><a class="wordmark" href="/"><img class="wordmark-logo" src="/assets/fountain-coach-logo-transparent.png" alt="Fountain Coach logo"><span>REFRAME <small>GOVERNANCE BOOK</small></span></a><button class="menu-button" type="button" data-menu-button aria-controls="chapter-nav" aria-expanded="false">Chapters</button></header>
  <div class="workspace">
    <nav class="chapter-rail" id="chapter-nav" data-chapter-nav aria-label="Governance chapters"><div class="rail-label">READING INDEX</div><a class="rail-home" href="/">Governance overview</a>{chapter_nav(active)}</nav>
    <main id="main" class="chapter-canvas"><div class="canvas-kicker">FCIS · REFRAME REFACTORING · PUBLIC PROJECTION</div>{content}<footer class="footer"><a href="/">Reframe Governance</a><span>Source: <a href="https://github.com/Fountain-Coach/Reframe-Refactoring">Reframe-Refactoring</a></span><span>Public projection · implementation truth remains in the governed runtime</span></footer></main>
  </div>
  <script src="/assets/governance.js" defer></script>
</body>
</html>'''


_chapter_cache: list[tuple[Path, str]] | None = None


def chapter_nav(active: str) -> str:
    global _chapter_cache
    if _chapter_cache is None:
        _chapter_cache = [(path, title_for(path)) for path in chapter_files()]
    return "".join(
        f'<a class="chapter-link{" active" if "/chapters/" + slug(path) + "/" == active else ""}" href="/chapters/{slug(path)}/"><span>{path.stem[:2] if path.stem[:2].isdigit() else "·"}</span>{html.escape(title)}</a>'
        for path, title in _chapter_cache
    )


def main() -> None:
    CHAPTERS.mkdir(exist_ok=True)
    for old in CHAPTERS.glob("*/index.html"):
        old.unlink()
    source_illustrations = DOCS / "illustrations"
    target_illustrations = ASSETS / "illustrations"
    if source_illustrations.exists():
        shutil.copytree(source_illustrations, target_illustrations, dirs_exist_ok=True)
    if not LOGO.exists():
        raise FileNotFoundError(f"missing reviewed Fountain Coach logo asset: {LOGO}")
    files = chapter_files()
    index_items = "".join(f'<a href="/chapters/{slug(path)}/"><span>{path.stem[:2] if path.stem[:2].isdigit() else "·"}</span>{html.escape(title_for(path))}</a>' for path in files)
    overview = f'''<section class="overview"><div class="eyebrow">PUBLIC FCIS PROJECTION</div><h1>Reframe Governance</h1><p class="lede">The architectural book behind the Reframe writing instrument: one readable source of doctrine for humans, maintainers, and implementation agents.</p><div class="overview-rule"></div><p class="muted">Choose a chapter from the semantic rail. The public projection explains intent and validation boundaries; the runtime, MIDI backplane, and live Store remain operational authority.</p></section><section class="chapter-index" aria-labelledby="index-title"><div class="section-label">CHAPTER INDEX</div><h2 id="index-title">Read by chapter.</h2><div class="index-grid">{index_items}</div></section>'''
    (ROOT / "index.html").write_text(shell("Reframe Governance", overview, "/"), encoding="utf-8")
    for path in files:
        current = f"/chapters/{slug(path)}/"
        content = f'<article class="governance-chapter"><div class="chapter-meta">GOVERNANCE CHAPTER · {path.stem[:2] if path.stem[:2].isdigit() else "—"}</div>{markdown_html(path)}</article>'
        target = CHAPTERS / slug(path)
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(shell(title_for(path), content, current), encoding="utf-8")
    print(f"built {len(files)} governance chapters")


if __name__ == "__main__":
    main()
