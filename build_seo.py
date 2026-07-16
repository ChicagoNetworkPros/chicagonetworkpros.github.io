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
    
    # Generate sitemap
    sitemap = generate_sitemap(cities)
    sitemap_path = os.path.join(OUTPUT_DIR, 'sitemap.xml')
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"\n🗺️  sitemap.xml generated with {len(cities) + 1} URLs")
    
    print(f"\n🎉 Build complete! {len(cities) + 1} pages generated.")


if __name__ == '__main__':
    main()
