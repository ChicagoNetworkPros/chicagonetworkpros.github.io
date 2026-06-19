# Tasks: Tailwind Visual Overhaul

## Task 1: Set Up Tailwind CDN and Configuration

**Requirements**: 1.1, 1.2, 2.1, 2.2, 8.1

- [ ] 1.1 Add Tailwind CDN script tag (`<script src="https://cdn.tailwindcss.com"></script>`) in `<head>` after the JSON-LD schema script and before the existing `<style>` block
- [ ] 1.2 Add inline `tailwind.config` script with brand emerald color ramp (50-900) and Inter font family extension
- [ ] 1.3 Add `<style type="text/tailwindcss">` block with `@layer utilities` for card-glow pseudo-element, range input thumb styling, and smooth scroll

---

## Task 2: Convert Navigation to Tailwind Classes

**Requirements**: 9.1, 9.2, 9.3, 9.4, 1.3

- [ ] 2.1 Replace nav element's CSS with Tailwind utilities: `sticky top-0 z-50 backdrop-blur-md bg-white/80 border-b border-slate-100`
- [ ] 2.2 Convert `.nav-inner` to `max-w-7xl mx-auto px-5 py-3.5 flex items-center justify-between`
- [ ] 2.3 Convert `.brand` link to `font-extrabold tracking-tight text-slate-900 text-lg no-underline`
- [ ] 2.4 Convert `.nav-actions` container to `hidden md:flex items-center gap-3`
- [ ] 2.5 Convert `.nav-pill` link to `text-slate-600 font-semibold text-sm px-3 py-1.5 rounded-full hover:bg-slate-50 hover:text-slate-900 transition-colors no-underline`
- [ ] 2.6 Convert `.nav-cta` to `bg-slate-900 text-white px-4 py-2.5 rounded-full font-bold text-sm shadow-lg hover:-translate-y-0.5 hover:shadow-xl transition-all no-underline`

---

## Task 3: Implement Mobile Navigation Drawer

**Requirements**: 3.1, 3.2, 3.3, 3.4, 3.5, 3.6

- [ ] 3.1 Add hamburger button with `md:hidden` class inside nav, with SVG icon and `aria-label="Open menu"`
- [ ] 3.2 Add drawer overlay div (`fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-40 opacity-0 pointer-events-none transition-opacity duration-300`)
- [ ] 3.3 Add drawer panel div (`fixed top-0 right-0 h-full w-72 bg-white z-50 shadow-2xl translate-x-full transition-transform duration-300 ease-in-out p-6`)
- [ ] 3.4 Add close button with X SVG icon inside drawer panel with `aria-label="Close menu"`
- [ ] 3.5 Add navigation links inside drawer (Services link + Request Field Dispatch CTA)
- [ ] 3.6 Add drawer toggle JavaScript: open on hamburger click, close on overlay/close/link click using class toggling (`translate-x-full` ↔ `translate-x-0`, overlay opacity)

---

## Task 4: Convert Hero Section to Tailwind

**Requirements**: 2.5, 8.2, 8.3, 8.5

- [ ] 4.1 Convert `<header>` to use Tailwind background with arbitrary radial gradients: `relative overflow-hidden bg-white` with a pseudo-element or inline style for the emerald radial gradient
- [ ] 4.2 Convert `.hero-inner` to `max-w-7xl mx-auto px-5 py-20 lg:py-24`
- [ ] 4.3 Convert `.badge` to `inline-flex items-center gap-2 bg-brand-50 text-brand-700 border border-brand-200 px-3 py-1.5 rounded-full text-sm font-bold tracking-wide`
- [ ] 4.4 Convert `h1` to responsive heading: `text-4xl md:text-5xl lg:text-6xl font-black tracking-tighter leading-none mt-4 mb-3`
- [ ] 4.5 Convert `.subtitle` to `text-slate-600 text-lg max-w-3xl mb-7`
- [ ] 4.6 Convert `.hero-cta` to `inline-flex items-center gap-2 bg-slate-900 text-white px-5 py-3.5 rounded-full font-bold shadow-xl hover:-translate-y-0.5 hover:shadow-2xl transition-all no-underline`
- [ ] 4.7 Convert `.hero-contact` to `mt-5 font-bold text-slate-900` with link styled as `text-brand-600 font-extrabold no-underline hover:text-brand-700`

---

## Task 5: Convert Metrics Grid to Tailwind

**Requirements**: 7.2, 6.4, 2.1

- [ ] 5.1 Convert `.metrics-grid` to `grid grid-cols-1 md:grid-cols-3 gap-5 mt-10`
- [ ] 5.2 Convert `.metric-card` to `relative overflow-hidden bg-gradient-to-b from-white to-slate-50 p-7 rounded-xl text-center border border-slate-200 shadow-md card-glow` (card-glow is the custom @layer utility for the pointer-move effect)
- [ ] 5.3 Convert `.metric-num` to `text-4xl font-black text-brand-600 leading-none mb-2 tracking-tight`
- [ ] 5.4 Convert `.metric-label` to `text-slate-600 text-sm font-semibold`

---

## Task 6: Convert Services Section with Premium Card Styling

**Requirements**: 4.1, 4.2, 4.3, 4.4, 4.5, 8.2, 8.4

- [ ] 6.1 Convert section heading `h2` to `text-2xl font-extrabold tracking-tight mt-12 mb-6 flex items-center gap-3` with a `before:` pseudo-element for the emerald bar (or use a span with `w-1 h-3.5 rounded-full bg-brand-500 opacity-85`)
- [ ] 6.2 Convert `.section-lead` to `text-slate-600 -mt-4 mb-6 text-sm`
- [ ] 6.3 Convert `.featured-services` grid to `grid grid-cols-1 md:grid-cols-3 gap-5`
- [ ] 6.4 Convert each `.featured-card` to premium B2B styling: `bg-gradient-to-b from-white to-slate-50 p-6 rounded-xl border border-slate-200 border-l-4 border-l-brand-500 shadow-md hover:shadow-xl hover:-translate-y-0.5 transition-all duration-300`
- [ ] 6.5 Convert card `h3` to `text-lg font-extrabold text-slate-900 mt-0 mb-2`
- [ ] 6.6 Convert card `p` to `text-slate-600 text-sm leading-relaxed mb-0`

---

## Task 7: Convert Project Scoping Console to Tailwind

**Requirements**: 6.1, 6.2, 6.3, 7.3

- [ ] 7.1 Convert `.estimator-box` to `bg-white border border-slate-200 rounded-xl p-7 grid grid-cols-1 md:grid-cols-[1.1fr_0.9fr] gap-7 shadow-lg`
- [ ] 7.2 Convert `.control-group` to `mb-5` with label as `flex justify-between items-baseline font-bold mb-2 text-sm text-slate-900`
- [ ] 7.3 Convert `.range-val` to `text-brand-600 font-extrabold tabular-nums`
- [ ] 7.4 Convert `select` styling to `w-full bg-white border border-slate-300 text-slate-900 px-3 py-2.5 rounded-lg outline-none focus:border-brand-500 focus:ring-2 focus:ring-brand-500/20 transition-all`
- [ ] 7.5 Convert `.output-panel` to `bg-gradient-to-b from-slate-50 to-white border border-slate-200 rounded-xl p-6 flex flex-col justify-center`
- [ ] 7.6 Convert `.stat-label` to `text-xs uppercase text-slate-500 tracking-widest block font-bold`
- [ ] 7.7 Convert `.stat-value` to `text-xl font-extrabold text-slate-900 tracking-tight` and `.highlight` variant adds `text-brand-600`

---

## Task 8: Convert Industry Verticals Grid to Tailwind

**Requirements**: 7.4, 2.4

- [ ] 8.1 Convert `.verticals-grid` to `grid grid-cols-2 md:grid-cols-4 gap-4`
- [ ] 8.2 Convert `.vertical-pill` to `bg-slate-50 border border-slate-200 px-3 py-3.5 rounded-full text-center font-bold text-slate-900 text-sm hover:bg-brand-50 hover:border-brand-200 transition-colors`

---

## Task 9: Convert Delivery Methodology Grid to Tailwind

**Requirements**: 7.5, 4.3, 4.4

- [ ] 9.1 Convert `.services-grid` to `grid grid-cols-1 md:grid-cols-3 gap-5`
- [ ] 9.2 Convert `.service-card` to `bg-white p-6 rounded-xl border border-slate-200 shadow-md hover:shadow-xl hover:-translate-y-1 transition-all duration-300`
- [ ] 9.3 Convert card `h3` to `mt-0 text-lg text-slate-900 font-extrabold`
- [ ] 9.4 Convert card `p` to `text-slate-600 mb-0 text-sm leading-relaxed`

---

## Task 10: Convert Footer to Tailwind

**Requirements**: 8.3

- [ ] 10.1 Convert `footer` to `text-center py-10 px-4 text-slate-500 text-sm border-t border-slate-200 bg-white`
- [ ] 10.2 Style footer link with `text-slate-500 hover:text-slate-700 transition-colors`

---

## Task 11: Remove Old CSS and Final Cleanup

**Requirements**: 1.3, 1.4, 5.1, 5.2, 5.3, 5.4, 5.5

- [ ] 11.1 Remove the entire original `<style>...</style>` block from `<head>` (the one with `:root`, `body`, `.nav-inner`, `.brand`, `.hero-inner`, etc.)
- [ ] 11.2 Verify all `<meta>` tags remain unchanged in `<head>` (OG, Twitter, geo, robots, viewport, charset)
- [ ] 11.3 Verify `<script type="application/ld+json">` LocalBusiness schema is preserved with identical JSON content
- [ ] 11.4 Verify `<title>` and `<link rel="canonical">` tags are unchanged
- [ ] 11.5 Verify `calculateMetrics()` function and all DOM IDs it references remain intact
- [ ] 11.6 Verify pointer-move event listeners on `.metric-card` (now `.card-glow`) elements still function
- [ ] 11.7 Verify no horizontal overflow at 320px, 768px, and 1440px viewport widths
- [ ] 11.8 Remove any leftover inline `style` attributes that were only bridge values (except the existing one on `outTools` span if needed)

---

## Task 12: Add Smooth Scroll and Base Utilities

**Requirements**: 7.1, 8.1

- [ ] 12.1 Add `class="scroll-smooth"` to `<html>` element
- [ ] 12.2 Add base body classes: `font-sans text-slate-900 leading-relaxed antialiased`
- [ ] 12.3 Verify `box-border` is Tailwind's default (preflight) and no additional reset is needed
