SLUG = "coe"
S1 = ("出入国審査・在留審査Q&A（出入国在留管理庁）", "https://www.moj.go.jp/isa/immigration/faq/kanri_qa.html")
S2 = ("在留資格認定証明書の電子化について（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/procedures/10_00136.html")
S3 = ("Informasi Visa Tokutei Ginou（在インドネシア日本国大使館）", "https://www.id.emb-japan.go.jp/visa_tokuteiginou.html")
S4 = ("特定技能ガイドブック（出入国在留管理庁）", "https://www.moj.go.jp/content/001326468.pdf")
PAGE = {
 "sources": [S1, S2, S3, S4],
 "ja": {
  "title": "内定からビザまで（COE）", "crumb_last": "COEとビザ",
  "h1": "内定からビザまで：在留資格認定証明書（COE）の流れ",
  "lead": "日本の会社から内定をもらった後、日本に入国するまでに必要な「在留資格認定証明書（COE）」とビザの手続きを、公式の情報からまとめました。",
  "notice": ("期限があること", "COEは<b>発行された日から3か月以内</b>に日本に入国しないと、使えなくなります。<sup><a href=\"#src\">[1]</a></sup>ビザの有効期間とは別なので注意してください。"),
  "sections": [
   {"h": "COEとビザの違い", "blocks": [
     ("dl", [
       ("COE（在留資格認定証明書）", "日本の入管が「この人はこの在留資格の条件を満たしている」と認めた書類。申請できるのは日本にいる会社（受け入れ先）などだけです", 3),
       ("ビザ（査証）", "日本大使館・総領事館が出す、入国のための書類。COEがあると手続きが早く進みます", 1),
       ("在留カード", "日本の空港で入国したときに渡されるカード", ""),
     ]),
   ]},
   {"h": "手続きの流れ", "blocks": [
     ("steps", [
       ("", "雇用契約を結ぶ", "給料や仕事の内容を書面で確認します。", 4),
       ("", "会社が日本の入管にCOEを申請する", "本人はインドネシアで待ちます。会社から、パスポートの写しなどを頼まれることがあります。", 4),
       ("", "COEを受け取る", "今はメールで電子のCOEを受け取ることもできます。そのメールを大使館や空港で見せられます。", 2),
       ("", "ビザを申請する", "インドネシアでは、大使館ではなく Japan Visa Application Center（JVAC、ジャカルタのクニンガン・シティ・モール2階）で申請し、受け取ります。", 3),
       ("COEの発行から3か月以内", "日本に入国する", "空港で在留カードを受け取ります。", 1),
     ]),
   ]},
   {"h": "ビザ申請に必要なもの（特定技能の場合）", "blocks": [
     ("dl", [
       ("パスポート", "", 3),
       ("ビザ申請書と写真", "申請書はQRコード付きのPDF。写真は6か月以内に撮ったもの", 3),
       ("KTPの写し", "", 3),
       ("COE", "原本または写し", 3),
       ("インドネシア政府の海外就労の登録", "大使館のページでは、政府のシステムに登録した証明（E-KTKLN）の印刷が必要とされています。今の登録方法はインドネシア政府の窓口で確認してください", 3),
     ]),
     ("note", "必要なものは変わることがあります。申請の前に、JVAC（VFS Global）のページで最新の一覧を確認してください。<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("ssw", "特定技能（SSW）で日本で働く：条件と流れ"), ("arrival", "日本に着いて最初の2週間にすること"), ("lpk", "LPK・仲介業者を選ぶ前に、公式情報で確認できること")])]},
  ]},
 "id": {
  "title": "Dari Tawaran Kerja sampai Visa (COE)", "crumb_last": "COE dan visa",
  "h1": "Dari Tawaran Kerja sampai Visa: Alur Certificate of Eligibility (COE)",
  "lead": "Setelah mendapat tawaran kerja dari perusahaan Jepang, Anda perlu COE (zairyu shikaku nintei shomeisho) dan visa sebelum masuk Jepang. Ringkasan alurnya dari informasi resmi.",
  "notice": ("Ada batas waktunya", "COE <b>tidak berlaku lagi jika Anda tidak masuk Jepang dalam 3 bulan</b> sejak tanggal terbit.<sup><a href=\"#src\">[1]</a></sup> Ini berbeda dengan masa berlaku visa."),
  "sections": [
   {"h": "Perbedaan COE dan visa", "blocks": [
     ("dl", [
       ("COE", "Dokumen dari imigrasi Jepang yang menyatakan Anda memenuhi syarat izin tinggal. Hanya bisa diajukan oleh pihak di Jepang, misalnya perusahaan penerima", 3),
       ("Visa", "Dokumen dari Kedutaan/Konsulat Jepang untuk masuk Jepang. Dengan COE, prosesnya lebih cepat", 1),
       ("Zairyu card", "Kartu izin tinggal yang diberikan di bandara Jepang saat masuk", ""),
     ]),
   ]},
   {"h": "Alur prosedur", "blocks": [
     ("steps", [
       ("", "Tanda tangan kontrak kerja", "Cek gaji dan isi pekerjaan secara tertulis.", 4),
       ("", "Perusahaan mengajukan COE ke imigrasi Jepang", "Anda menunggu di Indonesia. Perusahaan mungkin meminta fotokopi paspor dan dokumen lain.", 4),
       ("", "Terima COE", "Sekarang COE elektronik juga bisa diterima lewat email. Email itu bisa ditunjukkan di kedutaan dan bandara.", 2),
       ("", "Ajukan visa", "Di Indonesia, pengajuan dan pengambilan visa dilakukan di Japan Visa Application Center (JVAC), Kuningan City Mall lantai 2, bukan di kedutaan.", 3),
       ("Dalam 3 bulan sejak COE terbit", "Masuk Jepang", "Terima zairyu card di bandara.", 1),
     ]),
   ]},
   {"h": "Yang dibutuhkan untuk visa (Tokutei Ginou)", "blocks": [
     ("dl", [
       ("Paspor", "", 3),
       ("Formulir visa dan foto", "Formulir PDF dengan kode QR. Foto diambil dalam 6 bulan terakhir", 3),
       ("Fotokopi KTP", "", 3),
       ("COE", "Asli atau fotokopi", 3),
       ("Pendaftaran kerja luar negeri pemerintah Indonesia", "Halaman kedutaan menyebut cetakan E-KTKLN dari sistem pemerintah. Cek cara pendaftaran terbaru di instansi pemerintah Indonesia", 3),
     ]),
     ("note", "Daftar dokumen bisa berubah. Sebelum mengajukan, cek daftar terbaru di situs JVAC (VFS Global).<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("ssw", "Bekerja di Jepang dengan Tokutei Ginou (SSW)"), ("arrival", "Dua minggu pertama di Jepang"), ("lpk", "Sebelum memilih LPK atau agen")])]},
  ]},
}
