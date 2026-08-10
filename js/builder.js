/* LeadSetter AI — custom plan builder (pricing page) */
"use strict";
(function () {
  const SVCS = {
    ai:        { n: "AI Appointment Setting", p: 60, lead: true },
    gbp:       { n: "Google Maps Optimization", p: 60, was: 80 },
    social:    { n: "Social Media Management", p: 60, was: 80 },
    reviews:   { n: "Review Generation", p: 20 },
    website:   { n: "Website Management", p: 20 },
    sms:       { n: "SMS Marketing", p: 20 },
    email:     { n: "Email Marketing / Newsletter", p: 20 },
    citations: { n: "Listings & Directories", p: 20 },
    tracking:  { n: "Call Tracking & ROI Reports", p: 20 }
  };
  // fun combo discounts — stack AFTER the 50% bundle discount
  const COMBOS = [
    { s: ["ai", "social"], name: "Dynamic Duo", off: 0.05 },
    { s: ["gbp", "reviews"], name: "Local Hero", off: 0.05 },
    { s: ["sms", "email"], name: "Double Reach", off: 0.05 },
    { s: ["website", "tracking"], name: "Data Duo", off: 0.05 }
  ];
  const GHOST = ["Reputation Monitoring (coming soon)", "Instant Quote Engine (coming soon)"];

  function money(x) { return "$" + Math.round(x).toLocaleString(); }

  function init() {
    const grid = document.getElementById("builderGrid");
    const out = document.getElementById("builderOut");
    if (!grid || !out) return;

    const selected = new Set();
    const pills = {};

    Object.entries(SVCS).forEach(([k, v]) => {
      const el = document.createElement("button");
      el.className = "bp";
      el.innerHTML = '<span class="tick">✓</span><div class="bn">' + v.n + '</div><div class="bp2">' +
        (v.was ? '<s class="wasprice">$' + v.was + '</s>' : "") + "$" + v.p + "/mo" +
        (v.lead ? " + $20/lead" : "") + "</div>";
      el.addEventListener("click", () => {
        if (selected.has(k)) { selected.delete(k); el.classList.remove("on"); }
        else { selected.add(k); el.classList.add("on"); }
        render();
      });
      pills[k] = el;
      grid.appendChild(el);
    });
    GHOST.forEach(g => {
      const el = document.createElement("div");
      el.className = "bp ghost-card";
      el.innerHTML = '<div class="bn">' + g + "</div><div class=\"bp2\">more services are on the way</div>";
      grid.appendChild(el);
    });

    function render() {
      if (!selected.size) { out.hidden = true; return; }
      out.hidden = false;
      const list = [...selected].map(k => SVCS[k].n);
      document.getElementById("bList").textContent = list.join(", ");
      const menu = [...selected].reduce((a, k) => a + SVCS[k].p, 0);
      document.getElementById("bMenu").textContent = money(menu);
      const halfRow = document.getElementById("bHalfRow");
      const half = document.getElementById("bHalf");
      const comboRow = document.getElementById("bComboRow");
      const combo = document.getElementById("bCombo");
      let total = menu;
      if (selected.size >= 3) {
        half.textContent = "−" + money(menu / 2);
        total = menu / 2;
        halfRow.hidden = false;
      } else { halfRow.hidden = true; }
      const hits = COMBOS.filter(c => c.s.every(s => selected.has(s)));
      if (hits.length) {
        const saved = hits.reduce((a, c) => a + total * c.off, 0);
        combo.textContent = "−" + money(saved) + " (" + hits.map(c => c.name + " −5%").join(", ") + ")";
        total -= saved;
        comboRow.hidden = false;
      } else { comboRow.hidden = true; }
      document.getElementById("bTotal").textContent = money(total) + "/mo";
      const leads = Math.round(10 + selected.size * 4);
      const jobVal = "$500–$5,000";
      document.getElementById("bRoi").textContent = "~" + leads + " leads/mo, each worth " + jobVal + " — vs " + money(total) + "/mo";
      const badges = document.getElementById("bBadges");
      badges.innerHTML = "";
      if (selected.size >= 3) badges.appendChild(badge("50% OFF — " + selected.size + " services"));
      hits.forEach(c => badges.appendChild(badge(c.name + " −5%")));
      badges.appendChild(badge("$0 setup · 14-day refund"));
      document.getElementById("bCheckout").href = "checkout.html?custom=" + [...selected].join(",");
    }
    function badge(t) { const b = document.createElement("span"); b.className = "bbadge"; b.textContent = t; return b; }
  }
  document.addEventListener("DOMContentLoaded", init);
})();
