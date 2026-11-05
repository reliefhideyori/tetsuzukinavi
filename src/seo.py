"""site/ に canonical・hreflang・noindex と sitemap.xml・robots.txt を付ける（package.py の後に実行）。"""
import re, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
BASE = "https://tetsuzukinavi.org"
NOINDEX = {"contact", "thanks"}
def url(lang, slug): return f"{BASE}/{lang}/" if slug == "index" else f"{BASE}/{lang}/{slug}"
urls = []
for p in sorted(ROOT.glob("*/*.html")):
    lang, slug = p.parent.name, p.stem
    other = "id" if lang == "ja" else "ja"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r'<link rel="(alternate|canonical)"[^>]*>\n?', "", s)
    s = re.sub(r'<meta name="robots"[^>]*>\n?', "", s)
    tags = [f'<link rel="canonical" href="{url(lang, slug)}">']
    if (ROOT / other / p.name).exists():
        tags += [f'<link rel="alternate" hreflang="{lang}" href="{url(lang, slug)}">',
                 f'<link rel="alternate" hreflang="{other}" href="{url(other, slug)}">']
    if slug in NOINDEX: tags.append('<meta name="robots" content="noindex">')
    else: urls.append(url(lang, slug))
    s = s.replace("</head>", "\n".join(tags) + "\n</head>", 1)
    p.write_text(s, encoding="utf-8")
today = datetime.date.today().isoformat()
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"<url><loc>{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
print(len(urls), "urls")
