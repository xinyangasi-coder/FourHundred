# FourHundred

Static U.S. money-information site for people already under financial pressure. Education only. Not advice.

Live site: https://fourhundredx.com

What to open: Monday → `ops/monday.md`. File jobs → `ops/files.md`. New page chrome → `templates/chrome.html`.

Live pages are the `.html` files. Do not edit `content/*.md` expecting the site to change. Do not run `build.py` on Monday.

## Hosting

- Registrar: Porkbun (`fourhundredx.com`)
- DNS + HTTPS + Pages: Cloudflare
- Preview: `fourhundred.pages.dev`
- Build command: `exit 0`
- Output directory: `/`

Do not enable SPA fallback. `404.html` must stay at the repo root.
