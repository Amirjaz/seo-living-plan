# Brightside Dental — week 4 · 2026-11-15
blocked: site reachability. This workspace has no live site access, and brightsidedental.example is a placeholder domain, so DNS, registration/expiry and Googlebot (desktop + smartphone) on `/` and `/robots.txt` were not checked this week. No pass is claimed. Last seen in keyword session 11-12: DNS ok · expiry 2027-03-02 · Googlebot desktop `/` 200 · smartphone `/robots.txt` 200. Unblocks when you run the four checks (queue item 2), before applying either package.

**Alerts**
- **DROP: "dentist headingley" left the top 3**: 2.8 → 4.1 on 140 impressions, clicks 11 → 6 (11-07 → 11-13 vs 10-31 → 11-06). It was the only commercial top-3 query at baseline and earns 33 of the KPI's 60 clicks. The 28-day position is still 3.2, so this is one week on a small site. It's the KPI's main query, though, so its fix goes first.
- DROP (minor): "best dentist in leeds" 29.4 → 31.0 on 40 impressions, 0 clicks. That's normal movement at position 30, so no separate action.
- HEALTH: `/blog/composite-bonding-vs-veneers/` has returned 404 since 11-10 (keyword session 11-12). It had 64 impressions the week before and is missing from this week's pages export. The fix is packaged.
- Notification: this run has alerts and a blocked step. No notification channel is set up in this workspace, so they open this report.

**KPI** (GSC CSV exports in `data/2026-11-15/`. 11-14 excluded as incomplete: 143 impressions vs a 418 median. Windows in `windows.json`.)
- 7 d (11-07 → 11-13): 80 clicks · 2,997 impr · CTR 2.7 % · avg pos 16.0. Previous 7 d (10-31 → 11-06): 85 · 3,184 · 2.7 % · 16.0.
- 28 d (10-17 → 11-13): 339 clicks · 12,309 impr. Week 3: 331 / 12,150. Baseline (09-25 → 10-22): 312 / 10,940. The previous 28 days can't be computed because the daily export starts 10-16.
- **KPI, non-brand commercial clicks over 28 d: 60** (baseline 58, week 3 60, end-of-quarter target 85–115). 7 d: 14 (prev 17).
- Brand vs non-brand (7 d): brand query rows 47 clicks / 108 impr (prev 41 / 98); non-brand query rows 18 / 1,265 (prev 20 / 1,155); 15 clicks sit in anonymised queries. By page, the homepage has 49 of the 80 clicks. Over 28 d, brand query rows are 162 of 339 clicks (48 %, a floor).
- Indexed: unknown, because this week's exports don't include it (42 on 11-12).

**Scorecard** (the 8 baseline commercial keywords, 7 d 11-07 → 11-13, ± vs keyword session 11-12): top 3 1 (−1) · 4–10 2 (+1) · 11–20 3 (+1) · 21+/none 2 (−1) · weighted avg 15.2 (±0.0)
- Vs the first logged scorecard (week 2, 11-05): top 3 2 → 1 · 4–10 1 → 2 · 11–20 3 → 3 · 21+ 2 → 2 · avg 15.4 → 15.2. The quarter-start scorecard isn't recorded in the plan.
- Targets: top 3 2–4 · top 10 4–6. Now: 1 / 3.
- Moves: dentist headingley 2.8 → 4.1 (left the top 3); teeth whitening headingley 21.3 → 18.0 (on 15 impressions, too few to credit).

**Fail list** (tracked commercial, ≥ 20 impr/28 d, not top 3) · keyword · position · page · this week
1. dentist headingley · 4.1 · `/` · drop alert. Q1 of the message (Google duplicate removal + Doctify fix, both drafted and unsent for 18–21 days; L-009, L-024), plus the homepage snippet package (plan item, lever G). Dentist schema: skipped: owner facts needed. Unblocks on Q3, and no sooner than 14 d after the snippet's first crawl.
2. dental implants leeds · 7.1 · `/dental-implants-leeds/` · the title change is judged "worked". N4 section drafted from the real query "how long do dental implants take": your review first, then the clinical facts from the dentist. No site change this week.
3. veneers leeds · 11.2 · `/veneers/` · skipped: approval. The N3 FAQ waits for your review and `approved_by_dentist:`. The +28 verdict on the 10-20 change is due 11-18. Third week on the fail list, so the next lever is D (reviewer box with GDC number) in week 6.
4. cost of veneers uk · 24.5 · `/veneers/` · skipped: fact. A price range needs the dentist's written OK (proposal open since 11-05). Unblocks when Dr. Okafor gives a range.
5. best dentist in leeds · 31.0 · `/` · skipped: one change per page per 14 days (the homepage gets the snippet this week). Unblocks 14 d after the snippet's first crawl. Local signals via Q1.
6. invisalign headingley · 14.8 · `/invisalign/` · skipped: 14-day rule (last change 11-04, first crawl 11-05). Unblocks 11-19 with the +14 verdict.
7. teeth whitening headingley · 18.0 · `/teeth-whitening/` · skipped: approval. N2 has waited 20 days. Unblocks when Q2 = yes.
- Added to the tracker this week (they join the scorecard at the next check):
8. composite bonding leeds · 6.3 · `/blog/composite-bonding-vs-veneers/` (404) · 404 fix packaged. The push comes in week 5, once the URL resolves.
9. emergency dentist headingley · 19.2 · no page · skipped: fact. Whether the practice sees emergency patients is for the owner to say. See the 11-15 proposal.

**Watch**
- composite bonding leeds entered the top 10 (10.9 → 6.3 on 26 impressions). Volume is low, so it isn't credited (L-021), and which URL earned it is unknown while the post 404s.
- The `/dental-implants-leeds/` page average moved 10.9 → 10.1. That's a page average, so it's judged per query instead (L-004).
- No tracked keyword fell ≥ 3 positions.

**Verdicts**
- Implant title/H1 (10-12, first crawl 10-13), +28 → **worked**: 9.8 → 7.1 on 236 impr/28 d; CTR 1.4 → 3.8 %, but that's ≈ 3 → 9 clicks, so the CTR part carries little weight. Read on 10-17 → 11-13, the closest complete 28-day window. **The +28 was due 11-10 and was missed in week 3**: that run logged "none due".
- Veneers answer-first change (10-20): +28 due 11-18, next run. Invisalign links (11-04): +14 due 11-19, next run.

**Done**
- Measured on complete days and saved the windows to `data/2026-11-15/windows.json`. Updated the tracker, adding composite bonding leeds, emergency dentist headingley, and "how long do dental implants take" (info).
- Packaged both fixes, each logged in the Change log as "packaged 11-15":
  - the 404 fix (`seo/changes/2026-11-15-composite-bonding-404.md`)
  - the homepage title + description (`seo/changes/2026-11-15-homepage-snippet.md`)
- Drafted N4, the implant section (`seo/drafts/N4-implants-how-long.md`), with clinical facts left in brackets for the dentist. Drafted the Dentist schema + reviewer box spec (`seo/drafts/dentist-schema.md`), which is blocked on facts.
- Replaced three asks that had waited 18–21 days with one 3-question message to Dr. Okafor (below).
- Plan: 3 revisions, 2 new proposals, the week 4 log entry. Lessons: strengthened L-024, added L-025.

**Not done → moved / dropped**
- Dentist schema + reviewer box → moved to week 6. It needs owner facts, and the homepage is under the 14-day rule after this week's snippet change.
- Keyword session 11-12, action 2 ("address and hours exactly as on the second Google listing") → not done as written. Address and hours are facts and come only from the owner, and one Google listing still shows the old address. Asked as Q3 instead.
- Last week's queue: N2 approval and the listing sends have been carried for 3 weeks, so they're escalated in the message. N3 review is carried (2nd week).
- Root-canal booking link → stays in the improvement queue (#3).

**Your queue (85 of 180 min)**, most valuable first
1. **[week 3 carried]** Forward the message below to Dr. Okafor (5 min). It unblocks dentist headingley (the drop alert), teeth whitening headingley and the Dentist schema.
2. Run the four Googlebot checks in `site-checks.md` §1 (5 min). If any fails, fix that and apply nothing else this week.
3. Apply the 404 fix (`seo/changes/2026-11-15-composite-bonding-404.md`) (15 min). It protects the 64 impr/week the post had and "composite bonding leeds" (6.3).
4. Apply the homepage title + description (`seo/changes/2026-11-15-homepage-snippet.md`) (10 min). Record the current title and description in the package first.
5. Review N3, the veneers FAQ, and pass it to Dr. Okafor (15 min, carried 2nd week).
6. Review N4, the implant section, and pass it to Dr. Okafor (15 min).
7. When Q1 = yes: the practice manager sends the Google + Doctify corrections. Write the "sent on" dates in the plan's listings tracker (10 min).
8. After 3 and 4 are live: Request indexing once each for the kept composite-bonding URL and for `/` (5 min).
9. Export the `/dental-implants-leeds/` queries (last 3 months) into a new `data/` folder, so N4 only adds real questions (5 min).

**Message, ready to forward, to Dr. Hannah Okafor**

> Subject: Three yes/no questions for the website
>
> Dear Dr Okafor,
>
> Three website items are ready and only need a yes or no from you. A reply like "1 yes, 2 yes, 3 no" is all we need.
>
> 1. **Google and Doctify listings** (ready since 25 and 28 October, so 18–21 days): may the practice manager send both corrections this week? (a) Ask Google to remove the duplicate listing that still shows the old address. (b) Correct Doctify, which lists the practice under "orthodontist", and add the website link. For context, the practice's main local search, "dentist headingley", averaged about 3rd place last week and about 4th this week. **Yes / No**
> 2. **Teeth whitening page** (draft N2, waiting since 26 October, so 20 days): is it approved to go live as drafted? If not, one line on what to change is enough. **Yes / No**
> 3. **Address, phone and opening hours in the site's structured data** (the code Google reads): may we use them exactly as they appear on the website's Contact page? We won't copy them from Google, because one Google listing still shows the old address. **Yes / No**
>
> Thank you,
> [your name]

**Plan revisions** (3)
1. Week 4 split: the homepage snippet stays and the Dentist schema + reviewer box move to week 6. Evidence: the schema needs owner facts (keyword-watch/2026-11-12.md action 2 would have copied them from a Google listing, and one listing shows the old address). The homepage is also under the 14-day rule after the snippet change.
2. Week 5 re-scoped to composite bonding: confirm the 404 fix is live and crawled, name the owner page (lever B), then push. Evidence: "composite bonding leeds" 10.9 → 6.3 (26 impr/7 d, 90/28 d) while its page 404s (data/2026-11-15/; keyword-watch 11-12 health check).
3. Improvement queue refilled with N4, the implant "how long" section (990 impr/28 d at 12.7), and emergency dentist headingley (61 impr/28 d at 19.2; needs a fact).

**Proposals waiting for you**
- 11-05 · Veneers price range (open 10 days). "cost of veneers uk" is still at 820 impr/28 d and position 25.4. It needs the dentist's figures and written OK. It's left out of this week's message because the message is capped at 3 questions.
- 11-15 · Emergency appointments section for "emergency dentist headingley" (34 impr/7 d at 19.2). Only if the practice sees emergency patients, in Dr. Okafor's wording.
- 11-15 · KPI scope: keep the KPI on the 8 baseline keywords (60), or count newly tracked keywords too (62)? Adding keywords raises the KPI without any ranking change.

**Assumptions** (unattended run, no one to ask)
- The CSV exports carry no dates. I took queries/pages "cur" = 11-07 → 11-13, "prev" = 10-31 → 11-06 and "28d" = 10-17 → 11-13. "prev" matches the 11-12 keyword session's 10-31 → 11-06 figures exactly.
- Query → page links marked "inferred" (for example "how long do dental implants take" → the implant page) come from impression arithmetic. There's no query × page export.
- No `rivals.md` exists in this workspace, and the site rules don't list one, so rival facts came from `seo/keyword-watch/2026-11-12.md`.
- Scheduler: I couldn't check it from here. The 11-12 keyword session file exists, so that job ran. Please confirm both scheduled jobs (keyword session + weekly run) still exist.
- Nothing was sent to anyone and nothing on the site was changed. Changes are packages for you to apply, per the workspace rules.
