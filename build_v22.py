#!/usr/bin/env python3
# build_v22.py — Semiconductor & Industrial pages build script
import sys, os
filepath = '/Users/alexchan.ksa/Downloads/ksa-website-prototype/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()
original_len = len(html)
print(f"Loaded {len(html):,} chars")

# ─────────────────────────────────────────
# 1. VERSION
# ─────────────────────────────────────────
html = html.replace(
    'Kromax South Asia — Website Prototype v21',
    'Kromax South Asia — Website Prototype v22', 1
)

# ─────────────────────────────────────────
# 2. NAV SEMICONDUCTOR SUB-ITEMS
# ─────────────────────────────────────────
OLD_NAV = """            <div class="mega-sub ms-active" id="mega-semi">
              <div class="mega-sub-label">Semiconductor &amp; Industrial</div>
              <div class="mega-sub-item" onclick="showPage('solar')">Intelligent Solar &amp; Sustainability</div>
              <div class="mega-sub-item" onclick="showPage('semi')">AI Chiller Energy Optimisation</div>
              <div class="mega-sub-item" onclick="showPage('semi')">Smart Factory Monitoring</div>
              <div class="mega-sub-item" onclick="showPage('semi')">Predictive Equipment Health</div>
              <div class="mega-sub-item" onclick="showPage('semi')">Gas Safety &amp; Scrubber Systems</div>
            </div>"""
NEW_NAV = """            <div class="mega-sub ms-active" id="mega-semi">
              <div class="mega-sub-label">Semiconductor &amp; Industrial</div>
              <div class="mega-sub-item" onclick="showPage('semi-energy')">Energy Management &amp; Sustainability</div>
              <div class="mega-sub-item" onclick="showPage('semi-predictive')">Predictive Equipment Health &amp; Monitoring</div>
              <div class="mega-sub-item" onclick="showPage('semi-heating')">Industrial Heating Solutions</div>
              <div class="mega-sub-item" onclick="showPage('semi-fab')">Fabrication &amp; Inspection Equipment</div>
              <div class="mega-sub-item" onclick="showPage('semi-gas')">Gas, Chemical &amp; Wet Process Solutions</div>
              <div class="mega-sub-item" onclick="showPage('semi-parts')">Parts, Maintenance &amp; Consumables</div>
            </div>"""
assert OLD_NAV in html, "NAV anchor not found"
html = html.replace(OLD_NAV, NEW_NAV, 1)
print("Nav updated")

# ─────────────────────────────────────────
# 3. CSS ADDITIONS
# ─────────────────────────────────────────
NEW_CSS = """
  /* ═══ SEMICONDUCTOR & INDUSTRIAL — v22 ═══ */
  .semi-sol-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:22px; margin-top:32px; }
  .semi-sol-card { background:var(--white); border:1.5px solid var(--border); border-radius:14px; padding:28px 24px 24px; transition:box-shadow .2s,transform .2s; cursor:pointer; }
  .semi-sol-card:hover { box-shadow:0 8px 32px rgba(26,75,156,0.14); transform:translateY(-3px); }
  .semi-sol-icon { font-size:28px; margin-bottom:14px; }
  .semi-sol-card h3 { font-family:'Montserrat',sans-serif; font-size:15px; font-weight:800; color:var(--dark-navy); margin-bottom:8px; line-height:1.3; }
  .semi-sol-card p { font-size:13px; color:var(--gray); line-height:1.72; margin-bottom:18px; }
  .semi-sol-link { font-size:13px; font-weight:700; color:var(--kblue); font-family:'Montserrat',sans-serif; }
  .semi-kw-section { background:#f4f7fc; padding:60px 56px; }
  .semi-kw-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:24px; }
  .semi-kw-card { background:var(--white); border:1.5px solid var(--border); border-radius:12px; padding:20px 18px 16px; cursor:pointer; transition:box-shadow .18s,transform .18s; }
  .semi-kw-card:hover { box-shadow:var(--shadow-card-hover); transform:translateY(-2px); }
  .semi-kw-card h4 { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; color:var(--dark-navy); margin-bottom:6px; line-height:1.3; }
  .semi-kw-card p { font-size:12px; color:var(--gray); line-height:1.65; margin-bottom:10px; }
  .semi-kw-link { font-size:12px; font-weight:700; color:var(--kblue); font-family:'Montserrat',sans-serif; }
  .semi-pill-section { background:var(--white); padding:56px 56px; }
  .semi-pills { display:flex; flex-wrap:wrap; gap:8px; margin-top:20px; }
  .semi-pill { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:600; color:var(--dark-navy); font-family:'Montserrat',sans-serif; background:var(--white); }
  .semi-pill.test { font-size:11.5px; background:var(--kblue-50); border-color:var(--kblue-light); color:var(--gray); font-style:italic; }
  .semi-pillar-section { background:#f4f7fc; padding:72px 56px; }
  .semi-pillar-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:22px; margin-top:32px; }
  .semi-pillar-card { background:var(--white); border:1.5px solid var(--border); border-radius:14px; padding:28px 22px; }
  .semi-pillar-icon { font-size:26px; margin-bottom:14px; }
  .semi-pillar-card h3 { font-family:'Montserrat',sans-serif; font-size:14px; font-weight:800; color:var(--dark-navy); margin-bottom:8px; line-height:1.3; }
  .semi-pillar-card p { font-size:13px; color:var(--gray); line-height:1.72; }
  .semi-cross-nudge { margin-top:28px; background:var(--kblue-light); border-radius:10px; padding:18px 24px; font-size:13.5px; color:var(--dark-navy); line-height:1.7; }
  .semi-res-section { background:var(--white); padding:72px 56px; }
  .semi-res-filters { display:flex; flex-wrap:wrap; gap:8px; margin:20px 0 28px; }
  .semi-res-filter { padding:7px 16px; border-radius:100px; border:1.5px solid var(--border); font-size:12.5px; font-weight:700; color:var(--gray); font-family:'Montserrat',sans-serif; background:var(--white); cursor:pointer; transition:all .15s; }
  .semi-res-filter.active,.semi-res-filter:hover { background:var(--kblue); color:var(--white); border-color:var(--kblue); }
  .semi-res-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }
  .semi-res-card { border:1.5px solid var(--border); border-radius:12px; padding:20px; background:#f8f9fb; }
  .semi-res-card h4 { font-family:'Montserrat',sans-serif; font-size:13px; font-weight:800; color:var(--dark-navy); margin-bottom:6px; line-height:1.3; }
  .semi-res-card p { font-size:12.5px; color:var(--gray); line-height:1.65; margin-bottom:14px; }
  .semi-res-btn { display:block; width:100%; background:var(--kblue); color:var(--white); border:none; padding:9px 16px; border-radius:7px; font-weight:700; font-size:12.5px; cursor:pointer; font-family:'Montserrat',sans-serif; text-align:center; }
  .semi-stat-strip { background:var(--kblue-50); border:1px solid var(--kblue-light); padding:32px 24px; margin:28px 0; border-radius:10px; }
  .semi-stat-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:20px; text-align:center; }
  .semi-stat-num { font-family:'Montserrat',sans-serif; font-size:clamp(20px,2.8vw,36px); font-weight:800; color:var(--dark-navy); letter-spacing:-0.03em; line-height:1.1; margin-bottom:5px; }
  .semi-stat-desc { font-size:12px; color:var(--gray); line-height:1.5; }
  .semi-stat-fine { text-align:center; font-size:11px; color:var(--gray); margin-top:14px; font-style:italic; }
  .semi-inline-cta { background:var(--kblue-50); border:1.5px solid var(--kblue-light); border-radius:12px; padding:24px 28px; margin-top:32px; display:flex; justify-content:space-between; align-items:center; gap:24px; flex-wrap:wrap; }
  .semi-inline-cta h3 { font-family:'Montserrat',sans-serif; font-size:15px; font-weight:800; color:var(--dark-navy); margin-bottom:5px; }
  .semi-inline-cta p { font-size:13px; color:var(--gray); line-height:1.7; margin:0; }
  .semi-also-cards { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:20px; }
  .semi-also-card { background:rgba(255,255,255,0.09); border:1px solid rgba(255,255,255,0.15); border-radius:12px; padding:22px 24px; cursor:pointer; transition:background .18s; }
  .semi-also-card:hover { background:rgba(255,255,255,0.15); }
  .semi-also-card h3 { font-family:'Montserrat',sans-serif; font-size:14px; font-weight:800; color:var(--white); margin-bottom:7px; line-height:1.3; }
  .semi-also-card p { font-size:13px; color:rgba(255,255,255,0.72); line-height:1.72; margin-bottom:14px; }
  .semi-also-card-link { font-size:12.5px; font-weight:700; color:var(--kyellow); font-family:'Montserrat',sans-serif; }
  .semi-cross-sell { background:rgba(255,255,255,0.07); border:1px solid rgba(255,255,255,0.12); border-left:4px solid var(--kyellow); border-radius:0 10px 10px 0; padding:24px 28px; }
  .semi-cross-sell h3 { font-family:'Montserrat',sans-serif; font-size:15px; font-weight:800; color:var(--white); margin-bottom:10px; line-height:1.3; }
  .semi-cross-sell p { font-size:13.5px; color:rgba(255,255,255,0.78); line-height:1.75; margin-bottom:18px; }
  .semi-img-ph { width:100%; background:var(--kblue-light); border-radius:10px; border:1px dashed #b8c8e4; display:flex; align-items:center; justify-content:center; color:#8fa8cc; font-size:11.5px; font-family:'Montserrat',sans-serif; font-weight:700; letter-spacing:0.04em; text-align:center; }
  .semi-gallery { display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin-top:20px; }
  .semi-gallery-img { aspect-ratio:4/3; background:var(--kblue-light); border-radius:8px; border:1px dashed #b8c8e4; display:flex; align-items:center; justify-content:center; color:#8fa8cc; font-size:11px; font-family:'Montserrat',sans-serif; font-weight:700; }
  .semi-stub { display:flex; flex-direction:column; align-items:center; justify-content:center; min-height:52vh; padding:80px 56px; text-align:center; background:var(--offwhite); }
  .semi-stub h1 { font-family:'Montserrat',sans-serif; font-size:clamp(22px,2.5vw,36px); font-weight:800; color:var(--dark-navy); margin-bottom:14px; letter-spacing:-0.02em; line-height:1.2; }
  .semi-stub p { font-size:15px; color:var(--gray); line-height:1.85; max-width:480px; margin-bottom:28px; }
  @media (max-width:1024px) {
    .semi-sol-grid { grid-template-columns:repeat(2,1fr); }
    .semi-kw-grid { grid-template-columns:repeat(2,1fr); }
    .semi-pillar-grid { grid-template-columns:repeat(2,1fr); }
    .semi-stat-grid { grid-template-columns:repeat(2,1fr); }
    .semi-res-grid { grid-template-columns:repeat(2,1fr); }
  }
  @media (max-width:768px) {
    .semi-kw-section,.semi-pill-section,.semi-pillar-section,.semi-res-section { padding-left:24px; padding-right:24px; }
    .semi-sol-grid,.semi-kw-grid,.semi-pillar-grid,.semi-stat-grid,.semi-res-grid { grid-template-columns:1fr; }
    .semi-also-cards { grid-template-columns:1fr; }
    .semi-inline-cta { flex-direction:column; }
    .semi-gallery { grid-template-columns:repeat(2,1fr); }
    .semi-stub { padding:60px 24px; min-height:40vh; }
  }
"""
assert '</style>' in html, "</style> not found"
html = html.replace('</style>', NEW_CSS + '</style>', 1)
print("CSS added")

# ─────────────────────────────────────────
# SHARED FOOTER HELPER
# ─────────────────────────────────────────
def FOOTER(active_section='semi'):
    return """  <footer>
    <div class="footer-grid">
      <div><p class="footer-desc">Engineering solutions from semiconductor fabrication to final outcomes &mdash; powering possibilities across South and Southeast Asia.</p></div>
      <div class="footer-col"><h4>Solutions</h4>
        <span class="footer-link" onclick="showPage('semi')">Semiconductor &amp; Industrial</span>
        <span class="footer-link" onclick="showPage('medical')">Healthcare &amp; Medical</span>
        <span class="footer-link" onclick="showPage('personalhealth')">Personal Health</span>
        <span class="footer-link" onclick="showPage('shop')">E-Shop</span>
      </div>
      <div class="footer-col"><h4>Company</h4>
        <span class="footer-link" onclick="showPage('about')">About Us</span>
        <span class="footer-link" onclick="showPage('news')">News &amp; Events</span>
        <span class="footer-link" onclick="showPage('careers')">Careers</span>
        <span class="footer-link" onclick="showPage('partnerships')">Partner With Us</span>
      </div>
      <div class="footer-col"><h4>Connect</h4>
        <span class="footer-link" onclick="showPage('contact')">Get in Touch</span>
        <span class="footer-link" onclick="showPage('resources')">Resources</span>
        <span class="footer-link" onclick="showPage('contact')">Singapore Office</span>
        <span class="footer-link" onclick="showPage('contact')">Malaysia Office</span>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Kromax South Asia Pte. Ltd. All rights reserved.</p>
      <div class="footer-bottom-links">
        <span class="footer-link" style="margin:0">Privacy Policy</span>
        <span class="footer-link" style="margin:0">Cookie Policy</span>
      </div>
    </div>
  </footer>"""

# ─────────────────────────────────────────
# 4. PAGE-SEMI (FULL LANDING PAGE)
# ─────────────────────────────────────────
PAGE_SEMI = """<div id="page-semi" class="page">
  <div class="med-sub-hero" style="background:url('https://images.unsplash.com/photo-1518770660439-4636190af475?w=1400&q=85') center/cover no-repeat">
    <div class="med-sub-hero-overlay"></div>
    <div class="med-sub-hero-content">
      <div class="breadcrumb" onclick="showPage('industries')">&#8592; Our Solutions</div>
      <div style="font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.55);font-family:'Syne',sans-serif;margin-bottom:14px">Semiconductor &amp; Industrial Solutions</div>
      <h1 style="font-family:'Montserrat',sans-serif;font-size:clamp(28px,4vw,54px);font-weight:800;color:var(--white);line-height:1.1;letter-spacing:-0.025em;margin-bottom:20px;max-width:740px">The team that knows your process.</h1>
      <p style="color:rgba(255,255,255,0.75);font-size:15.5px;line-height:1.85;max-width:640px;margin-bottom:30px">From semiconductor fabrication facilities to pharmaceutical cleanrooms, food processing plants and industrial operations across Southeast Asia &mdash; Kromax South Asia partners with facilities managers, process engineers and procurement teams who need more than a supplier. With over 22 years in the semiconductor and industrial sectors, we bring deep engineering expertise across energy management, predictive monitoring, heating solutions, fabrication equipment, gas and chemical systems, and parts support. When something critical is at stake, we&rsquo;re the team you call.</p>
      <button class="btn-primary" onclick="document.getElementById('semi-solutions').scrollIntoView({behavior:'smooth'})">Explore Our Solutions &#8595;</button>
    </div>
  </div>

  <!-- S3A: OUR SOLUTIONS (6 cards) -->
  <section class="section" id="semi-solutions">
    <div class="section-inner">
      <div class="sec-label">Our Solutions</div>
      <h2 class="sec-title">Our Solutions</h2>
      <p style="font-size:15px;color:var(--gray);line-height:1.8;max-width:720px;margin-bottom:8px">We organise our Semiconductor and Industrial portfolio into six solution areas &mdash; each supported by our engineering specialists, system integration expertise and on-site field service. Explore by category or scroll down to find your specific application area.</p>
      <div class="semi-sol-grid">
        <div class="semi-sol-card" onclick="showPage('semi-energy')">
          <div class="semi-sol-icon">&#9889;</div>
          <h3>Energy Management &amp; Sustainability</h3>
          <p>AI-driven chiller optimisation, equipment-level energy monitoring, solar generation and power efficiency solutions for semiconductor fabs and industrial facilities.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
        <div class="semi-sol-card" onclick="showPage('semi-predictive')">
          <div class="semi-sol-icon">&#128225;</div>
          <h3>Predictive Equipment Health &amp; Monitoring</h3>
          <p>Patented smart sensors and wireless condition monitoring for vacuum pumps, diffusion furnaces and critical fab equipment &mdash; catch failures before they happen.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
        <div class="semi-sol-card" onclick="showPage('semi-heating')">
          <div class="semi-sol-icon">&#128293;</div>
          <h3>Industrial Heating Solutions</h3>
          <p>Custom heating jackets, thermal insulation and multi-zone temperature control systems for OEM equipment, process piping and specialty industrial applications.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
        <div class="semi-sol-card" onclick="showPage('semi-fab')">
          <div class="semi-sol-icon">&#128300;</div>
          <h3>Fabrication &amp; Inspection Equipment</h3>
          <p>Wafer inspection, horizontal furnace systems, bonding and de-bonding, and high-precision capillary printing for front-end and advanced packaging processes.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
        <div class="semi-sol-card" onclick="showPage('semi-gas')">
          <div class="semi-sol-icon">&#128299;</div>
          <h3>Gas, Chemical &amp; Wet Process Solutions</h3>
          <p>Real-time chemical concentration analysis, specialty gas equipment, industrial scrubbers and wet process chemical supply for semiconductor and cleanroom environments.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
        <div class="semi-sol-card" onclick="showPage('semi-parts')">
          <div class="semi-sol-icon">&#128295;</div>
          <h3>Parts, Maintenance &amp; Consumables</h3>
          <p>Genuine sealing solutions, custom fabrication materials, fittings, cleanroom components and circuit board diagnostics &mdash; across all product lines with responsive reorder support.</p>
          <div class="semi-sol-link">Learn More &#8594;</div>
        </div>
      </div>
    </div>
  </section>

  <!-- S3B: EXPLORE BY INDUSTRIAL NEED (8 compact cards) -->
  <div class="semi-kw-section">
    <div style="max-width:1180px;margin:0 auto">
      <div class="sec-label">Explore by Industrial Need</div>
      <h2 class="sec-title" style="margin-bottom:6px">Explore by Industrial Need</h2>
      <p style="font-size:14px;color:var(--gray);margin-bottom:0">Looking for a specific application or process challenge? Browse directly by industrial need.</p>
      <div class="semi-kw-grid">
        <div class="semi-kw-card" onclick="showPage('semi-energy')">
          <h4>AI Chiller &amp; HVAC Optimisation</h4>
          <p>Cut energy costs in semiconductor fabs and industrial facilities with AI-driven chiller control.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-energy')">
          <h4>Equipment Energy Monitoring &amp; ESG Compliance</h4>
          <p>Real-time machine-level energy visibility with built-in ISO&nbsp;50001 and SEMI&nbsp;S23 compliance.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-predictive')">
          <h4>Predictive Maintenance &amp; Smart Sensors</h4>
          <p>Prevent unplanned downtime with patented smart sensors for critical fab equipment.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-heating')">
          <h4>Custom Heating &amp; Thermal Insulation</h4>
          <p>Precision heating jackets and temperature control systems for OEM and process equipment.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-fab')">
          <h4>Wafer Inspection &amp; Defect Detection</h4>
          <p>Surface and macro inspection systems for unpatterned and patterned wafers, front-end processes.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-fab')">
          <h4>Advanced Packaging &amp; Bonding</h4>
          <p>Wafer bonding, de-bonding and high-precision printing for advanced packaging applications.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-gas')">
          <h4>Gas Safety &amp; Scrubber Systems</h4>
          <p>Turnkey specialty gas equipment, industrial scrubbers and abatement for fab and chemical facilities.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
        <div class="semi-kw-card" onclick="showPage('semi-gas')">
          <h4>Wet Process Chemical Analysis</h4>
          <p>Real-time concentration monitoring for SC-1, SC-2, HF and other wet process chemistries.</p>
          <div class="semi-kw-link">Learn More &#8594;</div>
        </div>
      </div>
    </div>
  </div>

  <!-- S4: INDUSTRIES & APPLICATIONS WE SERVE -->
  <div class="semi-pill-section">
    <div style="max-width:1180px;margin:0 auto">
      <div class="sec-label">Industries &amp; Applications We Serve</div>
      <h2 class="sec-title" style="margin-bottom:8px">Industries &amp; Applications We Serve</h2>
      <p style="font-size:14px;color:var(--gray)">Our solutions are deployed across a broad range of industries throughout Southeast Asia.</p>
      <div class="semi-pills">
        <span class="semi-pill">Semiconductor Fabrication</span>
        <span class="semi-pill">Pharmaceutical &amp; Cleanroom</span>
        <span class="semi-pill">Oil, Gas &amp; Energy</span>
        <span class="semi-pill">F&amp;B &amp; Palm Oil Processing</span>
        <span class="semi-pill">Solar &amp; Renewable Energy</span>
        <span class="semi-pill">Research &amp; Life Sciences</span>
        <span class="semi-pill">General Manufacturing</span>
        <span class="semi-pill">Hospitality &amp; Hotels</span>
        <span class="semi-pill">Corporate, MNC &amp; Commercial Facilities</span>
        <span class="semi-pill">MEMS, Photonics &amp; Biomedical</span>
        <span class="semi-pill">Solar Cell Manufacturing</span>
        <span class="semi-pill">Research Institutes &amp; University Labs</span>
        <span class="semi-pill">Government &amp; Statutory Boards</span>
        <span class="semi-pill test">Data Centre &amp; Facilities</span>
        <span class="semi-pill test">Flat Panel Display Manufacturing</span>
        <span class="semi-pill test">Bulk Gas &amp; Cryogenic</span>
      </div>
    </div>
  </div>

  <!-- S5: BEYOND THE EQUIPMENT -->
  <div class="semi-pillar-section">
    <div style="max-width:1180px;margin:0 auto">
      <div class="sec-label">Beyond the Equipment</div>
      <h2 class="sec-title" style="margin-bottom:6px">Beyond the Equipment</h2>
      <p style="font-size:12.5px;font-weight:700;color:var(--gray);margin-bottom:20px;font-family:'Syne',sans-serif;text-transform:uppercase;letter-spacing:0.07em">Engineering Partnership &amp; Field Support</p>
      <p style="font-size:15.5px;line-height:1.85;color:var(--gray);max-width:820px;margin-bottom:32px">Kromax South Asia has spent over 22 years embedded in semiconductor fabs and industrial operations across Southeast Asia. That depth of experience shapes everything &mdash; how we specify, how we commission, how we support and how we advise. From initial assessment through to long-term optimisation, we stay with you until the problem is fully resolved &mdash; bringing the diagnostic capability, technical analysis and solution expertise to see it through.</p>
      <div class="semi-pillar-grid">
        <div class="semi-pillar-card">
          <div class="semi-pillar-icon">&#128208;</div>
          <h3>System Design &amp; Integration</h3>
          <p>We work with your engineering team at the specification stage &mdash; collecting operational data, analysing process requirements, mapping your existing infrastructure and identifying integration points &mdash; so what goes in is configured for your facility from the start, not adjusted after the fact.</p>
        </div>
        <div class="semi-pillar-card">
          <div class="semi-pillar-icon">&#9881;&#65039;</div>
          <h3>Installation &amp; Commissioning</h3>
          <p>Our engineers manage every phase of commissioning &mdash; from pre-installation checks and phased system bring-up through to process validation and final sign-off. We stay on-site until the system is running to your process standard, not just powered on and handed over.</p>
        </div>
        <div class="semi-pillar-card">
          <div class="semi-pillar-icon">&#128202;</div>
          <h3>Predictive Diagnostics &amp; Baseline</h3>
          <p>We establish performance baselines, run diagnostic assessments and conduct data testing and benchmarking before making any recommendation. Every proposal we put forward is grounded in your actual operating conditions &mdash; measured, not assumed.</p>
        </div>
        <div class="semi-pillar-card">
          <div class="semi-pillar-icon">&#128295;</div>
          <h3>On-Site Field Service &amp; Support</h3>
          <p>Our field service team covers Singapore, Malaysia and Indonesia &mdash; on-site or remotely &mdash; for scheduled maintenance, unplanned issues and ongoing optimisation. And when you need parts, consumables or ancillary support along the way, we have it covered. One partner, one point of contact, less to manage on your end.</p>
        </div>
      </div>
      <div class="semi-cross-nudge">Already working with us on one solution? Our portfolio spans energy management, predictive monitoring, heating, fabrication, gas and chemical systems, and parts support &mdash; speak to us about what else we can cover for your facility.</div>
    </div>
  </div>

  <!-- S6: RESOURCES & DOWNLOADS -->
  <div class="semi-res-section" id="semi-resources">
    <div style="max-width:1180px;margin:0 auto">
      <div class="sec-label">Resources &amp; Downloads</div>
      <h2 class="sec-title" style="margin-bottom:8px">Resources &amp; Downloads</h2>
      <p style="font-size:14px;color:var(--gray);margin-bottom:0">Browse and download our solution brochures. Select a category below to find what&rsquo;s relevant to your facility or process.</p>
      <div class="semi-res-filters" id="semiResFilters">
        <button class="semi-res-filter active" onclick="filterSemiRes('all',this)">All</button>
        <button class="semi-res-filter" onclick="filterSemiRes('energy',this)">Energy Management</button>
        <button class="semi-res-filter" onclick="filterSemiRes('predictive',this)">Predictive Monitoring</button>
        <button class="semi-res-filter" onclick="filterSemiRes('heating',this)">Industrial Heating</button>
        <button class="semi-res-filter" onclick="filterSemiRes('fab',this)">Fabrication &amp; Inspection</button>
        <button class="semi-res-filter" onclick="filterSemiRes('gas',this)">Gas &amp; Chemical</button>
        <button class="semi-res-filter" onclick="filterSemiRes('parts',this)">Parts &amp; Consumables</button>
      </div>
      <div class="semi-res-grid" id="semiResGrid">
        <div class="semi-res-card" data-semi-cat="energy">
          <h4>AI Chiller Optimisation (OptiSave)</h4>
          <p>AI-driven chiller energy optimisation for semiconductor fabs and commercial facilities.</p>
          <button class="semi-res-btn" onclick="showGatedForm('AI Chiller Optimisation — OptiSave Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="energy">
          <h4>Equipment Energy Monitoring (iEECMS)</h4>
          <p>Real-time equipment-level energy monitoring, anomaly detection and ISO&nbsp;50001 compliance platform.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Equipment Energy Monitoring — iEECMS Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="energy">
          <h4>Intelligent Solar (SmartFlower)</h4>
          <p>All-in-one dual-axis tracking solar system for commercial and government facilities.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Intelligent Solar — SmartFlower Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="predictive">
          <h4>Predictive Equipment Health (InControl Engineering)</h4>
          <p>Smart sensor platform brochure covering HERSS, VSS and DAQSS for semiconductor and industrial equipment.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Predictive Equipment Health — InControl Engineering Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="predictive">
          <h4>Wireless Condition Monitoring (SmartTag)</h4>
          <p>Wireless sensor deployment and patented decay rate algorithm for facility-wide machine health monitoring.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Wireless Condition Monitoring — SmartTag Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="heating">
          <h4>Industrial Heating Solutions (BriskHeat)</h4>
          <p>Custom jackets, heating tapes, laboratory heating and composite curing &mdash; comprehensive product brochure.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Industrial Heating Solutions — BriskHeat Brochure')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="fab">
          <h4>Fabrication &amp; Inspection Equipment</h4>
          <p>Wafer inspection, horizontal furnace systems and bonding equipment for front-end and advanced packaging.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Fabrication & Inspection Equipment — Product Overview')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="gas">
          <h4>Gas, Chemical &amp; Wet Process Solutions</h4>
          <p>Specialty gas equipment, wet process chemical analysis and industrial scrubber systems overview.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Gas, Chemical & Wet Process — Product Overview')">Download Brochure</button>
        </div>
        <div class="semi-res-card" data-semi-cat="parts">
          <h4>Semiconductor &amp; Industrial Portfolio Overview</h4>
          <p>Complete portfolio overview covering all six solution areas and the Kromax South Asia engineering service offer.</p>
          <button class="semi-res-btn" onclick="showGatedForm('Semiconductor & Industrial — Portfolio Overview')">Download Brochure</button>
        </div>
      </div>
      <p style="margin-top:24px;font-size:13.5px;color:var(--gray)">Can&rsquo;t find what you&rsquo;re looking for? <span style="color:var(--kblue);font-weight:700;cursor:pointer" onclick="showPage('contact')">Reach out to our team directly.</span></p>
    </div>
  </div>

  <!-- S7: CTA STRIP -->
  <div class="med-cta-strip">
    <h2>Ready to explore what&rsquo;s possible for your facility?</h2>
    <p>Whether you&rsquo;re evaluating a specific solution or looking for a partner to assess your facility&rsquo;s broader needs, our team is ready to listen. No pressure, no generic pitch &mdash; just an honest conversation about what makes sense for your operation.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:10px">
      <button class="btn-primary" onclick="showPage('contact')">Get in Touch &#8594;</button>
      <button class="btn-outline-white" onclick="document.getElementById('semi-resources').scrollIntoView({behavior:'smooth'})">Download Brochures</button>
    </div>
  </div>
""" + FOOTER() + """
</div>"""

# ─────────────────────────────────────────
# 5. PAGE-SOLAR (REDIRECT)
# ─────────────────────────────────────────
PAGE_SOLAR = """<!-- ════════════════ SOLAR — RETIRED, REDIRECTS TO ENERGY MANAGEMENT -->
<div id="page-solar" class="page">
  <div class="med-sub-hero" style="background:linear-gradient(135deg,var(--dark-navy) 0%,#0a3580 100%)">
    <div class="med-sub-hero-overlay" style="background:none"></div>
    <div class="med-sub-hero-content" style="text-align:center;max-width:620px;margin:0 auto">
      <div class="sec-label" style="color:rgba(255,255,255,0.5);margin-bottom:16px">Page Updated</div>
      <h1 style="font-family:'Montserrat',sans-serif;font-size:clamp(22px,3vw,40px);font-weight:800;color:var(--white);line-height:1.15;letter-spacing:-0.02em;margin-bottom:16px">Intelligent Solar &amp; Sustainability has moved.</h1>
      <p style="color:rgba(255,255,255,0.7);font-size:15.5px;line-height:1.8;margin-bottom:28px">Our solar solutions are now part of our Energy Management &amp; Sustainability portfolio. You&rsquo;ll find SmartFlower and all solar content under the Intelligent Solar tab on that page.</p>
      <button class="btn-primary" onclick="showPage('semi-energy')">Go to Energy Management &amp; Sustainability &#8594;</button>
    </div>
  </div>
""" + FOOTER() + """
</div>"""

# ─────────────────────────────────────────
# 6. L3 SHARED HELPERS
# ─────────────────────────────────────────
def stat_block(stats, fine_print=True):
    items = ''
    for num, desc in stats:
        items += f'        <div><div class="semi-stat-num">{num}</div><div class="semi-stat-desc">{desc}</div></div>\n'
    fp = '\n      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>' if fine_print else ''
    return f"""    <div class="semi-stat-strip">
      <div class="semi-stat-grid">
{items}      </div>{fp}
    </div>"""

def highlight(title, body):
    return f"""          <div class="med-highlight-item">
            <h4>{title}</h4>
            <p>{body}</p>
          </div>"""

def img_ph(label, height=220):
    return f'    <div class="semi-img-ph" style="height:{height}px;margin-bottom:24px">[ {label} ]</div>'

def inline_cta(h, p, btn_label, gate_title):
    return f"""    <div class="semi-inline-cta">
      <div><h3>{h}</h3><p>{p}</p></div>
      <div style="flex-shrink:0"><button class="btn-primary" onclick="showGatedForm('{gate_title}')">{btn_label}</button></div>
    </div>"""

def gallery(labels):
    items = ''.join(f'      <div class="semi-gallery-img">[ {l} ]</div>\n' for l in labels)
    return f'    <div class="semi-gallery">\n{items}    </div>'

def accordion(groups):
    items = ''
    for title, body in groups:
        items += f"""    <div class="med-acc-item">
      <button class="med-acc-trigger" onclick="toggleMedAcc(this)">{title} <span class="med-acc-arrow">&#9662;</span></button>
      <div class="med-acc-body"><p style="font-size:13.5px;color:var(--gray);line-height:1.8;padding:8px 0">{body}</p></div>
    </div>\n"""
    return items

def l3_footer_cta(h, p, back_page='semi-energy'):
    return f"""  <div class="med-cta-strip">
    <h2>{h}</h2>
    <p>{p}</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:10px">
      <button class="btn-primary" onclick="showPage('contact')">Get in Touch &#8594;</button>
      <button class="btn-outline-white" onclick="showPage('semi');setTimeout(function(){{document.getElementById('semi-resources').scrollIntoView({{behavior:'smooth'}})}},350)">Download Brochures</button>
    </div>
  </div>"""

def also_section(intro, cards, cross_title, cross_body):
    card_html = ''
    for title, desc, page in cards:
        card_html += f"""      <div class="semi-also-card" onclick="showPage('{page}')">
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="semi-also-card-link">Learn More &#8594;</div>
      </div>\n"""
    return f"""  <div class="med-also-section section">
    <div class="section-inner">
      <div class="sec-label" style="color:rgba(255,255,255,0.5);margin-bottom:8px">Also Relevant To</div>
      <h2 class="sec-title" style="color:var(--white);margin-bottom:14px">Frequently Evaluated Together</h2>
      <p style="color:rgba(255,255,255,0.72);font-size:15px;line-height:1.8;max-width:680px;margin-bottom:28px">{intro}</p>
      <div class="semi-also-cards">
{card_html}      </div>
      <div class="semi-cross-sell">
        <h3>{cross_title}</h3>
        <p>{cross_body}</p>
        <button class="btn-primary" onclick="showPage('contact')">Talk to Our Team &#8594;</button>
      </div>
    </div>
  </div>"""

def l3_hero(page_id, bg_url, breadcrumb_label, page_label, h1, intro, footnote=''):
    fn = f'\n      <p class="med-sub-disclaimer" style="font-size:11.5px">{footnote}</p>' if footnote else ''
    return f"""<div id="{page_id}" class="page">
  <div class="med-sub-hero" style="background:url('{bg_url}') center/cover no-repeat">
    <div class="med-sub-hero-overlay"></div>
    <div class="med-sub-hero-content">
      <div class="breadcrumb" onclick="showPage('semi')">&#8592; {breadcrumb_label}</div>
      <div style="font-size:12px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:rgba(255,255,255,0.55);font-family:'Syne',sans-serif;margin-bottom:14px">{page_label}</div>
      <h1 style="font-family:'Montserrat',sans-serif;font-size:clamp(26px,3.6vw,50px);font-weight:800;color:var(--white);line-height:1.1;letter-spacing:-0.025em;margin-bottom:18px;max-width:700px">{h1}</h1>
      <p style="color:rgba(255,255,255,0.75);font-size:15.5px;line-height:1.85;max-width:640px;margin-bottom:26px">{intro}</p>{fn}
      <button class="btn-primary" onclick="document.querySelector('#{page_id} .med-cat-tab-bar').scrollIntoView({{behavior:'smooth'}})">Explore Our Solutions &#8595;</button>
    </div>
  </div>"""

def key_advantages(headline, cards):
    card_html = ''
    for icon, title, body in cards:
        card_html += f"""        <div class="med-adv-card">
          <div class="med-adv-icon">{icon}</div>
          <h3>{title}</h3>
          <p>{body}</p>
        </div>\n"""
    return f"""  <div class="med-adv-section section">
    <div class="section-inner">
      <div class="sec-label">Key Advantages</div>
      <h2 class="sec-title">{headline}</h2>
      <div class="med-adv-grid" style="margin-top:28px">
{card_html}      </div>
    </div>
  </div>"""

def tab_bar(page_id, tabs):
    items = ''
    for i, (label, tid) in enumerate(tabs):
        cls = 'med-cat-tab act' if i == 0 else 'med-cat-tab'
        items += f'        <div class="{cls}" onclick="medTabClick(this,\'{tid}\')">{label}</div>\n'
    return f"""  <div class="med-tab-bar-wrap">
    <div class="med-cat-tab-bar">
      <div class="med-tab-inner">
{items}      </div>
    </div>
  </div>"""

def tab_section(tab_id, active, content):
    cls = 'med-product-section act' if active else 'med-product-section'
    return f"""  <div class="{cls}" id="{tab_id}">
    <div class="section-inner">
{content}    </div>
  </div>"""

def section_h2(text):
    return f'    <h2 style="font-family:\'Montserrat\',sans-serif;font-size:clamp(20px,2.4vw,30px);font-weight:800;color:var(--dark-navy);letter-spacing:-0.02em;margin-bottom:14px;line-height:1.2">{text}</h2>'

def section_intro(text, max_width=760):
    return f'    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:{max_width}px;margin-bottom:24px">{text}</p>'

def highlights_grid(h1, b1, h2, b2):
    return f"""    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:28px">
{highlight(h1, b1)}
{highlight(h2, b2)}
    </div>"""

def capability_stmt(text):
    return f'    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">{text}</p>'


# ─────────────────────────────────────────
# 7. PAGE-SEMI-ENERGY (4 tabs)
# ─────────────────────────────────────────

# Tab 1: AI Chiller Optimisation
tab1_content = (
    img_ph('AI Chiller Optimisation — Section Image') + '\n' +
    section_h2('AI Chiller Optimisation') + '\n' +
    section_intro('Chiller systems typically account for 30 to 40 percent of a facility’s total energy consumption. OptiSave applies adaptive AI algorithms to your existing chiller infrastructure — integrating with your SCADA, BMS, DDC and PLC controls to reduce energy use without replacing equipment or interrupting operations.') +
    highlights_grid(
        'No Replacement. No Downtime.',
        'OptiSave is a software retrofit. It integrates directly with your existing chiller plant controls — no new chillers, no power interruption, no production stoppage. Deployment is completed within days, with a structured POC to validate projected savings before full rollout.',
        'Continuously Learning, Continuously Optimising.',
        'OptiSave controls over 100 parameters across chillers, cooling towers, AHUs and MAUs in real time — adjusting dynamically to weather conditions, occupancy patterns and production load to maintain optimal chiller plant efficiency at all times.'
    ) +
    stat_block([('Up to 30%','Energy savings, software optimisation only'),('Up to 65%','Energy savings, full system renewal'),('0.48 kW/RT','Target chiller plant efficiency'),('1–3 years','Typical payback period')]) + '\n' +
    img_ph('OptiSave — Product Video Thumbnail (click to play)', 180) + '\n' +
    capability_stmt('OptiSave delivers measurable chiller energy reduction through AI-driven optimisation of your existing variable frequency drives, chilled water temperatures, pump speeds and cooling tower operations — without modifying your current infrastructure. For facilities requiring deeper savings, integrated hardware renewal options combining variable frequency chillers, pumps and cooling towers with OptiSave software are available. Proven across semiconductor fabs, pharmaceutical cleanrooms, hospitality facilities and commercial campuses throughout Asia Pacific.') + '\n' +
    gallery(['OptiSave Installation — Chiller Plant','Dashboard Display','Facility Monitoring Context']) + '\n' +
    inline_cta('See Real Facility Results','We have documented energy savings from deployments across semiconductor fabs, commercial buildings and hospitality facilities throughout the region. Download a case study relevant to your industry.','Download Case Study','AI Chiller Optimisation — OptiSave Case Study')
)

# Tab 2: Equipment Energy Monitoring (accordion)
acc2 = accordion([
    ('Smart Hook Meters','Non-contact wireless energy meters for three-phase and single-phase circuits. Rogowski coil design measures voltage, current, power factor, harmonics and kWh simultaneously. Self-charging — no external power required. Accuracy within plus or minus 3 percent. Suitable for semiconductor cleanrooms, industrial panels and commercial electrical distribution boards.'),
    ('Sensors and Accessories','Complementary wireless sensors for temperature, humidity and DC current monitoring — extending facility visibility beyond power consumption to environmental and equipment condition parameters. Battery-powered, BLE transmission, compatible with the iEECMS platform.'),
    ('Gateway and Platform','BLE-to-WiFi and BLE-to-Ethernet gateways connect field devices to our cloud monitoring platform. Supports RS-485 integration with existing SCADA and BMS systems, third-party smart meters, flow meters and chiller controls. Real-time dashboards accessible on desktop, tablet and mobile.')
])
tab2_content = (
    img_ph('Equipment Energy Monitoring — Section Image') + '\n' +
    section_h2('Equipment Energy &amp; Anomaly Monitoring') + '\n' +
    section_intro('Effective energy management starts with visibility. The iEECMS platform delivers real-time equipment-level power consumption data, carbon emission tracking and anomaly detection across your entire facility — from individual process tools to full production lines — with zero downtime installation and zero wiring modifications.') +
    highlights_grid(
        'Equipment-Level Visibility. Zero Downtime.',
        'iEECMS uses non-contact wireless smart hook meters that clip directly onto live circuits — no power interruption, no rewiring, no production stoppage. Data is transmitted wirelessly to the cloud platform, giving your engineering team full facility visibility within days of deployment.',
        'From ISO 50001 to Carbon Auditing in One Platform.',
        'Our specially designed cloud platform consolidates real-time energy consumption, equipment anomaly alerts, carbon emission calculations and ESG reporting data — helping facilities meet ISO 50001, SEMI S23 and EU CBAM disclosure requirements from a single dashboard.'
    ) +
    stat_block([('Level 5','Sub-system energy footprint measurement — industry first'),('Zero','Downtime required for installation'),('Real-time','Equipment anomaly detection and alerts'),('ISO 50001','Energy management compliance ready')], fine_print=False) + '\n' +
    img_ph('iEECMS — Product Video Thumbnail (click to play)', 180) + '\n' +
    capability_stmt('iEECMS captures granular power consumption data at equipment, sub-system and facility level — enabling process power optimisation, demand contract management, equipment aging diagnostics and utilisation rate analysis. Applicable across semiconductor cleanrooms, pharmaceutical facilities, F&amp;B processing plants, commercial campuses and data centres. Developed and proven in world-class semiconductor fabrication environments across Asia Pacific.') + '\n' +
    '    <div style="margin-top:24px">\n' + acc2 + '    </div>\n' +
    gallery(['iEECMS Meter Installation','Platform Dashboard on Screen','Facility Monitoring Environment']) + '\n' +
    inline_cta("Want to See Your Facility's Energy Footprint?",'We have documented iEECMS deployments across semiconductor fabs and industrial facilities in the region. Download a case study or speak to our team about a site assessment.','Download Case Study','Equipment Energy Monitoring — iEECMS Case Study')
)

# Tab 3: Intelligent Solar (SmartFlower)
tab3_content = (
    img_ph('SmartFlower — Installed in Commercial Context') + '\n' +
    section_h2('Intelligent Solar') + '\n' +
    section_intro('SmartFlower is the world’s first all-in-one solar system — Austrian-engineered, award-winning, and built around a single principle: capture every last ray of sunlight. For organisations at the forefront of renewable energy adoption, it is as much a visible commitment as it is a power source.') +
    highlights_grid(
        'Tracks the Sun. Automatically.',
        'SmartFlower’s dual-axis tracking system follows the sun from sunrise to sunset — maintaining the optimal 90-degree angle throughout the day. This delivers up to 40 percent more energy output per square metre compared to conventional fixed-panel solar installations.',
        'Fully Autonomous. Minimal Maintenance.',
        'SmartFlower self-cleans twice daily, continuously monitors wind speeds and folds automatically into a protected position when conditions require it. Self-ventilated panel design contributes up to an additional 10 percent efficiency gain through natural cooling.'
    ) +
    stat_block([('Up to 40%','More energy output than conventional fixed solar'),('2,000+','Installations worldwide'),('Red Dot','Design Award Winner'),('SEA Award','Sustainable Entrepreneurship Award')], fine_print=True) + '\n' +
    img_ph('SmartFlower — Product Video Thumbnail (click to play)', 180) + '\n' +
    capability_stmt('Backed by over 160 patents and more than a decade of refinement, SmartFlower generates clean renewable energy across commercial campuses, government facilities, hospitality properties and industrial sites. Factory assembled and tested, it installs in hours with no complex civil works — compatible with battery storage integration and EV charging infrastructure. Recipient of the Red Dot Design Award, the Green Good Design Award, the SEA Sustainable Entrepreneurship Award and the Austria Born Global Champions Award.') + '\n' +
    gallery(['SmartFlower — Open Tracking','SmartFlower on Commercial Campus','SmartFlower — Installation Detail']) + '\n' +
    inline_cta('Make Sustainability Visible','SmartFlower is as much a statement as it is a solar system. Speak to our team about site suitability, ROI projection and installation — we provide a free site assessment for qualified enquiries.','Request a Free Site Assessment','SmartFlower — Free Site Assessment Enquiry')
)

# Tab 4: Power Efficiency Enhancement (EFE)
tab4_content = (
    img_ph('Power Efficiency Enhancement — Electrical Distribution Context') + '\n' +
    section_h2('Power Efficiency Enhancement') + '\n' +
    section_intro('Most energy efficiency programmes focus on major equipment — chillers, motors, HVAC. The Electron Flow Enhancer works at the electrical distribution level, addressing energy loss caused by electromagnetic interference, conductor inefficiency and connection degradation — recovering power that conventional approaches overlook, with no downtime and no infrastructure changes.') +
    highlights_grid(
        'Works on What’s Already There.',
        'The Electron Flow Enhancer is applied directly to your existing electrical distribution panels, sub-distribution boards and connection points — no equipment replacement, no civil works, no operational interruption. Implementation is completed in hours.',
        'Economical Entry Point for Energy Savings.',
        'The Electron Flow Enhancer delivers measurable energy savings as a standalone measure or as a complementary layer alongside AI chiller optimisation and equipment monitoring — making it an accessible first step for facilities beginning their energy efficiency journey, or an additional gain for those already optimising.'
    ) +
    stat_block([('Up to 12%','Energy savings at distribution panel level'),('Hours','Typical implementation time'),('Zero','Downtime required'),('SGS RoHS','Certified non-toxic, non-flammable')]) + '\n' +
    img_ph('Electron Flow Enhancer — Mechanism Diagram / Explainer', 180) + '\n' +
    capability_stmt('The Electron Flow Enhancer addresses energy loss at the source — reducing electromagnetic interference, minimising resistance at connection points and improving current flow efficiency across your electrical distribution system. Two application formats are available to suit different facility configurations and energy consumption levels, with savings verified through pre and post-implementation measurement. Non-corrosive, non-toxic and non-flammable. Suitable for industrial, commercial and cleanroom environments.') + '\n' +
    inline_cta('Not Sure Where to Start?','The Electron Flow Enhancer works well as a standalone measure or alongside our broader energy optimisation portfolio. Our team can assess your facility’s distribution system and identify where efficiency gains are available — at no obligation.','Request a Facility Assessment','Electron Flow Enhancer — Facility Assessment Enquiry')
)

PAGE_SEMI_ENERGY = (
    l3_hero(
        'semi-energy',
        'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1400&q=85',
        'Semiconductor &amp; Industrial Solutions',
        'Energy Management &amp; Sustainability',
        'Smarter energy. Measurable results.',
        'Energy accounts for a significant share of operating costs in semiconductor fabs, industrial facilities and commercial operations across Southeast Asia. Kromax South Asia brings together AI-driven chiller optimisation, equipment-level energy monitoring, intelligent solar generation and power efficiency enhancement — supporting facilities teams working toward ISO 50001 compliance, carbon auditing, ESG reporting and Singapore’s Green Mark certification. Whether you are reducing consumption, qualifying for energy efficiency grants, or building toward net-zero targets, we help you find what works for your facility — and stay to make sure it does.'
    ) + '\n' +
    key_advantages(
        'Why Energy Management &amp; Sustainability?',
        [
            ('&#128200;','From Assessment to Optimisation','We baseline your facility’s energy profile before recommending anything. Every solution we propose is grounded in your actual consumption data — not assumptions.'),
            ('&#129297;','Solutions That Work Together','Our energy portfolio is designed to stack. AI chiller optimisation, equipment monitoring, solar generation and power efficiency enhancement can be deployed individually or as an integrated facility-wide energy strategy.'),
            ('&#9989;','Compliance and Reporting Ready','Every solution on this page supports ISO 50001 energy management, carbon auditing and ESG reporting requirements — helping your facility meet regulatory obligations and qualify for energy efficiency grants.'),
            ('&#127758;','Proven Across the Region','Deployed in semiconductor fabs, industrial facilities, hotels and commercial campuses across Singapore, Malaysia and the wider Asia Pacific region — with field service teams on the ground to support implementation and ongoing optimisation.')
        ]
    ) + '\n' +
    tab_bar('semi-energy', [
        ('AI Chiller Optimisation', 'tab-chiller'),
        ('Equipment Energy Monitoring', 'tab-monitoring'),
        ('Intelligent Solar', 'tab-solar'),
        ('Power Efficiency Enhancement', 'tab-efe')
    ]) + '\n' +
    tab_section('tab-chiller', True, tab1_content) + '\n' +
    tab_section('tab-monitoring', False, tab2_content) + '\n' +
    tab_section('tab-solar', False, tab3_content) + '\n' +
    tab_section('tab-efe', False, tab4_content) + '\n' +
    also_section(
        'Energy efficiency rarely stands alone. These solution areas work alongside what you have just explored — and are often deployed together as part of a broader facility optimisation programme.',
        [
            ('Predictive Equipment Health &amp; Monitoring', 'Knowing your equipment’s health status complements your energy strategy — catching anomalies before they become failures and protecting the efficiency gains you have worked to achieve.', 'semi-predictive'),
            ('Industrial Heating Solutions', 'Precise thermal management across process piping, OEM equipment and storage systems — reducing heat loss and supporting facility-wide energy performance targets.', 'semi-heating')
        ],
        'The Complete Energy Intelligence Stack',
        'OptiSave and iEECMS are designed to work together. OptiSave optimises your chiller plant consumption at system level. iEECMS monitors energy usage at individual equipment level across your entire facility. Together they give you complete visibility and control — from the chiller room to the production floor.'
    ) + '\n' +
    l3_footer_cta(
        'Ready to Build a Smarter Energy Strategy for Your Facility?',
        'Whether you are starting with a single solution or looking to build a connected energy management programme across your facility, our team is ready to assess what makes sense for your operation. No pressure, no generic pitch — just an honest conversation.'
    ) + '\n' +
    FOOTER() + '\n</div>'
)

# ─────────────────────────────────────────
# 8. PAGE-SEMI-PREDICTIVE (2 tabs)
# ─────────────────────────────────────────

# Predictive Tab 1 accordion
acc_pred = accordion([
    ('Heating Element Resistance Smart Sensor (HERSS)',
     'Designed for diffusion furnace heating elements, HERSS monitors resistance, current, voltage, power and temperature continuously across multiple zones — sampling every 100µs to detect wire aging, element sagging, SCR and SSR degradation, wiring oxidation and low voltage conditions before they cause wafer scrap or recipe failure. Compatible with ASM, Kokusai, Tokyo Electron, Tempress, SVG-Thermco, MRL, Bruce Technologies, Centrotherm, Tystar and more. Mounts inside or adjacent to the furnace. Interfaces directly with furnace control systems to trigger pre-flight recipe checks. Monitors across 5 measurement parameters, detecting 6 classified fault types. Accessible from any smartphone, tablet or computer — no additional software required.'),
    ('Vibration Smart Sensor (VSS)',
     'VSS applies real-time Fast Fourier Transform analysis to decompose complex machine vibrations into individual frequency components — monitoring each mechanical element independently rather than as a combined signal. Detects bearing wear, shaft imbalance, gear degradation, motor winding deterioration and rotor damage across dry, turbomolecular, cryogenic and scroll vacuum pumps and general rotating equipment. Auto-modelling establishes your equipment baseline with a single button press. Alerts interface directly with equipment control systems. Supports 4 sensor input types across up to 8 inputs per unit. Accessible from any smartphone, tablet or computer — no additional software required.'),
    ('Data Acquisition Smart Sensor (DAQSS)',
     'DAQSS is the flexible sensor integration platform for everything else your facility needs to monitor. With 16 or 32 analog and digital inputs per module, it connects into a single edge computing platform — processing data locally at the equipment before transmitting to your existing factory systems via Ethernet, Wi-Fi, SECS/GEM or REST API. For facilities with unique monitoring requirements beyond HERSS or VSS, DAQSS supports over 50 sensor types across 20 monitoring categories — temperature, pressure, flow, vibration, leak detection, liquid level, air quality, gas concentration, particle detection and more. Accessible from any smartphone, tablet or computer — no additional software required.')
])

pred_tab1_content = (
    img_ph('InControl Engineering — Smart Sensor Installation Context') + '\n' +
    section_h2('Realtime Predictive Equipment Health') + '\n' +
    section_intro('InControl Engineering’s smart sensor systems deliver true predictive maintenance for semiconductor fabs and critical industrial facilities. Built on edge computing architecture and patented AI algorithms, each system is customised to your equipment, commissioned to your process standard and integrated with your existing factory control infrastructure from day one.') +
    highlights_grid(
        'Sampling at 100µs — Nothing Gets Past It.',
        'InControl sensors sample current, voltage and resistance waveforms every 100µs — calculating instantaneous resistance independent of power levels. Where conventional RMS sensors fail below full power, InControl keeps monitoring accurately across every operating state, every process phase, around the clock.',
        'Fault Detection That Tells You What, Not Just When.',
        'The patented AI algorithm does more than raise an alarm — it classifies the fault. Heating wire aging, element sagging, SCR and SSR degradation, bearing wear, shaft imbalance, rotor damage — identified and labelled before they become failures, so your team knows exactly where to act.'
    ) +
    stat_block([('Up to 90%','Reduction in unscheduled downtime'),('100µs','Sampling rate — instantaneous measurement at any power level'),('Same day','Integration into existing factory control systems'),('20+','Equipment failure modes detected and classified per sensor type')]) + '\n' +
    img_ph('InControl Engineering — Product Video (click to play)', 180) + '\n' +
    capability_stmt('InControl Engineering’s smart sensor platform covers the full spectrum of critical equipment health monitoring — from diffusion furnace heating elements and vacuum pump vibration to process utilities, automation systems and facility support equipment. Each system combines high-speed edge computing with patented fault classification algorithms, integrating directly with SCADA, MES and existing factory control systems via Ethernet, Wi-Fi or SECS/GEM communication gateways. Proven across semiconductor fabs, pharmaceutical cleanrooms and industrial facilities throughout Asia Pacific.') + '\n' +
    '    <div style="margin-top:24px">\n' + acc_pred + '    </div>\n' +
    gallery(['HERSS on Diffusion Furnace','VSS on Vacuum Pump','DAQSS Module — Panel Installation']) + '\n' +
    inline_cta('See How It Performs in a Real Fab Environment','We have documented InControl Engineering deployments across semiconductor fabrication facilities in the region. Download a case study relevant to your equipment or process challenge.','Download Case Study','InControl Engineering — Predictive Equipment Health Case Study')
)

pred_tab2_content = (
    img_ph('SmartTag — Sensor on Equipment Surface') + '\n' +
    section_h2('Wireless Condition Monitoring') + '\n' +
    section_intro('SmartTag was built for facilities that move fast and need results faster. Wireless, flexible and deployable on any machine in minutes — it brings enterprise-grade condition monitoring within reach of any operation, any size, without the complexity of traditional sensor infrastructure.') +
    highlights_grid(
        'Adheres to Any Surface. Deployed in Minutes.',
        'SmartTag’s patented flexible ceramic PCB adheres directly to any machine surface — no drilling, no rewiring, no production stoppage. Where traditional sensor integration requires 15 to 18 weeks and multiple engineering teams for a single equipment model, SmartTag is operational within minutes of placement. Scale across your entire facility without a single line of custom code.',
        'Raw Data Tells You Something Is Wrong. SmartTag Tells You Which Machine and How Fast.',
        'SmartTag’s patented decay rate algorithm converts raw vibration, temperature and humidity readings into a clear machine health score — ranking equipment by rate of deterioration. Where raw data leaves your team guessing, the decay rate model makes the answer immediately apparent. Catch the machines aging fastest before they take your production line down with them.'
    ) +
    stat_block([('Minutes','From placement to live monitoring data'),('90%','Of manufacturing sites currently without predictive maintenance'),('4x','Deterioration gap detectable between healthy and degrading equipment'),('APICTA','Award-winning AI-powered machine health technology')]) + '\n' +
    img_ph('SmartTag — Decay Rate Diagram: Raw Data vs. Decay Rate Model Output (Machine A healthy, Machine B deteriorating at 4x rate)', 200) + '\n' +
    capability_stmt('SmartTag delivers wireless condition monitoring across your entire facility — from semiconductor fab equipment and production line machinery to utilities, support systems and general industrial assets. The patented decay rate algorithm continuously analyses machine health variations, surfacing deterioration trends that raw sensor data alone cannot reveal. Recognised by APICTA and backed by partnerships with AWS, NVIDIA and Qualcomm, SmartTag scales from a single critical asset to facility-wide deployment without complexity or disruption.') + '\n' +
    gallery(['SmartTag on Equipment Surface','Fog Box Edge Computing Unit','Decay Rate Dashboard']) + '\n' +
    inline_cta('See How SmartTag Reads Your Equipment Health','Speak to our team about deploying SmartTag across your facility. We assess your equipment environment and identify where wireless condition monitoring adds the most immediate value — at no obligation.','Request a Facility Assessment','SmartTag — Wireless Condition Monitoring Assessment')
)

PAGE_SEMI_PREDICTIVE = (
    l3_hero(
        'semi-predictive',
        'https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=1400&q=85',
        'Semiconductor &amp; Industrial Solutions',
        'Predictive Equipment Health &amp; Monitoring',
        'Tired of Unscheduled Downtime?',
        'Unplanned equipment failures in semiconductor fabs and industrial facilities cost more than the repair — in lost production, scrap and schedule disruption. Kromax South Asia brings together state-of-the-art smart sensor systems and wireless condition monitoring technology that sample critical equipment parameters every 100µs*, detecting early warning signs that conventional monitoring misses entirely. From diffusion furnaces and vacuum pumps to general production equipment, our solutions are configured and customised to your process environment from day one.',
        '*Sampling rate applies to InControl Engineering smart sensor systems. Results may vary based on equipment type, configuration and site conditions.'
    ) + '\n' +
    key_advantages(
        'Why Predictive Equipment Health &amp; Monitoring?',
        [
            ('&#9888;','Your Current Sensors May Be Missing the Point','Conventional RMS-based monitoring only reads accurately when equipment is running at full power. Every other operating state produces unreliable data — giving your team false confidence while early warning signs go undetected.'),
            ('&#9881;','Configured and Integrated — Not Dropped In','Every deployment starts with your equipment list, your process environment and your existing control infrastructure. What goes in is specified, customised and commissioned for your facility — with same-day integration into your existing factory systems.'),
            ('&#128202;','From Raw Data to a Clear Answer','Raw sensor data alone rarely tells you which machine needs attention and why. Our solutions apply patented AI algorithms and fault classification to translate sensor readings into actionable equipment health intelligence — so your team acts on insight, not guesswork.'),
            ('&#9654;','Deploy Without Stopping Production','Both solutions on this page install without equipment shutdowns, rewiring or production stoppages. Start with your most critical assets and scale across your facility over time — no rip and replace, no long integration projects.')
        ]
    ) + '\n' +
    tab_bar('semi-predictive', [
        ('Realtime Predictive Equipment Health', 'tab-smartsensors'),
        ('Wireless Condition Monitoring', 'tab-wireless')
    ]) + '\n' +
    tab_section('tab-smartsensors', True, pred_tab1_content) + '\n' +
    tab_section('tab-wireless', False, pred_tab2_content) + '\n' +
    also_section(
        'Predictive equipment health works best as part of a broader facility strategy. These solution areas are frequently deployed alongside condition monitoring for a more complete picture.',
        [
            ('Energy Management &amp; Sustainability', 'Understanding your equipment’s energy consumption at machine level complements your health monitoring data — anomaly detection and energy efficiency working from the same foundation.', 'semi-energy'),
            ('Industrial Heating Solutions', 'Precise thermal management across process piping and OEM equipment — where heating performance and equipment health monitoring are often evaluated together.', 'semi-heating')
        ],
        'Realtime Health and Energy Intelligence — Together',
        'InControl Engineering’s smart sensors and the iEECMS energy monitoring platform are designed to work alongside each other. Equipment health data and energy consumption data from the same assets, surfaced in the same facility management workflow — giving your engineering team a fuller picture of what is happening on the floor and why.'
    ) + '\n' +
    l3_footer_cta(
        'Ready to Stop Unscheduled Downtime in Your Facility?',
        'Whether you are monitoring critical process equipment or looking to bring condition monitoring to your broader facility, our team is ready to assess what makes sense for your operation. No pressure, no generic pitch — just an honest conversation.'
    ) + '\n' +
    FOOTER() + '\n</div>'
)

# ─────────────────────────────────────────
# 9. PAGE-SEMI-HEATING (4 tabs)
# ─────────────────────────────────────────

# Heating Tab 1 accordion
acc_heat = accordion([
    ('Custom Cloth Heating Jackets',
     'Designed for semiconductor forelines, exhaust lines, process piping, valves, chambers and OEM equipment across AMAT, Lam Research, TEL, ASM, Edwards and Ebara tool sets. Each jacket is custom-made to equipment geometry — heating element layout engineered per jacket, flanges and openings incorporated into one continuous piece. Inner liner: PTFE-coated fabric. Outer liner: aluminised glass cloth up to 204°C or PTFE-coated fabric up to 260°C. Fibreglass insulation core. Patented grounded multi-stranded heating element rated for up to 10 years. Easy installation and removal — Velcro closure, no tools required. Suitable for cleanroom environments.'),
    ('Cloth Insulation &amp; Foam Insulators',
     'Removable insulation blankets designed to work alongside custom heating jackets or as standalone thermal insulation for process piping, valves and fittings. Cloth insulators are required for FlexTrace heat wrap systems and recommended across all surface heating applications to minimise heat loss and improve energy efficiency. Foam insulator options available for lower-temperature applications. Custom sizing available to match any equipment geometry. Silver Series available for high-visibility or high-hygiene environments.'),
    ('LYNX Temperature Control System',
     'LYNX is the intelligent control platform for BriskHeat heating jacket systems — managing up to 1,024 zones across 8 strings from a single operator interface. IDLE Mode automatically lowers temperature setpoints during non-production periods, reducing energy consumption without manual intervention. Built-in data logging records current, duty cycle and temperature per jacket for performance tracking and fault diagnosis. Email alert capability eliminates the need for a separate CMS. Built-in PID safety cutoff on over-temperature detection. CMS-ready via Modbus and MQTT — integrates with existing SCADA and FDC systems across multiple fab buildings. Accessible from any device with user-configurable graphic mapping.')
])

heat_tab1_content = (
    img_ph('BriskHeat — Custom Heating Jacket on Process Piping') + '\n' +
    section_h2('Custom Heating Jackets &amp; Insulation') + '\n' +
    section_intro('Our custom cloth heating jackets and insulation solutions are built to specification — each jacket engineered with wattage calculated for its exact application, maximum heating element coverage across fittings and flanges, and construction materials selected for your process environment, temperature range and cleanliness requirements.') +
    highlights_grid(
        'The Only Maker That Designs Wattage Per Jacket.',
        'Most heating jacket manufacturers apply a standard wattage across a run. Our patented multi-stranded grounded heating element is designed individually for each jacket — delivering uniform heat distribution and eliminating the hot spots and cold zones that standard designs leave behind. Temperature variation held within ±5°C across the full jacket length.',
        'Fits Once. Performs for Up to 10 Years.',
        'Custom-made to your exact equipment geometry — including flanges, fittings and valve openings built into one continuous piece, not attached separately. PTFE-coated outer liner for cleanliness and abrasion resistance. Patented grounded element construction rated for up to 10 years of service life under continuous industrial operation.'
    ) +
    stat_block([('±5°C','Temperature uniformity across full jacket length'),('Up to 10 years','Heating element service life'),('Up to 50%*','Energy savings verified in fab environment'),('76 years','BriskHeat surface heating expertise')]) + '\n' +
    img_ph('BriskHeat — Product Video (click to play)', 180) + '\n' +
    capability_stmt('Our custom cloth heating jackets cover the full range of semiconductor and industrial heating requirements — from diffusion furnace forelines and exhaust piping to process chambers, valves, gas delivery lines and storage vessels. Available in aluminised glass cloth up to 204°C or PTFE-coated fabric up to 260°C, with fibreglass insulation options up to 700°C for extreme temperature applications. Hazardous area variants are available with ATEX, FM and CSA approvals.') + '\n' +
    '    <div style="margin-top:24px">\n' + acc_heat + '    </div>\n' +
    gallery(['Custom Jacket on Semiconductor Foreline','Flange &amp; Fitting Coverage Detail','LYNX Controller Panel']) + '\n' +
    inline_cta('See How Our Heating Systems Perform in Your Process Environment','We have documented BriskHeat deployments across semiconductor fabs and industrial facilities in the region — including verified energy savings and long-term performance data. Download a case study relevant to your equipment or application.','Download Case Study','BriskHeat — Industrial Heating Case Study')
)

heat_tab2_content = (
    img_ph('FlexTrace or XtremeFLEX — Installed on Process Piping') + '\n' +
    section_h2('Flexible Heating Tapes &amp; Wraps') + '\n' +
    section_intro('Where custom jackets are engineered for precision fit, our flexible heating tapes and wraps are built for speed, versatility and broad coverage. From semiconductor exhaust and foreline installations to process piping, valves, pumps and gas tubing — deployable quickly across a wide range of configurations without custom lead times.') +
    highlights_grid(
        'Expands Along the Pipe. Installs in Minutes.',
        'FlexTrace expandable heat wrap unrolls straight along the pipe and follows elbows, tees, valves, flanges and unistruts — snapping into position without spiral wrapping or custom fitting. Where traditional spiral wrap heaters require careful control from start to finish, FlexTrace is fully adjustable mid-installation and can be partially fitted to check coverage before completing. Removable and reusable up to 180°C.',
        'Wide Range. One Reliable Platform.',
        'XtremeFLEX silicone rubber heating tapes handle temperatures up to 218°C across pipes, valves, bearings, pumps, gas tubing and filter housings — with adjustable thermostat control, IP54 moisture and chemical resistance, and grounded and non-grounded models available. Plug-and-play design for fast deployment across varied process touchpoints.'
    ) +
    stat_block([('Up to 180°C','FlexTrace operating temperature'),('Up to 218°C','XtremeFLEX operating temperature'),('IP54','Moisture and chemical resistance rating'),('Minutes','Typical installation time per section')]) + '\n' +
    capability_stmt('Our flexible heating tape and wrap range covers semiconductor exhaust and foreline installations, process piping heat tracing, valve and fitting freeze protection, viscosity control, emergency de-icing and temperature maintenance across general industrial applications. FlexTrace is recommended where uniformity and faster installation are priorities. XtremeFLEX silicone rubber tapes are suited to higher-temperature applications and irregular surface geometries. LYNX temperature control integration available across both product lines.') + '\n' +
    gallery(['FlexTrace on Semiconductor Exhaust Line','XtremeFLEX on Valve Assembly','Installation Context']) + '\n' +
    inline_cta('Not Sure Which Heating Solution Fits Your Application?','Our team can assess your process piping layout and recommend the right heating approach — custom jacket, flexible wrap or tape — based on your temperature requirements, installation constraints and budget. No obligation.','Speak to Our Team','BriskHeat — Flexible Heating Tape &amp; Wrap Enquiry')
)

heat_tab3_content = (
    img_ph('BriskHeat Laboratory Heating — Heating Mantle in Lab Context') + '\n' +
    section_h2('Laboratory &amp; Process Heating') + '\n' +
    section_intro('Precise, controlled heating for research, analytical and process laboratory environments. Our laboratory heating range covers benchtop applications from heating mantles and beaker heaters to laboratory tapes and cords — built for the temperature accuracy and operational reliability that research and quality control workflows demand.') +
    highlights_grid(
        'Consistent Heat for Critical Bench Applications.',
        'Heating mantles and silicone rubber beaker heaters deliver uniform, controlled heat to round-bottom flasks, beakers and laboratory vessels — without direct flame or immersion. Suitable for distillation, reflux, synthesis and sample preparation across pharmaceutical, life sciences and industrial quality control laboratories.',
        'Flexible Heating for Tubing and Process Lines.',
        'Laboratory heating tapes and cords maintain temperature across tubing, small-diameter piping and process connections — preventing condensation, maintaining sample viscosity and protecting temperature-sensitive process flows in analytical and semiconductor process environments.'
    ) +
    stat_block([('Up to 450°C','Maximum exposure temperature — laboratory heating tapes'),('Up to 260°C','Silicone rubber beaker heaters'),('Cleanroom','Compatible construction materials available'),('76 years','BriskHeat surface heating expertise')]) + '\n' +
    capability_stmt('Our laboratory heating range covers heating mantles, silicone rubber beaker heaters, laboratory heating tapes and cords — serving pharmaceutical research, life sciences, semiconductor process laboratories and industrial quality control environments across Southeast Asia. All products are available through Kromax South Asia with local application support, product selection guidance and responsive reorder service for ongoing laboratory operations.') + '\n' +
    gallery(['Heating Mantle on Flask in Lab','Beaker Heater in Use','Lab Tape on Process Tubing']) + '\n' +
    inline_cta('Looking for the Right Heating Solution for Your Lab?','Our team can help identify the right product for your bench application or process line — from initial selection through to ongoing support. Speak to us directly or download our laboratory heating brochure.','Get in Touch','BriskHeat — Laboratory Heating Enquiry')
)

heat_tab4_content = (
    img_ph('BriskHeat — Composite Curing Context / ACR Hot Bonder in Use') + '\n' +
    section_h2('Composite Curing &amp; Specialty Applications') + '\n' +
    section_intro('Controlled heat application for composite repair, curing and non-destructive testing — where temperature ramp rates, hold times and uniformity across the cure zone directly determine structural integrity. Our composite curing range covers portable hot bonders, curing blankets, vacuum debulking systems and infrared NDT inspection kits.') +
    highlights_grid(
        'Portable Curing Control for Field and Facility.',
        'ACR hot bonders deliver programmable temperature ramp and soak cycles for composite repair and curing — monitoring and controlling multiple heat zones simultaneously to meet aerospace and industrial repair specifications. Portable and field-deployable, with data logging for repair traceability and quality documentation.',
        'Full Cure Cycle. Verified Results.',
        'Composite curing heating blankets deliver uniform heat across complex surface geometries — working alongside vacuum debulking tables to consolidate laminate layers and remove entrapped air before cure. Aircraft infrared NDT kits provide post-cure inspection capability, identifying subsurface defects without disassembly.'
    ) +
    stat_block([('Multi-zone','Simultaneous cure zone monitoring and control'),('Portable','Field-deployable hot bonder systems'),('Full cycle','Ramp, soak and cool — programmable per repair specification'),('NDT','Post-cure infrared inspection capability included')], fine_print=False) + '\n' +
    capability_stmt('Our composite curing range covers ACR hot bonders and controls, composite curing heating blankets, vacuum curing and debulking tables, and aircraft infrared NDT inspection kits — serving aerospace MRO, defence, marine composite and advanced manufacturing facilities across the region. Available through Kromax South Asia with application support and product selection guidance for both facility-based and field repair programmes.') + '\n' +
    gallery(['ACR Hot Bonder in Field Context','Curing Blanket on Composite Structure','Vacuum Debulking Table in Use']) + '\n' +
    inline_cta('Have a Composite Repair or Curing Requirement?','Whether you are specifying equipment for a new MRO facility or sourcing for a field repair programme, our team can identify the right configuration and support your procurement process from selection through to delivery.','Speak to Our Team','BriskHeat — Composite Curing &amp; NDT Enquiry')
)

PAGE_SEMI_HEATING = (
    l3_hero(
        'semi-heating',
        'https://images.unsplash.com/photo-1565043589221-1a6fd9ae45c7?w=1400&q=85',
        'Semiconductor &amp; Industrial Solutions',
        'Industrial Heating Solutions',
        'Precision Heat. Consistent Performance.',
        'Our custom heating systems are engineered jacket by jacket — wattage calculated per application, element coverage maximised across every fitting and flange, and performance validated to within ±5°C across the full heating length. Recognised and spec-in by AMAT, Lam Research, TEL, ASM, Edwards and Ebara. Backed by 76 years of surface heating expertise from BriskHeat.'
    ) + '\n' +
    key_advantages(
        'Why Industrial Heating Solutions?',
        [
            ('&#128295;','Engineered to Your Equipment, Not Around It','Every heating jacket is designed to your exact equipment geometry — wattage specified per application, element layout covering flanges and fittings, inner liner fitted tight. What goes on your equipment was built for it.'),
            ('&#127777;&#65039;','Uniformity You Can Measure','Our patented grounded heating element maintains temperature variation within ±5°C across the full jacket length — including flanges — delivering the process consistency that commodity heating solutions rarely achieve in practice.'),
            ('&#128737;','Built to Last, Not to Replace','With a heating element lifespan of up to 10 years and construction tested across semiconductor fabs, pharmaceutical cleanrooms and industrial operations, our heating systems are specified for durability — not just initial fit.'),
            ('&#9989;','Recognised by the OEMs That Set the Standard','Spec-in by AMAT, Lam Research, TEL, ASM, Edwards and Ebara — the equipment manufacturers whose process standards define what reliable heating looks like. Regional field service and bench test support across Singapore, Malaysia and Indonesia.')
        ]
    ) + '\n' +
    tab_bar('semi-heating', [
        ('Custom Heating Jackets &amp; Insulation', 'tab-jackets'),
        ('Flexible Heating Tapes &amp; Wraps', 'tab-tapes'),
        ('Laboratory &amp; Process Heating', 'tab-lab'),
        ('Composite Curing &amp; Specialty Applications', 'tab-curing')
    ]) + '\n' +
    tab_section('tab-jackets', True, heat_tab1_content) + '\n' +
    tab_section('tab-tapes', False, heat_tab2_content) + '\n' +
    tab_section('tab-lab', False, heat_tab3_content) + '\n' +
    tab_section('tab-curing', False, heat_tab4_content) + '\n' +
    also_section(
        'Thermal management and equipment health are often evaluated together. These solution areas are frequently specified alongside industrial heating as part of a broader facility or process optimisation programme.',
        [
            ('Predictive Equipment Health &amp; Monitoring', 'Heating element resistance monitoring and equipment health data often go hand in hand — understanding how your heating systems are performing is the first step toward preventing process failures before they occur.', 'semi-predictive'),
            ('Fabrication &amp; Inspection Equipment', 'For facilities specifying heating solutions alongside wafer processing or inspection equipment, our fabrication and inspection portfolio covers the broader process tool environment your heating systems operate within.', 'semi-fab')
        ],
        'Heating Performance and Equipment Health — Together',
        'BriskHeat custom heating jackets and InControl Engineering’s Heating Element Resistance Smart Sensor (HERSS) are a natural pairing — one delivers precise, uniform heat to your diffusion furnace elements, the other monitors those elements continuously at 100µs sampling to detect degradation before it causes wafer scrap or recipe failure. Two solutions, one complete picture of your thermal process.'
    ) + '\n' +
    l3_footer_cta(
        'Ready to Specify the Right Heating Solution for Your Process?',
        'Whether you are replacing an existing heating system, specifying for new equipment or exploring a broader thermal management programme for your facility, our team is ready to assess what works for your process. No pressure, no generic pitch — just an honest conversation.'
    ) + '\n' +
    FOOTER() + '\n</div>'
)

# ─────────────────────────────────────────
# 10. STUB PAGES (FAB, GAS, PARTS)
# ─────────────────────────────────────────
def stub_page(page_id, title, subtitle, desc, back_label='Semiconductor &amp; Industrial Solutions'):
    return f"""<div id="{page_id}" class="page">
  <div class="med-sub-hero" style="background:linear-gradient(135deg,var(--dark-navy) 0%,#112065 100%)">
    <div class="med-sub-hero-overlay" style="background:none"></div>
    <div class="med-sub-hero-content">
      <div class="breadcrumb" onclick="showPage('semi')">&#8592; {back_label}</div>
    </div>
  </div>
  <div class="semi-stub">
    <div style="font-size:12px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;color:var(--kblue);font-family:'Montserrat',sans-serif;margin-bottom:12px">Coming Soon</div>
    <h1 class="sec-title" style="font-size:clamp(22px,2.6vw,36px);margin-bottom:12px">{title}</h1>
    <p style="font-size:13.5px;font-weight:600;color:var(--kblue);font-family:'Montserrat',sans-serif;margin-bottom:16px">{subtitle}</p>
    <p style="font-size:15px;color:var(--gray);line-height:1.85;max-width:480px;margin-bottom:28px">{desc}</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
      <button class="btn-primary" onclick="showPage('contact')">Get in Touch &#8594;</button>
      <button class="btn-outline" onclick="showPage('semi')">&#8592; Back to Semiconductor &amp; Industrial</button>
    </div>
  </div>
""" + FOOTER() + '\n</div>'

PAGE_SEMI_FAB = stub_page(
    'semi-fab',
    'Fabrication &amp; Inspection Equipment',
    'Wafer Inspection — Furnace Systems — Bonding &amp; De-Bonding',
    'This page is being updated. Our fabrication and inspection portfolio covers wafer surface inspection, horizontal furnace systems and wafer bonding equipment for front-end and advanced packaging processes. Contact us to discuss your requirements.'
)

PAGE_SEMI_GAS = stub_page(
    'semi-gas',
    'Gas, Chemical &amp; Wet Process Solutions',
    'Chemical Analysis — Specialty Gas — Scrubbers &amp; Abatement',
    'This page is being updated. Our gas and chemical portfolio covers real-time wet process chemical concentration analysis, specialty gas equipment, industrial scrubbers and abatement systems for semiconductor and cleanroom environments. Contact us to discuss your requirements.'
)

PAGE_SEMI_PARTS = stub_page(
    'semi-parts',
    'Parts, Maintenance &amp; Consumables',
    'Sealing Solutions — Custom Fabrication — Fittings &amp; Diagnostics',
    'This page is being updated. Our parts and consumables portfolio covers genuine sealing solutions, custom fabrication materials, fittings, cleanroom components and circuit board diagnostics across all Semiconductor &amp; Industrial product lines. Contact us to discuss your requirements.'
)

# ─────────────────────────────────────────
# 11. ASSEMBLE ALL NEW PAGES
# ─────────────────────────────────────────
ALL_NEW_PAGES = (
    '\n' + PAGE_SEMI + '\n\n' +
    PAGE_SOLAR + '\n\n' +
    '<!-- ════════════════ ENERGY MANAGEMENT & SUSTAINABILITY -->\n' +
    PAGE_SEMI_ENERGY + '\n\n' +
    '<!-- ════════════════ PREDICTIVE EQUIPMENT HEALTH -->\n' +
    PAGE_SEMI_PREDICTIVE + '\n\n' +
    '<!-- ════════════════ INDUSTRIAL HEATING SOLUTIONS -->\n' +
    PAGE_SEMI_HEATING + '\n\n' +
    '<!-- ════════════════ FABRICATION & INSPECTION (STUB) -->\n' +
    PAGE_SEMI_FAB + '\n\n' +
    '<!-- ════════════════ GAS, CHEMICAL & WET PROCESS (STUB) -->\n' +
    PAGE_SEMI_GAS + '\n\n' +
    '<!-- ════════════════ PARTS, MAINTENANCE & CONSUMABLES (STUB) -->\n' +
    PAGE_SEMI_PARTS + '\n\n'
)

# ─────────────────────────────────────────
# 12. SPLICE INTO HTML
# ─────────────────────────────────────────
SEMI_START = '<div id="page-semi" class="page">'
CONTACT_ANCHOR = '<!-- ════════════════ CONTACT -->'

assert SEMI_START in html, f"page-semi anchor not found"
assert CONTACT_ANCHOR in html, f"CONTACT anchor not found: {CONTACT_ANCHOR!r}"

idx_start = html.index(SEMI_START)
idx_after = html.index(CONTACT_ANCHOR)

html = html[:idx_start] + ALL_NEW_PAGES + html[idx_after:]
print(f"HTML block spliced: removed old {idx_after-idx_start:,} chars, inserted {len(ALL_NEW_PAGES):,} chars")

# ─────────────────────────────────────────
# 13. JS: filterSemiRes
# ─────────────────────────────────────────
NEW_JS = """
function filterSemiRes(cat, btn) {
  document.querySelectorAll('#semiResFilters .semi-res-filter').forEach(function(b){ b.classList.remove('active'); });
  btn.classList.add('active');
  document.querySelectorAll('#semiResGrid .semi-res-card').forEach(function(card){
    card.style.display = (cat === 'all' || card.dataset.semiCat === cat) ? '' : 'none';
  });
}

"""
assert 'function toggleMedAcc(el)' in html, "toggleMedAcc not found for JS insertion"
html = html.replace('function toggleMedAcc(el)', NEW_JS + 'function toggleMedAcc(el)', 1)
print("JS added")

# ─────────────────────────────────────────
# 14. WRITE OUTPUT
# ─────────────────────────────────────────
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

new_len = len(html)
print(f"Done. {original_len:,} → {new_len:,} chars (+{new_len-original_len:,})")
print(f"Lines: {html.count(chr(10)):,}")
