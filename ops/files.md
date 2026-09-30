# File map — by job

Live site = the `.html` readers hit on fourhundredx.com.
Cloudflare Pages publishes those files as-is. Markdown in `content/` is not what readers see.

## Monday only

| File | Job |
|---|---|
| `ops/monday.md` | Monday script. Open this first. |
| `playbook/index.html` | Playbook shelf: This week vs Earlier. |
| `index.html` | Home. On Monday touch only the Playbook card and the week date. |
| `playbook/NEW-SLUG.html` | New method page, only if you ship. Copy chrome from `templates/chrome.html`. |
| `templates/chrome.html` | One copy of nav, icon, footer, sheet sentence. |

## Read on Monday, do not edit

| File | Job |
|---|---|
| `method.html` | Publish rules. Gate, not a rewrite target. |
| `ops/files.md` | This map. |
| `playbook/due-date.html` | Current This week method until replaced. |
| `playbook/minimum-payment.html` | Earlier method. Stays up. |
| `about.html` | Who publishes. Not part of the weekly swap. |

## Rooms (not Monday)

| File | Job |
|---|---|
| `start-here/index.html` | List of the six paths. |
| `start-here/bills-this-month.html` | Method: this month cannot cover every bill. |
| `start-here/bills-this-month-sheet.html` | One-page list + call script. |
| `start-here/bill-i-cannot-pay.html` | One invoice that will not fit. |
| `start-here/cash-buffer.html` | No thin cash buffer. |
| `start-here/card-balance.html` | Card balance rising or not falling. |
| `start-here/income-still-tight.html` | Pay looks fine, month still empties. |
| `start-here/collections.html` | Late, collector, or court paper. |
| `foundations/index.html` | Foundations shelf. |
| `foundations/400-test.html` | What the $400 test is and is not. |
| `foundations/7-day-cash-map.html` | Timing method + teaching table. |
| `foundations/7-day-cash-map-sheet.html` | Blank seven-day grid. |
| `evidence/index.html` | Evidence shelf. |
| `evidence/400.html` | SHED $400 cash-or-equivalent. |
| `evidence/bills-last-month.html` | SHED unpaid bills last month. |
| `evidence/unmanageable-debt.html` | Pulse unmanageable debt. |
| `evidence/card-balances-pressure.html` | SHED card balances under pressure. |
| `evidence/unexpected-expenses.html` | SHED surprise bills. |
| `ai-tools.html` | What a model may not do here. |
| `privacy.html` | What the static site does not collect. |
| `disclaimer.html` | Education only. |
| `404.html` | Missing page. Keep at repo root. |

## Plumbing

| File | Job |
|---|---|
| `css/styles.css` | Type, color, print. |
| `favicon.svg` | Tab icon. |
| `robots.txt` | Allow pages; block `/content/`, `/ops/`, `/templates/`. |
| `sitemap.xml` | Public URL list. |
| `templates/README.md` | How to use chrome.html. |
| `build.py` | Old generator. Do not run on Monday. |
| `content/*.md` | Stale drafts. Editing them does not change the live site. |
| `README.md` | Hosting notes + pointers to this map. |
