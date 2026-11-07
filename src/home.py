"""トップページ（ja/id）の本文。finish.py から呼ばれる。"""
C = {
"id": dict(
 h1="Informasi resmi sebelum bekerja di Jepang",
 lead="Gaji bersih, biaya LPK, jenis visa, ujian bahasa, prosedur setelah tiba, dan pengembalian pensiun. Semua dicek dari situs resmi pemerintah Jepang, dalam bahasa Indonesia.",
 cta=("gaji", "Hitung gaji bersih Anda"),
 feat=("kontrak", "Baru", "Cek kontrak kerja sebelum tanda tangan", "Masukkan gaji, jam kerja, dan potongan dari kontrak Anda. Lihat apakah sesuai upah minimum dan aturan jam kerja, lalu dapatkan daftar pertanyaan untuk perusahaan atau LPK. Data tidak dikirim ke mana pun.", "Mulai cek kontrak"),
 road_h="Mulai dari tahap Anda sekarang",
 stages=[
  ("Sebelum mendaftar", [("kerja", "Cara bekerja di Jepang: syarat dan langkah", "Jalur utama dan urutan dari ujian sampai berangkat."),
                         ("ssw", "Apa itu Tokutei Ginou (SSW)", "19 bidang kerja, ujian, dan alur sampai ke Jepang."),
                         ("epa", "Program EPA (G to G) perawat dan kaigo", "Syarat, pelatihan 6 bulan, dan ujian nasional Jepang."),
                         ("magang", "Program magang (Ginou Jisshu)", "Tahapan sampai 5 tahun, hal yang dilarang, dan tempat konsultasi."),
                         ("lpk", "Sebelum memilih LPK atau agen", "Biaya, uang jaminan, dan cara mengecek lembaga resmi."),
                         ("visa", "Perbedaan SSW, magang, dan Ikusei Shuro", "Lama tinggal, keluarga, bahasa Jepang, dan pindah kerja.")]),
  ("Persiapan", [("test", "Cara ikut JFT-Basic dan JLPT", "Jadwal di Indonesia, cara daftar sendiri, dan skor A2."),
                 ("kaigo", "Tokutei Ginou bidang kaigo", "3 ujian, nilai lulus, dan siapa yang bebas ujian."),
                 ("ujian", "Ujian keterampilan per bidang", "Nama ujian dan situs resmi untuk 16 bidang SSW."),
                 ("gaji", "Kalkulator gaji bersih", "Masukkan gaji dari lowongan, lihat sisa uang setiap bulan."),
                 ("upah", "Gaji rata-rata SSW dan magang", "Data pemerintah: SSW 221.400 yen, magang 190.300 yen."),
                 ("coe", "Dari tawaran kerja sampai visa (COE)", "COE berlaku 3 bulan. Visa diajukan di JVAC."),
                 ("siskop2mi", "Daftar SISKOP2MI", "Daftar sendiri setelah COE, sebelum visa.")]),
  ("Setelah tiba", [("arrival", "Dua minggu pertama di Jepang", "Lapor alamat dalam 14 hari, asuransi, dan rekening bank."),
                    ("hak", "Hak pekerja: lembur, cuti, libur", "Lembur minimal +25%, 10 hari cuti setelah 6 bulan."),
                    ("kesehatan", "Asuransi kesehatan dan biaya berobat", "Bayar 30% di rumah sakit, ada batas biaya per bulan."),
                    ("zairyu", "Zairyu card (kartu izin tinggal)", "Wajib selalu dibawa. Jika hilang, ajukan ulang dalam 14 hari."),
                    ("mynumber", "My Number dan My Number Card", "Nomor datang 2–3 minggu setelah lapor alamat. Kartu gratis."),
                    ("pindah", "Pindah perusahaan (SSW)", "Perlu mengajukan perubahan status izin tinggal dan lapor dalam 14 hari.")]),
  ("Saat pulang", [("nenkin", "Pengembalian uang pensiun", "Sebagian iuran pensiun bisa kembali. Ajukan dalam 2 tahun.")]),
 ],
 facts_h="Hal yang sering tidak diketahui",
 facts=[("lpk", "Untuk Tokutei Ginou (SSW), lewat P3MI tidak wajib.", "Lihat sumber resmi"),
        ("visa", "Perusahaan Jepang tidak boleh memungut uang jaminan atau membuat perjanjian denda (penalti) untuk pekerja SSW.", "Lihat sumber resmi"),
        ("nenkin", "Iuran pensiun yang dipotong dari gaji sebagian bisa diminta kembali setelah pulang.", "Lihat sumber resmi")],
 trust_h="Mengapa Anda bisa memercayai situs ini",
 trust=[("Hanya sumber resmi", "Setiap angka diberi sumber dari kementerian atau lembaga publik Jepang dan tanggal dicek."),
        ("Dicek tiap minggu", "Jika aturan atau upah minimum berubah, halaman diperbaiki dan dicatat di riwayat perubahan."),
        ("Tanpa komisi", "Pendapatan hanya dari iklan. Kami tidak menerima uang dari LPK, agen, atau perusahaan.")],
 op_role="Pengelola, tinggal di Jepang", op_link="Baca pesan dan kebijakan pengelola",
 upd="Terakhir dicek: 5 November 2026",
),
"ja": dict(
 h1="日本で働く前に知っておきたい、公式の情報",
 lead="手取り、LPKの費用、在留資格、日本語の試験、来日直後の手続き、帰国するときの年金。すべて日本の省庁・公的機関の公式ページで確かめてまとめています。",
 cta=("gaji", "手取りを計算する"),
 feat=("kontrak", "新しい機能", "サインする前に、雇用契約書をチェック", "契約書の給料・労働時間・天引きを入れると、最低賃金や労働時間のルールと比べて、会社やLPKに聞くべき質問の一覧が出ます。入力した内容はどこにも送られません。", "契約書をチェックする"),
 road_h="今の段階から読む",
 stages=[
  ("申し込む前", [("kerja", "日本で働くには：条件と流れ", "主な方法と、試験から出発までの順番。"),
                 ("ssw", "特定技能（SSW）とは", "19の分野、必要な試験、日本に来るまでの流れ。"),
                 ("epa", "EPA看護師・介護福祉士候補者", "条件、6か月の研修、日本の国家試験。"),
                 ("magang", "技能実習（magang）のしくみ", "最長5年の段階、禁止されていること、相談先。"),
                 ("lpk", "LPK・仲介業者を選ぶ前に", "費用、保証金、公式に確認できる方法。"),
                 ("visa", "特定技能・技能実習・育成就労の違い", "期間、家族、日本語、会社を変えられるか。")]),
  ("準備", [("test", "JFT-BasicとJLPTの受け方", "インドネシアでの日程、自分での申し込み方、A2の点数。"),
           ("kaigo", "介護分野の特定技能", "3つの試験、合格点、試験が免除される人。"),
           ("ujian", "分野ごとの技能試験", "16分野の試験名と公式サイトの一覧。"),
           ("gaji", "手取り計算機", "求人の給料を入れると、毎月いくら残るかが分かります。"),
           ("upah", "特定技能・技能実習の平均の給料", "政府の統計：特定技能22万1,400円、技能実習19万300円。"),
           ("coe", "内定からビザまで（COE）", "COEの期限は3か月。ビザはJVACで申請。"),
           ("siskop2mi", "SISKOP2MIの登録", "COEのあと、ビザの前に本人が登録します。")]),
  ("日本に着いたら", [("arrival", "最初の2週間にすること", "14日以内の住所の届出、保険、銀行口座。"),
                   ("hak", "働く人の権利", "残業は25%以上の割増、6か月で有給10日。"),
                   ("kesehatan", "健康保険と医療費", "病院で払うのは3割。1か月の上限もあります。"),
                   ("zairyu", "在留カード", "いつも持ち歩く義務。なくしたら14日以内に再交付。"),
                   ("mynumber", "マイナンバーとカード", "住所の届出から2〜3週間で番号が届きます。カードは無料。"),
                   ("pindah", "特定技能で会社を変える", "変更許可申請と、14日以内の届出が必要です。")]),
  ("帰国するとき", [("nenkin", "年金の脱退一時金", "払った年金の一部が戻ります。期限は2年。")]),
 ],
 facts_h="意外と知られていないこと",
 facts=[("lpk", "特定技能では、P3MI（送り出し機関）を通すことは必須ではありません。", "公式の出典を見る"),
        ("visa", "特定技能で受け入れる会社は、保証金を取ったり違約金の契約を結んだりしてはいけません。", "公式の出典を見る"),
        ("nenkin", "給料から引かれた年金の保険料は、帰国後に一部を請求して受け取れます。", "公式の出典を見る")],
 trust_h="このサイトが信頼できる理由",
 trust=[("公式の情報だけ", "すべての数字に、日本の省庁・公的機関の出典と確認した日を書いています。"),
        ("毎週確認", "制度や最低賃金が変わったら、ページを直して変更履歴に書きます。"),
        ("紹介料なし", "収入は広告だけです。LPK・仲介業者・会社からお金を受け取りません。")],
 op_role="運営者・日本在住", op_link="運営者のメッセージと方針を読む",
 upd="最終確認日：2026年11月5日",
),
}
CSS = """<style>
.hero{padding:var(--s3) 0 var(--s2)}.hero h1{font-size:26px;line-height:1.4;margin:0 0 var(--s2)}
.hero .btn{background:var(--key);color:var(--key-fg);margin-top:var(--s1)}
.hero .upd{font-size:14px;color:var(--fg-sub);margin-top:var(--s2)}
.road{list-style:none;padding:0;margin:0}.road>li{position:relative;padding:0 0 var(--s3) 28px}
.road>li::before{content:"";position:absolute;left:4px;top:8px;width:12px;height:12px;border-radius:50%;background:var(--key)}
.road>li:not(:last-child)::after{content:"";position:absolute;left:9px;top:24px;bottom:0;border-left:2px solid var(--line)}
.road .stage{font-size:14px;font-weight:700;color:var(--key);margin:0 0 var(--s1)}
.card{display:block;border:1px solid var(--line);border-radius:8px;padding:12px var(--s2);margin-bottom:var(--s1);text-decoration:none;color:var(--fg)}
.card:hover{border-color:var(--key)}.card b{display:block;color:var(--key)}.card span{font-size:14px;color:var(--fg-sub)}
.facts{list-style:none;padding:0;margin:0}.facts li{border-left:4px solid var(--ok);background:var(--ok-bg);padding:12px var(--s2);margin-bottom:var(--s1)}
.facts a{font-size:14px}
.why{display:grid;gap:var(--s1)}.why div{background:var(--bg-soft);border-radius:8px;padding:12px var(--s2)}.why b{display:block}
.why p{font-size:14px;color:var(--fg-sub);margin:0}
.feat{border:2px solid var(--key);border-radius:8px;padding:var(--s5);margin:var(--s6) 0 var(--s10)}.feat .tag{display:inline-block;font-size:12px;font-weight:700;color:var(--key-fg);background:var(--key);border-radius:4px;padding:0 var(--s2);margin-bottom:var(--s2)}
.feat h2{font-size:19px;border:0;padding:0;margin:0 0 var(--s2)}.feat p{font-size:15px;color:var(--fg-sub);margin:0}.feat .btn{background:var(--key);color:var(--key-fg)}
.op{display:flex;gap:var(--s2);align-items:center;margin-top:var(--s2)}.op img{width:64px;height:64px;border-radius:50%;object-fit:cover;flex:none}
.op p{margin:0}.op small{color:var(--fg-sub)}
</style></head>"""
def main(lang):
    c = C[lang]; L = lambda s: f"/{lang}/{s}"
    road = "".join(f'<li><p class="stage">{st}</p>' + "".join(f'<a class="card" href="{L(s)}"><b>{t}</b><span>{d}</span></a>' for s, t, d in items) + '</li>' for st, items in c["stages"])
    facts = "".join(f'<li>{t} <a href="{L(s)}#src">{a}</a></li>' for s, t, a in c["facts"])
    why = "".join(f'<div><b>{h}</b><p>{p}</p></div>' for h, p in c["trust"])
    return (f'<main class="wrap"><div class="hero"><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p>'
            f'<a class="btn" href="{L(c["cta"][0])}">{c["cta"][1]}</a><p class="upd">{c["upd"]}</p></div>'
            f'<div class="feat"><span class="tag">{c["feat"][1]}</span><h2>{c["feat"][2]}</h2><p>{c["feat"][3]}</p><a class="btn" href="{L(c["feat"][0])}">{c["feat"][4]}</a></div>'
            f'<section><h2>{c["road_h"]}</h2><ol class="road">{road}</ol></section>'
            f'<section><h2>{c["facts_h"]}</h2><ul class="facts">{facts}</ul></section>'
            f'<section><h2>{c["trust_h"]}</h2><div class="why">{why}</div>'
            f'<div class="op"><img src="/img/operator.jpg" alt="Hideyori Shiraki" width="64" height="64"><p><b>Hideyori Shiraki</b><br><small>{c["op_role"]}</small><br><a href="{L("about")}">{c["op_link"]}</a></p></div></section></main>')
