"""site/ の仕上げ：プライバシーポリシーと404ページを作り、全ページのタイトル・説明文・言語切替・フッターをそろえる。
順番: package.py → finish.py → seo.py"""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent / "site"
SITE = {"ja": "手続きナビ", "id": "Tetsuzuki Navi"}
OTHER = {"ja": "id", "id": "ja"}
FOOT = {
 "ja": [("/ja/about", "運営者と方針"), ("/ja/privacy", "プライバシーポリシー"), ("/ja/contact", "お問い合わせ・間違いの報告")],
 "id": [("/id/about", "Pengelola dan Kebijakan"), ("/id/privacy", "Kebijakan Privasi"), ("/id/contact", "Kontak dan laporan kesalahan")],
}
TITLES = {  # 自動の見出しが合わないページだけ
 ("ja", "index"): "手続きナビ｜日本で働く前に知っておきたい公式情報",
 ("id", "index"): "Tetsuzuki Navi | Informasi resmi sebelum bekerja di Jepang",
 ("ja", "contact"): "お問い合わせ・間違いの報告", ("id", "contact"): "Kontak dan Laporan Kesalahan",
 ("ja", "thanks"): "送信しました", ("id", "thanks"): "Pesan terkirim",
}
PRIVACY = {
"ja": ("プライバシーポリシー", "このサイトが集める情報と、その使い方です。", [
 ("集める情報", "<p>このサイトは会員登録がなく、名前や住所を入力する場所はありません。集めるのは、お問い合わせフォームに書かれた内容と、任意で書かれた返信用のメールアドレスだけです。</p>"),
 ("情報の使い方", "<p>お問い合わせの内容は、返信と、ページの間違いを直すためだけに使います。法律で求められた場合を除き、ほかの人や会社に渡しません。</p>"),
 ("広告について", "<p>このサイトは、Google AdSense などの広告で運営費をまかないます（準備中を含みます）。Google などの広告配信事業者は、Cookie を使って、このサイトやほかのサイトへの過去のアクセスにもとづいた広告を表示することがあります。</p><p>あなたに合わせた広告（パーソナライズ広告）は、<a href='https://adssettings.google.com/'>Google の広告設定</a>で止められます。Google による Cookie の使い方は<a href='https://policies.google.com/technologies/ads?hl=ja'>Google のポリシーと規約</a>で確認できます。</p><p>LPK・仲介業者・借金（ローン）の広告は表示しないように設定します。</p>"),
 ("アクセスの記録", "<p>サイトは Cloudflare で配信しています。安全に配信するため、Cloudflare が IP アドレスなどの技術的な記録を扱います。今のところ、アクセス解析ツールは使っていません。使い始めるときは、このページに書きます。</p>"),
 ("このページの変更", "<p>内容を変えたときは、このページを更新し、下の変更履歴に書きます。</p>"),
], "2026年11月6日　公開"),
"id": ("Kebijakan Privasi", "Informasi apa yang dikumpulkan situs ini dan bagaimana digunakan.", [
 ("Informasi yang dikumpulkan", "<p>Situs ini tidak punya pendaftaran anggota dan tidak meminta nama atau alamat. Yang dikumpulkan hanya isi formulir kontak dan alamat email untuk balasan jika Anda menuliskannya.</p>"),
 ("Cara penggunaan", "<p>Isi pesan hanya dipakai untuk membalas dan memperbaiki kesalahan di halaman. Kami tidak memberikannya kepada orang atau perusahaan lain, kecuali jika diwajibkan oleh hukum.</p>"),
 ("Tentang iklan", "<p>Biaya situs ini ditanggung dari iklan seperti Google AdSense (termasuk yang sedang disiapkan). Penyedia iklan seperti Google dapat memakai cookie untuk menampilkan iklan berdasarkan kunjungan Anda sebelumnya ke situs ini atau situs lain.</p><p>Iklan yang disesuaikan untuk Anda (iklan yang dipersonalisasi) bisa dimatikan di <a href='https://adssettings.google.com/'>Setelan Iklan Google</a>. Cara Google memakai cookie bisa dibaca di <a href='https://policies.google.com/technologies/ads?hl=id'>Kebijakan dan Persyaratan Google</a>.</p><p>Iklan LPK, agen, dan pinjaman diatur agar tidak tampil.</p>"),
 ("Catatan akses", "<p>Situs ini dikirim lewat Cloudflare. Agar aman, Cloudflare memproses catatan teknis seperti alamat IP. Saat ini kami tidak memakai alat analisis akses. Jika mulai memakainya, akan kami tulis di halaman ini.</p>"),
 ("Perubahan halaman ini", "<p>Jika isinya berubah, halaman ini diperbarui dan dicatat di riwayat perubahan di bawah.</p>"),
], "6 November 2026  Diterbitkan"),
}
LOG_H = {"ja": "変更履歴", "id": "Riwayat perubahan"}

def shell(lang):  # thanks.html を外枠として使う
    return (ROOT / lang / "thanks.html").read_text(encoding="utf-8")

def put_main(s, main): return re.sub(r"<main.*?</main>", main, s, count=1, flags=re.S)

# 1) privacy pages
for lang, (h1, lead, secs, log) in PRIVACY.items():
    body = "".join(f"<section><h2>{h}</h2>{b}</section>" for h, b in secs)
    main = (f'<main class="wrap"><nav class="crumb" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{SITE[lang]}</a></li><li>{h1}</li></ol></nav>'
            f'<h1>{h1}</h1><p class="lead">{lead}</p>{body}<aside class="trust"><h3>{LOG_H[lang]}</h3><ul><li>{log}</li></ul></aside></main>')
    (ROOT / lang / "privacy.html").write_text(put_main(shell(lang), main), encoding="utf-8")

# 1b) 住民税ページ（古い断片）をサイトの外枠に入れる
jp = ROOT / "ja" / "shinjuku-juminzei.html"
js = jp.read_text(encoding="utf-8")
if "</head>" not in js:
    body = js.split("</style>", 1)[1]
    main = body[body.index("<main"):body.index("</main>") + 7].replace("<main>", '<main class="wrap">', 1)
    main = main.replace("<ol><li>手続きナビ</li>", '<ol><li><a href="/ja/">手続きナビ</a></li>', 1)
    script = body[body.index("</main>") + 7:]
    out = put_main(shell("ja"), main)
    out = out.replace("</body>", script.strip() + "\n</body>", 1)
    out = re.sub(r'<meta name="robots"[^>]*>\n?', "", out)
    jp.write_text(out, encoding="utf-8")

# 2) 404 (both languages on one page)
nf = put_main(shell("id"), '<main class="wrap"><h1>Halaman tidak ditemukan</h1><p>Halaman ini tidak ada atau sudah dipindahkan.</p>'
    '<p><a class="btn" href="/id/">Ke halaman utama (Bahasa Indonesia)</a></p><h2 lang="ja">ページが見つかりません</h2>'
    '<p lang="ja">このページはないか、移動しました。</p><p><a class="btn" href="/ja/">トップへ（日本語）</a></p></main>')
nf = re.sub(r"<title>[^<]*</title>", "<title>404 | Tetsuzuki Navi</title>", nf)
(ROOT / "404.html").write_text(nf, encoding="utf-8")

# 2b) home page (src/home.py)
import home
for lang in ("ja", "id"):
    p = ROOT / lang / "index.html"; s = p.read_text(encoding="utf-8")
    s = put_main(s, home.main(lang))
    p.write_text(s, encoding="utf-8")

SHARE = {"ja": ("このページを共有する", "リンクをコピー", "コピーしました"), "id": ("Bagikan halaman ini", "Salin link", "Link disalin")}
CONTENT = {"gaji", "lpk", "visa", "test", "arrival", "nenkin", "shinjuku-juminzei"}
SHARE_CSS = "<style>.share{margin:var(--s3) 0}.share h2{font-size:16px;margin:0 0 var(--s1)}.share div{display:flex;flex-wrap:wrap;gap:var(--s1)}.share a,.share button{display:inline-flex;align-items:center;min-height:44px;padding:0 var(--s2);border:1px solid var(--line-strong);border-radius:8px;background:var(--bg);color:var(--fg);font-weight:700;text-decoration:none;font-size:14px;cursor:pointer}</style></head>"

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#18794e"/>'
        '<path d="M10 23v-5.5a3.5 3.5 0 0 1 3.5-3.5h5a3.5 3.5 0 0 0 3.5-3.5V9" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>'
        '<circle cx="10" cy="23" r="2.6" fill="#fff"/><path d="M18.5 9.5 22 6l3.5 3.5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CSS_V = "7"
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9784894740329526" crossorigin="anonymous"></script>'

# 3) every page: title, description, language toggle, footer
for p in [q for q in sorted(ROOT.glob("*/*.html")) if "</head>" in q.read_text(encoding="utf-8")]:
    lang, slug = p.parent.name, p.stem
    s = p.read_text(encoding="utf-8")
    h1 = re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", s, re.S).group(1)).strip()
    title = TITLES.get((lang, slug)) or f"{h1} | {SITE[lang]}"
    s = re.sub(r"<title>[^<]*</title>", f"<title>{title}</title>", s, count=1)
    m = re.search(r'<p class="lead">(.*?)</p>', s, re.S)
    s = re.sub(r'<meta name="description"[^>]*>\n?', "", s)
    if m:
        desc = re.sub(r"<[^>]+>", "", m.group(1)).replace('"', "&quot;").strip()
        s = s.replace("</title>", f'</title>\n<meta name="description" content="{desc}">', 1)
    s = re.sub(r'(<nav class="crumb".*?</nav>)', lambda m: re.sub(r'<li><a href="(#|[^"]*contact[^"]*)">([^<]*)</a></li>', r'<li>\2</li>', m.group(1)), s, count=1, flags=re.S)
    head, rest = s.split("</head>", 1)
    head = re.sub(r"<style>.*?</style>\n?", "", head, flags=re.S)
    head = re.sub(r'<link rel="stylesheet" href="/assets/site.css[^>]*>\n?', "", head)
    head = re.sub(r'<script async src="https://pagead2[^>]*></script>\n?', "", head)
    s = head + f'<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">\n{ADSENSE}\n</head>' + rest
    s = re.sub(r'(<a class="brand"[^>]*>)\s*<svg.*?</svg>', lambda mm: mm.group(1) + LOGO, s, count=1, flags=re.S)
    o = OTHER[lang]
    target = f"/{o}/" if slug == "index" else (f"/{o}/{slug}" if (ROOT / o / p.name).exists() else f"/{o}/")
    s = re.sub(r'(<a class="lang" href=")[^"]*"', rf'\g<1>{target}"', s, count=1)
    items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in FOOT[lang])
    s = re.sub(r"<footer>.*?</footer>", f'<footer><div class="wrap"><ul>{items}<li>© 2026 {SITE[lang]}</li></ul></div></footer>', s, count=1, flags=re.S)
    u = f"https://tetsuzukinavi.org/{lang}/" + ("" if slug == "index" else slug)
    s = re.sub(r'<link rel="icon"[^>]*>\n?|<meta property="og:[^>]*>\n?|<meta name="twitter:[^>]*>\n?', "", s)
    og = [f'<link rel="icon" href="/favicon.svg" type="image/svg+xml">', f'<meta property="og:type" content="website">',
          f'<meta property="og:site_name" content="{SITE[lang]}">', f'<meta property="og:title" content="{title}">',
          f'<meta property="og:url" content="{u}">', f'<meta property="og:image" content="https://tetsuzukinavi.org/img/og-{lang}.png">',
          f'<meta property="og:locale" content="{"ja_JP" if lang == "ja" else "id_ID"}">', '<meta name="twitter:card" content="summary_large_image">']
    if m: og.insert(4, f'<meta property="og:description" content="{desc}">')
    s = s.replace("</title>", "</title>\n" + "\n".join(og), 1)
    if slug in CONTENT and 'class="share"' not in s:
        from urllib.parse import quote
        h, c1, c2 = SHARE[lang]; q = quote(f"{title}\n{u}")
        box = (f'<div class="share"><h2>{h}</h2><div><a href="https://wa.me/?text={q}" rel="noopener" target="_blank">WhatsApp</a>'
               f'<a href="https://www.facebook.com/sharer/sharer.php?u={quote(u)}" rel="noopener" target="_blank">Facebook</a>'
               f'<button type="button" onclick="navigator.clipboard.writeText(\'{u}\').then(()=>{{this.textContent=\'{c2}\'}})">{c1}</button></div></div>')
        s = re.sub(r'(<aside class="trust")', lambda mm: box + mm.group(1), s, count=1)
    p.write_text(s, encoding="utf-8")
print("ok")
