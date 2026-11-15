# Measurement

## Contents
1. Windows and the latest complete day
2. Totals, queries, pages, brand
3. Scorecard
4. Fail list and drop alerts
5. Change verdicts
6. Reading small sites
7. Month checkpoints

## 1. Windows and the latest complete day

Search Console data lags about 2 days. If a window ends on today − 1, the newest week looks like a drop.

- **Latest complete day:** the newest date in a daily read, *unless* its impressions are below 60 % of the median of the 7 days before it — then step back a day and check again. Usually it lands on today − 2.
- **Weekly window:** the 7 days ending on the latest complete day, compared with the 7 days before.
- **KPI window:** 28 days ending on the latest complete day (and the 28 before, when the KPI compares).
- Always pass explicit dates. Relative presets ("last 7 days") shift with the lag.

`python scripts/gsc_compare.py window --daily <daily.csv|json>` does this.

## 2. Totals, queries, pages, brand

- **Property totals** come from a read with no query or page dimension (or the sum of daily rows). Summing query rows undercounts: anonymised queries are missing from query tables, and on name-heavy sites they can be most of the clicks.
- **Queries and pages** per window: query or page plus clicks, impressions, CTR, position. Read them unfiltered unless the property is huge; if you filter (e.g. impressions ≥ 10), say so — a row missing from a filtered read means "below the filter", not "zero".
- **Brand vs non-brand:** use the plan's brand terms (name spellings, the owner's name, transliterations). Split by query *and* by page (home, about, contact count as brand pages) because brand searches hide in anonymised queries. On a brand-heavy site, click totals mostly measure brand demand — never call a week good or bad from totals alone.
- Mark the source on every number: "GSC API, 3–9 Nov vs 27 Oct–2 Nov".

## 3. Scorecard

Computed from `keyword-tracker.md` for the **tracked commercial set** — keywords with intent buy / booking / patient / lead (not info, not brand):

- count in the top 3, at 4–10, at 11–20, at 21+ or not ranking;
- the impression-weighted average position of the set;
- each with the change since the previous check and since the quarter start.

The plan's Ranking strategy sets targets for the top-3 and top-10 counts. `gsc_compare.py compare --tracked keywords.txt` prints it.

## 4. Fail list and drop alerts

A plan can adopt "top 3 is the standard" (most do, because positions 4+ get a small share of clicks):

- **Fail list:** every tracked commercial keyword with ≥ 20 impressions in 28 days that is *not* in the top 3 (7-day position ≥ 3.5, or below #3 in a live check). The report lists each first: keyword · position · owner page · this week's action — or `skipped: <rule>; unblocks when <action>`.
- **Drop alert:** a tracked keyword that leaves the top 3, or falls ≥ 0.5 positions (≥ 1 live position) on ≥ 20 impressions. Top of the report, a notification, and its fix goes first in the week's work order.
- What blocks a fail-list item (an approval, a fact only the owner has) goes first in the human's queue as a yes/no question naming the keyword it unblocks.
- A fail carried 3 weeks running is escalated with a different lever (`ranking-playbook.md` C–E), not the same change again.

## 5. Change verdicts

Every site change has a Change log row with a **28-day baseline** on its target keywords and rechecks at **+14 and +28 days** (counted from the first crawl after the change). At each recheck, on the target keywords:

| Verdict | Condition |
|---|---|
| **worked** | ≥ 2 positions better, **or** CTR up ≥ 30 % (relative) at a similar position (±1) |
| **no effect** | within those bounds |
| **worse** | ≥ 3 positions worse, **or** CTR down ≥ 30 % at a similar position — on ≥ 50 impressions → revert or rethink, as the site's rules allow |

Below 50 impressions, a "worse" reading is recorded as "worse (low volume — confirm at +28)" rather than acted on. The +28 verdict is the one that counts; +14 is an early read.

When a verdict rests on a handful of clicks (under ~20 in either window), say so next to it — e.g. "worked (CTR +58 %, but ≈ 8 → 13 clicks)" — and confirm it at the next recheck or with the per-query numbers. The table decides the label; the click count tells the reader how much weight it carries.

`python scripts/gsc_compare.py verdict --base-pos P --base-ctr C --new-pos P2 --new-ctr C2 --impressions N` applies the table.

Before judging, check:
- Was the page crawled after the change? If a refused indexing request left it uncrawled, any movement has nothing to do with the change.
- Did something site-wide happen in the window (an outage, a core update, a migration)? Then say the verdict is confounded.
- Did the page's average move because new queries joined? Judge the target keywords, not the page average.

## 6. Reading small sites

- Sites with a few hundred impressions a day are noisy. Lead with impressions, like-for-like position and the watch list; don't narrate click swings.
- A one-week jump of 10+ positions on a low-impression query, with no change to the page, often reverts the next week. Don't credit it or re-plan on it; use 28 days.
- When a query falls, split it by page first: two URLs sharing a query can make it look like a drop while the owner page holds.
- A page's impressions can come from a different meaning of its keyword (a shared acronym, a namesake). Read the page's own queries before treating impressions as demand.

## 7. Month checkpoints

At the end of months 1, 2 and 3 of the quarter, recalibrate the plan's expected ranges from measured data. Write the old range, the new one, and the arithmetic. Never edit a missed target to look met — it stays recorded as missed.
