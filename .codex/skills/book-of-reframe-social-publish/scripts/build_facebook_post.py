#!/usr/bin/env python3
"""Build a reviewable Facebook post package from a command or publication chapter."""

import argparse
import json
from pathlib import Path
import re
import shutil


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("book_root", type=Path)
    parser.add_argument("command_page", nargs="?", type=Path)
    parser.add_argument("--chapter-page", type=Path, help="Publication chapter page for a governed illustration post")
    parser.add_argument("--publication-root", type=Path, help="Reframe-Refactoring checkout containing site/")
    parser.add_argument("--public-url", help="Canonical public URL to place in the post")
    parser.add_argument("--teaser", required=True)
    parser.add_argument("--book-url")
    parser.add_argument("--output", type=Path, default=Path("facebook-post"))
    args = parser.parse_args()

    if bool(args.command_page) == bool(args.chapter_page):
        raise SystemExit("provide exactly one of command_page or --chapter-page")

    if args.chapter_page:
        publication_root = args.publication_root or args.book_root
        page = args.chapter_page if args.chapter_page.is_absolute() else publication_root / args.chapter_page
        text = page.read_text(encoding="utf-8")
        image_match = re.search(r'<meta property="og:image" content="([^"]+)"', text)
        if not image_match:
            raise SystemExit("chapter page has no og:image")
        image = publication_root / "site" / "assets" / "social" / Path(image_match.group(1)).name
        if not image.is_file():
            raise SystemExit(f"social image missing: {image}")
        share_match = re.search(r'href="(/social/[^\"]+/)"', text)
        if not share_match:
            raise SystemExit("chapter page has no cache-safe social share URL")
        if not args.public_url:
            raise SystemExit("--public-url is required for a chapter post")
        chapter_title = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.S)
        title = re.sub(r"<[^>]+>", "", chapter_title.group(1)).strip() if chapter_title else page.parent.name
        caption = (
            f"{args.teaser.strip()}\n\n"
            f"{title} — a governed publication projection, not a claim that the feature is live in Reframe.\n"
            f"Read the full story: {args.public_url.rstrip('/')}/"
        )
        package = {
            "kind": "chapter-publication",
            "chapter": page.parent.name,
            "image": image.name,
            "imageUrl": image_match.group(1),
            "caption": caption,
            "publicUrl": args.public_url.rstrip("/") + "/",
            "sharePath": share_match.group(1),
            "externalPublish": False,
        }
        args.output.mkdir(parents=True, exist_ok=True)
        shutil.copy2(image, args.output / image.name)
        (args.output / "facebook-post.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
        (args.output / "README.md").write_text(
            "# Facebook post package\n\n"
            f"Chapter: `{page.parent.name}`\n\n"
            "The image is the publication's generated social illustration. The caption labels it as a governed "
            "projection. This package has not been posted externally.\n",
            encoding="utf-8",
        )
        print(f"built Facebook package for {page.parent.name}: {args.output}")
        return 0

    if not args.book_url:
        raise SystemExit("--book-url is required for a command post")

    page = args.command_page if args.command_page.is_absolute() else args.book_root / args.command_page
    text = page.read_text(encoding="utf-8")
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines or not lines[0].startswith("!["):
        raise SystemExit("command page must begin with its GUI snapshot image")
    image_match = re.search(r"\]\(([^)]+)\)", lines[0])
    if not image_match:
        raise SystemExit("snapshot image link is missing")
    image = (page.parent / image_match.group(1)).resolve()
    if not image.is_file():
        raise SystemExit(f"snapshot image missing: {image}")
    if "Live drive:" not in text:
        raise SystemExit("command page has no live-drive proof reference")
    command_match = re.search(r"`(/[^`]+)`", text)
    if not command_match:
        raise SystemExit("command page has no slash command identity")
    command = command_match.group(1)
    evidence = args.book_root / "evidence/2026-08-03/command-evidence.json"
    evidence_doc = json.loads(evidence.read_text(encoding="utf-8"))
    command_evidence = evidence_doc.get("commands", {}).get(command)
    if not command_evidence or command_evidence.get("status") != "live-accepted":
        raise SystemExit(f"command is not live-accepted in evidence manifest: {command}")
    release_doc = json.loads((args.book_root / "evidence/2026-08-03/reframe-release-surface.json").read_text(encoding="utf-8"))
    release_status = release_doc.get("status", "unknown")
    status_line = "Development/evidence preview — no released App surface is recorded." if release_status != "released" else "From a named Reframe release."
    caption = f"{args.teaser.strip()}\n\n{command} — {status_line}\nRead the evidence-backed story in The Book of Reframe: {args.book_url}"
    args.output.mkdir(parents=True, exist_ok=True)
    output_image = args.output / image.name
    shutil.copy2(image, output_image)
    package = {
        "command": command,
        "image": output_image.name,
        "caption": caption,
        "evidence": command_evidence,
        "releaseStatus": release_status,
        "externalPublish": False,
    }
    (args.output / "facebook-post.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")
    (args.output / "README.md").write_text(
        "# Facebook post package\n\n"
        f"Command: `{command}`\n\n"
        "The image is the command page's own live-drive GUI snapshot. This package has not been posted externally.\n",
        encoding="utf-8",
    )
    print(f"built Facebook package for {command}: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
