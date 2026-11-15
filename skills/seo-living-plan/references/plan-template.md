# Setting up a living plan

## Before writing: gather

Ask only for what you can't find. Most of this is in the workspace or Search Console.

- **Site and type** — e.g. `local-business`, `medical`, `ecommerce`, `saas`, `publisher`. The type decides which lessons and levers apply.
- **Quarter dates** — 12–13 weeks. Use the calendar the owner uses (Gregorian, Jalali…) and give ISO dates alongside.
- **KPI** — one measurable outcome tied to the business: commercial-intent clicks, leads, bookings, non-brand impressions. Not "rankings" in general.
- **Human time budget** — hours per week the human (you or the client) can spend on approvals, reviews and messages.
- **Autonomy level** — what runs may do alone: e.g. *read-only* (reports and drafts only), *drafts + non-fact fixes* (internal links, schema, alt text, titles), or *publish approved content*. Write it down; every run checks it.
- **Brand terms** — every spelling and transliteration of the business and owner names.
- **Facts owner** — who confirms prices, hours, credentials, claims. Facts come only from them.
- **Data access** — how Search Console is read (connector/API, UI, export).

Then pull a **baseline**: 28 days (or longer if available) of totals, queries and pages; indexed / not indexed counts; a reachability check (`site-checks.md`). Save it as the first dated data folder.

## Building the plan

1. **Profile the site** from the baseline: brand vs non-brand share, top pages, where commercial queries sit (top 3 / 4–10 / 11–20 / 21+), the push zone (positions 4–15 with ≥ 20 impressions in 28 days), pages ranking 50+, indexing gaps, health issues.
2. **Pick and rank the levers** (`ranking-playbook.md`) for this site, each with an evidence line from the baseline. This is the **Ranking strategy** section — runs work from its order.
3. **Seed `keyword-tracker.md`** with the commercial keywords that matter (from the baseline queries and the owner's services/products), each with intent and target page. Seed `rivals.md` from a first SERP look if you can search; otherwise leave it for the first keyword session.
4. **Write the week table:** one main item per week, front-loading fixes and push-zone work, with human minutes per item inside the time budget.
5. **Set targets** as ranges, not points (top-3 count, top-10 count, KPI), derived from the baseline with the arithmetic shown. Revisit at month checkpoints.
6. **Create the empty bottom sections** so the first run has somewhere to write.
7. **Create or seed `lessons.md`** (shared across the user's sites). If none exists, copy `assets/lessons.md` and offer to seed it from `field-lessons.md`.

**Write the plan file first** — it's the deliverable; the tracker, rivals and lessons files come after it. If the plan is long, write it in parts (create, then append) rather than one huge write. When you're done, check the files agree with each other: week numbers, page owners and message numbers in the tracker must match the plan.

**Human time** means all of it: approvals, reviews, client messages and any recurring check the human does. Every week's total must fit the budget — agent work has no budget, but it must stay inside the week's plan.

## Plan skeleton

```markdown
# <Site> — SEO plan, <quarter name> (<start> → <end>)

## Decisions
- Site type: <type> · KPI: <KPI with its baseline value and window>
- Human time budget: <h> h/week · Autonomy: <level, in one line>
- Brand terms: <list> · Facts owner: <who>
- Data source: <how GSC is read>

## Baseline (<window>, <source>)
<totals; brand / non-brand; indexed; top pages; reachability line>

## Ranking strategy
Profile: <2–4 lines on where the site stands and why>
1. <Lever> — evidence: <number / path> — targets: <keywords or pages>
2. …
Never: <site-specific "never" rules — these are rules: runs propose, don't change>
Targets (end of quarter): top 3 <range> · top 10 <range> · KPI <range> (arithmetic: …)

## Weeks
| Week | Dates | Main item | Human minutes | Status |
|---|---|---|---|---|

## Improvement queue
<ranked list of candidate pages/changes with their evidence; runs refill it>

## Listings & links tracker
| Item | Platform | Drafted | Sent on | Status |

## Weekly log
### Week N · <date> — <run id>
- KPI: <7-day and 28-day, brand / non-brand, indexed> (source path)
- Scorecard: top 3 <n> (±) · 4–10 <n> (±) · 11–20 <n> (±) · 21+/none <n> · weighted avg <x> (±)
- Done: …
- Not done → moved / dropped: …
- Blocked: … (unblocks when …)
- Verdicts: <change → worked / no effect / worse>
- Human queue: <items, minutes> — total <m> of <budget> min

## Change log
| date | page | change | target keyword(s) | baseline (pos · impr · CTR, 28 d) | recheck 14 d | recheck 28 d | verdict |

## Plan revisions
| date | week | what changed | why (evidence / lesson) |

## Proposals
| date | proposal | why | status (open / approved <date> / declined <date>) |
```

## Revising the plan

**A run may change on its own** (logging each in Plan revisions):
- Reorder or move upcoming weeks' items; split, merge or re-scope them.
- Swap an upcoming topic or target for one with better evidence — same KPI, same rules.
- Re-rank the levers in the Ranking strategy and refresh their evidence lines.
- Refill the improvement queue; update human-minute estimates.
- Add a small task the data shows is needed and fits the budget.
- Mark items blocked, with what unblocks them.
- At month checkpoints only: recalibrate target ranges (old, new, arithmetic).

**A run must propose, not change** (Proposals table):
- The KPI, the time budget, the quarter dates, anything under Decisions.
- Site rules, "Never" lines, content or medical/legal rules, the autonomy level.
- Anything touching facts: prices, hours, contact details, credentials, claims, product specs.
- Dropping a goal, or a change bigger than one week of work.

When the human answers a proposal, apply it in the next run and log "approved <date>". When they approve something in conversation, record their words and the date in the file *in the same turn* — approvals that live only in chat get lost.
