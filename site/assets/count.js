// 手続きナビ: 人の訪問だけを数える小さなカウンター（Cookie なし）。
// ページを5秒以上表示するか、スクロール・タップ・キー入力があったときに1回だけ送る。
(function () {
  try {
    var u = new URL(location.href);
    if (u.searchParams.get("count") === "off") localStorage.setItem("tn_nocount", "1");
    if (u.searchParams.get("count") === "on") localStorage.removeItem("tn_nocount");
    if (localStorage.getItem("tn_nocount") === "1") return; // 運営者自身の端末
  } catch (e) {}
  if (navigator.webdriver || /bot|crawl|spider|slurp|headless|lighthouse|preview|facebookexternalhit/i.test(navigator.userAgent)) return;
  var sent = false, timer = null, shown = 0;
  function send(how) {
    if (sent) return; sent = true;
    var ref = "";
    try { var r = new URL(document.referrer); if (r.hostname !== location.hostname) ref = r.hostname; } catch (e) {}
    var data = JSON.stringify({ p: location.pathname, r: ref, h: how, w: screen.width });
    if (!(navigator.sendBeacon && navigator.sendBeacon("/api/hit", data)))
      fetch("/api/hit", { method: "POST", body: data, keepalive: true });
  }
  function tick() {
    clearTimeout(timer);
    if (document.visibilityState === "visible") timer = setTimeout(function () { send("time"); }, 5000 - shown);
  }
  document.addEventListener("visibilitychange", tick);
  ["scroll", "pointerdown", "keydown"].forEach(function (e) {
    addEventListener(e, function () { send(e); }, { once: true, passive: true });
  });
  tick();
})();
