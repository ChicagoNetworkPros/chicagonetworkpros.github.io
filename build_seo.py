#!/usr/bin/env python3
"""
Programmatic SEO Build Script for Chicago Network Pros
Generates localized landing pages from template + city data.
"""

import json
import os
import re
import shutil
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
# City pages inherit the production homepage design so that the visual system
# stays consistent as the site evolves.
TEMPLATE_PATH = os.path.join(BASE_DIR, 'index.html')
DATA_PATH = os.path.join(SRC_DIR, 'data_cities.json')
OUTPUT_DIR = BASE_DIR  # Output to repo root for GitHub Pages

# Constants
SITE_URL = 'https://chicagonetworkpros.github.io'
PHONE_DISPLAY = '773-697-1292'
PHONE_LINK = '7736971292'
COPYRIGHT_YEAR = str(datetime.now().year)

SERVICE_PAGES = [
    {
        "slug": "network-cabling",
        "title": "Network Cabling in Chicago IL",
        "meta_desc": "Chicago Network Pros provides network cabling, structured cabling, fiber, and Cat6 installation for Chicago businesses and properties.",
        "hero": "Network cabling built for real work.",
        "summary": "From office buildouts to warehouse retrofits, we install clean, scalable cabling systems that keep business networks stable and easy to maintain.",
        "highlights": [
            "Structured cabling and Cat6 layouts",
            "Fiber optic and low-voltage wiring",
            "Labeling, testing, and documentation",
            "Closet cleanup and patching support",
        ],
    },
    {
        "slug": "website-design",
        "title": "Website Design in Chicago IL",
        "meta_desc": "Website design for Chicago businesses, residents, and local brands. Modern landing pages, service pages, and SEO-friendly layouts.",
        "hero": "Websites that look sharp and work hard.",
        "summary": "We design modern, mobile-friendly websites for businesses and local projects that need a clearer online presence and a better first impression.",
        "highlights": [
            "Homepage and service page design",
            "SEO-friendly structure and copy layout",
            "Lead capture and contact flows",
            "Clean, fast, responsive pages",
        ],
    },
    {
        "slug": "ai-automation",
        "title": "AI Automation in Chicago IL",
        "meta_desc": "AI automation services for Chicago companies and residents. Improve intake, follow-up, workflows, and repetitive tasks with practical automation.",
        "hero": "AI automation that saves time.",
        "summary": "We build practical automations that reduce repetitive work, improve follow-up, and keep your team moving without adding extra complexity.",
        "highlights": [
            "Intake and follow-up workflows",
            "Automated notifications and routing",
            "Repetitive task elimination",
            "Operations support for small teams",
        ],
    },
    {
        "slug": "content-creation",
        "title": "Content Creation in Chicago IL",
        "meta_desc": "Content creation for Chicago businesses. Website copy, service pages, blog posts, and brand messaging written to sound natural and clear.",
        "hero": "Content that sounds human.",
        "summary": "We write practical, useful content for websites, service pages, blog posts, and local marketing so your message feels clear and trustworthy.",
        "highlights": [
            "Website copy and page refreshes",
            "Service descriptions and local pages",
            "Blog and article support",
            "Brand messaging that sounds like you",
        ],
    },
    {
        "slug": "security-cameras",
        "title": "Security Camera Installation in Chicago IL",
        "meta_desc": "Chicago security camera installation for offices, warehouses, retail spaces, and residential properties that need better visibility and coverage.",
        "hero": "Camera systems with cleaner coverage.",
        "summary": "We help place and deploy camera systems for properties that need better visibility, easier monitoring, and a more practical security setup.",
        "highlights": [
            "Camera placement and cabling",
            "Commercial property coverage",
            "Residential security setups",
            "System coordination and testing",
        ],
    },
    {
        "slug": "voip-phone-systems",
        "title": "VoIP and Phone Systems in Chicago IL",
        "meta_desc": "VoIP and phone system setup in Chicago for offices, branches, and service teams that need dependable communications.",
        "hero": "Voice systems that stay connected.",
        "summary": "We help businesses set up modern voice systems that are easier to manage, easier to scale, and better suited to how teams work now.",
        "highlights": [
            "Office phone system setup",
            "VoIP deployment and staging",
            "Branch communication support",
            "Device and network coordination",
        ],
    },
]


def load_template():
    """Load the HTML template."""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def load_cities():
    """Load city data from JSON."""
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def render_page(template, city):
    """Render a localized city page from the production homepage design."""
    canonical = f"{SITE_URL}/{city['slug']}/"

    rendered = template
    title = f"Chicago Network Pros | Enterprise IT Infrastructure Services in {city['name']} IL"
    keywords = (
        f"{city['name']} IT services, enterprise IT {city['name']} IL, "
        f"structured cabling {city['name']}, fiber optic installation {city['name']}, "
        f"low voltage cabling {city['name']}, Wi-Fi installation {city['name']}, "
        f"network switch installation {city['name']}, smart hands {city['name']}, "
        f"IT field services {city['name']}, website design {city['name']}, "
        f"AI automation {city['name']}, content creation {city['name']}, "
        f"business support {city['name']}, residential tech support {city['name']}, "
        f"Chicago Network Pros"
    )
    rendered = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', rendered, count=1)
    rendered = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{city["meta_desc"]}">', rendered, count=1)
    rendered = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{keywords}">', rendered, count=1)
    rendered = rendered.replace('<link rel="canonical" href="https://chicagonetworkpros.github.io/">', f'<link rel="canonical" href="{canonical}">')
    rendered = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', rendered, count=1)
    rendered = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{city["meta_desc"]}">', rendered, count=1)
    rendered = rendered.replace('<meta property="og:url" content="https://chicagonetworkpros.github.io/">', f'<meta property="og:url" content="{canonical}">')
    rendered = rendered.replace('"url":"https://chicagonetworkpros.github.io/"', f'"url":"{canonical}"')
    rendered = rendered.replace('"addressLocality":"Chicago"', f'"addressLocality":"{city["name"]}"')
    rendered = rendered.replace('"name":"Chicago"},"hasOfferCatalog"', f'"name":"{city["name"]}"}},"hasOfferCatalog"')
    rendered = rendered.replace('"telephone":"+1-773-697-1292"', '"telephone":"773-697-1292"')
    rendered = rendered.replace('"serviceArea":{"@type":"GeoCircle","geoMidpoint":{"@type":"GeoCoordinates","latitude":41.8781,"longitude":-87.6298},"radius":"80467"}', '"serviceArea":{"@type":"GeoCircle","geoMidpoint":{"@type":"GeoCoordinates","latitude":41.8781,"longitude":-87.6298},"radius":"80467"}')
    rendered = rendered.replace('"image":"https://chicagonetworkpros.github.io/logo.svg"', '"image":"https://chicagonetworkpros.github.io/logo.svg"')
    rendered = rendered.replace('Chicago’s onsite infrastructure partner', f'{city["name"]} onsite infrastructure partner')
    rendered = rendered.replace('Infrastructure, websites, and automation that <em>keep business moving.</em>', city['hero_heading'])
    rendered = rendered.replace('From a single network closet to a new website launch, we put skilled technicians and builders on the ground to support Chicago businesses and residents with IT, AI automation, and content work that actually ships.', city['hero_subtitle'])
    rendered = rendered.replace('across the Chicago metro.', f'across {city["name"]} and the Chicago metro.')
    rendered = rendered.replace('Chicago metro coverage, ready to deploy.', f'{city["name"]} coverage, ready to deploy.')
    rendered = rendered.replace('throughout Chicagoland.', f'throughout {city["name"]} and Chicagoland.')
    rendered = rendered.replace('CHICAGO, IL · ENTERPRISE FIELD SERVICES', f'{city["name"].upper()}, IL · ENTERPRISE FIELD SERVICES')
    rendered = rendered.replace('The team behind your network, website, and content.', 'The field team behind your network, website, and content.')
    rendered = rendered.replace('Built for businesses, residents, and property teams that want reliable support across infrastructure, digital presence, and everyday tech needs.', 'Built for businesses, residents, and property teams that want reliable support across infrastructure, digital presence, and everyday tech needs.')
    return rendered


def render_root_page(template):
    """Render the root Chicago page."""
    rendered = template
    rendered = rendered.replace('{{CITY_NAME}}', 'Chicago')
    rendered = rendered.replace('{{CITY_STATE}}', 'IL')
    rendered = rendered.replace('{{PAGE_TITLE}}', 'Chicago Network Pros | Enterprise IT & Network Infrastructure Services in Chicago IL')
    rendered = rendered.replace('{{META_DESC}}', 'Chicago Network Pros delivers enterprise IT, website design, AI automation, content creation, and hands-on support in Chicago IL for businesses and residents.')
    rendered = rendered.replace('{{CANONICAL_URL}}', f'{SITE_URL}/')
    rendered = rendered.replace('{{AREA_SERVED_CITY}}', 'Chicago')
    rendered = rendered.replace('{{HERO_HEADING}}', 'Enterprise IT Infrastructure Services in Chicago IL')
    rendered = rendered.replace('{{HERO_SUBTITLE}}', 'Chicago Network Pros engineers high-performance, scalable IT infrastructure and digital support for Chicago-area data centers, corporate offices, warehouses, residential clients, and retail locations. From cabling and wireless to websites, AI automation, content, and edge/IoT deployments, we deliver onsite field execution for practical growth.')
    rendered = rendered.replace('{{INDUSTRY_FOCUS_TEXT}}', 'Enterprise IT & Infrastructure')
    rendered = rendered.replace('{{PHONE_DISPLAY}}', PHONE_DISPLAY)
    rendered = rendered.replace('{{PHONE_LINK}}', PHONE_LINK)
    rendered = rendered.replace('{{COPYRIGHT_YEAR}}', COPYRIGHT_YEAR)
    
    return rendered


def render_service_page(service):
    """Render a dedicated service page."""
    canonical = f"{SITE_URL}/services/{service['slug']}/"
    title = f"Chicago Network Pros | {service['title']}"
    highlights = "".join(
        f"<li>{item}</li>" for item in service["highlights"]
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{service['meta_desc']}">
  <meta name="keywords" content="{service['title']}, Chicago Network Pros, Chicago IL, local services, business support">
  <meta name="author" content="Chicago Network Pros">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{service['meta_desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{{--ink:#171717;--muted:#a1a1a1;--line:#2a2a2a;--green:#3ecf8e;--panel:#1d1d1d}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--ink);color:#f6f6f6;font-family:Inter,Arial,sans-serif}}a{{color:inherit;text-decoration:none}}.wrap{{width:min(1120px,calc(100% - 40px));margin:auto}}.eyebrow{{font:500 11px 'DM Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--green)}}header{{padding:22px 0;border-bottom:1px solid var(--line);position:sticky;top:0;background:#171717cc;backdrop-filter:blur(12px);z-index:2}}.nav{{display:flex;justify-content:space-between;align-items:center}}.brand{{display:flex;gap:10px;align-items:center;font-weight:800}}.mark{{width:20px;height:20px;border-radius:5px;background:var(--green);display:grid;place-items:center;color:#072719;font:700 10px 'DM Mono',monospace}}.phone{{font:500 12px 'DM Mono',monospace;color:#ddd}}.hero{{padding:92px 0 70px;border-bottom:1px solid var(--line)}}h1{{font-size:clamp(42px,6vw,74px);line-height:.98;letter-spacing:-.07em;max-width:760px;margin:16px 0 18px}}.lede{{font-size:17px;line-height:1.65;color:#b9b9b9;max-width:700px;margin:0 0 30px}}.buttons{{display:flex;gap:12px;flex-wrap:wrap}}.button{{display:inline-flex;align-items:center;gap:10px;padding:13px 18px;border-radius:7px;font-size:14px;font-weight:700}}.primary{{background:var(--green);color:#092518}}.secondary{{border:1px solid #424242;color:#eee}}.panel{{border:1px solid #356d53;background:#16342480;border-radius:12px;padding:24px;max-width:420px;margin-top:18px}}.panel strong{{display:block;font-size:18px;margin-bottom:10px}}.section{{padding:84px 0}}h2{{font-size:clamp(30px,4vw,48px);letter-spacing:-.06em;line-height:1.05;margin:12px 0 0}}.note{{max-width:420px;color:#a9a9a9;line-height:1.6}}.list{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:28px}}.list div{{background:#1f1f1f;border:1px solid var(--line);border-radius:10px;padding:16px;font-size:14px;line-height:1.5}}footer{{border-top:1px solid var(--line);padding:28px 0;color:#868686;font-size:12px}}@media(max-width:700px){{.list{{grid-template-columns:1fr}}.phone{{display:none}}}}
  </style>
</head>
<body>
  <header>
    <div class="wrap nav">
      <a class="brand" href="{SITE_URL}/"><span class="mark">CNP</span>Chicago Network Pros</a>
      <a class="phone" href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a>
    </div>
  </header>
  <main>
    <section class="hero wrap">
      <div class="eyebrow">Service page</div>
      <h1>{service['hero']}</h1>
      <p class="lede">{service['summary']}</p>
      <div class="buttons">
        <a class="button primary" href="tel:{PHONE_LINK}">Talk to a specialist</a>
        <a class="button secondary" href="mailto:dispatch@chicagonetworkpros.com">Request a work order</a>
      </div>
      <div class="panel">
        <strong>Built for Chicago-area projects</strong>
        <div>{service['title']} for businesses, property teams, and residents who want practical support and clean execution.</div>
      </div>
    </section>
    <section class="section wrap">
      <div class="eyebrow">What this includes</div>
      <h2>Clear scope, strong follow-through.</h2>
      <p class="note">We keep the work focused on the actual outcome you need, whether that is a cleaner network, a better website, a simpler workflow, or a more reliable setup.</p>
      <div class="list">{highlights}</div>
    </section>
  </main>
  <footer>
    <div class="wrap">© {COPYRIGHT_YEAR} Chicago Network Pros</div>
  </footer>
</body>
</html>"""


def generate_sitemap(cities):
    """Generate sitemap.xml with all pages."""
    today = datetime.now().strftime('%Y-%m-%d')
    
    urls = []
    # Root page
    urls.append(f'''  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>''')
    
    # City pages
    for city in cities:
        urls.append(f'''  <url>
    <loc>{SITE_URL}/{city['slug']}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>''')

    # Service pages
    for service in SERVICE_PAGES:
        urls.append(f'''  <url>
    <loc>{SITE_URL}/services/{service['slug']}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>''')
    
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemapindex.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>'''
    
    return sitemap


def main():
    """Main build function."""
    print("🔨 Chicago Network Pros — Programmatic SEO Build")
    print("=" * 50)
    
    # Load resources
    template = load_template()
    cities = load_cities()
    
    print(f"📄 Template loaded ({len(template)} chars)")
    print(f"🏙️  {len(cities)} cities loaded")
    print()
    
    # Generate city pages
    for city in cities:
        city_dir = os.path.join(OUTPUT_DIR, city['slug'])
        os.makedirs(city_dir, exist_ok=True)
        
        page_html = render_page(template, city)
        page_path = os.path.join(city_dir, 'index.html')
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(page_html)
        
        print(f"✅ /{city['slug']}/index.html — {city['name']} ({city['profile']})")

    # Generate service pages
    services_dir = os.path.join(OUTPUT_DIR, 'services')
    os.makedirs(services_dir, exist_ok=True)
    for service in SERVICE_PAGES:
        service_dir = os.path.join(services_dir, service['slug'])
        os.makedirs(service_dir, exist_ok=True)
        page_path = os.path.join(service_dir, 'index.html')
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(render_service_page(service))
        print(f"✅ /services/{service['slug']}/index.html — {service['title']}")
    
    # Generate sitemap
    sitemap = generate_sitemap(cities)
    sitemap_path = os.path.join(OUTPUT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"\n🗺️  sitemap.xml generated with {len(cities) + len(SERVICE_PAGES) + 1} URLs")
    
    print(f"\n🎉 Build complete! {len(cities) + len(SERVICE_PAGES) + 1} pages generated.")


if __name__ == '__main__':
    main()
