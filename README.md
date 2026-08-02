# Beyond Frame — beyondframe.studio

Static site for Beyond Frame photography mentorship, deployed on Cloudflare Pages.

- `/*.html` — pages (plain static HTML, generated from `build.py`)
- `/assets` — CSS, JS, images
- `/downloads/The-Direction-Audit.pdf` — standalone download used by MailerLite automations (not linked anywhere on the site)
- `/functions/api/contact.js` — Cloudflare Pages Function that sends the Contact form to hello@beyondframe.studio via Resend

## Editing content
Edit `build.py`, then run `python3 build.py` to regenerate the `.html` files.

## Environment variables (set in Cloudflare Pages project settings)
- `RESEND_API_KEY` — Resend API key (secret)
- `CONTACT_FROM_ADDRESS` — optional, defaults to Resend's shared sandbox sender
- `CONTACT_TO_ADDRESS` — optional, defaults to hello@beyondframe.studio
