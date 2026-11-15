# Hearth & Crumb — SEO plan, Winter 2026–27 (2026-12-01 → 2027-03-01)

13 weeks, Gregorian calendar, each week Tuesday → Monday. Written 2026-11-15 (setup run). Companion files in this folder: `keyword-tracker.md`, `rivals.md`, `lessons.md`, `data/2026-11-15/` (baseline rows and checks).

## Decisions
- **Site type:** `local-business` — one bakery in East Austin, TX (hearthandcrumb.example).
- **KPI:** non-brand commercial clicks, 28 days (GSC query rows that contain no brand term and are not `info` intent). **Baseline 51 clicks on 7,530 impressions** (GSC CSV `queries-28d.csv`, window assumed 2026-10-17 → 2026-11-13). Chosen by the setup run because no KPI was given — confirm or replace (Proposal P3).
- **Human time budget:** 2 h/week (120 min) for you, the SEO lead. Maya's time is not budgeted: she gets at most one message of ≤ 3 yes/no questions at a time (FL-24), and none 2026-12-15 → 2027-01-01 (assumed holiday rush).
- **Autonomy: drafts + non-fact fixes.** Runs may change on their own: titles, meta descriptions, H1s, internal links, alt text, schema (non-fact properties). Runs draft and you approve before publishing: new body copy, FAQs, new pages, profile/listing edits, outreach. Maya must confirm in writing first: **prices, hours, ingredients / allergens / dietary claims**, plus any other fact (products offered, order lead times, address or phone changes).
- **Brand terms:** hearth and crumb · hearth & crumb · hearthandcrumb · hearth n crumb · Maya + surname (surname unknown — add when known; "maya" alone is too ambiguous to match). Brand pages: `/`, `/about`, `/contact` (and `/menu` partly).
- **Facts owner:** Maya (owner). You send her the ready-to-forward message; her answers are recorded with her words and the date in Proposals.
- **Data source:** GSC CSV exports by you (daily, queries, pages), always with explicit date ranges. A connector/API is proposed (P1).
- **Indexing requests:** a human item, ≤ 5 URLs/day, never the same URL within 14 days (FL-01, FL-15).
- **Schedule (suggested):** weekly run every Tuesday (first 2026-12-01); keyword session every Saturday (first 2026-11-28). Each weekly run confirms both jobs still exist (FL-12) and judges other jobs by the file they wrote (FL-13).

## Baseline (GSC CSV exports 2026-09-18 → 2026-11-14; saved in `data/2026-11-15/`)
- **Latest complete day 2026-11-13** — 2026-11-14 had 141 impressions vs a 390 median, so it was dropped (FL-02; `window.json`).
- **28 d (2026-10-17 → 11-13):** 348 clicks · 10,418 impr · CTR 3.34 % · avg pos 14.4. Prior 28 d (09-19 → 10-16): 335 · 9,735 · 3.44 % · 14.5 → clicks +3.9 %, impressions +7.0 %.
- **7 d (11-07 → 11-13):** 92 clicks · 2,772 impr vs 83 · 2,483 the 7 days before. Weekly impressions rose steadily over 8 weeks (2,282 → 2,772). Weekends run ~17 % above weekdays (401 vs 343 impr/day).
- **Brand / non-brand (query rows, 28 d):** brand 203 clicks / 710 impr (4 queries at #1.0–1.3) · non-brand 54 / 8,840 (commercial 51 / 7,530; info 3 / 1,310) · not in query rows (anonymised) 91 / 868, probably mostly brand (FL-04, not verifiable). By page: `/`, `/about`, `/contact` = 250 of 327 page-row clicks (76 %).
- **Pages (28 d, clicks · impr · pos):** `/` 230 · 2,400 · 9.8 (brand at ~1.1 mixed with generic queries — judge per query, FL-03) · `/bread/sourdough` 14 · 1,300 · 8.0 · `/blog/feed-sourdough-starter` 3 · 1,350 · 20.1 · `/cakes` 4 · 1,100 · 18.9 · `/menu` 40 · 900 · 5.1 · `/pastries` 12 · 900 · 8.4 · `/cakes/custom` 1 · 420 · 23.5 · `/gluten-free` 3 · 310 · 10.2 · `/about` 9 · 160 · 3.4 · `/contact` 11 · 120 · 2.2.
- **Indexed / not indexed:** unknown — not in the exports (week 1).
- **Reachability:** **blocked** — `hearthandcrumb.example` returns NXDOMAIN, and `.example` is a reserved name that never resolves, so it is a placeholder for the live domain. Registration: not checkable (no RDAP for `.example`). Googlebot desktop/smartphone on `/` and `/robots.txt`: could not resolve. Rerun on the live domain before any site change (`data/2026-11-15/reachability.txt`).

## Ranking strategy
Profile: a small, steadily growing local site (~370 impressions and ~12 clicks a day). Clicks are mostly brand, but 93 % of visible impressions are non-brand. The demand is there and the site isn't converting it: non-brand commercial CTR is 0.68 % because most commercial queries sit at positions 6–41. The product pages already reach page 1 for sourdough, croissants, kolaches and gluten-free (4.8–9.7), and the site is at 2.9 for "bakery east austin". The gaps are cakes (17.5–41.2), the map-pack query "bakery near me" (34.0) and the "best bakery austin" list SERP (12.8).

1. **A — Push zone on product pages.** Evidence: 8 commercial queries at 4–15 with ≥ 20 impressions (`compare-queries-baseline.txt`): sourdough bread austin 820 @ 6.4 → `/bread/sourdough`; croissants 540 @ 8.9, kolaches 260 @ 4.8, pastry shop 120 @ 11.2, cinnamon rolls 95 @ 7.2 → `/pastries` (895 of its 900 impr). On this site a keyword at 4.8 gets 2.7 % CTR and one at 6.4–9.7 gets 1.0–1.1 %, so each position gained near the top counts. Titles and snippets (lever G) are part of each change. Targets: those 5 keywords, plus gluten free bakery austin 290 @ 9.7 (structure only until Maya confirms the wording).
2. **C — Local and entity signals.** Evidence: "bakery near me" is the biggest non-brand query (2,100 impr, 22 % of visible impressions) at 34.0. It is answered by the map pack, which GSC doesn't show. Every commercial query carries "austin" or "east austin". FL-09: unmanaged profiles outrank sites. Targets: Google Business Profile verified, category "Bakery", site and menu links, hours = what Maya confirms; identical name, address and phone everywhere; existing profiles claimed and corrected; reviews only from real customers asked directly. "best bakery austin" (1,450 @ 12.8) goes here too: if the first keyword session confirms list pages hold its top 10, the lever is a factual note to those editors. No paid placements.
3. **B — One owner per query: cakes.** Evidence: `/cakes` (1,100 @ 18.9) and `/cakes/custom` (420 @ 23.5) both carry cake queries: birthday cakes austin 610 @ 17.5, custom cakes austin 380 @ 22.4, wedding cake austin 340 @ 41.2. The split is inferred from totals; a query × page read confirms it in week 4. Targets: `/cakes` owns birthday cakes; `/cakes/custom` owns custom cakes (and wedding cakes, if Maya confirms). Link both ways first, and decide anything bigger on 28-day numbers (FL-11).
4. **F — Crawl and index.** Evidence: none yet (no indexing counts). This becomes a lever only if week 1's Page indexing read shows gaps.

Not used: E (no page at 50+; the deepest is 41.2), D (not YMYL, but allergen wording is treated as facts-only), H (no online shop known).

**Never** (site rules — runs propose, don't change):
- No price, hours, ingredient, allergen or dietary wording ("gluten-free", "nut-free", "vegan", "celiac-safe", "dedicated kitchen") anywhere without Maya's written yes. That covers page copy, titles, FAQs, alt text, schema (`priceRange`, `openingHoursSpecification`, `Offer.price`, `suitableForDiet`) and listings.
- No claim about what the bakery offers (wedding cakes, delivery, coffee/seating, catering, seasonal items, order lead times) until Maya confirms it.
- Name, address and phone are copied word for word from the site's contact page. Any mismatch with a listing goes to Maya; we don't pick one.
- No area/city doorway pages ("bakery in Round Rock", "South Austin bakery"): there is one shop, in East Austin.
- Reviews only from real customers asked directly. No incentives, no filtering for happy customers, no staff or friend reviews.
- No "best bakery in Austin" self-description in titles or copy. Describe what's sold.
- The brand stays first in the home page title (brand queries are ~58 % of clicks, at #1.1).
- No copying rival menus, text or photos. Own photos only, with alt text that describes the actual item.

**Targets (end of quarter, 28 d ending on the latest complete day of week 13):**
- **Top 3: 2–4** (now 1). Arithmetic: bakery east austin (2.9) holds, plus 1–3 of the three keywords at 4.8–7.2 (kolaches, sourdough, cinnamon rolls) that get changes in weeks 1–2.
- **Top 10: 6–9** (now 6). Arithmetic: the 6 hold, plus 0–3 of pastry shop 11.2, best bakery 12.8 and coffee shop east austin 14.1 (only if Maya confirms coffee). Birthday cakes 17.5 is upside.
- **KPI: 55–80 non-brand commercial clicks / 28 d** (now 51). Arithmetic uses this site's own CTR at each position (2.9 → 5.7 %, 4.8 → 2.7 %, 6.4–9.7 → 1.0–1.1 %, 11–22 → 0.3–0.8 %): kolaches 4.8 → top 3 ≈ +8; sourdough 6.4 → ~4.8 ≈ +13; croissants 8.9 → ~6 ≈ +5; birthday cakes 17.5 → ~10 ≈ +4. All four ≈ +30 (→ ~81). One or two of them ≈ +5 to +20 (→ 56–71).
- No seasonal adjustment yet: Dec–Feb demand vs Oct–Nov is unknown until the year-ago export arrives. Recalibrate at the month-1 checkpoint. These are planning ranges, not promises: Google decides positions.

## Weeks
One main item per week. Fixes and push-zone work come first. Minutes are yours (the SEO lead). "Export 10" means the weekly GSC CSV export; it drops to 0 if P1 (connector) is approved. Planned load is 30–75 min a week; the rest of the 120 is buffer for Maya follow-ups and approvals.

| Week | Dates | Main item | Human minutes | Status |
|---|---|---|---|---|
| 0 (pre-quarter) | 2026-11-16 → 11-30 | Send Maya message #1 (below) before the holiday rush. Tell the runs the live domain and how they edit the site (P2). Export year-ago data, 2025-11-01 → 2026-03-01 daily + queries, for seasonality. A run on or after 11-24 drafts week 1's copy so week 1 starts ready. | Maya msg 5 · domain/access 10 · year-ago export 10 · P1/P3 decisions 5 = **30** | planned |
| 1 | 12-01 → 12-07 | Reachability on the live domain, the first 7-day read, indexing counts and a query × page read. **Push-zone change #1: `/bread/sourdough`** (sourdough bread austin 820 @ 6.4): title/H1 in the query's wording, answer-first intro, H2s from real queries, alt text, plus a contextual link from `/blog/feed-sourdough-starter` (1,350 impr). | Google Business Profile audit (owner, verification, category "Bakery", site + menu links; hours untouched until Maya's Q1) 30 · review copy 15 · export 10 · indexing 5 = **60** | planned |
| 2 | 12-08 → 12-14 | **Push-zone change #2: `/pastries`** (croissants 540 @ 8.9, kolaches 260 @ 4.8, pastry shop 120 @ 11.2, cinnamon rolls 95 @ 7.2): title naming croissants + kolaches, one H2 per pastry already on the page, alt text, plus a link from `/menu` (900 impr). | Claim/correct the 2 most important profiles from the keyword session 45 · review copy 15 · export 10 · indexing 5 = **75** | planned |
| 3 | 12-15 → 12-21 | **Home `/`:** title/meta with the brand first plus "East Austin bakery" (keeps bakery east austin 2.9, aims at best bakery austin 12.8); descriptive links to `/bread/sourdough`, `/pastries`, `/cakes`, `/gluten-free`; `Bakery` schema (name, URL, logo, address/phone as published, `hasMenu` URL, `sameAs` claimed profiles; `openingHoursSpecification` only after Maya's Q1 yes). Early +14 read on sourdough. | Review home title 10 · check the profile's hours match Maya's answer 10 · export 10 · indexing 5 = **35** | planned |
| 4 | 12-22 → 12-28 | Light week (Christmas). **`/gluten-free`:** structure, alt text and breadcrumb only, re-ordering the existing wording if Maya's Q2 is yes; if no or no answer → skipped: fact rule, unblocks when Maya answers. Early +14 read on `/pastries`. | Query × page export for `/cakes` and `/cakes/custom` 10 · review 5 · export 10 · indexing 5 = **30** | planned |
| 5 | 12-29 → 2027-01-04 | **Month-1 checkpoint** (recalibrate targets with the year-ago data) + sourdough +28 verdict. **`/cakes` owner change:** `/cakes` owns birthday cakes austin (610 @ 17.5); title/H1/intro for birthday cakes, H2s from real queries, alt text, links `/cakes` ↔ `/cakes/custom`. No prices or lead times (they wait on message #2). | Checkpoint review 15 · review copy 15 · check message #2 5 · export 10 · indexing 5 = **50** | planned |
| 6 | 01-05 → 01-11 | **Send Maya message #2** (01-05). **"best bakery austin" list pages:** a short factual note from you to the editors of 2–3 list pages the keyword sessions found (list pages often refresh in January). `/pastries` +28 verdict. | Send msg 5 · editor notes (agent-drafted) 45 · export 10 = **60** | planned |
| 7 | 01-12 → 01-18 | **Valentine's pre-order page/section**, only if Maya says yes in message #2 and gives the items, prices and order deadline (P4). Live by 01-18 so it is crawled well before 02-14, and linked from `/` and `/cakes`. If no → swap in Improvement queue #1. Home +28 verdict. | Review page 20 · indexing 5 · export 10 = **35** | conditional (P4) |
| 8 | 01-19 → 01-25 | **`/cakes/custom` push** (custom cakes austin 380 @ 22.4): title, "How to order" H2, FAQ from real queries; starting price and lead time only if message #2 says yes; a wedding-cakes section only if message #1 Q3 is yes (wedding cake austin 340 @ 41.2). `/gluten-free` +28 verdict. | Review copy 20 · indexing 5 · export 10 = **35** | planned |
| 9 | 01-26 → 02-01 | **Month-2 checkpoint** + `/cakes` +28 verdict. **Escalation slot:** the fail-list keyword carried longest gets a *different* lever (C or B), not the same change again. | Checkpoint review 15 · review 15 · export 10 = **40** | planned |
| 10 | 02-02 → 02-08 | **Profiles round 2:** claim/correct the remaining profiles (Apple Maps, Bing Places, Yelp, Tripadvisor, delivery apps). Name, address and phone must match the site everywhere. | Claims 45 · export 10 · indexing 5 = **60** | planned |
| 11 | 02-09 → 02-15 | Valentine's week, so no edits to the Valentine's page. **Flex slot:** Improvement queue #1 as refilled by the runs from evidence. `/cakes/custom` +14 read. | Review 15 · export 10 · indexing 5 = **30** | flex |
| 12 | 02-16 → 02-22 | **Maya message #3** (delivery? review card? spring/Easter 2027-03-28 items?) + draft next quarter's seasonal proposal. `/cakes/custom` +28 verdict. | Send msg 5 · review proposal 15 · export 10 = **30** | planned |
| 13 | 02-23 → 03-01 | **End of quarter:** whole-quarter measurement against the baseline, month-3 checkpoint, final verdicts, and next quarter's plan as a proposal. | Review 30 · export 10 = **40** | planned |

**Page change calendar** (one change per page per 14 days; the clock starts at the first crawl after the change, FL-26): `/bread/sourdough` W1 (+14 ≈ W3, +28 ≈ W5) · `/blog/feed-sourdough-starter` W1 (link only) · `/pastries` + `/menu` link W2 (+14 W4, +28 W6) · `/` W3 (+14 W5, +28 W7) · `/gluten-free` W4 (+14 W6, +28 W8) · `/cakes` W5 (+14 W7, +28 W9) · Valentine's page W7 (new: judge by impressions) · `/cakes/custom` W8 (+14 W10, +28 W12). Pages under measurement are not touched again before their +28 read unless a drop alert forces it. Verdicts on December changes may be confounded by holiday demand, so judge them on per-keyword position more than on CTR.

## Improvement queue
Ranked. Runs refill it from evidence (position · 28-d impressions · page).
1. `/bread/sourdough`: sourdough bread austin 6.4 · 820. Week 1.
2. `/pastries`: croissants 8.9 · 540, kolaches 4.8 · 260, pastry shop 11.2 · 120, cinnamon rolls 7.2 · 95. Week 2.
3. Google Business Profile + profiles: bakery near me 34.0 · 2,100 (map pack). Weeks 1, 2, 10.
4. `/`: best bakery austin 12.8 · 1,450; bakery east austin 2.9 · 140. Week 3 on-page, week 6 list pages.
5. `/cakes`: birthday cakes austin 17.5 · 610. Week 5.
6. `/gluten-free`: 9.7 · 290. Week 4, fact-gated (Maya Q2).
7. `/cakes/custom`: custom cakes 22.4 · 380; wedding cake 41.2 · 340. Week 8, fact-gated (messages #1 Q3 and #2).
8. Coffee: coffee shop east austin 14.1 · 300. Fact-gated (message #2): if yes, home/about wording plus schema `servesCuisine`/amenities; if no, retire.
9. `/blog/feed-sourdough-starter`: info queries 18.3–25.0 · 1,310. Answer-first rewrite only if a slot frees up (not KPI).
10. Delivery: bread delivery austin 19.6 · 85. Fact-gated (message #3); retire if no.

## Listings & links tracker
| Item | Platform | Drafted | Sent on | Status |
|---|---|---|---|---|
| Maya message #1 (hours · gluten-free page · wedding cakes) | email/text from you | 2026-11-15 | — | waiting for you to send (ideally before 12-01) |
| Google Business Profile check (owner, category, links) | Google | — | — | week 1 |
| Existing profiles: claim & correct (top 2) | from keyword session | — | — | week 2 |
| "best bakery austin" list-page notes (2–3 editors) | list/guide sites found by keyword session | — | — | week 6 |
| Maya message #2 (custom-cake price & lead time · Valentine's · coffee) | email/text from you | — | — | week 6 (send 01-05) |
| Remaining profiles: claim & correct | Apple Maps, Bing Places, Yelp, Tripadvisor, delivery apps | — | — | week 10 |
| Maya message #3 | email/text from you | — | — | week 12 |

### Ready to send — Maya message #1 (drafted 2026-11-15, all three items new)
> Hi Maya, three quick yes/no questions so I can fix the website and your Google listing before the holiday rush. A Y or N on each is enough (add a correction if it's a no):
> 1. Are the opening hours on the website's contact page right for December, holiday closures included? (If not, what are they?)
> 2. Is everything on the gluten-free page still accurate? I'd only reorganise it and add links, with no new claims.
> 3. Do you make wedding cakes, and is it OK to say so on the cakes page?
> Thanks!

## Weekly log
### Week 0 · 2026-11-15 — setup run
- blocked: reachability — `hearthandcrumb.example` is a reserved `.example` name that never resolves (NXDOMAIN). Unblocks when you give the live domain (P2); week 1 reruns all four checks before any change.
- KPI baseline: non-brand commercial 51 clicks / 7,530 impr (28 d, assumed 2026-10-17 → 11-13, query CSV). Property 348 clicks / 10,418 impr (28 d, daily CSV); 7 d 92 / 2,772 (11-07 → 11-13) vs 83 / 2,483. Brand 203 / 710 · non-brand 54 / 8,840 · anonymised 91 / 868. Indexed: unknown. Source: `data/2026-11-15/`.
- Scorecard (28-d baseline, 14 tracked): top 3 1 · 4–10 5 · 11–20 5 · 21+/none 3 · weighted avg 19.34 (no previous check).
- Fail list (13 of 14; all but bakery east austin 2.9), each with its action:
  - bakery near me 34.0 · 2,100 → W1–2 profiles
  - best bakery austin 12.8 · 1,450 → W3 home, W6 list pages
  - sourdough bread austin 6.4 · 820 → W1
  - birthday cakes austin 17.5 · 610 → W5
  - croissants austin 8.9 · 540 → W2
  - custom cakes austin 22.4 · 380 → W8
  - wedding cake austin 41.2 · 340 → skipped: fact rule; unblocks when Maya answers #1 Q3
  - coffee shop east austin 14.1 · 300 → skipped: fact rule; unblocks with message #2
  - gluten free bakery austin 9.7 · 290 → W4, wording gated by #1 Q2
  - kolaches austin 4.8 · 260 → W2
  - pastry shop austin 11.2 · 120 → W2
  - cinnamon rolls austin 7.2 · 95 → W2
  - bread delivery austin 19.6 · 85 → skipped: fact rule; unblocks with message #3
- Done: baseline saved (`data/2026-11-15/`); plan, `keyword-tracker.md`, `rivals.md` and `lessons.md` (seeded from the field lessons) created; Maya message #1 drafted.
- Not done → moved: rival/SERP check → first keyword session (11-28); indexing counts and query × page mapping → week 1 (not in the exports).
- Verdicts: none (no changes yet).
- Human queue: Maya message #1 5 · live domain + edit access 10 · year-ago export 10 · decide P1/P3 5 — total 30 of 120 min.

## Change log
No site changes at setup.

| date | page | change | target keyword(s) | baseline (pos · impr · CTR, 28 d) | recheck 14 d | recheck 28 d | verdict |
|---|---|---|---|---|---|---|---|

## Plan revisions
| date | week | what changed | why (evidence / lesson) |
|---|---|---|---|
| 2026-11-15 | setup | Plan created | Baseline `data/2026-11-15/` (window.json, compare-queries-baseline.txt); FL-02, FL-03, FL-04, FL-09, FL-24 |

## Proposals
| date | proposal | why | status (open / approved <date> / declined <date>) |
|---|---|---|---|
| 2026-11-15 | P1 — Give the weekly runs read access to Search Console (connector or API) instead of weekly CSV exports. | CSV exports cost ~10 of your 120 min every week (~130 min a quarter) and can't do query × page reads without extra exports | open |
| 2026-11-15 | P2 — Confirm the live domain and whether runs edit the site directly (CMS access) or hand you changes as drafts. | Reachability check blocked (`data/2026-11-15/reachability.txt`); the autonomy level assumes runs can make non-fact fixes | open |
| 2026-11-15 | P3 — Confirm the KPI: non-brand commercial clicks / 28 d (baseline 51). Or replace it with a business number if Maya tracks one (cake inquiries, calls). | No KPI was given; brand clicks (203 of 257 visible) mostly measure existing demand (FL-04) | open |
| 2026-11-15 | P4 — Valentine's pre-order page in week 7, built only from Maya's items, prices and order deadline. | Seasonal demand is inferred, with no GSC evidence yet; the keyword session checks Valentine's queries in early January. Facts rule applies | open |
| 2026-11-15 | P5 — A "review us on Google" card at the counter or a link on receipts, offered to every customer (no incentives, no filtering). This is Maya's call. | "bakery near me" (2,100 impr @ 34.0) is a map-pack query where reviews are one input. Inferred, not measured | open |
