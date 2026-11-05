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

# 2) 404 (both languages on one page)
nf = put_main(shell("id"), '<main class="wrap"><h1>Halaman tidak ditemukan</h1><p>Halaman ini tidak ada atau sudah dipindahkan.</p>'
    '<p><a class="btn" href="/id/">Ke halaman utama (Bahasa Indonesia)</a></p><h2 lang="ja">ページが見つかりません</h2>'
    '<p lang="ja">このページはないか、移動しました。</p><p><a class="btn" href="/ja/">トップへ（日本語）</a></p></main>')
nf = re.sub(r"<title>[^<]*</title>", "<title>404 | Tetsuzuki Navi</title>", nf)
(ROOT / "404.html").write_text(nf, encoding="utf-8")

# 3) every page: title, description, language toggle, footer
for p in sorted(ROOT.glob("*/*.html")):
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
    o = OTHER[lang]
    target = f"/{o}/" if slug == "index" else (f"/{o}/{slug}" if (ROOT / o / p.name).exists() else f"/{o}/")
    s = re.sub(r'(<a class="lang" href=")[^"]*"', rf'\g<1>{target}"', s, count=1)
    items = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in FOOT[lang])
    s = re.sub(r"<footer>.*?</footer>", f'<footer><div class="wrap"><ul>{items}<li>© 2026 {SITE[lang]}</li></ul></div></footer>', s, count=1, flags=re.S)
    p.write_text(s, encoding="utf-8")
print("ok")
