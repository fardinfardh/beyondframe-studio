// Cloudflare Pages Function — POST /api/contact
// Sends contact form submissions to hello@beyondframe.studio via Resend.
// Requires env var RESEND_API_KEY to be set in the Cloudflare Pages project settings.

export async function onRequestPost(context) {
  const { request, env } = context;

  let data;
  try {
    data = await request.json();
  } catch (e) {
    return json({ error: "Invalid request body" }, 400);
  }

  const name = (data.name || "").toString().trim();
  const email = (data.email || "").toString().trim();
  const subject = (data.subject || "").toString().trim();
  const message = (data.message || "").toString().trim();
  const honeypot = (data.company || "").toString().trim();

  // Honeypot: silently accept but do nothing (bot trap)
  if (honeypot) {
    return json({ ok: true });
  }

  if (!name || !email || !subject || !message) {
    return json({ error: "Please fill in all required fields." }, 400);
  }
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    return json({ error: "Please provide a valid email address." }, 400);
  }

  const apiKey = env.RESEND_API_KEY;
  if (!apiKey) {
    return json({ error: "Email service is not configured yet." }, 500);
  }

  const fromAddress = env.CONTACT_FROM_ADDRESS || "Beyond Frame Website <onboarding@resend.dev>";
  const toAddress = env.CONTACT_TO_ADDRESS || "hello@beyondframe.studio";

  const escape = (str) => str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  const html = `
    <div style="font-family:sans-serif;font-size:15px;color:#171512;line-height:1.6;">
      <h2 style="font-family:serif;">New message from beyondframe.studio</h2>
      <p><strong>Name:</strong> ${escape(name)}</p>
      <p><strong>Email:</strong> ${escape(email)}</p>
      <p><strong>Subject:</strong> ${escape(subject)}</p>
      <p><strong>Message:</strong></p>
      <p style="white-space:pre-wrap;border-left:3px solid #a8481f;padding-left:14px;">${escape(message)}</p>
    </div>
  `;

  try {
    const resendRes = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${apiKey}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        from: fromAddress,
        to: [toAddress],
        reply_to: email,
        subject: `[Beyond Frame Contact] ${subject}`,
        html
      })
    });

    if (!resendRes.ok) {
      const errText = await resendRes.text();
      console.log("Resend error:", errText);
      return json({ error: "Could not send your message right now." }, 502);
    }

    return json({ ok: true });
  } catch (err) {
    return json({ error: "Could not send your message right now." }, 500);
  }
}

function json(obj, status = 200) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json" }
  });
}
