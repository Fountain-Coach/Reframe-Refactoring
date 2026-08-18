#!/usr/bin/env python3
"""Build the public governance projection from the repository's reviewed Markdown chapters."""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
DOCS = REPO / "docs"
CHAPTERS = ROOT / "chapters"
ASSETS = ROOT / "assets"
SOCIAL_ASSETS = ASSETS / "social"
LOGO = ASSETS / "fountain-coach-logo-transparent.png"
LEGAL_CONTENT = ROOT / "legal-content"
SITE_CONTENT = ROOT / "content"
STATUS_MAP_PATH = ROOT / "chapter-status.json"
LEGAL_ROUTES = {
    "legal": ("Legal notices", "legal-notices.md"),
    "privacy": ("Privacy", "privacy.md"),
    "accessibility": ("Accessibility", "accessibility.md"),
    "copyright": ("Copyright", "copyright.md"),
    "compliance": ("EU compliance scope", "compliance.md"),
}


def title_for(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()
    for line in first:
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def chapter_files() -> list[Path]:
    return sorted(
        (path for path in DOCS.glob("*.md") if path.name not in {"README.md"} and not path.name.startswith("._")),
        key=lambda path: (int(path.name[:2]) if path.name[:2].isdigit() else 999, path.name),
    )


def slug(path: Path) -> str:
    return path.stem


def status_map() -> dict:
    return json.loads(STATUS_MAP_PATH.read_text(encoding="utf-8"))


def chapter_status(path: Path) -> dict:
    statuses = status_map()
    return statuses.get("chapters", {}).get(path.stem, statuses["default"])


def status_badge(status: dict) -> str:
    return f'<span class="status-badge status-{html.escape(status["key"])}">{html.escape(status["label"])}</span>'


def status_description(status: dict) -> str:
    return html.escape(status["description"])


def illustration_for(path: Path) -> str | None:
    match = re.search(r"!\[[^\]]*\]\(illustrations/([^\)]+)\)", path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def social_card_for(path: Path) -> str | None:
    illustration = illustration_for(path)
    return f"/assets/social/{path.stem}.jpg" if illustration else None


def build_social_card(path: Path, title: str) -> str | None:
    illustration = illustration_for(path)
    if not illustration:
        return None
    source = DOCS / "illustrations" / illustration
    if not source.exists():
        raise FileNotFoundError(f"missing illustration for social card: {source}")
    SOCIAL_ASSETS.mkdir(parents=True, exist_ok=True)
    destination = SOCIAL_ASSETS / f"{path.stem}.jpg"
    with tempfile.TemporaryDirectory(prefix="reframe-social-card-") as temp_dir:
        rendered_source = Path(temp_dir) / "source.png"
        if source.suffix.lower() == ".svg":
            subprocess.run(["rsvg-convert", "-o", str(rendered_source), str(source)], check=True)
        else:
            rendered_source = source
        image_panel = Path(temp_dir) / "image-panel.png"
        subprocess.run([
            "magick", str(rendered_source), "-auto-orient", "-resize", "600x370>",
            "-background", "#edf2f4", "-gravity", "center", "-extent", "600x370", str(image_panel),
        ], check=True)
        logo = Path(temp_dir) / "logo.png"
        subprocess.run([
            "magick", str(LOGO), "-resize", "52x52", "-fill", "#607985", "-colorize", "100%", str(logo),
        ], check=True)
        title_image = Path(temp_dir) / "title.png"
        subprocess.run([
            "magick", "-background", "none", "-fill", "#3d5664", "-font", "Courier-Bold",
            "-pointsize", "28", "-size", "430x160", f"caption:{title}", str(title_image),
        ], check=True)
        subprocess.run([
            "magick", "-size", "1200x630", "xc:#f6f8f9",
            "-stroke", "#c6d1d7", "-strokewidth", "2", "-fill", "none",
            "-draw", "rectangle 24,24 1176,606",
            str(image_panel), "-geometry", "+42+122", "-composite",
            str(logo), "-geometry", "+42+36", "-composite",
            "-stroke", "none",
            "-font", "Courier-Bold", "-fill", "#3d5664", "-pointsize", "22",
            "-draw", "text 112,58 'FOUNTAIN COACH'",
            "-font", "Courier", "-fill", "#72848e", "-pointsize", "14",
            "-draw", "text 112,82 'REFRAME GOVERNANCE'",
            "-font", "Courier-Bold", "-fill", "#477a88", "-pointsize", "15",
            "-draw", f"text 700,125 'CHAPTER {path.stem[:2] if path.stem[:2].isdigit() else '—'}'",
            str(title_image), "-geometry", "+700+150", "-composite",
            "-stroke", "#c6d1d7", "-strokewidth", "2", "-draw", "line 700,390 1140,390",
            "-stroke", "none",
            "-font", "Courier-Bold", "-fill", "#3d5664", "-pointsize", "16",
            "-draw", "text 700,425 'REVIEWED ILLUSTRATION'",
            "-font", "Courier", "-fill", "#72848e", "-pointsize", "15",
            "-draw", "text 700,465 'PUBLIC GOVERNANCE PROJECTION'",
            "-draw", "text 700,495 'SOURCE ARTWORK PRESERVED'",
            "-draw", "text 700,565 'SOCIAL POST ILLUSTRATION'",
            "-strip", "-quality", "90", str(destination),
        ], check=True)
    return social_card_for(path)


def markdown_html(path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=gfm", "--to=html", "--wrap=none", str(path)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    result = re.sub(r'href="(?!https?://)(?:\.\./)?(?:docs/)?([^\"]+?)\.md(#[^\"]+)?"',
                    lambda m: f'href="/chapters/{m.group(1)}/{m.group(2) or ""}"', result)
    result = result.replace('href="https://github.com/Fountain-Coach/Reframe-Refactoring/blob/main/README.md"', 'href="/"')
    result = result.replace('href="https://github.com/Fountain-Coach/Reframe-Refactoring"', 'href="/"')
    result = result.replace('href="https://github.com/Fountain-Coach/midi2-gpu-fabric/tree/main/apps/modernization-studio/docs/reframe-grounding-first-refactor"', 'href="/status-quo/"')
    result = re.sub(r'<a href="https://github.com/Fountain-Coach/UncertaintyScoreKit">([^<]+)</a>', r'\1', result)
    result = result.replace('src="illustrations/', 'src="/assets/illustrations/')
    result = result.replace('src="assets/', 'src="/assets/')
    return result


def legal_files() -> list[tuple[str, str, Path]]:
    return [(route, title, LEGAL_CONTENT / filename) for route, (title, filename) in LEGAL_ROUTES.items()]


def shell(page_title: str, content: str, active: str = "", canonical: str | None = None,
          social_image: str | None = None) -> str:
    canonical = canonical or active
    home_active = ' active' if active == '/' else ''
    home_current = ' aria-current="page"' if active == '/' else ''
    status_active = ' active' if active == '/status-quo/' else ''
    status_current = ' aria-current="page"' if active == '/status-quo/' else ''
    structured = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": page_title,
        "url": f"https://governance.fountain.coach{canonical}",
        "isPartOf": {"@type": "Book", "name": "Reframe Governance", "url": "https://governance.fountain.coach/"},
        "publisher": {"@type": "Organization", "name": "Fountain Coach", "url": "https://fountain.coach/"},
    })
    social_tags = ""
    if social_image:
        social_url = f"https://governance.fountain.coach{social_image}"
        social_tags = f'''\n  <meta property="og:type" content="article">\n  <meta property="og:title" content="{html.escape(page_title)}">\n  <meta property="og:image" content="{social_url}">\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:image" content="{social_url}">'''
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
  <link rel="canonical" href="https://governance.fountain.coach{canonical}">
{social_tags}
  <script type="application/ld+json">{structured}</script>
  <link rel="stylesheet" href="/assets/governance.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to chapter</a>
  <header class="topbar"><a class="wordmark" href="/"><img class="wordmark-logo" src="/assets/fountain-coach-logo-transparent.png" alt="Fountain Coach logo"><span>REFRAME <small>GOVERNANCE BOOK</small></span></a><button class="menu-button" type="button" data-menu-button aria-controls="chapter-nav" aria-expanded="false">Chapters</button></header>
  <div class="workspace">
    <nav class="chapter-rail" id="chapter-nav" data-chapter-nav aria-label="Governance chapters"><div class="rail-label">READING INDEX</div><a class="rail-home{home_active}" href="/"{home_current}>Governance overview</a><a class="rail-status{status_active}" href="/status-quo/"{status_current}>Current status</a>{chapter_nav(active)}</nav>
    <main id="main" class="chapter-canvas"><div class="canvas-kicker">FCIS · REFRAME REFACTORING · PUBLIC PROJECTION</div>{content}<footer class="footer"><a href="/">Reframe Governance</a><span>Source: <a href="/status-quo/">reviewed governance projection</a></span><span><a href="/legal/">Legal notices</a> · <a href="/privacy/">Privacy</a> · <a href="/accessibility/">Accessibility</a> · <a href="/copyright/">Copyright</a> · <a href="/compliance/">EU compliance</a></span><span>Public projection · implementation truth remains in the governed runtime</span></footer></main>
  </div>
  <script src="/assets/governance.js" defer></script>
</body>
</html>'''


_chapter_cache: list[tuple[Path, str]] | None = None


def chapter_nav(active: str) -> str:
    global _chapter_cache
    if _chapter_cache is None:
        _chapter_cache = [(path, title_for(path)) for path in chapter_files()]
    links = []
    for path, title in _chapter_cache:
        current = "/chapters/" + slug(path) + "/"
        active_class = " active" if current == active else ""
        current_attr = ' aria-current="page"' if current == active else ""
        links.append(
            f'<a class="chapter-link{active_class}" href="{current}"{current_attr}>'
            f'<span>{path.stem[:2] if path.stem[:2].isdigit() else "·"}</span>'
            f'<span>{html.escape(title)} {status_badge(chapter_status(path))}</span></a>'
        )
    return "".join(links)


def main() -> None:
    # Finder/AppleDouble sidecars are not publication content. Remove stale sidecars from prior macOS copies
    # before generating so validators never mistake them for UTF-8 HTML or Markdown.
    for sidecar in ROOT.rglob("._*"):
        if sidecar.is_file() or sidecar.is_symlink():
            sidecar.unlink()
        elif sidecar.is_dir():
            shutil.rmtree(sidecar)
    CHAPTERS.mkdir(exist_ok=True)
    for old in CHAPTERS.glob("*/index.html"):
        old.unlink()
    SOCIAL_ASSETS.mkdir(exist_ok=True)
    for old in SOCIAL_ASSETS.glob("*.jpg"):
        old.unlink()
    source_illustrations = DOCS / "illustrations"
    target_illustrations = ASSETS / "illustrations"
    if source_illustrations.exists():
        shutil.copytree(
            source_illustrations,
            target_illustrations,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("._*", ".DS_Store", "__pycache__"),
        )
    if not LOGO.exists():
        raise FileNotFoundError(f"missing reviewed Fountain Coach logo asset: {LOGO}")
    files = chapter_files()
    index_items = "".join(
        f'<a href="/chapters/{slug(path)}/"><span>{path.stem[:2] if path.stem[:2].isdigit() else "·"}</span>'
        f'<span>{html.escape(title_for(path))} {status_badge(chapter_status(path))}</span></a>' for path in files
    )
    status_content = markdown_html(SITE_CONTENT / "status-quo.md")
    landing_status_content = re.sub(r"<h1[^>]*>.*?</h1>", "", status_content, count=1, flags=re.DOTALL)
    overview = f'''<section class="overview"><div class="eyebrow">PUBLIC FCIS PROJECTION · STATUS QUO</div><h1>Reframe Governance</h1>{landing_status_content}<p class="landing-note"><a href="/status-quo/">Open the stable status-quo page</a> · <a href="#index-title">Browse every retained chapter</a></p></section><section class="chapter-index" aria-labelledby="index-title"><div class="section-label">CHAPTER INDEX</div><h2 id="index-title">Read by chapter.</h2><p class="muted">Every chapter remains available. Labels describe its relationship to the current operating position; they do not erase the historical record.</p><div class="index-grid">{index_items}</div></section>'''
    (ROOT / "index.html").write_text(shell("Reframe Governance", overview, "/"), encoding="utf-8")
    status_page = f'<article class="status-quo-page"><div class="chapter-meta">PUBLICATION STATUS · CURRENT POSITION</div>{status_content}<p class="status-disclaimer">This page is a navigational status statement, not a replacement for the governed chapters or runtime evidence.</p></article>'
    (ROOT / "status-quo").mkdir(exist_ok=True)
    (ROOT / "status-quo" / "index.html").write_text(shell("Current Reframe Governance Status", status_page, "/status-quo/"), encoding="utf-8")
    for path in files:
        current = f"/chapters/{slug(path)}/"
        status = chapter_status(path)
        title = title_for(path)
        social_image = build_social_card(path, title)
        social_link = (f'<p class="social-preview-link"><a href="{social_image}">Open social post illustration (1200×630)</a></p>'
                       if social_image else "")
        content = f'<article class="governance-chapter"><div class="chapter-meta">GOVERNANCE CHAPTER · {path.stem[:2] if path.stem[:2].isdigit() else "—"}</div><p class="chapter-state"><strong>{html.escape(status["label"])}</strong> · {status_description(status)}</p>{social_link}{markdown_html(path)}</article>'
        target = CHAPTERS / slug(path)
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(shell(title, content, current, social_image=social_image), encoding="utf-8")
    for route, title, path in legal_files():
        current = f"/{route}/"
        content = f'<article class="legal-page"><div class="chapter-meta">PUBLICATION POLICY · {route.upper()}</div>{markdown_html(path)}</article>'
        target = ROOT / route
        target.mkdir(exist_ok=True)
        (target / "index.html").write_text(shell(title, content, current), encoding="utf-8")
    for sidecar in ROOT.rglob("._*"):
        if sidecar.is_file() or sidecar.is_symlink():
            sidecar.unlink()
    print(f"built {len(files)} governance chapters")


if __name__ == "__main__":
    main()
