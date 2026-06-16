#!/usr/bin/env python3
# polish_v22.py — post-critique polish pass
filepath = '/Users/alexchan.ksa/Downloads/ksa-website-prototype/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
original_len = len(html)
changes = []

def replace(old, new, desc, count=1):
    global html
    if old not in html:
        print(f"  MISSING: {desc}")
        return False
    html = html.replace(old, new, count)
    changes.append(desc)
    print(f"  ✓ {desc}")
    return True

print("── Font import ──")
replace(
    'family=DM+Sans:wght@300;400;500;600&family=Syne:wght@400;600;700;800',
    'family=DM+Sans:wght@400;500;600&family=Syne:wght@700;800',
    "Trim unused font weights: DM Sans 300, Syne 400/600"
)

print("\n── BANNED: border-left accent stripes ──")

# 1. med-highlight-item — redesign: full border + tinted background, no left stripe
replace(
    '.med-highlight-item { background:#f4f7fb; border-left:4px solid var(--kblue); border-radius:0 10px 10px 0; padding:18px 20px; }',
    '.med-highlight-item { background:var(--kblue-50); border:1.5px solid var(--kblue-light); border-radius:10px; padding:18px 20px; }',
    "med-highlight-item: remove banned border-left, replace with full border + tint"
)

# 2. semi-cross-sell — redesign: warm yellow-tinted background, no left stripe
replace(
    '.semi-cross-sell { background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); border-left:4px solid var(--kyellow); border-radius:0 10px 10px 0; padding:24px 28px; }',
    '.semi-cross-sell { background:rgba(245,208,0,0.07); border:1px solid rgba(245,208,0,0.22); border-radius:12px; padding:28px 32px; }',
    "semi-cross-sell: remove banned border-left, replace with warm-tint + full border"
)

print("\n── Contrast: white-on-dark surfaces ──")

# Breadcrumb: 0.40 → 0.65
replace(
    '.breadcrumb { font-size:12px; color:rgba(255,255,255,0.4); margin-bottom:14px; cursor:pointer; font-weight:600; font-family:\'DM Sans\',sans-serif; letter-spacing:0.03em; transition:color 0.15s; }',
    '.breadcrumb { font-size:12px; color:rgba(255,255,255,0.65); margin-bottom:14px; cursor:pointer; font-weight:600; font-family:\'DM Sans\',sans-serif; letter-spacing:0.03em; transition:color 0.15s; }',
    "Breadcrumb: raise opacity 0.40 → 0.65"
)

# Footer description: 0.45 → 0.68
replace(
    '.footer-desc { color:rgba(255,255,255,0.45); font-size:13.5px; line-height:1.8; max-width:260px; font-family:\'DM Sans\',sans-serif; }',
    '.footer-desc { color:rgba(255,255,255,0.68); font-size:13.5px; line-height:1.8; max-width:260px; font-family:\'DM Sans\',sans-serif; }',
    "Footer description: raise opacity 0.45 → 0.68"
)

# Footer links: 0.45 → 0.68
replace(
    '.footer-link { display:block; color:rgba(255,255,255,0.45); font-size:13.5px; margin-bottom:9px; cursor:pointer; transition:all 0.18s; font-family:\'DM Sans\',sans-serif; }',
    '.footer-link { display:block; color:rgba(255,255,255,0.68); font-size:13.5px; margin-bottom:9px; cursor:pointer; transition:color 0.18s, transform 0.18s; font-family:\'DM Sans\',sans-serif; }',
    "Footer links: raise opacity 0.45 → 0.68, fix transition:all"
)

# Footer copyright: 0.28 → 0.52 (SEVERE failure)
replace(
    '.footer-bottom p { font-size:12px; color:rgba(255,255,255,0.28); font-family:\'DM Sans\',sans-serif; }',
    '.footer-bottom p { font-size:12px; color:rgba(255,255,255,0.52); font-family:\'DM Sans\',sans-serif; }',
    "Footer copyright: raise opacity 0.28 → 0.52 (WCAG severe failure)"
)

# med-also-desc: 0.55 → 0.72 (failing for 12.5px)
replace(
    '.med-also-desc { font-size:12.5px; color:rgba(255,255,255,0.55); line-height:1.55; }',
    '.med-also-desc { font-size:12.5px; color:rgba(255,255,255,0.72); line-height:1.55; }',
    "Healthcare also-section desc: raise opacity 0.55 → 0.72"
)

# .med-also-intro: 0.68 → 0.72 (small improvement for readability)
replace(
    '.med-also-intro { font-size:15.5px; color:rgba(255,255,255,0.68); line-height:1.82; max-width:680px; margin-bottom:32px; }',
    '.med-also-intro { font-size:15.5px; color:rgba(255,255,255,0.78); line-height:1.82; max-width:680px; margin-bottom:32px; }',
    "Healthcare also-section intro: raise opacity 0.68 → 0.78"
)

# Also raise bu-card body text: 0.52 → 0.68
replace(
    '.bu-card p { color:rgba(255,255,255,0.52); font-size:12.5px; line-height:1.65; margin-bottom:16px; font-family:\'DM Sans\',sans-serif; }',
    '.bu-card p { color:rgba(255,255,255,0.68); font-size:12.5px; line-height:1.65; margin-bottom:16px; font-family:\'DM Sans\',sans-serif; }',
    "Hero BU cards body text: raise opacity 0.52 → 0.68"
)

print("\n── transition:all → specific properties ──")

# nav-link: color + background only
replace(
    'cursor:pointer; transition:all 0.18s; position:relative; letter-spacing:0.01em;',
    'cursor:pointer; transition:color 0.18s, background 0.18s; position:relative; letter-spacing:0.01em;',
    "nav-link: transition:all → color + background"
)

# dd-item: color + background + transform
replace(
    'border-radius:8px; cursor:pointer; transition:all 0.15s;',
    'border-radius:8px; cursor:pointer; transition:color 0.15s, background 0.15s, transform 0.15s;',
    "dd-item: transition:all → color + background + transform"
)

# nav-cta: background + transform + box-shadow
replace(
    'cursor:pointer; border:none; font-family:\'DM Sans\',sans-serif;\n    transition:all 0.26s var(--ease-spring); letter-spacing:0.02em;',
    'cursor:pointer; border:none; font-family:\'DM Sans\',sans-serif;\n    transition:background 0.26s var(--ease-spring), transform 0.26s var(--ease-spring), box-shadow 0.26s var(--ease-spring); letter-spacing:0.02em;',
    "nav-cta: transition:all → background + transform + box-shadow"
)

# btn-primary: background + transform + box-shadow
replace(
    'font-family:\'DM Sans\',sans-serif; letter-spacing:0.025em;\n    transition:all 0.28s var(--ease-spring);',
    'font-family:\'DM Sans\',sans-serif; letter-spacing:0.025em;\n    transition:background 0.28s var(--ease-spring), transform 0.28s var(--ease-spring), box-shadow 0.28s var(--ease-spring);',
    "btn-primary: transition:all → background + transform + box-shadow"
)

# btn-outline: border-color + background + transform
replace(
    'cursor:pointer; border:1.5px solid rgba(255,255,255,0.4);\n    font-family:\'DM Sans\',sans-serif; letter-spacing:0.02em;\n    transition:all 0.26s var(--ease-spring);',
    'cursor:pointer; border:1.5px solid rgba(255,255,255,0.4);\n    font-family:\'DM Sans\',sans-serif; letter-spacing:0.02em;\n    transition:border-color 0.26s var(--ease-spring), background 0.26s var(--ease-spring), transform 0.26s var(--ease-spring);',
    "btn-outline: transition:all → border-color + background + transform"
)

# bu-card: background + border-color + transform + box-shadow (the border-top-color hover)
replace(
    'border-radius:18px; padding:28px 24px; cursor:pointer;\n    transition:all 0.3s var(--ease-spring); border-top:3px solid transparent;',
    'border-radius:18px; padding:28px 24px; cursor:pointer;\n    transition:background 0.3s var(--ease-spring), border-color 0.3s var(--ease-spring), transform 0.3s var(--ease-spring), box-shadow 0.3s var(--ease-spring); border-top:3px solid transparent;',
    "bu-card: transition:all → background + border-color + transform + box-shadow"
)

# slide-dot: explicitly name width + background (intentional layout animation for dot expand)
replace(
    'border-radius:2px; cursor:pointer; transition:all 0.3s;',
    'border-radius:2px; cursor:pointer; transition:background 0.3s, width 0.3s;',
    "slide-dot: transition:all → background + width (intentional width animation for active state)"
)

# stat-box: transform + box-shadow only
replace(
    'transition:all 0.22s; box-shadow:var(--shadow-card);',
    'transition:transform 0.22s, box-shadow 0.22s; box-shadow:var(--shadow-card);',
    "stat-box: transition:all → transform + box-shadow"
)

# pillar (on homepage): transition on transform + box-shadow + border-color
replace(
    'transition:all 0.28s var(--ease-spring); box-shadow:var(--shadow-card);\n    border-top:3px solid transparent;',
    'transition:transform 0.28s var(--ease-spring), box-shadow 0.28s var(--ease-spring), border-color 0.28s var(--ease-spring); box-shadow:var(--shadow-card);\n    border-top:3px solid transparent;',
    "pillar card: transition:all → transform + box-shadow + border-color"
)

# ind-card: transform + border-color + box-shadow
replace(
    'cursor:pointer; transition:all 0.3s var(--ease-spring); overflow:hidden;',
    'cursor:pointer; transition:transform 0.3s var(--ease-spring), border-color 0.3s var(--ease-spring), box-shadow 0.3s var(--ease-spring); overflow:hidden;',
    "ind-card: transition:all → transform + border-color + box-shadow"
)

# proto-pill: background + color + transform + box-shadow
replace(
    'color:rgba(255,255,255,0.5); cursor:pointer; transition:all 0.22s var(--ease-spring);',
    'color:rgba(255,255,255,0.5); cursor:pointer; transition:background 0.22s var(--ease-spring), color 0.22s var(--ease-spring), transform 0.22s var(--ease-spring), box-shadow 0.22s var(--ease-spring);',
    "proto-pill: transition:all → background + color + transform + box-shadow"
)

# semi-res-filter: background + color + border-color
replace(
    '.semi-res-filter { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:700; color:var(--gray); font-family:\'Montserrat\',sans-serif; background:var(--white); cursor:pointer; transition:all .15s; }',
    '.semi-res-filter { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:700; color:var(--gray); font-family:\'Montserrat\',sans-serif; background:var(--white); cursor:pointer; transition:background .15s, color .15s, border-color .15s; }',
    "semi-res-filter: transition:all → background + color + border-color"
)

print("\n── .semi-cross-nudge: upgrade from generic info box ──")
replace(
    '.semi-cross-nudge { margin-top:28px; background:var(--kblue-light); border-radius:10px; padding:18px 24px; font-size:13.5px; color:var(--dark-navy); line-height:1.7; }',
    '.semi-cross-nudge { margin-top:28px; background:var(--kblue-50); border:1.5px solid var(--kblue-light); border-radius:10px; padding:20px 24px; font-size:13.5px; color:var(--dark-navy); line-height:1.7; font-style:italic; }',
    "semi-cross-nudge: add border, refine padding, italic to distinguish as insight callout"
)

print("\n── Reduced-motion: add @media prefers-reduced-motion ──")
REDUCED_MOTION = """
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
    .hero-slide { transition: none !important; }
    #heroText { transition: none !important; }
  }
"""
replace(
    '</style>',
    REDUCED_MOTION + '</style>',
    "Add prefers-reduced-motion support"
)

print("\n── Summary ──")
print(f"Changes applied: {len(changes)}")
print(f"Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved.")
