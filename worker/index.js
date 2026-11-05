// 手続きナビ: 静的ページを配信し、連絡フォーム (/api/contact) をメールで運営者に届ける。
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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === "/api/contact") {
      if (request.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
      try { return await contact(request, env); }
      catch (e) { console.error(e); return new Response("送信できませんでした。時間をおいてもう一度お試しください。 / Gagal mengirim. Coba lagi nanti.", { status: 500, headers: { "content-type": "text/plain; charset=utf-8" } }); }
    }
    return env.ASSETS.fetch(request);
  },
};
