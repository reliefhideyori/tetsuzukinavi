"""Package pages into dist/ for Cloudflare Pages: /ja/*.html, /id/*.html, root redirect to /id/."""
import os, re, json, shutil
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(D, "dist")
shutil.rmtree(OUT, ignore_errors=True)
L = json.load(open(os.path.join(D, "links.json")))
L["about"] = {"ja": "https://claude.ai/artifact/2tPzvnjGiCfbMEjD61wUWS", "id": "https://claude.ai/artifact/Bc82QWebd8N6QCPFHtGBHe"}
SLUGS = ["gaji", "lpk", "visa", "test", "arrival", "about"]
url2path = {}
for slug, m in L.items():
    for lang, u in m.items():
        if slug == "juminzei": url2path[u] = "/ja/shinjuku-juminzei.html"
        else: url2path.setdefault(u, f"/{lang}/{slug}.html")
TITLES = {}
for lang in ("ja", "id"):
    os.makedirs(os.path.join(OUT, lang), exist_ok=True)
    other = "id" if lang == "ja" else "ja"
    for slug in SLUGS:
        h = open(os.path.join(D, f"{slug}-{lang}.html"), encoding="utf-8").read()
        for u, p in url2path.items(): h = h.replace(u, p)
        h = h.replace('<a class="lang" href="#">', f'<a class="lang" href="/{other}/{slug}.html" hreflang="{other}">', 1)
        h = h.replace('<a class="brand" href="#">', f'<a class="brand" href="/{lang}/">', 1)
        h = re.sub(r'(<nav class="crumb"[^>]*><ol><li>)<a href="#">', rf'\1<a href="/{lang}/">', h, count=1)
        h = h.replace('<head>', f'<head>\n<link rel="alternate" hreflang="{other}" href="https://tetsuzukinavi.org/{other}/{slug}.html">', 1)
        TITLES[(lang, slug)] = re.search(r"<h1>(.*?)</h1>", h).group(1)
        open(os.path.join(OUT, lang, f"{slug}.html"), "w", encoding="utf-8").write(h)
jm = os.path.join(D, "..", "shinjuku-juminzei-ja.html")
if os.path.exists(jm): shutil.copy(jm, os.path.join(OUT, "ja", "shinjuku-juminzei.html"))
# simple index per language, built from the about page shell
for lang in ("ja", "id"):
    shell = open(os.path.join(OUT, lang, "about.html"), encoding="utf-8").read()
    head, _ = shell.split('<main class="wrap">', 1)
    foot = shell[shell.index("<footer>"):]
    intro = {"ja": ("手続きナビ", "日本で働く前に知っておきたいことを、公式の情報だけでまとめています。"),
             "id": ("Tetsuzuki Navi", "Informasi yang perlu diketahui sebelum bekerja di Jepang, hanya dari sumber resmi.")}[lang]
    items = "".join(f'<a href="/{lang}/{s}.html">{TITLES[(lang, s)]}</a>' for s in SLUGS if s != "about")
    body = f'<main class="wrap"><h1>{intro[0]}</h1><p class="lead">{intro[1]}</p><div class="related" style="margin-top:24px">{items}</div><style>.related a{{display:block;padding:14px 0;border-bottom:1px solid var(--line);font-weight:700}}</style></main>'
    open(os.path.join(OUT, lang, "index.html"), "w", encoding="utf-8").write(head + body + foot)
open(os.path.join(OUT, "index.html"), "w").write('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=/id/"><link rel="canonical" href="/id/"><title>Tetsuzuki Navi</title><a href="/id/">Bahasa Indonesia</a> / <a href="/ja/">日本語</a>')
print(sorted(os.listdir(os.path.join(OUT, "ja"))), sorted(os.listdir(os.path.join(OUT, "id"))))

# ---- contact form (FormSubmit: no server, sends to the site Gmail; first submission triggers an activation email) ----
FORM_ACTION = "/api/contact"
CT = {
 "ja": dict(h1="お問い合わせ・間違いの報告", lead="間違いや古い情報の報告、ご意見を受け付けます。どの言語でも大丈夫です。",
   note="個人のビザや契約の相談には答えられません。困ったときは、各ページの「相談先」にある公的な窓口に相談してください。",
   kind="種類", k=["間違いの報告", "ご意見", "その他"], page="どのページですか（任意）", msg="内容", mail="返信用メールアドレス（任意）",
   mail_note="返信が必要なときだけ入れてください。返信以外には使いません。", send="送信する", req="必須",
   thanks_h="送信しました", thanks="ありがとうございます。内容を確認し、公式の情報で確かめてから直します。", back="トップに戻る"),
 "id": dict(h1="Kontak dan Laporan Kesalahan", lead="Kami menerima laporan kesalahan, informasi yang sudah lama, dan saran. Bahasa apa pun boleh.",
   note="Kami tidak bisa menjawab konsultasi pribadi soal visa atau kontrak. Jika ada masalah, hubungi layanan resmi di bagian \"Tempat konsultasi\" di setiap halaman.",
   kind="Jenis", k=["Laporan kesalahan", "Saran", "Lainnya"], page="Halaman mana? (opsional)", msg="Isi pesan", mail="Email untuk balasan (opsional)",
   mail_note="Isi hanya jika perlu dibalas. Tidak dipakai untuk hal lain.", send="Kirim", req="wajib",
   thanks_h="Pesan terkirim", thanks="Terima kasih. Kami akan membaca pesan Anda dan mencocokkannya dengan informasi resmi sebelum memperbaiki halaman.", back="Kembali ke beranda"),
}
FORM_CSS = "<style>.cform label{display:block;font-weight:700;margin:0 0 4px}.cform .f{margin-bottom:24px}.cform input[type=text],.cform input[type=email],.cform textarea{width:100%;min-height:48px;padding:8px 12px;border:1px solid var(--line-strong);border-radius:8px;background:var(--bg);font:inherit;color:inherit}.cform textarea{min-height:160px}.cform .opt{display:flex;align-items:center;gap:8px;min-height:44px;font-weight:400}.cform .opt input{width:20px;height:20px}.cform .req{font-size:12px;color:var(--error);margin-left:6px;font-weight:700}.cform button{min-height:48px;padding:0 32px;border-radius:8px;border:0;background:var(--key);color:var(--key-fg);font-weight:700;font:inherit;font-weight:700}.hp{position:absolute;left:-9999px}</style>"
for lang in ("ja", "id"):
    c = CT[lang]
    shell = open(os.path.join(OUT, lang, "about.html"), encoding="utf-8").read()
    head, _ = shell.split('<main class="wrap">', 1)
    foot = shell[shell.index("<footer>"):]
    head = head.replace("</head>", FORM_CSS + "</head>", 1)
    radios = "".join(f'<label class="opt"><input type="radio" name="kind" value="{v}" required{" checked" if i == 0 else ""}> {v}</label>' for i, v in enumerate(c["k"]))
    form = f'''<main class="wrap"><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p><div class="notice"><p>{c["note"]}</p></div>
<form class="cform" action="{FORM_ACTION}" method="POST">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<input type="hidden" name="lang" value="{lang}">
<fieldset class="f"><legend style="font-weight:700">{c["kind"]}<span class="req">{c["req"]}</span></legend>{radios}</fieldset>
<div class="f"><label for="page">{c["page"]}</label><input type="text" id="page" name="page"></div>
<div class="f"><label for="msg">{c["msg"]}<span class="req">{c["req"]}</span></label><textarea id="msg" name="message" required></textarea></div>
<div class="f"><label for="mail">{c["mail"]}</label><p class="small" style="margin:0 0 8px">{c["mail_note"]}</p><input type="email" id="mail" name="email" autocomplete="email"></div>
<button type="submit">{c["send"]}</button></form>
<script>document.getElementById("page").value = new URLSearchParams(location.search).get("page") || "";</script></main>'''
    open(os.path.join(OUT, lang, "contact.html"), "w", encoding="utf-8").write(head + form + foot)
    thanks = f'<main class="wrap"><h1>{c["thanks_h"]}</h1><p>{c["thanks"]}</p><a class="btn" href="/{lang}/">{c["back"]}</a></main>'
    open(os.path.join(OUT, lang, "thanks.html"), "w", encoding="utf-8").write(head + thanks + foot)
    # wire every "report an error" button and footer link to the contact page, passing the page name
    for f in os.listdir(os.path.join(OUT, lang)):
        if f in ("contact.html", "thanks.html") or not f.endswith(".html"): continue
        p = os.path.join(OUT, lang, f); h = open(p, encoding="utf-8").read()
        h = h.replace('<a class="btn" href="#">', f'<a class="btn" href="/{lang}/contact.html?page={f}">')
        h = re.sub(r'<li><a href="#">([^<]*)</a></li>', rf'<li><a href="/{lang}/contact.html?page={f}">\1</a></li>', h)
        open(p, "w", encoding="utf-8").write(h)
print("contact pages done")
for lang, old, new in [("ja", "（公開時に連絡フォームを設置します）", '<a class="btn" href="/ja/contact.html?page=about.html">お問い合わせフォーム</a>'),
                       ("id", "(Formulir kontak akan dipasang saat situs dibuka)", '<a class="btn" href="/id/contact.html?page=about.html">Formulir kontak</a>')]:
    p = os.path.join(OUT, lang, "about.html"); h = open(p, encoding="utf-8").read()
    h = h.replace(f'<p class="small">{old}</p>', new).replace(old, new)
    open(p, "w", encoding="utf-8").write(h)
