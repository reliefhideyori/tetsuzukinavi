-- D1 データベース tetsuzukinavi-stats の表（最初に1回だけ実行）
CREATE TABLE IF NOT EXISTS hits (
  ts INTEGER NOT NULL,      -- 送信時刻 (ミリ秒, UTC)
  day TEXT NOT NULL,        -- 日本時間の日付 YYYY-MM-DD
  path TEXT NOT NULL,       -- 例 /id/gaji
  lang TEXT,                -- ja / id
  country TEXT,             -- 国コード (Cloudflare が判定) 例 ID, JP
  ref TEXT,                 -- どこから来たか (外部サイトのドメイン。直接なら空)
  vid TEXT,                 -- その日の訪問者の目印 (IP は保存しない)
  device TEXT,              -- mobile / desktop
  how TEXT                  -- 数えたきっかけ: time(5秒表示) / scroll / pointerdown / keydown
);
CREATE INDEX IF NOT EXISTS hits_day ON hits(day);
