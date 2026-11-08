# Genereert de artikelpagina's uit één sjabloon. Uitvoeren: python3 _build/site.py
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://lexedit766.github.io/bibob-zorg./"
MAIL = "bibob@jurist.nl"
TODAY = "2026-11-08"

NAV = [
    ("bibob-onderzoek.html", "Bibob-onderzoek"),
    ("bibob-vragenformulier.html", "Vragenformulier"),
    ("kennisbank.html", "Kennisbank"),
    ("./#diensten", "Diensten"),
    ("./#contact", "Contact"),
]

KENNIS = [
    ("wet-bibob.html", "Wat is de Wet Bibob"),
    ("bibob-toets.html", "De Bibob-toets"),
    ("bibob-onderzoek.html", "Het Bibob-onderzoek"),
    ("bibob-vragenformulier.html", "Het vragenformulier"),
    ("negatief-bibob-advies.html", "Negatief advies en zienswijze"),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,300;1,6..72,400&family=IBM+Plex+Sans:wght@400;500&display=swap" rel="stylesheet">'

def header(current):
    items = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a></li>' for h, t in NAV)
    return f'''<header class="site">
  <div class="wrap nav">
    <a class="brand" href="./">Bibob voor zorgaanbieders <span>— mr. J. Smit</span></a>
    <nav aria-label="Hoofdnavigatie"><ul>{items}</ul></nav>
  </div>
</header>'''

def footer(current):
    links = " &nbsp;·&nbsp; ".join(f'<a href="{h}">{t}</a>' for h, t in [("kennisbank.html","Kennisbank"),("bibob-onderzoek.html","Bibob-onderzoek"),("negatief-bibob-advies.html","Zienswijze")] if h != current)
    return f'''<footer class="site">
  <div class="wrap">
    <span>© 2026 mr. J. Smit, jurist — Bibob voor zorgaanbieders</span>
    <span><a href="./">Home</a> &nbsp;·&nbsp; {links}</span>
    <span class="disclaimer">De informatie op deze site is algemeen van aard en geen juridisch advies voor uw situatie. Wetsartikelen verwijzen naar de Wet Bibob, tenzij anders vermeld.</span>
  </div>
</footer>'''

def contact(h2, p, subject):
    return f'''<section id="contact">
  <div class="wrap contact">
    <div>
      <h2>{h2}</h2>
      <p class="intro" style="margin-bottom:20px">{p}</p>
      <a class="cta" href="mailto:{MAIL}?subject={subject}">E-mail de brief</a>
    </div>
    <address>
      <strong>mr. J. Smit, jurist</strong><br>
      Juffrouw Idastraat 11<br>
      2513 BE Den Haag<br><br>
      <a href="mailto:{MAIL}">{MAIL}</a>
    </address>
  </div>
</section>'''

def faq_schema(faq):
    return [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]

def faq_html(faq):
    return '<div class="faq">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq) + "</div>"

def page(slug, title, desc, h1, intro, marge, body, faq, contact_h2, contact_p, subject, breadcrumb):
    url = BASE + slug
    graph = [
        {"@type": "Article", "headline": h1, "inLanguage": "nl", "datePublished": TODAY, "dateModified": TODAY,
         "author": {"@type": "Person", "name": "mr. J. Smit", "jobTitle": "jurist"}, "mainEntityOfPage": url,
         "about": ["Wet Bibob", "zorgaanbieders", "Wmo 2015", "Jeugdwet"]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE},
            {"@type": "ListItem", "position": 2, "name": breadcrumb, "item": url}]},
    ]
    if faq:
        graph.append({"@type": "FAQPage", "mainEntity": faq_schema(faq)})
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    faqsec = f"<h2>Veelgestelde vragen</h2>{faq_html(faq)}" if faq else ""
    html = f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="nl_NL">
{FONTS}
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(slug)}

<main class="wrap artikelpagina">
<aside class="marge" aria-label="Kerngegevens">
{marge}
</aside>

<article class="body">
  <h1>{h1}</h1>
  <p class="intro">{intro}</p>
{body}
{faqsec}
</article>
</main>

{contact(contact_h2, contact_p, subject)}

{footer(slug)}
</body>
</html>
'''
    (ROOT / slug).write_text(html, encoding="utf-8")
    return url

def steps(items):
    out = '<ol class="stappen">'
    for i, (h, p) in enumerate(items, 1):
        out += f'<li><span class="n">Stap {i}</span><h3>{h}</h3><p>{p}</p></li>'
    return out + "</ol>"

def marge(rows):
    out = "<dl>"
    for k, v in rows:
        if isinstance(v, list):
            v = "<ul>" + "".join(f"<li>{x}</li>" for x in v) + "</ul>"
        out += f"<dt>{k}</dt><dd>{v}</dd>"
    return out + f"<dt>Bijgewerkt</dt><dd>8 november 2026</dd></dl>"
