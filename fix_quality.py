#!/usr/bin/env python3
# fix_quality.py — code-quality + emoji cleanup pass
#  A. Replace all `transition:all` with specific properties (design-system compliance)
#  B. Emoji removal site-wide (faded numbers for icon grids, strip for pills/labels)
#  C. loading="lazy" on remaining hotlinked <img>
# Keeps functional glyphs: arrows, dropdown carets, info, map geo markers, preview banner.
import re

filepath = '/Users/alexchan.ksa/Downloads/ksa-website-prototype/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
original_len = len(html)
changes = []

def lit(old, new, desc, expect=1):
    """Literal replace with count assertion."""
    global html
    n = html.count(old)
    if n != expect:
        print(f'  !! {desc}: expected {expect}, found {n} — SKIPPED')
        return
    html = html.replace(old, new)
    changes.append(desc)
    print(f'  ✓ {desc} (×{n})')

def rx(pattern, repl, desc, expect=None, flags=0):
    """Regex replace with optional count assertion."""
    global html
    matches = re.findall(pattern, html, flags)
    n = len(matches)
    if expect is not None and n != expect:
        print(f'  !! {desc}: expected {expect}, found {n} — SKIPPED')
        return
    if n == 0:
        print(f'  !! {desc}: 0 matches — SKIPPED')
        return
    html = re.sub(pattern, repl, html, flags=flags)
    changes.append(desc)
    print(f'  ✓ {desc} (×{n})')

def rx_counter(pattern, values, desc, flags=0):
    """Regex replace, cycling through `values` positionally."""
    global html
    state = {'i': 0}
    def _sub(m):
        v = values[state['i'] % len(values)]
        state['i'] += 1
        return m.group(1) + str(v) + m.group(2)
    new_html, n = re.subn(pattern, _sub, html, flags=flags)
    if n == 0:
        print(f'  !! {desc}: 0 matches — SKIPPED')
        return
    html = new_html
    changes.append(desc)
    print(f'  ✓ {desc} (×{n})')

# ─────────────────────────────────────────────────────────────────────────────
print('── A. transition:all → specific (CSS) ──')
lit('cursor:pointer; transition:all 0.28s var(--ease-spring);',
    'cursor:pointer; transition:border-color 0.28s var(--ease-spring),box-shadow 0.28s var(--ease-spring),transform 0.28s var(--ease-spring);',
    '.sol-card transition')
lit('transition:all 0.15s; margin-bottom:0; background:transparent;',
    'transition:background 0.15s,color 0.15s; margin-bottom:0; background:transparent;',
    '.mega-group (mobile) transition')
lit('background:var(--kblue); border-radius:2px; transition:all 0.22s ease;',
    'background:var(--kblue); border-radius:2px; transition:transform 0.22s ease,opacity 0.22s ease,background 0.22s ease;',
    '.nav-hamburger span transition')
lit('transition:all 0.15s; margin-bottom:2px;',
    'transition:background 0.15s; margin-bottom:2px;',
    '.mega-group (desktop) transition')
lit('.mega-group-arrow { font-size:14px; color:var(--gray); transition:all 0.15s; line-height:1; }',
    '.mega-group-arrow { font-size:14px; color:var(--gray); transition:color 0.15s,transform 0.15s; line-height:1; }',
    '.mega-group-arrow transition')
lit('border-radius:8px; cursor:pointer; transition:all 0.15s;',
    'border-radius:8px; cursor:pointer; transition:background 0.15s,color 0.15s,padding-left 0.15s;',
    '.mega-sub-item transition')
lit('    border:1.5px solid var(--border); background:var(--white); color:var(--gray);\n    transition:all .18s;',
    '    border:1.5px solid var(--border); background:var(--white); color:var(--gray);\n    transition:background .18s,color .18s,border-color .18s;',
    '.med-filter-btn transition')

print('\n── A. transition:all → specific (inline) ──')
lit(';transition:all 0.22s"', ';transition:transform 0.22s,box-shadow 0.22s"',
    'news cards transition', expect=6)
lit('overflow:hidden;transition:all 0.2s;cursor:pointer',
    'overflow:hidden;transition:transform 0.2s,box-shadow 0.2s;cursor:pointer',
    'resource cards transition', expect=6)
lit('cursor:pointer;transition:all 0.2s"', 'cursor:pointer;transition:border-color 0.2s"',
    'careers job rows transition', expect=4)
lit('overflow:hidden;transition:all 0.2s"', 'overflow:hidden;transition:transform 0.2s,box-shadow 0.2s"',
    'shop item cards transition', expect=6)
lit(';transition:all 0.18s"', ';transition:background 0.18s"',
    'add-to-cart buttons transition', expect=6)

# ─────────────────────────────────────────────────────────────────────────────
print('\n── B. Icon-grid emoji → faded numbers ──')
# semicon "Key Advantages" — 3 sections × 4 cards, faded ghost numbers
lit('.med-adv-icon { font-size:26px; margin-bottom:14px; }',
    ".med-adv-icon { font-size:54px; font-weight:800; font-family:'Montserrat',sans-serif; color:rgba(26,75,156,0.11); line-height:1; margin-bottom:10px; letter-spacing:-0.03em; user-select:none; }",
    '.med-adv-icon CSS → faded number')
rx_counter(r'(<div class="med-adv-icon">)[^<]*(</div>)', [1,2,3,4],
           'med-adv-icon emoji → 1-4')

# About "why us" pillars — 3 cards, faded numbers
lit('.pillar .ico { font-size:30px; margin-bottom:16px; display:block; }',
    ".pillar .ico { font-size:48px; font-weight:800; font-family:'Montserrat',sans-serif; color:rgba(26,75,156,0.11); line-height:1; margin-bottom:12px; letter-spacing:-0.03em; display:block; user-select:none; }",
    '.pillar .ico CSS → faded number')
rx_counter(r'(<div class="ico">)[^<]*(</div>)', [1,2,3],
           'about pillar .ico emoji → 1-3')

# Medical "why partner" pillars — keep blue badge box, white numbers
lit('    font-size:22px; margin-bottom:18px;\n  }',
    "    font-size:22px; font-weight:800; font-family:'Montserrat',sans-serif; color:#fff; margin-bottom:18px;\n  }",
    '.med-pillar-icon CSS → white number')
rx_counter(r'(<div class="med-pillar-icon">)[^<]*(</div>)', [1,2,3,4],
           'med-pillar-icon emoji → 1-4')

# ─────────────────────────────────────────────────────────────────────────────
print('\n── B. Icon-box emoji → removed ──')
# medical brochure cards (44px icon boxes)
rx(r'<div style="width:44px;height:44px;background:var\(--kblue-light\);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px">[^<]*</div>\n\s*',
   '', 'medical brochure icon boxes removed', expect=3)
# careers partner cards (28px emoji)
rx(r'<div style="font-size:28px;margin-bottom:8px">[^<]*</div>\n\s*',
   '', 'careers partner card emoji removed', expect=4)
# shop bulk-orders icon
rx(r'<div style="font-size:36px">[^<]*</div>\n\s*',
   '', 'shop bulk-order emoji removed', expect=1)
# contact email / linkedin inline emoji spans
rx(r'<span style="font-size:20px;margin-top:2px">[^<]*</span>',
   '', 'contact inline emoji spans removed', expect=2)

# ─────────────────────────────────────────────────────────────────────────────
print('\n── B. QI step-flow emoji → removed (inline + JS-injected) ──')
rx(r'<div class="ph-qi-step-icon">[^<]*</div>', '',
   'ph-qi-step-icon emoji removed')

# ─────────────────────────────────────────────────────────────────────────────
print('\n── B. Pill / label prefix emoji → stripped ──')
# PH audience pills: strip leading emoji + space (everything before first letter)
rx(r'(<span class="ph-audience-pill">)[^A-Za-z<]+', r'\1',
   'ph-audience-pill emoji prefixes stripped')
# Members-only labels
lit('🔒 MEMBERS ONLY', 'MEMBERS ONLY', 'MEMBERS ONLY label emoji', expect=2)
# Search overlay quick chips
lit('>⚙️ Semiconductor Solutions<', '>Semiconductor Solutions<', 'search chip ⚙️', expect=1)
lit('>📩 Request a Quote<', '>Request a Quote<', 'search chip 📩', expect=1)
# About region flag tags (map markers keep theirs — different surrounding text)
lit('>🇸🇬 Singapore HQ<', '>Singapore HQ<', 'about flag SG', expect=1)
lit('>🇲🇾 Malaysia<', '>Malaysia<', 'about flag MY', expect=1)
lit('>🇮🇩 Indonesia<', '>Indonesia<', 'about flag ID', expect=1)
lit('>🇹🇼 Taiwan<', '>Taiwan<', 'about flag TW', expect=1)
# Form success emoji
lit("'✅ Submitted! We\\'ll be in touch within 24 hours.'",
    "'Submitted! We\\'ll be in touch within 24 hours.'",
    'form success ✅', expect=1)

# ─────────────────────────────────────────────────────────────────────────────
print('\n── C. loading="lazy" on remaining <img> ──')
before = html.count('loading="lazy"')
html = re.sub(r'<img (?!loading=)', '<img loading="lazy" ', html)
after = html.count('loading="lazy"')
print(f'  ✓ added loading="lazy" to {after - before} imgs (had {before}, now {after})')
changes.append('loading=lazy on imgs')

# ─────────────────────────────────────────────────────────────────────────────
print('\n── Summary ──')
print(f'Changes applied: {len(changes)}')
print(f'Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved.')
