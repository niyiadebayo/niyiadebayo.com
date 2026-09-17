#!/usr/bin/env python3
"""Page templating for niyiadebayo.com.

The site is hand-maintained static HTML with no framework and no client JS, and
that does not change here: this renders plain HTML files that are committed to
the repo and served by GitHub Pages exactly as before. The only thing it removes
is having to edit the same <head>, nav and analytics block in 24 files by hand.

The contract is round-tripping. `extract()` parses an existing page into a dict
of its variable fields plus its body; `render()` builds the page back from them.
`python3 build.py --check` asserts render(extract(page)) == page, byte for byte,
for every essay on the site. If that passes, the template provably represents
the site as it stands, and new pages built from it will match.

    python3 build.py --check          verify round-trip over all essays
    python3 build.py --show <file>    print the fields extracted from one page
"""
import re
import sys
import glob
import json

SITE = "https://niyiadebayo.com"
BEACON = "769bf8adc2c4487188b82059b27f0419"


def _find(pattern, text, default=None, flags=0):
    m = re.search(pattern, text, flags)
    return m.group(1) if m else default


def extract(html):
    """Parse a rendered essay page into its variable fields plus body."""
    head = html.split("</head>")[0]
    ld = json.loads(_find(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>',
                          html, "{}", re.S))
    # body begins after the <h1>, which render() emits separately
    body_start = html.index("</h1>") + len("</h1>")
    if html[body_start] == "\n":
        body_start += 1
    body_end = html.index('      <div class="share">')
    prev = re.search(r'<a class="prev" href="([^"]+)"><span class="lbl">Previous</span>'
                     r'<span class="ttl">(.*?)</span></a>', html)
    nxt = re.search(r'<a class="next" href="([^"]+)"><span class="lbl">Next</span>'
                    r'<span class="ttl">(.*?)</span></a>', html)
    return {
        "slug": _find(r'<link rel="canonical" href="' + SITE + r'/([^"]+)">', head),
        "title": _find(r"<title>(.*?) &mdash; Adeniyi Adebayo</title>", head)
                 or _find(r"<title>(.*?) — Adeniyi Adebayo</title>", head),
        "description": _find(r'<meta name="description" content="([^"]*)">', head),
        "og_title": _find(r'<meta property="og:title" content="([^"]*)">', head),
        "og_description": _find(r'<meta property="og:description" content="([^"]*)">', head),
        "og_image": _find(r'<meta property="og:image" content="([^"]*)">', head),
        "og_image_alt": _find(r'<meta property="og:image:alt" content="([^"]*)">', head),
        "twitter_card": _find(r'<meta name="twitter:card" content="([^"]*)">', head),
        "twitter_title": _find(r'<meta name="twitter:title" content="([^"]*)">', head),
        "twitter_description": _find(r'<meta name="twitter:description" content="([^"]*)">', head),
        "date": ld.get("datePublished"),
        "ld_headline": ld.get("headline"),
        "ld_description": ld.get("description"),
        "crumb": _find(r'<span class="crumb">(.*?)</span>', html),
        "h1": _find(r"<h1>(.*?)</h1>", html),
        "share_text": _find(r"&text=([^\"]*)\"", html),
        "prev": (prev.group(1), prev.group(2)) if prev else None,
        "next": (nxt.group(1), nxt.group(2)) if nxt else None,
        "body": html[body_start:body_end],
    }


def render(m):
    """Build a full page from extracted fields. Inverse of extract()."""
    url = f"{SITE}/{m['slug']}"
    alt = (f'\n  <meta property="og:image:alt" content="{m["og_image_alt"]}">'
           if m.get("og_image_alt") else "")
    nav = ""
    if m["prev"] or m["next"]:
        rows = []
        if m["prev"]:
            rows.append(f'        <a class="prev" href="{m["prev"][0]}">'
                        f'<span class="lbl">Previous</span>'
                        f'<span class="ttl">{m["prev"][1]}</span></a>')
        if m["next"]:
            rows.append(f'        <a class="next" href="{m["next"][0]}">'
                        f'<span class="lbl">Next</span>'
                        f'<span class="ttl">{m["next"][1]}</span></a>')
        nav = '      <nav class="arc-nav">\n' + "\n".join(rows) + "\n      </nav>\n"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{m['title']} — Adeniyi Adebayo</title>
  <meta name="description" content="{m['description']}">
  <meta name="color-scheme" content="dark light">
  <link rel="canonical" href="{url}">
  <meta property="og:title" content="{m['og_title']}">
  <meta property="og:description" content="{m['og_description']}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="article:author" content="{SITE}">
  <meta property="og:image" content="{m['og_image']}">{alt}
  <meta name="twitter:card" content="{m['twitter_card']}">
  <meta name="twitter:site" content="@niyiadebayo">
  <meta name="twitter:title" content="{m['twitter_title']}">
  <meta name="twitter:description" content="{m['twitter_description']}">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{m['ld_headline']}",
    "author": {{"@type": "Person", "name": "Adeniyi Adebayo", "url": "{SITE}"}},
    "url": "{url}",
    "datePublished": "{m['date']}",
    "description": "{m['ld_description']}"
  }}
  </script>
  <link rel="icon" href="/favicon.ico" sizes="16x16 32x32 48x48">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="alternate" type="application/rss+xml" title="Adeniyi Adebayo" href="/feed.xml">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <p class="back"><a href="/">&larr; Home</a><span class="crumb">{m['crumb']}</span></p>
    <article>
      <h1>{m['h1']}</h1>
{m['body']}      <div class="share">
        <a href="https://x.com/intent/tweet?url={url}&text={m['share_text']}" target="_blank" rel="noopener">Share on X</a>
        <a href="https://www.linkedin.com/sharing/share-offsite/?url={url}" target="_blank" rel="noopener">Share on LinkedIn</a>
        <button onclick="navigator.clipboard.writeText('{url}');this.textContent='Copied';setTimeout(()=>this.textContent='Copy link',2000)">Copy link</button>
      </div>
{nav}    </article>
  </main>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "{BEACON}"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""


def check():
    """render(extract(page)) must equal page exactly, for every essay."""
    files = sorted(f for f in glob.glob("*.html") if f not in ("index.html", "404.html"))
    bad = []
    for f in files:
        original = open(f).read()
        try:
            out = render(extract(original))
        except Exception as exc:                      # noqa: BLE001
            bad.append((f, f"{type(exc).__name__}: {exc}"))
            continue
        if out != original:
            a, b = original.split("\n"), out.split("\n")
            diff = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
            bad.append((f, f"line {diff + 1}\n      was: {a[diff][:100] if diff < len(a) else '<eof>'}"
                           f"\n      got: {b[diff][:100] if diff < len(b) else '<eof>'}"))
    for f, why in bad:
        print(f"  MISMATCH {f}: {why}")
    print(f"\n  {len(files) - len(bad)}/{len(files)} essays round-trip byte-identical")
    return 1 if bad else 0


if __name__ == "__main__":
    if "--check" in sys.argv:
        sys.exit(check())
    if "--show" in sys.argv:
        target = sys.argv[sys.argv.index("--show") + 1]
        data = extract(open(target).read())
        data["body"] = f"<{len(data['body'])} chars>"
        print(json.dumps(data, indent=2))
        sys.exit(0)
    print(__doc__)
