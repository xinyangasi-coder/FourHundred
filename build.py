#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).parent
CONTENT = ROOT.parent

def md_to_html(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*-+", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if re.match(r"^\|?\s*-+", lines[i]):
                    i += 1
                    continue
                cells = [c.strip() for c in lines[i].strip("|").split("|")]
                rows.append(cells)
                i += 1
            if rows:
                head, *body = rows
                html = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
                for row in body:
                    html += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                html += "</tbody></table>"
                out.append(html)
            continue
        if line.startswith("> "):
            quote = []
            while i < len(lines) and lines[i].startswith("> "):
                quote.append(lines[i][2:])
                i += 1
            out.append(f"<blockquote><p>{inline(' '.join(quote))}</p></blockquote>")
            continue
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\s*[-*]\s+', '', lines[i]))}</li>")
                i += 1
            out.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(f"<li>{inline(re.sub(r'^\s*\d+\.\s+', '', lines[i]))}</li>")
                i += 1
            out.append("<ol>" + "".join(items) + "</ol>")
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{inline(line[2:])}</h1>")
        elif line.strip() == "---":
            out.append("<hr>")
        elif line.strip() == "":
            out.append("")
        else:
            para = [line]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^(#|---|[-*]\s|\d+\.\s|>\s|\|)", lines[i + 1]):
                i += 1
                para.append(lines[i])
            out.append(f"<p>{inline(' '.join(para))}</p>")
        i += 1
    return "\n".join(out)

def inline(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"(https://[^\s<]+)", r'<a href="\1">\1</a>', s)
    return s

HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — FourHundred</title>
  <meta name="description" content="U.S. money information for people already under financial pressure. Education only.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;550;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <header class="site-header">
    <div class="wrap header-inner">
      <a class="wordmark" href="{home}">FourHundred</a>
      <nav class="nav">
        <a href="{startx}">Start here</a>
        <a href="{foundx}">Foundations</a>
        <a href="{playx}">Playbook</a>
        <a href="{evidx}">Evidence</a>
        <a href="{meth}">Method</a>
        <a href="{ai}">AI</a>
      </nav>
    </div>
  </header>
"""

FOOTER = """
  <footer class="site-footer">
    <div class="wrap">
      <p class="legal">FourHundred is an education tool. It is not personalized financial, tax, or legal advice.</p>
      <p><a href="{home}">Home</a> · <a href="{meth}">Method</a> · <a href="{ai}">AI tools</a> · <a href="{disc}">Disclaimer</a></p>
      <p>Minimum launch, week of September 29, 2026. United States only.</p>
    </div>
  </footer>
</body>
</html>
"""

def paths(depth: int):
    prefix = "../" * depth
    return {
        "css": f"{prefix}css/styles.css",
        "home": f"{prefix}index.html",
        "found": f"{prefix}foundations/400-test.html",
        "play": f"{prefix}playbook/minimum-payment.html",
        "evid": f"{prefix}evidence/400.html",
        "meth": f"{prefix}method.html",
        "disc": f"{prefix}disclaimer.html",
        "bills": f"{prefix}start-here/bills-this-month.html",
        "card": f"{prefix}start-here/card-balance.html",
        "coll": f"{prefix}start-here/collections.html",
        "tight": f"{prefix}start-here/income-still-tight.html",
        "cash": f"{prefix}foundations/7-day-cash-map.html",
        "ai": f"{prefix}ai-tools.html",
        "evid2": f"{prefix}evidence/unmanageable-debt.html",
        "evid3": f"{prefix}evidence/bills-last-month.html",
        "evid4": f"{prefix}evidence/card-balances-pressure.html",
        "evid5": f"{prefix}evidence/unexpected-expenses.html",
        "evidx": f"{prefix}evidence/index.html",
        "foundx": f"{prefix}foundations/index.html",
        "playx": f"{prefix}playbook/index.html",
        "startx": f"{prefix}start-here/index.html",
    }


def write_article(rel_path: str, title: str, layer: str, meta: str, who: str, skip: str, md_file: Path, depth: int):
    p = paths(depth)
    body_md = md_file.read_text()
    # drop first heading; page title is in template
    body_md = re.sub(r"^# .*\n", "", body_md, count=1)
    body_md = re.sub(r"^Layer:.*\nWho this is for:.*\nWho should skip this:.*\n+", "", body_md)
    html = md_to_html(body_md)
    page = HEADER.format(title=title, **p)
    page += f"""
  <main class="wrap article">
    <p class="eyebrow">{layer}</p>
    <h1>{title}</h1>
    <p class="meta">{meta}</p>
    <div class="who"><strong>Who this is for.</strong> {who}<br><strong>Who should skip this.</strong> {skip}</div>
    {html}
  </main>
"""
    page += FOOTER.format(**p)
    dest = ROOT / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest)


def write_home():
    p = paths(0)
    page = HEADER.format(title="Money information for people already under pressure", **p)
    page += f"""
  <main>
    <section class="hero">
      <div class="wrap">
        <p class="eyebrow">United States · Education only</p>
        <h1>FourHundred</h1>
        <p class="deck">Money information for people already under pressure.</p>
        <p class="support">If a $400 bill would create a problem, start here. We show core money knowledge, current methods, and primary-source data. We do not give personalized advice.</p>
        <p class="chooser-label" id="chooser">What is true right now?</p>
        <div class="chooser">
          <a href="{p['bills']}">I may not make this month’s bills</a>
          <a href="{p['card']}">My credit card balance is growing</a>
          <a href="{p['found']}">I do not have a cash buffer</a>
          <a href="{p['bills']}">I got a bill I cannot pay</a>
          <a href="{p['tight']}">I earn enough and still run out</a>
          <a href="{p['coll']}">I am late, or in collections</a>
        </div>
        <p class="layers-line">Or browse the three layers: <a href="{p['foundx']}">Foundations</a> · <a href="{p['playx']}">Playbook</a> · <a href="{p['evidx']}">Evidence</a></p>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>This week</h2>
        <p class="sub">One item from each layer. Week of September 29, 2026.</p>
        <div class="week-grid">
          <article class="card">
            <p class="kicker">Foundation</p>
            <h3>The $400 test is a small-shock test, not a full emergency fund.</h3>
            <p>63 percent of U.S. adults would cover $400 with cash, savings, or a card paid off at the next statement. A card balance you carry is not that.</p>
            <a href="{p['found']}">Read the Foundation</a>
          </article>
          <article class="card">
            <p class="kicker">Playbook</p>
            <h3>The minimum payment keeps the account current. It does not retire the balance.</h3>
            <p>On a $2,000 balance at 22 percent APR, a typical first minimum puts most of the payment on interest. Use the warning box on your own statement first.</p>
            <a href="{p['play']}">Read the Playbook</a>
          </article>
          <article class="card">
            <p class="kicker">Evidence</p>
            <h3>37 percent would not use cash or its equivalent. That is not the same as 37 percent having zero dollars.</h3>
            <p>12 percent of adults said they could not pay $400 by any means. Definitions stay on the card.</p>
            <a href="{p['evid']}">Read the Evidence card</a>
          </article>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>Five gauges</h2>
        <p class="sub">National pictures, not a score for your household. Each card links to a definition.</p>
        <div class="gauges">
          <article class="gauge">
            <p class="kicker">$400 shock</p>
            <p class="state stable">Stable, 2022–2025</p>
            <p class="num">63%</p>
            <p>of U.S. adults would cover $400 with cash or its equivalent. Unchanged for four surveys, below 68 percent in 2021. 12 percent could not pay by any means.</p>
            <p class="source">Fed SHED 2025, released May 2026</p>
            <a href="{p['evid']}">Open the definition</a>
          </article>
          <article class="gauge">
            <p class="kicker">Bills last month</p>
            <p class="state stable">Similar to 2024</p>
            <p class="num">16%</p>
            <p>of U.S. adults did not pay all bills in the prior month. Same survey: 8 percent said someone in the family sometimes or often did not have enough to eat.</p>
            <p class="source">Fed SHED 2025, Economic Hardships</p>
            <a href="{p['evid3']}">Open the definition</a>
          </article>
          <article class="gauge">
            <p class="kicker">Unmanageable debt</p>
            <p class="state worse">Worse · highest in nine Pulse years</p>
            <p class="num">31%</p>
            <p>of U.S. households say they have a bit more or far more debt than is manageable. Up from 29 percent. Financially vulnerable households rose to 17 percent.</p>
            <p class="source">Financial Health Pulse 2026, September 2026</p>
            <a href="{p['evid2']}">Open the definition</a>
          </article>
          <article class="gauge">
            <p class="kicker">Card balances under pressure</p>
            <p class="state worse">Worse for that group</p>
            <p class="num">+$2,530</p>
            <p>average card-balance change, 2023 to 2025, among adults “finding it difficult to get by.” Adults “living comfortably” saw +$59.</p>
            <p class="source">Fed SHED 2025, credit records match</p>
            <a href="{p['evid4']}">Open the definition</a>
          </article>
          <article class="gauge">
            <p class="kicker">Most common surprise bill</p>
            <p class="state common">Common, not rare</p>
            <p class="num">30%</p>
            <p>of U.S. adults had a major vehicle repair or replacement in the prior 12 months. 59 percent had at least one major unexpected expense.</p>
            <p class="source">Fed SHED 2025, Economic Hardships</p>
            <a href="{p['evid5']}">Open the definition</a>
          </article>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2>How FourHundred is built</h2>
        <div class="build-grid">
          <article class="card">
            <h3>Foundations</h3>
            <p>Stay stable. We revise them when a definition or a law changes. Live now: the $400 test and the 7-day cash map.</p>
            <a href="{p['foundx']}">All Foundations</a>
          </article>
          <article class="card">
            <h3>Playbook</h3>
            <p>Updates weekly. One method, with who it is for and who should skip it. This week: minimum payments.</p>
            <a href="{p['playx']}">All Playbook pages</a>
          </article>
          <article class="card">
            <h3>Evidence</h3>
            <p>Updates when the source updates. Five live cards. Different surveys stay on different cards.</p>
            <a href="{p['evidx']}">All Evidence cards</a>
          </article>
        </div>
        <div class="ai-box">
          <p class="kicker">AI</p>
          <h3>What AI is allowed to do here</h3>
          <p>AI can help you understand a term on FourHundred, compare two methods we already published, or draft questions for a landlord, issuer, or nonprofit counselor. It should not pick a product, tell you to file anything, or receive live account access.</p>
          <a href="{p['ai']}">Read the AI tools page</a>
        </div>
        <p class="sub" style="margin-top:1.2rem">Figures on this page come from the Federal Reserve SHED 2025 report (May 2026) and the Financial Health Pulse 2026 U.S. Trends Report. <a href="https://www.federalreserve.gov/publications/2026-economic-well-being-of-us-households-in-2025-executive-summary.htm">Fed executive summary</a> · <a href="https://finhealthnetwork.org/">Financial Health Network</a></p>
      </div>
    </section>
  </main>
"""
    page += FOOTER.format(**p)
    (ROOT / "index.html").write_text(page)
    print("wrote index.html")


def write_evidence_index():
    p = paths(1)
    page = HEADER.format(title="Evidence", **p)
    page += f"""
  <main class="wrap article">
    <p class="eyebrow">Evidence</p>
    <h1>Evidence cards</h1>
    <p class="meta">Last reviewed September 29, 2026</p>
    <p>Each card is one number, one definition, and a list of what the number does not prove. Cards update when the source updates. Fed SHED and Financial Health Pulse stay on separate cards.</p>
    <div class="who"><strong>Who this is for.</strong> Readers who want the definition behind a Home gauge.<br><strong>Who should skip this.</strong> People who need a this-month action. Use Start here.</div>
    <h2>Live cards</h2>
    <ul>
      <li><a href="400.html">Would cover a $400 expense with cash or its equivalent</a> — 63 percent of U.S. adults. Fed SHED 2025.</li>
      <li><a href="bills-last-month.html">Did not pay all bills in full last month</a> — 16 percent of U.S. adults. Fed SHED 2025.</li>
      <li><a href="unmanageable-debt.html">Households with unmanageable debt</a> — 31 percent of U.S. households. Pulse 2026.</li>
      <li><a href="card-balances-pressure.html">Card balances among adults finding it difficult to get by</a> — +$2,530 from 2023 to 2025. Fed SHED matched to credit records.</li>
      <li><a href="unexpected-expenses.html">Major unexpected expenses in the prior 12 months</a> — 59 percent any shock; 30 percent a major vehicle repair. Fed SHED 2025, new questions.</li>
    </ul>
    <p>Related: <a href="{p['found']}">$400 Foundation</a> · <a href="{p['cash']}">7-day cash map</a> · <a href="{p['meth']}">Method</a></p>
  </main>
"""
    page += FOOTER.format(**p)
    dest = ROOT / "evidence/index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest)


def write_foundations_index():
    p = paths(1)
    page = HEADER.format(title="Foundations", **p)
    page += f"""
  <main class="wrap article">
    <p class="eyebrow">Foundations</p>
    <h1>Foundations</h1>
    <p class="meta">Last reviewed September 29, 2026</p>
    <p>Foundations stay stable. We revise them when a definition or a law changes, not when a headline moves. Each page gives shared language and one small action.</p>
    <div class="who"><strong>Who this is for.</strong> Readers who need the basic clock: this week’s cash, or a $400 shock.<br><strong>Who should skip this.</strong> People whose rent or utilities are already at risk today. Use Start here.</div>
    <h2>Live pages</h2>
    <ul>
      <li><a href="400-test.html">The $400 test and the three cash buffers</a> — whether a small shock becomes a carried card balance. Rung 1 is $400, not three months.</li>
      <li><a href="7-day-cash-map.html">A 7-day cash map</a> — whether the next week’s cash covers the next week’s required outflows, before any shock arrives.</li>
    </ul>
    <p>Not live yet: a three-month reserve page. Do not treat Rung 1 as that page.</p>
    <p>Related: <a href="{p['startx']}">Start here</a> · <a href="{p['evidx']}">Evidence</a> · <a href="{p['meth']}">Method</a></p>
  </main>
"""
    page += FOOTER.format(**p)
    dest = ROOT / "foundations/index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest)


def write_playbook_index():
    p = paths(1)
    page = HEADER.format(title="Playbook", **p)
    page += f"""
  <main class="wrap article">
    <p class="eyebrow">Playbook</p>
    <h1>Playbook</h1>
    <p class="meta">Last reviewed September 29, 2026</p>
    <p>Playbook updates weekly. One method per week, with who it is for and who should skip it. Old methods stay up if they are still accurate. They are dated.</p>
    <div class="who"><strong>Who this is for.</strong> Readers whose essentials are covered this month and who need one current method.<br><strong>Who should skip this.</strong> People who may miss rent, utilities, food, or medicine. Use Start here first.</div>
    <h2>This week</h2>
    <ul>
      <li><a href="minimum-payment.html">Why the minimum payment keeps a card balance alive</a> — the minimum keeps the account current. It does not retire the balance. Use the warning box on your own statement.</li>
    </ul>
    <p>Next methods are not published until this one has a week in the wild. No product picks live here.</p>
    <p>Related: <a href="{p['card']}">Card balance is growing</a> · <a href="{p['evid4']}">Card-balance Evidence</a> · <a href="{p['meth']}">Method</a></p>
  </main>
"""
    page += FOOTER.format(**p)
    dest = ROOT / "playbook/index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest)


def write_start_index():
    p = paths(1)
    page = HEADER.format(title="Start here", **p)
    page += f"""
  <main class="wrap article">
    <p class="eyebrow">Start here</p>
    <h1>Start here</h1>
    <p class="meta">Last reviewed September 29, 2026</p>
    <p>Pick the sentence that is true today. These paths are for this month, not for a lifetime plan.</p>
    <div class="who"><strong>Who this is for.</strong> Adults in the United States already under pressure.<br><strong>Who should skip this.</strong> Readers who only want a definition. Use Evidence or Foundations.</div>
    <h2>Live paths</h2>
    <ul>
      <li><a href="bills-this-month.html">I may not make this month’s bills</a> — also the path for “I got a bill I cannot pay.” Protect housing, utilities, food, and medicine first.</li>
      <li><a href="card-balance.html">My credit card balance is growing</a> — the number is rising or not falling while you pay. Leave if rent is at risk.</li>
      <li><a href="collections.html">I am late, or in collections</a> — name the stage: original company, collector, or court paper.</li>
      <li><a href="income-still-tight.html">I earn enough and still run out</a> — the paycheck looks fine and the month still ends empty, short, or on a card.</li>
    </ul>
    <h2>Uses a Foundation instead</h2>
    <ul>
      <li><a href="{p['found']}">I do not have a cash buffer</a> — goes to the $400 test. That page is the method.</li>
    </ul>
    <p>Related: <a href="{p['foundx']}">Foundations</a> · <a href="{p['playx']}">Playbook</a> · <a href="{p['home']}#chooser">Home chooser</a></p>
  </main>
"""
    page += FOOTER.format(**p)
    dest = ROOT / "start-here/index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page)
    print("wrote", dest)


def write_disclaimer():
    p = paths(0)
    page = HEADER.format(title="Disclaimer", **p)
    page += """
  <main class="wrap article">
    <p class="eyebrow">About</p>
    <h1>Disclaimer</h1>
    <p>FourHundred is an education tool for adults in the United States. It is not personalized financial, tax, or legal advice. Nothing on this site is an offer to sell a financial product or a substitute for a licensed professional who can see your full situation.</p>
    <p>Pages are dated. Evidence cards change when their primary source changes. If a number or definition is wrong, see Method for how corrections are handled.</p>
    <p>Minimum launch pages do not sell products and do not take referral fees.</p>
  </main>
"""
    page += FOOTER.format(**p)
    (ROOT / "disclaimer.html").write_text(page)


if __name__ == "__main__":
    write_home()
    write_disclaimer()
    write_article(
        "method.html",
        "Method",
        "About",
        "Last reviewed September 29, 2026 · 8 minutes",
        "Anyone using FourHundred who wants to know how pages are chosen, dated, and limited.",
        "Readers who only need a situation path today. Use Start here instead.",
        CONTENT / "FourHundred-method.md",
        0,
    )
    write_article(
        "foundations/400-test.html",
        "The $400 test and the three cash buffers",
        "Foundation",
        "Last reviewed September 29, 2026 · 9 minutes",
        "Anyone in the U.S. who would have to think twice about a few-hundred-dollar surprise.",
        "Readers whose cash buffer already covers several months of essential bills.",
        CONTENT / "FourHundred-foundation-400-test.md",
        1,
    )
    write_article(
        "playbook/minimum-payment.html",
        "Why the minimum payment keeps a card balance alive",
        "Playbook",
        "Last reviewed September 29, 2026 · 8 minutes",
        "People who are current on a card, or trying to stay current, and whose statement balance is not going away.",
        "Anyone who already pays the statement balance in full, or who has an active collection lawsuit.",
        CONTENT / "FourHundred-playbook-minimum-payment.md",
        1,
    )
    write_article(
        "evidence/400.html",
        "Would cover a $400 expense with cash or its equivalent",
        "Evidence",
        "Last reviewed September 29, 2026 · Card EV-400-SHED-2025",
        "Readers who want the definition behind the 63 percent figure.",
        "Readers looking for a personalized savings target. Use the Foundation instead.",
        CONTENT / "FourHundred-evidence-400.md",
        1,
    )
    write_article(
        "start-here/bills-this-month.html",
        "I may not make this month’s bills",
        "Start here",
        "Last reviewed September 29, 2026 · 30–45 minutes today",
        "Adults in the United States who already know this month’s money may not cover every bill.",
        "People whose bills are current and who only need a buffer or interest explanation.",
        CONTENT / "FourHundred-start-here-bills-this-month.md",
        1,
    )
    write_article(
        "start-here/card-balance.html",
        "My credit card balance is growing",
        "Start here",
        "Last reviewed September 29, 2026 · 25–40 minutes",
        "Adults in the United States whose card balance is higher than last month, or who keep paying and watch the number stay put.",
        "People who already pay in full, or whose rent and utilities are at risk this month.",
        CONTENT / "FourHundred-start-here-card-balance.md",
        1,
    )
    write_article(
        "start-here/collections.html",
        "I am late, or in collections",
        "Start here",
        "Last reviewed September 29, 2026 · 30–40 minutes",
        "Adults in the United States who missed a payment, received a collection call or letter, or saw an account leave the original company.",
        "People whose accounts are current, or who already have a lawyer handling a case.",
        CONTENT / "FourHundred-start-here-collections.md",
        1,
    )
    write_article(
        "start-here/income-still-tight.html",
        "I earn enough and still run out",
        "Start here",
        "Last reviewed September 29, 2026 · 30–40 minutes",
        "Adults in the United States whose pay looks fine on paper and whose month still ends empty, short, or on a card.",
        "People who cannot cover this month’s essentials, or who only need card-balance math.",
        CONTENT / "FourHundred-start-here-income-still-tight.md",
        1,
    )
    write_article(
        "foundations/7-day-cash-map.html",
        "A 7-day cash map",
        "Foundation",
        "Last reviewed September 29, 2026 · 8 minutes",
        "Anyone in the U.S. whose month looks possible on paper and still breaks in a particular week.",
        "Readers who already cannot cover this month’s essentials, or who only need the $400 definition.",
        CONTENT / "FourHundred-foundation-7-day-cash-map.md",
        1,
    )
    write_article(
        "ai-tools.html",
        "AI tools",
        "About",
        "Last reviewed September 29, 2026 · 7 minutes",
        "Readers who want a model to explain a FourHundred page, compare two published methods, or draft a question for a company or counselor.",
        "Anyone about to paste a statement, account number, Social Security number, or bank login into a chatbot.",
        CONTENT / "FourHundred-ai-tools.md",
        0,
    )
    write_article(
        "evidence/unmanageable-debt.html",
        "Households with unmanageable debt",
        "Evidence",
        "Last reviewed September 29, 2026 · Card EV-PULSE-DEBT-2026",
        "Readers who want the definition behind the 31 percent Pulse figure.",
        "Readers looking for a personalized payoff order. Use Start here instead.",
        CONTENT / "FourHundred-evidence-unmanageable-debt.md",
        1,
    )
    write_article(
        "evidence/bills-last-month.html",
        "Did not pay all bills in full last month",
        "Evidence",
        "Last reviewed September 29, 2026 · Card EV-SHED-BILLS-2025",
        "Readers who want the definition behind the 16 percent SHED figure.",
        "Readers who need a this-month payment order. Use Start here instead.",
        CONTENT / "FourHundred-evidence-bills-last-month.md",
        1,
    )
    write_article(
        "evidence/card-balances-pressure.html",
        "Card balances among adults finding it difficult to get by",
        "Evidence",
        "Last reviewed September 29, 2026 · Card EV-SHED-CC-WELLBEING-2025",
        "Readers who want the definition behind the +$2,530 figure.",
        "Readers who need a this-month card action. Use the growing-balance path instead.",
        CONTENT / "FourHundred-evidence-card-balances-pressure.md",
        1,
    )
    write_article(
        "evidence/unexpected-expenses.html",
        "Major unexpected expenses in the prior 12 months",
        "Evidence",
        "Last reviewed September 29, 2026 · Card EV-SHED-SHOCKS-2025",
        "Readers who want the definition behind the 59 percent and 30 percent shock figures.",
        "Readers who need to handle a bill this week. Use Start here instead.",
        CONTENT / "FourHundred-evidence-unexpected-expenses.md",
        1,
    )
    write_evidence_index()
    write_foundations_index()
    write_playbook_index()
    write_start_index()
