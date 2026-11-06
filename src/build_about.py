"""Builds the 'about & policy' page (ja, id) reusing the calculator page's header and CSS."""
import re, os
D = os.path.dirname(__file__)
tpl = open(os.path.join(D, "template.html"), encoding="utf-8").read()
head = tpl.split("<main")[0]          # doctype .. badges
style_ok = "<footer>" in tpl

C = {
"ja": dict(
 title="運営者と方針", h1="運営者と方針",
 lead="このサイトを誰が、なぜ、どうやって作っているか。どう収入を得ているか。",
 sections=[
  ("運営者からのメッセージ", "<p>日々の暮らしや仕事の中で、海外から来た方と関わる機会があります。私自身も役所で手続きをすることが多く、そのたびに「この難しくて複雑な手続きを、外国から来た人はどうやってこなしているのだろう」と気になっていました。それが、このサイトを始めたきっかけです。</p><p>日本の仕組みや本当の情報は、実際に来てみないと分からないことがたくさんあります。だからこそ、日本に来る前の方には、怪しいサイトではなく、中立で正確な情報から選んでほしいと思っています。</p><p>読んでほしいのは、日本に行くことに不安を抱えている人です。このサイトを読んで、日本での暮らしや仕事のイメージが少しでも湧いたらうれしいです。このサイトだけで全部が解決しなくても、困ったときにどこに相談すればいいかがはっきり分かる。そんな状態をつくれたら、とてもうれしく思います。</p><p style='text-align:right'>Hideyori Shiraki</p>"),
  ("このサイトの目的", "<p>日本で働きたい人が、来る前に<b>公式の正しい情報</b>を、自分の言葉で読めるようにすることです。この分野には、LPKや仲介業者に送り込むことで紹介料を得るサイトが多くあります。このサイトはそうしたお金を受け取らず、どの業者にも中立です。</p>"),
  ("誰が運営しているか", "<div class='prof'><div class='photo'><img src='PHOTO' alt='Hideyori Shiraki'></div><div><p class='pname'>Hideyori Shiraki</p><p class='small'>運営者</p></div></div><p>日本に住む Hideyori Shiraki が運営しています。文章の作成と翻訳にはAIを使い、すべての数字と制度の説明を、日本の省庁・自治体・公的機関の公式ページと照らし合わせています。</p>"),
  ("お金について", "<ul><li><b>収入は広告だけです。</b></li><li>LPK、仲介業者、送り出し機関、日本の会社から、紹介料や掲載料を受け取りません。</li><li>特定の業者を勧めたり、ランキングを作ったりしません。</li><li>LPK・仲介業者・借金（ローン）の広告は表示しないように設定しています。</li><li>メール登録、有料相談、LINEやWhatsAppへの誘導はありません。</li></ul>"),
  ("情報の正しさを守る方法", "<ol><li>すべての数字に、公式の出典と確認した日を書きます。出典のない数字は載せません。</li><li>毎週、出典の公式ページが変わっていないかを確認します。最低賃金や税金が変わる時期（4月・10月・12月など）は回数を増やします。</li><li>公式ページが変わったら、ページを直し、変更履歴に書きます。</li><li>読者から間違いの報告があれば、公式の情報で確かめてから直します。</li></ol>"),
  ("このサイトがしないこと", "<p>このサイトは一般的な情報を伝えるもので、あなた個人のビザ申請や契約について判断することはできません。個別の相談は、各ページの「困ったときの相談先」にある公的な窓口か、日本の行政書士・弁護士に相談してください。</p>"),
  ("間違いの報告・連絡先", "<p>間違いや古い情報を見つけたら教えてください。どの言語でも受け付けます。</p><p class=\"small\">（公開時に連絡フォームを設置します）</p>"),
 ],
 log="2026年11月5日　公開",
),
"id": dict(
 title="Pengelola dan Kebijakan", h1="Pengelola dan Kebijakan",
 lead="Siapa yang membuat situs ini, mengapa, dan bagaimana. Dari mana situs ini mendapat uang.",
 sections=[
  ("Pesan dari pengelola", "<p>Dalam kehidupan sehari-hari dan pekerjaan, saya sering bertemu dengan orang-orang yang datang dari luar negeri. Saya sendiri juga sering mengurus berbagai prosedur di kantor pemerintah. Setiap kali, saya bertanya-tanya: \"Bagaimana orang asing bisa menyelesaikan prosedur yang sulit dan rumit seperti ini?\" Itulah awal saya membuat situs ini.</p><p>Banyak hal tentang sistem Jepang dan keadaan yang sebenarnya baru bisa dipahami setelah tinggal di sini. Karena itu, saya ingin Anda yang akan berangkat ke Jepang mengambil keputusan berdasarkan informasi yang netral dan akurat, bukan dari situs yang mencurigakan.</p><p>Situs ini saya buat untuk Anda yang merasa cemas tentang berangkat ke Jepang. Saya akan senang jika situs ini bisa membantu Anda membayangkan kehidupan dan pekerjaan di Jepang, walaupun hanya sedikit. Walaupun tidak semua masalah bisa selesai di situs ini, saya ingin Anda setidaknya tahu dengan jelas ke mana harus bertanya saat mengalami kesulitan.</p><p style='text-align:right'>Hideyori Shiraki</p>"),
  ("Tujuan situs ini", "<p>Agar orang yang ingin bekerja di Jepang bisa membaca <b>informasi resmi yang benar</b> dalam bahasanya sendiri sebelum berangkat. Di bidang ini banyak situs yang mendapat komisi dengan mengirim pembaca ke LPK atau agen. Situs ini tidak menerima uang seperti itu dan netral terhadap semua lembaga.</p>"),
  ("Siapa pengelolanya", "<div class='prof'><div class='photo'><img src='PHOTO' alt='Hideyori Shiraki'></div><div><p class='pname'>Hideyori Shiraki</p><p class='small'>Pengelola</p></div></div><p>Situs ini dikelola oleh Hideyori Shiraki, yang tinggal di Jepang. Tulisan dan terjemahan dibuat dengan bantuan AI, dan semua angka serta penjelasan aturan dicocokkan dengan halaman resmi kementerian, pemerintah daerah, dan lembaga publik Jepang.</p>"),
  ("Tentang uang", "<ul><li><b>Pendapatan hanya dari iklan.</b></li><li>Kami tidak menerima komisi atau biaya pemasangan dari LPK, agen, lembaga pengirim (P3MI/SO), atau perusahaan Jepang.</li><li>Kami tidak merekomendasikan lembaga tertentu dan tidak membuat peringkat.</li><li>Iklan LPK, agen, dan pinjaman diatur agar tidak tampil.</li><li>Tidak ada pendaftaran email, konsultasi berbayar, atau ajakan ke LINE atau WhatsApp.</li></ul>"),
  ("Cara kami menjaga keakuratan informasi", "<ol><li>Setiap angka diberi sumber resmi dan tanggal dicek. Angka tanpa sumber tidak dimuat.</li><li>Setiap minggu kami mengecek apakah halaman resmi sumbernya berubah. Saat upah minimum atau pajak berubah (misalnya April, Oktober, Desember), pengecekan lebih sering.</li><li>Jika halaman resmi berubah, kami memperbaiki halaman dan mencatatnya di riwayat perubahan.</li><li>Jika pembaca melaporkan kesalahan, kami cek dengan informasi resmi lalu memperbaikinya.</li></ol>"),
  ("Yang tidak dilakukan situs ini", "<p>Situs ini memberi informasi umum dan tidak bisa menilai permohonan visa atau kontrak pribadi Anda. Untuk konsultasi pribadi, hubungi layanan resmi di bagian \"Tempat konsultasi\" di setiap halaman, atau gyoseishoshi (ahli administrasi) atau pengacara di Jepang.</p>"),
  ("Laporkan kesalahan / kontak", "<p>Jika menemukan informasi yang salah atau sudah lama, beri tahu kami. Bahasa apa pun diterima.</p><p class=\"small\">(Formulir kontak akan dipasang saat situs dibuka)</p>"),
 ],
 log="5 November 2026  Diterbitkan",
),
}
TXT = {"ja": {"html_lang":"ja","site":"手続きナビ","site_sub":"日本で暮らす・働くための公式情報ガイド","badge1":"公式の情報だけ","badge2":"毎週確認","badge3":"紹介料なし","tr_other_lang":"Bahasa Indonesia","font":"Noto+Sans+JP:wght@400;700","font_family":'"Noto Sans JP", "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif', "log_h":"変更履歴"},
       "id": {"html_lang":"id","site":"Tetsuzuki Navi","site_sub":"Panduan informasi resmi untuk tinggal dan bekerja di Jepang","badge1":"Hanya sumber resmi","badge2":"Dicek tiap minggu","badge3":"Tanpa komisi","tr_other_lang":"日本語","font":"Noto+Sans:wght@400;700","font_family":'"Noto Sans", "Segoe UI", Roboto, sans-serif', "log_h":"Riwayat perubahan"}}

CSS='<style>.prof{display:flex;align-items:center;gap:16px;margin-bottom:16px}.photo{width:88px;height:88px;border-radius:50%;background:var(--bg-sub);border:1px solid var(--line);display:grid;place-items:center;color:var(--fg-sub);font-size:14px;flex:none;overflow:hidden}.photo img{width:100%;height:100%;object-fit:cover}.pname{font-weight:700;font-size:18px;margin:0}</style></head>'
import base64
PHOTO_URI='data:image/jpeg;base64,'+base64.b64encode(open(os.path.join(D,'operator.jpg'),'rb').read()).decode()
for lang, c in C.items():
    tx = dict(TXT[lang]); tx["title"] = c["title"]
    h = re.sub(r"\{\{(\w+)\}\}", lambda m: tx[m.group(1)], head).replace("</head>", CSS, 1)
    body = [f'<main class="wrap">', f'<nav class="crumb" aria-label="breadcrumb"><ol><li><a href="#">{tx["site"]}</a></li><li>{c["title"]}</li></ol></nav>',
            f'<h1>{c["h1"]}</h1>', f'<p class="lead">{c["lead"]}</p>', '<p class="updated"></p>']
    for i, (hh, html) in enumerate(c["sections"]):
        cls = ' class="notice"' if i == 3 else ""
        body.append(f'<section{cls}><h2>{hh}</h2>{html}</section>')
    body.append(f'<aside class="trust"><h3>{tx["log_h"]}</h3><ul><li>{c["log"]}</li></ul></aside></main>')
    body.append('<footer><div class="wrap"><ul><li>' + tx["site"] + '</li></ul></div></footer></body></html>')
    out = h + "\n".join(body)
    out = out.replace('<p class="updated"></p>', '').replace("src='PHOTO'", "src='"+PHOTO_URI+"'")
    open(os.path.join(D, f"about-{lang}.html"), "w", encoding="utf-8").write(out)
    print(lang, len(out))
