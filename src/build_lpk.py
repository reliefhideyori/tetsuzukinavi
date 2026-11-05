"""Builds the LPK / agent check page (ja, id). Reuses header + CSS from template.html."""
import re, os
D = os.path.dirname(__file__)
tpl = open(os.path.join(D, "template.html"), encoding="utf-8").read()
head = tpl.split("<main")[0]

SRC = [
 ("インドネシアとの特定技能に関する協力覚書・インドネシア側の手続（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/ssw/nyuukokukanri06_00108.html"),
 ("特定技能外国人を受け入れる際の注意点（出入国在留管理庁）", "https://www.moj.go.jp/isa/policies/ssw/chuui.html"),
 ("技能実習制度 送出国との二国間取決め（出入国在留管理庁）", "https://www.moj.go.jp/isa/applications/titp/nyuukokukanri07_00139.html"),
 ("認定送出機関一覧（外国人技能実習機構）", "https://www.otit.go.jp/soushutsu_kikan_list/"),
 ("P3MI一覧 SISKOP2MI（インドネシア政府）", "https://siskop2mi.bp2mi.go.id/profil/lembaga/list_lembaga/p3mi"),
 ("外国人労働者向け相談ダイヤル（厚生労働省）", "https://www.mhlw.go.jp/content/001708139.pdf"),
]

C = {
"ja": dict(
 title="LPK・仲介業者を選ぶ前に", crumb="日本で働く",
 h1="LPK・仲介業者を選ぶ前に、公式情報で確認できること",
 lead="日本で働くためにLPK（研修所）や仲介業者を使う前に、日本とインドネシアの公式情報で確かめられることをまとめました。",
 updated="最終確認日：2026年11月5日（毎週確認）　／　出典：出入国在留管理庁・外国人技能実習機構・インドネシア政府の公式情報（ページの最後に一覧）",
 notice_h="このページについて",
 notice="このサイトは、特定のLPK・仲介業者を紹介したり、ランキングを作ったりしません。紹介料も受け取っていません。自分で確かめるための方法だけを書いています。",
 toc=["まず知っておくこと","確認の手順","注意したほうがいいこと","相談先"],
 s1=[
  ("特定技能では、業者を使うかどうかは自分で選べます", "インドネシアの職業紹介事業者（P3MI）の利用は<b>任意</b>だと、日本の出入国在留管理庁が案内しています。<sup><a href=\"#src\">[1]</a></sup>"),
  ("特定技能では、保証金や違約金は認められていません", "日本の受入れ機関は、保証金を取ったり、違約金の契約を結んだりしていないことが条件です。また、日本での生活の支援にかかる費用を、働く本人に払わせてはいけません。<sup><a href=\"#src\">[2]</a></sup>"),
  ("技能実習の送出機関は、両国が認めた機関だけです", "技能実習で行く場合、送出機関は日本とインドネシアが認めた機関である必要があります。一覧は外国人技能実習機構が公開しています。<sup><a href=\"#src\">[3][4]</a></sup>技能実習は、2027年4月から「育成就労」という新しい制度に変わる予定です。"),
 ],
 steps=[
  ("自分の在留資格を確かめる", "行くのが「特定技能」か「技能実習」かで、確認する場所が違います。"),
  ("技能実習なら、送出機関の一覧を見る", "外国人技能実習機構の「認定送出機関一覧」に、その機関の名前があるか確認します。<sup><a href=\"#src\">[4]</a></sup>"),
  ("業者を使うなら、P3MIの一覧を見る", "インドネシア政府のSISKOP2MIに、その会社がP3MIとして載っているか確認します。<sup><a href=\"#src\">[5]</a></sup>"),
  ("払うお金の内訳を書面でもらう", "何のためのお金か、いつ払うか、途中でやめたら返ってくるかを、紙かデータで受け取ります。"),
  ("日本の会社の雇用条件を確認する", "給料、労働時間、寮費などが書かれた雇用条件書を見せてもらい、<a href=\"https://claude.ai/artifact/Mk38o639LkR864artsvASS\">手取り計算機</a>で毎月いくら残るか確かめます。"),
 ],
 flags=[
  "費用の内訳を書面で出さない",
  "「保証金」や、途中でやめたときの「違約金」「罰金」を求める",
  "日本の会社の雇用条件書を見せないのに「仕事は必ずある」と言う",
  "給料が働く都道府県の最低賃金より低い、または手取りの説明がない",
  "借金（ローン）をして払うよう強く勧める",
  "一覧に名前がないのに「政府の公認」と言う",
 ],
 flags_note="ひとつでも当てはまったら、お金を払う前に下の相談先に聞いてください。",
 c_id_h="インドネシア政府の窓口（日本の出入国在留管理庁が案内しているもの）",
 c1="インドネシア労働省　国外移民配置・保護局", c1l="英語・インドネシア語",
 c2="インドネシア移民労働者保護庁（BP2MI）アジア・アフリカ地域民間配置局", c2l="英語・インドネシア語",
 c_jp_h="日本に来てからの相談先", c3="外国人労働者向け相談ダイヤル（厚生労働省）", c3d="インドネシア語：火曜・木曜 10:00〜15:00（12:00〜13:00を除く）",
 tr_h="この情報について", src_h="出典（確認日：2026年11月5日）", log_h="変更履歴", log="2026年11月5日　第1版を公開",
 money="<b>このサイトの収入は広告だけです。</b>LPK、仲介業者、会社から紹介料は受け取っていません。",
 fix="間違いを見つけたら教えてください", about="運営者と方針", about_url="https://claude.ai/artifact/2tPzvnjGiCfbMEjD61wUWS",
 lang_link="https://claude.ai/artifact/",
),
"id": dict(
 title="Sebelum Memilih LPK atau Agen", crumb="Bekerja di Jepang",
 h1="Sebelum Memilih LPK atau Agen: Yang Bisa Dicek dari Sumber Resmi",
 lead="Ringkasan hal yang bisa Anda cek sendiri dari informasi resmi Jepang dan Indonesia sebelum memakai LPK atau agen untuk bekerja di Jepang.",
 updated="Terakhir dicek: 5 November 2026 (dicek tiap minggu)  /  Sumber: informasi resmi Badan Imigrasi Jepang (ISA), OTIT, dan pemerintah Indonesia (daftar di bagian bawah)",
 notice_h="Tentang halaman ini",
 notice="Situs ini tidak merekomendasikan LPK atau agen tertentu dan tidak membuat peringkat. Kami juga tidak menerima komisi. Halaman ini hanya berisi cara agar Anda bisa mengecek sendiri.",
 toc=["Yang perlu diketahui dulu","Langkah pengecekan","Tanda-tanda yang perlu diwaspadai","Tempat konsultasi"],
 s1=[
  ("Untuk Tokutei Ginou (SSW), memakai agen atau tidak adalah pilihan Anda", "Badan Imigrasi Jepang menjelaskan bahwa penggunaan perusahaan penempatan Indonesia (P3MI) bersifat <b>tidak wajib (opsional)</b>.<sup><a href=\"#src\">[1]</a></sup>"),
  ("Untuk Tokutei Ginou, uang jaminan dan denda tidak diperbolehkan", "Perusahaan penerima di Jepang harus tidak memungut uang jaminan dan tidak membuat kontrak denda (penalti). Biaya dukungan hidup di Jepang juga tidak boleh dibebankan kepada pekerja.<sup><a href=\"#src\">[2]</a></sup>"),
  ("Untuk magang (Ginou Jisshu), lembaga pengirim harus yang diakui kedua negara", "Jika berangkat lewat program magang, lembaga pengirim (sending organization) harus diakui oleh Jepang dan Indonesia. Daftarnya dipublikasikan oleh OTIT.<sup><a href=\"#src\">[3][4]</a></sup> Program magang direncanakan berganti menjadi sistem baru \"Ikusei Shuro\" mulai April 2027."),
 ],
 steps=[
  ("Pastikan jenis visa Anda", "Tempat pengecekan berbeda untuk Tokutei Ginou dan magang."),
  ("Jika magang, cek daftar lembaga pengirim", "Pastikan nama lembaganya ada di \"Daftar Lembaga Pengirim yang Diakui\" milik OTIT.<sup><a href=\"#src\">[4]</a></sup>"),
  ("Jika memakai agen, cek daftar P3MI", "Pastikan perusahaannya terdaftar sebagai P3MI di SISKOP2MI milik pemerintah Indonesia.<sup><a href=\"#src\">[5]</a></sup>"),
  ("Minta rincian biaya secara tertulis", "Minta di kertas atau file: biaya untuk apa, kapan dibayar, dan apakah dikembalikan jika berhenti di tengah jalan."),
  ("Cek syarat kerja dari perusahaan Jepang", "Minta lihat dokumen syarat kerja (gaji, jam kerja, asrama, dll.), lalu cek berapa yang tersisa tiap bulan dengan <a href=\"https://claude.ai/artifact/L6sqNYiPWnkv6wEwuouN8X\">kalkulator gaji bersih</a>."),
 ],
 flags=[
  "Tidak mau memberi rincian biaya secara tertulis",
  "Meminta \"uang jaminan\", atau \"denda/penalti\" jika berhenti di tengah jalan",
  "Tidak menunjukkan syarat kerja dari perusahaan Jepang, tetapi bilang \"pasti dapat kerja\"",
  "Gaji di bawah upah minimum prefektur tempat kerja, atau tidak ada penjelasan gaji bersih",
  "Sangat mendorong Anda meminjam uang (dana talangan / pinjaman) untuk membayar",
  "Mengaku \"resmi dari pemerintah\" padahal namanya tidak ada di daftar",
 ],
 flags_note="Jika ada satu saja yang cocok, tanyakan ke tempat konsultasi di bawah sebelum membayar.",
 c_id_h="Kontak pemerintah Indonesia (yang dicantumkan oleh Badan Imigrasi Jepang)",
 c1="Kementerian Ketenagakerjaan RI, Direktorat Penempatan dan Pelindungan Pekerja Migran Indonesia", c1l="Bahasa Inggris, Bahasa Indonesia",
 c2="BP2MI, Direktorat Penempatan Non-Pemerintah Kawasan Asia dan Afrika", c2l="Bahasa Inggris, Bahasa Indonesia",
 c_jp_h="Konsultasi setelah tiba di Jepang", c3="Layanan Konsultasi untuk Pekerja Asing (MHLW)", c3d="Bahasa Indonesia: Selasa dan Kamis 10.00–15.00 (kecuali 12.00–13.00)",
 tr_h="Tentang informasi ini", src_h="Sumber (dicek: 5 November 2026)", log_h="Riwayat perubahan", log="5 November 2026  Versi 1 diterbitkan",
 money="<b>Pendapatan situs ini hanya dari iklan.</b> Kami tidak menerima komisi dari LPK, agen, atau perusahaan.",
 fix="Laporkan jika ada kesalahan", about="Pengelola dan kebijakan", about_url="https://claude.ai/artifact/Bc82QWebd8N6QCPFHtGBHe",
 lang_link="",
),
}
TXT = {"ja": {"html_lang":"ja","site":"手続きナビ","site_sub":"日本で暮らす・働くための公式情報ガイド","badge1":"公式の情報だけ","badge2":"毎週確認","badge3":"紹介料なし","tr_other_lang":"Bahasa Indonesia","font":"Noto+Sans+JP:wght@400;700","font_family":'"Noto Sans JP", "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif'},
       "id": {"html_lang":"id","site":"Tetsuzuki Navi","site_sub":"Panduan informasi resmi untuk tinggal dan bekerja di Jepang","badge1":"Hanya sumber resmi","badge2":"Dicek tiap minggu","badge3":"Tanpa komisi","tr_other_lang":"日本語","font":"Noto+Sans:wght@400;700","font_family":'"Noto Sans", "Segoe UI", Roboto, sans-serif'}}

EXTRA_CSS = """<style>
ol.steps { list-style: none; padding: 0; counter-reset: st; }
ol.steps li { position: relative; padding: 0 0 var(--s2) 40px; margin: 0; }
ol.steps li::before { counter-increment: st; content: counter(st); position: absolute; left: 0; top: 0; width: 28px; height: 28px; border: 2px solid var(--key); color: var(--key); border-radius: 50%; display: grid; place-items: center; font-size: 14px; font-weight: 700; }
ol.steps li:not(:last-child)::after { content: ""; position: absolute; left: 14px; top: 32px; bottom: 4px; border-left: 2px solid var(--line); }
ol.steps b { display: block; }
ul.flags { list-style: none; padding: 0; }
ul.flags li { position: relative; padding: 10px 0 10px 32px; border-bottom: 1px solid var(--line); margin: 0; }
ul.flags li::before { content: "!"; position: absolute; left: 0; top: 12px; width: 20px; height: 20px; border-radius: 50%; background: var(--error); color: #fff; font-weight: 700; font-size: 13px; display: grid; place-items: center; }
.fact { border-left: 6px solid var(--key); background: var(--bg-soft); padding: var(--s2); margin-bottom: var(--s2); }
.fact h3 { margin-top: 0; }
</style>
</head>"""

def build(lang):
    c = C[lang]; tx = dict(TXT[lang]); tx["title"] = c["title"]
    h = re.sub(r"\{\{(\w+)\}\}", lambda m: tx[m.group(1)], head).replace("</head>", EXTRA_CSS, 1)
    b = ['<main class="wrap">',
         f'<nav class="crumb" aria-label="breadcrumb"><ol><li><a href="#">{tx["site"]}</a></li><li><a href="#">{c["crumb"]}</a></li><li>LPK</li></ol></nav>',
         f'<h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p><p class="updated">{c["updated"]}</p>',
         f'<div class="notice"><h2>{c["notice_h"]}</h2><p>{c["notice"]}</p></div>',
         '<nav class="toc"><h2>' + ("このページの内容" if lang == "ja" else "Isi halaman ini") + '</h2><ol>' + "".join(f'<li><a href="#s{i+1}">{x}</a></li>' for i, x in enumerate(c["toc"])) + '</ol></nav>']
    b.append(f'<section id="s1"><h2>{c["toc"][0]}</h2>' + "".join(f'<div class="fact"><h3>{a}</h3><p>{d}</p></div>' for a, d in c["s1"]) + '</section>')
    b.append(f'<section id="s2"><h2>{c["toc"][1]}</h2><ol class="steps">' + "".join(f'<li><b>{a}</b>{d}</li>' for a, d in c["steps"]) + '</ol></section>')
    b.append(f'<section id="s3"><h2>{c["toc"][2]}</h2><ul class="flags">' + "".join(f'<li>{x}</li>' for x in c["flags"]) + f'</ul><div class="notice warn"><p>{c["flags_note"]}</p></div></section>')
    b.append(f'''<section id="s4"><h2>{c["toc"][3]}</h2><h3>{c["c_id_h"]}</h3>
<div class="contact"><h3>{c["c1"]}</h3><p class="tel"><a href="tel:+6281359915990">+62 813 5991 5990</a><br><a href="tel:+6281399500091">+62 813 9950 0091</a></p><p>Email: layanansiapkerja@gmail.com<br><span class="small">{c["c1l"]}</span><sup><a href="#src">[1]</a></sup></p></div>
<div class="contact"><h3>{c["c2"]}</h3><p class="tel"><a href="tel:+6281314414789">+62 813 1441 4789</a></p><p>Email: pnpasaf.bp2mi@gmail.com<br><span class="small">{c["c2l"]}</span><sup><a href="#src">[1]</a></sup></p></div>
<h3>{c["c_jp_h"]}</h3>
<div class="contact"><h3>{c["c3"]}</h3><p class="tel"><a href="tel:0570001715">0570-001-715</a></p><p>{c["c3d"]}<sup><a href="#src">[6]</a></sup></p></div></section>''')
    src = "".join(f'<li>{n}<br><a href="{u}">{u}</a></li>' for n, u in SRC)
    b.append(f'<aside class="trust" id="src"><h2>{c["tr_h"]}</h2><div class="money">{c["money"]}</div><h3>{c["src_h"]}</h3><ol>{src}</ol><h3>{c["log_h"]}</h3><ul><li>{c["log"]}</li></ul><a class="btn" href="#">{c["fix"]}</a></aside></main>')
    b.append(f'<footer><div class="wrap"><ul><li><a href="{c["about_url"]}">{c["about"]}</a></li><li>{tx["site"]}</li></ul></div></footer></body></html>')
    out = h + "\n".join(b)
    assert "{{" not in out
    open(os.path.join(D, f"lpk-{lang}.html"), "w", encoding="utf-8").write(out)
    print(lang, len(out))

for l in ("ja", "id"): build(l)
