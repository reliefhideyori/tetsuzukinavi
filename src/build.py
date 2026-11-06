"""Builds the take-home pay page in Japanese (master) and Indonesian from one template.
Run: python3 build.py  -> gaji-ja.html, gaji-id.html"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from data import PREFS, RATES, CHECKED

T = {}
def t(key, ja, id_): T[key] = {"ja": ja, "id": id_}

# ---------- page text ----------
t("html_lang", "ja", "id")
t("title", "日本で手元に残るお金", "Gaji Bersih di Jepang")
t("font", "Noto+Sans+JP:wght@400;700", "Noto+Sans:wght@400;700")
t("font_family", '"Noto Sans JP", "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif', '"Noto Sans", "Segoe UI", Roboto, sans-serif')
t("site", "手続きナビ", "Tetsuzuki Navi")
t("site_sub", "日本で暮らす・働くための公式情報ガイド", "Panduan informasi resmi untuk tinggal dan bekerja di Jepang")
t("badge1", "公式の情報だけ", "Hanya sumber resmi")
t("badge2", "毎週確認", "Dicek tiap minggu")
t("badge3", "紹介料なし", "Tanpa komisi")
t("crumb1", "日本で働く", "Bekerja di Jepang")
t("crumb2", "お金", "Uang")
t("h1", "日本で本当に手元に残るお金（手取り計算）", "Berapa Uang yang Benar-benar Tersisa di Jepang (Kalkulator Gaji Bersih)")
t("lead", "求人の「月給」から、税金・保険・寮費などを引いて、毎月いくら残るかを計算します。特定技能・技能実習で日本に来る前に使ってください。",
  "Hitung berapa yang tersisa setiap bulan setelah gaji di lowongan dipotong pajak, asuransi, asrama, dan lainnya. Gunakan sebelum berangkat ke Jepang lewat Tokutei Ginou (SSW) atau magang.")
t("updated", "最終確認日：2026年11月5日（毎週確認）　／　出典：厚生労働省・協会けんぽ・国税庁などの公式情報（ページの最後に一覧）",
  "Terakhir dicek: 5 November 2026 (dicek tiap minggu)  /  Sumber: informasi resmi Kementerian Kesehatan, Tenaga Kerja, dan Kesejahteraan Jepang (MHLW), Kyokai Kenpo, Badan Pajak Nasional, dan lainnya (daftar di bagian bawah)")
t("first_h", "はじめに知っておくこと", "Yang perlu diketahui dulu")
t("first_p", "求人に書かれた「月給20万円」は、20万円もらえるという意味ではありません。給料からは<b>社会保険料と税金</b>が自動で引かれ、さらに<b>寮費や光熱費</b>が引かれることがあります。日本に来て2年目からは<b>住民税</b>も始まるので、手取りが減ります。",
  "\"Gaji 200.000 yen per bulan\" di lowongan <b>bukan</b> berarti Anda menerima 200.000 yen. Gaji otomatis dipotong <b>asuransi sosial dan pajak</b>, dan kadang juga <b>biaya asrama dan listrik/air</b>. Mulai tahun kedua di Jepang, <b>pajak penduduk (juminzei)</b> juga mulai dipotong, jadi gaji bersih turun.")
t("toc", "このページの内容", "Isi halaman ini")
t("toc1", "手取りを計算する", "Hitung gaji bersih")
t("toc2", "給料から引かれるお金", "Potongan dari gaji")
t("toc3", "よくある勘違い", "Salah paham yang sering terjadi")
t("toc4", "契約の前に確認すること", "Yang harus dicek sebelum tanda tangan kontrak")
t("toc5", "困ったときの相談先", "Tempat konsultasi jika ada masalah")

# calculator
t("c_pref", "働く都道府県", "Prefektur tempat bekerja")
t("c_pref_note", "最低賃金と健康保険料が都道府県で変わります。", "Upah minimum dan iuran asuransi kesehatan berbeda tiap prefektur.")
t("c_pay", "給料の決め方", "Cara gaji ditentukan")
t("c_hourly", "時給", "Per jam")
t("c_monthly", "月給", "Per bulan")
t("c_wage", "時給（円）", "Upah per jam (yen)")
t("c_minw", "この都道府県の最低賃金：", "Upah minimum prefektur ini: ")
t("c_yen_h", "円／時間", " yen/jam")
t("c_from", "から", " mulai ")
t("c_hours", "1日の労働時間", "Jam kerja per hari")
t("c_days", "1か月の労働日数", "Hari kerja per bulan")
t("c_ot", "1か月の残業時間", "Jam lembur per bulan")
t("c_msal", "月給（円・残業代を除く）", "Gaji per bulan (yen, tanpa lembur)")
t("c_age", "年齢", "Usia")
t("c_age1", "39歳以下", "39 tahun ke bawah")
t("c_age2", "40〜64歳", "40–64 tahun")
t("c_year", "日本で働いて何年目か", "Tahun ke berapa bekerja di Jepang")
t("c_y1", "1年目", "Tahun pertama")
t("c_y2", "2年目から", "Tahun kedua dst.")
t("c_costs", "毎月の生活費（円）", "Biaya hidup per bulan (yen)")
t("c_costs_note", "金額は例です。契約書や求人に書かれた金額に変えてください。", "Angka ini hanya contoh. Ganti dengan angka di kontrak atau lowongan Anda.")
t("c_rent", "寮費・家賃", "Asrama / sewa")
t("c_util", "電気・ガス・水道", "Listrik, gas, air")
t("c_food", "食費", "Makan")
t("c_phone", "スマホ・ネット", "HP / internet")
t("c_other", "その他", "Lainnya")
t("c_rate", "為替レート（1円＝何ルピア）", "Kurs (1 yen = berapa rupiah)")
t("c_rate_note", "2026年11月4日の目安は約114ルピアです。送金するときは送金会社のレートを確認してください。", "Perkiraan per 4 November 2026: sekitar 114 rupiah. Saat mengirim uang, cek kurs dari jasa pengiriman uang.")
t("r_title", "計算結果（毎月の目安）", "Hasil (perkiraan per bulan)")
t("r_gross", "給料の総額", "Gaji kotor")
t("r_social", "社会保険料", "Iuran asuransi sosial")
t("r_tax", "税金", "Pajak")
t("r_net", "手取り（振り込まれる額）", "Gaji bersih (yang ditransfer)")
t("r_costs", "生活費", "Biaya hidup")
t("r_left", "毎月残るお金", "Uang tersisa per bulan")
t("r_year", "1年で残るお金", "Uang tersisa per tahun")
t("r_detail", "引かれるお金の内訳", "Rincian potongan")
t("r_health", "健康保険", "Asuransi kesehatan")
t("r_shien", "子ども・子育て支援金", "Iuran dukungan anak")
t("r_kaigo", "介護保険", "Asuransi perawatan lansia")
t("r_pension", "厚生年金", "Pensiun karyawan (kosei nenkin)")
t("r_koyo", "雇用保険", "Asuransi ketenagakerjaan")
t("r_itax", "所得税", "Pajak penghasilan")
t("r_jtax", "住民税", "Pajak penduduk (juminzei)")
t("r_jtax0", "1年目は0円", "Tahun pertama 0 yen")
t("r_below", "この時給は最低賃金より低いです。日本では外国人にも最低賃金が適用されるので、この条件は違法です。契約する前に相談してください。",
  "Upah per jam ini di bawah upah minimum. Di Jepang, upah minimum juga berlaku untuk pekerja asing, jadi syarat ini melanggar hukum. Konsultasikan sebelum tanda tangan kontrak.")
t("r_neg", "生活費が手取りより多く、毎月赤字になります。", "Biaya hidup lebih besar dari gaji bersih. Anda akan kekurangan uang (tekor) setiap bulan.")
t("r_note", "これは目安です。実際の額は、会社の計算方法、賞与、家族の扶養、市区町村によって変わります。所得税は1年分を12で割った額で、毎月の天引きとは少し違うことがあります（年末調整で精算されます）。",
  "Ini hanya perkiraan. Jumlah sebenarnya tergantung cara hitung perusahaan, bonus, tanggungan keluarga, dan kota tempat tinggal. Pajak penghasilan dihitung dari pajak setahun dibagi 12, jadi bisa sedikit berbeda dari potongan bulanan (selisihnya disesuaikan di akhir tahun / nenmatsu chosei).")
t("legend_social", "社会保険", "Asuransi")
t("legend_tax", "税金", "Pajak")
t("legend_costs", "生活費", "Biaya hidup")
t("legend_left", "残るお金", "Tersisa")

# section 2
t("s2_intro", "日本の会社員は、次のお金が給料から自動で引かれます。どれも法律で決まっていて、会社が勝手に決めることはできません。",
  "Karyawan di Jepang otomatis dipotong biaya berikut dari gajinya. Semuanya ditentukan oleh hukum, bukan oleh perusahaan.")
t("d_health", "病院で払うお金が3割になります。保険料は会社と半分ずつ払います。料率は都道府県で違い、約9.4〜10.6%（本人はその半分）です。",
  "Anda hanya membayar 30% biaya berobat. Iuran dibayar setengah oleh perusahaan, setengah oleh Anda. Tarifnya berbeda tiap prefektur, sekitar 9,4–10,6% (Anda membayar setengahnya).")
t("d_shien", "2026年4月分から始まった新しいお金です。全国同じ0.23%で、本人はその半分です。", "Iuran baru mulai April 2026. Tarif sama di seluruh Jepang 0,23%, Anda membayar setengahnya.")
t("d_kaigo", "40歳から64歳の人だけ払います。1.62%で、本人はその半分です。", "Hanya untuk usia 40–64 tahun. Tarif 1,62%, Anda membayar setengahnya.")
t("d_pension", "18.3%で、本人はその半分の9.15%です。一番大きい天引きです。<b>帰国するときに一部が戻ります</b>（脱退一時金）。6か月以上加入していれば請求でき、計算の上限は5年分です。日本を出てから2年以内に請求が必要です。",
  "Tarif 18,3%, Anda membayar setengahnya yaitu 9,15%. Ini potongan terbesar. <b>Sebagian bisa dikembalikan saat pulang ke negara asal</b> (dattai ichijikin). Bisa diajukan jika ikut minimal 6 bulan, dihitung maksimal 5 tahun. Harus diajukan dalam 2 tahun setelah meninggalkan Jepang.")
t("d_koyo", "仕事を失ったときの手当などのための保険です。本人負担は0.5%です（2026年4月〜2027年3月）。", "Asuransi untuk tunjangan jika kehilangan pekerjaan, dll. Bagian Anda 0,5% (April 2026–Maret 2027).")
t("d_itax", "収入にかかる国の税金です。2026年分から、給料だけの人は年収178万円までかかりません。", "Pajak negara atas penghasilan. Mulai tahun 2026, orang yang hanya punya gaji tidak kena pajak ini sampai penghasilan 1,78 juta yen per tahun.")
t("d_jtax", "住んでいる市区町村に払う税金です。前の年の収入で決まるので、<b>1年目はかかりません。2年目の6月から</b>天引きが始まります。帰国する年も払う必要があります。",
  "Pajak yang dibayar ke kota tempat tinggal. Dihitung dari penghasilan tahun sebelumnya, jadi <b>tahun pertama tidak ada. Mulai Juni tahun kedua</b> gaji dipotong. Pada tahun pulang ke negara asal pun tetap harus dibayar.")
t("jtax_link", "住民税の詳しい説明（新宿区の例）", "Penjelasan lengkap pajak penduduk (contoh: Shinjuku, saat ini dalam bahasa Jepang)")

# section 3
t("m1q", "「月給20万円」なら20万円もらえる？", "\"Gaji 200.000 yen\" berarti terima 200.000 yen?")
t("m1a", "いいえ。社会保険料と税金で、1年目でも約3万円が引かれます。寮費などを引くと、残るのは10万円前後のことが多いです。上の計算機で確かめてください。",
  "Tidak. Bahkan di tahun pertama, sekitar 30.000 yen dipotong untuk asuransi dan pajak. Setelah dipotong asrama dan lainnya, sering kali yang tersisa sekitar 100.000 yen. Cek dengan kalkulator di atas.")
t("m2q", "1年目と2年目の手取りは同じ？", "Gaji bersih tahun pertama dan kedua sama?")
t("m2a", "いいえ。2年目の6月から住民税が始まるので、毎月数千円〜1万円ほど減ります。1年目の手取りで生活の計画を立てないでください。",
  "Tidak. Mulai Juni tahun kedua pajak penduduk dipotong, jadi gaji bersih turun beberapa ribu sampai sekitar 10.000 yen per bulan. Jangan membuat rencana hidup berdasarkan gaji tahun pertama.")
t("m3q", "会社は給料から何でも引ける？", "Perusahaan boleh memotong gaji untuk apa saja?")
t("m3a", "いいえ。給料は全額を払うのが原則です。税金と社会保険料のほかに引けるのは、会社と働く人の代表が書面で約束したもの（寮費など）だけです（労働基準法第24条）。説明のない天引きがあれば相談してください。",
  "Tidak. Pada prinsipnya gaji harus dibayar penuh. Selain pajak dan asuransi sosial, perusahaan hanya boleh memotong hal yang disepakati secara tertulis antara perusahaan dan perwakilan pekerja, seperti biaya asrama (Undang-Undang Standar Ketenagakerjaan Pasal 24). Jika ada potongan tanpa penjelasan, konsultasikan.")
t("m4q", "残業しても給料は同じ？", "Lembur tidak menambah gaji?")
t("m4a", "いいえ。1日8時間・週40時間を超えた残業には、通常の1.25倍以上の賃金が払われます（労働基準法第37条）。計算機の「残業時間」に入れると反映されます。",
  "Tidak. Lembur di atas 8 jam per hari atau 40 jam per minggu harus dibayar minimal 1,25 kali upah biasa (UU Standar Ketenagakerjaan Pasal 37). Masukkan ke \"jam lembur\" di kalkulator.")
t("m5q", "外国人は最低賃金より安くてもいい？", "Pekerja asing boleh dibayar di bawah upah minimum?")
t("m5a", "いいえ。最低賃金は国籍に関係なく、日本で働くすべての人に適用されます。特定技能では、同じ仕事をする日本人と同じ以上の給料が必要です。",
  "Tidak. Upah minimum berlaku untuk semua orang yang bekerja di Jepang, apa pun kewarganegaraannya. Untuk Tokutei Ginou, gaji harus sama atau lebih tinggi daripada gaji orang Jepang yang melakukan pekerjaan yang sama.")

# section 4
t("s4_intro", "日本に来る前に、雇用契約書（雇用条件書）で次のことを確認してください。わからない言葉があれば、サインする前に質問してください。",
  "Sebelum berangkat ke Jepang, cek hal berikut di kontrak kerja (koyo joken sho). Jika ada kata yang tidak dipahami, tanyakan sebelum tanda tangan.")
t("k1", "月給または時給が書かれているか。働く都道府県の最低賃金より高いか", "Apakah gaji bulanan atau per jam tertulis? Apakah lebih tinggi dari upah minimum prefektur tempat kerja?")
t("k2", "寮費・光熱費など、給料から引かれるものと金額が書かれているか", "Apakah potongan seperti asrama dan listrik/air tertulis beserta jumlahnya?")
t("k3", "1日の労働時間、休日、残業の有無が書かれているか", "Apakah jam kerja per hari, hari libur, dan ada/tidaknya lembur tertulis?")
t("k4", "自分が読める言語の契約書をもらえるか", "Apakah Anda mendapat kontrak dalam bahasa yang Anda pahami?")
t("k5", "日本に来る前に払うお金（研修費・手数料など）がいくらで、何のためか", "Berapa biaya yang harus dibayar sebelum berangkat (biaya pelatihan, biaya agen, dll.) dan untuk apa?")
t("k6_note", "このサイトは、特定の会社・LPK・仲介業者を紹介しません。個別の契約が正しいかどうかは、下の公的な相談先に聞いてください。",
  "Situs ini tidak merekomendasikan perusahaan, LPK, atau agen tertentu. Untuk menanyakan apakah kontrak Anda benar, hubungi tempat konsultasi resmi di bawah.")

# section 5
t("h_dial", "外国人労働者向け相談ダイヤル（厚生労働省）", "Layanan Konsultasi untuk Pekerja Asing (MHLW)")
t("h_dial_d", "インドネシア語：火曜・木曜 10:00〜15:00（12:00〜13:00を除く）。給料や労働条件の相談ができます。無料ですが通話料がかかります。",
  "Bahasa Indonesia: Selasa dan Kamis 10.00–15.00 (kecuali 12.00–13.00). Bisa konsultasi soal gaji dan syarat kerja. Layanannya gratis, tetapi Anda tetap membayar biaya telepon.")
t("h_hot", "労働条件相談ほっとライン（厚生労働省）", "Hotline Konsultasi Syarat Kerja (MHLW)")
t("h_hot_d", "無料で電話できます。インドネシア語にも対応していますが、言語によって曜日が違うので、公式ページで確認してください。",
  "Telepon gratis. Tersedia dalam bahasa Indonesia, tetapi hari layanan berbeda tiap bahasa. Cek di halaman resmi.")
t("h_note", "日本にいる間に使える相談先です。日本に来る前の契約やLPKについては、インドネシアの政府機関（BP2MI／P2MI省）に確認してください。",
  "Layanan ini bisa digunakan selama di Jepang. Untuk kontrak atau LPK sebelum berangkat, tanyakan ke lembaga pemerintah Indonesia (BP2MI / Kementerian P2MI).")

# trust
t("tr_h", "この情報について", "Tentang informasi ini")
t("tr_money", "<b>このサイトの収入は広告だけです。</b>LPK、仲介業者、会社から紹介料は受け取っていません。メール登録や有料相談もありません。",
  "<b>Pendapatan situs ini hanya dari iklan.</b> Kami tidak menerima komisi dari LPK, agen, atau perusahaan. Tidak ada pendaftaran email atau konsultasi berbayar.")
t("tr_src", "出典（確認日）", "Sumber (tanggal dicek)")
t("tr_log", "変更履歴", "Riwayat perubahan")
t("tr_log1", "2026年11月5日　第1版を公開。2026年度の最低賃金・保険料率・所得税の改正を反映。", "5 November 2026  Versi 1 diterbitkan. Sudah memakai upah minimum, tarif asuransi, dan perubahan pajak penghasilan tahun 2026.")
t("tr_fix", "間違いを見つけたら教えてください", "Laporkan jika ada kesalahan")
t("tr_about", "運営者と方針", "Pengelola dan kebijakan")
t("about_url", "https://claude.ai/artifact/2tPzvnjGiCfbMEjD61wUWS", "https://claude.ai/artifact/Bc82QWebd8N6QCPFHtGBHe")
t("tr_lang", "日本語", "Bahasa Indonesia")
t("tr_other_lang", "Bahasa Indonesia", "日本語")

SOURCES = [
 ("令和8年度 地域別最低賃金 答申状況（厚生労働省）","https://www.mhlw.go.jp/content/11302000/001745621.pdf","2026-11-05"),
 ("令和8年度 都道府県単位保険料率・介護保険料率・子ども・子育て支援金率（協会けんぽ）","https://www.kyoukaikenpo.or.jp/g7/cat330/sb3130/r08/","2026-11-05"),
 ("令和8年度の雇用保険料率（山形労働局）","https://jsite.mhlw.go.jp/yamagata-roudoukyoku/koyouhoken-20260316.html","2026-11-05"),
 ("令和8年度税制改正の解説（財務省）","https://www.mof.go.jp/tax_policy/tax_reform/outline/fy2026/explanation/PDF/p0003-0010.pdf","2026-11-05"),
 ("脱退一時金の制度（日本年金機構、2026年4月1日更新）","https://www.nenkin.go.jp/service/jukyu/seido/sonota-kyufu/dattai-ichiji/20150406.html","2026-11-05"),
 ("外国人労働者向け相談ダイヤル（厚生労働省）","https://www.mhlw.go.jp/content/001708139.pdf","2026-11-05"),
 ("為替レート JPY/IDR（Trading Economics、2026年11月4日）","https://id.tradingeconomics.com/jpyidr:cur","2026-11-05"),
]

JS_L = {
 "ja": {"yen": "円", "rp": "ルピア", "minw": "最低賃金", "per_h": "円／時間"},
 "id": {"yen": " yen", "rp": "", "minw": "Upah minimum", "per_h": " yen/jam"},
}

TEMPLATE = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()

def build(lang):
    html = TEMPLATE
    def rep(m):
        k = m.group(1)
        return T[k][lang]
    html = re.sub(r"\{\{(\w+)\}\}", rep, html)
    prefs = [{"n": (p[0] if lang == "ja" else p[1]), "w": p[2], "d": p[3], "k": p[4]} for p in PREFS]
    html = html.replace("/*PREFS*/", json.dumps(prefs, ensure_ascii=False))
    html = html.replace("/*RATES*/", json.dumps(RATES))
    html = html.replace("/*L*/", json.dumps(JS_L[lang], ensure_ascii=False))
    src = "\n".join(f'<li>{s[0]}（{s[2]}）<br><a href="{s[1]}">{s[1]}</a></li>' for s in SOURCES)
    html = html.replace("<!--SOURCES-->", src)
    left = re.findall(r"\{\{\w+\}\}", html)
    assert not left, left
    out = os.path.join(os.path.dirname(__file__), f"gaji-{lang}.html")
    open(out, "w", encoding="utf-8").write(html)
    print("wrote", out, len(html))

if __name__ == "__main__":
    for lang in ("ja", "id"):
        build(lang)
