#!/usr/bin/env python3
# semi_cleanup.py
# 1. Remove emoji sol-card icons (photo overlay cards no longer need them)
# 2. Remove emoji pillar icons → replace with faded numbers 1-4
# 3. Semi landing hero → ph-hero style (matching personalhealth)
filepath = '/Users/alexchan.ksa/Downloads/ksa-website-prototype/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
original_len = len(html)
changes = []

def replace(old, new, desc):
    global html
    count = html.count(old)
    if count == 0:
        print(f'  MISSING: {desc}')
        return False
    if count > 1:
        print(f'  AMBIGUOUS ({count}): {desc}')
        return False
    html = html.replace(old, new, 1)
    changes.append(desc)
    print(f'  ✓ {desc}')
    return True

# ─────────────────────────────────────────────────────────────────────────────
# 1. CSS: pillar-icon → faded number style
# ─────────────────────────────────────────────────────────────────────────────
print('── CSS: pillar-icon faded number ──')
replace(
    '  .semi-pillar-icon { font-size:26px; margin-bottom:14px; }',
    "  .semi-pillar-icon { font-size:54px; font-weight:800; font-family:'Montserrat',sans-serif; color:rgba(26,75,156,0.11); line-height:1; margin-bottom:10px; letter-spacing:-0.03em; user-select:none; }",
    'semi-pillar-icon: faded number style'
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. HTML: Remove semi-sol-icon divs (photo overlay cards — icons clutter)
# ─────────────────────────────────────────────────────────────────────────────
print('\n── HTML: remove sol-card emoji icons ──')

SOL_ICONS = [
    '          <div class="semi-sol-icon">&#9889;</div>\n',       # energy ⚡
    '          <div class="semi-sol-icon">&#128225;</div>\n',     # predictive 📡
    '          <div class="semi-sol-icon">&#128293;</div>\n',     # heating 🔥
    '          <div class="semi-sol-icon">&#128300;</div>\n',     # fab 🔬
    '          <div class="semi-sol-icon">&#128299;</div>\n',     # gas 🔐?
    '          <div class="semi-sol-icon">&#128295;</div>\n',     # parts 🔧
]
for icon in SOL_ICONS:
    entity = icon.strip().replace('<div class="semi-sol-icon">', '').replace('</div>', '').strip()
    replace(icon, '', f'remove sol-icon {entity}')

# ─────────────────────────────────────────────────────────────────────────────
# 3. HTML: Replace emoji pillar icons with faded numbers
# ─────────────────────────────────────────────────────────────────────────────
print('\n── HTML: pillar emoji → faded numbers ──')

replace(
    '          <div class="semi-pillar-icon">&#128208;</div>',
    '          <div class="semi-pillar-icon">1</div>',
    'pillar icon 1: &#128208; → 1'
)
replace(
    '          <div class="semi-pillar-icon">&#9881;&#65039;</div>',
    '          <div class="semi-pillar-icon">2</div>',
    'pillar icon 2: ⚙️ → 2'
)
replace(
    '          <div class="semi-pillar-icon">&#128202;</div>',
    '          <div class="semi-pillar-icon">3</div>',
    'pillar icon 3: &#128202; → 3'
)
replace(
    '          <div class="semi-pillar-icon">&#128295;</div>',
    '          <div class="semi-pillar-icon">4</div>',
    'pillar icon 4: &#128295; → 4'
)

# ─────────────────────────────────────────────────────────────────────────────
# 4. HTML: Semi hero → ph-hero style
# ─────────────────────────────────────────────────────────────────────────────
print('\n── HTML: semi hero → ph-hero ──')
replace(
    "  <div class=\"med-sub-hero\" style=\"background:url('https://images.unsplash.com/photo-1518770660439-4636190af475?w=1400&q=85') center/cover no-repeat\">\n"
    "    <div class=\"med-sub-hero-overlay\"></div>\n"
    "    <div class=\"med-sub-hero-content\">\n"
    "      <div class=\"breadcrumb\" onclick=\"showPage('industries')\">&#8592; Our Solutions</div>\n"
    "      <div style=\"font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.55);font-family:'Syne',sans-serif;margin-bottom:14px\">Semiconductor &amp; Industrial Solutions</div>\n"
    "      <h1 style=\"font-family:'Montserrat',sans-serif;font-size:clamp(28px,4vw,54px);font-weight:800;color:var(--white);line-height:1.1;letter-spacing:-0.025em;margin-bottom:20px;max-width:740px\">The team that knows your process.</h1>\n"
    "      <p style=\"color:rgba(255,255,255,0.75);font-size:15.5px;line-height:1.85;max-width:640px;margin-bottom:30px\">From semiconductor fabrication facilities to pharmaceutical cleanrooms, food processing plants and industrial operations across Southeast Asia &mdash; Kromax South Asia partners with facilities managers, process engineers and procurement teams who need more than a supplier. With over 22 years in the semiconductor and industrial sectors, we bring deep engineering expertise across energy management, predictive monitoring, heating solutions, fabrication equipment, gas and chemical systems, and parts support. When something critical is at stake, we&rsquo;re the team you call.</p>\n"
    "      <button class=\"btn-primary\" onclick=\"document.getElementById('semi-solutions').scrollIntoView({behavior:'smooth'})\">Explore Our Solutions &#8595;</button>\n"
    "    </div>\n"
    "  </div>",

    "  <div class=\"ph-hero\" style=\"background-image:url('https://images.unsplash.com/photo-1518770660439-4636190af475?w=1400&q=85')\">\n"
    "    <div class=\"ph-hero-overlay\"></div>\n"
    "    <div class=\"ph-hero-content\">\n"
    "      <div class=\"breadcrumb\" onclick=\"showPage('industries')\">&#8592; Our Solutions</div>\n"
    "      <h1>Semiconductor &amp; Industrial</h1>\n"
    "      <div class=\"ph-hero-tagline\">The team that knows your process.</div>\n"
    "      <p>From semiconductor fabrication facilities to pharmaceutical cleanrooms, food processing plants and industrial operations across Southeast Asia &mdash; Kromax South Asia partners with facilities managers, process engineers and procurement teams who need more than a supplier. With over 22 years in the semiconductor and industrial sectors, we bring deep engineering expertise across energy management, predictive monitoring, heating solutions, fabrication equipment, gas and chemical systems, and parts support. When something critical is at stake, we&rsquo;re the team you call.</p>\n"
    "      <div class=\"ph-hero-cta\">\n"
    "        <button class=\"btn-primary\" onclick=\"document.getElementById('semi-solutions').scrollIntoView({behavior:'smooth'})\">Explore Our Solutions &#8595;</button>\n"
    "      </div>\n"
    "    </div>\n"
    "  </div>",
    'semi landing hero: med-sub-hero → ph-hero'
)

# ─────────────────────────────────────────────────────────────────────────────
print('\n── Summary ──')
print(f'Changes applied: {len(changes)}')
print(f'Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved.')
