#!/usr/bin/env python3
"""Build the multi-page LeadSetter AI site. Run: python3 _build.py"""

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<canvas id="particles"></canvas>
<div class="orb orb-g"></div><div class="orb orb-b"></div><div class="orb orb-g2"></div>
<div class="launchbar"><span class="pulse"></span><b>LAUNCH PRICING:</b> any 3+ services <b>50% OFF</b> at checkout · FULL STACK — all 9 services — <b>$200/mo</b> · <b>$0 setup</b> · <b>14-day money-back</b> · <a href="pricing.html">pick your plan →</a></div>
<nav><div class="wrap">
  <div class="logo">LeadSetter<span>AI</span></div>
  <div style="display:flex;align-items:center;flex-wrap:wrap">
    <a class="navl{ON_HOME}" href="index.html">Home</a>
    <a class="navl{ON_PRICING}" href="pricing.html">Pricing</a>
    <a class="navl{ON_HOW}" href="how-it-works.html">How It Works</a>
    <a class="navl{ON_COMPARE}" href="compare.html">Compare</a>
    <a class="navl{ON_FAQ}" href="faq.html">FAQ</a>
    <a class="btn btn-gold cta-mini" href="pricing.html">Get 50% Off →</a>
  </div>
</div></nav>
"""

FOOT = """
<footer>
  <div class="wrap">
    <div>
      <div class="logo" style="font-size:17px">LeadSetter<span>AI</span></div>
      <div style="margin-top:10px">Mamaroneck, NY · <a href="mailto:hello@leadsetter.ai">hello@leadsetter.ai</a> · <a href="tel:+19145550123">(914) 555-0123</a></div>
    </div>
    <div>
      <a href="pricing.html">Pricing</a> · <a href="how-it-works.html">How It Works</a> · <a href="compare.html">Compare</a> · <a href="faq.html">FAQ</a> · <a href="build-log.html">Build Log</a> · <a href="research.html">Research</a>
    </div>
    <div class="comp">© 2026 LeadSetter AI · FCC-compliant: we only contact homeowners who asked to be contacted. Every plan: $0 setup, no contract, 14-day refund on plans (à la carte $20 add-ons are month-to-month). Competitor prices are public 2026 ranges — verify your own numbers before switching. Results vary by market &amp; effort.</div>
  </div>
</footer>
<script src="js/site.js"></script>
{BODY_SCRIPT}
</body>
</html>
"""

def page(fname, title, desc, body, active="", body_script=""):
    on = {("ON_" + k): (" on" if k == active else "") for k in
          ["HOME", "PRICING", "HOW", "COMPARE", "FAQ"]}
    html = HEAD.format(TITLE=title, DESC=desc, **on)
    html += body
    EMOJI2IC = {"📞": "phone", "🗺️": "map", "⭐": "star", "🎯": "target",
                "📇": "card", "⚡": "zap", "🔒": "lock", "📅": "calendar",
                "🧾": "receipt", "🛡️": "shield", "🚪": "unlock", "🗽": "compass"}
    for e, n in EMOJI2IC.items():
        html = html.replace(e, ic(n))
    html += FOOT.format(BODY_SCRIPT=body_script)
    open(fname, "w", encoding="utf-8").write(html)
    print("wrote", fname, len(html)//1024, "KB")

# ── minimal gold icon set (feather-style, stroke = currentColor) ──
SVGS = {
  "phone":    '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
  "map":      '<polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/>',
  "star":     '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
  "target":   '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
  "card":     '<rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/>',
  "zap":      '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
  "lock":     '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
  "calendar": '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
  "receipt":  '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>',
  "shield":   '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
  "unlock":   '<rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
  "compass":  '<circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/>'
}
def ic(name, size=22):
    return ('<svg class="ic" width="%d" height="%d" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            'stroke-linejoin="round">%s</svg>' % (size, size, SVGS[name]))

CTA = """
<section class="cta-final" id="cta"><div class="wrap">
  <div class="kicker reveal">Launch pricing — lock it in</div>
  <h2 class="reveal">Any 3+ services = <span class="grad">50% off.</span> Full Stack, $200.</h2>
  <p>Checkout takes 60 seconds. $0 setup, cancel anytime, 14-day money-back — if no leads land in your first two weeks, you get a full refund. You only pay the $20/lead for leads actually delivered.</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
    <a class="btn btn-gold" href="pricing.html">See Plans + Checkout →</a>
    <a class="btn btn-ghost" href="faq.html#contact">Questions? Talk to us</a>
  </div>
  <p class="trustline mono" style="color:var(--dim);margin-top:18px">LAUNCH PRICING — any 3+ services 50% OFF · Full Stack $200/mo · $0 setup · cancel anytime · <b>14-day money-back</b></p>
</div></section>
"""

# ══════════════════════════════════════════════════════════════════
# 1. HOME
# ══════════════════════════════════════════════════════════════════
home = """
<header class="hero">
  <div class="wrap">
    <div class="badge">NYC-born · done-for-you · FCC-compliant</div>
    <h1>Stop buying shared leads from Angi.<br><span class="grad">Get 20–40 exclusive leads a month.</span></h1>
    <p class="lead">Your phone rings at 7pm — it's a <b>$12,000 roof</b>. You're on a ladder, so he calls the next guy. <b>Our AI answers in 2 seconds, 24/7</b> and books the job into your calendar — while our 9-service stack keeps the calls coming: Google Maps, reviews, social, SMS, and past-customer reactivation. Every lead is <b>yours alone</b>, confirmed, and $20 each.</p>
    <div class="ctas">
      <a class="btn btn-gold" href="pricing.html">Get 50% Off — See Plans →</a>
      <a class="btn btn-ghost" href="how-it-works.html">How We Get Leads</a>
    </div>
    <div class="trustline">$20 per qualified lead · <b>$0 setup</b> · no contract · <b>14-day money-back: no leads in 2 weeks = full refund</b> · you own every lead</div>
    <div class="floaters">
      <div class="fcard fc1"><div class="n">2 SEC</div><div class="l">AI answers every call</div></div>
      <div class="fcard fc2"><div class="n">24/7</div><div class="l">weekends &amp; holidays</div></div>
      <div class="fcard fc3"><div class="n">$20</div><div class="l">per qualified lead — yours alone</div></div>
      <div class="fcard fc4"><div class="n">$200</div><div class="l">full stack, all 9 services</div></div>
    </div>
  </div>
</header>

<section class="stats reveal"><div class="wrap"><div class="stats">
  <div class="stat"><div class="v"><span class="cnt" data-to="2" data-suffix="s">0</span></div><div class="l">AI answer speed</div></div>
  <div class="stat"><div class="v"><span class="cnt" data-to="50" data-suffix="%">0</span></div><div class="l">of jobs go to whoever answers first</div></div>
  <div class="stat"><div class="v"><span class="cnt" data-to="20" data-prefix="$">0</span></div><div class="l">per qualified lead (vs $45–228 Google)</div></div>
  <div class="stat"><div class="v"><span class="cnt" data-to="9">0</span></div><div class="l">services in the Full Stack</div></div>
  <div class="stat"><div class="v">$0</div><div class="l">setup fee — cancel anytime</div></div>
  <div class="stat"><div class="v">14</div><div class="l">day money-back — no leads in 2 weeks = refund</div></div>
  <div class="stat"><div class="v">65%</div><div class="l">cheaper than Angi's $300+/mo plans</div></div>
  <div class="stat"><div class="v">24/7</div><div class="l">answered — nights, weekends, holidays</div></div>
  <div class="stat"><div class="v">50%</div><div class="l">off when you stack 3+ services</div></div>
</div></div></section>

<section class="enemy" id="enemy"><div class="wrap">
  <div class="kicker reveal">The problem</div>
  <h2 class="reveal">Right now, you're paying to lose.</h2>
  <p class="sub reveal">The lead industry runs on a game designed against you. Here's the actual math — no spin.</p>
  <div class="cards reveal">
    <div class="ecard"><div class="big red">3–8</div><h3>contractors get the same lead</h3><p>Angi/HomeAdvisor sells your "exclusive" lead to up to 8 competitors at once. You're not buying a lead — you're buying a race.</p></div>
    <div class="ecard"><div class="big red">$45–228</div><h3>per lead on Google Ads</h3><p>And NYC emergency HVAC/roofing clicks routinely clear $200. One job covers it — if you win it. Most don't.</p></div>
    <div class="ecard"><div class="big red">15–25%</div><h3>of booked jobs never show up</h3><p>No confirmation system, no reminders. Technicians burn hours on empty driveways.</p></div>
    <div class="ecard"><div class="big gold">&gt;50%</div><h3>of jobs go to the first responder</h3><p>Speed-to-lead wins. Voicemail loses. Every minute you wait, the job is being booked by someone else.</p></div>
  </div>
  <div class="verdict reveal"><b>The fix isn't more leads. It's faster, exclusive, confirmed appointments — at a price that makes the old way embarrassing.</b> That's exactly what LeadSetter AI is.</div>
</div></section>

<section id="how"><div class="wrap">
  <div class="kicker reveal">How it works</div>
  <h2 class="reveal">Three steps. Five days. Done.</h2>
  <p class="sub reveal">No software to learn. No dashboards to babysit. We build it, launch it, and run it. <a href="how-it-works.html">See exactly how we get your leads →</a></p>
  <div class="picker reveal" id="svcPicker">
    <button class="pick-arrow" id="pickPrev" aria-label="Previous service">‹</button>
    <div class="pick-pills" id="pickPills">
      <button class="pill" data-svc="ai">AI Answering</button>
      <button class="pill" data-svc="gbp">Google Maps</button>
      <button class="pill" data-svc="social">Social Media</button>
      <button class="pill" data-svc="reviews">Reviews</button>
      <button class="pill" data-svc="website">Website</button>
      <button class="pill" data-svc="sms">SMS</button>
      <button class="pill" data-svc="email">Email</button>
      <button class="pill" data-svc="citations">Listings</button>
      <button class="pill" data-svc="tracking">Call Tracking</button>
    </div>
    <button class="pick-arrow" id="pickNext" aria-label="Next service">›</button>
    <div class="pick-dots" id="pickDots"></div>
  </div>
  <div class="steps reveal" id="flowSteps">
    <div class="step"><div class="num">STEP 01</div><h3 class="fs-t1">We plug in</h3><p class="fs-p1">We point our AI at your business number, calendar, and Google profile. You approve the setup — that's your whole job.</p></div>
    <div class="step"><div class="num">STEP 02</div><h3 class="fs-t2">AI answers everything</h3><p class="fs-p2">Missed calls, after-hours calls, weekend calls, form fills — answered in ~2 seconds. Qualified, booked, confirmed by text.</p></div>
    <div class="step"><div class="num">STEP 03</div><h3 class="fs-t3">You show up and get paid</h3><p class="fs-p3">Booked appointments land in your calendar with context. You close the job. We send the ROI report.</p></div>
  </div>
</div></section>

<section id="guarantee"><div class="wrap">
  <div class="kicker reveal">Risk reversal</div>
  <h2 class="reveal">You can't lose on this deal.</h2>
  <div class="guar reveal">
    <div class="gcard"><div class="gico">🛡️</div><h3>14-day risk-free trial</h3><p>Full refund if we don't deliver booked appointments in the first two weeks. No forms, no fights.</p></div>
    <div class="gcard"><div class="gico">🎯</div><h3>Pay only for delivered leads</h3><p>The $20/lead charge exists only when a qualified lead lands. Zero delivered = zero lead fees.</p></div>
    <div class="gcard"><div class="gico">🚪</div><h3>Cancel anytime</h3><p>No contract, no exit fee. Two weeks in, if it's not printing money — walk away.</p></div>
    <div class="gcard"><div class="gico">🗽</div><h3>Local operator, direct line</h3><p>You deal with the owner — Mamaroneck, NY. No call centers, no ticket queues.</p></div>
  </div>
</div></section>
""" + CTA

page("index.html", "LeadSetter AI — Never Miss a Job Again | AI Appointment Setting for Contractors",
     "AI answers your missed calls in 2 seconds, 24/7, and books appointments. $20 per qualified lead. Full Stack — all 9 services — $200/mo. $0 setup.",
     home, active="HOME")

# ══════════════════════════════════════════════════════════════════
# 2. PRICING (with checkout)
# ══════════════════════════════════════════════════════════════════
pricing = """
<section class="page-head"><div class="wrap">
  <div class="kicker reveal">Pricing — launch window</div>
  <h1 class="reveal">Enterprise infrastructure. <span class="grad">Contractor pricing.</span></h1>
  <p class="sub reveal">Secure checkout below. Every plan: <b>$0 setup · no contract · 14-day money-back</b> (no leads in 2 weeks = full refund) — and you only pay the $20/lead for leads actually delivered.</p>
</div></section>

<section id="plans"><div class="wrap">
  <div class="rule-banner reveal">
    <div class="big">Any 3+ services → 50% OFF, applied automatically at checkout.</div>
    <p>Every service is $20–60/mo. Stack three or more and the discount applies instantly on your card. $0 setup. 14-day money-back — no leads in 2 weeks = full refund. Cancel anytime.</p>
  </div>
  <div class="tiers reveal">
    <div class="tier">
      <div class="tname">Starter Bundle</div>
      <div class="tprice">$60<small>/mo</small></div>
      <div class="was">menu $100</div>
      <div class="save">YOU SAVE $40/mo</div>
      <ul>
        <li>AI appointment setting</li>
        <li>Call tracking &amp; ROI reports</li>
        <li>Review generation</li>
        <li>+ $20 per qualified lead</li>
      </ul>
      <a class="btn btn-ghost" href="checkout.html?bundle=starter">Checkout →</a>
    </div>
    <div class="tier">
      <div class="tname">Advertising Bundle</div>
      <div class="tprice">$110<small>/mo</small></div>
      <div class="was">menu $180</div>
      <div class="save">YOU SAVE $70/mo</div>
      <ul>
        <li>AI appointment setting</li>
        <li>Social media management</li>
        <li>SMS marketing</li>
        <li>Email marketing</li>
        <li>Call tracking &amp; ROI reports</li>
        <li>+ $20 per qualified lead</li>
      </ul>
      <a class="btn btn-ghost" href="checkout.html?bundle=advertising">Checkout →</a>
    </div>
    <div class="tier">
      <div class="tname">Local Domination</div>
      <div class="tprice">$110<small>/mo</small></div>
      <div class="was">menu $180</div>
      <div class="save">YOU SAVE $70/mo</div>
      <ul>
        <li>Google Maps / GBP optimization</li>
        <li>Review generation</li>
        <li>Citations &amp; directories</li>
        <li>Website management</li>
        <li>Social media management</li>
        <li>No lead fee — rank &amp; convert</li>
      </ul>
      <a class="btn btn-ghost" href="checkout.html?bundle=domination">Checkout →</a>
    </div>
    <div class="tier hot">
      <div class="badgehot">MOST VALUE</div>
      <div class="tname">Full Stack</div>
      <div class="tprice">$200<small>/mo</small></div>
      <div class="was">menu $300</div>
      <div class="save">YOU SAVE $100/mo</div>
      <ul>
        <li>All 9 services</li>
        <li>AI appointment setting + $20/lead</li>
        <li>Everything a $2,500/mo agency does</li>
        <li>Done for you — we run it all</li>
      </ul>
      <a class="btn btn-gold" href="checkout.html?bundle=full-stack">Checkout → Everything. $200.</a>
    </div>
  </div>
  <p class="leadnote">Every plan: <b>$0 setup · no contract · 14-day money-back</b> (no leads in 2 weeks = full refund) · cancel anytime — and you only pay the $20/lead <b>for leads actually delivered</b>.</p>

  <div class="services reveal">
    <h3>À la carte — all 9 services <span style="color:var(--green);font-family:var(--mono);font-size:13px">(tap to build · add 3+ → each is 50% off)</span></h3>
    <div class="sgrid" id="svcGrid">
      <div class="svc" data-svc="ai"><span class="tick">✓</span><span class="sn">AI Appointment Setting</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo + $20/lead</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=ai">Buy</a></div>
      <div class="svc" data-svc="gbp"><span class="tick">✓</span><span class="sn">Google Maps / GBP Optimization</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=gbp">Buy</a></div>
      <div class="svc" data-svc="social"><span class="tick">✓</span><span class="sn">Social Media Management</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=social">Buy</a></div>
      <div class="svc" data-svc="reviews"><span class="tick">✓</span><span class="sn">Review Generation</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=reviews">Buy</a></div>
      <div class="svc" data-svc="website"><span class="tick">✓</span><span class="sn">Website Management</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=website">Buy</a></div>
      <div class="svc" data-svc="sms"><span class="tick">✓</span><span class="sn">SMS Marketing</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=sms">Buy</a></div>
      <div class="svc" data-svc="email"><span class="tick">✓</span><span class="sn">Email Marketing / Newsletter</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=email">Buy</a></div>
      <div class="svc" data-svc="citations"><span class="tick">✓</span><span class="sn">Listings &amp; Directories (Yelp, BBB…)</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=citations">Buy</a></div>
      <div class="svc" data-svc="tracking"><span class="tick">✓</span><span class="sn">Call Tracking &amp; ROI Reports</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small buy" href="checkout.html?service=tracking">Buy</a></div>
    </div>
    <div class="builder-out" id="builderOut" hidden>
      <div class="kicker" style="margin-top:26px">Build your own plan</div>
      <div class="b-summary">
        <div class="b-row"><span class="k">Services picked</span><span class="v" id="bList">—</span></div>
        <div class="b-row"><span class="k">Menu price</span><span class="v" id="bMenu">—</span></div>
        <div class="b-row" id="bHalfRow" hidden><span class="k">3+ services → 50% OFF</span><span class="v good" id="bHalf">—</span></div>
        <div class="b-row" id="bKindRow" hidden><span class="k">Kindness −5%</span><span class="v good" id="bKind">—</span></div>
        <div class="b-row total"><span class="k">Your monthly price</span><span class="v gold" id="bTotal">—</span></div>
        <div class="b-row"><span class="k">Estimated ROI</span><span class="v good" id="bRoi">—</span></div>
        <div class="b-badges" id="bBadges"></div>
      </div>
      <div style="margin-top:16px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a class="btn btn-gold" id="bCheckout" href="#">Checkout This Plan →</a>
        <span class="mono" style="font-size:12px;color:var(--dim);align-self:center">$0 setup · cancel anytime · 14-day money-back</span>
      </div>
    </div>
  </div>
</div></section>

<section id="math"><div class="wrap">
  <div class="kicker reveal">The no-brainer math</div>
  <h2 class="reveal">Move the slider. Do the math.</h2>
  <p class="sub reveal">Qualified appointments are worth <b>$500–$5,000</b> each. One $1,500 job covers your entire Full Stack <b>and</b> 10 leads — with change to spare.</p>
  <div class="calc">
    <div class="calc-box reveal">
      <label for="leads">Qualified leads you want / month</label>
      <input type="range" id="leads" min="5" max="50" step="5" value="30">
      <div class="range-vals"><span>5</span><span id="leadsVal">30 leads</span><span>50</span></div>
      <div class="out">
        <div class="orow total"><span class="k">💰 LeadSetter AI — Full Stack + leads</span><span class="v gold" id="outUs">—</span></div>
        <div class="orow"><span class="k">Google Ads equivalent (est. $100/lead)</span><span class="v bad" id="outGoogle">—</span></div>
        <div class="orow"><span class="k">Angi equivalent ($75/lead, shared)</span><span class="v bad" id="outAngi">—</span></div>
        <div class="orow"><span class="k">🟢 Your savings vs Google Ads</span><span class="v good" id="outSave">—</span></div>
      </div>
      <p class="note-math">Google CPL $45–228 (HVAC–roofing benchmarks, 2026). Angi ~$20–150 per shared lead. We use conservative midpoints.</p>
    </div>
    <div class="mathbits reveal">
      <div class="mbit"><div class="ico">⚡</div><div><b>Speed wins the job</b><p>&gt;50% of home-service jobs go to whoever responds first. We answer in 2 seconds — not "within 24 hours."</p></div></div>
      <div class="mbit"><div class="ico">🔒</div><div><b>Your leads are yours</b><p>Never shared, never resold. Angi sells the same lead to up to 8 competitors. We sell it to zero.</p></div></div>
      <div class="mbit"><div class="ico">📅</div><div><b>Booked ≠ shown up</b><p>15–25% of unconfirmed appointments no-show. Our AI confirms by text and re-books the gaps.</p></div></div>
      <div class="mbit"><div class="ico">🧾</div><div><b>One job pays for the month</b><p>At $20/lead, a single $1,500 repair covers 75 leads. One job covers your entire subscription.</p></div></div>
    </div>
  </div>
</div></section>
""" + CTA

page("pricing.html", "Pricing — 50% Off Bundles & Full Stack $200 | LeadSetter AI",
     "Any 3+ services 50% off at checkout. Starter $60, Advertising $110, Local Domination $110, Full Stack $200. Secure checkout, $0 setup, cancel anytime.",
     pricing, active="PRICING", body_script='<script src="js/builder.js"></script>')

# ══════════════════════════════════════════════════════════════════
# 3. HOW IT WORKS
# ══════════════════════════════════════════════════════════════════
how = """
<section class="page-head"><div class="wrap">
  <div class="kicker reveal">How it works</div>
  <h1 class="reveal">Three steps. Five days. <span class="grad">Done.</span></h1>
  <p class="sub reveal">No software to learn. No dashboards to babysit. We build it, launch it, and run it — and we only contact homeowners who already reached out.</p>
</div></section>

<section><div class="wrap">
  <div class="kicker reveal">Pick a service — see its flow</div>
  <div class="picker reveal" id="svcPicker">
    <button class="pick-arrow" id="pickPrev" aria-label="Previous service">‹</button>
    <div class="pick-pills" id="pickPills">
      <button class="pill" data-svc="ai">AI Answering</button>
      <button class="pill" data-svc="gbp">Google Maps</button>
      <button class="pill" data-svc="social">Social Media</button>
      <button class="pill" data-svc="reviews">Reviews</button>
      <button class="pill" data-svc="website">Website</button>
      <button class="pill" data-svc="sms">SMS</button>
      <button class="pill" data-svc="email">Email</button>
      <button class="pill" data-svc="citations">Listings</button>
      <button class="pill" data-svc="tracking">Call Tracking</button>
    </div>
    <button class="pick-arrow" id="pickNext" aria-label="Next service">›</button>
    <div class="pick-dots" id="pickDots"></div>
  </div>
  <div class="steps reveal" id="flowSteps">
    <div class="step"><div class="num">STEP 01</div><h3 class="fs-t1">We plug in</h3><p class="fs-p1">We point our AI at your business number, calendar, and Google profile. You approve the setup — that's your whole job.</p></div>
    <div class="step"><div class="num">STEP 02</div><h3 class="fs-t2">AI answers everything</h3><p class="fs-p2">Missed calls, after-hours calls, weekend calls, form fills — answered in ~2 seconds. Qualified, booked, confirmed by text.</p></div>
    <div class="step"><div class="num">STEP 03</div><h3 class="fs-t3">You show up and get paid</h3><p class="fs-p3">Booked appointments land in your calendar with context. You close the job. We send the ROI report.</p></div>
  </div>
</div></section>

<section id="channels"><div class="wrap">
  <div class="kicker reveal">Where your leads actually come from</div>
  <h2 class="reveal">We don't buy strangers. We capture demand you already have — and add the channels that grow it.</h2>
  <div class="channels reveal">
    <div class="chan"><div class="ico">📞</div><div><b>Missed-call capture</b><span class="pct">~50–60% of your 30 leads</span><p>You already get calls: yard signs, van wraps, Google "near me", past customers. You miss 15–25% of them. Our AI answers those in 2 seconds and books them. Leads you were already paying to generate — we stop the leak.</p></div></div>
    <div class="chan"><div class="ico">🗺️</div><div><b>Google Business Profile optimization</b><span class="pct">~20%</span><p>We tune your GBP — categories, keywords, photos, reviews — so "AC repair near me" finds you first. More inbound calls, answered by the AI, booked.</p></div></div>
    <div class="chan"><div class="ico">⭐</div><div><b>Review engine</b><span class="pct">~10%</span><p>Automated review requests after every job → a 4.8-star profile → Google ranks you higher → more calls. Compounding.</p></div></div>
    <div class="chan"><div class="ico">🎯</div><div><b>Paid ads (Google Local Services / Meta)</b><span class="pct">~10–20% when you want volume</span><p>Your ad account, your budget, we run the campaigns. Booked appointments at $20 each — vs $45–228 on Google Ads DIY.</p></div></div>
    <div class="chan"><div class="ico">📇</div><div><b>Past-customer reactivation</b><span class="pct">~5%</span><p>Your own list, with permission: "time for a seasonal tune-up." Confirmed bookings, zero cold outreach.</p></div></div>
  </div>
  <div class="verdict reveal" style="margin-top:30px"><b>The rule:</b> every homeowner we touch asked to be contacted. Missed calls, form fills, opted-in texts, your customers. That's why "answers in 2 seconds" is a promise, not a liability.</div>
</div></section>

<section id="timeline"><div class="wrap">
  <div class="kicker reveal">The first 30 days</div>
  <h2 class="reveal">What you see, week by week.</h2>
  <div class="steps reveal">
    <div class="step"><div class="num">WEEK 1</div><h3>Capture on</h3><p>AI live on your line + calendar. First booked appointments from calls you'd have missed.</p></div>
    <div class="step"><div class="num">WEEK 2</div><h3>GBP + reviews</h3><p>Profile optimized, review engine live. Inbound calls start climbing.</p></div>
    <div class="step"><div class="num">WEEK 3–4</div><h3>Volume</h3><p>Ads optional. Dashboard shows every lead, source, and booked value. Full 30-lead month in reach.</p></div>
  </div>
</div></section>
""" + CTA

page("how-it-works.html", "How It Works — 5 Ways We Get Your Leads | LeadSetter AI",
     "Three steps, five days: AI answers missed calls, books appointments, confirms by text. 5 lead channels: missed-call capture, GBP, reviews, ads, reactivation. FCC-compliant.",
     how, active="HOW")

# ══════════════════════════════════════════════════════════════════
# 4. COMPARE
# ══════════════════════════════════════════════════════════════════
compare = """
<section class="page-head"><div class="wrap">
  <div class="kicker reveal">Us vs. them</div>
  <h1 class="reveal">The honest comparison.</h1>
  <p class="sub reveal">Every number below is from public pricing and industry benchmarks — checked 2026.</p>
</div></section>

<section><div class="wrap">
  <div class="vstable reveal">
    <div style="overflow-x:auto">
    <table class="vs">
      <thead>
        <tr>
          <th>How they get you leads</th>
          <th class="us">LeadSetter AI</th>
          <th>Angi / HomeAdvisor</th>
          <th>Thumbtack</th>
          <th>Google Local Services</th>
          <th>Yelp Ads</th>
          <th>Podium / Broadly</th>
          <th>Smith.ai / Ruby</th>
          <th>Agencies</th>
          <th>DIY tools (GHL)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="feat">Your leads are <b>exclusive</b></td>
          <td class="us usrow-hl">✅ 100% — never shared</td>
          <td><span class="pill p-bad">❌ sold to 3–8</span></td>
          <td><span class="pill p-bad">❌ shared</span></td>
          <td>mostly yours</td>
          <td><span class="pill p-bad">❌ shared</span></td>
          <td>your own calls</td>
          <td>your own calls</td>
          <td>yours (if it works)</td>
          <td>your own calls</td>
        </tr>
        <tr>
          <td class="feat">Speed-to-lead</td>
          <td class="us usrow-hl">✅ ~2 seconds, 24/7</td>
          <td><span class="pill p-bad">hours</span></td>
          <td><span class="pill p-bad">hours</span></td>
          <td>fast</td>
          <td><span class="pill p-bad">hours</span></td>
          <td>instant</td>
          <td>instant</td>
          <td>depends</td>
          <td>you monitor it</td>
        </tr>
        <tr>
          <td class="feat">Cost / month</td>
          <td class="us usrow-hl">✅ $60–200 flat + $20/lead</td>
          <td><span class="pill p-bad">$300+ + $20–150/lead</span></td>
          <td><span class="pill p-bad">$15–60/lead</span></td>
          <td><span class="pill p-bad">$45–228/lead</span></td>
          <td><span class="pill p-bad">$300+/mo</span></td>
          <td><span class="pill p-mid">$300–500/mo</span></td>
          <td><span class="pill p-bad">$240–2,100/mo</span></td>
          <td><span class="pill p-bad">$500–5,000 + ad spend</span></td>
          <td><span class="pill p-mid">$97–497/mo</span></td>
        </tr>
        <tr>
          <td class="feat">Who does the work</td>
          <td class="us usrow-hl">✅ We do — done for you</td>
          <td>you chase leads</td>
          <td>you chase leads</td>
          <td>you answer calls</td>
          <td>you chase leads</td>
          <td><span class="pill p-bad">100% DIY setup</span></td>
          <td>they answer</td>
          <td>they manage</td>
          <td><span class="pill p-bad">100% DIY</span></td>
        </tr>
        <tr>
          <td class="feat">Books + confirms appointments</td>
          <td class="us usrow-hl">✅ AI books &amp; text-confirms</td>
          <td><span class="pill p-bad">no</span></td>
          <td><span class="pill p-bad">no</span></td>
          <td>no</td>
          <td><span class="pill p-bad">no</span></td>
          <td>if you build it</td>
          <td>yes</td>
          <td>maybe</td>
          <td>only if you build it</td>
        </tr>
        <tr>
          <td class="feat">Setup fee / contract</td>
          <td class="us usrow-hl">✅ $0 · cancel anytime · 14-day money-back</td>
          <td>month-to-month</td>
          <td>pay per lead</td>
          <td>pay per lead</td>
          <td>month-to-month</td>
          <td>month-to-month</td>
          <td>month-to-month</td>
          <td>contracts</td>
          <td>month-to-month</td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>
  <p class="small-print">Sources: Angi/HomeAdvisor, Thumbtack, Yelp, Smith.ai, GoHighLevel, Podium, Ruby, AnswerConnect pricing pages + Searchlight Digital &amp; Tradesmen Guild benchmarks, checked 2026-08. Individual results vary; numbers are market ranges, not guarantees.</p>
</div></section>

<section id="guarantee"><div class="wrap">
  <div class="kicker reveal">Risk reversal</div>
  <h2 class="reveal">You can't lose on this deal.</h2>
  <div class="guar reveal">
    <div class="gcard"><div class="gico">🛡️</div><h3>14-day risk-free trial</h3><p>Full refund if we don't deliver booked appointments in the first two weeks. No forms, no fights.</p></div>
    <div class="gcard"><div class="gico">🎯</div><h3>Pay only for delivered leads</h3><p>The $20/lead charge exists only when a qualified lead lands. Zero delivered = zero lead fees.</p></div>
    <div class="gcard"><div class="gico">🚪</div><h3>Cancel anytime</h3><p>No contract, no exit fee. Two weeks in, if it's not printing money — walk away.</p></div>
    <div class="gcard"><div class="gico">🗽</div><h3>Local operator, direct line</h3><p>You deal with the owner — Mamaroneck, NY. No call centers, no ticket queues.</p></div>
  </div>
</div></section>
""" + CTA

page("compare.html", "LeadSetter AI vs Angi vs DIY — Honest Comparison",
     "Exclusive leads vs shared, 2-second AI response vs hours, $60-200 flat vs $300+ per month. Full comparison table with 2026 verified pricing.",
     compare, active="COMPARE")

# ══════════════════════════════════════════════════════════════════
# 5. FAQ
# ══════════════════════════════════════════════════════════════════
faq = """
<section class="page-head"><div class="wrap">
  <div class="kicker reveal">FAQ</div>
  <h1 class="reveal">Straight answers.</h1>
</div></section>

<section><div class="wrap">
  <div class="faq reveal">
    <div class="fitem"><button class="fq">Is this legal? Won't homeowners hate an AI answering?<span class="chev">▾</span></button><div class="fa"><p>We're FCC-compliant by design: we only contact homeowners who already reached out — missed calls, form fills, opted-in texts. Homeowners don't care who picks up — they care that someone picks up in 2 seconds instead of voicemail. The AI books the appointment; you close the job.</p></div></div>
    <div class="fitem"><button class="fq">I'm not technical. Will I have to learn software?<span class="chev">▾</span></button><div class="fa"><p>Zero. We build everything — AI agent, calendar sync, texts, reporting — and launch it in about 5 days. Your only job is to approve the setup and show up for the booked appointments.</p></div></div>
    <div class="fitem"><button class="fq">Why is it so cheap compared to agencies?<span class="chev">▾</span></button><div class="fa"><p>Because we run on AI and automation instead of account-manager overhead, we operate on slimmer margins than traditional agencies — we don't need $2,500/mo to make a client profitable. We pass that saving to you: $20 per delivered lead, not per hour of "management." Cheaper for you because it costs us less to run — not because it's a temporary deal.</p></div></div>
    <div class="fitem"><button class="fq">What's the 14-day refund?<span class="chev">▾</span></button><div class="fa"><p>Every plan (Starter, Advertising, Local Domination, Full Stack, and any custom plan) comes with a 14-day refund: if we don't deliver booked appointments in your first two weeks, you get your money back — no forms, no fights. The $20 à la carte add-ons are month-to-month, so there's nothing to refund — you just cancel. That's the whole deal: $0 setup, no contract, 14-day refund, cancel anytime.</p></div></div>
    <div class="fitem"><button class="fq">What counts as a "qualified lead"?<span class="chev">▾</span></button><div class="fa"><p>A homeowner who called or submitted a request about your actual service, got qualified by the AI (real need, real contact info, ready to book), and an appointment was booked or attempted within your service area. No tire-kickers, no lead resale, no mystery data.</p></div></div>
    <div class="fitem"><button class="fq">What if I already have a receptionist?<span class="chev">▾</span></button><div class="fa"><p>Perfect — the AI is your after-hours, weekend, and overflow backup. It answers when she can't, books into the same calendar, and confirms every appointment. Contractors with receptionists typically see the biggest lift from missed-call capture.</p></div></div>
    <div class="fitem"><button class="fq">Can I start with just the AI and add services later?<span class="chev">▾</span></button><div class="fa"><p>Yes — that's the whole point. Start with the Starter bundle at $60, watch booked appointments land for two weeks, then stack the services that move your business. The 50% bundle discount applies the moment you hit three.</p></div></div>
    <div class="fitem"><button class="fq">How does checkout work?<span class="chev">▾</span></button><div class="fa"><p>Pick a plan, hit Checkout, and you'll be on a secure payment page in seconds — no sales call required. Recurring billing, cancel anytime, and you only pay the $20/lead for leads actually delivered. Prefer a human? We're one call away.</p></div></div>
  </div>
</div></section>

<section id="contact" style="margin-top:70px"><div class="wrap">
  <div class="contact-card reveal">
    <div class="kicker">Prefer to talk it through?</div>
    <div class="big">One call. Five minutes.</div>
    <p>We'll run a free missed-call audit while we're on the phone: calls missed, hours lost, estimated revenue leaked. You get the numbers whether you hire us or not.</p>
    <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
      <a class="btn btn-gold" href="pricing.html">Skip the call — see plans →</a>
      <a class="btn btn-ghost" href="tel:+19145550123">Call (914) 555-0123</a>
    </div>
    <p class="mono" style="font-size:12px;color:var(--dim);margin-top:16px">or email <a href="mailto:hello@leadsetter.ai">hello@leadsetter.ai</a></p>
  </div>
</div></section>
"""

page("faq.html", "FAQ — Straight Answers | LeadSetter AI",
     "Is it legal? Do I need to learn software? What counts as a qualified lead? Straight answers about LeadSetter AI appointment setting.",
     faq, active="FAQ")

# ══════════════════════════════════════════════════════════════════
# 6. CHECKOUT
# ══════════════════════════════════════════════════════════════════
checkout = """
<section class="page-head"><div class="wrap">
  <div class="kicker reveal">Secure checkout</div>
  <h1 class="reveal">You're <span class="grad">two taps</span> from getting this set up.</h1>
</div></section>

<section><div class="wrap">
  <div class="checkout-wrap">
    <div class="plan-card reveal" id="planCard">
      <div class="plan-name" id="planName">—</div>
      <div class="plan-price" id="planPrice">—</div>
      <div class="plan-note" id="planNote"></div>
      <ul id="planFeatures"></ul>
      <a class="btn btn-gold" id="checkoutBtn" href="#">Secure Checkout →</a>
      <div class="secure-line">🔒 256-bit encrypted · Stripe checkout · recurring, cancel anytime</div>
      <div class="fallback" id="fallback" style="display:none">
        <div>Checkout for this plan is being activated — it takes one tap from us to switch on. Meanwhile:</div>
        <div style="margin-top:14px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
          <a class="btn btn-ghost small" href="mailto:hello@leadsetter.ai?subject=Checkout%20-%20PLAN">Email to lock your discount</a>
          <a class="btn btn-ghost small" href="tel:+19145550123">Call (914) 555-0123</a>
        </div>
      </div>
      <div class="redirect-note" id="redirectNote"></div>
    </div>
    <p class="leadnote" style="margin-top:30px">Every plan: <b>$0 setup · no contract · 14-day refund · cancel anytime</b> · $20/lead only for leads actually delivered.</p>
  </div>
</div></section>
"""

page("checkout.html", "Checkout — LeadSetter AI",
     "Secure checkout for LeadSetter AI plans. Stripe-powered, $0 setup, cancel anytime.",
     checkout, active="", body_script='<script src="js/checkout.js"></script>')

print("done")
