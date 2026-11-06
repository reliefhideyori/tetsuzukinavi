SLUG = "ssw"
S1 = ("在留資格「特定技能」（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/status/specifiedskilledworker.html")
S2 = ("特定技能制度及び育成就労制度の分野別運用方針（抜粋、2026年1月23日閣議決定、出入国在留管理庁）", "https://www.moj.go.jp/isa/content/001457603.pdf")
S3 = ("特定技能制度に関するQ&A（出入国在留管理庁）", "https://www.moj.go.jp/isa/policies/ssw/faq.html")
S4 = ("特定技能ガイドブック（出入国在留管理庁）", "https://www.moj.go.jp/content/001326468.pdf")
S5 = ("Informasi Visa Tokutei Ginou（在インドネシア日本国大使館）", "https://www.id.emb-japan.go.jp/visa_tokuteiginou.html")
FIELDS_JA = "介護、ビルクリーニング、建設、造船・舶用工業、自動車整備、航空、宿泊、自動車運送業、鉄道、物流倉庫、農業、漁業、飲食料品製造業、外食業、林業、木材産業、工業製品製造業、リネンサプライ、資源循環"
FIELDS_ID = "perawatan lansia (kaigo), pembersihan gedung, konstruksi, galangan kapal dan industri perkapalan, perbaikan mobil, penerbangan, perhotelan, transportasi kendaraan (sopir), perkeretaapian, gudang logistik, pertanian, perikanan, pengolahan makanan dan minuman, restoran, kehutanan, industri kayu, manufaktur produk industri, penyediaan linen, dan daur ulang sumber daya"
PAGE = {
 "sources": [S1, S2, S3, S4, S5],
 "ja": {
  "title": "特定技能（SSW）とは", "crumb_last": "特定技能",
  "h1": "特定技能（SSW）で日本で働く：条件と流れ",
  "lead": "人手が足りない分野で、試験に合格した人が働ける在留資格です。働ける分野、必要な試験、日本に来るまでの流れ、守られるルールを公式の資料からまとめました。",
  "notice": ("いちばん大事なこと", "特定技能1号は<b>通算5年まで</b>、家族はつれて来られません。<sup><a href=\"#src\">[1][3]</a></sup>受け入れる会社は、<b>保証金を取ることも、違約金の契約を結ぶことも禁止</b>されています。<sup><a href=\"#src\">[3]</a></sup>"),
  "sections": [
   {"h": "働ける分野（19分野）", "blocks": [
     ("p", f"特定技能で働ける分野は19分野です。<sup><a href=\"#src\">[2]</a></sup>{FIELDS_JA}。"),
     ("note", "物流倉庫・リネンサプライ・資源循環は新しく加わった分野です。受け入れが始まる時期は、出入国在留管理庁のページで確認してください。<sup><a href=\"#src\">[2]</a></sup>"),
   ]},
   {"h": "1号と2号の違い", "blocks": [
     ("table", ["特定技能1号", "特定技能2号"], [
       ["働ける期間", "1回に最長3年、通算5年まで", "3年・2年・1年・6か月ごとに更新"],
       ["家族", "つれて来られない", "つれて来られる（家族滞在）"],
       ["日本語", "A2.2くらい以上（分野で違う）", "B1くらい以上"],
       ["生活の支援", "会社（または登録支援機関）が支援する", "支援の義務はない"],
     ], "出典：[1] 在留資格「特定技能」、[2] 分野別運用方針、[3] Q&A。"),
   ]},
   {"h": "必要な試験", "blocks": [
     ("dl", [
       ("技能の試験", "分野ごとの「特定技能1号評価試験」に合格する", 2),
       ("日本語の試験", "JFT-Basic（国際交流基金日本語基礎テスト）または日本語能力試験（JLPT）N4以上。介護は「介護日本語評価試験」も必要", 4),
       ("試験が免除される人", "技能実習2号を良好に終えた人は、仕事の内容に関連があれば、技能と日本語の試験が免除されます", 4),
     ]),
   ]},
   {"h": "日本に来るまでの流れ", "blocks": [
     ("steps", [
       ("", "試験に合格する", "技能の試験と日本語の試験に合格します。", 4),
       ("", "日本の会社と雇用契約を結ぶ", "給料や労働時間は、同じ仕事をする日本人と同じかそれ以上でなければいけません。", 4),
       ("", "会社が在留資格認定証明書（COE）を申請する", "申請は日本の会社が、日本の出入国在留管理局にします。", 4),
       ("", "日本大使館・総領事館でビザを申請する", "インドネシアでは Japan Visa Application Center（JVAC）で申請します。COE、パスポート、KTPの写しなどが必要です。", 5),
       ("COEの発行から3か月以内", "日本に入国して働き始める", "", 4),
     ]),
     ("note", "仲介業者を通すことは必須ではありません。日本と二国間の取り決めを結んでいる国では、悪質な仲介業者をなくすことが目的とされています。<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "あなたを守るルール", "blocks": [
     ("dl", [
       ("保証金・違約金", "取ること・契約に入れることは違法です", 3),
       ("支援の費用", "空港の送迎や住まい探しなど、会社がしなければならない支援の費用を、働く本人に払わせてはいけません", 3),
       ("会社を変える", "同じ分野の中なら会社を変えられます。在留資格の変更の申請が必要です", 3),
       ("副業", "ほかの会社でアルバイトすることはできません", 3),
     ]),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("coe", "内定からビザまで：在留資格認定証明書（COE）"), ("test", "JLPTとJFT-Basicの受け方"), ("visa", "特定技能・技能実習・育成就労の違い"), ("kaigo", "介護分野の特定技能"), ("gaji", "日本で本当に手元に残るお金（手取り計算）")])]},
  ]},
 "id": {
  "title": "Apa Itu Tokutei Ginou (SSW)", "crumb_last": "Tokutei Ginou",
  "h1": "Bekerja di Jepang dengan Tokutei Ginou (SSW): Syarat dan Alur",
  "lead": "Izin tinggal untuk orang yang lulus ujian dan bekerja di bidang yang kekurangan tenaga kerja. Ringkasan bidang kerja, ujian, alur sampai ke Jepang, dan aturan yang melindungi Anda, dari dokumen resmi.",
  "notice": ("Hal paling penting", "SSW 1 berlaku <b>total maksimal 5 tahun</b>, dan keluarga tidak bisa dibawa.<sup><a href=\"#src\">[1][3]</a></sup> Perusahaan penerima <b>dilarang memungut uang jaminan dan membuat kontrak denda</b>.<sup><a href=\"#src\">[3]</a></sup>"),
  "sections": [
   {"h": "Bidang kerja (19 bidang)", "blocks": [
     ("p", f"Ada 19 bidang kerja Tokutei Ginou:<sup><a href=\"#src\">[2]</a></sup> {FIELDS_ID}."),
     ("note", "Gudang logistik, penyediaan linen, dan daur ulang sumber daya adalah bidang yang baru ditambahkan. Cek kapan penerimaan dimulai di situs Imigrasi Jepang (ISA).<sup><a href=\"#src\">[2]</a></sup>"),
   ]},
   {"h": "Perbedaan SSW 1 dan SSW 2", "blocks": [
     ("table", ["SSW 1", "SSW 2"], [
       ["Lama bekerja", "Maksimal 3 tahun per izin, total 5 tahun", "Diperpanjang tiap 3 tahun, 2 tahun, 1 tahun, atau 6 bulan"],
       ["Keluarga", "Tidak bisa dibawa", "Bisa dibawa (izin tinggal keluarga)"],
       ["Bahasa Jepang", "Sekitar A2.2 atau lebih (berbeda per bidang)", "Sekitar B1 atau lebih"],
       ["Dukungan hidup", "Perusahaan (atau lembaga pendukung terdaftar) wajib mendukung", "Tidak ada kewajiban dukungan"],
     ], "Sumber: [1] izin tinggal Tokutei Ginou, [2] kebijakan per bidang, [3] Tanya jawab ISA."),
   ]},
   {"h": "Ujian yang dibutuhkan", "blocks": [
     ("dl", [
       ("Ujian keterampilan", "Lulus ujian keterampilan SSW 1 untuk bidang masing-masing", 2),
       ("Ujian bahasa Jepang", "JFT-Basic atau JLPT N4 ke atas. Untuk kaigo, juga perlu ujian bahasa Jepang khusus perawatan", 4),
       ("Bebas ujian", "Lulusan magang 2 (Ginou Jisshu 2-go) yang baik dibebaskan dari ujian keterampilan dan bahasa jika pekerjaannya berhubungan", 4),
     ]),
   ]},
   {"h": "Alur sampai ke Jepang", "blocks": [
     ("steps", [
       ("", "Lulus ujian", "Lulus ujian keterampilan dan ujian bahasa Jepang.", 4),
       ("", "Tanda tangan kontrak kerja dengan perusahaan Jepang", "Gaji dan jam kerja harus sama atau lebih baik dari orang Jepang yang melakukan pekerjaan yang sama.", 4),
       ("", "Perusahaan mengajukan Certificate of Eligibility (COE)", "Diajukan oleh perusahaan di Jepang ke kantor imigrasi di Jepang.", 4),
       ("", "Ajukan visa", "Di Indonesia, pengajuan lewat Japan Visa Application Center (JVAC). Perlu COE, paspor, fotokopi KTP, dan lain-lain.", 5),
       ("Dalam 3 bulan sejak COE terbit", "Masuk Jepang dan mulai bekerja", "", 4),
     ]),
     ("note", "Lewat agen tidak wajib. Kerja sama Jepang dengan negara pengirim bertujuan menghilangkan agen yang curang.<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "Aturan yang melindungi Anda", "blocks": [
     ("dl", [
       ("Uang jaminan dan denda", "Memungut atau memasukkannya ke kontrak adalah ilegal", 3),
       ("Biaya dukungan", "Biaya dukungan wajib seperti antar-jemput bandara dan bantuan mencari tempat tinggal tidak boleh dibebankan kepada pekerja", 3),
       ("Pindah perusahaan", "Bisa pindah perusahaan dalam bidang yang sama. Perlu mengajukan perubahan izin tinggal", 3),
       ("Kerja sampingan", "Tidak boleh kerja paruh waktu di perusahaan lain", 3),
     ]),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("coe", "Dari tawaran kerja sampai visa: COE"), ("test", "Cara ikut JLPT dan JFT-Basic"), ("visa", "Perbedaan Tokutei Ginou, magang, dan Ikusei Shuro"), ("kaigo", "Tokutei Ginou bidang kaigo (perawatan lansia)"), ("gaji", "Kalkulator gaji bersih")])]},
  ]},
}
