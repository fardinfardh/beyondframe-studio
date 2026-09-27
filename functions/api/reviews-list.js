// GET /api/reviews-list?key=ADMIN_KEY  — admin: list all reviews
const J = (o, st = 200) => new Response(JSON.stringify(o), { status: st, headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } });

export async function onRequestGet({ request, env }) {
  const url = new URL(request.url);
  const key = url.searchParams.get('key') || request.headers.get('x-admin-key') || '';
  if (!env.ADMIN_KEY || key !== env.ADMIN_KEY) return J({ ok: false, error: 'Unauthorized' }, 401);
  if (!env.REVIEWS) return J({ ok: false, error: 'Storage not configured.' }, 500);
  const out = [];
  let cursor;
  do {
    const list = await env.REVIEWS.list({ prefix: 'review:', cursor });
    for (const k of list.keys) { const v = await env.REVIEWS.get(k.name); if (v) out.push(JSON.parse(v)); }
    cursor = list.list_complete ? null : list.cursor;
  } while (cursor);
  out.sort((a, b) => String(b.created || '').localeCompare(String(a.created || '')));
  return J({ ok: true, reviews: out });
}
