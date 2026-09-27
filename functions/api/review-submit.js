// POST /api/review-submit  — student submits a review (stored as "pending")
const J = (o, st = 200) => new Response(JSON.stringify(o), { status: st, headers: { 'Content-Type': 'application/json' } });
const s = (v, n) => String(v == null ? '' : v).slice(0, n).trim();

export async function onRequestPost({ request, env }) {
  try {
    if (!env.REVIEWS) return J({ ok: false, error: 'Storage not configured.' }, 500);
    const b = await request.json().catch(() => ({}));
    if (b._hp) return J({ ok: true });                 // honeypot: pretend success for bots
    if (!env.REVIEW_CODE || s(b.code, 64) !== env.REVIEW_CODE) return J({ ok: false, error: 'Invalid access code. Please check the code you were given.' }, 403);
    if (!s(b.name, 80) || !s(b.comment, 4000) || !b.rating) return J({ ok: false, error: 'Please add your name, a star rating, and your review.' }, 400);
    if (!b.consent) return J({ ok: false, error: 'Please tick the consent box so we may publish your review.' }, 400);
    const rating = Math.max(1, Math.min(5, parseInt(b.rating, 10) || 0));
    let photo = '';
    if (typeof b.photo === 'string' && b.photo.startsWith('data:image/') && b.photo.length < 700000) photo = b.photo;
    const id = Date.now().toString(36) + '-' + Math.random().toString(36).slice(2, 8);
    const rec = {
      id, status: 'pending', created: new Date().toISOString(),
      name: s(b.name, 80), country: s(b.country, 60), profession: s(b.profession, 90),
      rating, comment: s(b.comment, 4000), photo, consent: true
    };
    await env.REVIEWS.put('review:' + id, JSON.stringify(rec));
    return J({ ok: true });
  } catch (e) {
    return J({ ok: false, error: 'Something went wrong. Please try again.' }, 500);
  }
}
