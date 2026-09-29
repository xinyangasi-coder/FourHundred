# FourHundred

Static U.S. money-information site for people already under financial pressure. Education only. Not advice.

Site root is this folder (`index.html` at the top). Weekly updates: edit the markdown in `/content`, run `python3 build.py`, commit the generated HTML.

## Cloudflare Pages

1. Push this repo to GitHub.
2. In Cloudflare: Workers & Pages → Create → Pages → Connect to Git.
3. Build command: `exit 0`
4. Output directory: `/`
5. After the first `*.pages.dev` URL works, add the custom domain.

Do not enable SPA fallback. `404.html` must stay at the repo root.
