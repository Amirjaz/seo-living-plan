# Site checks

## 1. Reachable the way Google sees it (first thing, every run)

A browser getting HTTP 200 proves nothing. Check four things and write all four results on one line in the report, even when they pass:

**DNS**
```bash
nslookup example.com 8.8.8.8
# or, when local DNS is unreliable (VPNs, some ccTLDs):
curl -s "https://dns.google/resolve?name=example.com&type=A"
```

**Registration status and expiry** (RDAP; `.com`/`.net` shown — other TLDs have their own RDAP server or `whois`):
```bash
curl -s https://rdap.verisign.com/com/v1/domain/example.com
```
Read `status` and the `expiration` event. If neither RDAP nor whois answers for a ccTLD, write "expiry: not checkable" (not an alert).

**Googlebot, desktop and smartphone**, on `/` and `/robots.txt`:
```bash
UA_DESKTOP="Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
UA_PHONE="Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
curl -s -o /dev/null -w "%{http_code}\n" -A "$UA_DESKTOP" https://example.com/
curl -s -o /dev/null -w "%{http_code}\n" -A "$UA_PHONE"   https://example.com/robots.txt
```
On Windows PowerShell, `curl` is an alias for something else — run these in Git Bash or call `curl.exe`.

**Alert** when: NXDOMAIN; a status containing `hold`; expiry less than 45 days away; anything but 200 for a Googlebot request. Then: first line of the report, a notification, "fix <what>" first in the human's queue — and no other site change that run. Read-only work continues.

Why each one matters:
- **Registrar hold.** A domain went on `client hold` a day after its renewal date; DNS answered NXDOMAIN while the server still served the site by IP. Google kept showing it for ~2.5 days, then impressions fell 99 % and recovery lagged after DNS returned. Renew well before expiry.
- **Googlebot-only errors.** A security plugin's "is this really Google?" check crashed on every Googlebot request — HTTP 500 for robots.txt, sitemap and every page — while browsers, Bingbot *and* URL Inspection's live test got 200. Updating the plugin fixed it; traffic came back partly within a day.

## 2. Technical traps worth checking by stack

Check the ones that fit the site; report only what's new since the last check.

| Stack / situation | Trap | How to check |
|---|---|---|
| Next.js 15.2+ (dynamic routes) | `<title>`, meta description and `rel=canonical` streamed into `<body>` for Googlebot; Google ignores a canonical outside `<head>`. URL Inspection's live test hides it (it's on Next's "limited bots" list, Googlebot isn't). Fix: `htmlLimitedBots` in `next.config`. | `curl -A "<Googlebot UA>"` and compare the byte offset of `<title>`/canonical with `</head>` |
| Next.js `<Link>` prefetch | Googlebot fetches `?_rsc=` payload URLs that crowd out real pages on a small crawl budget. Fix: `prefetch={false}` on crawl-heavy links or `Disallow: /*?_rsc=`. | GSC Crawl stats → by file type / URL |
| Headless storefront | A front end that turns every failed API read into "not found" serves **200 + `noindex`** during deploys and outages. A noindex fetch drops an indexed page; a 5xx only delays it. Return 5xx (or 503) on API failure. | Crawl during a deploy, or with the API stopped on a local build |
| Faceted navigation | Crawlable filter/sort links let Googlebot fetch thousands of noindexed combinations while sitemap products wait as "Discovered – not indexed". | GSC "Excluded by noindex" count; robots.txt; `<a href>` on filters |
| WordPress + Rank Math (and similar) | Breadcrumb and `articleSection` schema come from the post's category — a wrong category labels the page's topic wrong. | Check the post's category (REST `categories`) before working on a lead page |
| Any CMS | `status: publish` in an API doesn't mean the URL resolves; table-of-contents `#fragment` rows in GSC page tables double-count pages. | Fetch the URL; strip fragments before summing |

## 3. Reading indexing

- "Last crawl" in URL Inspection reflects the indexing crawler (usually Googlebot Smartphone). A section can get Desktop fetches and still show "Last crawl N/A". Judge crawl tests in Crawl stats by Googlebot type.
- A changed page whose indexing request hit the quota can stay uncrawled for weeks — check last crawl before crediting or blaming the change.
