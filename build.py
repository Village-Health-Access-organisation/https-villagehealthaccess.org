#!/usr/bin/env python3
"""Builds the Village Health Access site.

Outputs:
  site/      multi-page static site (upload this folder to any static host)
  preview/   single-file preview with hash navigation (for sharing a link)

Edit page content in pages.py and styles in src/styles.css, then run:  python3 build.py
Anything wrapped in <span class="ph">...</span> is a placeholder that still needs a real fact.
"""
import pathlib, re, shutil
from pages import PAGES, NAV, LOGO

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT / "src" / "styles.css").read_text()
JS = (ROOT / "src" / "site.js").read_text()
FONT_CSS = (ROOT / "src" / "fonts.css").read_text()
SELF_FONTS = ('<link rel="preload" href="/fonts/plus-jakarta-sans-latin.woff2" as="font" type="font/woff2" crossorigin>'
              '<link rel="preload" href="/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>')
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500..800&family=Inter:wght@400..700&display=swap">')
DESC = "Free telemedicine and essential medicine delivery for underserved communities across West Africa. A humanitarian initiative launching in Togo at the end of 2027."


def header(active):
    links = "".join(
        f'<li><a href="{f}"{" aria-current=\"page\"" if f == active else ""}>{label}</a></li>'
        for f, label in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><nav class="wrap nav" aria-label="Main">
  <a class="brand" href="index.html" aria-label="Village Health Access home">{LOGO}<span>Village Health Access<small>Healthcare for every village</small></span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
  <ul class="nav-links" id="nav-links">{links}</ul>
  <a class="btn btn-gold" href="donate.html">Donate</a>
</nav></header>'''


FOOTER = f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div>
      <a class="brand foot-brand" href="index.html">{LOGO}<span>Village Health Access<small>Healthcare for every village</small></span></a>
      <p style="margin-top:1rem">A humanitarian initiative, in partnership with Verakou, providing free telemedicine and essential medicine delivery across West Africa.</p>
    </div>
    <div><h2 class="foot-h">Organization</h2><ul><li><a href="about.html">About</a></li><li><a href="programs.html">Programs</a></li><li><a href="impact.html">Impact</a></li></ul></div>
    <div><h2 class="foot-h">Get involved</h2><ul><li><a href="partners.html">Partner with us</a></li><li><a href="donate.html">Donate</a></li><li><a href="contact.html">Volunteer</a></li></ul></div>
    <div><h2 class="foot-h">More</h2><ul><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
    <div>
      <h2 class="foot-h">Monthly field updates</h2>
      <p style="margin-bottom:.8rem">Program milestones and stories from the field, once a month.</p>
      <form class="news-form" data-mailto="contact@villagehealthaccess.org" data-subject="Newsletter sign-up">
        <label for="news-email" class="sr-only">Email address</label>
        <input id="news-email" name="email" type="email" placeholder="you@example.org" required>
        <button class="btn btn-gold" type="submit">Subscribe</button>
      </form>
      <p class="form-status small" aria-live="polite"></p>
    </div>
  </div>
  <div class="foot-base">
    <span>© 2026 Village Health Access · In partnership with Verakou · Powered by <a href="https://klinova.co">Klinova</a>, built on Kinara</span>
    <span>501(c)(3) status pending. All donations support direct program delivery.</span>
  </div>
</div></footer>'''


SITE_URL = "https://villagehealthaccess.org"
PAGE_DESC = {
    "home": DESC,
    "about": "Village Health Access was founded after seeing patients in Togo turned away from clinics. Our story, mission, values and leadership.",
    "programs": "Telemedicine, essential medicines, government integration, and cholera and vaccine programs for underserved communities in West Africa.",
    "impact": "Our 2030 goals, country roadmap and how we report progress. Updated monthly, with anonymized data.",
    "partners": "Clinics, pharmacies, NGOs and health agencies: join the Village Health Access network across West Africa.",
    "donate": "Fund telemedicine consultations, medicines and community health workers in West Africa. $25 pays for one consultation.",
    "news": "Regional health news, disease alerts, policy and technology updates from Village Health Access.",
    "contact": "Contact Village Health Access about partnerships, donations, volunteering or media.",
    "privacy": "How Village Health Access protects patient data.",
    "404": "Page not found.",
}
JSONLD = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"NGO","name":"Village Health Access",'
          '"url":"https://villagehealthaccess.org","logo":"https://villagehealthaccess.org/icon-512.png",'
          '"description":"Free telemedicine and essential medicine delivery for underserved communities across West Africa.",'
          '"email":"contact@villagehealthaccess.org","areaServed":["Togo","Ghana","Benin","Nigeria","Burkina Faso","Côte d\'Ivoire","Senegal"],'
          '"foundingLocation":"Togo","sameAs":["https://x.com/villagehealthacc","https://linkedin.com/company/village-health-access"]}</script>')

NOT_FOUND = '''<section class="band page-hero"><div class="wrap">
  <p class="eyebrow">Error 404</p><h1>We couldn't find that page.</h1>
  <p class="lead">It may have moved when we updated our website.</p>
  <div class="actions"><a class="btn btn-gold" href="index.html">Go to the home page</a><a class="btn btn-ghost" href="contact.html">Contact us</a></div>
</div></section>'''


def clean_links(html):
    html = re.sub(r'href="index\.html(#[\w-]+)?"', lambda m: f'href="/{m.group(1) or ""}"', html)
    return re.sub(r'href="([a-z]+)\.html(#[\w-]+)?"', lambda m: f'href="/{m.group(1)}{m.group(2) or ""}"', html)


def page_html(key, fname, title, body):
    full_title = "Village Health Access | Healthcare for every village" if key == "home" else f"{title} | Village Health Access"
    path = "/" if key == "home" else f"/{fname[:-5]}"
    desc = PAGE_DESC[key]
    noindex = '<meta name="robots" content="noindex">' if key == "404" else ""
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{noindex}<link rel="canonical" href="{SITE_URL}{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Village Health Access">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}{path}">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Village Health Access: healthcare for every village">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@villagehealthacc">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
{SELF_FONTS}
<style>{FONT_CSS}{CSS}</style>
{JSONLD if key == "home" else ""}
</head>
<body>
{header(fname)}
<main id="main">{body}</main>
{FOOTER}
<script src="/site.js" defer></script>
</body>
</html>
'''
    return clean_links(html)


def build_site():
    out = ROOT / "site"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir()
    (out / "site.js").write_text(JS)
    shutil.copytree(ROOT / "src" / "static", out, dirs_exist_ok=True)
    (out / "favicon.svg").write_text(LOGO.replace('aria-hidden="true" ', ""))
    pages = dict(PAGES)
    pages["404"] = ("404.html", "Page not found", NOT_FOUND)
    for key, (fname, title, body) in pages.items():
        (out / fname).write_text(page_html(key, fname, title, body))
    urls = "".join(f"<url><loc>{SITE_URL}{'/' if k == 'home' else '/' + f[:-5]}</loc></url>" for k, (f, _, _) in PAGES.items())
    (out / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")


def build_preview():
    out = ROOT / "preview"
    out.mkdir(exist_ok=True)
    name_for = {fname: key for key, (fname, _, _) in PAGES.items()}

    def rewrite(html):
        def sub(m):
            return f'href="#{name_for.get(m.group(1) + ".html", "home")}"'
        return re.sub(r'href="([a-z]+)\.html(?:#[\w-]+)?"', sub, html)

    sections = "".join(
        f'<div class="view" data-view="{key}"{"" if key == "home" else " hidden"}>{rewrite(header(fname))}<main id="main-{key}">{rewrite(body)}</main></div>'
        for key, (fname, _, body) in PAGES.items())
    router = '''<script>
(function(){
  function show(){
    var k=(location.hash||"#home").slice(1); var views=document.querySelectorAll(".view");
    var found=false; views.forEach(function(v){ if(v.dataset.view===k) found=true; });
    if(!found) k="home";
    views.forEach(function(v){ v.hidden = v.dataset.view!==k; });
    window.scrollTo(0,0);
  }
  window.addEventListener("hashchange", show); show();
})();
</script>'''
    html = f'''<title>Village Health Access</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
<style>{CSS}</style>
{sections}
{rewrite(FOOTER)}
<script>{JS}</script>
{router}
'''
    (out / "index.html").write_text(html)


if __name__ == "__main__":
    build_site()
    build_preview()
    print("Built site/ and preview/index.html")
