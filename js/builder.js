/* LeadSetter AI — custom plan builder (pricing page)
   The à la carte grid IS the builder: tap service cards to pick them.
   Discounts: 3+ services → 50% OFF, then a "Kindness" −5% applies to
   roughly half of all possible combos (deterministic parity rule,
   includes 1- and 2-service picks). Same rule lives in checkout.js. */
"use strict";
(function () {
  const SVCS = {
    ai:        { n: "AI Appointment Setting", p: 60 },
    gbp:       { n: "Google Maps / GBP Optimization", p: 60 },
    social:    { n: "Social Media Management", p: 60 },
    reviews:   { n: "Review Generation", p: 20 },
    website:   { n: "Website Management", p: 20 },
    sms:       { n: "SMS Marketing", p: 20 },
    email:     { n: "Email Marketing / Newsletter", p: 20 },
    citations: { n: "Listings & Directories", p: 20 },
    tracking:  { n: "Call Tracking & ROI Reports", p: 20 }
  };
  const ORDER = Object.keys(SVCS); // ai=1 … tracking=9

  // Kindness −5%: applies when the sum of (1-based) service positions is even.
  // Exactly half of all subsets qualify (255 of 511 non-empty) — deterministic.
  function kindness(ids) {
    return (ids.reduce((a, k) => a + (ORDER.indexOf(k) + 1), 0) % 2) === 0;
  }
  function money(x) { return "$" + Math.round(x).toLocaleString(); }

  function init() {
    const cards = document.querySelectorAll("#svcGrid .svc");
    const out = document.getElementById("builderOut");
    if (!cards.length || !out) return;

    const selected = new Set();

    cards.forEach(card => {
      card.addEventListener("click", (e) => {
        if (e.target.closest(".buy")) return; // let the Buy link do its thing
        const k = card.dataset.svc;
        if (selected.has(k)) { selected.delete(k); card.classList.remove("on"); }
        else { selected.add(k); card.classList.add("on"); }
        render();
      });
    });

    function render() {
      if (!selected.size) { out.hidden = false; document.getElementById("bTotal").textContent = "Tap any service above"; document.getElementById("bMenu").textContent = "—"; document.getElementById("bList").textContent = "—"; document.getElementById("bHalfRow").hidden = true; document.getElementById("bKindRow").hidden = true; document.getElementById("bRoi").textContent = "—"; document.getElementById("bBadges").innerHTML = ""; document.getElementById("bCheckout").href = "#"; return; }
      out.hidden = false;
      const ids = [...selected];
      document.getElementById("bList").textContent = ids.map(k => SVCS[k].n).join(", ");
      const menu = ids.reduce((a, k) => a + SVCS[k].p, 0);
      document.getElementById("bMenu").textContent = money(menu);
      const halfRow = document.getElementById("bHalfRow");
      const half = document.getElementById("bHalf");
      const kindRow = document.getElementById("bKindRow");
      const kindEl = document.getElementById("bKind");
      let total = menu;
      if (ids.length >= 3) {
        half.textContent = "−" + money(menu / 2);
        total = menu / 2;
        halfRow.hidden = false;
      } else { halfRow.hidden = true; }
      let kindActive = false;
      if (kindness(ids)) {
        const saved = total * 0.05;
        kindEl.textContent = "−" + money(saved);
        total -= saved;
        kindActive = true;
        kindRow.hidden = false;
      } else { kindRow.hidden = true; }
      document.getElementById("bTotal").textContent = money(total) + "/mo";
      const leads = Math.round(10 + ids.length * 4);
      document.getElementById("bRoi").textContent = "~" + leads + " leads/mo, each worth $500–$5,000 — vs " + money(total) + "/mo";
      const badges = document.getElementById("bBadges");
      badges.innerHTML = "";
      if (ids.length >= 3) badges.appendChild(badge("50% OFF — " + ids.length + " services"));
      if (kindActive) badges.appendChild(badge("Kindness −5%"));
      badges.appendChild(badge("$0 setup · 14-day money-back"));
      document.getElementById("bCheckout").href = "checkout.html?custom=" + ids.join(",");
    }
    function badge(t) { const b = document.createElement("span"); b.className = "bbadge"; b.textContent = t; return b; }
  }
  document.addEventListener("DOMContentLoaded", init);
})();
