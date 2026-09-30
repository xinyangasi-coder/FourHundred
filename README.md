# FourHundred

Static U.S. money-information site for people already under financial pressure. Education only. Not advice.

Live site: https://fourhundredx.com

Site root is this folder (`index.html` at the top). Weekly updates: edit the markdown in `/content`, run `python3 build.py`, commit the generated HTML.

## Hosting

- Registrar: Porkbun (`fourhundredx.com`)
- DNS + HTTPS + Pages: Cloudflare
- Preview: `fourhundred.pages.dev`
- Build command: `exit 0`
- Output directory: `/`

Do not enable SPA fallback. `404.html` must stay at the repo root.
