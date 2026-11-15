# Keyword session (mid-week)

Runs 1–4 days before the weekly run. It **reports; the weekly run acts.** It changes no website and edits no plan — it writes only its own report, `keyword-tracker.md`, `rivals.md` and any crawl output.

Start with the reachability check (`site-checks.md` §1); an alert there becomes the first action in the report.

## 1. Keyword check (every session)

Search Console, rolling 7 days ending on the latest complete day, compared with the previous check. Update `keyword-tracker.md`:

`keyword · intent (buy / booking / patient / lead / info) · target page · position (7-day) · previous check · impressions · status (rising / falling / stuck / new) · next action`

- Add new keywords that earned ≥ 10 impressions in 7 days and have commercial intent.
- Retire keywords the plan dropped — mark them retired, never delete.
- Flag: a tracked keyword falling ≥ 3 positions with ≥ 20 impressions; one entering positions 4–15 (the push zone); one stuck 3+ checks; a new commercial query.
- Small sites are noisy: judge per keyword, not the site average.
- Compute the Scorecard (`measurement.md` §3).

## 2. Rival check (every session)

Search Google for the 10–15 most valuable tracked keywords, rotating the rest across weeks. Use the market's own Google settings (e.g. `https://www.google.com/search?q=<q>&hl=<lang>&gl=<country>`); note when results look like the wrong country (a VPN may be on).

**Pacing — Google blocks automated searches quickly:**
- at most **8 searches per session**;
- **60–120 seconds apart, varied** — never a fixed gap;
- **one search per tool call** — never queue several searches in one batch: a queue keeps firing after Google blocks;
- check every result for a `/sorry/` page or "unusual traffic" before the next search. At the first one, stop the rival check for this session and report it. Never try to solve or get around a CAPTCHA.
- Keywords beyond 8 rotate to the next session; area/map keywords and last session's unfinished ones go first.
- Read directory and list pages directly (fetch the URL), not through Google.

Record per keyword: your position (or "not in top 20"), the top 10 domains, map pack yes/no and who is in it, SERP features (People also ask, featured snippet, video, shopping). For the keywords where you're closest, open the top 1–3 rival pages and compare: depth, H2 outline, FAQ, structured data, reviews/ratings, photos/video, freshness, directory presence, prices. Update `rivals.md` — add, never wipe.

Look for profiles of the business you didn't know about (directories, booking platforms, map apps). An unclaimed or wrong profile can outrank the site on its own name; the action is "claim and correct", not "create".

**Never:** copy rival text, images or structure (describe, don't reproduce); click rivals' ads; submit anything on a rival site; do anything meant to harm a rival's ranking.

## 3. Health check (every session, read-only)

Run the site's crawl script if it has one. Otherwise a light check with `curl`: status, canonical and robots meta of every tracked target page, the sitemap, and the traps in `site-checks.md` §2 that fit the site's stack. Compare with the previous crawl and report only what's new. Never fix anything here — the fix goes into the actions.

## 4. Output

Write `keyword-watch/<YYYY-MM-DD>.md`: reachability line, keyword flags, scorecard, rival findings, health findings — then end with:

```
## Actions for the weekly run
1. To outrank <rival> on <keyword>: <change> on <page>, because <evidence>.
2. Fix <health finding> on <page>, because <traffic at risk>.
```

1–5 concrete items. The weekly run reads this section first and folds the items into its week (or into Proposals when they need the human).
