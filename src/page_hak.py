SLUG = "hak"
S1 = ("時間外・休日労働と割増賃金（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/study/roudousya_jikangai.html")
S2 = ("年次有給休暇をとる条件は？（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/qa/roudousya/yukyu/q1.html")
S3 = ("労働基準法（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/law/roudoukijun.html")
S4 = ("外国人労働者向け相談ダイヤル（厚生労働省）", "https://www.mhlw.go.jp/content/001708139.pdf")
PAGE = {
 "sources": [S1, S2, S3, S4],
 "ja": {
  "title": "日本で働く人の権利", "crumb_last": "働く人の権利",
  "h1": "日本で働く人の権利：残業代・有給休暇・休み",
  "lead": "日本の労働の法律は、外国人にも同じように適用されます。労働時間、残業代、休み、有給休暇、給料の払い方、解雇のルールを、厚生労働省の情報からまとめました。",
  "notice": ("いちばん大事なこと", "残業には<b>25%以上の割増賃金</b>が払われます。<sup><a href=\"#src\">[1]</a></sup>6か月働くと<b>10日の有給休暇</b>がもらえます。<sup><a href=\"#src\">[2]</a></sup>特定技能でも技能実習でも同じです。"),
  "sections": [
   {"h": "労働時間と休み", "blocks": [
     ("dl", [
       ("労働時間", "原則1日8時間、1週40時間まで", 1),
       ("休日", "毎週少なくとも1日（または4週間で4日以上）", 1),
       ("残業の上限", "原則として月45時間、年360時間まで。残業させるには会社と労働者の代表との協定（36協定）が必要", 1),
     ]),
   ]},
   {"h": "残業代（割増賃金）", "blocks": [
     ("table", ["割増", "時給1,200円の例"], [
       ["残業（1日8時間・週40時間を超えた分）", "25%以上", "1,500円以上"],
       ["深夜（22時〜5時）", "25%以上", "1,500円以上"],
       ["休日（法定の休日）", "35%以上", "1,620円以上"],
       ["残業が月60時間を超えた分", "50%以上", "1,800円以上"],
     ], "出典：[1] 厚生労働省。残業と深夜が重なると割増は足し算になります（例：休日の深夜は1.6倍）。"),
   ]},
   {"h": "有給休暇", "blocks": [
     ("p", "6か月続けて働き、働く日の8割以上出勤した人は、10日の有給休暇がもらえます。<sup><a href=\"#src\">[2]</a></sup>その後は1年ごとに増えます。"),
     ("table", ["もらえる日数"], [["6か月", "10日"], ["1年6か月", "11日"], ["2年6か月", "12日"], ["3年6か月", "14日"], ["4年6か月", "16日"], ["5年6か月", "18日"], ["6年6か月以上", "20日"]], "フルタイムの場合。出典：[2]"),
     ("note", "10日以上もらえる人は、会社が1年に5日以上を必ず取らせなければいけません。<sup><a href=\"#src\">[2]</a></sup>"),
   ]},
   {"h": "給料と解雇のルール", "blocks": [
     ("dl", [
       ("給料の払い方", "お金で、本人に直接、全額を、毎月、決まった日に払う（5つの原則）", 3),
       ("解雇", "会社は30日以上前に知らせるか、30日分以上の平均賃金を払わなければいけません", 3),
       ("最低賃金", "都道府県ごとの最低賃金より低い給料は違法です。手取り計算機で確認できます", ""),
     ]),
   ]},
   {"h": "困ったときの相談先", "blocks": [
     ("fact", "外国人労働者向け相談ダイヤル（厚生労働省）0570-001-715", "インドネシア語：火曜・木曜 10:00〜15:00（12:00〜13:00を除く）。残業代が払われない、休みがもらえないなどの相談ができます。", 4),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("gaji", "日本で本当に手元に残るお金（手取り計算）"), ("ssw", "特定技能（SSW）で日本で働く：条件と流れ"), ("magang", "技能実習のしくみと、実習生を守るルール")])]},
  ]},
 "id": {
  "title": "Hak Pekerja di Jepang", "crumb_last": "Hak pekerja",
  "h1": "Hak Pekerja di Jepang: Upah Lembur, Cuti Tahunan, dan Hari Libur",
  "lead": "Hukum ketenagakerjaan Jepang berlaku sama untuk pekerja asing. Ringkasan jam kerja, upah lembur, hari libur, cuti tahunan berbayar, cara pembayaran gaji, dan aturan PHK, dari informasi MHLW.",
  "notice": ("Hal paling penting", "Upah lembur <b>minimal 25% lebih tinggi</b> dari upah biasa.<sup><a href=\"#src\">[1]</a></sup> Setelah bekerja 6 bulan, Anda mendapat <b>10 hari cuti berbayar</b>.<sup><a href=\"#src\">[2]</a></sup> Berlaku sama untuk SSW maupun magang."),
  "sections": [
   {"h": "Jam kerja dan hari libur", "blocks": [
     ("dl", [
       ("Jam kerja", "Pada dasarnya maksimal 8 jam sehari dan 40 jam seminggu", 1),
       ("Hari libur", "Minimal 1 hari setiap minggu (atau minimal 4 hari dalam 4 minggu)", 1),
       ("Batas lembur", "Pada dasarnya maksimal 45 jam sebulan dan 360 jam setahun. Lembur hanya boleh jika ada perjanjian antara perusahaan dan perwakilan pekerja (perjanjian 36)", 1),
     ]),
   ]},
   {"h": "Upah lembur", "blocks": [
     ("table", ["Tambahan", "Contoh upah 1.200 yen/jam"], [
       ["Lembur (lebih dari 8 jam/hari atau 40 jam/minggu)", "25% atau lebih", "1.500 yen atau lebih"],
       ["Malam (22.00–05.00)", "25% atau lebih", "1.500 yen atau lebih"],
       ["Hari libur wajib mingguan (hotei kyujitsu)", "35% atau lebih", "1.620 yen atau lebih"],
       ["Lembur lebih dari 60 jam sebulan", "50% atau lebih", "1.800 yen atau lebih"],
     ], "Sumber: [1] MHLW. Jika lembur dan kerja malam bersamaan, tambahannya dijumlahkan (contoh: malam di hari libur = 1,6 kali)."),
   ]},
   {"h": "Cuti tahunan berbayar (yukyu)", "blocks": [
     ("p", "Jika bekerja terus-menerus selama 6 bulan dan hadir 80% atau lebih dari hari kerja, Anda mendapat 10 hari cuti berbayar.<sup><a href=\"#src\">[2]</a></sup> Setelah itu bertambah setiap tahun."),
     ("table", ["Jumlah hari"], [["6 bulan", "10 hari"], ["1 tahun 6 bulan", "11 hari"], ["2 tahun 6 bulan", "12 hari"], ["3 tahun 6 bulan", "14 hari"], ["4 tahun 6 bulan", "16 hari"], ["5 tahun 6 bulan", "18 hari"], ["6 tahun 6 bulan atau lebih", "20 hari"]], "Untuk pekerja penuh waktu. Sumber: [2]"),
     ("note", "Jika mendapat 10 hari atau lebih, perusahaan wajib memastikan Anda mengambil minimal 5 hari dalam setahun.<sup><a href=\"#src\">[2]</a></sup>"),
   ]},
   {"h": "Aturan gaji dan PHK", "blocks": [
     ("dl", [
       ("Cara bayar gaji", "Dibayar dengan uang, langsung kepada pekerja, secara penuh, setiap bulan, pada tanggal tetap (5 prinsip)", 3),
       ("PHK", "Perusahaan harus memberi tahu minimal 30 hari sebelumnya, atau membayar minimal 30 hari upah rata-rata", 3),
       ("Upah minimum", "Gaji di bawah upah minimum prefektur adalah ilegal. Bisa dicek dengan kalkulator gaji bersih", ""),
     ]),
   ]},
   {"h": "Tempat konsultasi", "blocks": [
     ("fact", "Layanan Konsultasi untuk Pekerja Asing (MHLW) 0570-001-715", "Bahasa Indonesia: Selasa dan Kamis 10.00–15.00 (kecuali 12.00–13.00). Bisa konsultasi jika upah lembur tidak dibayar atau tidak diberi libur.", 4),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("gaji", "Kalkulator gaji bersih"), ("ssw", "Bekerja di Jepang dengan Tokutei Ginou (SSW)"), ("magang", "Program magang Jepang dan aturan yang melindungi peserta")])]},
  ]},
}
