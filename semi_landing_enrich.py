#!/usr/bin/env python3
# semi_landing_enrich.py
# - Sol-cards: convert to photo overlay cards (dark gradient + hover reveal)
# - Kw-cards: add image banner strip at top of each card
# - Pills: staggered entrance animation + hover colour fill
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
# 1. CSS — sol-cards → photo overlay cards
# ─────────────────────────────────────────────────────────────────────────────
print('── CSS: sol-card photo overlay ──')

replace(
    '  .semi-sol-card { background:var(--white); border:1.5px solid var(--border); border-radius:14px; padding:28px 24px 24px; transition:box-shadow .2s,transform .2s; cursor:pointer; }\n'
    '  .semi-sol-card:hover { box-shadow:0 8px 32px rgba(26,75,156,0.14); transform:translateY(-3px); }\n'
    '  .semi-sol-icon { font-size:28px; margin-bottom:14px; }\n'
    "  .semi-sol-card h3 { font-family:'Montserrat',sans-serif; font-size:15px; font-weight:800; color:var(--dark-navy); margin-bottom:8px; line-height:1.3; }\n"
    '  .semi-sol-card p { font-size:13px; color:var(--gray); line-height:1.72; margin-bottom:18px; }\n'
    "  .semi-sol-link { font-size:13px; font-weight:700; color:var(--kblue); font-family:'Montserrat',sans-serif; }",
    '  .semi-sol-card { background-size:cover; background-position:center; border:none; border-radius:14px; padding:0; min-height:230px; position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:flex-end; transition:box-shadow .3s ease,transform .3s ease; cursor:pointer; }\n'
    '  .semi-sol-card::before { content:\'\'; position:absolute; inset:0; background:linear-gradient(to top,rgba(10,20,50,0.94) 0%,rgba(10,20,50,0.52) 52%,rgba(10,20,50,0.14) 100%); transition:background 0.38s ease; z-index:1; }\n'
    '  .semi-sol-card:hover { box-shadow:0 16px 44px rgba(8,18,40,0.34); transform:translateY(-3px); }\n'
    '  .semi-sol-card:hover::before { background:linear-gradient(to top,rgba(10,20,50,0.97) 0%,rgba(10,20,50,0.78) 58%,rgba(10,20,50,0.42) 100%); }\n'
    '  .semi-sol-icon { position:absolute; top:14px; left:14px; z-index:2; font-size:18px; width:34px; height:34px; border-radius:8px; background:rgba(255,255,255,0.15); display:flex; align-items:center; justify-content:center; }\n'
    "  .semi-sol-card h3 { font-family:'Montserrat',sans-serif; font-size:14px; font-weight:800; color:#fff; margin-bottom:6px; line-height:1.3; position:relative; z-index:2; padding:0 16px; }\n"
    '  .semi-sol-card p { font-size:12px; color:rgba(255,255,255,0.8); line-height:1.65; position:relative; z-index:2; padding:0 16px; margin-bottom:10px; max-height:0; overflow:hidden; opacity:0; transform:translateY(4px); transition:max-height 0.38s ease,opacity 0.28s ease 0.06s,transform 0.32s ease; }\n'
    '  .semi-sol-card:hover p { max-height:120px; opacity:1; transform:translateY(0); }\n'
    "  .semi-sol-link { font-size:12.5px; font-weight:700; color:var(--kyellow); font-family:'Montserrat',sans-serif; position:relative; z-index:2; padding:0 16px 16px; display:block; }",
    'sol-card CSS → photo overlay card with hover reveal'
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. CSS — cs-badge: add z-index + left indent for overlay context
# ─────────────────────────────────────────────────────────────────────────────
print('\n── CSS: cs-badge overlay positioning ──')

replace(
    "  .semi-cs-badge { display:block; font-size:9.5px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; background:var(--kyellow); color:var(--dark-navy); border-radius:4px; padding:3px 8px; margin-bottom:10px; font-family:'Montserrat',sans-serif; width:fit-content; }",
    "  .semi-cs-badge { display:block; font-size:9.5px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; background:var(--kyellow); color:var(--dark-navy); border-radius:4px; padding:3px 8px; margin-bottom:6px; margin-left:16px; font-family:'Montserrat',sans-serif; width:fit-content; position:relative; z-index:2; }",
    'cs-badge: add z-index:2 + margin-left for overlay context'
)

# ─────────────────────────────────────────────────────────────────────────────
# 3. CSS — kw-cards: add image strip + body wrapper
# ─────────────────────────────────────────────────────────────────────────────
print('\n── CSS: kw-card image strip ──')

replace(
    '  .semi-kw-card { background:var(--white); border:1.5px solid var(--border); border-radius:12px; padding:20px 18px 16px; cursor:pointer; transition:box-shadow .18s,transform .18s; }\n'
    '  .semi-kw-card:hover { box-shadow:var(--shadow-card-hover); transform:translateY(-2px); }\n'
    "  .semi-kw-card h4 { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; color:var(--dark-navy); margin-bottom:6px; line-height:1.3; }\n"
    '  .semi-kw-card p { font-size:12px; color:var(--gray); line-height:1.65; margin-bottom:10px; }\n'
    "  .semi-kw-link { font-size:12px; font-weight:700; color:var(--kblue); font-family:'Montserrat',sans-serif; }",
    '  .semi-kw-card { background:var(--white); border:1.5px solid var(--border); border-radius:12px; padding:0; cursor:pointer; transition:box-shadow .18s ease,transform .18s ease; overflow:hidden; }\n'
    '  .semi-kw-card:hover { box-shadow:var(--shadow-card-hover); transform:translateY(-2px); }\n'
    '  .semi-kw-img { width:100%; height:96px; background-size:cover; background-position:center; display:block; }\n'
    '  .semi-kw-body { padding:14px 18px 14px; }\n'
    "  .semi-kw-card h4 { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; color:var(--dark-navy); margin-bottom:6px; line-height:1.3; }\n"
    '  .semi-kw-card p { font-size:12px; color:var(--gray); line-height:1.65; margin-bottom:10px; }\n'
    "  .semi-kw-link { font-size:12px; font-weight:700; color:var(--kblue); font-family:'Montserrat',sans-serif; }",
    'kw-card CSS: add image strip + body wrapper'
)

# ─────────────────────────────────────────────────────────────────────────────
# 4. CSS — pills: entrance animation + hover fill
# ─────────────────────────────────────────────────────────────────────────────
print('\n── CSS: pill animation ──')

replace(
    "  .semi-pill { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:600; color:var(--dark-navy); font-family:'Montserrat',sans-serif; background:var(--white); }\n"
    '  .semi-pill.test { font-size:11.5px; background:var(--kblue-50); border-color:var(--kblue-light); color:var(--gray); font-style:italic; }',
    "  @keyframes pillIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }\n"
    "  .semi-pill { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:600; color:var(--dark-navy); font-family:'Montserrat',sans-serif; background:var(--white); opacity:0; cursor:default; transition:background 0.22s ease,color 0.22s ease,border-color 0.22s ease,transform 0.2s ease; }\n"
    "  .semi-pill:hover { background:var(--kblue); color:#fff; border-color:var(--kblue); transform:translateY(-2px); }\n"
    '  .semi-pill.test { font-size:11.5px; background:var(--kblue-50); border-color:var(--kblue-light); color:var(--gray); font-style:italic; }\n'
    "  .semi-pill.test:hover { background:var(--kblue-light); color:var(--kblue); border-color:var(--kblue-mid); transform:translateY(-2px); }\n"
    '  .semi-pills.anim .semi-pill { animation:pillIn 0.42s ease forwards; }\n'
    '  .semi-pills.anim .semi-pill:nth-child(1){animation-delay:0s} .semi-pills.anim .semi-pill:nth-child(2){animation-delay:0.04s} .semi-pills.anim .semi-pill:nth-child(3){animation-delay:0.08s} .semi-pills.anim .semi-pill:nth-child(4){animation-delay:0.12s}\n'
    '  .semi-pills.anim .semi-pill:nth-child(5){animation-delay:0.16s} .semi-pills.anim .semi-pill:nth-child(6){animation-delay:0.20s} .semi-pills.anim .semi-pill:nth-child(7){animation-delay:0.24s} .semi-pills.anim .semi-pill:nth-child(8){animation-delay:0.28s}\n'
    '  .semi-pills.anim .semi-pill:nth-child(9){animation-delay:0.32s} .semi-pills.anim .semi-pill:nth-child(10){animation-delay:0.36s} .semi-pills.anim .semi-pill:nth-child(11){animation-delay:0.40s} .semi-pills.anim .semi-pill:nth-child(12){animation-delay:0.44s}\n'
    '  .semi-pills.anim .semi-pill:nth-child(13){animation-delay:0.48s} .semi-pills.anim .semi-pill:nth-child(14){animation-delay:0.52s} .semi-pills.anim .semi-pill:nth-child(15){animation-delay:0.56s} .semi-pills.anim .semi-pill:nth-child(16){animation-delay:0.60s}',
    'pills CSS: entrance keyframe animation + hover colour fill + stagger delays'
)

# reduced-motion: show pills immediately
replace(
    '    .semi-stub { padding:60px 24px; min-height:40vh; }\n'
    '    .semi-stub-list { grid-template-columns:1fr; }',
    '    .semi-stub { padding:60px 24px; min-height:40vh; }\n'
    '    .semi-stub-list { grid-template-columns:1fr; }\n'
    '  }\n'
    '  @media (prefers-reduced-motion: reduce) {\n'
    '    .semi-pill { opacity:1 !important; animation:none !important; transform:none !important; }\n'
    '    .semi-sol-card p { transition:none; }',
    'pills + sol-card: prefers-reduced-motion overrides'
)

# ─────────────────────────────────────────────────────────────────────────────
# 5. HTML — sol-cards: add background-image per card
# ─────────────────────────────────────────────────────────────────────────────
print('\n── HTML: sol-card background images ──')

IMG = {
    'semi-energy':    'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=600&q=80',
    'semi-predictive':'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=600&q=80',
    'semi-heating':   'https://images.unsplash.com/photo-1565514020179-026b92b84bb6?w=600&q=80',
    'semi-fab':       'https://images.unsplash.com/photo-1518770660439-4636190af475?w=600&q=80',
    'semi-gas':       'https://images.unsplash.com/photo-1569428034239-f9565e32e224?w=600&q=80',
    'semi-parts':     'https://images.unsplash.com/photo-1585435557343-3b092031a831?w=600&q=80',
}
for page_id, img_url in IMG.items():
    replace(
        f'        <div class="semi-sol-card" onclick="showPage(\'{page_id}\')">\n',
        f'        <div class="semi-sol-card" style="background-image:url(\'{img_url}\')" onclick="showPage(\'{page_id}\')">\n',
        f'sol-card photo: {page_id}'
    )

# ─────────────────────────────────────────────────────────────────────────────
# 6. HTML — kw-cards: add image strip + body wrapper (8 cards)
# ─────────────────────────────────────────────────────────────────────────────
print('\n── HTML: kw-card image strips ──')

KW = [
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-energy\')">\n'
            '          <h4>AI Chiller &amp; HVAC Optimisation</h4>\n'
            '          <p>Cut energy costs in semiconductor fabs and industrial facilities with AI-driven chiller control.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=400&q=80',
        'title': 'AI Chiller & HVAC Optimisation',
        'p': 'Cut energy costs in semiconductor fabs and industrial facilities with AI-driven chiller control.',
        'onclick': "showPage('semi-energy')",
        'desc': 'kw-card: AI Chiller'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-energy\')">\n'
            '          <h4>Equipment Energy Monitoring &amp; ESG Compliance</h4>\n'
            '          <p>Real-time machine-level energy visibility with built-in ISO&nbsp;50001 and SEMI&nbsp;S23 compliance.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43?w=400&q=80',
        'title': 'Equipment Energy Monitoring &amp; ESG Compliance',
        'p': 'Real-time machine-level energy visibility with built-in ISO&nbsp;50001 and SEMI&nbsp;S23 compliance.',
        'onclick': "showPage('semi-energy')",
        'desc': 'kw-card: Energy Monitoring'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-predictive\')">\n'
            '          <h4>Predictive Maintenance &amp; Smart Sensors</h4>\n'
            '          <p>Prevent unplanned downtime with patented smart sensors for critical fab equipment.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=400&q=80',
        'title': 'Predictive Maintenance &amp; Smart Sensors',
        'p': 'Prevent unplanned downtime with patented smart sensors for critical fab equipment.',
        'onclick': "showPage('semi-predictive')",
        'desc': 'kw-card: Predictive Maintenance'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-heating\')">\n'
            '          <h4>Custom Heating &amp; Thermal Insulation</h4>\n'
            '          <p>Precision heating jackets and temperature control systems for OEM and process equipment.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1565514020179-026b92b84bb6?w=400&q=80',
        'title': 'Custom Heating &amp; Thermal Insulation',
        'p': 'Precision heating jackets and temperature control systems for OEM and process equipment.',
        'onclick': "showPage('semi-heating')",
        'desc': 'kw-card: Custom Heating'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-fab\')">\n'
            '          <h4>Wafer Inspection &amp; Defect Detection</h4>\n'
            '          <p>Surface and macro inspection systems for unpatterned and patterned wafers, front-end processes.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&q=80',
        'title': 'Wafer Inspection &amp; Defect Detection',
        'p': 'Surface and macro inspection systems for unpatterned and patterned wafers, front-end processes.',
        'onclick': "showPage('semi-fab')",
        'desc': 'kw-card: Wafer Inspection'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-fab\')">\n'
            '          <h4>Advanced Packaging &amp; Bonding</h4>\n'
            '          <p>Wafer bonding, de-bonding and high-precision printing for advanced packaging applications.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1585435557343-3b092031a831?w=400&q=80',
        'title': 'Advanced Packaging &amp; Bonding',
        'p': 'Wafer bonding, de-bonding and high-precision printing for advanced packaging applications.',
        'onclick': "showPage('semi-fab')",
        'desc': 'kw-card: Advanced Packaging'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-gas\')">\n'
            '          <h4>Gas Safety &amp; Scrubber Systems</h4>\n'
            '          <p>Turnkey specialty gas equipment, industrial scrubbers and abatement for fab and chemical facilities.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1569428034239-f9565e32e224?w=400&q=80',
        'title': 'Gas Safety &amp; Scrubber Systems',
        'p': 'Turnkey specialty gas equipment, industrial scrubbers and abatement for fab and chemical facilities.',
        'onclick': "showPage('semi-gas')",
        'desc': 'kw-card: Gas Safety'
    },
    {
        'old': (
            '        <div class="semi-kw-card" onclick="showPage(\'semi-gas\')">\n'
            '          <h4>Wet Process Chemical Analysis</h4>\n'
            '          <p>Real-time concentration monitoring for SC-1, SC-2, HF and other wet process chemistries.</p>\n'
            '          <div class="semi-kw-link">Learn More &#8594;</div>\n'
            '        </div>'
        ),
        'img': 'https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=400&q=80',
        'title': 'Wet Process Chemical Analysis',
        'p': 'Real-time concentration monitoring for SC-1, SC-2, HF and other wet process chemistries.',
        'onclick': "showPage('semi-gas')",
        'desc': 'kw-card: Wet Process Chemical'
    },
]

for card in KW:
    new_html = (
        f'        <div class="semi-kw-card" onclick="{card["onclick"]}">\n'
        f'          <div class="semi-kw-img" style="background-image:url(\'{card["img"]}\')"></div>\n'
        f'          <div class="semi-kw-body">\n'
        f'            <h4>{card["title"]}</h4>\n'
        f'            <p>{card["p"]}</p>\n'
        f'            <div class="semi-kw-link">Learn More &#8594;</div>\n'
        f'          </div>\n'
        f'        </div>'
    )
    replace(card['old'], new_html, card['desc'])

# ─────────────────────────────────────────────────────────────────────────────
# 7. JS — IntersectionObserver for pills entrance
# ─────────────────────────────────────────────────────────────────────────────
print('\n── JS: pills IntersectionObserver ──')

replace(
    'function filterSemiRes(cat, btn) {',
    '// Semi pills entrance animation\n'
    '(function(){\n'
    '  var pills = document.querySelector(\'#page-semi .semi-pills\');\n'
    '  if(!pills){ return; }\n'
    '  if(!window.IntersectionObserver){ pills.classList.add(\'anim\'); return; }\n'
    '  var io = new IntersectionObserver(function(entries){\n'
    '    entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add(\'anim\'); io.unobserve(e.target); } });\n'
    '  }, { threshold:0.2 });\n'
    '  io.observe(pills);\n'
    '})();\n\n'
    'function filterSemiRes(cat, btn) {',
    'JS: IntersectionObserver for semi pills entrance animation'
)

# ─────────────────────────────────────────────────────────────────────────────
print('\n── Summary ──')
print(f'Changes applied: {len(changes)}')
print(f'Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})')
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved.')
