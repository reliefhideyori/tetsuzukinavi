// 手続きナビ: 静的ページを配信し、連絡フォーム (/api/contact) をメールで運営者に届ける。
// /api/hit は人の訪問だけを数える（site/assets/count.js から送られる）。D1 (binding DB) に1行ずつ保存。
import { EmailMessage } from "cloudflare:email";

const FROM = "form@tetsuzukinavi.org";
const TO = "tetsuzukinavi@gmail.com";

const b64 = (s) => btoa(String.fromCharCode(...new TextEncoder().encode(s)));
const b64wrap = (s) => b64(s).replace(/.{1,76}/g, "$&\r\n");
const clip = (v, n) => String(v ?? "").slice(0, n).trim();

async function contact(request, env) {
  const f = await request.formData();
  const lang = f.get("lang") === "ja" ? "ja" : "id";
  const back = new URL(`/${lang}/thanks.html`, request.url);
  if (clip(f.get("_honey"), 100)) return Response.redirect(back, 303); // bot
  const message = clip(f.get("message"), 5000);
  if (!message) return Response.redirect(new URL(`/${lang}/contact.html`, request.url), 303);
  const kind = clip(f.get("kind"), 50), page = clip(f.get("page"), 200);
  const email = clip(f.get("email"), 200).replace(/[\r\n]/g, "");
  const body = [
    `種類 / Jenis: ${kind}`,
    `ページ / Halaman: ${page}`,
    `言語 / Bahasa: ${lang}`,
    `返信先 / Email: ${email || "(なし)"}`,
    "",
    message,
  ].join("\n");
  const headers = [
    `From: =?UTF-8?B?${b64("手続きナビ フォーム")}?= <${FROM}>`,
    `To: ${TO}`,
    `Subject: =?UTF-8?B?${b64(`[手続きナビ] ${kind} (${lang})`)}?=`,
    `Date: ${new Date().toUTCString()}`,
    `Message-ID: <${crypto.randomUUID()}@tetsuzukinavi.org>`,
    ...(/^[^\s@<>]+@[^\s@<>]+$/.test(email) ? [`Reply-To: ${email}`] : []),
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=UTF-8",
    "Content-Transfer-Encoding: base64",
  ];
  const raw = headers.join("\r\n") + "\r\n\r\n" + b64wrap(body);
  await env.MAIL.send(new EmailMessage(FROM, TO, raw));
  return Response.redirect(back, 303);
}

const BOT_UA = /bot|crawl|spider|slurp|headless|lighthouse|preview|facebookexternalhit|python|curl|wget|go-http|java\//i;

// 訪問者の目印：日付＋IP＋ブラウザ名のハッシュの先頭だけ（IP そのものは保存しない。日付が変わると別の値になる）
async function visitorId(day, ip, ua) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(`tn|${day}|${ip}|${ua}`));
  return [...new Uint8Array(buf)].slice(0, 8).map((b) => b.toString(16).padStart(2, "0")).join("");
}

async function hit(request, env) {
  const ok = new Response(null, { status: 204 });
  if (!env.DB) return ok;
  const ua = request.headers.get("user-agent") || "";
  if (!ua || BOT_UA.test(ua)) return ok;
  const origin = request.headers.get("origin");
  if (origin && new URL(origin).hostname !== new URL(request.url).hostname) return ok;
  const text = await request.text();
  if (text.length > 1000) return ok;
  let d; try { d = JSON.parse(text); } catch { return ok; }
  const path = clip(d.p, 200);
  if (!path.startsWith("/")) return ok;
  const now = new Date(Date.now() + 9 * 3600e3); // 日本時間で日付を切る
  const day = now.toISOString().slice(0, 10);
  const ip = request.headers.get("cf-connecting-ip") || "";
  const lang = path.split("/")[1] || "";
  const device = /Mobi|Android|iPhone/i.test(ua) ? "mobile" : "desktop";
  await env.DB.prepare(
    "INSERT INTO hits (ts, day, path, lang, country, ref, vid, device, how) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
  ).bind(Date.now(), day, path, clip(lang, 5), clip(request.cf?.country, 4), clip(d.r, 100), await visitorId(day, ip, ua), device, clip(d.h, 20)).run();
  return ok;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/contact") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      try { return await contact(request, env); }
      catch (e) { console.error(e); return new Response("送信できませんでした。時間をおいてもう一度お試しください。 / Gagal mengirim. Coba lagi nanti.", { status: 500, headers: { "content-type": "text/plain; charset=utf-8" } }); }
    }
    if (url.pathname === "/api/hit") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      try { return await hit(request, env); }
      catch (e) { console.error(e); return new Response(null, { status: 204 }); }
    }
    return env.ASSETS.fetch(request);
  },
};
