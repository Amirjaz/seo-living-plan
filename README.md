<div align="center">

# 🌱 seo-living-plan

**An SEO plan that measures itself, judges its own changes, and gets smarter every week.**

A [Claude skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) built from three months of running real client sites.

![Claude Skill](https://img.shields.io/badge/Claude-Skill-D97757)
![Tests](https://img.shields.io/badge/tests-23%2F24%20with%20skill%20·%2014%2F24%20without-2ea44f)
![Python](https://img.shields.io/badge/python-3.8%2B%20·%20no%20dependencies-3776AB)
![License](https://img.shields.io/badge/license-MIT-blue)

</div>

## Why

Most SEO plans are dead by week three. Nobody re-measures the title change from last month. One lucky week gets celebrated, then reverses. Every site walks into the same technical trap. Finished drafts sit "waiting for the client" for weeks.

This skill makes Claude run the plan with discipline, every week, without being reminded.

## What you get

- 📋 **A quarter plan** built from your Search Console data, where every lever cites the number behind it.
- 🩺 **A weekly run.** It checks the site the way Googlebot sees it, measures complete days only, flags drops, judges past changes, does the work you allow, and logs it all.
- ⚖️ **Honest verdicts.** Every change gets a baseline and rechecks at +14 and +28 days: *worked*, *no effect* or *worse*.
- 🧠 **A plan that learns.** At most 3 evidence-backed revisions a week, plus a lessons file shared across all your sites. It comes seeded with 29 lessons from the field.
- 🤝 **Respect for the owner.** Prices, hours and medical claims come only from them. Stuck questions go out as one message of 3 yes/no answers.

## A weekly run, in brief

From a test run on a made-up dental practice in Leeds:

```text
# Brightside Dental — week 4 · 2026-11-15
blocked: site reachability — no live access this week. No pass is claimed.

Alerts
- DROP: "dentist headingley" left the top 3: 2.8 → 4.1 on 140 impressions.
- HEALTH: /blog/composite-bonding-vs-veneers/ returns 404 since 11-10. Fix packaged.

Fail list
- veneers leeds · 11.2 — skipped: waits for the dentist's approval. Third week here,
  so the next lever is different: a reviewer box with the GDC number.
- cost of veneers uk · 24.5 — skipped: a price range is a fact; unblocks when the dentist gives one.

Verdict
- Implant title (10-12), +28 → worked: 9.8 → 7.1 (but only ≈ 3 → 9 clicks).

Not done as written
- "Copy the address from the second Google listing" → refused: it shows the old address.

Your queue (85 of 180 min)
1. [week 3 carried] Forward one 3-question message to Dr. Okafor (5 min).
```

Full report: [examples/weekly-report-dental-practice.md](examples/weekly-report-dental-practice.md) · a full quarter plan: [examples/setup-bakery-plan.md](examples/setup-bakery-plan.md)

## Does it help?

Same model, same tasks, with and without the skill, graded against written checks:

| Task | With skill | Without |
|---|:---:|:---:|
| Set up a quarter plan for a bakery from 8 weeks of exports | **10 / 10** | 6 / 10 |
| Run week 4 of a dental practice's plan | **9 / 10** | 6 / 10 |
| "Did my title change work, and can I edit the H2s now?" | **4 / 4** | 2 / 4 |

Without the skill, Claude still writes a sensible plan. It skips the discipline: no baseline for the next change, too many plan revisions, drops filed as "watch", and the human's weekly hours overbooked.

## Install

```bash
npx skills add Amirjaz/seo-living-plan
```

Or copy [`skills/seo-living-plan/`](skills/seo-living-plan/) into `~/.claude/skills/`. Then just ask:

```text
Set up a living SEO plan for this site for next quarter. Exports are in /data. I have 2 hours a week.
Run this week's SEO plan.
I changed the title on /pricing on Oct 14. Before: pos 8.4, CTR 1.2 %. Now: 7.9, 1.9 %. Did it work?
```

## Every rule has a story

- A security plugin answered **HTTP 500 to Googlebot only**. Browsers and Google's own live test saw a healthy site. → Each run fetches the site with a Googlebot user agent first.
- A domain went on **registrar hold** and kept serving by IP. Three days later impressions fell 99 %. → Each run checks DNS and registration status.
- A directory profile nobody managed took **#1 for the dentist's own name** while the claim sat unsent. → Drafted work is tracked until it's actually sent.

More in [`field-lessons.md`](skills/seo-living-plan/references/field-lessons.md).

## Inside

`SKILL.md` holds the method and its 10 rules. `references/` has the weekly routine, measurement rules and a ranking playbook, `assets/` has the templates, and `evals/` has the test cases. [`gsc_compare.py`](skills/seo-living-plan/scripts/gsc_compare.py) does the Search Console arithmetic (windows, scorecard, drop alerts, verdicts) with only the Python standard library, and works with any language, including right-to-left scripts.

---

<div align="center">

Built by **[Amir Jazayeri](https://github.com/Amirjaz)** · MIT License · a ⭐ helps others find it

</div>
