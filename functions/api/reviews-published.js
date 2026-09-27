// GET /api/reviews-published  — public: approved reviews only (for the Testimonials page)
const J = (o) => new Response(JSON.stringify(o), { headers: { 'Content-Type': 'application/json', 'Cache-Control': 'public, max-age=120' } });

export async function onRequestGet({ env }) {
  if (!env.REVIEWS) return J({ ok: true, reviews: [] });
  const out = [];
  let cursor;
  do {
    const list = await env.REVIEWS.list({ prefix: 'review:', cursor });
    for (const k of list.keys) {
      const v = await env.REVIEWS.get(k.name);
      if (!v) continue;
      const r = JSON.parse(v);
      if (r.status === 'approved' && r.consent) out.push({ name: r.name, country: r.country, profession: r.profession, rating: r.rating, comment: r.comment, photo: r.photo, created: r.created });
    }
    cursor = list.list_complete ? null : list.cursor;
  } while (cursor);
  out.sort((a, b) => String(b.created || '').localeCompare(String(a.created || '')));
  return J({ ok: true, reviews: out });
}
