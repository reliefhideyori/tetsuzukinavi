"""雇用契約書セルフチェック（/ja/kontrak, /id/kontrak）を site/ に書き出す。
入力はブラウザの中だけで計算し、どこにも送らない。結果は「公的なルールの数字との比較」と「会社・LPKに聞く質問」。
順番: python3 build_kontrak.py && python3 finish.py && python3 seo.py"""
import json, os, re, sys, pathlib
D = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(D))
from data import PREFS, RATES
SITE = D.parent / "site"
CHECKED = "2026-11-07"

SRC = [
 ("令和8年度 地域別最低賃金 答申状況（厚生労働省）", "https://www.mhlw.go.jp/content/11302000/001745621.pdf"),
 ("最低賃金額以上かどうかを確認する方法（厚生労働省）", "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/koyou_roudou/roudoukijun/chingin/newpage_43899.html"),
 ("労働基準法（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/law/roudoukijun.html"),
 ("時間外・休日労働と割増賃金（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/study/roudousya_jikangai.html"),
 ("年次有給休暇をとる条件は？（確かめよう労働条件、厚生労働省）", "https://www.check-roudou.mhlw.go.jp/qa/roudousya/yukyu/q1.html"),
 ("特定技能外国人を受け入れる際の注意点（出入国在留管理庁）", "https://www.moj.go.jp/isa/policies/ssw/chuui.html"),
 ("参考様式第1-9号 徴収費用の説明書（出入国在留管理庁）", "https://www.moj.go.jp/isa/content/001372371.pdf"),
 ("外国人技能実習制度について（出入国在留管理庁・厚生労働省、2026年8月14日改訂版）", "https://www.moj.go.jp/isa/content/930005177.pdf"),
 ("新しい在留管理制度 Q&A（出入国在留管理庁）", "https://www.moj.go.jp/isa/publications/faq/newimmiact_4_q-and-a_page2.html"),
 ("外国人労働者向け相談ダイヤル（厚生労働省）", "https://www.mhlw.go.jp/content/001708139.pdf"),
]

# ---------------- 文章 ----------------
T = {
"ja": dict(
 crumb="雇用契約書チェック",
 h1="雇用契約書チェック：サインする前に、自分の契約を確かめる",
 lead="契約書（雇用条件書）に書かれた給料・時間・天引きを入れると、最低賃金や労働時間のルールと比べて、気をつける点と、会社やLPKに聞くべき質問が分かります。",
 privacy="<b>入力した内容は、どこにも送られません。</b>計算はすべてあなたのスマホの中で行います。名前や会社名を入れる場所もありません。",
 notlegal="結果は、あなたが入れた数字を日本の公的なルールと比べたものです。契約が正しいかどうかを判断するものではありません。気になる点は、ページの下の公的な相談先に聞いてください。",
 upd="最終確認日：2026年11月7日　／　出典：厚生労働省・出入国在留管理庁の公式情報（ページの最後に一覧）",
 st1="1. 基本のこと", st2="2. 給料と働く時間", st3="3. 給料から引かれるお金・来日前の費用", st4="4. 契約書に書いてあるか",
 visa="在留資格", v_ssw="特定技能", v_titp="技能実習・育成就労", v_unk="まだ分からない",
 pref="働く都道府県", pref_ph="選んでください", pref_hint="最低賃金は都道府県で違います。",
 pay="給料の決め方", hourly="時給", monthly="月給",
 wage="時給（円）", msal="月給（円）",
 msal_hint="基本給と、毎月決まって払われる手当の合計。残業代・通勤手当・家族手当・皆勤手当は入れません（最低賃金と比べるときに除くお金です）。",
 hours="1日の労働時間（所定労働時間）", hours_hint="休憩時間は入れません。",
 hol="1年の休日の日数（年間休日）", hol_hint="契約書の「休日」の欄に書かれています。分からなければ空けておいてください。",
 ot="残業代の割増率", ot_hint="契約書の「賃金」の欄の「所定時間外」などに書かれています。",
 ot_ge="25%以上", ot_lt="25%より低い", ot_none="書いていない", ot_no="残業なしと書いてある",
 unit_yen="円", unit_h="時間", unit_d="日", unit_rp="ルピア",
 rent="寮費・家賃", util="電気・ガス・水道", food="食費", other="その他の天引き",
 ded_hint="給料から引かれると書かれている金額（1か月）。税金と社会保険料は自動で計算するので入れません。",
 fee="日本に来る前に払うお金の合計（研修費・手数料など）", fee_hint="LPKや送り出し機関に払う、または払うと言われた金額。",
 q_job="働く場所と仕事の内容", q_ded="給料から引かれるものと、その金額", q_lang="自分が読める言語（インドネシア語など）の契約書",
 q_hoken="健康保険と厚生年金に入ること", q_yukyu="有給休暇", q_feelist="来日前の費用の内訳（何にいくら）を書いた紙",
 q_deposit="保証金を預ける、または途中でやめたら違約金・罰金を払う約束がある",
 q_passport="会社やLPKが、パスポートや在留カードを預かると言っている",
 yes="ある", no="ない", unk="分からない", yes2="はい", no2="いいえ",
 run="チェックする", need="都道府県と給料を入れてください。",
 r_h="チェックの結果", r_red="すぐ確認", r_yel="聞いた方がいい", r_ok="ルールの数字を満たす",
 r_money="お金のまとめ（1か月の目安）",
 m_hourly="時給に直すと", m_minw="最低賃金", m_gross="給料（残業なし）", m_social="社会保険料・税金（1年目）", m_ded="契約書の天引き", m_left="毎月残るお金", m_fee="来日前の費用", m_months="毎月残るお金の約{x}か月分",
 q_h="会社・LPKに聞く質問", q_lead="次の質問を、サインする前に会社やLPKに送ってください。答えは書面（メッセージやメール）でもらうと安心です。",
 q_copy="質問をコピー", q_copied="コピーしました", q_wa="WhatsAppで送る", q_none="特に聞くことはありません。それでも、分からない言葉があればサインする前に聞いてください。",
 share_res="結果をWhatsAppで送る",
 again="入力を直すと、結果もすぐ変わります。",
 how_h="このチェックで分かること・分からないこと",
 how_p="<p>分かること：給料が最低賃金より高いか、労働時間と休日が法律の基本の数字に合っているか、残業の割増率、天引きのあとに残るお金、来日前の費用が何か月分の給料にあたるか、契約書に書かれているべきことが書かれているか。</p><p>分からないこと：会社やLPKが信頼できるか、契約書に書かれていないこと、日本人と同じ仕事での給料との比較。これらは公的な相談先に聞いてください。</p>",
 help_h="相談先",
 help=[("外国人労働者向け相談ダイヤル（厚生労働省）", "0570001715", "0570-001-715", "インドネシア語：火曜・木曜 10:00〜15:00（12:00〜13:00を除く）。給料や労働条件の相談ができます。無料ですが通話料がかかります。"),
       ("外国人技能実習機構（OTIT）母国語相談", "", "", "技能実習生は、インドネシア語で相談できます。<a href=\"https://www.support.otit.go.jp/soudan/id/\">公式ページ</a>")],
 help_note="日本に来る前の契約やLPKのことは、インドネシアの政府機関（BP2MI／P2MI省）にも確認してください。",
 rel_h="関連するページ", rel=[("gaji", "手取り計算機（くわしい計算）"), ("lpk", "LPK・仲介業者を選ぶ前に"), ("hak", "日本で働く人の権利"), ("visa", "特定技能・技能実習・育成就労の違い")],
 tr_h="この情報について", tr_money="<b>このサイトの収入は広告だけです。</b>LPK、仲介業者、会社から紹介料は受け取っていません。メール登録や有料相談もありません。",
 tr_src="出典（確認日）", tr_log="変更履歴", log="2026年11月7日　第1版を公開。", fix="間違いを見つけたら教えてください",
 gaji_btn="自分の契約書でチェックする",
),
"id": dict(
 crumb="Cek kontrak kerja",
 h1="Cek Kontrak Kerja Jepang: Periksa Kontrak Anda Sebelum Tanda Tangan",
 lead="Masukkan gaji, jam kerja, dan potongan yang tertulis di kontrak (koyo joken sho). Hasilnya dibandingkan dengan aturan upah minimum dan jam kerja Jepang, lalu muncul hal yang perlu diwaspadai serta pertanyaan untuk perusahaan atau LPK.",
 privacy="<b>Data yang Anda masukkan tidak dikirim ke mana pun.</b> Semua perhitungan dilakukan di HP Anda. Tidak ada kolom untuk nama atau nama perusahaan.",
 notlegal="Hasil ini membandingkan angka yang Anda masukkan dengan aturan resmi Jepang. Ini bukan penilaian apakah kontrak Anda sah atau tidak. Jika ada yang mengkhawatirkan, tanyakan ke tempat konsultasi resmi di bagian bawah halaman.",
 upd="Terakhir dicek: 7 November 2026  /  Sumber: informasi resmi Kementerian Kesehatan, Tenaga Kerja, dan Kesejahteraan Jepang (MHLW) dan Badan Imigrasi Jepang (ISA) (daftar di bagian bawah)",
 st1="1. Hal dasar", st2="2. Gaji dan jam kerja", st3="3. Potongan gaji dan biaya sebelum berangkat", st4="4. Apakah tertulis di kontrak?",
 visa="Status izin tinggal", v_ssw="Tokutei Ginou (SSW)", v_titp="Magang / Ikusei Shuro", v_unk="Belum tahu",
 pref="Prefektur tempat bekerja", pref_ph="Pilih prefektur", pref_hint="Upah minimum berbeda tiap prefektur.",
 pay="Cara gaji ditentukan", hourly="Per jam", monthly="Per bulan",
 wage="Upah per jam (yen)", msal="Gaji per bulan (yen)",
 msal_hint="Gaji pokok ditambah tunjangan yang dibayar tetap setiap bulan. Jangan masukkan upah lembur, tunjangan transportasi, tunjangan keluarga, atau tunjangan kehadiran (uang ini tidak dihitung saat dibandingkan dengan upah minimum).",
 hours="Jam kerja per hari (sesuai kontrak)", hours_hint="Tidak termasuk jam istirahat.",
 hol="Jumlah hari libur dalam setahun", hol_hint="Tertulis di bagian \"hari libur\" pada kontrak. Jika tidak tahu, kosongkan saja.",
 ot="Tambahan upah lembur", ot_hint="Tertulis di bagian \"upah\" pada kontrak, misalnya \"di luar jam kerja yang ditetapkan\".",
 ot_ge="25% atau lebih", ot_lt="Kurang dari 25%", ot_none="Tidak tertulis", ot_no="Tertulis tidak ada lembur",
 unit_yen="yen", unit_h="jam", unit_d="hari", unit_rp="rupiah",
 rent="Asrama / sewa", util="Listrik, gas, air", food="Makan", other="Potongan lain",
 ded_hint="Jumlah per bulan yang menurut kontrak akan dipotong dari gaji. Pajak dan asuransi sosial dihitung otomatis, jadi tidak perlu dimasukkan.",
 fee="Total biaya sebelum berangkat (biaya pelatihan, biaya agen, dll.)", fee_hint="Jumlah yang dibayar, atau diminta untuk dibayar, ke LPK atau lembaga pengirim.",
 q_job="Tempat kerja dan jenis pekerjaan", q_ded="Potongan gaji beserta jumlahnya", q_lang="Kontrak dalam bahasa yang Anda pahami (misalnya bahasa Indonesia)",
 q_hoken="Ikut asuransi kesehatan dan pensiun karyawan (kosei nenkin)", q_yukyu="Cuti tahunan berbayar (yukyu)", q_feelist="Dokumen rincian biaya sebelum berangkat (untuk apa dan berapa)",
 q_deposit="Ada perjanjian menitipkan uang jaminan, atau membayar denda/penalti jika berhenti di tengah jalan",
 q_passport="Perusahaan atau LPK mengatakan akan menyimpan paspor atau zairyu card Anda",
 yes="Ada", no="Tidak ada", unk="Tidak tahu", yes2="Ya", no2="Tidak",
 run="Cek sekarang", need="Isi prefektur dan gaji terlebih dahulu.",
 r_h="Hasil pengecekan", r_red="Segera cek", r_yel="Sebaiknya ditanyakan", r_ok="Sesuai angka aturan",
 r_money="Ringkasan uang (perkiraan per bulan)",
 m_hourly="Jika dihitung per jam", m_minw="Upah minimum", m_gross="Gaji (tanpa lembur)", m_social="Asuransi sosial dan pajak (tahun pertama)", m_ded="Potongan di kontrak", m_left="Uang tersisa per bulan", m_fee="Biaya sebelum berangkat", m_months="setara sekitar {x} bulan uang tersisa",
 q_h="Pertanyaan untuk perusahaan atau LPK", q_lead="Kirim pertanyaan berikut ke perusahaan atau LPK sebelum tanda tangan. Lebih aman jika jawabannya diterima secara tertulis (pesan atau email). Setiap pertanyaan juga ditulis dalam bahasa Jepang agar bisa ditunjukkan ke perusahaan di Jepang.",
 q_copy="Salin pertanyaan", q_copied="Sudah disalin", q_wa="Kirim lewat WhatsApp", q_none="Tidak ada hal khusus yang perlu ditanyakan. Tetap tanyakan jika ada kata yang tidak Anda pahami sebelum tanda tangan.",
 share_res="Kirim hasil lewat WhatsApp",
 again="Jika isian diubah, hasilnya langsung ikut berubah.",
 how_h="Apa yang bisa dan tidak bisa dicek",
 how_p="<p>Yang bisa dicek: apakah gaji lebih tinggi daripada upah minimum, apakah jam kerja dan hari libur sesuai angka dasar dalam hukum, tambahan upah lembur, sisa uang setelah potongan, biaya sebelum berangkat setara berapa bulan gaji, dan apakah hal yang wajib tertulis sudah ada di kontrak.</p><p>Yang tidak bisa dicek: apakah perusahaan atau LPK bisa dipercaya, hal yang tidak tertulis di kontrak, dan perbandingan dengan gaji orang Jepang untuk pekerjaan yang sama. Tanyakan hal ini ke tempat konsultasi resmi.</p>",
 help_h="Tempat konsultasi",
 help=[("Layanan Konsultasi untuk Pekerja Asing (MHLW)", "0570001715", "0570-001-715", "Bahasa Indonesia: Selasa dan Kamis 10.00–15.00 (kecuali 12.00–13.00). Bisa konsultasi soal gaji dan syarat kerja. Layanannya gratis, tetapi Anda tetap membayar biaya telepon."),
       ("Konsultasi bahasa ibu OTIT (Organisasi Pelatihan Teknis Pekerja Asing)", "", "", "Peserta magang bisa berkonsultasi dalam bahasa Indonesia. <a href=\"https://www.support.otit.go.jp/soudan/id/\">Halaman resmi</a>")],
 help_note="Untuk kontrak atau LPK sebelum berangkat, tanyakan juga ke lembaga pemerintah Indonesia (BP2MI / Kementerian P2MI).",
 rel_h="Halaman terkait", rel=[("gaji", "Kalkulator gaji bersih (perhitungan lengkap)"), ("lpk", "Sebelum memilih LPK atau agen"), ("hak", "Hak pekerja di Jepang"), ("visa", "Perbedaan SSW, magang, dan Ikusei Shuro")],
 tr_h="Tentang informasi ini", tr_money="<b>Pendapatan situs ini hanya dari iklan.</b> Kami tidak menerima komisi dari LPK, agen, atau perusahaan. Tidak ada pendaftaran email atau konsultasi berbayar.",
 tr_src="Sumber (tanggal dicek)", tr_log="Riwayat perubahan", log="7 November 2026  Versi 1 diterbitkan.", fix="Laporkan jika ada kesalahan",
 gaji_btn="Cek kontrak kerja Anda sendiri",
),
}

# ---------------- 結果の文（JS に渡す） ----------------
# {x} はJSで置き換える。q_ja は会社に見せる日本語、q は読者の言語の質問。
R = {
"ja": {
 "minw_red": ("時給に直すと約{h}円で、{p}の最低賃金{w}円（{d}から）より低くなっています", "最低賃金は国籍に関係なく、日本で働くすべての人に適用されます。<sup><a href=\"#src\">[1]</a></sup>月給の場合は、月給を1か月の平均の労働時間で割って比べます。<sup><a href=\"#src\">[2]</a></sup>"),
 "minw_yel": ("時給に直すと約{h}円で、{p}の最低賃金{w}円とほぼ同じです", "最低賃金は毎年秋ごろに上がります。上がったときに給料も上がるか、聞いておきましょう。<sup><a href=\"#src\">[1]</a></sup>"),
 "minw_ok": ("時給に直すと約{h}円で、{p}の最低賃金{w}円より{x}円高いです", "特定技能では、同じ仕事をする日本人と同じ以上の給料であることも条件です。<sup><a href=\"#src\">[6]</a></sup>"),
 "minw_note": "1年の休日が空いているので、月給は、1日の時間×1か月の平均の労働日数（約21日）で時給に直しています。",
 "hol_red": ("休日が1年で{x}日しかありません", "法律では、毎週少なくとも1日（または4週間で4日以上）の休日が必要です。<sup><a href=\"#src\">[3]</a></sup>"),
 "week_yel": ("1週間の平均の労働時間が約{x}時間で、40時間を超えています", "労働時間は原則1日8時間・1週40時間までです。<sup><a href=\"#src\">[3]</a></sup>「変形労働時間制」という決まりがあれば認められることがありますが、契約書に書かれているか確認してください。"),
 "day_yel": ("1日の労働時間が{x}時間で、8時間を超えています", "1日8時間を超えた分は、原則として残業（25%以上の割増）になります。<sup><a href=\"#src\">[4]</a></sup>「変形労働時間制」が書かれているか確認してください。"),
 "time_ok": ("労働時間と休日は、法律の基本の数字に合っています", "1日8時間・1週40時間まで、休日は毎週1日以上が基本です。<sup><a href=\"#src\">[3]</a></sup>"),
 "hol_unk": ("年間休日が分かりません", "休日の日数は、契約書に書かれているべきことです。<sup><a href=\"#src\">[3]</a></sup>何日あるか聞きましょう。"),
 "ot_red": ("残業代の割増率が25%より低くなっています", "1日8時間・1週40時間を超えた残業には、25%以上の割増賃金が必要です。<sup><a href=\"#src\">[4]</a></sup>"),
 "ot_yel": ("残業代の割増率が書かれていません", "残業には25%以上の割増賃金が必要です。<sup><a href=\"#src\">[4]</a></sup>割増率と、残業がどれくらいあるかを聞きましょう。"),
 "ot_ok": ("残業代の割増率は25%以上です", "深夜（22時〜5時）も25%以上、法定の休日は35%以上です。<sup><a href=\"#src\">[4]</a></sup>"),
 "ot_no": ("残業なしと書かれています", "もし残業をしたら、25%以上の割増賃金が払われます。<sup><a href=\"#src\">[4]</a></sup>"),
 "left_red": ("天引きのあと、手元にお金が残りません（毎月{x}）", "給料から引かれるお金が多すぎます。寮費などの金額と、その理由を聞いてください。"),
 "ded_yel": ("天引きの金額が書面で確かめられていません", "給料は全額を払うのが原則で、税金と社会保険料のほかに引けるのは、会社と働く人の代表が書面で約束したものだけです。<sup><a href=\"#src\">[3]</a></sup>"),
 "ded_ssw": "特定技能では、会社が食費や居住費などを本人から取るときに使う「徴収費用の説明書」という様式があります。<sup><a href=\"#src\">[7]</a></sup>見せてもらえるか聞きましょう。",
 "ded_ok": ("天引きのあと、毎月約{x}が残ります", "社会保険料と税金は1年目の目安です。2年目の6月から住民税が始まり、少し減ります。"),
 "fee_yel": ("来日前の費用は、毎月残るお金の約{x}か月分です", "借金をして払う場合は、返し終わるまでの期間も考えてください。何にいくらかかるのか、内訳を書面でもらいましょう。"),
 "fee_ok": ("来日前の費用は、毎月残るお金の約{x}か月分です", "何にいくらかかるのか、内訳と領収書をもらっておきましょう。"),
 "fee_ssw": "特定技能では、インドネシアの送り出し機関（P3MI）を通すことは必須ではありません。<a href=\"/ja/lpk\">くわしく</a>",
 "feelist_yel": ("来日前の費用の内訳をもらっていません", "研修費・手数料などが何のためのお金か、書面で確かめてからお金を払いましょう。"),
 "dep_red": ("保証金・違約金の約束があります", "特定技能で受け入れる会社は、保証金を取ること、違約金の契約を結ぶことが認められていません。<sup><a href=\"#src\">[6]</a></sup>技能実習でも、違約金を決めることは法律で禁止されています。<sup><a href=\"#src\">[8]</a></sup>サインする前に相談してください。"),
 "dep_yel": ("保証金・違約金があるか分かりません", "特定技能でも技能実習でも、保証金や違約金は認められていません。<sup><a href=\"#src\">[6][8]</a></sup>ないことを書面で確かめましょう。"),
 "pass_red": ("パスポートや在留カードを預かると言われています", "技能実習では、本人の意思に反してパスポートや在留カードを預かることは法律で禁止されています。<sup><a href=\"#src\">[8]</a></sup>在留カードは、本人がいつも持ち歩く義務があります。<sup><a href=\"#src\">[9]</a></sup>"),
 "job_yel": ("働く場所と仕事の内容が確かめられていません", "会社は、働く場所、仕事の内容、給料、労働時間、休日などを書面で示さなければいけません。<sup><a href=\"#src\">[3]</a></sup>"),
 "lang_yel": ("自分が読める言語の契約書がありません", "分からない言葉があるままサインしないでください。インドネシア語の契約書をもらえるか聞きましょう。"),
 "hoken_yel": ("健康保険と厚生年金に入るか確かめられていません", "会社員は健康保険と厚生年金に入り、病院で払うお金は3割になります。厚生年金は帰国するときに一部が戻ります（脱退一時金）。"),
 "yukyu_yel": ("有給休暇が確かめられていません", "6か月続けて働き、8割以上出勤すると、10日の有給休暇がもらえます。<sup><a href=\"#src\">[5]</a></sup>"),
 "ok_list": ("書かれていることを確かめた項目", ""),
},
"id": {
 "minw_red": ("Jika dihitung per jam, sekitar {h} yen. Ini lebih rendah daripada upah minimum {p} sebesar {w} yen (berlaku mulai {d})", "Upah minimum berlaku untuk semua orang yang bekerja di Jepang, apa pun kewarganegaraannya.<sup><a href=\"#src\">[1]</a></sup> Untuk gaji bulanan, gaji dibagi dengan rata-rata jam kerja per bulan, lalu dibandingkan.<sup><a href=\"#src\">[2]</a></sup>"),
 "minw_yel": ("Jika dihitung per jam, sekitar {h} yen. Hampir sama dengan upah minimum {p} sebesar {w} yen", "Upah minimum naik setiap tahun sekitar musim gugur. Tanyakan apakah gaji Anda juga akan naik saat itu.<sup><a href=\"#src\">[1]</a></sup>"),
 "minw_ok": ("Jika dihitung per jam, sekitar {h} yen. Lebih tinggi {x} yen daripada upah minimum {p} sebesar {w} yen", "Untuk Tokutei Ginou, gaji juga harus sama atau lebih tinggi daripada gaji orang Jepang yang melakukan pekerjaan yang sama.<sup><a href=\"#src\">[6]</a></sup>"),
 "minw_note": "Karena jumlah hari libur dikosongkan, gaji bulanan diubah menjadi upah per jam dengan membaginya dengan jam kerja per hari × rata-rata hari kerja per bulan (sekitar 21 hari).",
 "hol_red": ("Hari libur hanya {x} hari dalam setahun", "Menurut hukum, harus ada minimal 1 hari libur setiap minggu (atau minimal 4 hari dalam 4 minggu).<sup><a href=\"#src\">[3]</a></sup>"),
 "week_yel": ("Rata-rata jam kerja per minggu sekitar {x} jam, lebih dari 40 jam", "Pada dasarnya jam kerja maksimal 8 jam sehari dan 40 jam seminggu.<sup><a href=\"#src\">[3]</a></sup> Bisa diizinkan jika ada sistem \"jam kerja variabel\" (henkei rodo jikan sei), tetapi cek apakah hal itu tertulis di kontrak."),
 "day_yel": ("Jam kerja per hari {x} jam, lebih dari 8 jam", "Kelebihan dari 8 jam sehari pada dasarnya dihitung sebagai lembur (tambahan minimal 25%).<sup><a href=\"#src\">[4]</a></sup> Cek apakah ada sistem \"jam kerja variabel\" (henkei rodo jikan sei) di kontrak."),
 "time_ok": ("Jam kerja dan hari libur sesuai angka dasar dalam hukum", "Pada dasarnya maksimal 8 jam sehari dan 40 jam seminggu, dengan minimal 1 hari libur setiap minggu.<sup><a href=\"#src\">[3]</a></sup>"),
 "hol_unk": ("Jumlah hari libur belum diketahui", "Jumlah hari libur adalah hal yang harus tertulis di kontrak.<sup><a href=\"#src\">[3]</a></sup> Tanyakan berapa harinya."),
 "ot_red": ("Tambahan upah lembur kurang dari 25%", "Lembur di atas 8 jam sehari atau 40 jam seminggu harus dibayar dengan tambahan minimal 25%.<sup><a href=\"#src\">[4]</a></sup>"),
 "ot_yel": ("Tambahan upah lembur tidak tertulis", "Lembur harus dibayar dengan tambahan minimal 25%.<sup><a href=\"#src\">[4]</a></sup> Tanyakan berapa persen tambahannya dan seberapa sering ada lembur."),
 "ot_ok": ("Tambahan upah lembur 25% atau lebih", "Kerja malam (22.00–05.00) juga minimal 25%, dan kerja pada hari libur wajib mingguan (hotei kyujitsu) minimal 35%.<sup><a href=\"#src\">[4]</a></sup>"),
 "ot_no": ("Tertulis tidak ada lembur", "Jika ternyata ada lembur, Anda harus dibayar dengan tambahan minimal 25%.<sup><a href=\"#src\">[4]</a></sup>"),
 "left_red": ("Setelah potongan, tidak ada uang yang tersisa (per bulan {x})", "Potongan dari gaji terlalu besar. Tanyakan jumlah biaya asrama dan lainnya serta alasannya."),
 "ded_yel": ("Jumlah potongan gaji belum dipastikan secara tertulis", "Pada prinsipnya gaji harus dibayar penuh. Selain pajak dan asuransi sosial, perusahaan hanya boleh memotong potongan yang disepakati secara tertulis antara perusahaan dan perwakilan pekerja.<sup><a href=\"#src\">[3]</a></sup>"),
 "ded_ssw": "Untuk Tokutei Ginou, ada formulir \"penjelasan biaya yang dipungut\" (choshu hiyo no setsumeisho) yang dipakai perusahaan saat memungut biaya makan, tempat tinggal, dan lainnya dari pekerja.<sup><a href=\"#src\">[7]</a></sup> Tanyakan apakah Anda bisa melihatnya.",
 "ded_ok": ("Setelah potongan, tersisa sekitar {x} per bulan", "Asuransi sosial dan pajak adalah perkiraan tahun pertama. Sejak Juni tahun kedua, pajak penduduk (juminzei) juga dipotong, jadi sisa uang sedikit berkurang."),
 "fee_yel": ("Biaya sebelum berangkat setara sekitar {x} bulan uang tersisa", "Jika Anda berutang untuk membayarnya, pikirkan juga berapa lama sampai lunas. Minta rincian tertulis: untuk apa dan berapa."),
 "fee_ok": ("Biaya sebelum berangkat setara sekitar {x} bulan uang tersisa", "Simpan rincian biaya dan kuitansinya."),
 "fee_ssw": "Untuk Tokutei Ginou (SSW), lewat lembaga pengirim Indonesia (P3MI) tidak wajib. <a href=\"/id/lpk\">Selengkapnya</a>",
 "feelist_yel": ("Belum menerima rincian biaya sebelum berangkat", "Pastikan secara tertulis untuk apa biaya pelatihan, biaya agen, dan lainnya, sebelum membayar."),
 "dep_red": ("Ada perjanjian uang jaminan atau denda", "Perusahaan penerima Tokutei Ginou tidak diperbolehkan memungut uang jaminan atau membuat perjanjian denda.<sup><a href=\"#src\">[6]</a></sup> Untuk magang, menetapkan denda juga dilarang oleh hukum.<sup><a href=\"#src\">[8]</a></sup> Konsultasikan sebelum tanda tangan."),
 "dep_yel": ("Belum tahu apakah ada uang jaminan atau denda", "Untuk Tokutei Ginou maupun magang, uang jaminan dan denda tidak diperbolehkan.<sup><a href=\"#src\">[6][8]</a></sup> Pastikan secara tertulis bahwa hal itu tidak ada."),
 "pass_red": ("Anda diberi tahu bahwa paspor atau zairyu card akan disimpan", "Untuk magang, menyimpan paspor atau zairyu card tanpa persetujuan pemiliknya dilarang oleh hukum.<sup><a href=\"#src\">[8]</a></sup> Zairyu card wajib selalu dibawa oleh pemiliknya sendiri.<sup><a href=\"#src\">[9]</a></sup>"),
 "job_yel": ("Tempat kerja dan jenis pekerjaan belum dipastikan", "Perusahaan wajib memberikan secara tertulis tempat kerja, jenis pekerjaan, gaji, jam kerja, hari libur, dan lainnya.<sup><a href=\"#src\">[3]</a></sup>"),
 "lang_yel": ("Tidak ada kontrak dalam bahasa yang Anda pahami", "Jangan tanda tangan jika masih ada kata yang tidak dipahami. Tanyakan apakah Anda bisa mendapat kontrak dalam bahasa Indonesia."),
 "hoken_yel": ("Belum dipastikan ikut asuransi kesehatan dan pensiun karyawan", "Karyawan perusahaan ikut asuransi kesehatan dan pensiun karyawan (kosei nenkin), sehingga hanya membayar 30% biaya berobat. Sebagian iuran pensiun bisa kembali saat pulang (dattai ichijikin)."),
 "yukyu_yel": ("Cuti tahunan berbayar belum dipastikan", "Jika bekerja terus-menerus 6 bulan dan hadir 80% atau lebih, Anda mendapat 10 hari cuti tahunan berbayar.<sup><a href=\"#src\">[5]</a></sup>"),
 "ok_list": ("Hal yang sudah dipastikan tertulis", ""),
},
}
# 会社に見せる日本語の質問と、その読者向けの訳
Q = {
 "minw": ("給料は{p}の最低賃金（{w}円）以上ですか。時給に直すといくらですか。", "Apakah gaji saya sama dengan atau lebih tinggi daripada upah minimum {p} ({w} yen)? Berapa jika dihitung per jam?"),
 "minw_up": ("最低賃金が上がったときは、給料も上がりますか。", "Jika upah minimum naik, apakah gaji saya juga naik?"),
 "time": ("1日の労働時間と1年の休日の日数を教えてください。変形労働時間制ですか。", "Berapa jam kerja per hari dan berapa hari libur dalam setahun? Apakah memakai sistem jam kerja variabel (henkei rodo jikan sei)?"),
 "ot": ("残業代の割増率は何％ですか。残業は1か月に何時間くらいありますか。", "Berapa persen tambahan upah lembur? Kira-kira berapa jam lembur dalam sebulan?"),
 "ded": ("給料から引かれるもの（寮費・光熱費・食費など）の金額と、その理由を書面で教えてください。", "Tolong beri tahu secara tertulis jumlah potongan gaji (asrama, listrik/air, makan, dll.) dan alasannya."),
 "ded_ssw": ("「徴収費用の説明書」を見せてください。", "Bolehkah saya melihat \"penjelasan biaya yang dipungut\" (choshu hiyo no setsumeisho)?"),
 "fee": ("日本に来る前に払うお金の内訳（何にいくら）を書面でください。", "Tolong berikan rincian tertulis biaya sebelum berangkat: untuk apa dan berapa."),
 "dep": ("保証金や、途中でやめたときの違約金・罰金はありますか。ないことを書面で確認させてください。", "Apakah ada uang jaminan, atau denda/penalti jika saya berhenti di tengah jalan? Tolong pastikan secara tertulis bahwa itu tidak ada."),
 "pass": ("パスポートと在留カードは、自分で持っていてもいいですか。", "Bolehkah saya menyimpan paspor dan zairyu card saya sendiri?"),
 "job": ("働く場所（住所）と仕事の内容を教えてください。", "Tolong beri tahu alamat tempat kerja dan jenis pekerjaannya."),
 "lang": ("インドネシア語の雇用契約書（雇用条件書）をもらえますか。", "Bisakah saya mendapat kontrak kerja (koyo joken sho) dalam bahasa Indonesia?"),
 "hoken": ("健康保険と厚生年金に入りますか。", "Apakah saya ikut asuransi kesehatan dan pensiun karyawan (kosei nenkin)?"),
 "yukyu": ("有給休暇は何日ありますか。", "Berapa hari cuti tahunan berbayar (yukyu) yang saya dapat?"),
}
SHARE_TXT = {
 "ja": ("手続きナビの雇用契約書チェック", "すぐ確認", "聞いた方がいい", "毎月残るお金", "自分の契約書でもチェックできます："),
 "id": ("Cek kontrak kerja di Tetsuzuki Navi", "Segera cek", "Sebaiknya ditanyakan", "Uang tersisa per bulan", "Cek kontrak Anda sendiri di sini:"),
}

CSS = """<style>
:root{--warn:#8a5a00;--warn-bg:#fdf5e1}@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--warn:#f0c05a;--warn-bg:#2b2412}}
.kc .step{border:1px solid var(--line);border-radius:var(--r);padding:var(--s5);margin-bottom:var(--s4)}
.kc .step h2{font-size:17px;margin:0 0 var(--s5);padding:0 0 var(--s3)}
.seg3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--s2)}
.seg3 button,.seg2 button,.seg4 button{min-height:48px;border:1px solid var(--line-strong);border-radius:var(--r);background:var(--bg);padding:var(--s2);cursor:pointer;font-size:14px;line-height:1.4}
.seg2{display:grid;grid-template-columns:1fr 1fr;gap:var(--s2)}
.seg4{display:grid;grid-template-columns:1fr 1fr;gap:var(--s2)}
.seg3 button[aria-pressed=true],.seg2 button[aria-pressed=true],.seg4 button[aria-pressed=true]{border:2px solid var(--key);background:var(--key-bg);font-weight:700;color:var(--key)}
.yn{padding:var(--s4) 0;border-top:1px solid var(--line)}.yn:first-of-type{border-top:0;padding-top:0}
.yn p{font-weight:700;margin:0 0 var(--s2);font-size:15px}
.run{width:100%;min-height:56px;border:0;border-radius:var(--r);background:var(--key);color:var(--key-fg);font-weight:700;font-size:17px;cursor:pointer;margin-top:var(--s2)}
.run:hover{background:var(--key-hover)}
.need{display:none;color:var(--error);font-weight:700;margin-top:var(--s3)}.need.show{display:block}
#out{display:none;margin-top:var(--s8)}#out.show{display:block}
.sum3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:var(--s2);margin-bottom:var(--s6)}
.sum3 div{border-radius:var(--r);padding:var(--s3);text-align:center;background:var(--bg-sub)}
.sum3 b{display:block;font-size:28px;line-height:1.2;font-variant-numeric:tabular-nums}
.sum3 span{font-size:12px;line-height:1.4;display:block}
.sum3 .r{background:var(--error-bg)}.sum3 .r b{color:var(--error)}
.sum3 .y{background:var(--warn-bg)}.sum3 .y b{color:var(--warn)}
.sum3 .g{background:var(--key-bg)}.sum3 .g b{color:var(--key)}
.items{list-style:none;padding:0;margin:0 0 var(--s8)}
.items li{position:relative;padding:var(--s4) 0 var(--s4) var(--s8);border-bottom:1px solid var(--line);margin:0}
.items li::before{content:"";position:absolute;left:2px;top:22px;width:16px;height:16px;border-radius:50%}
.items li.r::before{background:var(--error)}.items li.y::before{background:var(--warn)}.items li.g::before{background:var(--key)}
.items b{display:block;line-height:1.6}.items p{font-size:14px;color:var(--fg-sub);margin:var(--s1) 0 0}
.items .tag{font-size:12px;font-weight:700;margin-right:var(--s2)}.items li.r .tag{color:var(--error)}.items li.y .tag{color:var(--warn)}.items li.g .tag{color:var(--key)}
.qs{counter-reset:q;list-style:none;padding:0;margin:0 0 var(--s4)}
.qs li{counter-increment:q;position:relative;padding:var(--s3) 0 var(--s3) var(--s8);border-bottom:1px solid var(--line);margin:0}
.qs li::before{content:counter(q);position:absolute;left:0;top:var(--s3);width:24px;height:24px;border-radius:50%;background:var(--key);color:var(--key-fg);font-size:13px;font-weight:700;text-align:center;line-height:24px}
.qs .jp{display:block;font-size:14px;color:var(--fg-sub);margin-top:var(--s1)}
.acts{display:flex;flex-wrap:wrap;gap:var(--s2);margin-bottom:var(--s6)}
.acts button,.acts a{display:inline-flex;align-items:center;min-height:48px;padding:0 var(--s4);border:1px solid var(--key);border-radius:var(--r);background:var(--bg);color:var(--key);font-weight:700;text-decoration:none;font-size:14px;cursor:pointer}
.acts .pri{background:var(--key);color:var(--key-fg)}
#money td.n{white-space:normal;text-align:right}#money th{font-weight:400}
.priv{display:flex;gap:var(--s3);align-items:flex-start}.priv svg{width:24px;height:24px;flex:none;fill:var(--key);margin-top:2px}
</style>"""
LOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a5 5 0 0 0-5 5v3H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8a2 2 0 0 0-2-2h-1V7a5 5 0 0 0-5-5zm-3 8V7a3 3 0 1 1 6 0v3H9z"/></svg>'

def seg(cls, name, opts, default=None):
    b = "".join(f'<button type="button" data-v="{v}" aria-pressed="{"true" if v == default else "false"}">{t}</button>' for v, t in opts)
    return f'<div class="{cls}" data-k="{name}" role="group">{b}</div>'

def num(id_, label, unit, hint="", val="", ph=""):
    h = f'<p class="hint">{hint}</p>' if hint else ""
    return (f'<div class="field"><label for="{id_}">{label}</label>{h}<div class="unit"><input type="number" inputmode="numeric" id="{id_}" min="0" value="{val}" placeholder="{ph}"><span>{unit}</span></div></div>')

def main(lang):
    c = T[lang]; L = lambda s: f"/{lang}/{s}"
    prefs = "".join(f'<option value="{i}">{p[0] if lang == "ja" else p[1]}</option>' for i, p in enumerate(PREFS))
    yn3 = lambda k, label: f'<div class="yn"><p>{label}</p>{seg("seg3", k, [("y", c["yes"]), ("n", c["no"]), ("u", c["unk"])])}</div>'
    yn2 = lambda k, label: f'<div class="yn"><p>{label}</p>{seg("seg2", k, [("y", c["yes2"]), ("n", c["no2"])], "n")}</div>'
    form = f'''<form class="kc" id="kc" onsubmit="return false">
<div class="step"><h2>{c["st1"]}</h2>
 <fieldset><legend>{c["visa"]}</legend>{seg("seg3", "visa", [("ssw", c["v_ssw"]), ("titp", c["v_titp"]), ("unk", c["v_unk"])], "ssw")}</fieldset>
 <div class="field"><label for="pref">{c["pref"]}</label><p class="hint">{c["pref_hint"]}</p><select id="pref"><option value="">{c["pref_ph"]}</option>{prefs}</select></div>
</div>
<div class="step"><h2>{c["st2"]}</h2>
 <fieldset><legend>{c["pay"]}</legend>{seg("seg2", "mode", [("m", c["monthly"]), ("h", c["hourly"])], "m")}</fieldset>
 <div id="f-msal">{num("msal", c["msal"], c["unit_yen"], c["msal_hint"])}</div>
 <div id="f-wage" hidden>{num("wage", c["wage"], c["unit_yen"])}</div>
 <div class="grid2">{num("hours", c["hours"], c["unit_h"], c["hours_hint"], "8")}{num("hol", c["hol"], c["unit_d"], c["hol_hint"])}</div>
 <fieldset><legend>{c["ot"]}</legend><p class="hint small">{c["ot_hint"]}</p>{seg("seg4", "ot", [("ge", c["ot_ge"]), ("lt", c["ot_lt"]), ("none", c["ot_none"]), ("no", c["ot_no"])])}</fieldset>
</div>
<div class="step"><h2>{c["st3"]}</h2>
 <p class="hint small">{c["ded_hint"]}</p>
 <div class="costs">
  <div><label for="rent">{c["rent"]}</label><div class="unit"><input type="number" inputmode="numeric" id="rent" min="0"><span>{c["unit_yen"]}</span></div></div>
  <div><label for="util">{c["util"]}</label><div class="unit"><input type="number" inputmode="numeric" id="util" min="0"><span>{c["unit_yen"]}</span></div></div>
  <div><label for="food">{c["food"]}</label><div class="unit"><input type="number" inputmode="numeric" id="food" min="0"><span>{c["unit_yen"]}</span></div></div>
  <div><label for="other">{c["other"]}</label><div class="unit"><input type="number" inputmode="numeric" id="other" min="0"><span>{c["unit_yen"]}</span></div></div>
 </div>
 <div style="margin-top:var(--s6)">{num("fee", c["fee"], c["unit_rp"], c["fee_hint"])}</div>
</div>
<div class="step"><h2>{c["st4"]}</h2>
 {yn3("job", c["q_job"])}{yn3("ded", c["q_ded"])}{yn3("lang", c["q_lang"])}{yn3("hoken", c["q_hoken"])}{yn3("yukyu", c["q_yukyu"])}{yn3("feelist", c["q_feelist"])}
 {yn3("dep", c["q_deposit"])}{yn2("pass", c["q_passport"])}
</div>
<button type="button" class="run" id="run">{c["run"]}</button><p class="need" id="need" role="alert">{c["need"]}</p>
</form>
<div id="out" aria-live="polite">
 <h2 id="out-h" tabindex="-1">{c["r_h"]}</h2>
 <div class="sum3"><div class="r"><b id="n-r">0</b><span>{c["r_red"]}</span></div><div class="y"><b id="n-y">0</b><span>{c["r_yel"]}</span></div><div class="g"><b id="n-g">0</b><span>{c["r_ok"]}</span></div></div>
 <ul class="items" id="items"></ul>
 <h3>{c["r_money"]}</h3>
 <table><tbody id="money"></tbody></table>
 <h3>{c["q_h"]}</h3><p class="small">{c["q_lead"]}</p>
 <ol class="qs" id="qs"></ol><p id="q-none" class="small" hidden>{c["q_none"]}</p>
 <div class="acts"><button type="button" class="pri" id="copy">{c["q_copy"]}</button><a id="wa-q" href="#" target="_blank" rel="noopener">{c["q_wa"]}</a><a id="wa-r" href="#" target="_blank" rel="noopener">{c["share_res"]}</a></div>
 <p class="small">{c["notlegal"]}</p><p class="small">{c["again"]}</p>
</div>'''
    helps = "".join(f'<div class="contact"><h3>{h}</h3>' + (f'<p class="tel"><a href="tel:{tel}">{tl}</a></p>' if tel else "") + f'<p>{d}</p></div>' for h, tel, tl, d in c["help"])
    rel = "".join(f'<a href="{L(s)}">{t}</a>' for s, t in c["rel"])
    srcs = "".join(f'<li>{n}（{CHECKED}）<br><a href="{u}">{u}</a></li>' for n, u in SRC)
    data = dict(prefs=[{"n": p[0] if lang == "ja" else p[1], "j": p[0], "w": p[2], "d": p[3], "k": p[4]} for p in PREFS], rates=RATES,
                R=R[lang], Q={k: (v[0] if lang == "ja" else v[1], v[0]) for k, v in Q.items()}, lang=lang, share=SHARE_TXT[lang],
                url=f"https://tetsuzukinavi.org/{lang}/kontrak", copied=c["q_copied"],
                L=dict(m_hourly=c["m_hourly"], m_minw=c["m_minw"], m_gross=c["m_gross"], m_social=c["m_social"], m_ded=c["m_ded"], m_left=c["m_left"], m_fee=c["m_fee"], m_months=c["m_months"], red=c["r_red"], yel=c["r_yel"], ok=c["r_ok"]))
    return f'''<main class="wrap">{CSS}
<nav class="crumb" aria-label="breadcrumb"><ol><li><a href="/{lang}/">{"手続きナビ" if lang == "ja" else "Tetsuzuki Navi"}</a></li><li>{c["crumb"]}</li></ol></nav>
<h1>{c["h1"]}</h1>
<p class="lead">{c["lead"]}</p>
<div class="notice"><div class="priv">{LOCK}<p>{c["privacy"]}</p></div></div>
<p class="updated">{c["upd"]}</p>
{form}
<section style="margin-top:var(--s12)"><h2>{c["how_h"]}</h2>{c["how_p"]}</section>
<section><h2>{c["help_h"]}</h2>{helps}<p class="small">{c["help_note"]}</p></section>
<section><h2>{c["rel_h"]}</h2><div class="related">{rel}</div></section>
<aside class="trust" id="src"><h2>{c["tr_h"]}</h2><div class="money">{c["tr_money"]}</div>
<h3>{c["tr_src"]}</h3><ol>{srcs}</ol><h3>{c["tr_log"]}</h3><ul><li>{c["log"]}</li></ul>
<a class="btn" href="/{lang}/contact?page=kontrak">{c["fix"]}</a></aside>
<script>const K={json.dumps(data, ensure_ascii=False)};</script>
<script>{JS}</script>
</main>'''

JS = r"""
(function(){
const $=id=>document.getElementById(id), P=K.prefs, R=K.R, ja=K.lang==="ja";
const fmt=n=>Math.round(n).toLocaleString(ja?"en-US":"de-DE");
const yen=n=>ja?fmt(n)+"円":"¥"+fmt(n);
const rp=n=>"Rp "+Math.round(n).toLocaleString("de-DE");
const st={visa:"ssw",mode:"m",ot:"",pass:"n"}; let ran=false;
document.querySelectorAll("[data-k]").forEach(g=>g.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;
  g.querySelectorAll("button").forEach(x=>x.setAttribute("aria-pressed",x===b?"true":"false"));st[g.dataset.k]=b.dataset.v;
  if(g.dataset.k==="mode"){$("f-msal").hidden=st.mode!=="m";$("f-wage").hidden=st.mode!=="h";}
  if(ran)check();}));
document.querySelectorAll("#kc input,#kc select").forEach(i=>i.addEventListener("input",()=>{if(ran)check();}));
const n=id=>{const v=parseFloat($(id).value);return isFinite(v)&&v>0?v:0;};
const f=(s,o)=>s.replace(/\{(\w)\}/g,(_,k)=>o[k]);
function dstr(d){const[y,m,dd]=d.split("-").map(Number);const M=["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"];return ja?`${y}年${m}月${dd}日`:`${dd} ${M[m-1]} ${y}`;}
function kyuyo(a){let x;if(a<=1900000)x=650000;else if(a<=3600000)x=a*.3+80000;else if(a<=6600000)x=a*.2+440000;else if(a<=8500000)x=a*.1+1100000;else x=1950000;return Math.min(a,Math.max(740000,x));}
function itax(t){const b=[[1950000,.05,0],[3300000,.1,97500],[6950000,.2,427500],[9000000,.23,636000],[18000000,.33,1536000],[40000000,.4,2796000],[Infinity,.45,4796000]];for(const[l,r,d]of b)if(t<=l)return Math.max(0,t*r-d)*1.021;}
function check(){
  const pi=$("pref").value, wage=st.mode==="h"?n("wage"):n("msal");
  if(pi===""||!wage){$("need").classList.add("show");return false;}
  $("need").classList.remove("show");
  const p=P[pi], h=n("hours")||8, hol=n("hol");
  const days=hol?(365-hol)/12:21, mh=h*days;
  const hourly=st.mode==="h"?wage:wage/mh, gross=st.mode==="h"?wage*mh:wage;
  const it=[], qs=[]; const add=(lv,key,o,extra)=>{const[t,d]=R[key];it.push({lv,t:f(t,o||{}),d:d+(extra?" "+extra:"")});};
  const q=(k,o,oj)=>{const[a,b]=K.Q[k];qs.push([f(a,o||{}),f(b,oj||o||{})]);};
  const qo={p:p.n,w:fmt(p.w)}, qj={p:p.j,w:p.w.toLocaleString("en-US")};
  const dec=x=>x.toLocaleString(ja?"en-US":"de-DE",{minimumFractionDigits:1,maximumFractionDigits:1});
  // 1 最低賃金
  const mo={h:fmt(Math.floor(hourly)),p:p.n,w:fmt(p.w),d:dstr(p.d),x:fmt(Math.floor(hourly)-p.w)};
  const note=(st.mode==="m"&&!hol)?" "+R.minw_note:"";
  if(Math.floor(hourly)<p.w){add("r","minw_red",mo,note);q("minw",qo,qj);}
  else if(hourly<p.w*1.03){add("y","minw_yel",mo,note);q("minw_up");}
  else add("g","minw_ok",mo,note);
  // 2 時間と休日
  let tflag=false;
  if(hol&&hol<52){add("r","hol_red",{x:fmt(hol)});tflag=true;}
  const wk=hol?h*(365-hol)/(365/7):0;
  if(h>8){add("y","day_yel",{x:h});tflag=true;}
  else if(hol&&wk>40.05&&hol>=52){add("y","week_yel",{x:dec(wk)});tflag=true;}
  if(!hol){add("y","hol_unk");tflag=true;}
  if(tflag)q("time"); else add("g","time_ok");
  // 3 残業
  if(st.ot==="lt"){add("r","ot_red");q("ot");}
  else if(st.ot==="none"||st.ot===""){add("y","ot_yel");q("ot");}
  else if(st.ot==="ge")add("g","ot_ok"); else add("g","ot_no");
  // お金
  const social=Math.round(gross*p.k/200)+Math.round(gross*K.rates.shien/200)+Math.round(gross*K.rates.pension/200)+Math.round(gross*K.rates.koyo_worker/100);
  const A=gross*12,S=social*12,sh=A-kyuyo(A),kiso=sh<=4890000?1040000:sh<=6550000?670000:620000;
  const tax=Math.round(itax(Math.floor(Math.max(0,sh-S-kiso)/1000)*1000)/12);
  const ded=n("rent")+n("util")+n("food")+n("other"), left=gross-social-tax-ded;
  const ssw=st.visa==="ssw";
  if(left<=0){add("r","left_red",{x:yen(left)});q("ded");if(ssw)q("ded_ssw");}
  else if(st.ded!=="y"){add("y","ded_yel",null,ssw?R.ded_ssw:"");q("ded");if(ssw)q("ded_ssw");}
  else add("g","ded_ok",{x:yen(left)});
  // 来日前の費用
  const fee=n("fee"), feeY=fee/K.rates.jpy_idr, months=left>0?feeY/left:0;
  if(fee&&left>0&&months>=6)add("y","fee_yel",{x:dec(months)},ssw?R.fee_ssw:"");
  if(st.feelist!=="y"&&(fee||st.feelist==="n")){add("y","feelist_yel");q("fee");}
  // 保証金・パスポート
  if(st.dep==="y"){add("r","dep_red");q("dep");} else if(st.dep!=="n"){add("y","dep_yel");q("dep");}
  if(st.pass==="y"){add("r","pass_red");q("pass");}
  // 書いてあるか
  [["job","job_yel"],["lang","lang_yel"],["hoken","hoken_yel"],["yukyu","yukyu_yel"]].forEach(([k,key])=>{if(st[k]!=="y"){add("y",key);q(k);}});
  const okw=[["job",0],["lang",0],["hoken",0],["yukyu",0]].filter(([k])=>st[k]==="y");
  // 表示
  const order={r:0,y:1,g:2}; it.sort((a,b)=>order[a.lv]-order[b.lv]);
  const tag={r:K.L.red,y:K.L.yel,g:K.L.ok};
  $("items").innerHTML=it.map(x=>`<li class="${x.lv}"><b><span class="tag">${tag[x.lv]}</span>${x.t}</b><p>${x.d}</p></li>`).join("");
  ["r","y","g"].forEach(l=>$("n-"+l).textContent=it.filter(x=>x.lv===l).length);
  const rows=[[K.L.m_hourly,yen(hourly)],[K.L.m_minw,yen(p.w)+" ("+p.n+")"],[K.L.m_gross,yen(gross)],[K.L.m_social,"−"+yen(social+tax)],[K.L.m_ded,"−"+yen(ded)],[K.L.m_left,"<b>"+yen(left)+"</b><br><span class='small'>≈ "+rp(left*K.rates.jpy_idr)+"</span>"]];
  if(fee)rows.push([K.L.m_fee,rp(fee)+"<br><span class='small'>≈ "+yen(feeY)+(left>0?"<br>"+K.L.m_months.replace("{x}",dec(months)):"")+"</span>"]);
  $("money").innerHTML=rows.map(([a,b])=>`<tr><th scope="row">${a}</th><td class="n">${b}</td></tr>`).join("");
  $("qs").innerHTML=qs.map(([a,b])=>`<li>${a}${ja?"":`<span class="jp" lang="ja">${b}</span>`}</li>`).join("");
  $("q-none").hidden=qs.length>0;
  const qtext=qs.map(([a,b],i)=>`${i+1}. ${a}`+(ja?"":`\n   ${b}`)).join("\n");
  $("copy").onclick=()=>navigator.clipboard.writeText(qtext).then(()=>{$("copy").textContent=K.copied;});
  $("wa-q").href="https://wa.me/?text="+encodeURIComponent(qtext);
  const s=K.share, nr=it.filter(x=>x.lv==="r").length, ny=it.filter(x=>x.lv==="y").length;
  $("wa-r").href="https://wa.me/?text="+encodeURIComponent(`${s[0]}\n${s[1]}: ${nr} / ${s[2]}: ${ny}\n${s[3]}: ${yen(left)}\n\n${s[4]}\n${K.url}`);
  return true;
}
$("run").addEventListener("click",()=>{if(check()){ran=true;$("out").classList.add("show");$("out-h").focus();$("out").scrollIntoView({behavior:"smooth"});}});
})();
"""

def put_main(s, m): return re.sub(r"<main.*?</main>", lambda _: m, s, count=1, flags=re.S)

for lang in ("ja", "id"):
    shell = (SITE / lang / "gaji.html").read_text(encoding="utf-8")
    out = put_main(shell, main(lang))
    i = out.index("</main>"); out = out[:i] + re.sub(r"<script>.*?</script>\n?", "", out[i:], flags=re.S)
    (SITE / lang / "kontrak.html").write_text(out, encoding="utf-8")
    # 手取りページの「契約の前に確認すること」からツールへ
    g = SITE / lang / "gaji.html"; s = g.read_text(encoding="utf-8")
    if "/kontrak" not in s:
        s = s.replace('</ul>\n    <div class="notice"><p>', f'</ul>\n    <p><a class="btn primary" href="/{lang}/kontrak">{T[lang]["gaji_btn"]}</a></p>\n    <div class="notice"><p>', 1)
        g.write_text(s, encoding="utf-8")
print("kontrak written")
