SLUG = "jlpt"
S1 = ("JLPT インドネシア：よくある質問（実施機関）", "https://jlptonline.or.id/faq")
S2 = ("JLPT インドネシア（実施機関トップ）", "https://jlptonline.or.id/")
S3 = ("海外の実施都市・実施機関一覧（JLPT公式）", "https://www.jlpt.jp/e/application/overseas_list.html")
S4 = ("N1〜N5 認定の目安（JLPT公式）", "https://www.jlpt.jp/e/about/levelsummary.html")
S5 = ("特定技能 試験関係（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/ssw/nyuukokukanri01_00135.html")
CITIES = "Jakarta, Bandung, Surabaya, Medan, Yogyakarta, Padang, Denpasar, Manado, Malang, Semarang, Makassar, Palembang, Cirebon, Bogor, Tangerang, Samarinda"
PAGE = {
 "date": "2026-11-16",
 "sources": [S1, S2, S3, S4, S5],
 "ja": {
  "title": "JLPT 2026：インドネシアでの日程と申し込み", "crumb_last": "JLPT",
  "h1": "JLPT 2026：インドネシアでの日程・受験料・申し込み方とN1〜N5",
  "lead": "日本語能力試験（JLPT）をインドネシアで受けるときの日程、受験料、オンライン申し込みの注意、結果と証明書の受け取り、N1〜N5のレベルを、公式の情報からまとめました。",
  "notice": ("まず知っておくこと", "インドネシアのJLPTは<b>年2回（7月と12月）</b>です。2026年の第2回は<b>12月6日（日）</b>。<sup><a href=\"#src\">[2]</a></sup>申し込みは<b>オンラインだけ</b>で、窓口や代理での申し込みはできません。<sup><a href=\"#src\">[1]</a></sup>"),
  "sections": [
   {"h": "日程と申し込み期間", "blocks": [
     ("table", ["申し込み（目安）", "結果", "証明書の受け取り"], [
       ["7月の試験", "3月中旬〜4月上旬", "8月末ごろ", "10月末ごろ"],
       ["12月の試験", "8月中旬〜9月上旬", "翌年1月末ごろ", "翌年3月末〜4月ごろ"],
     ], "出典：[1] インドネシアの実施機関。正確な期間は毎回jlptonline.or.idで発表されます。都市によっては1回だけのところもあります。"),
     ("note", "2026年12月の試験の申し込みはすでに終わっています。次は<b>2027年7月の試験</b>で、申し込みは3月中旬ごろからの見込みです。"),
   ]},
   {"h": "受験料", "blocks": [
     ("dl", [("N1・N2", "350,000ルピア", 1), ("N3・N4・N5", "250,000ルピア", 1)]),
     ("p", "このほかに事務手数料がかかります。払ったお金は戻りません。<sup><a href=\"#src\">[1]</a></sup>"),
   ]},
   {"h": "申し込みの注意", "blocks": [
     ("steps", [
       ("", "アカウントを作る", "申し込み期間にjlptonline.or.idで作ります。アカウントは1回の試験だけ使えます。確認メールが届くよう、できればGmailを使います。", 1),
       ("", "会場・レベル・支払い方法を選ぶ", "支払ったあとは変更できません。2026年12月の試験から、写真は申し込みのときにシステムで撮ります。", 1),
       ("時間内に", "支払う", "銀行ATM（バーチャルアカウント）は2時間以内、QRISやGopayは1時間以内。モバイルバンキング、ネットバンキング、クレジットカード、OVO、DANA、ShopeePayなどは使えません。期限を過ぎると申し込みは消えます。", 1),
       ("試験の日", "受ける", "鉛筆（2BかHB）と消しゴム、受験票、写真つき身分証の原本を持っていきます。家族カード（KK）やデジタルの身分証はだめです。受付の30分前には着くようにします。", 1),
     ]),
   ]},
   {"h": "試験を行う都市", "blocks": [("p", f"{CITIES}の16都市です。<sup><a href=\"#src\">[3]</a></sup>")]},
   {"h": "N1〜N5のレベル", "blocks": [
     ("dl", [
       ("N1", "幅広い場面で使われる日本語を理解できる", 4),
       ("N2", "日常的な場面の日本語に加え、より幅広い場面の日本語をある程度理解できる", 4),
       ("N3", "日常的な場面で使われる日本語をある程度理解できる", 4),
       ("N4", "基本的な日本語を理解できる。特定技能1号の日本語の条件はN4以上", 5),
       ("N5", "基本的な日本語をある程度理解できる", 4),
     ]),
     ("p", "合格には、総合点が合格点以上で、さらに各科目の基準点以上が必要です。<sup><a href=\"#src\">[1]</a></sup>"),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("jft", "JFT-Basic：受験料・申し込み・合格点"), ("ujian", "分野別の技能試験"), ("ssw", "特定技能（SSW）とは"), ("kerja", "日本で働くには：条件と流れ")])]},
  ]},
 "id": {
  "title": "JLPT 2026 di Indonesia: Jadwal dan Pendaftaran", "crumb_last": "JLPT",
  "h1": "JLPT 2026 di Indonesia: Jadwal, Biaya, Cara Pendaftaran, dan Level N1–N5",
  "lead": "Halaman ini merangkum cara ikut Ujian Kemampuan Bahasa Jepang (JLPT) di Indonesia: jadwal, biaya, hal penting saat pendaftaran online, pengumuman hasil dan pengambilan sertifikat, serta arti level N1–N5, berdasarkan informasi resmi.",
  "notice": ("Yang perlu diketahui dulu", "JLPT di Indonesia diadakan <b>2 kali setahun (Juli dan Desember)</b>. Ujian kedua tahun 2026 diadakan pada <b>Minggu, 6 Desember 2026</b>.<sup><a href=\"#src\">[2]</a></sup> Pendaftaran <b>hanya secara online</b>; tidak bisa mendaftar langsung di loket atau diwakilkan orang lain.<sup><a href=\"#src\">[1]</a></sup>"),
  "sections": [
   {"h": "Jadwal dan masa pendaftaran", "blocks": [
     ("table", ["Pendaftaran (perkiraan)", "Hasil", "Pengambilan sertifikat"], [
       ["Ujian Juli", "Pertengahan Maret – awal April", "Sekitar akhir Agustus", "Sekitar akhir Oktober"],
       ["Ujian Desember", "Pertengahan Agustus – awal September", "Sekitar akhir Januari tahun berikutnya", "Sekitar akhir Maret – April tahun berikutnya"],
     ], "Sumber: [1] penyelenggara JLPT di Indonesia. Tanggal pasti diumumkan setiap periode di jlptonline.or.id. Beberapa kota hanya mengadakan satu kali setahun."),
     ("note", "Pendaftaran untuk ujian Desember 2026 sudah ditutup. Berikutnya adalah <b>ujian Juli 2027</b>, dengan pendaftaran diperkirakan mulai sekitar pertengahan Maret."),
   ]},
   {"h": "Biaya ujian", "blocks": [
     ("dl", [("N1 dan N2", "Rp350.000", 1), ("N3, N4, dan N5", "Rp250.000", 1)]),
     ("p", "Selain itu, ada biaya administrasi. Biaya yang sudah dibayar tidak dikembalikan.<sup><a href=\"#src\">[1]</a></sup>"),
   ]},
   {"h": "Hal penting saat mendaftar", "blocks": [
     ("steps", [
       ("", "Buat akun", "Buat akun di jlptonline.or.id saat masa pendaftaran. Akun hanya berlaku untuk satu periode ujian. Sebaiknya pakai Gmail agar email konfirmasi bisa diterima.", 1),
       ("", "Pilih lokasi, level, dan cara bayar", "Tidak bisa diubah setelah membayar. Mulai JLPT Desember 2026, foto diambil langsung oleh sistem saat pendaftaran.", 1),
       ("Dalam batas waktu", "Bayar", "ATM bank (Virtual Account): 2 jam. QRIS atau Gopay: 1 jam. Mobile banking, internet banking, kartu kredit, OVO, DANA, ShopeePay, dan lainnya tidak diterima. Jika lewat batas waktu, pendaftaran akan dihapus.", 1),
       ("Hari ujian", "Ikut ujian", "Bawa pensil 2B atau HB, penghapus, kartu ujian, dan kartu identitas asli berfoto. Kartu Keluarga (KK) dan identitas digital tidak diterima. Datang minimal 30 menit sebelum waktu check-in.", 1),
     ]),
   ]},
   {"h": "Kota tempat ujian", "blocks": [("p", f"Ada 16 kota: {CITIES}.<sup><a href=\"#src\">[3]</a></sup>")]},
   {"h": "Arti level N1–N5", "blocks": [
     ("dl", [
       ("N1", "Bisa memahami bahasa Jepang yang dipakai dalam berbagai situasi", 4),
       ("N2", "Bisa memahami bahasa Jepang sehari-hari, dan sampai batas tertentu bahasa Jepang dalam situasi yang lebih luas", 4),
       ("N3", "Bisa memahami bahasa Jepang sehari-hari sampai batas tertentu", 4),
       ("N4", "Bisa memahami bahasa Jepang dasar. Syarat bahasa Jepang untuk SSW 1 adalah N4 ke atas", 5),
       ("N5", "Bisa memahami sebagian bahasa Jepang dasar", 4),
     ]),
     ("p", "Untuk lulus, skor total harus mencapai nilai lulus dan setiap bagian harus mencapai nilai minimum.<sup><a href=\"#src\">[1]</a></sup>"),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("jft", "JFT-Basic: biaya, cara daftar, dan nilai lulus"), ("ujian", "Ujian keterampilan per bidang"), ("ssw", "Apa itu Tokutei Ginou (SSW)"), ("kerja", "Cara bekerja di Jepang: syarat dan langkah")])]},
  ]},
}
