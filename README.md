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

## 訪問者カウンター（人だけを数える）
- 全ページの `<head>` に `/assets/count.js`（`src/finish.py` の `COUNT`）。ページを5秒表示するか、スクロール・タップしたときに1回だけ `/api/hit` に送る。ボットの多くは数えない。
- `worker/index.js` の `hit()` が D1（binding `DB`）の表 `hits` に1行保存。IP は保存せず、その日だけの目印 `vid` に変える。表の作り方は `stats/schema.sql`、集計例は `stats/queries.sql`。
- 運営者の端末を数えないようにするには、その端末で一度 `https://tetsuzukinavi.org/ja/?count=off` を開く（戻すときは `?count=on`）。
