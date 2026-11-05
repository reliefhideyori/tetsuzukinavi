"""Render a page_<slug>.py straight into ../site/{ja,id}/<slug>.html (site-native version of build_pages + package).
Usage: python3 addpage.py nenkin   then: python3 finish.py && python3 seo.py"""
import sys, os, re, json, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); SITE = os.path.join(D, "..", "site")
sys.path.insert(0, D); import build_pages as bp
slug = sys.argv[1]
spec = importlib.util.spec_from_file_location("pg", os.path.join(D, f"page_{slug}.py")); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
L = json.load(open(os.path.join(D, "links.json")))
for lang in ("ja", "id"):
    h = bp.render(m.PAGE, lang)
    for key, mm in L.items():
        for lg, u in mm.items():
            h = h.replace(u, "/ja/shinjuku-juminzei" if key == "juminzei" else f"/{lg}/{key}")
    for lg, u in bp.ABOUT.items(): h = h.replace(u, f"/{lg}/about")
    h = h.replace('<a class="lang" href="#">', '<a class="lang" href="#" hreflang="x">', 1)
    h = h.replace('<a class="brand" href="#">', f'<a class="brand" href="/{lang}/">', 1)
    h = re.sub(r'(<nav class="crumb"[^>]*><ol><li>)<a href="#">', rf'\1<a href="/{lang}/">', h, count=1)
    h = re.sub(r'(<nav class="crumb"[^>]*><ol><li><a href="/{lang}/">[^<]*</a></li><li>)<a href="#">([^<]*)</a>', r'\1\2', h, count=1)
    h = h.replace('<a class="btn" href="#">', f'<a class="btn" href="/{lang}/contact?page={slug}">')
    open(os.path.join(SITE, lang, f"{slug}.html"), "w", encoding="utf-8").write(h)
print("added", slug)
