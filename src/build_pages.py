"""Generic builder for content pages (ja, id). Each page = list of blocks. Reuses header/CSS of template.html."""
import re, os, json
D = os.path.dirname(__file__)
tpl = open(os.path.join(D, "template.html"), encoding="utf-8").read()
head = tpl.split("<main")[0]
TXT = {"ja": {"html_lang":"ja","site":"手続きナビ","site_sub":"日本で暮らす・働くための公式情報ガイド","badge1":"公式の情報だけ","badge2":"毎週確認","badge3":"紹介料なし","tr_other_lang":"Bahasa Indonesia","font":"Noto+Sans+JP:wght@400;700","font_family":'"Noto Sans JP", "Hiragino Sans", "Yu Gothic", "Meiryo", sans-serif',
              "toc":"このページの内容","tr_h":"この情報について","src_h":"出典（確認日：2026年11月5日）","log_h":"変更履歴","log":"2026年11月5日　第1版を公開","money":"<b>このサイトの収入は広告だけです。</b>LPK、仲介業者、会社から紹介料は受け取っていません。","fix":"間違いを見つけたら教えてください","about":"運営者と方針","crumb":"日本で働く",
              "updated":"最終確認日：2026年11月5日（毎週確認）　／　出典：日本の省庁・公的機関の公式情報（ページの最後に一覧）","related":"関連するページ"},
       "id": {"html_lang":"id","site":"Tetsuzuki Navi","site_sub":"Panduan informasi resmi untuk tinggal dan bekerja di Jepang","badge1":"Hanya sumber resmi","badge2":"Dicek tiap minggu","badge3":"Tanpa komisi","tr_other_lang":"日本語","font":"Noto+Sans:wght@400;700","font_family":'"Noto Sans", "Segoe UI", Roboto, sans-serif',
              "toc":"Isi halaman ini","tr_h":"Tentang informasi ini","src_h":"Sumber (dicek: 5 November 2026)","log_h":"Riwayat perubahan","log":"5 November 2026  Versi 1 diterbitkan","money":"<b>Pendapatan situs ini hanya dari iklan.</b> Kami tidak menerima komisi dari LPK, agen, atau perusahaan.","fix":"Laporkan jika ada kesalahan","about":"Pengelola dan kebijakan","crumb":"Bekerja di Jepang",
              "updated":"Terakhir dicek: 5 November 2026 (dicek tiap minggu)  /  Sumber: informasi resmi kementerian dan lembaga publik Jepang (daftar di bagian bawah)","related":"Halaman terkait"}}
ABOUT = {"ja": "https://claude.ai/artifact/2tPzvnjGiCfbMEjD61wUWS", "id": "https://claude.ai/artifact/Bc82QWebd8N6QCPFHtGBHe"}
LINKS = json.load(open(os.path.join(D, "links.json"))) if os.path.exists(os.path.join(D, "links.json")) else {}

EXTRA_CSS = """<style>
ol.steps { list-style: none; padding: 0; counter-reset: st; }
ol.steps li { position: relative; padding: 0 0 var(--s2) 40px; margin: 0; }
ol.steps li::before { counter-increment: st; content: counter(st); position: absolute; left: 0; top: 0; width: 28px; height: 28px; border: 2px solid var(--key); color: var(--key); border-radius: 50%; display: grid; place-items: center; font-size: 14px; font-weight: 700; }
ol.steps li:not(:last-child)::after { content: ""; position: absolute; left: 14px; top: 32px; bottom: 4px; border-left: 2px solid var(--line); }
ol.steps b { display: block; }
ol.steps .when { display: inline-block; font-size: 12px; font-weight: 700; color: var(--key); border: 1px solid var(--key); border-radius: 4px; padding: 0 6px; margin-bottom: 4px; }
.fact { border-left: 6px solid var(--key); background: var(--bg-soft); padding: var(--s2); margin-bottom: var(--s2); }
.fact h3 { margin-top: 0; }
.cmp { overflow-x: auto; margin-bottom: var(--s2); }
.cmp table { min-width: 34rem; font-size: 14px; }
.cmp th[scope=row] { background: var(--bg-sub); white-space: nowrap; }
.cmp thead th { font-size: 14px; }
.cmp-note { font-size: 14px; color: var(--fg-sub); }
.related a { display: block; padding: 12px 0; border-bottom: 1px solid var(--line); font-weight: 700; }
</style>
</head>"""

def sup(n): return f'<sup><a href="#src">[{n}]</a></sup>' if n else ""

def render(page, lang):
    p = page[lang]; tx = dict(TXT[lang]); tx["title"] = p["title"]
    h = re.sub(r"\{\{(\w+)\}\}", lambda m: tx[m.group(1)], head).replace("</head>", EXTRA_CSS, 1)
    out = ['<main class="wrap">',
           f'<nav class="crumb" aria-label="breadcrumb"><ol><li><a href="#">{tx["site"]}</a></li><li><a href="#">{tx["crumb"]}</a></li><li>{p["crumb_last"]}</li></ol></nav>',
           f'<h1>{p["h1"]}</h1><p class="lead">{p["lead"]}</p><p class="updated">{tx["updated"]}</p>']
    if p.get("notice"):
        out.append(f'<div class="notice"><h2>{p["notice"][0]}</h2><p>{p["notice"][1]}</p></div>')
    secs = p["sections"]
    out.append(f'<nav class="toc"><h2>{tx["toc"]}</h2><ol>' + "".join(f'<li><a href="#s{i+1}">{s["h"]}</a></li>' for i, s in enumerate(secs)) + '</ol></nav>')
    for i, s in enumerate(secs):
        b = [f'<section id="s{i+1}"><h2>{s["h"]}</h2>']
        for blk in s["blocks"]:
            k = blk[0]
            if k == "p": b.append(f'<p>{blk[1]}</p>')
            elif k == "fact": b.append(f'<div class="fact"><h3>{blk[1]}</h3><p>{blk[2]}{sup(blk[3] if len(blk) > 3 else "")}</p></div>')
            elif k == "warn": b.append(f'<div class="notice warn"><p>{blk[1]}</p></div>')
            elif k == "note": b.append(f'<div class="notice"><p>{blk[1]}</p></div>')
            elif k == "steps":
                lis = []
                for st in blk[1]:
                    when = f'<span class="when">{st[0]}</span>' if st[0] else ""
                    lis.append(f'<li>{when}<b>{st[1]}</b>{st[2]}{sup(st[3] if len(st) > 3 else "")}</li>')
                b.append('<ol class="steps">' + "".join(lis) + '</ol>')
            elif k == "table":
                cols, rows = blk[1], blk[2]
                th = "".join(f'<th scope="col">{c}</th>' for c in cols)
                tr = "".join('<tr><th scope="row">' + r[0] + '</th>' + "".join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rows)
                b.append(f'<div class="cmp" role="region" tabindex="0"><table><thead><tr><th></th>{th}</tr></thead><tbody>{tr}</tbody></table></div>')
                if len(blk) > 3: b.append(f'<p class="cmp-note">{blk[3]}</p>')
            elif k == "dl":
                b.append('<dl class="rows">' + "".join(f'<div><dt>{a}</dt><dd>{d}{sup(n)}</dd></div>' for a, d, n in blk[1]) + '</dl>')
            elif k == "details":
                b.append("".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in blk[1]))
            elif k == "related":
                b.append('<div class="related">' + "".join(f'<a href="{LINKS.get(key, {}).get(lang, "#")}">{label}</a>' for key, label in blk[1]) + '</div>')
        b.append('</section>')
        out.append("".join(b))
    src = "".join(f'<li>{n}<br><a href="{u}">{u}</a></li>' for n, u in page["sources"])
    out.append(f'<aside class="trust" id="src"><h2>{tx["tr_h"]}</h2><div class="money">{tx["money"]}</div><h3>{tx["src_h"]}</h3><ol>{src}</ol><h3>{tx["log_h"]}</h3><ul><li>{tx["log"]}</li></ul><a class="btn" href="#">{tx["fix"]}</a></aside></main>')
    out.append(f'<footer><div class="wrap"><ul><li><a href="{ABOUT[lang]}">{tx["about"]}</a></li><li>{tx["site"]}</li></ul></div></footer></body></html>')
    html = h + "\n".join(out)
    assert "{{" not in html
    return html

if __name__ == "__main__":
    import importlib.util, glob
    for f in sorted(glob.glob(os.path.join(D, "page_*.py"))):
        spec = importlib.util.spec_from_file_location("pg", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for lang in ("ja", "id"):
            name = f"{m.SLUG}-{lang}.html"
            open(os.path.join(D, name), "w", encoding="utf-8").write(render(m.PAGE, lang))
            print("wrote", name)
