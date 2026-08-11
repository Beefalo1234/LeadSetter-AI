/* LeadSetter AI — shared site interactions (particles, reveal, counters, FAQ) */
"use strict";
(function () {
  /* ── service flow picker (home + how-it-works) ────── */
  const FLOWS = {
    ai:        ["We plug in", "We connect our AI to your business phone number and calendar. You approve the setup — that's your whole job.",
                "AI answers everything", "Missed, after-hours, and weekend calls get answered in ~2 seconds — qualified, booked, and confirmed by text.",
                "You show up and get paid", "Booked jobs land in your calendar with the details. You close the work; we send the ROI report."],
    gbp:       ["We audit your Google profile", "We check your categories, photos, keywords, and service area against how neighbors actually search.",
                "We optimize it daily", "So 'AC repair near me' finds you first — and every new review makes Google trust you more.",
                "More local calls, all answered", "Inbound calls climb as you rank higher. The AI answers them and books the jobs."],
    social:    ["We set up your pages", "Google, Facebook, Instagram — brand photos, service list, and a posting calendar.",
                "We post every week", "Before/afters, seasonal offers, helpful tips. We reply to comments and messages too.",
                "Neighbors find you", "Steady visibility turns into calls — and the AI books the work while you're on a job."],
    reviews:   ["We set up the review flow", "After every job, your customer gets a simple text: 'How did we do?' with a one-tap link.",
                "Happy customers leave 5 stars", "Easy links and gentle reminders — no begging, no awkward asks.",
                "Your rating climbs", "A higher rating and more reviews push you up Google's results, which means more calls and bookings."],
    website:   ["We build or refresh your site", "Clean, fast, and mobile-first — it looks great on a phone because that's where your customers are.",
                "We keep it updated", "Prices, photos, offers, and security — handled monthly, no work from you.",
                "Visitors become callers", "Clear call buttons on every page. When they call, the AI picks up and books."],
    sms:       ["We build your list", "From customers who opted in and new leads we capture — your people, with permission.",
                "We send seasonal offers", "Tune-up reminders, specials, 'we're booking this week' texts. No spam, no blasts.",
                "Old customers come back", "Reactivation texts book repeat jobs — and every call is captured by the AI."],
    email:     ["We build your list", "Past customers and opted-in leads, organized by service and season.",
                "We send useful emails", "Monthly newsletters, seasonal reminders, and offers — written and scheduled by us.",
                "Past customers return", "A steady stream of repeat work on autopilot, all tracked in your ROI report."],
    citations: ["We list you everywhere", "Google, Yelp, BBB, and 40+ directories — same name, address, phone on all of them.",
                "We fix the wrong info", "Old listings, wrong numbers, duplicates — cleaned up so you're findable everywhere.",
                "Google trusts you more", "Consistent listings boost your ranking, which means more calls — answered and booked by the AI."],
    tracking:  ["We install call tracking", "Every call gets tagged with where it came from — your sign, a ad, Google, a past customer.",
                "We report every lead", "One dashboard: source, cost, and booked value. You see what works and what doesn't.",
                "You double down on winners", "Cut what's wasting money, spend where the calls come from. Your ROI report tells you exactly where."]
  };
  function initPicker() {
    const pills = document.querySelectorAll("#pickPills .pill");
    const steps = document.getElementById("flowSteps");
    const dotsWrap = document.getElementById("pickDots");
    const prev = document.getElementById("pickPrev");
    const next = document.getElementById("pickNext");
    if (!pills.length || !steps) return;
    const names = [...pills].map(p => p.dataset.svc);
    function show(svc) {
      const f = FLOWS[svc];
      steps.querySelector(".fs-t1").textContent = f[0];
      steps.querySelector(".fs-p1").textContent = f[1];
      steps.querySelector(".fs-t2").textContent = f[2];
      steps.querySelector(".fs-p2").textContent = f[3];
      steps.querySelector(".fs-t3").textContent = f[4];
      steps.querySelector(".fs-p3").textContent = f[5];
      pills.forEach(p => p.classList.toggle("on", p.dataset.svc === svc));
      [...dotsWrap.children].forEach((d, i) => d.classList.toggle("on", names[i] === svc));
    }
    if (dotsWrap) {
      dotsWrap.innerHTML = "";
      names.forEach(svc => {
        const d = document.createElement("span");
        d.className = "dot";
        d.addEventListener("click", () => show(svc));
        dotsWrap.appendChild(d);
      });
    }
    pills.forEach(p => p.addEventListener("click", () => show(p.dataset.svc)));
    const idx = () => names.indexOf([...pills].find(p => p.classList.contains("on"))?.dataset.svc ?? "ai");
    if (prev) prev.addEventListener("click", () => show(names[(idx() - 1 + names.length) % names.length]));
    if (next) next.addEventListener("click", () => show(names[(idx() + 1) % names.length]));
    show("ai");
  }
  document.addEventListener("DOMContentLoaded", initPicker);

  /* ── canvas particles ───────────────────────────── */
  const c = document.getElementById("particles");
  if (c) {
    const x = c.getContext("2d");
    let w, h, ps = [];
    function size() { w = c.width = innerWidth; h = c.height = innerHeight; }
    size(); addEventListener("resize", size);
    const N = Math.min(70, innerWidth / 18);
    for (let i = 0; i < N; i++) ps.push({ x: Math.random() * w, y: Math.random() * h, r: Math.random() * 1.8 + .4, vx: (Math.random() - .5) * .25, vy: (Math.random() - .5) * .25, a: Math.random() * .5 + .15 });
    (function tick() {
      x.clearRect(0, 0, w, h);
      for (const p of ps) {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > w) p.vx *= -1;
        if (p.y < 0 || p.y > h) p.vy *= -1;
        x.beginPath(); x.arc(p.x, p.y, p.r, 0, 7);
        x.fillStyle = `rgba(232,163,61,${p.a})`; x.fill();
      }
      requestAnimationFrame(tick);
    })();
  }

  /* ── scroll reveal ──────────────────────────────── */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .12 });
  document.querySelectorAll(".reveal").forEach(el => io.observe(el));

  /* ── counters (cascade: each square counts up one by one) ── */
  const cnts = [...document.querySelectorAll(".cnt")];
  if (cnts.length) {
    const run = () => cnts.forEach((el, i) => {
      const to = +el.dataset.to, pre = el.dataset.prefix || "", suf = el.dataset.suffix || "", D = 1200;
      setTimeout(() => {
        const t0 = performance.now();
        (function step(t) {
          const p = Math.min(1, (t - t0) / D), v = Math.round(to * (1 - Math.pow(1 - p, 3)));
          el.textContent = pre + v + suf;
          if (p < 1) requestAnimationFrame(step);
        })(t0);
      }, i * 420);
    });
    const cio = new IntersectionObserver(es => es.forEach(e => {
      if (!e.isIntersecting) return;
      cio.disconnect(); run();
    }), { threshold: .2 });
    cio.observe(cnts[0].closest("section") || cnts[0]);
  }

  /* ── calculator (pricing page) ──────────────────── */
  const leads = document.getElementById("leads");
  if (leads) {
    const lv = document.getElementById("leadsVal"),
      oUs = document.getElementById("outUs"), oG = document.getElementById("outGoogle"),
      oA = document.getElementById("outAngi"), oS = document.getElementById("outSave");
    const money = n => "$" + n.toLocaleString("en-US");
    function calc() {
      const n = +leads.value; lv.textContent = n + " leads";
      const us = 200 + n * 20, gg = n * 100, an = n * 75;
      oUs.textContent = money(us); oG.textContent = money(gg); oA.textContent = money(an); oS.textContent = money(gg - us);
    }
    leads.addEventListener("input", calc); calc();
  }

  /* ── FAQ accordion ──────────────────────────────── */
  document.querySelectorAll(".fq").forEach(b => b.addEventListener("click", () => {
    const it = b.parentElement, fa = b.nextElementSibling;
    const open = it.classList.contains("open");
    document.querySelectorAll(".fitem.open").forEach(o => { o.classList.remove("open"); o.querySelector(".fa").style.maxHeight = null; });
    if (!open) { it.classList.add("open"); fa.style.maxHeight = fa.scrollHeight + "px"; }
  }));
})();
