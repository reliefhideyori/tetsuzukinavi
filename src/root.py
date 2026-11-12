"""トップ https://tetsuzukinavi.org/ を、リダイレクトではなく中身のある2言語の入口ページにする。
（以前は meta refresh で /id/ に飛ばしていたため、Search Console で「ページにリダイレクトがあります」になり、
AdSense の審査でもトップに中身がないと見られていた。）seo.py の最後から呼ばれる。"""
import re, pathlib
import home
ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
BASE = "https://tetsuzukinavi.org"
TITLE = "Tetsuzuki Navi（手続きナビ）| Informasi resmi sebelum bekerja di Jepang"
CSS = """<style>
.langs{display:grid;gap:var(--s2);margin:var(--s3) 0 var(--s6)}
.langs a{display:block;border:2px solid var(--key);border-radius:8px;padding:var(--s3);text-decoration:none;color:var(--fg)}
.langs a b{display:block;font-size:19px;color:var(--key);margin-bottom:var(--s1)}.langs a span{font-size:14px;color:var(--fg-sub)}
.idx h3{font-size:15px;color:var(--key);margin:var(--s3) 0 var(--s1)}
.idx ul{list-style:none;padding:0;margin:0}.idx li{border-bottom:1px solid var(--line)}
.idx li a{display:block;padding:10px 0;font-weight:700;text-decoration:none}
.idx li span{display:block;font-size:13px;color:var(--fg-sub);font-weight:400}
@media(min-width:720px){.langs{grid-template-columns:1fr 1fr}}
</style></head>"""

def index(lang):
    c = home.C[lang]
    return "".join(f'<h3>{st}</h3><ul>' + "".join(f'<li><a href="/{lang}/{s}">{t}<span>{d}</span></a></li>' for s, t, d in items) + '</ul>'
                   for st, items in c["stages"])

def trust(lang):
    c = home.C[lang]
    return f'<h3>{c["trust_h"]}</h3><ul>' + "".join(f'<li><a href="/{lang}/about">{h}<span>{p}</span></a></li>' for h, p in c["trust"]) + '</ul>'

def build():
    s = (ROOT / "id" / "index.html").read_text(encoding="utf-8")
    i, j = home.C["id"], home.C["ja"]
    main = (f'<main class="wrap"><div class="hero"><h1>Tetsuzuki Navi <span lang="ja">（手続きナビ）</span></h1>'
            f'<p class="lead">{i["lead"]}</p><p class="lead" lang="ja">{j["lead"]}</p></div>'
            f'<div class="langs"><a href="/id/" hreflang="id"><b>Bahasa Indonesia</b><span>{i["h1"]}</span></a>'
            f'<a href="/ja/" hreflang="ja" lang="ja"><b>日本語</b><span>{j["h1"]}</span></a></div>'
            f'<section class="idx"><h2>{i["road_h"]}</h2>{index("id")}{trust("id")}</section>'
            f'<section class="idx" lang="ja"><h2>{j["road_h"]}</h2>{index("ja")}{trust("ja")}</section></main>')
    s = re.sub(r"<main.*?</main>", lambda m: main, s, count=1, flags=re.S)
    s = s.replace("</head>", CSS, 1)
    s = re.sub(r"<title>[^<]*</title>", f"<title>{TITLE}</title>", s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*"', rf'\g<1>{TITLE}"', s, count=1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*"', rf'\g<1>{BASE}/"', s, count=1)
    s = re.sub(r'<link rel="(alternate|canonical)"[^>]*>\n?', "", s)
    s = s.replace("</head>", f'<link rel="canonical" href="{BASE}/">\n<link rel="alternate" hreflang="x-default" href="{BASE}/">\n'
                  f'<link rel="alternate" hreflang="id" href="{BASE}/id/">\n<link rel="alternate" hreflang="ja" href="{BASE}/ja/">\n</head>', 1)
    s = re.sub(r'<a class="brand" href="/id/">', '<a class="brand" href="/">', s, count=1)
    (ROOT / "index.html").write_text(s, encoding="utf-8")

if __name__ == "__main__":
    build(); print("root ok")
