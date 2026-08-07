// ═══════════════════════════════════════════════════════════════
//  BUSINESS PLAN DATA — edit this file to update the dashboard.
//  Every change: commit + push → GitHub Pages updates live.
// ═══════════════════════════════════════════════════════════════

const PLAN = {
  updated: "2026-08-07",
  phase: "Planning complete — execution starts 2026-08-08",
  business: {
    name: "LeadSetter AI — appointment-setting & lead-gen for home-service businesses",
    model: "Done-for-you AI lead generation as a subscription service. We find, qualify, and book appointments for high-ticket home-service businesses (HVAC, roofing, solar, remodeling) using an automated Hermes Agent workflow.",
    why: [
      "Observed pricing from research: lead-gen/outreach services sell at EUR 300–800/mo per client (KEqhu_bAjkk), $1–5K setup + $500–2K/mo maintenance (FAR_Fr87gm0), and $4–5K/mo × 17–21 clients ≈ $1M ARR (GkHwnQdoDpM).",
      "Each booked job for these niches is worth $500–$5,000 to the client — paying $750/mo for 3–5 extra booked jobs is an easy yes.",
      "Runs on the stack we already own (Hermes Agent + skills + yt-scraper pipeline) → near-zero startup cost, ~92–96% gross margin.",
      "Playbook from research: one painful niche → one expensive problem → one workflow → sell a clear outcome (GkHwnQdoDpM)."
    ]
  },
  offer: {
    setupFee: 1000,        // USD, one-time
    retainer: 750,         // USD / month
    deliverables: [
      "30 qualified leads/mo (name, contact, source, signal)",
      "Automated multi-touch follow-up (email + SMS/voicemail drip)",
      "Calendar of booked appointments delivered weekly",
      "Live dashboard for the client (via our dashboard)"
    ],
    costToServePerClient: 45,  // API + tooling, USD/mo
    grossMarginPct: 94         // (750-45)/750
  },
  // ── THE EXACT MATH ───────────────────────────────────────────
  math: {
    currency: "USD",
    unit: {
      setupFee: 1000,
      retainerMonthly: 750,
      monthlyCostToServe: 45,
      grossMarginPerClientPerMonth: 705,
      grossMarginPct: 94,
      leadsPerClientPerMonth: 30,
      costPerLead: 1.5           // 45 / 30
    },
    breakeven: {
      fixedMonthlyCosts: 100,     // domain, minor tooling, buffer
      clientsToBreakeven: 1,      // 1 retainer covers all fixed costs
      note: "Client #1 setup fee ($1,000) alone covers ~10 months of fixed costs. No external funding required."
    },
    // Monthly projections — conservative ramp, one person + automations
    projection: [
      { m: 1, clients: 2,  setup: 2000, mrr: 1500,  revenue: 3500,  costs: 190,  profit: 3310 },
      { m: 2, clients: 4,  setup: 2000, mrr: 3000,  revenue: 5000,  costs: 280,  profit: 4720 },
      { m: 3, clients: 6,  setup: 2000, mrr: 4500,  revenue: 6500,  costs: 370,  profit: 6130 },
      { m: 4, clients: 8,  setup: 1000, mrr: 6000,  revenue: 7000,  costs: 460,  profit: 6540 },
      { m: 5, clients: 10, setup: 1000, mrr: 7500,  revenue: 8500,  costs: 550,  profit: 7950 },
      { m: 6, clients: 12, setup: 1000, mrr: 9000,  revenue: 10000, costs: 640,  profit: 9360 }
    ],
    annualNote: "Month-6 run rate: $9,000 MRR ≈ $108K/yr. Path to $1M ARR: 17–21 clients at $4–5K/mo (full-agency tier), per research observation.",
    assumptions: [
      "Close rate: 1 in 20 prospects (5%) — conservative for outbound with a paid outcome.",
      "Client churn: 10%/mo assumed in ramp (not shown; net adds still positive).",
      "Costs: API (deepseek/gemini-flash-lite tier) + email infra + minor tooling.",
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
      { m: "Month 2 (Sep)", theme: "Reach 8 clients; $5K revenue; raise retainer to $1K for new clients", done: false },
      { m: "Month 3 (Oct)", theme: "10 clients; $6.5K revenue; productize sales (script + case study as closer)", done: false },
      { m: "Month 4 (Nov)", theme: "12 clients; test full-agency tier ($2–5K/mo); decide VA hire", done: false },
      { m: "Month 5 (Dec)", theme: "13–15 clients; $8.5K revenue; system handoff-ready", done: false },
      { m: "Month 6 (Jan)", theme: "15+ clients; $10K/mo run rate; evaluate second offer (clipping/YT niche)", done: false }
    ]
  },
  // ── LIVE PROGRESS TRACKER (agent updates daily) ─────────────
  progress: {
    lastUpdated: "2026-08-07",
    log: [
      { date: "2026-08-07", text: "Plan built: niche, offer, exact math, 4-week day-by-day calendar. Dashboard deployed." },
      { date: "2026-08-08", text: "EXECUTION STARTS: niche + offer page + 100-prospect list." }
    ],
    metrics: { clients: 0, mrr: 0, revenue: 0, prospectsContacted: 0, callsBooked: 0, leadsDelivered: 0 }
  }
};
