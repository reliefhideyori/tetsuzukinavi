# 手続きナビ (Tetsuzuki Navi)

https://tetsuzukinavi.org — 日本で働く人のための公式情報ガイド（日本語 /ja/、インドネシア語 /id/）。

- `site/` 公開されるページ（Cloudflare Workers の静的アセット）。`main` に push すると自動で公開されます。
- `src/` ページを作るスクリプトと元データ。公式の数字は `src/data.py` に出典と確認日つきでまとめています。

## ページを足す・直す
1. `src/page_<slug>.py` を書く（ja/id の文章と出典）
2. `cd src && python3 addpage.py <slug> && python3 finish.py && python3 seo.py`
3. `main` に push すると公開されます

## 雇用契約書チェック（/kontrak）
`src/build_kontrak.py` が `site/{ja,id}/kontrak.html` を書き出します（入力はブラウザ内だけで計算）。最低賃金は `src/data.py` の値を使います。
`cd src && python3 build_kontrak.py && python3 finish.py && python3 seo.py`
