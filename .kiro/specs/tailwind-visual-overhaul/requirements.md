# Requirements: Tailwind Visual Overhaul

## Overview

Replace the existing embedded custom CSS in `index.html` with Tailwind CSS loaded via CDN, introducing an emerald/slate color scheme, modern spacing, a mobile navigation drawer, and premium B2B sub-card styling for the services section — while preserving all meta tags, schema scripts, and JavaScript functionality.

---

## Requirement 1: Tailwind CSS CDN Integration

### User Story
As a site maintainer, I want the site styled entirely with Tailwind CSS utility classes loaded via CDN so that the custom CSS is eliminated and future styling changes are faster and more consistent.

### Acceptance Criteria
- 1.1 The Tailwind CSS Play CDN script (`https://cdn.tailwindcss.com`) is included in `<head>` before any body content renders.
- 1.2 A `tailwind.config` object is defined inline extending the theme with brand emerald colors (50–900 ramp based on #10b981/#059669 palette) and Inter font family.
- 1.3 The original `<style>` block with raw CSS declarations is completely removed from the document.
- 1.4 Only a `<style type="text/tailwindcss">` block may remain for edge-case directives (e.g., range input thumb, card glow `@layer` utility) that cannot be expressed as inline utilities.

---

## Requirement 2: Emerald/Slate Color Scheme

### User Story
As a visitor, I want to see a polished emerald and slate color palette throughout the site so that the brand feels premium and cohesive.

### Acceptance Criteria
- 2.1 Primary accent color is emerald-600 (`#059669`) used for CTA text, badge, metric numbers, and card accents.
- 2.2 Dark text uses slate-900 (`#0f172a`) for headings and slate-600 (`#475569`) for body/subtitle text.
- 2.3 Card backgrounds use a gradient from white to slate-50 (`#f8fafc`).
- 2.4 Borders use slate-200 (`#e2e8f0`) for subtle separation.
- 2.5 The hero section has a radial gradient with emerald tint matching or enhancing the original design.

---

## Requirement 3: Mobile Navigation Drawer

### User Story
As a mobile user, I want a smooth slide-in navigation drawer so that I can access site navigation without it taking up screen space when closed.

### Acceptance Criteria
- 3.1 A hamburger menu button is visible only on screens below the `md` breakpoint (< 768px).
- 3.2 Tapping the hamburger slides a panel in from the right with smooth CSS transition (`transition-transform duration-300`).
- 3.3 The drawer displays navigation links (Services) and the primary CTA (Request Field Dispatch).
- 3.4 The drawer closes when: the close button is clicked, the backdrop overlay is clicked, or a navigation link is clicked.
- 3.5 A semi-transparent backdrop overlay appears behind the drawer when open.
- 3.6 Desktop navigation links remain visible as-is on `md:` and above breakpoints (drawer is not rendered on desktop).

---

## Requirement 4: Premium B2B Service Card Styling

### User Story
As a prospective B2B client, I want the services section to look premium and modern so that I perceive the company as enterprise-grade.

### Acceptance Criteria
- 4.1 Each of the 12 featured service cards has a left emerald accent border (`border-l-4` in brand-500).
- 4.2 Cards use a subtle gradient background (white to slate-50) with rounded corners (`rounded-xl`).
- 4.3 Cards have a shadow that elevates on hover (`shadow-md` → `shadow-xl` on hover).
- 4.4 Cards shift upward slightly on hover (`hover:-translate-y-0.5`) with smooth transition.
- 4.5 The services grid displays 3 columns on desktop (`md:grid-cols-3`) and 1 column on mobile.

---

## Requirement 5: Preserve Meta Tags and Schema Scripts

### User Story
As a site owner focused on SEO, I want all existing meta tags, Open Graph data, Twitter Cards, geo meta, and JSON-LD schema markup preserved exactly so that search engine indexing and social sharing are unaffected.

### Acceptance Criteria
- 5.1 All `<meta>` tags in `<head>` are preserved with identical attribute values (no additions, removals, or modifications).
- 5.2 The `<script type="application/ld+json">` LocalBusiness schema is preserved with identical JSON content.
- 5.3 The `<title>` tag content is unchanged.
- 5.4 The `<link rel="canonical">` tag is preserved with the same href value.
- 5.5 The Google Site Verification meta tag is preserved unchanged.

---

## Requirement 6: Preserve JavaScript Functionality

### User Story
As a user interacting with the Project Scoping Console, I want the calculator to work exactly as before so that I can estimate project parameters without any regression.

### Acceptance Criteria
- 6.1 The `calculateMetrics()` function remains fully intact and produces identical output for identical inputs.
- 6.2 All DOM element IDs referenced by JavaScript (`projectScale`, `rackCount`, `cableZen`, `rackVal`, `cableVal`, `outHours`, `outCrew`, `outTools`) are preserved unchanged.
- 6.3 Event listeners for `input` events on the select and range elements continue to fire and trigger recalculation.
- 6.4 The pointer-move radial glow effect on metric cards continues to function (CSS custom properties `--mx`, `--my` still used by the card-glow utility).
- 6.5 The initial `calculateMetrics()` call on page load still executes and populates output fields.

---

## Requirement 7: Responsive Layout

### User Story
As a user on any device, I want the site to look great and function properly from 320px mobile to 1920px+ desktop widths.

### Acceptance Criteria
- 7.1 No horizontal scrollbar appears at any viewport width between 320px and 1920px.
- 7.2 The metrics grid shows 1 column on mobile, 3 columns on `md:` and above.
- 7.3 The estimator box shows stacked layout on mobile, 2-column layout on `md:` and above.
- 7.4 The industry verticals grid shows 2 columns on mobile, 4 columns on `md:` and above.
- 7.5 The delivery methodology grid shows 1 column on mobile, 3 columns on `md:` and above.
- 7.6 Text sizes scale appropriately using Tailwind responsive prefixes or clamp values.

---

## Requirement 8: Crisp Spacing and Typography

### User Story
As a visitor, I want consistent, generous spacing and clean typography so that content is easy to scan and the site feels professionally crafted.

### Acceptance Criteria
- 8.1 Inter font family is set as the primary sans-serif font via Tailwind config.
- 8.2 Section headings use `font-extrabold` with tight letter-spacing (`tracking-tight`).
- 8.3 Consistent vertical rhythm is maintained between sections using Tailwind spacing utilities (e.g., `py-16`, `mt-12`, `mb-6`).
- 8.4 Card internal padding is uniform (`p-6`) across all card types.
- 8.5 The main content container is constrained to `max-w-7xl` (1280px) with horizontal auto-margin.

---

## Requirement 9: Navigation Glassmorphism Effect

### User Story
As a visitor scrolling the page, I want the sticky navigation to have a frosted-glass effect so that it feels modern while still showing content scrolling underneath.

### Acceptance Criteria
- 9.1 The nav bar uses `backdrop-blur-md` and semi-transparent white background (`bg-white/80`).
- 9.2 The nav remains fixed at the top (`sticky top-0`) with a high z-index (`z-50`).
- 9.3 A subtle bottom border separates the nav from content below (`border-b border-slate-100`).
- 9.4 The nav CTA button has a dark background (`bg-slate-900`) with hover state and shadow.
