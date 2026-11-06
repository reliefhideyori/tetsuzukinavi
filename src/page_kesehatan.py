SLUG = "kesehatan"
S1 = ("医療費の一部負担（自己負担）割合について（厚生労働省）", "https://www.mhlw.go.jp/content/000937919.pdf")
S2 = ("高額療養費（協会けんぽ）", "https://www.kyoukaikenpo.or.jp/benefit/high_cost_medical_expenses/002/index.html")
S3 = ("限度額適用認定証（協会けんぽ）", "https://www.kyoukaikenpo.or.jp/benefit/high_cost_medical_expenses/001/index.html")
PAGE = {
 "sources": [S1, S2, S3],
 "ja": {
  "title": "日本の健康保険と医療費", "crumb_last": "健康保険と医療費",
  "h1": "日本の健康保険：病院でいくら払うか、高いときの上限",
  "lead": "日本で働く人は健康保険に入ります。病院の窓口で払う割合と、医療費が高くなったときに1か月の支払いに上限がある「高額療養費」のしくみを、公式の情報からまとめました。",
  "notice": ("まず知っておくこと", "健康保険に入っていると、病院で払うのは<b>医療費の3割</b>です（6歳〜69歳）。<sup><a href=\"#src\">[1]</a></sup>入院などで高くなっても、<b>1か月に払う金額には上限</b>があります。<sup><a href=\"#src\">[2]</a></sup>"),
  "sections": [
   {"h": "どの保険に入るか", "blocks": [
     ("dl", [
       ("会社の健康保険", "会社で社会保険に入る人。保険料は給料から引かれ、会社も半分払います。多くの中小企業は協会けんぽです", ""),
       ("国民健康保険", "会社の保険に入らない人。住んでいる市区町村の役所で入ります", ""),
     ]),
     ("p", "保険料がいくら引かれるかは、手取り計算機で確かめられます。"),
   ]},
   {"h": "病院で払う割合", "blocks": [
     ("table", ["窓口で払う割合"], [["小学校に入る前", "2割"], ["6歳〜69歳", "3割"]], "出典：[1] 厚生労働省。"),
     ("p", "例えば、医療費が1万円なら、窓口で払うのは3,000円です。"),
   ]},
   {"h": "医療費が高いときの上限（高額療養費）", "blocks": [
     ("p", "1か月に病院で払った金額が上限を超えると、超えた分が戻ります。上限は給料の高さで決まります。<sup><a href=\"#src\">[2]</a></sup>"),
     ("table", ["1か月の上限（2026年8月〜2027年7月）"], [
       ["標準報酬月額26万円以下", "61,500円"],
       ["標準報酬月額28万〜50万円", "85,800円＋（医療費−286,000円）×1%"],
       ["住民税がかからない人", "36,900円"],
     ], "70歳未満、協会けんぽの場合。出典：[2]。直近12か月に3回以上上限に達すると、4回目からは44,400円（住民税がかからない人は24,600円）になります。"),
     ("note", "窓口で上限より多く払わないためには、<b>マイナ保険証</b>（健康保険証として登録したマイナンバーカード）を使います。使えない病院では、先に「限度額適用認定証」を申請して見せます。<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("gaji", "日本で本当に手元に残るお金（手取り計算）"), ("arrival", "日本に着いて最初の2週間にすること"), ("hak", "日本で働く人の権利：残業代・有給・休み")])]},
  ]},
 "id": {
  "title": "Asuransi Kesehatan dan Biaya Berobat di Jepang", "crumb_last": "Asuransi kesehatan",
  "h1": "Asuransi Kesehatan Jepang: Berapa yang Dibayar di Rumah Sakit dan Batas Biayanya",
  "lead": "Pekerja di Jepang ikut asuransi kesehatan. Ringkasan berapa persen yang dibayar di loket rumah sakit dan sistem kogaku ryoyohi, yaitu batas biaya berobat per bulan, dari informasi resmi.",
  "notice": ("Yang perlu diketahui dulu", "Jika ikut asuransi kesehatan, Anda hanya membayar <b>30% dari biaya berobat</b> (usia 6–69 tahun).<sup><a href=\"#src\">[1]</a></sup> Walaupun biaya menjadi mahal, misalnya karena rawat inap, <b>ada batas jumlah yang dibayar per bulan</b>.<sup><a href=\"#src\">[2]</a></sup>"),
  "sections": [
   {"h": "Asuransi apa yang diikuti", "blocks": [
     ("dl", [
       ("Asuransi kesehatan perusahaan", "Untuk yang ikut asuransi sosial (shakai hoken) dari perusahaan. Iuran dipotong dari gaji, dan perusahaan membayar setengahnya. Banyak perusahaan kecil dan menengah memakai Kyokai Kenpo", ""),
       ("Asuransi kesehatan nasional (kokumin kenko hoken)", "Untuk yang tidak ikut asuransi perusahaan. Daftar di kantor kota/kecamatan tempat tinggal", ""),
     ]),
     ("p", "Besarnya potongan iuran bisa dicek dengan kalkulator gaji bersih."),
   ]},
   {"h": "Persentase yang dibayar di rumah sakit", "blocks": [
     ("table", ["Dibayar di loket"], [["Sebelum masuk SD", "20%"], ["6–69 tahun", "30%"]], "Sumber: [1] MHLW."),
     ("p", "Contoh: jika biaya berobat 10.000 yen, yang dibayar di loket 3.000 yen."),
   ]},
   {"h": "Batas biaya per bulan (kogaku ryoyohi)", "blocks": [
     ("p", "Jika jumlah yang dibayar di rumah sakit dalam sebulan melewati batas, kelebihannya dikembalikan. Batasnya ditentukan oleh besarnya gaji.<sup><a href=\"#src\">[2]</a></sup>"),
     ("table", ["Batas per bulan (Agustus 2026–Juli 2027)"], [
       ["Gaji standar bulanan 260.000 yen atau kurang", "61.500 yen"],
       ["Gaji standar bulanan 280.000–500.000 yen", "85.800 yen + (biaya berobat − 286.000 yen) × 1%"],
       ["Tidak dikenai pajak penduduk", "36.900 yen"],
     ], "Untuk usia di bawah 70 tahun, Kyokai Kenpo. Sumber: [2]. Jika mencapai batas 3 kali atau lebih dalam 12 bulan terakhir, mulai kali ke-4 batasnya 44.400 yen (24.600 yen jika tidak dikenai pajak penduduk)."),
     ("note", "Agar tidak membayar lebih dari batas di loket, pakai <b>My Number Card yang didaftarkan sebagai kartu asuransi</b> (maina hokensho). Di rumah sakit yang belum bisa, ajukan dulu sertifikat batas biaya (gendogaku tekiyo ninteisho) lalu tunjukkan.<sup><a href=\"#src\">[3]</a></sup>"),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("gaji", "Kalkulator gaji bersih"), ("arrival", "Dua minggu pertama di Jepang"), ("hak", "Hak pekerja di Jepang: lembur, cuti, dan hari libur")])]},
  ]},
}
