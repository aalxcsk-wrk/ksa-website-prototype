#!/usr/bin/env python3
# distill_v22.py — reduce stat strips from 12 to 3, fix sec-label duplication
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

print("── Stat strip removals (keep: chiller, smartsensors, jackets) ──")

# 1. tab-monitoring — no semi-stat-fine
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Level 5</div><div class="semi-stat-desc">Sub-system energy footprint measurement — industry first</div></div>\n'
    '        <div><div class="semi-stat-num">Zero</div><div class="semi-stat-desc">Downtime required for installation</div></div>\n'
    '        <div><div class="semi-stat-num">Real-time</div><div class="semi-stat-desc">Equipment anomaly detection and alerts</div></div>\n'
    '        <div><div class="semi-stat-num">ISO 50001</div><div class="semi-stat-desc">Energy management compliance ready</div></div>\n'
    '      </div>\n'
    '    </div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ iEECMS',
    '</div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ iEECMS',
    "Remove tab-monitoring stat strip"
)

# 2. tab-solar — has semi-stat-fine
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Up to 40%</div><div class="semi-stat-desc">More energy output than conventional fixed solar</div></div>\n'
    '        <div><div class="semi-stat-num">2,000+</div><div class="semi-stat-desc">Installations worldwide</div></div>\n'
    '        <div><div class="semi-stat-num">Red Dot</div><div class="semi-stat-desc">Design Award Winner</div></div>\n'
    '        <div><div class="semi-stat-num">SEA Award</div><div class="semi-stat-desc">Sustainable Entrepreneurship Award</div></div>\n'
    '      </div>\n'
    '      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>\n'
    '    </div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ SmartFlower',
    '</div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ SmartFlower',
    "Remove tab-solar stat strip"
)

# 3. tab-efe — has semi-stat-fine
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Up to 12%</div><div class="semi-stat-desc">Energy savings at distribution panel level</div></div>\n'
    '        <div><div class="semi-stat-num">Hours</div><div class="semi-stat-desc">Typical implementation time</div></div>\n'
    '        <div><div class="semi-stat-num">Zero</div><div class="semi-stat-desc">Downtime required</div></div>\n'
    '        <div><div class="semi-stat-num">SGS RoHS</div><div class="semi-stat-desc">Certified non-toxic, non-flammable</div></div>\n'
    '      </div>\n'
    '      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>\n'
    '    </div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ Electron Flow',
    '</div>\n'
    '    <div class="semi-img-ph" style="height:180px;margin-bottom:24px">[ Electron Flow',
    "Remove tab-efe stat strip"
)

# 4. tab-wireless — has semi-stat-fine
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Minutes</div><div class="semi-stat-desc">From placement to live monitoring data</div></div>\n'
    '        <div><div class="semi-stat-num">90%</div><div class="semi-stat-desc">Of manufacturing sites currently without predictive maintenance</div></div>\n'
    '        <div><div class="semi-stat-num">4x</div><div class="semi-stat-desc">Deterioration gap detectable between healthy and degrading equipment</div></div>\n'
    '        <div><div class="semi-stat-num">APICTA</div><div class="semi-stat-desc">Award-winning AI-powered machine health technology</div></div>\n'
    '      </div>\n'
    '      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>\n'
    '    </div>\n'
    '    <div class="semi-img-ph" style="height:200px;margin-bottom:24px">[ SmartTag',
    '</div>\n'
    '    <div class="semi-img-ph" style="height:200px;margin-bottom:24px">[ SmartTag',
    "Remove tab-wireless stat strip"
)

# 5. tab-tapes — has semi-stat-fine; followed by <p style
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Up to 180°C</div><div class="semi-stat-desc">FlexTrace operating temperature</div></div>\n'
    '        <div><div class="semi-stat-num">Up to 218°C</div><div class="semi-stat-desc">XtremeFLEX operating temperature</div></div>\n'
    '        <div><div class="semi-stat-num">IP54</div><div class="semi-stat-desc">Moisture and chemical resistance rating</div></div>\n'
    '        <div><div class="semi-stat-num">Minutes</div><div class="semi-stat-desc">Typical installation time per section</div></div>\n'
    '      </div>\n'
    '      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>\n'
    '    </div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our flexible heating tape',
    '</div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our flexible heating tape',
    "Remove tab-tapes stat strip"
)

# 6. tab-lab — has semi-stat-fine; followed by <p style
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Up to 450°C</div><div class="semi-stat-desc">Maximum exposure temperature — laboratory heating tapes</div></div>\n'
    '        <div><div class="semi-stat-num">Up to 260°C</div><div class="semi-stat-desc">Silicone rubber beaker heaters</div></div>\n'
    '        <div><div class="semi-stat-num">Cleanroom</div><div class="semi-stat-desc">Compatible construction materials available</div></div>\n'
    '        <div><div class="semi-stat-num">76 years</div><div class="semi-stat-desc">BriskHeat surface heating expertise</div></div>\n'
    '      </div>\n'
    '      <p class="semi-stat-fine">Results may vary based on site conditions, equipment status and operational factors.</p>\n'
    '    </div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our laboratory heating range',
    '</div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our laboratory heating range',
    "Remove tab-lab stat strip"
)

# 7. tab-curing — no semi-stat-fine; followed by <p style
replace(
    '</div>    <div class="semi-stat-strip">\n'
    '      <div class="semi-stat-grid">\n'
    '        <div><div class="semi-stat-num">Multi-zone</div><div class="semi-stat-desc">Simultaneous cure zone monitoring and control</div></div>\n'
    '        <div><div class="semi-stat-num">Portable</div><div class="semi-stat-desc">Field-deployable hot bonder systems</div></div>\n'
    '        <div><div class="semi-stat-num">Full cycle</div><div class="semi-stat-desc">Ramp, soak and cool — programmable per repair specification</div></div>\n'
    '        <div><div class="semi-stat-num">NDT</div><div class="semi-stat-desc">Post-cure infrared inspection capability included</div></div>\n'
    '      </div>\n'
    '    </div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our composite curing range',
    '</div>\n'
    '    <p style="font-size:14.5px;color:var(--gray);line-height:1.88;margin:20px 0 0;border-top:1px solid var(--border);padding-top:20px">Our composite curing range',
    "Remove tab-curing stat strip"
)

print("\n── sec-label deduplication on page-semi landing ──")

replace(
    '<div class="sec-label">Our Solutions</div>',
    '<div class="sec-label">Semiconductor &amp; Industrial</div>',
    "sec-label: 'Our Solutions' → BU context"
)

replace(
    '<div class="sec-label">Explore by Industrial Need</div>',
    '<div class="sec-label">Semiconductor &amp; Industrial</div>',
    "sec-label: 'Explore by Industrial Need' → BU context"
)

replace(
    '<div class="sec-label">Industries &amp; Applications We Serve</div>',
    '<div class="sec-label">Semiconductor &amp; Industrial</div>',
    "sec-label: 'Industries & Applications We Serve' → BU context"
)

replace(
    '<div class="sec-label">Beyond the Equipment</div>',
    '<div class="sec-label">Semiconductor &amp; Industrial</div>',
    "sec-label: 'Beyond the Equipment' → BU context"
)

replace(
    '<div class="sec-label">Resources &amp; Downloads</div>',
    '<div class="sec-label">Semiconductor &amp; Industrial</div>',
    "sec-label: 'Resources & Downloads' → BU context"
)

print("\n── Summary ──")
print(f"Changes applied: {len(changes)}")
print(f"Chars: {original_len:,} → {len(html):,} ({len(html)-original_len:+,})")

# Verify: count remaining semi-stat-strip instances
remaining = html.count('class="semi-stat-strip"')
print(f"Remaining semi-stat-strip instances: {remaining} (expected 3)")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved.")
