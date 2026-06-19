#!/usr/bin/env python3
"""
Programmatic SEO Build Script for Chicago Network Pros
Generates localized landing pages from template + city data.
"""

import json
import os
import shutil
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, 'src')
TEMPLATE_PATH = os.path.join(SRC_DIR, 'template.html')
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
    """Render a page by replacing template placeholders with city data."""
    canonical = f"{SITE_URL}/{city['slug']}/"
    
    rendered = template
    rendered = rendered.replace('{{CITY_NAME}}', city['name'])
    rendered = rendered.replace('{{CITY_STATE}}', 'IL')
    rendered = rendered.replace('{{PAGE_TITLE}}', f"Chicago Network Pros | Enterprise IT & Network Infrastructure Services in {city['name']} IL")
    rendered = rendered.replace('{{META_DESC}}', city['meta_desc'])
    rendered = rendered.replace('{{CANONICAL_URL}}', canonical)
    rendered = rendered.replace('{{AREA_SERVED_CITY}}', city['name'])
    rendered = rendered.replace('{{HERO_HEADING}}', city['hero_heading'])
    rendered = rendered.replace('{{HERO_SUBTITLE}}', city['hero_subtitle'])
    rendered = rendered.replace('{{INDUSTRY_FOCUS_TEXT}}', city['industry_focus'])
    rendered = rendered.replace('{{PHONE_DISPLAY}}', PHONE_DISPLAY)
    rendered = rendered.replace('{{PHONE_LINK}}', PHONE_LINK)
    rendered = rendered.replace('{{COPYRIGHT_YEAR}}', COPYRIGHT_YEAR)
    
    return rendered


def render_root_page(template):
    """Render the root Chicago page."""
    rendered = template
    rendered = rendered.replace('{{CITY_NAME}}', 'Chicago')
    rendered = rendered.replace('{{CITY_STATE}}', 'IL')
    rendered = rendered.replace('{{PAGE_TITLE}}', 'Chicago Network Pros | Enterprise IT & Network Infrastructure Services in Chicago IL')
    rendered = rendered.replace('{{META_DESC}}', 'Chicago Network Pros delivers enterprise IT and network infrastructure services in Chicago IL: data center build-out, structured cabling, wireless, networking, audio visual, electrical, edge/IoT/POS, IT staffing, and 24/7 smart hands dispatch.')
    rendered = rendered.replace('{{CANONICAL_URL}}', f'{SITE_URL}/')
    rendered = rendered.replace('{{AREA_SERVED_CITY}}', 'Chicago')
    rendered = rendered.replace('{{HERO_HEADING}}', 'Enterprise IT Infrastructure Services in Chicago IL')
    rendered = rendered.replace('{{HERO_SUBTITLE}}', 'Chicago Network Pros engineers high-performance, scalable IT infrastructure for Chicago-area data centers, corporate offices, warehouses, and retail locations. From cabling and wireless to networking, audio visual, electrical, and edge/IoT deployments, we deliver onsite field execution for enterprise digital transformation.')
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
    
    # Generate root index.html
    root_html = render_root_page(template)
    root_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(root_path, 'w', encoding='utf-8') as f:
        f.write(root_html)
    print(f"✅ Root: /index.html")
    
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
