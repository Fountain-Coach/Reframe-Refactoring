#!/usr/bin/env python3
"""Build the public governance projection from the repository's reviewed Markdown chapters."""

from __future__ import annotations

import html
import hashlib
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
DEFAULT_SOCIAL_IMAGE = "/assets/social/92-fountain-coach-publication-estate-3682394af134.jpg"


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


def build_social_illustration(path: Path, title: str) -> str | None:
    illustration = illustration_for(path)
    if not illustration:
        return None
    source = DOCS / "illustrations" / illustration
    if not source.exists():
        raise FileNotFoundError(f"missing principal illustration for social post: {source}")
    SOCIAL_ASSETS.mkdir(parents=True, exist_ok=True)
    destination = SOCIAL_ASSETS / f"{path.stem}.jpg"
    with tempfile.TemporaryDirectory(prefix="reframe-social-card-") as temp_dir:
        rendered_source = Path(temp_dir) / "source.png"
        if source.suffix.lower() == ".svg":
            subprocess.run(["rsvg-convert", "-o", str(rendered_source), str(source)], check=True)
        else:
            rendered_source = source
        # Facebook's post image is the chapter's principal reviewed illustration.
        # Fit it into the stable 1200×630 transport canvas without adding a second
        # branded/card composition that could be mistaken for the source artwork.
        subprocess.run([
            "magick", str(rendered_source), "-auto-orient", "-background", "#f6f8f9",
            "-alpha", "remove", "-alpha", "off", "-resize", "1200x630",
            "-gravity", "center", "-extent", "1200x630", "-strip", "-quality", "92", str(destination),
        ], check=True)
    digest = hashlib.sha256(destination.read_bytes()).hexdigest()[:12]
    versioned = SOCIAL_ASSETS / f"{path.stem}-{digest}.jpg"
    destination.replace(versioned)
    return f"/assets/social/{versioned.name}"


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


def chapter_pager(path: Path, files: list[Path]) -> str:
    index = files.index(path)
    previous = files[index - 1] if index else None
    following = files[index + 1] if index + 1 < len(files) else None
    previous_link = (f'<a class="chapter-pager-link" data-chapter-prev rel="prev" href="/chapters/{slug(previous)}/" '
                    f'aria-label="Previous chapter: {html.escape(title_for(previous))}">'
                    f'<span aria-hidden="true">←</span><span><small>PREVIOUS CHAPTER</small>{html.escape(title_for(previous))}</span></a>'
                    if previous else '<span class="chapter-pager-link chapter-pager-disabled" aria-hidden="true"><span>←</span><span><small>PREVIOUS CHAPTER</small>Beginning of book</span></span>')
    next_link = (f'<a class="chapter-pager-link chapter-pager-next" data-chapter-next rel="next" href="/chapters/{slug(following)}/" '
                 f'aria-label="Next chapter: {html.escape(title_for(following))}"><span><small>NEXT CHAPTER</small>{html.escape(title_for(following))}</span><span aria-hidden="true">→</span></a>'
                 if following else '<span class="chapter-pager-link chapter-pager-disabled chapter-pager-next" aria-hidden="true"><span><small>NEXT CHAPTER</small>End of book</span><span>→</span></span>')
    return (f'<nav class="chapter-pager" data-chapter-pager aria-label="Chapter navigation">'
            f'{previous_link}<span class="chapter-pager-position">CHAPTER {index + 1} OF {len(files)}</span>{next_link}</nav>')


def shell(page_title: str, content: str, active: str = "", canonical: str | None = None,
          social_image: str | None = None, pager: str = "") -> str:
    canonical = canonical or active
    social_image = social_image or DEFAULT_SOCIAL_IMAGE
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
        "publisher": {"@type": "Organization", "name": "Fountain Coach", "url": "https://fountain.coach/", "logo": "https://fountain.coach/assets/fountain-coach-logo.png"},
    })
    social_url = f"https://governance.fountain.coach{social_image}"
    social_tags = f'''\n  <meta property="og:type" content="article">\n  <meta property="og:title" content="{html.escape(page_title)}">\n  <meta property="og:url" content="https://governance.fountain.coach{canonical}">\n  <meta property="og:image" content="{social_url}">\n  <meta property="og:image:alt" content="Fountain Coach publication estate illustration for {html.escape(page_title)}">\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:image" content="{social_url}">'''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{html.escape(page_title)} — Reframe Governance</title>
  <meta name="description" content="The public Reframe Governance book: reviewed architectural doctrine, validation rules, and publication boundaries.">
  <meta name="fountain:publication-role" content="Rules and authority">
  <link rel="icon" type="image/png" href="/assets/fountain-coach-logo-transparent.png">
  <link rel="apple-touch-icon" href="/assets/fountain-coach-logo-transparent.png">
  <link rel="canonical" href="https://governance.fountain.coach{canonical}">
{social_tags}
  <script type="application/ld+json">{structured}</script>
  <link rel="stylesheet" href="/assets/governance.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to chapter</a>
  <header class="topbar"><a class="wordmark" href="https://fountain.coach/" aria-label="Fountain Coach home"><img class="wordmark-logo" src="/assets/fountain-coach-logo-transparent.png" alt="Fountain Coach logo"><span>FOUNTAIN COACH <small>GOVERNANCE · RULES AND AUTHORITY</small></span></a><nav class="estate-nav" aria-label="Fountain Coach publications"><a href="https://fountain.coach/">Estate</a><a href="https://book.fountain.coach/">Book</a><a href="https://governance.fountain.coach/" aria-current="page">Governance</a><a href="https://instruments.fountain.coach/">Instruments</a><a href="https://status.fountain.coach/">Status</a></nav><div class="topbar-actions"><button class="theme-button" type="button" data-theme-toggle aria-pressed="false">Theme: system</button><button class="menu-button" type="button" data-menu-button aria-controls="chapter-nav" aria-expanded="false">Chapters</button></div></header>
  <div class="workspace">
    <nav class="chapter-rail" id="chapter-nav" data-chapter-nav aria-label="Governance chapters"><div class="rail-label">READING INDEX</div><a class="rail-home{home_active}" href="/"{home_current}>Governance overview</a><a class="rail-status{status_active}" href="/status-quo/"{status_current}>Current status</a>{chapter_nav(active)}</nav>
    <main id="main" class="chapter-canvas"><nav class="breadcrumbs" aria-label="Breadcrumb"><a href="https://fountain.coach/">Fountain Coach</a><span aria-hidden="true">›</span><a href="https://governance.fountain.coach/">Governance</a><span aria-hidden="true">›</span><span aria-current="page">{html.escape(page_title)}</span></nav><div class="canvas-kicker"><span>FCIS · REFRAME REFACTORING · <span class="publication-state">PUBLISHED PROJECTION</span></span></div>{pager}{content}<footer class="footer"><div class="footer-estate"><strong>Fountain Coach publication estate</strong><a href="https://fountain.coach/">Identity</a><a href="https://book.fountain.coach/">Book · human reference</a><a href="https://governance.fountain.coach/">Governance · rules and authority</a><a href="https://instruments.fountain.coach/">Instruments · MIDI2 catalog</a><a href="https://status.fountain.coach/">Status · company and legal context</a></div><div class="footer-legal"><a href="/legal/">Legal notices</a><a href="/privacy/">Privacy</a><a href="/accessibility/">Accessibility</a><a href="/copyright/">Copyright</a><a href="/compliance/">EU compliance</a><a href="/status-quo/">Source and provenance</a></div><span>Public projection · governance establishes doctrine, not runtime state or live acceptance.</span></footer></main>
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
    social_routes = ROOT / "social"
    if social_routes.exists():
        shutil.rmtree(social_routes)
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
        social_image = build_social_illustration(path, title)
        social_link = (f'<p class="social-preview-link"><a href="{current}">Open this semantic chapter route for social sharing</a> · '
                       f'<a href="{social_image}">1200×630 image</a></p>'
                       if social_image else "")
        content = f'<article class="governance-chapter"><div class="chapter-meta">GOVERNANCE CHAPTER · {path.stem[:2] if path.stem[:2].isdigit() else "—"}</div><p class="chapter-state"><strong>{html.escape(status["label"])}</strong> · {status_description(status)}</p>{social_link}{markdown_html(path)}</article>'
        target = CHAPTERS / slug(path)
        target.mkdir(exist_ok=True)
        # A changed principal illustration changes the digest-named share route.
        # Remove superseded routes so generated output cannot retain stale Facebook targets.
        chapter_share_root = target / "share"
        if chapter_share_root.exists():
            shutil.rmtree(chapter_share_root)
        (target / "index.html").write_text(shell(title, content, current, social_image=social_image,
                                                  pager=chapter_pager(path, files)), encoding="utf-8")
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
