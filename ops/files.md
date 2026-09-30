# Files you actually touch

Live site = the `.html` files at the repo root and in `start-here/`, `foundations/`, `playbook/`, `evidence/`.
Cloudflare Pages publishes those files. Markdown in `content/` is not what readers see.

## Monday only

| File | Role |
|---|---|
| `ops/monday.md` | The Monday checklist. Open this first. |
| `playbook/index.html` | Playbook shelf: This week vs Earlier. |
| `index.html` | Home This week Playbook card + week date. |
| `playbook/NEW-SLUG.html` | The new method page, only if you ship. |
| `templates/chrome.html` | Copy header/footer/icon from here for a new page. |

## Read on Monday, do not edit

| File | Role |
|---|---|
| `method.html` | Publish rules. Use as a gate, not a page to rewrite. |
| `playbook/due-date.html` | Current This week method (until you replace it). |
| `about.html` | Who publishes. Irrelevant to the weekly swap. |

## Other live rooms (not Monday)

Situation paths, sheets, Foundations, Evidence, AI, legal pages. Edit when that room is wrong, not because it is Monday.

## Plumbing

`css/styles.css`, `favicon.svg`, `robots.txt`, `sitemap.xml`, `templates/README.md`.
`build.py` and `content/*.md` are not the live site. Do not run or edit them expecting Monday to publish.
