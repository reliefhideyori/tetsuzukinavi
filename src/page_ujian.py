SLUG = "ujian"
S1 = ("特定技能 試験関係（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/ssw/nyuukokukanri01_00135.html")
S3 = ("外国人食品産業技能評価機構（OTAFF）", "https://otaff1.jp/")
S2 = ("国際交流基金日本語基礎テスト（JFT-Basic）", "https://www.jpf.go.jp/jft-basic/")
F = [
 ("介護", "Perawatan lansia (kaigo)", "介護技能評価試験", "厚生労働省", "https://www.mhlw.go.jp/stf/newpage_000117702.html"),
 ("ビルクリーニング", "Pembersihan gedung", "ビルクリーニング分野特定技能１号評価試験", "全国ビルメンテナンス協会", "https://www.j-bma.or.jp/qualification-training/zairyu"),
 ("工業製品製造業", "Manufaktur produk industri", "製造分野特定技能評価試験", "工業製品製造技能人材機構", "https://www.jaim-skill.or.jp/exam/?stt_lang=ja"),
 ("建設", "Konstruksi", "建設分野特定技能１号評価試験", "建設技能人材機構", "https://jac-skill.or.jp/exam/index.php"),
 ("造船・舶用工業", "Pembuatan kapal", "造船・舶用工業分野特定技能１号試験", "日本海事協会", "http://www.classnk.or.jp/hp/ja/authentication/evaluation/index.html"),
 ("自動車整備", "Perawatan mobil", "自動車整備分野特定技能１号評価試験", "日本自動車整備振興会連合会", "https://www.jaspa.or.jp/mechanic/specific-skill/index.html"),
 ("航空", "Penerbangan", "航空分野特定技能評価試験（グランドハンドリング／航空機整備）", "日本航空技術協会", "https://exam.jaea.or.jp/"),
 ("宿泊", "Perhotelan", "宿泊分野特定技能１号評価試験", "宿泊業技能試験センター", "https://caipt.or.jp/"),
 ("自動車運送業", "Transportasi (sopir)", "自動車運送業分野特定技能１号評価試験", "日本海事協会", "https://www.classnk.or.jp/hp/ja/authentication/evaluation/motortransport.html"),
 ("鉄道", "Perkeretaapian", "鉄道分野特定技能１号評価試験", "国土交通省", "https://www.mlit.go.jp/tetudo/tetudo_fr7_000056.html"),
 ("農業", "Pertanian", "１号農業技能測定試験", "全国農業会議所", "http://asat-nca.jp/"),
 ("漁業", "Perikanan", "１号漁業技能測定試験（漁業／養殖業）", "大日本水産会", "https://suisankai.or.jp/skill/"),
 ("飲食料品製造業", "Pengolahan makanan dan minuman", "飲食料品製造業特定技能技能測定試験", "外国人食品産業技能評価機構（OTAFF）", "https://otaff1.jp/"),
 ("外食業", "Restoran (gaishoku)", "外食業特定技能測定試験", "外国人食品産業技能評価機構（OTAFF）", "https://otaff1.jp/"),
 ("林業", "Kehutanan", "林業技能測定試験", "林業技能向上センター", "https://ringyou-gino.org/specific/index.php"),
 ("木材産業", "Industri kayu", "木材産業特定技能１号測定試験", "全国木材組合連合会", "https://www.zenmoku.jp/foreigner/"),
]
def rows(lang):
    i = 0 if lang == "ja" else 1
    return [(f[i], f'{f[2]}<br><small>{f[3]} ・ <a href="{f[4]}">{f[4].split("/")[2]}</a></small>', "") for f in F]
PAGE = {
 "date": "2026-11-06",
 "sources": [S1, S2, S3],
 "ja": {
  "title": "特定技能の分野別 技能試験の一覧", "crumb_last": "分野別の技能試験",
  "h1": "特定技能1号：分野ごとの技能試験と公式サイト",
  "lead": "特定技能1号で働くには、多くの場合、分野ごとの技能試験と日本語の試験に合格します。出入国在留管理庁が載せている試験名と実施団体を、分野ごとにまとめました。",
  "notice": ("まず知っておくこと", "試験は<b>分野ごとに別の団体</b>が行っています。日程や受験できる国は、<b>必ずその団体の公式サイト</b>で確認してください。<sup><a href=\"#src\">[1]</a></sup>"),
  "sections": [
   {"h": "合格が必要な2つの試験", "blocks": [
     ("dl", [
       ("分野の技能試験", "働く分野の仕事ができるかを確かめる試験。下の一覧から選びます", "1"),
       ("日本語の試験", "全分野で国際交流基金日本語基礎テスト（JFT-Basic）、または日本語能力試験（JLPT）N4以上。介護は、これに加えて介護日本語評価試験", "1"),
     ]),
     ("p", "技能実習2号を良好に修了した人は、同じ仕事の分野なら試験が免除されることがあります。"),
   ]},
   {"h": "分野ごとの試験と実施団体", "blocks": [
     ("dl", rows("ja")),
     ("p", "<small>出典：[1] 出入国在留管理庁「試験関係」。2026年11月6日確認。新しく加わった分野は、試験の情報がまだ載っていないことがあります。</small>"),
     ("warn", "外食業の国外試験は、実施団体のサイトで「現在試験を停止しています」と案内されています。<sup><a href=\"#src\">[3]</a></sup>受ける前に必ず最新の案内を見てください。"),
   ]},
   {"h": "試験を受けるときの注意", "blocks": [
     ("steps", [
       ("", "公式サイトで日程を見る", "試験の日程・場所・申込方法は団体ごとに違います。", 1),
       ("", "自分で申し込めるか確かめる", "多くの試験は本人が申し込めます。「試験を受けるために高いお金が必要」と言われたら、公式の受験料と比べてください。"),
       ("", "合格したら会社を探す", "合格だけでは日本に行けません。日本の会社と雇用契約を結び、会社がCOEを申請します。"),
     ]),
   ]},
   {"h": "関連するページ", "blocks": [("related", [("ssw", "特定技能（SSW）とは"), ("test", "JFT-BasicとJLPTの受け方"), ("kaigo", "介護分野の特定技能"), ("coe", "内定からビザまで（COE）")])]},
  ]},
 "id": {
  "title": "Daftar Ujian Keterampilan SSW per Bidang", "crumb_last": "Ujian keterampilan per bidang",
  "h1": "Tokutei Ginou No.1: Ujian Keterampilan per Bidang dan Situs Resminya",
  "lead": "Untuk bekerja dengan Tokutei Ginou No.1, biasanya Anda harus lulus ujian keterampilan bidang kerja dan ujian bahasa Jepang. Nama ujian dan lembaga penyelenggaranya dirangkum per bidang dari situs imigrasi Jepang (ISA).",
  "notice": ("Yang perlu diketahui dulu", "Ujian diadakan oleh <b>lembaga yang berbeda untuk setiap bidang</b>. Jadwal dan negara tempat ujian <b>wajib dicek di situs resmi lembaga itu</b>.<sup><a href=\"#src\">[1]</a></sup>"),
  "sections": [
   {"h": "Dua ujian yang harus lulus", "blocks": [
     ("dl", [
       ("Ujian keterampilan bidang", "Mengecek apakah Anda bisa melakukan pekerjaan di bidang itu. Pilih dari daftar di bawah", "1"),
       ("Ujian bahasa Jepang", "Untuk semua bidang: JFT-Basic dari Japan Foundation, atau JLPT N4 ke atas. Untuk kaigo, ditambah ujian bahasa Jepang perawatan (kaigo nihongo)", "1"),
     ]),
     ("p", "Orang yang menyelesaikan magang (Ginou Jisshu) No.2 dengan baik bisa bebas ujian untuk bidang pekerjaan yang sama."),
   ]},
   {"h": "Ujian dan lembaga per bidang", "blocks": [
     ("dl", rows("id")),
     ("p", "<small>Sumber: [1] ISA, halaman ujian. Dicek 6 November 2026. Nama ujian ditulis dalam bahasa Jepang agar mudah dicari di situs resmi. Bidang yang baru ditambahkan mungkin belum memiliki info ujian.</small>"),
     ("warn", "Untuk bidang restoran (gaishoku), situs lembaga penyelenggara menyebutkan ujian di luar Jepang <b>sedang dihentikan</b>.<sup><a href=\"#src\">[3]</a></sup> Cek pengumuman terbaru sebelum mendaftar."),
   ]},
   {"h": "Hal yang perlu diperhatikan", "blocks": [
     ("steps", [
       ("", "Lihat jadwal di situs resmi", "Jadwal, tempat, dan cara daftar berbeda untuk setiap lembaga.", 1),
       ("", "Cek apakah bisa daftar sendiri", "Banyak ujian bisa didaftar sendiri. Jika dikatakan \"perlu uang banyak untuk ikut ujian\", bandingkan dengan biaya ujian resmi."),
       ("", "Setelah lulus, cari perusahaan", "Lulus ujian saja belum cukup untuk ke Jepang. Anda perlu kontrak kerja dengan perusahaan Jepang, lalu perusahaan mengajukan COE."),
     ]),
   ]},
   {"h": "Halaman terkait", "blocks": [("related", [("ssw", "Apa itu Tokutei Ginou (SSW)"), ("test", "Cara ikut JFT-Basic dan JLPT"), ("kaigo", "Tokutei Ginou bidang kaigo"), ("coe", "Dari tawaran kerja sampai visa (COE)")])]},
  ]},
}
