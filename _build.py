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
<div class="launchbar"><span class="pulse"></span><b>LOCK-IN PRICING:</b> any 3+ services <b>50% OFF</b> at checkout · FULL STACK — all 9 services — <b>$200/mo</b> · <b>$0 setup</b> · <b>14-day refund</b> · <a href="pricing.html">pick your plan →</a></div>
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
    html += FOOT.format(BODY_SCRIPT=body_script)
    open(fname, "w", encoding="utf-8").write(html)
    print("wrote", fname, len(html)//1024, "KB")

CTA = """
<section class="cta-final" id="cta"><div class="wrap">
  <div class="kicker reveal">Lock it in</div>
  <h2 class="reveal">Any 3+ services = <span class="grad">50% off.</span> Full Stack, $200.</h2>
  <p>Checkout takes 60 seconds. $0 setup, cancel anytime, 14-day refund on every plan — and you only pay the $20/lead for leads actually delivered.</p>
  <div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap">
    <a class="btn btn-gold" href="pricing.html">See Plans + Checkout →</a>
    <a class="btn btn-ghost" href="faq.html#contact">Questions? Talk to us</a>
  </div>
  <p class="trustline mono" style="color:var(--dim);margin-top:18px">$0 setup · cancel anytime · <b>14-day refund</b> · any 3+ services 50% OFF · Full Stack $200/mo</p>
</div></section>
"""

# ══════════════════════════════════════════════════════════════════
# 1. HOME
# ══════════════════════════════════════════════════════════════════
home = """
<header class="hero">
  <div class="wrap">
    <div class="badge">⚡ NYC-born · done-for-you · FCC-compliant</div>
    <h1>Stop buying shared leads from Angi.<br><span class="grad">Never miss a call again.</span></h1>
    <p class="lead">Your phone rings at 7pm — it's a <b>$12,000 roof</b>. You don't answer, so he calls the next guy. <b>Our AI answers in 2 seconds, 24/7</b>, and books the job into your calendar before your competitor even sees the notification.</p>
    <div class="ctas">
      <a class="btn btn-gold" href="pricing.html">Get 50% Off — See Plans →</a>
      <a class="btn btn-ghost" href="how-it-works.html">How We Get Leads</a>
    </div>
    <div class="trustline">$20 per qualified lead · <b>$0 setup</b> · no contract · <b>14-day refund</b> · you own every lead</div>
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
  <div class="stat"><div class="v">14</div><div class="l">day refund — no forms, no fights</div></div>
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
  <div class="kicker reveal">Pricing — built lean, priced fair</div>
  <h1 class="reveal">Enterprise-level features. <span class="grad">Contractor-sized prices.</span></h1>
  <p class="sub reveal">Secure checkout below. Every plan: <b>$0 setup · no contract · 14-day refund · cancel anytime</b> — you only pay the $20/lead for leads actually delivered.</p>
</div></section>

<section id="plans"><div class="wrap">
  <div class="rule-banner reveal">
    <div class="big">Any 3+ services → 50% OFF, applied automatically at checkout.</div>
    <p>Every service is $20–60/mo. Stack three or more and the discount applies instantly on your card. $0 setup. 14-day refund on plans. Cancel anytime.</p>
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
  <p class="leadnote">Every plan: <b>$0 setup · no contract · 14-day refund · cancel anytime</b> — and you only pay the $20/lead <b>for leads actually delivered</b>.</p>

  <div class="services reveal">
    <h3>À la carte — all 9 services <span style="color:var(--green);font-family:var(--mono);font-size:13px">(add 3+ → each is 50% off)</span></h3>
    <div class="sgrid">
      <div class="svc"><span class="sn">AI Appointment Setting</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo + $20/lead</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=ai">Buy</a></div>
      <div class="svc"><span class="sn">Google Maps Optimization</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=gbp">Buy</a></div>
      <div class="svc"><span class="sn">Social Media Management</span><div class="sprice"><span class="sp"><s class="wasprice">$80</s> $60/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=social">Buy</a></div>
      <div class="svc"><span class="sn">Review Generation</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=reviews">Buy</a></div>
      <div class="svc"><span class="sn">Website Management</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=website">Buy</a></div>
      <div class="svc"><span class="sn">SMS Marketing</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=sms">Buy</a></div>
      <div class="svc"><span class="sn">Email Marketing / Newsletter</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=email">Buy</a></div>
      <div class="svc"><span class="sn">Listings &amp; Directories (Yelp, BBB…)</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=citations">Buy</a></div>
      <div class="svc"><span class="sn">Call Tracking &amp; ROI Reports</span><div class="sprice"><span class="sp">$20/mo</span><span class="off">50% OFF at 3+</span></div><a class="btn btn-ghost small" href="checkout.html?service=tracking">Buy</a></div>
    </div>
  </div>

  <div class="builder reveal" id="builder">
    <div class="kicker">Build your own plan</div>
    <h3>Tap the services you want. <span class="grad">We do the math.</span></h3>
    <p class="sub" style="margin-top:6px">Stack 3+ and every service drops 50% — then combo discounts stack on top. Total, savings, and projected ROI update as you tap.</p>
    <div class="builder-grid" id="builderGrid"></div>
    <div class="builder-out" id="builderOut" hidden>
      <div class="b-summary">
        <div class="b-row"><span class="k">Services picked</span><span class="v" id="bList">—</span></div>
        <div class="b-row"><span class="k">Menu price</span><span class="v" id="bMenu">—</span></div>
        <div class="b-row" id="bHalfRow" hidden><span class="k">3+ services → 50% OFF</span><span class="v good" id="bHalf">—</span></div>
        <div class="b-row" id="bComboRow" hidden><span class="k">Combo discounts</span><span class="v good" id="bCombo">—</span></div>
        <div class="b-row total"><span class="k">Your monthly price</span><span class="v gold" id="bTotal">—</span></div>
        <div class="b-row"><span class="k">Estimated ROI</span><span class="v good" id="bRoi">—</span></div>
        <div class="b-badges" id="bBadges"></div>
      </div>
      <div style="margin-top:16px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
        <a class="btn btn-gold" id="bCheckout" href="#">Checkout This Plan →</a>
        <span class="mono" style="font-size:12px;color:var(--dim);align-self:center">$0 setup · cancel anytime · 14-day refund</span>
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
    <table class="vs">
      <thead>
        <tr>
          <th>What matters</th>
          <th class="us">LeadSetter AI</th>
          <th>Angi / Thumbtack</th>
          <th>DIY AI tools (GHL, etc.)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="feat">Your leads are <b>exclusive</b></td>
          <td class="us usrow-hl">✅ 100% — never shared</td>
          <td><span class="pill p-bad">❌ sold to 3–8 at once</span></td>
          <td>n/a</td>
        </tr>
        <tr>
          <td class="feat">Speed-to-lead</td>
          <td class="us usrow-hl">✅ ~2 seconds, 24/7</td>
          <td><span class="pill p-bad">hours / manual</span></td>
          <td><span class="pill p-mid">you build &amp; monitor it</span></td>
        </tr>
        <tr>
          <td class="feat">Cost / month</td>
          <td class="us usrow-hl">✅ $60–200 flat</td>
          <td><span class="pill p-bad">$300+ + $20–150/lead</span></td>
          <td><span class="pill p-mid">$97–497 + usage</span></td>
        </tr>
        <tr>
          <td class="feat">Who does the work</td>
          <td class="us usrow-hl">✅ We do — done for you</td>
          <td>you chase leads</td>
          <td><span class="pill p-bad">100% DIY setup</span></td>
        </tr>
        <tr>
          <td class="feat">Books + confirms appointments</td>
          <td class="us usrow-hl">✅ AI books &amp; text-confirms</td>
          <td><span class="pill p-bad">no</span></td>
          <td>only if you build it</td>
        </tr>
        <tr>
          <td class="feat">Setup fee / contract</td>
          <td class="us usrow-hl">✅ $0 · cancel anytime</td>
          <td>month-to-month</td>
          <td>month-to-month</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="small-print">Sources: Angi/HomeAdvisor, Thumbtack, Yelp, Smith.ai, GoHighLevel, Podium, Ruby, AnswerConnect pricing pages + Searchlight Digital &amp; Tradesmen Guild benchmarks, checked 2026-08. Individual results vary; numbers are market ranges, not guarantees.</p>
  <div class="rest-table reveal" style="margin-top:34px">
    <h3>The rest of the market, in one glance</h3>
    <div class="vstable" style="margin-top:14px">
    <table class="vs">
      <thead><tr><th>Competitor</th><th>What you get</th><th>Their cost</th><th>Why we win</th></tr></thead>
      <tbody>
        <tr><td class="feat">Yelp Ads</td><td>Paid placement above reviews; leads shared across advertisers</td><td><span class="pill p-bad">$300+/mo</span></td><td class="us usrow-hl">Exclusive leads, $60–200 flat, AI answers</td></tr>
        <tr><td class="feat">Google Local Services</td><td>"Google Guaranteed" badge calls from search</td><td><span class="pill p-bad">$45–228/lead</span></td><td class="us usrow-hl">$20 per lead — 2–4x cheaper</td></tr>
        <tr><td class="feat">Podium / Broadly</td><td>Self-serve software that replies to your missed calls &amp; texts</td><td><span class="pill p-bad">$300–500/mo</span></td><td class="us usrow-hl">Done for you — we build it, run it</td></tr>
        <tr><td class="feat">Smith.ai / Ruby</td><td>Human receptionists answer your forwarded calls</td><td><span class="pill p-bad">$240–2,100/mo</span></td><td class="us usrow-hl">AI answers 24/7 for $60–200 flat</td></tr>
        <tr><td class="feat">Marketing agencies</td><td>Monthly retainer, they run ads + SEO for you</td><td><span class="pill p-bad">$500–5,000/mo + ad spend</span></td><td class="us usrow-hl">Same work, slimmer margins, $200 Full Stack</td></tr>
        <tr><td class="feat">DIY tools (GHL, etc.)</td><td>Software you set up and babysit yourself</td><td><span class="pill p-mid">$97–497/mo</span></td><td class="us usrow-hl">You skip the months of learning</td></tr>
      </tbody>
    </table>
    </div>
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
  <h1 class="reveal">You're <span class="grad">two taps</span> from never missing a call.</h1>
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
