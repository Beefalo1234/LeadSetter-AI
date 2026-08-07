# LeadSetter AI — Market Research, Competitive Analysis & Advertising Channels
**Date:** 2026-08-07 | **Prepared for:** Gray Neuringer | **Status:** Live build-log → execution starts 2026-08-08

---

## 1. Executive Summary

- **Price point validated.** $1,000 setup + $750/mo for 30 qualified appointment leads = **$25 per qualified lead**, vs $45–$228 cost-per-lead on Google Ads for HVAC/roofing and $250–$1,000+ *true* cost per booked job on Angi (shared leads, 8–20% close rates). The offer undercuts every acquisition channel the customer currently uses.
- **Clear white space.** Contractors are squeezed between (a) junk shared leads from Angi/Thumbtack/Yelp, (b) DIY AI platforms (Retell/Vapi/Bland/GHL) that require technical skill they don't have, and (c) expensive human services (Smith.ai, Ruby) that only answer inbound calls. Nobody sells *done-for-you, outcome-based AI appointment setting* at a fixed monthly price.
- **⚠️ Regulatory constraint shapes the product.** The FCC ruled AI-generated voices = "artificial or prerecorded voice" under TCPA → **prior express written consent required for outbound AI calls**. Florida (FTSA), Oklahoma, and California add state penalties. **Safe model: inbound-first** — AI follows up on form fills / opted-in leads (consent on the form), confirms appointments, reduces no-shows. Cold AI calling is a legal liability, not a feature.
- **Fastest acquisition channels:** cold email (7–14 days to first lead) and cold calling (1–7 days). Highest trust-per-dollar: supply-house partnerships. Total 90-day budget: **$300–$500**.

---

## 2. Market Research

### Key numbers
| Metric | Value | Source |
|---|---|---|
| US home-services market size | $600B–$842B, growing 7–9%/yr | Searchlight Digital / LocaliQ 2025–26 |
| Contractors increasing marketing budgets | 72% | Thomas Town Digital 2026 |
| Typical contractor monthly marketing spend | $1,000–$10,000+ | industry benchmarks |
| Google Ads CPL — HVAC | $45–$104 (up to $149 non-branded) | Searchlight Digital |
| Google Ads CPL — Roofing | $79–$228+ (surges past $200 in peak seasons) | Searchlight Digital |
| Angi/HomeAdvisor lead cost | $15–$100+ per lead, SOLD to 3–8 contractors simultaneously | Tradesmen Guild / Baadigi |
| True cost per booked job (marketplace) | $250–$1,000+ (8–20% close rates) | Tradesmen Guild |
| Appointment no-show rate (no automated confirm) | 15–25% | SchedulingKit |
| Jobs lost without instant response | >50% (speed-to-lead) | CallRail / Thomas Town |

### Pain points (the wedge)
1. **Aggregator fatigue** — Angi/HomeAdvisor sell the same lead to 3–8 competitors; FTC fined Angi $7.2M in 2023 over lead billing practices. Contractors report fake leads and tire-kickers.
2. **Speed-to-lead** — over 50% of jobs go to the contractor who answers first. Manual follow-up loses deals.
3. **No-shows** — 15–25% of booked appointments without automated confirmation eat dispatch hours.
4. **DIY AI too technical** — voice platforms require prompt engineering, telephony, CRM wiring.

### Regulatory (compliance = competitive moat)
- **FCC (2025):** AI-generated voices classified as "artificial or prerecorded voice" under TCPA → prior express written consent needed for robocalls/autodialer + AI voice.
- **States:** Florida FTSA, Oklahoma, California have strict rules + private right of action; two-party consent states (e.g. CA) require recording disclosure.
- **Compliant playbook:** work inbound leads only (web form with TCPA consent disclosure), opted-in lists, text follow-up with consent, recorded calls with disclosure. Make compliance a selling point: "we never cold-call homeowners illegally."

---

## 3. Competitive Analysis

| Name | Bucket | Pricing | Positioning | Weakness we exploit |
|---|---|---|---|---|
| Retell AI / Vapi | DIY voice platform | ~$0.05–0.10/min + Twilio | Dev infrastructure for voice agents | Requires technical skill; no trade workflows |
| Bland.ai / Air AI | AI SDR platform | Bland $249+/mo + usage; Air $5,000+ setup | Outbound AI calling | High setup friction, enterprise pricing, no local-trade focus |
| GoHighLevel / Synthflow | CRM/AI builder | GHL $97–497/mo; Synthflow $29–990/mo | All-in-one agency/SMB stack | Contractor must configure & maintain it |
| Smith.ai | Human receptionist | $240–$1,500+/mo | Premium inbound call intake | Inbound-only, reactive, per-minute cost |
| Ruby Receptionists | Human receptionist | $300–$1,000+/mo | Answering service | No outbound pipeline generation |
| Angi / HomeAdvisor | Lead marketplace | $300+/mo + $20–150/lead | Dominant aggregator | Shared leads, price wars, poor quality |
| Thumbtack | Lead marketplace | $15–60+/lead | Bidding platform | Bidding wars, tire-kickers, no qualification |
| Yelp Ads | Marketplace/PPC | $300–$1,000+/mo | Review-driven directory | Expensive clicks, no booking |
| Done-for-you AI agencies | Agency | $1,500–$5,000+/mo (unverified) | AI lead-gen retainers | Cost-prohibitive for local contractors |

**White space:** outcome-based, done-for-you, fixed-price AI appointment setting for home services. $25/qualified lead beats every alternative; exclusive leads beat marketplaces; done-for-you beats DIY; fixed price beats $2.5K+ human retainers. *Note: "done-for-you AI agency pricing" figures are industry-standard estimates, not verified public prices.*

---

## 4. Free & Cheap Advertising (ranked)

| # | Channel | Cost | Timeline to first lead | Payoff | Start today |
|---|---|---|---|---|---|
| 1 | **Cold email** | $60–90/mo (3 domains ~$12 + Instantly $37; Apollo free tier) | 7–14 days | High (1–3% reply) | Buy 3 domains, set SPF/DKIM/DMARC, load 500 HVAC-owner emails from Apollo |
| 2 | **Cold calling / voicemail drops** | $0–30/mo (OpenPhone) | 1–7 days | High (fastest) | Scrape 100 local contractor #s from Google Maps + state licensing boards, 30-sec pitch |
| 3 | **Supply-house partnerships** | $0 + $250 referral fee/closed client | 14–30 days | Very high (trust transfer) | Walk into 5 Johnstone/Ferguson branches, pitch rev-share on missed-call clients |
| 4 | **Facebook contractor groups** | $0 | 14–21 days | Med-high | Join HVAC Nation / Roofing Success; post case-study breakdowns, don't pitch |
| 5 | **Local SEO + GBP** | $0 (DIY) | 30–60 days | Steady (long-term) | Claim "[City] AI solutions for contractors" GBP, embed booking link |
| 6 | **LinkedIn social selling** | $0 (or $80/mo Sales Nav) | 21–30 days | Medium | 50 connects/day to contractor owners → 60-sec Loom demo |
| 7 | **Reddit** (r/HVAC, r/sweatystartup) | $0 | 21–45 days | Low-med | Answer complaint threads with real advice; DMs only |
| 8 | **Nextdoor** | $0 organic (flagged often) / $10/day ads | 14–30 days | Low for B2B | Skip organic; only micro-budget zip-targeted ads |
| 9 | **Meta Ads (cheapest paid)** | $10–20/day ($300–600/mo) | 3–7 days | Moderate (CPL $40–80) | $150 test: "Free AI missed-call audit" → owners/GMs in HVAC/construction |

### Recommended 90-day plan ($300–$500 total)
- **Month 1 (~$150): Outbound velocity** — Instantly ($37) + 3 domains ($45) + dialer/Apollo buffer ($68). 100 emails/day + 30 calls/day in top 3 states. Goal: 5 discovery calls → 1 closed client ($1,000 + $750/mo).
- **Month 2 (~$150): Partnerships + community** — 15 supply-house visits, referral fees; 3 case-study posts/week in FB groups. Goal: 2 clients via referrals + DMs.
- **Month 3 (~$150): Paid retargeting** — Meta retargeting ($113 test) + email sequence refinement. Goal: $2,500–$3,500 MRR (cash-flow positive).

---

## 5. Implications for LeadSetter AI (action items)

1. **Lead with the math:** "$25 per qualified appointment lead — vs $50–228 on Google, vs shared $250–1000/booked on Angi."
2. **Product = inbound-first + confirmation engine.** Form-fill capture, instant AI follow-up (speed-to-lead), confirmation + reminders (cut 15–25% no-shows). Never cold-call homeowners without consent.
3. **Make compliance a marketing asset:** "FCC-compliant AI — we only call homeowners who asked to be called."
4. **Pitch against the status quo:** Angi receipts are the best sales tool. Ask "what did Angi cost you last year?" → math sells the swap.
5. **Execute the 90-day plan from Section 4.** Fastest revenue: cold email + cold calling + supply houses.

---

## Sources
1. https://searchlightdigital.io/what-is-a-good-cost-per-lead-for-hvac-google-ads/ (CPL benchmarks)
2. https://tradesmenguild.com/blog/angi-leads-reviews (Angi lead quality/costs)
3. https://schedulingkit.com/hub/industry-guides/average-no-show-rates-by-industry (no-shows)
4. https://www.thomastowndigital.com/home-services-marketing-statistics (market stats)
5. https://www.fcc.gov/ (TCPA & AI voice ruling)
6. Vendor pricing pages: Retell, Vapi, Bland.ai, GoHighLevel, Synthflow, Smith.ai, Ruby, Angi, Thumbtack, Yelp (fetched 2026-08-07)

*Unverified items flagged in text: done-for-you AI agency retainer range ($1.5K–5K/mo) is industry-standard estimate; marketplace CPL ranges vary by market/season.*
