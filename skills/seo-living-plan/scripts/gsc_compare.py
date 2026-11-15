#!/usr/bin/env python3
"""Search Console arithmetic for the seo-living-plan skill.

Standard library only, Python 3.8+. Works the same on Windows, macOS and Linux.

  window   --daily FILE [--today YYYY-MM-DD]
      Latest complete day (Search Console lags ~2 days) and the 7/28-day windows, with totals.
  compare  --cur FILE --prev FILE [--brand "a,b"] [--tracked FILE] [--min-impr 20] [--json]
      Query or page rows, current vs previous window: totals, brand split, drops, new top-3/10,
      push zone, pages that lost > 50 % of impressions, and (with --tracked) the scorecard and
      fail list for the tracked commercial set.
  verdict  --base-pos P --base-ctr C --new-pos P2 --new-ctr C2 --impressions N [--json]
      Change log verdict: worked / no effect / worse (references/measurement.md section 5).

Input files: a Search Console CSV export (columns like "Top queries"/"Top pages"/"Date",
"Clicks", "Impressions", "CTR", "Position") or JSON rows ([...] or {"data": [...]}) with keys
query/page/date, clicks, impressions, ctr, position. CTR is recomputed from clicks/impressions
whenever both exist, so percent vs fraction never matters.

--tracked accepts a plain list (one keyword per line) or a keyword-tracker.md table; rows whose
intent is info/brand or whose status starts with "retired" are left out of the scorecard.
"""
import argparse
import csv
import json
import statistics
import sys
from datetime import date, timedelta
from pathlib import Path

try:  # Windows consoles default to a legacy code page; Persian/emoji output would crash.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

KEY_ALIASES = {
    "query": ("query", "top queries", "queries", "search query"),
    "page": ("page", "top pages", "pages", "url", "landing page"),
    "date": ("date", "day"),
    "device": ("device", "devices"),
}
METRIC_ALIASES = {
    "clicks": ("clicks",),
    "impressions": ("impressions",),
    "ctr": ("ctr",),
    "position": ("position", "avg. position", "average position"),
}


# ---------- loading ----------

def _num(value):
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip().replace("%", "").replace(",", "")
    if text in ("", "-", "—"):
        return 0.0
    try:
        return float(text)
    except ValueError:
        return 0.0


def _match(header, aliases):
    h = header.strip().lower()
    return any(h == a for a in aliases)


def load_rows(path):
    """Return (kind, rows); kind is 'query', 'page', 'date' or 'device'; rows are dicts."""
    p = Path(path)
    if not p.exists():
        sys.exit("error: file not found: %s" % path)
    if p.suffix.lower() == ".json":
        data = json.loads(p.read_text(encoding="utf-8-sig"))
        if isinstance(data, dict):
            data = data.get("data") or data.get("rows") or []
        raw = [dict((str(k).lower(), v) for k, v in r.items()) for r in data]
    else:
        with p.open(encoding="utf-8-sig", newline="") as fh:
            raw = [dict((str(k).strip().lower(), v) for k, v in r.items() if k is not None)
                   for r in csv.DictReader(fh)]
    if not raw:
        return None, []
    headers = list(raw[0].keys())
    kind, key_col = None, None
    for k, aliases in KEY_ALIASES.items():
        for h in headers:
            if _match(h, aliases):
                kind, key_col = k, h
                break
        if kind:
            break
    if not kind:
        sys.exit("error: %s has no query/page/date column (headers: %s)" % (path, ", ".join(headers)))
    cols = {}
    for m, aliases in METRIC_ALIASES.items():
        for h in headers:
            if _match(h, aliases):
                cols[m] = h
                break
    rows = []
    for r in raw:
        key = str(r.get(key_col, "")).strip()
        if not key:
            continue
        clicks = _num(r.get(cols.get("clicks")))
        impr = _num(r.get(cols.get("impressions")))
        if impr > 0:
            ctr = clicks / impr * 100.0
        else:
            ctr = _num(r.get(cols.get("ctr")))
            if 0 < ctr <= 1 and "%" not in str(r.get(cols.get("ctr"), "")):
                ctr *= 100.0
        rows.append({"key": key, "clicks": clicks, "impressions": impr, "ctr": ctr,
                     "position": _num(r.get(cols.get("position")))})
    return kind, rows


def totals(rows):
    clicks = sum(r["clicks"] for r in rows)
    impr = sum(r["impressions"] for r in rows)
    pos = (sum(r["position"] * r["impressions"] for r in rows) / impr) if impr else 0.0
    return {"clicks": round(clicks), "impressions": round(impr),
            "ctr": round(clicks / impr * 100, 2) if impr else 0.0, "position": round(pos, 2)}


def norm(text):
    """Lower-case, unify Arabic/Persian letter forms, drop spaces and half-spaces."""
    t = str(text).lower()
    for a, b in (("ي", "ی"), ("ى", "ی"), ("ك", "ک"), ("ة", "ه"), ("‌", ""), ("‏", ""),
                 ("‎", ""), (" ", ""), ("-", "")):
        t = t.replace(a, b)
    return t


# ---------- window ----------

def cmd_window(args):
    kind, rows = load_rows(args.daily)
    if kind != "date":
        sys.exit("error: --daily needs a file with a date column")
    by_day = {}
    for r in rows:
        try:
            d = date.fromisoformat(r["key"][:10])
        except ValueError:
            continue
        by_day[d] = r
    if not by_day:
        sys.exit("error: no parseable dates in %s" % args.daily)
    days = sorted(by_day)
    today = date.fromisoformat(args.today) if args.today else date.today()
    candidates = [d for d in days if d < today]
    if not candidates:
        sys.exit("error: no dates before today (%s)" % today)
    notes = []
    latest = None
    for d in reversed(candidates):
        before = [by_day[x]["impressions"] for x in days if d - timedelta(days=7) <= x < d]
        if len(before) >= 3:
            med = statistics.median(before)
            if med and by_day[d]["impressions"] < 0.6 * med:
                notes.append("%s skipped: %d impressions < 60%% of the prior 7-day median (%d) — incomplete"
                             % (d, by_day[d]["impressions"], med))
                continue
        latest = d
        break
    if latest is None:
        sys.exit("error: could not find a complete day")

    def win(end, n):
        return [end - timedelta(days=n - 1), end]

    def sum_win(w):
        sel = [by_day[d] for d in days if w[0] <= d <= w[1]]
        t = totals(sel)
        t["days_with_data"] = len(sel)
        return t

    cur7 = win(latest, 7)
    prev7 = win(latest - timedelta(days=7), 7)
    cur28 = win(latest, 28)
    prev28 = win(latest - timedelta(days=28), 28)
    out = {
        "latest_complete_day": latest.isoformat(),
        "lag_days": (today - latest).days,
        "windows": {k: [w[0].isoformat(), w[1].isoformat()] for k, w in
                    (("cur7", cur7), ("prev7", prev7), ("cur28", cur28), ("prev28", prev28))},
        "totals": {"cur7": sum_win(cur7), "prev7": sum_win(prev7),
                   "cur28": sum_win(cur28), "prev28": sum_win(prev28)},
        "notes": notes,
    }
    for k in ("cur28", "prev28"):
        if out["totals"][k]["days_with_data"] < 28:
            out["notes"].append("%s has only %d days of data — partial" % (k, out["totals"][k]["days_with_data"]))
    print(json.dumps(out, ensure_ascii=False, indent=2))


# ---------- compare ----------

def load_tracked(path):
    """Return list of keywords in the commercial set."""
    lines = Path(path).read_text(encoding="utf-8-sig").splitlines()
    table = [l for l in lines if l.strip().startswith("|")]
    if not table:
        return [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]
    header = [c.strip().lower() for c in table[0].strip().strip("|").split("|")]
    i_kw = 0
    i_intent = next((i for i, h in enumerate(header) if h.startswith("intent")), None)
    i_status = next((i for i, h in enumerate(header) if h.startswith("status")), None)
    out = []
    for row in table[1:]:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= set("-: "):
            continue
        if i_intent is not None and i_intent < len(cells) and cells[i_intent].lower() in ("info", "brand"):
            continue
        if i_status is not None and i_status < len(cells) and cells[i_status].lower().startswith("retired"):
            continue
        if cells[i_kw]:
            out.append(cells[i_kw])
    return out


def norm_index(rows):
    """Merge rows whose queries differ only in spacing, half-spaces or Arabic/Persian letter forms,
    so a tracked keyword matches all its spellings (impression-weighted position)."""
    idx = {}
    for r in rows:
        k = norm(r["key"])
        a = idx.setdefault(k, {"key": r["key"], "clicks": 0.0, "impressions": 0.0, "_w": 0.0})
        a["clicks"] += r["clicks"]
        a["impressions"] += r["impressions"]
        a["_w"] += r["position"] * r["impressions"]
    for a in idx.values():
        a["position"] = a["_w"] / a["impressions"] if a["impressions"] else 0.0
    return idx


def bucket(pos):
    if pos <= 0:
        return "21+/none"
    if pos < 3.5:
        return "top 3"
    if pos < 10.5:
        return "4–10"
    if pos < 20.5:
        return "11–20"
    return "21+/none"


def scorecard(keywords, cur, prev, min_impr, vol28=None):
    names = ("top 3", "4–10", "11–20", "21+/none")
    result = {"set_size": len(keywords), "cur": dict((n, 0) for n in names),
              "prev": dict((n, 0) for n in names), "fail_list": [], "drop_alerts": [], "missing": []}
    w_cur = [0.0, 0.0]
    w_prev = [0.0, 0.0]
    for kw in keywords:
        nk = norm(kw)
        c = cur.get(nk)
        p = prev.get(nk)
        result["cur"][bucket(c["position"] if c else 0)] += 1
        result["prev"][bucket(p["position"] if p else 0)] += 1
        if c and c["impressions"]:
            w_cur[0] += c["position"] * c["impressions"]
            w_cur[1] += c["impressions"]
        if p and p["impressions"]:
            w_prev[0] += p["position"] * p["impressions"]
            w_prev[1] += p["impressions"]
        if c and p and c["position"] and p["position"] and max(c["impressions"], p["impressions"]) >= min_impr:
            if (p["position"] < 3.5 <= c["position"]) or (c["position"] - p["position"] >= 0.5):
                result["drop_alerts"].append({"keyword": kw, "from": round(p["position"], 1),
                                              "to": round(c["position"], 1), "impressions": int(c["impressions"]),
                                              "left_top3": p["position"] < 3.5 <= c["position"]})
        vol = vol28[nk]["impressions"] if (vol28 is not None and nk in vol28) else (c["impressions"] if c else 0)
        if not c:
            result["missing"].append(kw)
        elif vol >= min_impr and c["position"] >= 3.5:
            result["fail_list"].append({"keyword": kw, "position": round(c["position"], 1),
                                        "impressions": int(c["impressions"]), "impressions_28d": int(vol)
                                        if vol28 is not None else None})
    result["weighted_avg"] = round(w_cur[0] / w_cur[1], 2) if w_cur[1] else None
    result["weighted_avg_prev"] = round(w_prev[0] / w_prev[1], 2) if w_prev[1] else None
    result["fail_list"].sort(key=lambda x: -x["impressions"])
    return result


def cmd_compare(args):
    kind_c, cur_rows = load_rows(args.cur)
    kind_p, prev_rows = load_rows(args.prev)
    if kind_c != kind_p:
        sys.exit("error: --cur is %s rows but --prev is %s rows" % (kind_c, kind_p))
    if kind_c not in ("query", "page"):
        sys.exit("error: compare needs query or page rows (got %s)" % kind_c)
    m = args.min_impr
    cur = dict((r["key"], r) for r in cur_rows)
    prev = dict((r["key"], r) for r in prev_rows)
    v28 = None
    if args.q28:
        k28, rows28 = load_rows(args.q28)
        if k28 != kind_c:
            sys.exit("error: --q28 has %s rows but --cur has %s rows" % (k28, kind_c))
        v28 = dict((r["key"], r) for r in rows28)
    out = {"kind": kind_c, "min_impressions": m,
           "totals_from_rows": {"cur": totals(cur_rows), "prev": totals(prev_rows)},
           "note": "Totals summed from %s rows miss anonymised queries; take property totals from a "
                   "daily or no-dimension read." % kind_c}

    if args.brand and kind_c == "query":
        terms = [norm(t) for t in args.brand.split(",") if t.strip()]

        def split(rows):
            b = [r for r in rows if any(t in norm(r["key"]) for t in terms)]
            nb = [r for r in rows if not any(t in norm(r["key"]) for t in terms)]
            return {"brand": totals(b), "non_brand": totals(nb)}
        out["brand_split"] = {"cur": split(cur_rows), "prev": split(prev_rows)}

    drops, new_top3, new_top10, push, lost_pages, left_top3 = [], [], [], [], [], []
    for k, c in cur.items():
        p = prev.get(k)
        vol = max(c["impressions"], p["impressions"] if p else 0)
        if p and 0 < p["position"] < 3.5 and c["position"] >= 3.5 and vol >= m:
            left_top3.append({"key": c["key"], "from": round(p["position"], 1), "to": round(c["position"], 1),
                              "impressions": int(c["impressions"])})
        if p and p["position"] and c["position"] and c["position"] - p["position"] >= 3 and vol >= m:
            drops.append({"key": c["key"], "from": round(p["position"], 1), "to": round(c["position"], 1),
                          "impressions": int(c["impressions"])})
        if c["position"] and c["position"] < 3.5 and (not p or p["position"] >= 3.5):
            new_top3.append({"key": c["key"], "position": round(c["position"], 1),
                             "from": round(p["position"], 1) if p else None, "impressions": int(c["impressions"])})
        elif c["position"] and c["position"] < 10.5 and (not p or p["position"] >= 10.5):
            new_top10.append({"key": c["key"], "position": round(c["position"], 1),
                              "from": round(p["position"], 1) if p else None, "impressions": int(c["impressions"])})
        push_vol = v28[k]["impressions"] if (v28 is not None and k in v28) else c["impressions"]
        if 3.5 <= c["position"] < 15.5 and push_vol >= m:
            push.append({"key": c["key"], "position": round(c["position"], 1), "impressions": int(push_vol)})
    if kind_c == "page":
        for k, p in prev.items():
            c = cur.get(k)
            ci = c["impressions"] if c else 0
            if p["impressions"] >= m and ci < 0.5 * p["impressions"]:
                lost_pages.append({"key": p["key"], "from": int(p["impressions"]), "to": int(ci)})
    out["left_top3"] = sorted(left_top3, key=lambda x: -x["impressions"])
    out["drops_3plus"] = sorted(drops, key=lambda x: -x["impressions"])
    out["new_top3"] = sorted(new_top3, key=lambda x: -x["impressions"])
    out["new_top10"] = sorted(new_top10, key=lambda x: -x["impressions"])
    out["push_zone_4_15"] = sorted(push, key=lambda x: -x["impressions"])
    if kind_c == "page":
        out["pages_lost_50pct"] = sorted(lost_pages, key=lambda x: -x["from"])
    if args.tracked:
        if kind_c != "query":
            sys.exit("error: --tracked needs query rows")
        out["scorecard"] = scorecard(load_tracked(args.tracked), norm_index(cur_rows), norm_index(prev_rows), m,
                                     norm_index(rows28) if v28 is not None else None)
    out["threshold_window"] = ("28-day impressions from --q28" if v28 is not None else
                               "the --cur window's impressions (pass --q28 <28-day file> for 28-day thresholds)")

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return
    print_compare(out)


def print_compare(out):
    t = out["totals_from_rows"]
    print("## %s rows: current vs previous (min %d impressions for flags)" % (out["kind"], out["min_impressions"]))
    print("Push zone and fail list thresholds use %s.\n" % out["threshold_window"])
    print("Totals from rows — cur: %(clicks)s clicks · %(impressions)s impr · %(ctr)s %% CTR · pos %(position)s" % t["cur"])
    print("                  prev: %(clicks)s clicks · %(impressions)s impr · %(ctr)s %% CTR · pos %(position)s" % t["prev"])
    print("(%s)\n" % out["note"])
    if "brand_split" in out:
        b = out["brand_split"]
        for part in ("brand", "non_brand"):
            print("%-9s cur %s clicks / %s impr · prev %s clicks / %s impr" % (
                part.replace("_", "-"), b["cur"][part]["clicks"], b["cur"][part]["impressions"],
                b["prev"][part]["clicks"], b["prev"][part]["impressions"]))
        print()
    if "scorecard" in out:
        s = out["scorecard"]
        parts = []
        for n in ("top 3", "4–10", "11–20", "21+/none"):
            d = s["cur"][n] - s["prev"][n]
            parts.append("%s %d (%+d)" % (n, s["cur"][n], d))
        wa = s["weighted_avg"]
        wap = s["weighted_avg_prev"]
        delta = (" (%+.2f)" % (wa - wap)) if (wa is not None and wap is not None) else ""
        print("Scorecard (%d tracked): %s · weighted avg %s%s" % (s["set_size"], " · ".join(parts), wa, delta))
        if s["drop_alerts"]:
            print("\nDROP ALERTS (tracked, left the top 3 or fell >= 0.5):")
            for a in s["drop_alerts"]:
                print("- %s · %s → %s · %s impr%s" % (a["keyword"], a["from"], a["to"], a["impressions"],
                                                      " · LEFT THE TOP 3" if a["left_top3"] else ""))
        print("\nFail list (not top 3, >= %d impr):" % out["min_impressions"])
        for f in s["fail_list"] or [{"keyword": "none", "position": "", "impressions": ""}]:
            extra = (" · %s impr / 28 d" % f["impressions_28d"]) if f.get("impressions_28d") is not None else ""
            print("- %s · %s · %s impr%s" % (f["keyword"], f["position"], f["impressions"], extra))
        if s["missing"]:
            print("Not in the current rows (no impressions or below a filter): " + ", ".join(s["missing"]))
        print()
    sections = [("Left the top 3", "left_top3", "{key}: {from} → {to} ({impressions} impr)"),
                ("Dropped >= 3 positions", "drops_3plus", "{key}: {from} → {to} ({impressions} impr)"),
                ("New in top 3", "new_top3", "{key}: {position} (was {from}, {impressions} impr)"),
                ("New in top 10", "new_top10", "{key}: {position} (was {from}, {impressions} impr)"),
                ("Push zone (4–15)", "push_zone_4_15", "{key}: {position} ({impressions} impr)"),
                ("Pages that lost > 50 % of impressions", "pages_lost_50pct", "{key}: {from} → {to} impr")]
    for title, key, fmt in sections:
        if key not in out:
            continue
        items = out[key]
        print("### %s (%d)" % (title, len(items)))
        for it in items[:25]:
            print("- " + fmt.format(**it))
        if len(items) > 25:
            print("- … %d more (use --json)" % (len(items) - 25))
        print()


# ---------- verdict ----------

def verdict(base_pos, base_ctr, new_pos, new_ctr, impressions):
    gain = base_pos - new_pos  # positive = better
    similar = abs(gain) <= 1
    ctr_rel = ((new_ctr - base_ctr) / base_ctr * 100.0) if base_ctr else None
    ctr_txt = ("CTR %+.0f %%" % ctr_rel) if ctr_rel is not None else "CTR change unknown (baseline 0)"
    if gain >= 2:
        return "worked", "%.1f positions better (%.1f → %.1f)" % (gain, base_pos, new_pos)
    if similar and ctr_rel is not None and ctr_rel >= 30:
        return "worked", "%s at a similar position (%.1f → %.1f)" % (ctr_txt, base_pos, new_pos)
    worse_reason = None
    if gain <= -3:
        worse_reason = "%.1f positions worse (%.1f → %.1f)" % (-gain, base_pos, new_pos)
    elif similar and ctr_rel is not None and ctr_rel <= -30:
        worse_reason = "%s at a similar position (%.1f → %.1f)" % (ctr_txt, base_pos, new_pos)
    if worse_reason:
        if impressions >= 50:
            return "worse", worse_reason + " on %d impressions — revert or rethink as the site's rules allow" % impressions
        return "worse (low volume — confirm at +28)", worse_reason + " but only %d impressions (< 50)" % impressions
    return "no effect", "position %+.1f, %s — inside the bounds" % (gain, ctr_txt)


def cmd_verdict(args):
    v, why = verdict(args.base_pos, _num(args.base_ctr), args.new_pos, _num(args.new_ctr), args.impressions)
    if args.json:
        print(json.dumps({"verdict": v, "why": why}, ensure_ascii=False))
    else:
        print("%s — %s" % (v, why))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd")
    w = sub.add_parser("window", help="latest complete day and windows")
    w.add_argument("--daily", required=True)
    w.add_argument("--today")
    c = sub.add_parser("compare", help="current vs previous query/page rows")
    c.add_argument("--cur", required=True)
    c.add_argument("--prev", required=True)
    c.add_argument("--brand", default="")
    c.add_argument("--tracked")
    c.add_argument("--q28", help="28-day rows; push zone and fail list then use 28-day impressions")
    c.add_argument("--min-impr", type=int, default=20)
    c.add_argument("--json", action="store_true")
    v = sub.add_parser("verdict", help="change log verdict")
    v.add_argument("--base-pos", type=float, required=True)
    v.add_argument("--base-ctr", required=True)
    v.add_argument("--new-pos", type=float, required=True)
    v.add_argument("--new-ctr", required=True)
    v.add_argument("--impressions", type=int, required=True)
    v.add_argument("--json", action="store_true")
    args = ap.parse_args()
    if args.cmd == "window":
        cmd_window(args)
    elif args.cmd == "compare":
        cmd_compare(args)
    elif args.cmd == "verdict":
        cmd_verdict(args)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
