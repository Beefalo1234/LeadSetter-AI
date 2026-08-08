// ═══════════════════════════════════════════════════════════════
//  BUSINESS PLAN DATA — edit this file to update the dashboard.
//  Every change: commit + push → GitHub Pages updates live.
// ═══════════════════════════════════════════════════════════════

const PLAN = {
  updated: "2026-08-08",
  phase: "Execution starts 2026-08-08 — pricing v2: $149/mo + $20/lead, NO setup fee",
  business: {
    name: "LeadSetter AI — appointment-setting & lead-gen for home-service businesses",
    model: "Done-for-you AI appointment setting as a subscription service. We find, qualify, and book appointments for home-service businesses (HVAC, roofing, solar, remodeling) using AI voice + follow-up automation.",
    why: [
      "Observed pricing from research: lead-gen/outreach services sell at EUR 300–800/mo per client (KEqhu_bAjkk), $1–5K setup + $500–2K/mo maintenance (FAR_Fr87gm0), and $4–5K/mo × 17–21 clients ≈ $1M ARR (GkHwnQdoDpM).",
      "Each booked job for these niches is worth $500–$5,000 to the client — paying ~$20/qualified lead for 3–5 extra booked jobs is an easy yes.",
      "Zero setup fee + cancel anytime = lowest-friction offer in the market; we win on results, not upfront cash.",
      "Runs on the stack we already own (Hermes Agent + skills) → near-zero startup cost, ~96% gross margin."
    ]
  },
  offer: {
    setupFee: 0,             // USD, one-time — intentionally $0 (low friction, new business)
    retainer: 149,           // USD / month — platform base
    perLead: 20,             // USD / qualified appointment lead
    deliverables: [
      "30 qualified leads/mo (name, contact, source, signal) — $20/lead",
      "AI answers missed calls in ~2 seconds, 24/7, books into their calendar",
      "Automated confirmation + no-show reduction (text follow-up)",
      "Live dashboard for the client (via our dashboard)"
    ],
    costToServePerClient: 30,  // API + telephony + tooling, USD/mo
    grossMarginPct: 96         // (749-30)/749
  },
  // ── THE EXACT MATH ───────────────────────────────────────────
  math: {
    currency: "USD",
    unit: {
      setupFee: 0,
      retainerMonthly: 149,
      perLead: 20,
      monthlyCostToServe: 30,
      grossMarginPerClientPerMonth: 719,   // 749 - 30
      grossMarginPct: 96,
      leadsPerClientPerMonth: 30,
      costPerLead: 1.0           // 30 / 30 (our serving cost per lead)
    },
    breakeven: {
      fixedMonthlyCosts: 100,     // domain, minor tooling, buffer
      clientsToBreakeven: 1,      // 1 client at $749/mo covers all fixed costs
      note: "No setup fee — first client's $149 base alone covers fixed costs; 30 leads ≈ $600 more. Client #1 is profitable in month one."
    },
    // Monthly projections — conservative ramp, one person + automations. No setup revenue.
    projection: [
      { m: 1, clients: 2,  setup: 0, mrr: 1498,  revenue: 1498,  costs: 160,  profit: 1338 },
      { m: 2, clients: 4,  setup: 0, mrr: 2996,  revenue: 2996,  costs: 220,  profit: 2776 },
      { m: 3, clients: 6,  setup: 0, mrr: 4494,  revenue: 4494,  costs: 280,  profit: 4214 },
      { m: 4, clients: 8,  setup: 0, mrr: 5992,  revenue: 5992,  costs: 340,  profit: 5652 },
      { m: 5, clients: 10, setup: 0, mrr: 7490,  revenue: 7490,  costs: 400,  profit: 7090 },
      { m: 6, clients: 12, setup: 0, mrr: 8988,  revenue: 8988,  costs: 460,  profit: 8528 }
    ],
    annualNote: "Month-6 run rate: $8,988 MRR ≈ $108K/yr. Path to $1M ARR: 17–21 clients at $4–5K/mo (full-agency tier), per research observation.",
    assumptions: [
      "Close rate: 1 in 20 prospects (5%) — conservative for outbound with a paid outcome.",
      "Client churn: 10%/mo assumed in ramp (not shown; net adds still positive).",
      "Costs: API (gemini-flash-lite tier ≈ $0.001/call brain) + Twilio/telephony (~$0.10/call) + email infra + minor tooling.",
      "Time: ~20–30 hrs/wk during ramp, decreasing as workflows productize."
    ],
    fundingRequest: {
      needed: false,
      startupCosts: "≈ $100 total: domain (~$15/yr) + email-sending domain warmup tool (~$30) + misc (~$55). Covered by existing budget — no external capital requested.",
      ifNeeded: "If scaling past 8 clients requires a VA or paid ads, that would be requested separately with exact numbers."
    }
  },
  // ── CALENDAR: execution starts 2026-08-08 ────────────────────
  calendar: {
    start: "2026-08-08",
    weeks: [
      {
        week: 1, dates: "Aug 8–14", theme: "Foundation & validation",
        days: [
          { d: "Sat 08-08", task: "Lock niche (HVAC/roofing/solar); write offer page; define 30-lead ICP", done: false },
          { d: "Sun 08-09", task: "Build prospect list: 100 businesses w/ contact + owner name (Hermes research)", done: false },
          { d: "Mon 08-10", task: "Build outreach sequence: email + SMS/voicemail drip, scripts", done: false },
          { d: "Tue 08-11", task: "Launch outreach batch 1 (25 prospects); set up tracking sheet", done: false },
          { d: "Wed 08-12", task: "Outreach batch 2 (25); follow-up #1 on batch 1; refine script", done: false },
          { d: "Thu 08-13", task: "Book calls; prep sales script (value = booked jobs, not leads); 2–3 calls", done: false },
          { d: "Fri 08-14", task: "Close attempt #1; on win: onboard + deliver first 30 leads; weekly review", done: false }
        ]
      },
      {
        week: 2, dates: "Aug 15–21", theme: "First revenue",
        days: [
          { d: "Sat 08-15", task: "Outreach batch 3 (25); fix what underperformed", done: false },
          { d: "Sun 08-16", task: "Deliver client 1 first lead batch; build client dashboard", done: false },
          { d: "Mon 08-17", task: "Outreach batch 4 (25) = 100 total contacted", done: false },
          { d: "Tue 08-18", task: "Follow-ups; book 5+ calls for the week; 2–4 calls", done: false },
          { d: "Wed 08-19", task: "Close attempt #2; onboard if won", done: false },
          { d: "Thu 08-20", task: "Client 1 check-in: show booked jobs value; ask for referral", done: false },
          { d: "Fri 08-21", task: "Weekly review: pipeline, what converts, refresh list +50", done: false }
        ]
      },
      {
        week: 3, dates: "Aug 22–28", theme: "Scale to 3–4 clients",
        days: [
          { d: "Sat 08-22", task: "Outreach fresh 50 (new niches if needed: remodelers, plumbers)", done: false },
          { d: "Sun 08-23", task: "Productize: template the offer/onboarding for repeatability", done: false },
          { d: "Mon 08-24", task: "Follow-ups + referrals from client 1", done: false },
          { d: "Tue 08-25", task: "Calls; close attempts", done: false },
          { d: "Wed 08-26", task: "Deliver batches for all active clients", done: false },
          { d: "Thu 08-27", task: "Client success calls; collect testimonials", done: false },
          { d: "Fri 08-28", task: "Weekly review: target 4 clients active by end of week", done: false }
        ]
      },
      {
        week: 4, dates: "Aug 29–Sep 4", theme: "5 clients & systems",
        days: [
          { d: "Sat 08-29", task: "Refresh prospect pipeline; outreach", done: false },
          { d: "Sun 08-30", task: "Document workflow (skill-ify the process for reuse)", done: false },
          { d: "Mon 08-31", task: "Calls; close attempts to reach 5 active", done: false },
          { d: "Tue 09-01", task: "Onboard new clients; deliver lead batches", done: false },
          { d: "Wed 09-02", task: "Automate: cron-based lead delivery + reporting", done: false },
          { d: "Thu 09-03", task: "Client success; gather case-study numbers", done: false },
          { d: "Fri 09-04", task: "Monthly review: ≥5 clients, $3.5K+ revenue month 1", done: false }
        ]
      }
    ],
    months: [
      { m: "Month 2 (Sep)", theme: "Reach 8 clients; $5K revenue; introduce $4–5K full-agency tier", done: false },
      { m: "Month 3 (Oct)", theme: "10 clients; $6.5K revenue; productize sales (script + case study as closer)", done: false },
      { m: "Month 4 (Nov)", theme: "12 clients; test full-agency tier ($2–5K/mo); decide VA hire", done: false },
      { m: "Month 5 (Dec)", theme: "13–15 clients; $8.5K revenue; system handoff-ready", done: false },
      { m: "Month 6 (Jan)", theme: "15+ clients; $10K/mo run rate; evaluate second offer (clipping/YT niche)", done: false }
    ]
  },
  // ── LIVE PROGRESS TRACKER (agent updates daily) ─────────────
  progress: {
    lastUpdated: "2026-08-08",
    log: [
      { date: "2026-08-07", text: "Plan built: niche, offer, exact math, 4-week day-by-day calendar. Dashboard deployed." },
      { date: "2026-08-08", text: "Pricing v2: $0 setup, $149/mo + $20/lead. Prospect list built (12.8K NYC HIC contractors). Call scripts rewritten (Claude Sonnet 5). Short-form ad scripts drafted." }
    ],
    metrics: { clients: 0, mrr: 0, revenue: 0, prospectsContacted: 0, callsBooked: 0, leadsDelivered: 0 }
  }
};
