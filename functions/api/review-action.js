// POST /api/review-action  { key, id, action }  action = approve | reject | delete
const J = (o, st = 200) => new Response(JSON.stringify(o), { status: st, headers: { 'Content-Type': 'application/json' } });

export async function onRequestPost({ request, env }) {
  const b = await request.json().catch(() => ({}));
  if (!env.ADMIN_KEY || b.key !== env.ADMIN_KEY) return J({ ok: false, error: 'Unauthorized' }, 401);
  if (!env.REVIEWS) return J({ ok: false, error: 'Storage not configured.' }, 500);
  const rk = 'review:' + String(b.id || '');
  const v = await env.REVIEWS.get(rk);
  if (!v) return J({ ok: false, error: 'Review not found.' }, 404);
  if (b.action === 'delete') { await env.REVIEWS.delete(rk); return J({ ok: true }); }
  const rec = JSON.parse(v);
  if (b.action === 'approve') rec.status = 'approved';
  else if (b.action === 'reject') rec.status = 'rejected';
  else return J({ ok: false, error: 'Unknown action.' }, 400);
  await env.REVIEWS.put(rk, JSON.stringify(rec));
  return J({ ok: true });
}
