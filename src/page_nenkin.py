SLUG = "nenkin"
S1 = ("脱退一時金の制度（日本年金機構、2026年4月1日更新）", "https://www.nenkin.go.jp/service/jukyu/seido/sonota-kyufu/dattai-ichiji/20150406.html")
S2 = ("日本から出国される外国人のみなさまへ（脱退一時金の案内、インドネシア語版、日本年金機構）", "https://www.nenkin.go.jp/international/english/japanese-system/benefit/payment.files/F.pdf")
S3 = ("厚生年金保険の脱退一時金として、いくらもらえますか（日本年金機構）", "https://www.nenkin.go.jp/section/faq/jukyu/seido/sonota-kyufu/dattai-ichiji/2020042803.html")
ROWS_JA = [["6〜11か月", "0.5", "110,000円", "87,538円"], ["12〜17か月", "1.1", "242,000円", "192,584円"], ["24〜29か月", "2.2", "484,000円", "385,167円"],
           ["36〜41か月", "3.3", "726,000円", "577,751円"], ["48〜53か月", "4.4", "968,000円", "770,334円"], ["60か月以上", "5.5", "1,210,000円", "962,918円"]]
ROWS_ID = [[r[0].replace("か月以上", " bulan atau lebih").replace("か月", " bulan").replace("〜", "–"), r[1], r[2].replace("円", " yen"), r[3].replace("円", " yen")] for r in ROWS_JA]
PAGE = {
 "sources": [S1, S2, S3],
 "ja": {
  "title": "年金の脱退一時金", "crumb_last": "年金の脱退一時金",
  "h1": "帰国するときに年金の一部が戻る「脱退一時金」",
  "lead": "日本で働くと、給料から年金の保険料が引かれます。帰国した後に請求すると、その一部が戻ります。受け取れる人、金額の目安、請求のしかたを公式の情報からまとめました。",
  "notice": ("いちばん大事なこと", "日本の年金に<b>6か月以上</b>入っていた外国人は、日本に住所がなくなった日から<b>2年以内</b>に請求すれば、脱退一時金を受け取れます。<sup><a href=\"#src\">[1]</a></sup>2年を過ぎると請求できません。"),
  "sections": [
   {"h": "受け取れる人", "blocks": [
     ("dl", [
       ("国籍", "日本の国籍がない", 1),
       ("加入した期間", "厚生年金（会社の年金）または国民年金に、合わせて6か月以上入っていた（国民年金は保険料を払った月だけ数えます）", 1),
       ("住所", "日本に住所がない（帰国して住民票がなくなっている）", 1),
       ("期限", "日本に住所がなくなった日から2年以内", 1),
       ("そのほか", "日本の年金をもらう資格（加入10年以上）がない。障害年金などを受ける権利を持ったことがない", 1),
     ]),
   ]},
   {"h": "いくら戻るか（厚生年金の場合）", "blocks": [
     ("p", "金額は「入っていた間の平均の給料（平均標準報酬額）×支給率」で決まります。支給率は入っていた月数で決まり、60か月（5年）が上限です。<sup><a href=\"#src\">[1][3]</a></sup>"),
     ("table", ["支給率", "例：平均の給料22万円", "税金20.42%を引いた後"], ROWS_JA,
      "出典：[1][3] 日本年金機構。支給率は2026年の表の一部です。22万円は計算の例で、実際の金額は加入記録で決まります。"),
     ("fact", "国民年金の場合", "国民年金だけに入っていた人は、最後に払った年度の保険料で決まります。最後の月が2026年4月〜2027年3月の場合、6〜11か月で53,760円、60か月以上で537,600円です。国民年金の脱退一時金には税金はかかりません。", 1),
   ]},
   {"h": "請求のしかた", "blocks": [
     ("steps", [
       ("帰国の前", "役所で転出届を出す", "住んでいる市区町村の役所に、日本を出ることを届けます。出しておくと「日本に住所がないことの書類」が要らなくなります。", 2),
       ("帰国の前", "書類をそろえる", "請求書、パスポートの写し、銀行の口座がわかる書類（銀行が出したもの）、基礎年金番号がわかる書類（基礎年金番号通知書や年金手帳）。ゆうちょ銀行の口座では受け取れません。", 2),
       ("転出の日より後に届くように", "日本年金機構に郵送する", "あて先は「日本年金機構 外国業務グループ 〒168-8505 東京都杉並区高井戸西3-5-24」です。日本から送っても、帰国後に自分の国から送ってもかまいません。", 2),
       ("審査の後", "口座に振り込まれる", "書類が足りないと、請求書が送り返されることがあります。", 2),
     ]),
   ]},
   {"h": "税金を取り戻す手続き（厚生年金の場合）", "blocks": [
     ("p", "厚生年金の脱退一時金からは、所得税20.42%が引かれます。<sup><a href=\"#src\">[2]</a></sup>税務署に申告すると、引かれた税金が戻ることがあります。"),
     ("steps", [
       ("帰国の前", "納税管理人を決めて届け出る", "日本に住む人に、税金の手続きを任せます。「所得税・消費税の納税管理人の届出書」を、住んでいた地域の税務署に出します。", 2),
       ("脱退一時金を受け取った後", "還付の申告をする", "納税管理人が「退職所得の選択課税による還付のための申告書」を税務署に出します。脱退一時金の支給通知書（原本）が必要なので、納税管理人に送ってください。", 2),
     ]),
   ]},
   {"h": "受け取る前に知っておくこと", "blocks": [
     ("warn", "脱退一時金を受け取ると、<b>それまでの日本の年金に入っていた期間はすべてなくなります</b>。将来また日本で働いても、その期間は数えられません。<sup><a href=\"#src\">[2]</a></sup>"),
     ("dl", [
       ("60か月より長く入っていた人", "受け取れるのは60か月分までですが、入っていた期間はすべてなくなります。", 2),
       ("10年以上入っていた人", "脱退一時金は請求できません。日本の年金を受け取る資格があります。", 2),
       ("インドネシアとの協定", "日本とインドネシアの間には、年金の期間を合わせて数える協定（社会保障協定）はありません（2026年3月時点）。", 2),
       ("再入国許可で出国した人", "転出届を出さずに再入国許可で出国した場合は、許可の期限が過ぎるまで請求できません。", 2),
     ]),
   ]},
   {"h": "困ったときの相談先", "blocks": [
     ("fact", "日本年金機構 外国業務グループ　+81-3-6700-1165", "脱退一時金の手続きについて聞けます。日本語での対応です。", 2),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("gaji", "日本で本当に手元に残るお金（手取り計算）"), ("arrival", "日本に着いて最初の2週間にすること"), ("visa", "特定技能・技能実習・育成就労の違い")])]},
  ]},
 "id": {
  "title": "Pengembalian Uang Pensiun (Dattai Ichijikin)", "crumb_last": "Dattai ichijikin",
  "h1": "Uang Pensiun yang Kembali Saat Pulang: Dattai Ichijikin",
  "lead": "Saat bekerja di Jepang, iuran pensiun dipotong dari gaji. Setelah pulang, sebagian bisa diminta kembali. Ringkasan siapa yang bisa menerima, perkiraan jumlah, dan cara mengajukan dari informasi resmi.",
  "notice": ("Hal paling penting", "Orang asing yang ikut pensiun Jepang <b>6 bulan atau lebih</b> bisa menerima dattai ichijikin (Lump-sum Withdrawal Payment) jika mengajukan <b>dalam 2 tahun</b> sejak tidak lagi punya alamat di Jepang.<sup><a href=\"#src\">[1]</a></sup> Jika sudah lewat 2 tahun, tidak bisa diajukan lagi."),
  "sections": [
   {"h": "Siapa yang bisa menerima", "blocks": [
     ("dl", [
       ("Kewarganegaraan", "Bukan warga negara Jepang", 1),
       ("Lama ikut pensiun", "Ikut kosei nenkin (pensiun karyawan) atau kokumin nenkin (pensiun nasional) total 6 bulan atau lebih (untuk kokumin nenkin, hanya bulan yang iurannya dibayar)", 1),
       ("Alamat", "Tidak punya alamat di Jepang (sudah pulang dan data penduduk sudah dihapus)", 1),
       ("Batas waktu", "Dalam 2 tahun sejak tidak punya alamat di Jepang", 1),
       ("Lainnya", "Tidak memenuhi syarat pensiun Jepang (ikut 10 tahun atau lebih). Belum pernah punya hak atas pensiun disabilitas dan sejenisnya", 1),
     ]),
   ]},
   {"h": "Berapa yang kembali (kosei nenkin)", "blocks": [
     ("p", "Jumlahnya = rata-rata gaji selama ikut pensiun (heikin hyojun hoshu) × tingkat pembayaran. Tingkat pembayaran ditentukan oleh jumlah bulan, dengan batas 60 bulan (5 tahun).<sup><a href=\"#src\">[1][3]</a></sup>"),
     ("table", ["Tingkat pembayaran", "Contoh: rata-rata gaji 220.000 yen", "Setelah dipotong pajak 20,42%"], ROWS_ID,
      "Sumber: [1][3] Japan Pension Service. Sebagian dari tabel 2026. 220.000 yen hanya contoh; jumlah sebenarnya ditentukan dari catatan kepesertaan. 1 yen ≈ Rp114 (4 November 2026)."),
     ("fact", "Untuk kokumin nenkin", "Jika hanya ikut kokumin nenkin, jumlahnya ditentukan dari iuran tahun terakhir dibayar. Jika bulan terakhir antara April 2026 dan Maret 2027: 6–11 bulan 53.760 yen, 60 bulan atau lebih 537.600 yen. Tidak ada pajak untuk dattai ichijikin kokumin nenkin.", 1),
   ]},
   {"h": "Cara mengajukan", "blocks": [
     ("steps", [
       ("Sebelum pulang", "Lapor pindah keluar (tenshutsu todoke) di kantor kota", "Laporkan ke kantor kota/kecamatan bahwa Anda akan meninggalkan Jepang. Jika sudah lapor, dokumen bukti tidak punya alamat di Jepang tidak diperlukan.", 2),
       ("Sebelum pulang", "Siapkan dokumen", "Formulir permohonan, fotokopi paspor, dokumen dari bank yang menunjukkan rekening, dan dokumen yang menunjukkan nomor pensiun dasar (kiso nenkin bango tsuchisho atau nenkin techo). Rekening Japan Post Bank (Yucho) tidak bisa dipakai.", 2),
       ("Kirim agar tiba setelah tanggal pindah keluar", "Kirim lewat pos ke Japan Pension Service", "Alamat: Japan Pension Service, Foreign Affairs Group, 3-5-24 Takaido-nishi, Suginami-ku, Tokyo 168-8505, Japan. Boleh dikirim dari Jepang atau dari Indonesia setelah pulang.", 2),
       ("Setelah diperiksa", "Uang ditransfer ke rekening", "Jika dokumen kurang, formulir bisa dikembalikan.", 2),
     ]),
   ]},
   {"h": "Cara meminta kembali pajak (kosei nenkin)", "blocks": [
     ("p", "Dattai ichijikin kosei nenkin dipotong pajak penghasilan 20,42%.<sup><a href=\"#src\">[2]</a></sup> Dengan melapor ke kantor pajak, pajak yang dipotong bisa kembali."),
     ("steps", [
       ("Sebelum pulang", "Tunjuk dan laporkan wakil pajak (nozei kanrinin)", "Minta orang yang tinggal di Jepang untuk mengurus pajak Anda. Serahkan formulir penunjukan wakil pajak ke kantor pajak di daerah tempat tinggal Anda.", 2),
       ("Setelah menerima dattai ichijikin", "Ajukan pengembalian pajak", "Wakil pajak menyerahkan formulir pengembalian pajak (taishoku shotoku no sentaku kazei) ke kantor pajak. Surat pemberitahuan pembayaran dattai ichijikin (asli) diperlukan, jadi kirimkan ke wakil pajak.", 2),
     ]),
   ]},
   {"h": "Yang perlu diketahui sebelum menerima", "blocks": [
     ("warn", "Jika menerima dattai ichijikin, <b>semua masa kepesertaan pensiun Jepang sebelumnya hilang</b>. Jika nanti bekerja lagi di Jepang, masa itu tidak dihitung.<sup><a href=\"#src\">[2]</a></sup>"),
     ("dl", [
       ("Ikut lebih dari 60 bulan", "Yang dibayar maksimal 60 bulan, tetapi seluruh masa kepesertaan hilang.", 2),
       ("Ikut 10 tahun atau lebih", "Tidak bisa mengajukan dattai ichijikin. Anda berhak atas pensiun Jepang.", 2),
       ("Perjanjian dengan Indonesia", "Tidak ada perjanjian jaminan sosial antara Jepang dan Indonesia untuk menggabungkan masa pensiun (per Maret 2026).", 2),
       ("Keluar dengan izin masuk kembali", "Jika keluar Jepang dengan izin masuk kembali tanpa lapor pindah keluar, tidak bisa mengajukan sampai izin itu habis masa berlakunya.", 2),
     ]),
   ]},
   {"h": "Tempat konsultasi", "blocks": [
     ("fact", "Japan Pension Service, Foreign Affairs Group  +81-3-6700-1165", "Bisa bertanya soal prosedur dattai ichijikin. Layanan dalam bahasa Jepang.", 2),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("gaji", "Berapa uang yang benar-benar tersisa di Jepang (kalkulator gaji bersih)"), ("arrival", "Yang harus dilakukan di dua minggu pertama di Jepang"), ("visa", "Perbedaan Tokutei Ginou, magang, dan Ikusei Shuro")])]},
  ]},
}
