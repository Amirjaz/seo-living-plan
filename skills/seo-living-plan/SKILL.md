---
name: seo-living-plan
description: Run a site's SEO as a living quarterly plan that improves itself every week — one plan file with a ranking strategy, a weekly log, a change log where every edit is re-measured after 14 and 28 days, evidence-backed plan revisions, and a lessons file shared across sites. Use this whenever someone wants to set up or keep running an ongoing SEO plan, do the weekly SEO check-in for a site or client, decide what SEO work to do this week, judge whether a past SEO change worked, track keywords and competitors mid-week, or manage SEO for several client sites on a schedule — even if they never say "living plan". For a one-off audit with no ongoing plan, a plain audit skill fits better.
license: MIT
metadata:
  version: "1.0.0"
---

# SEO living plan

Ongoing SEO fails in predictable ways: changes nobody re-measures, wins credited to one noisy week, the same trap rediscovered on every site, finished drafts that never get sent, and a plan written in month one that never changes. This skill runs SEO as a **living plan** — a file that every run reads, measures against, acts on within agreed limits, logs into, and improves — so each week starts from evidence instead of memory.

## The files

Per site (keep them together in the site's workspace; ask where they live if you can't find them):

| File | What it holds |
|---|---|
| **Plan file** (e.g. `seo/plan-<quarter>.md`) | Decisions, KPI, time budget, autonomy level, ranking strategy, the week-by-week table, and at the bottom: Weekly log · Change log · Plan revisions · Proposals |
| `keyword-tracker.md` | Tracked keywords: intent, target page, position, previous check, impressions, status, next action |
| `rivals.md` | Main competitors, which keywords they beat you on, and what their ranking pages have |
| `keyword-watch/<YYYY-MM-DD>.md` | Mid-week keyword session reports |
| `data/<YYYY-MM-DD>/` | Raw Search Console rows per run — append-only, never overwritten |

Shared across all sites: **`lessons.md`** — what happened on one site that is likely to hold on others. Templates for the tracker, rivals and lessons files are in `assets/`. Market specifics (e.g. Iran, where Google Business Profile isn't available) are in `references/regional-notes.md`.

## Pick the mode

| The user wants… | Do this |
|---|---|
| A plan for a new site, or the next quarter | **Set up** — read `references/plan-template.md`, build the plan from real data |
| The weekly check-in / "run this week's SEO" | **Weekly run** — follow `references/weekly-run.md` step by step |
| A keyword, competitor and health check between weekly runs | **Keyword session** — follow `references/keyword-session.md` |
| To know if a change worked | Use the verdict rules in `references/measurement.md` §5 (or `scripts/gsc_compare.py verdict`), then log the verdict in the Change log |
| To record something learned | Add, strengthen or dispute a lesson (rules below) |
| "What should I work on this week?" | Read the plan's Ranking strategy and this week's row, then apply the work order in `references/weekly-run.md` step 5 |

If no plan exists yet and the user asks for a weekly run, say so and offer to set one up first — a weekly run without a plan has nothing to measure against.

## Rules for every mode

These carry the method. Each exists because skipping it produced a wrong call on a real site.

**1. Check the site is reachable the way Google sees it — first thing in every run** (setup, weekly run, keyword session; for a quick question like "did this change work?", just remind the user to check before publishing). DNS, registration status and expiry, and an HTTP 200 for `/` and `/robots.txt` with a *Googlebot* user agent (desktop and smartphone). A browser getting 200 proves nothing: security plugins can serve 500 to Googlebot only, and a domain on registrar hold still serves by IP. Commands and alert conditions: `references/site-checks.md`. If a check fails, that is the week's first job and the run changes nothing else on the site. If you can't run the checks (no network, placeholder domain), write that as a `blocked:` line — never report a pass you didn't see.

**2. Measure on complete data, per query.** Search Console lags about two days, so windows end on the latest *complete* day; 7 days vs the 7 before, plus 28 days for the KPI. Split brand from non-brand (by query *and* by page — anonymised queries hide most name searches). Judge rankings per query, never by the site average: a site that starts showing for new queries gets a worse average while every query holds. On small sites, credit nothing to one week — a 10-place jump on 20 impressions often reverts. Details: `references/measurement.md`.

**3. Every site change gets a Change log row and two rechecks.** Record the page, the change, the target keywords, a 28-day baseline (position · impressions · CTR), and recheck dates at +14 and +28 days. Make at most one change per page per 14 days so a verdict can be attributed. Start the clock at the first crawl after the change, not the edit date. Verdict thresholds (worked / no effect / worse) are in `references/measurement.md` §5.

**4. Revise the plan from evidence only.** Every revision cites a number, a report path or a lesson ID. At most 3 revisions per run; don't change the same item again within 2 weeks unless new evidence arrived. Past weeks are history: never rewrite them — mark moved items "→ moved to week N" in place.

**5. Stay inside the autonomy level; propose the rest.** The plan states what runs may change on their own (reorder weeks, swap a topic for one with better evidence, refill queues, re-rank levers). Anything touching the KPI, budget, quarter dates, site rules, or *facts* — prices, hours, phone, credentials, medical or legal claims, product specs — goes to **Proposals** for the human. Facts come only from the owner, never from a competitor or a guess. Approval fields (e.g. `approved_by:`) are filled only by the human who got the approval.

**6. Size the human's queue to their time budget.** Everything that needs the human or the client becomes a queue item with a minute estimate, most valuable first, within the weekly hours in the plan. A drafted outreach or listing does nothing until it is sent — track a "sent on" date. When two or more asks have waited 14+ days, replace them with **one ready-to-forward message of at most 3 yes/no questions**, addressed straight to the person who decides.

**7. Never end a run without a file.** If a step is blocked (no data access, a CAPTCHA, a failing script), still write the report with a first line `blocked: <step> — <reason>`, do every part that doesn't depend on it, and say what unblocks it. A run with no file is a failure even if it "succeeded".

**8. Learn across sites.** Read `lessons.md` entries for this site's type before planning, and cite the lesson ID when one drives a decision. After a run, add or update at most 2 lessons: **add** only with evidence from this site (best source: a Change log verdict), **strengthen** when a site shows it again (add the site, raise confidence `once` → `2+ sites` → `reliable`), **dispute** when a site shows the opposite. Never delete a lesson; keep each to 1–3 lines; no general SEO advice. A new `lessons.md` can be seeded from `references/field-lessons.md`.

**9. Be honest about what you know.** Google decides positions — never promise #1. Separate measured from inferred, label every number with its source and window, and say "unknown" when the data can't separate your change from Google's.

**10. Stay white-hat.** No bought links or reviews, no doorway area pages, no near-duplicates, no copying rivals' text or images, no keyword stuffing, no fake update dates. Reviews come only from real customers asked directly. When searching Google for rival checks, pace the searches and stop at the first CAPTCHA — never try to get around it.

## Getting Search Console data

Use whatever route the user has, in this order of preference: a Search Console connector or API (no browser, exact numbers) → the GSC Performance page read directly → a CSV export. Always request explicit date ranges. Take property totals from a date-only or daily read, not from summing query rows (anonymised queries drop out of query rows). Save raw rows in a new dated folder each run.

`scripts/gsc_compare.py` (Python 3.8+, standard library only) does the arithmetic deterministically:

```bash
python scripts/gsc_compare.py window  --daily daily.csv              # latest complete day + the windows
python scripts/gsc_compare.py compare --cur q-cur.csv --prev q-prev.csv --brand "acme,اکمی" --tracked keyword-tracker.md --q28 q-28d.csv
python scripts/gsc_compare.py verdict --base-pos 8.4 --base-ctr 1.2 --new-pos 7.9 --new-ctr 1.9 --impressions 230
```

It reads GSC CSV exports (`Top queries`/`Top pages`, `Clicks`, `Impressions`, `CTR`, `Position`) or JSON rows (`query`/`page`, `clicks`, `impressions`, `ctr`, `position`). Pass `--q28` with the 28-day rows so the push zone and fail list use the 28-day impression threshold the method defines; without it they use the current window's impressions. Prefer the script over mental arithmetic for windows, scorecards and verdicts. On Windows run it with `python`, not `python3` (often an old Store install).

## Running on a schedule

The method works on demand, and it works best as two recurring jobs per site: a **weekly run** and a **keyword session** 1–4 days before it, so keywords are examined twice a week and rivals and health once. The keyword session only reports; the weekly run acts. If the host has a scheduler, have each weekly run confirm both jobs still exist — scheduled jobs can disappear silently while their files stay on disk. Missed jobs may all fire at once, so a weekly run never waits on another job's output: judge another job by the file it wrote, and measure itself when that file is missing.

## Weekly report

Every weekly run ends with a report to the human (and the same facts in the plan's Weekly log):

```
# <site> — week <N> · <date>
<blocked: … line, only if something was blocked>
Alerts: <site-reachability, drop alerts — or "none">
KPI: <7-day and 28-day numbers, brand / non-brand, indexed> (source, window)
Scorecard: top 3 <n> (±) · 4–10 <n> (±) · 11–20 <n> (±) · 21+/none <n> · weighted avg <x> (±)
Fail list: <tracked keywords not in the top 3, each with this week's action or "skipped: <rule>; unblocks when <action>">
Verdicts: <change → worked / no effect / worse>
Done: …
Not done → moved / dropped: …
Your queue (<m> of <budget> min): <items with minute estimates, most valuable first>
Plan revisions: <up to 3, each with its evidence>
Proposals waiting for you: …
```
