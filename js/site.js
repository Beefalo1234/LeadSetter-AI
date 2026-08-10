/* LeadSetter AI — shared site interactions (particles, reveal, counters, FAQ) */
"use strict";
(function () {
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

  /* ── counters ───────────────────────────────────── */
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    const el = e.target; cio.unobserve(el);
    const to = +el.dataset.to, pre = el.dataset.prefix || "", suf = el.dataset.suffix || "", t0 = performance.now(), D = 1400;
    (function step(t) { const p = Math.min(1, (t - t0) / D), v = Math.round(to * (1 - Math.pow(1 - p, 3))); el.textContent = pre + v + suf; if (p < 1) requestAnimationFrame(step); })(t0);
  }), { threshold: .5 });
  document.querySelectorAll(".cnt").forEach(el => cio.observe(el));

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
