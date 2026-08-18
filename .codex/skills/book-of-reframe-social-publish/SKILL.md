---
name: book-of-reframe-social-publish
description: Prepare and, only with explicit confirmation, publish a verified Book of Reframe command or governed chapter illustration as a Facebook post with deterministic image, caption, and public URL packaging.
---

# Book of Reframe Social Publish

Package one verified Book of Reframe command page or one reviewed publication chapter for Facebook. Command posts use
the page's leading GUI snapshot. Chapter posts use the generator's digest-named 1200×630 social illustration and its
cache-safe `/social/<asset>/` URL. Captions are short, writer-facing, and honest about whether the source is live
evidence or a governed projection. External posting requires separate explicit confirmation naming the destination.

## Authority and safety

- Read the Book maintenance skill, release manifest, command page, and evidence manifest first.
- Command pages must pass `verify_command_pages.py`; their evidence must be `live-accepted` with AX, window-ID, and
  FountainStore proof. Do not package a catalog screenshot for a different command.
- Chapter pages must be generated publication pages with a reviewed `og:image`, a digest-named `/social/<asset>/`
  route, and a 1200×630 JPEG. A design/mock chapter must say it is a governed projection; it must never be presented
  as a successful scenario or live feature.
- If the release manifest says `no-released-build` or `development-snapshot`, the caption MUST say this is a
  development/evidence preview. Never imply that the command is shipped.
- Do not copy prompts, manuscript text, private store data, local paths, access tokens, or internal execution IDs into
  the caption. Use the public Book URL and sanitized evidence links only.
- Creating a package is local and reversible. Posting is an external side effect and requires explicit confirmation,
  a named Facebook Page, and credentials supplied through the environment or an approved connector; never ask for or
  print a token.

## Workflow

1. Resolve the command page and its evidence manifest. Confirm the first non-empty page line is the command's own
   alt-texted image and that the referenced file exists.
2. For a live command, run `scripts/build_facebook_post.py <book-root> <command-page> --teaser "..." --book-url "..."`.
   For a governed chapter illustration, run `scripts/build_facebook_post.py <integration-root> --chapter-page
   <publication-root>/site/chapters/<slug>/index.html --publication-root <publication-root> --teaser "..."
   --public-url https://governance.fountain.coach/chapters/<slug>/share/<asset>/`.
   The public URL MUST be the chapter/share page. Never use the `/assets/` image URL or the image-only `/social/` route
   as the Facebook link: those are preview assets, not the story site.
   Use the canonical site URL from `site/site-config.json` (the interim GitHub Pages URL until a custom domain is
   selected), not a raw GitHub file URL.
3. Inspect the generated `facebook-post.json` and image visually. Every package must contain `image`, `caption`, a
   public URL, and `externalPublish: false`; command packages additionally contain evidence and release status.
4. Edit the teaser only from verified facts. A good caption has: a hook about the writer's problem, the command's
   visible act/result, an honest evidence or development-status line, and the public Book link.
5. For explicit publishing, recheck the destination Page, caption, image, release status, and consent. Use the approved
   Facebook/Meta connector or Graph API; upload the image as the post image and retain the returned post ID in a
   private operator record, never in the public Book.
6. Record only sanitized publication provenance in the Book or integration `PLANS.md`: command, snapshot, public URL,
   destination Page name, date, and post URL/ID if the user authorizes it.

## Output contract

The package is a directory containing:

- `facebook-post.json` — deterministic post metadata and caption;
- the copied GUI snapshot image;
- `README.md` — review note stating the evidence and whether external publishing occurred.

The package is not proof of posting. Only the external platform's returned post record proves publication.
