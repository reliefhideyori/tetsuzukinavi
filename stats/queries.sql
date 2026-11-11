-- よく使う集計（Claude が Cloudflare コネクタの D1 クエリで実行する）
-- 1) 日別の人数とページビュー（直近14日）
SELECT day, COUNT(DISTINCT vid) AS people, COUNT(*) AS views FROM hits
WHERE day >= date('now', '+9 hours', '-13 days') GROUP BY day ORDER BY day;
-- 2) 国別の人数（直近7日）
SELECT country, COUNT(DISTINCT vid || day) AS people FROM hits
WHERE day >= date('now', '+9 hours', '-6 days') GROUP BY country ORDER BY people DESC;
-- 3) よく読まれたページ（直近7日）
SELECT path, COUNT(*) AS views, COUNT(DISTINCT vid || day) AS people FROM hits
WHERE day >= date('now', '+9 hours', '-6 days') GROUP BY path ORDER BY views DESC LIMIT 20;
-- 4) どこから来たか（直近7日）
SELECT CASE ref WHEN '' THEN '(直接・アプリ内)' ELSE ref END AS source, COUNT(DISTINCT vid || day) AS people FROM hits
WHERE day >= date('now', '+9 hours', '-6 days') GROUP BY source ORDER BY people DESC;
