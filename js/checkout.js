/* LeadSetter AI — checkout system.
   Every "50% off" / buy button on the site routes through checkout.html?bundle=X
   (or ?service=Y). This file holds the ONE place where real Stripe Payment Link
   URLs go. Until they're pasted (after Stripe setup, see STRIPE_SETUP.md), the
   checkout page shows a graceful fallback (call + email) instead of a dead link.
*/
"use strict";

// ── THE ONE CONFIG SPOT ──────────────────────────────────────────────
// After creating Payment Links in Stripe, paste each URL here. Empty string
// = checkout falls back to call/email. No page edits needed after this.
const CHECKOUT = {
  // bundles
  "starter":      "",   // $60/mo  Starter Bundle
  "advertising":  "",   // $110/mo Advertising Bundle
  "domination":   "",   // $110/mo Local Domination
  "full-stack":   "",   // $200/mo Full Stack (all 9)
  // à la carte services
  "ai":           "",   // $80/mo  AI Appointment Setting
  "gbp":          "",   // $80/mo  Google Maps / GBP Optimization
  "social":       "",   // $80/mo  Social Media Management
  "reviews":      "",   // $20/mo  Review Generation
  "website":      "",   // $20/mo  Website Management
  "sms":          "",   // $20/mo  SMS Marketing
  "email":        "",   // $20/mo  Email Marketing
  "citations":    "",   // $20/mo  Citations & Directories
  "tracking":     ""    // $20/mo  Call Tracking & ROI Reports
};

// plan metadata (name, monthly price, one-liner, features)
const PLANS = {
  "starter":     { name: "Starter Bundle", price: 60,  note: "AI + call tracking + reviews · 50% OFF ($120 menu)", features: ["AI appointment setting", "Call tracking & ROI reports", "Review generation", "+ $20 per qualified lead"] },
  "advertising": { name: "Advertising Bundle", price: 110, note: "AI + social + SMS + email + tracking · 50% OFF ($220 menu)", features: ["AI appointment setting", "Social media management", "SMS marketing", "Email marketing", "Call tracking & ROI reports", "+ $20 per qualified lead"] },
  "domination":  { name: "Local Domination", price: 110, note: "GBP + reviews + citations + website + social · 50% OFF ($220 menu)", features: ["Google Maps / GBP optimization", "Review generation", "Citations & directories", "Website management", "Social media management", "No lead fee — rank & convert"] },
  "full-stack":  { name: "Full Stack", price: 200, note: "All 9 services · $360 menu → $200 clean", features: ["All 9 services", "AI appointment setting + $20/lead", "Everything a $2,500/mo agency does", "Done for you — we run it all"] },
  "ai":          { name: "AI Appointment Setting", price: 80, note: "à la carte", features: ["AI answers missed calls ~2s, 24/7", "Books into your calendar", "Text confirmation & no-show reduction", "+ $20 per qualified lead"] },
  "gbp":         { name: "Google Maps / GBP Optimization", price: 80, note: "à la carte", features: ["Google Business Profile setup & tuning", "Category / service keyword optimization", "Photo & post management"] },
  "social":      { name: "Social Media Management", price: 80, note: "à la carte", features: ["Content calendar & posting", "Local audience growth", "Monthly performance recap"] },
  "reviews":     { name: "Review Generation", price: 20, note: "à la carte", features: ["Automated review requests after jobs", "Reply management", "Rating trend reporting"] },
  "website":     { name: "Website Management", price: 20, note: "à la carte", features: ["Landing page updates", "Speed & mobile polish", "Booking form integration"] },
  "sms":         { name: "SMS Marketing", price: 20, note: "à la carte", features: ["Campaign texts to opted-in lists", "Seasonal offers", "Compliance built in (STOP = stop)"] },
  "email":       { name: "Email Marketing / Newsletter", price: 20, note: "à la carte", features: ["Monthly newsletter", "Promo sends", "Open/click reporting"] },
  "citations":   { name: "Citations & Directories", price: 20, note: "à la carte", features: ["Consistent NAP across directories", "New citation setup", "Listing cleanup"] },
  "tracking":    { name: "Call Tracking & ROI Reports", price: 20, note: "à la carte", features: ["Per-source call tracking", "Monthly ROI report", "Missed-call leak alerts"] }
};

// 3+ services = 50% off — the à la carte bundle math helper
function alaCarteTotal(price, count) {
  if (count >= 3) return Math.round(price / 2);
  return price;
}

// ── checkout page renderer ─────────────────────────────────────────
(function () {
  const card = document.getElementById("planCard");
  if (!card) return; // not the checkout page

  const params = new URLSearchParams(location.search);
  const key = params.get("bundle") || params.get("service") || "";
  const plan = PLANS[key];

  document.getElementById("planName").textContent = plan ? plan.name : "Pick a plan";
  document.getElementById("planPrice").innerHTML = plan
    ? "$" + plan.price + "<small>/mo</small>"
    : "—";
  document.getElementById("planNote").textContent = plan ? plan.note : "";
  const feats = document.getElementById("planFeatures");
  feats.innerHTML = "";
  (plan ? plan.features : ["Choose a plan from the pricing page to check out."])
    .forEach(f => { const li = document.createElement("li"); li.textContent = f; feats.appendChild(li); });

  const btn = document.getElementById("checkoutBtn");
  const fallback = document.getElementById("fallback");
  const redirectNote = document.getElementById("redirectNote");
  const stripeUrl = plan ? (CHECKOUT[key] || "") : "";

  if (stripeUrl) {
    btn.href = stripeUrl;
    btn.textContent = "Continue to Secure Checkout →";
    redirectNote.textContent = "You'll be redirected to Stripe to complete your subscription. Recurring billing · cancel anytime.";
    fallback.style.display = "none";
    // auto-redirect after a beat — the checkout IS the default action now
    setTimeout(() => { location.href = stripeUrl; }, 2500);
  } else {
    btn.style.display = "none";
    fallback.style.display = "block";
    fallback.innerHTML = fallback.innerHTML.replace("PLAN", plan ? plan.name : "this plan");
    redirectNote.textContent = "Online checkout activates the moment we flip the switch (one tap after your Stripe setup) — until then, locking your discount is a 30-second email or call.";
  }
})();
