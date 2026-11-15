# Weekly run — step by step

Run every step in order. Steps that need data you can't get follow rule 7 in SKILL.md (write `blocked:`, keep going with the rest).

## 1. Read

In this order, because each one changes what the next one means:

1. The site's own rules (a `CLAUDE.md`, `AGENTS.md` or rules file in the workspace). They win over this skill.
2. The plan file — above all its **Ranking strategy** section and this week's row.
3. `lessons.md` — entries for `all` and for this site's type.
4. The newest **keyword session** report. Its "Actions for the weekly run" are your top candidates for this week.
5. `keyword-tracker.md` and `rivals.md`.
6. The plan's last two Weekly log entries, open Proposals, and the Change log.

## 2. Find the week

From today's date and the plan's week table.
- **Before the quarter starts:** if the start is ≤ 7 days away, prepare week 1's agent-side work so it starts ready; otherwise log "quarter not started" and stop.
- **After the quarter ends:** write the end-of-quarter measurement (§3 with the whole quarter as the window, against the baseline) and propose the next quarter's plan. Change nothing else.

## 3. Check and measure

1. **Site reachability** (`site-checks.md` §1). Any alert → it becomes work-order item (a), it goes first in the report and the human's queue, and this run makes no other site change.
2. **Search Console numbers** (`measurement.md`): the 7 complete days ending on the latest complete day vs the 7 before, plus 28-day totals for the KPI. Read totals, the queries table, the pages table, and indexed / not-indexed counts if available.
3. Split brand vs non-brand using the plan's brand terms.
4. Save the raw rows in a new dated folder under the site's data folder.
5. Update `keyword-tracker.md` positions, compute the **Scorecard** and the **Fail list** (`measurement.md` §3–4).
6. Flag (WATCH): a page that lost > 50 % of its impressions (≥ 20 before); a tracked keyword that fell ≥ 3 positions (≥ 20 impressions); a page published in the last 6 weeks with 0 impressions; the indexed count dropping for a reason that isn't a planned removal; a new query entering the top 3 or top 10.

If measurement is blocked, use the latest keyword session's numbers labelled with their date. Never estimate.

## 4. Judge past changes

For every Change log row whose +14 or +28 day recheck date has passed — including any a previous run should have judged and didn't (say so in the log: "+28 was due <date>, missed in week N") — confirm the page was crawled after the change (URL Inspection "last crawl" if you can see it — a change Google hasn't fetched can't have caused anything), read that page's numbers for the target keywords, and write the verdict (`measurement.md` §5). A clearly worse change is reverted only where the site's rules allow it; otherwise it goes to the human's queue with the evidence.

Three or more verdicts on changes of the same kind → that pattern becomes a lesson (step 10).

## 5. Do the week's work

Only what the plan's autonomy level allows. Work order:

- **(a)** Anything broken that costs traffic now — reachability alerts, health findings from the keyword session, a dropped page, a drop alert on a tracked keyword.
- **(b)** Push-zone work on 1–3 keywords (`ranking-playbook.md` lever A).
- **(c)** The plan's item for this week.
- **(d)** The recurring items the plan defines (e.g. one new page or brief a week, one off-site item a week).

Anything that needs the human or the client becomes a queue item with a minute estimate. Log every site change in the Change log, with its baseline, the moment you make it.

Respect the one-change-per-page-per-14-days rule. When it blocks the obvious action on a fail-list keyword, write "skipped: 14-day rule (last change <date>); unblocks <date>" and pick a different lever or page.

## 6. Indexing requests

Only where the plan allows it. New or changed URLs first. Search Console allows roughly 5–6 manual requests a day per property, and a repeated request burns a slot without moving the URL up — so at most 5 a day, never the same URL within 14 days, and log each one. If a request is refused (quota, or a permission guard on an unattended run), make it a queue item with the URL list.

## 7. Carry the leftovers

Every unfinished item from last week is done, moved (log where) or dropped (log why) — never silently. An item carried 3 weeks running goes to the top of the human's queue marked "week 3 carried". A fail-list keyword carried 3 weeks gets a *different* lever, not the same change again.

Before calling anything "waiting for approval", search the site's files (and recent conversation history, if you can) for an approval that never reached the file. Approvals that stall in chat are a common failure.

## 8. Log the week

Write the Weekly log entry (format in `plan-template.md`). Facts only; link the data folder.

## 9. Improve the plan

At most 3 revisions, each in the Plan revisions table with its evidence. What a run may change on its own vs must propose: `plan-template.md` "Revising the plan". At month checkpoints (end of months 1, 2, 3) recalibrate expected ranges from measured data: write the old range, the new one and the arithmetic. A missed target stays recorded as missed.

## 10. Learn

Add or update at most 2 lessons in `lessons.md` (rules in SKILL.md rule 8).

## 11. Report

The weekly report (format in SKILL.md). Send a notification only for an alert or a blocked step — a quiet week is silent.
