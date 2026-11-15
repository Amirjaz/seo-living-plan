# Ranking playbook — the levers

Each plan's **Ranking strategy** picks and orders these levers for its own site, with an evidence line for each. Runs work from that order, not from this list.

## A. Push zone first
Each week, 1–3 tracked commercial keywords at **positions 4–15 with ≥ 20 impressions in 28 days** get one focused change on the page that owns them:
- title and H1 use the query's own wording and intent;
- an answer-first opening paragraph, and an H2 per real sub-question (from the page's GSC queries and People also ask);
- FAQ only from real queries;
- 2–3 contextual internal links from the site's highest-impression related pages, with descriptive anchors.

One change per page per 14 days, logged in the Change log. Content that makes medical, legal or financial claims still needs the owner's approval.

## B. One owner per query
When two URLs split a query, name the owner and link from the other page to it. Decide a merge only after 3+ weeks of data — a link alone can give a 1–2 week gain that doesn't hold, so judge it on 28 days.

## C. Local and entity signals (local businesses, clinics)
- Identical name, address and phone everywhere.
- Search directories, booking platforms and map apps for existing profiles — and claim/correct them (including the category) before creating new ones. Unclaimed profiles can outrank the site on its own name.
- A site link on every profile.
- Reviews only from real customers asked directly.
- When the business name is shared with others, track and promise the **name + city/specialty** form, not the bare name — namesakes' map listings and knowledge panels cap the bare name.
- Where Google Business Profile isn't available, use the market's own map apps and directories (`regional-notes.md`).

## D. Trust for YMYL topics (medical, legal, financial)
The professional's exact credential and licence number on the site and on every profile; an author/reviewer box whose schema (`Physician`, `Dentist`, `Attorney`…) matches it, with `sameAs` pointing at the claimed profiles; a "reviewed by" line only after real approval; sources actually opened; real update dates. Ask what the practice legally is (clinic vs private practice, firm vs solo) before choosing its descriptor — owners reject the wrong one.

## E. Pages ranking 50+
Existing pages at 50+ rarely move from on-page work alone. Pair them with off-site/local signals, internal links and indexing, or consolidation — and judge on 28 days; at ~20 impressions a week they swing 20–40 places on their own. (New, well-linked pages for a query are different: they can reach the top 10 quickly on a site Google isn't demoting.)

## F. Crawl and index
A new URL is linked from a crawled page, in the sitemap, and requested once. When a whole section sits in "Discovered – currently not indexed", treat it as crawl capacity, not links: check Crawl stats by Googlebot type (Smartphone is usually the indexing crawler), server response time, and what is eating the crawl (parameter URLs, prefetch payloads — `site-checks.md` §2).

## G. Snippet CTR
On page-one pages (positions 1–5) with CTR below the site's median for that position, rewrite the title and description for the real queries. A means to more clicks, not the goal.

## H. Ecommerce
- Indexable hubs only where there is demand (category → segment → brand), each with a unique intro, FAQ and links to its best products.
- Product titles in the form people search (brand + model + key attribute).
- `Product` + `Offer` (price, availability) + `BreadcrumbList` schema that matches the visible page.
- Own photos with descriptive alt text in the page's language.
- Variant URLs canonical to the product unless they have their own demand.
- Price and stock always current; merchant listings and trust badges the market expects.
- Block crawlable filter/sort parameters (robots.txt); `noindex, follow` stops indexing, not crawling.
- No thin or duplicate pages.

## Never
Bought links or reviews, doorway area/city pages, near-duplicate pages, copying rivals, keyword stuffing, fake update dates.
