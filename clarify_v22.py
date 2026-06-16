#!/usr/bin/env python3
# clarify_v22.py — Coming Soon badges + interim product lists on stub pages
filepath = '/Users/alexchan.ksa/Downloads/ksa-website-prototype/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
original_len = len(html)
changes = []

def replace(old, new, desc):
    global html
    count = html.count(old)
    if count == 0:
        print(f"  MISSING: {desc}")
        return False
    if count > 1:
        print(f"  AMBIGUOUS ({count} matches): {desc}")
        return False
    html = html.replace(old, new, 1)
    changes.append(desc)
    print(f"  ✓ {desc}")
    return True

# ── CSS additions ──────────────────────────────────────────────────────────────
print("── CSS additions ──")

replace(
    '  .semi-stub { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:52vh; padding:80px 56px; text-align:center; background:var(--offwhite); }\n'
    '  .semi-stub h1 { font-family:\'Montserrat\',sans-serif; font-size:clamp(22px,2.5vw,36px); font-weight:800; color:var(--dark-navy); margin-bottom:14px; letter-spacing:-0.02em; line-height:1.2; }\n'
    '  .semi-stub p { font-size:15px; color:var(--gray); line-height:1.85; max-width:480px; margin-bottom:28px; }',
    '  .semi-stub { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:52vh; padding:80px 56px; text-align:center; background:var(--offwhite); }\n'
    '  .semi-stub h1 { font-family:\'Montserrat\',sans-serif; font-size:clamp(22px,2.5vw,36px); font-weight:800; color:var(--dark-navy); margin-bottom:14px; letter-spacing:-0.02em; line-height:1.2; }\n'
    '  .semi-stub > p { font-size:15px; color:var(--gray); line-height:1.85; max-width:480px; margin-bottom:28px; }\n'
    '  .mega-cs-badge { display:inline-block; font-size:9px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; background:var(--kyellow); color:var(--dark-navy); border-radius:3px; padding:2px 6px; vertical-align:middle; margin-left:8px; font-family:\'Montserrat\',sans-serif; line-height:1.5; }\n'
    '  .semi-cs-badge { display:block; font-size:9.5px; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; background:var(--kyellow); color:var(--dark-navy); border-radius:4px; padding:3px 8px; margin-bottom:10px; font-family:\'Montserrat\',sans-serif; width:fit-content; }\n'
    '  .semi-stub-list { display:grid; grid-template-columns:1fr 1fr; gap:10px; max-width:580px; width:100%; margin:0 auto 32px; text-align:left; }\n'
    '  .semi-stub .semi-stub-list-item { background:var(--white); border:1.5px solid var(--border); border-radius:10px; padding:14px 16px; }\n'
    '  .semi-stub .semi-stub-list-item h4 { font-family:\'Montserrat\',sans-serif; font-size:12px; font-weight:700; color:var(--dark-navy); margin-bottom:4px; line-height:1.35; }\n'
    '  .semi-stub .semi-stub-list-item p { font-size:11.5px; color:var(--gray); line-height:1.5; margin:0; max-width:none; }',
    "Add Coming Soon badge CSS + stub product list CSS, refine .semi-stub > p selector"
)

# Add .semi-stub-list responsive to 768px block
replace(
    '    .semi-stub { padding:60px 24px; min-height:40vh; }',
    '    .semi-stub { padding:60px 24px; min-height:40vh; }\n'
    '    .semi-stub-list { grid-template-columns:1fr; }',
    "Add .semi-stub-list mobile column collapse to 768px breakpoint"
)

# ── Nav mega-menu: Coming Soon badges ─────────────────────────────────────────
print("\n── Nav: Coming Soon badges ──")

replace(
    '<div class="mega-sub-item" onclick="showPage(\'semi-fab\')">Fabrication &amp; Inspection Equipment</div>',
    '<div class="mega-sub-item" onclick="showPage(\'semi-fab\')">Fabrication &amp; Inspection Equipment<span class="mega-cs-badge">Soon</span></div>',
    "Nav: badge on semi-fab"
)

replace(
    '<div class="mega-sub-item" onclick="showPage(\'semi-gas\')">Gas, Chemical &amp; Wet Process Solutions</div>',
    '<div class="mega-sub-item" onclick="showPage(\'semi-gas\')">Gas, Chemical &amp; Wet Process Solutions<span class="mega-cs-badge">Soon</span></div>',
    "Nav: badge on semi-gas"
)

replace(
    '<div class="mega-sub-item" onclick="showPage(\'semi-parts\')">Parts, Maintenance &amp; Consumables</div>',
    '<div class="mega-sub-item" onclick="showPage(\'semi-parts\')">Parts, Maintenance &amp; Consumables<span class="mega-cs-badge">Soon</span></div>',
    "Nav: badge on semi-parts"
)

# ── Sol-cards on landing page: Coming Soon badges ─────────────────────────────
print("\n── Sol-cards: Coming Soon badges ──")

replace(
    '        <div class="semi-sol-card" onclick="showPage(\'semi-fab\')">\n'
    '          <div class="semi-sol-icon">&#128300;</div>\n'
    '          <h3>Fabrication &amp; Inspection Equipment</h3>',
    '        <div class="semi-sol-card" onclick="showPage(\'semi-fab\')">\n'
    '          <div class="semi-sol-icon">&#128300;</div>\n'
    '          <span class="semi-cs-badge">Coming Soon</span>\n'
    '          <h3>Fabrication &amp; Inspection Equipment</h3>',
    "Sol-card: Coming Soon badge on semi-fab"
)

replace(
    '        <div class="semi-sol-card" onclick="showPage(\'semi-gas\')">\n'
    '          <div class="semi-sol-icon">&#128299;</div>\n'
    '          <h3>Gas, Chemical &amp; Wet Process Solutions</h3>',
    '        <div class="semi-sol-card" onclick="showPage(\'semi-gas\')">\n'
    '          <div class="semi-sol-icon">&#128299;</div>\n'
    '          <span class="semi-cs-badge">Coming Soon</span>\n'
    '          <h3>Gas, Chemical &amp; Wet Process Solutions</h3>',
    "Sol-card: Coming Soon badge on semi-gas"
)

replace(
    '        <div class="semi-sol-card" onclick="showPage(\'semi-parts\')">\n'
    '          <div class="semi-sol-icon">&#128295;</div>\n'
    '          <h3>Parts, Maintenance &amp; Consumables</h3>',
    '        <div class="semi-sol-card" onclick="showPage(\'semi-parts\')">\n'
    '          <div class="semi-sol-icon">&#128295;</div>\n'
    '          <span class="semi-cs-badge">Coming Soon</span>\n'
    '          <h3>Parts, Maintenance &amp; Consumables</h3>',
    "Sol-card: Coming Soon badge on semi-parts"
)

# ── Stub pages: improve copy + add interim product lists ───────────────────────
print("\n── Stub pages: improved copy + product lists ──")

FAB_STUB_OLD = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:12px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Fabrication &amp; Inspection Equipment</h1>\n'
    '    <p style="font-size:13.5px;font-weight:600;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:16px">Wafer Inspection &mdash; Furnace Systems &mdash; Bonding &amp; De-Bonding</p>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:480px;margin-bottom:28px">This page is being updated. Our fabrication and inspection portfolio covers wafer surface inspection, horizontal furnace systems and wafer bonding equipment for front-end and advanced packaging processes. Contact us to discuss your requirements.</p>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showPage(\'contact\')">Get in Touch &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

FAB_STUB_NEW = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:14px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Fabrication &amp; Inspection Equipment</h1>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:560px;margin-bottom:24px">Front-end wafer fabrication and advanced packaging equipment for semiconductor fabs across Singapore and Malaysia. Speak to our team for specifications, compatibility and availability.</p>\n'
    '    <div class="semi-stub-list">\n'
    '      <div class="semi-stub-list-item"><h4>Wafer Surface Inspection Systems</h4><p>Optical defect detection for particle, scratch and pattern faults in front-end wafer processes</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Horizontal Diffusion Furnace Systems</h4><p>Batch thermal processing for oxidation, annealing and diffusion</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Wafer Bonding &amp; De-Bonding Equipment</h4><p>Temporary bonding systems for advanced packaging and 3DIC integration</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>High-Precision Capillary Printing</h4><p>Direct-write deposition for interconnect and advanced packaging applications</p></div>\n'
    '    </div>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showGatedForm(\'Fabrication &amp; Inspection Equipment &mdash; Product Enquiry\')">Enquire About This Portfolio &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

replace(FAB_STUB_OLD, FAB_STUB_NEW, "semi-fab: improved copy + product list + gated enquiry CTA")

GAS_STUB_OLD = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:12px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Gas, Chemical &amp; Wet Process Solutions</h1>\n'
    '    <p style="font-size:13.5px;font-weight:600;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:16px">Chemical Analysis &mdash; Specialty Gas &mdash; Scrubbers &amp; Abatement</p>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:480px;margin-bottom:28px">This page is being updated. Our gas and chemical portfolio covers real-time wet process chemical concentration analysis, specialty gas equipment, industrial scrubbers and abatement systems for semiconductor and cleanroom environments. Contact us to discuss your requirements.</p>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showPage(\'contact\')">Get in Touch &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

GAS_STUB_NEW = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:14px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Gas, Chemical &amp; Wet Process Solutions</h1>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:560px;margin-bottom:24px">Gas, chemical and wet process equipment for semiconductor fabs and cleanroom environments across Southeast Asia. Speak to our team for product selection, system design and technical specifications.</p>\n'
    '    <div class="semi-stub-list">\n'
    '      <div class="semi-stub-list-item"><h4>Real-Time Chemical Concentration Analysers</h4><p>In-line monitoring for HF, H&#8322;O&#8322;, NaOH, CP and wet process chemistries</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Specialty Gas Equipment</h4><p>Gas delivery, purification and monitoring systems for cleanroom process gases</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Industrial Exhaust Gas Scrubbers</h4><p>Acid, alkali and solvent abatement for semiconductor cleanroom exhaust systems</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Wet Process Chemical Supply</h4><p>Bulk chemical storage, distribution and dispensing systems for fabs</p></div>\n'
    '    </div>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showGatedForm(\'Gas, Chemical &amp; Wet Process Solutions &mdash; Product Enquiry\')">Enquire About This Portfolio &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

replace(GAS_STUB_OLD, GAS_STUB_NEW, "semi-gas: improved copy + product list + gated enquiry CTA")

PARTS_STUB_OLD = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:12px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Parts, Maintenance &amp; Consumables</h1>\n'
    '    <p style="font-size:13.5px;font-weight:600;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:16px">Sealing Solutions &mdash; Custom Fabrication &mdash; Fittings &amp; Diagnostics</p>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:480px;margin-bottom:28px">This page is being updated. Our parts and consumables portfolio covers genuine sealing solutions, custom fabrication materials, fittings, cleanroom components and circuit board diagnostics across all Semiconductor &amp; Industrial product lines. Contact us to discuss your requirements.</p>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showPage(\'contact\')">Get in Touch &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

PARTS_STUB_NEW = (
    '  <div class="semi-stub">\n'
    '    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:\'Montserrat\',sans-serif;margin-bottom:14px">Coming Soon</div>\n'
    '    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">Parts, Maintenance &amp; Consumables</h1>\n'
    '    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:560px;margin-bottom:24px">Genuine parts and consumables across all Semiconductor &amp; Industrial product lines &mdash; with responsive reorder support and short lead times. Contact us for availability, compatibility and pricing.</p>\n'
    '    <div class="semi-stub-list">\n'
    '      <div class="semi-stub-list-item"><h4>Sealing Solutions</h4><p>O-rings, gaskets and seals in PTFE, Kalrez and Viton for semiconductor process environments</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Custom Fabrication Materials</h4><p>Precision-machined components in process-compatible grades (PEEK, PTFE, Al, SS316L)</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Fittings &amp; Cleanroom Components</h4><p>VCR, Swagelok and ISO-KF fittings, valves and cleanroom-compatible flow components</p></div>\n'
    '      <div class="semi-stub-list-item"><h4>Circuit Board Diagnostics &amp; Repair</h4><p>PCB inspection, component-level fault diagnosis and board repair services</p></div>\n'
    '    </div>\n'
    '    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">\n'
    '      <button class="btn-primary" onclick="showGatedForm(\'Parts, Maintenance &amp; Consumables &mdash; Product Enquiry\')">Enquire About This Portfolio &#8594;</button>\n'
    '      <button class="btn-outline" onclick="showPage(\'semi\')">&#8592; Back to Semiconductor &amp; Industrial</button>\n'
    '    </div>\n'
    '  </div>'
)

replace(PARTS_STUB_OLD, PARTS_STUB_NEW, "semi-parts: improved copy + product list + gated enquiry CTA")

print("\n── Summary ──")
print(f"Changes applied: {len(changes)}")
print(f"Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved.")
