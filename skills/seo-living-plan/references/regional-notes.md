# Market notes

Most of the method is the same everywhere. Read this when the site's market differs from the default assumptions (Google is the main engine, Google Business Profile is available, a Latin-script language). Add a section when you learn a market's specifics.

## When Google isn't the main search engine

Check the market's share first. Where another engine leads, measure with its own webmaster tools as well as Search Console, and put its local and map products into lever C:
- **China:** Baidu (Baidu Webmaster Tools; ICP licence and hosting in mainland China matter for crawling).
- **Russia:** Yandex (Yandex Webmaster; Yandex Maps / Business).
- **South Korea:** Naver (Naver Search Advisor; Naver Place), alongside Google.

## When Google Business Profile isn't available

In some sanctioned countries (Iran, for example) a business can't claim or verify a Google Business Profile, though reviews on an existing Maps place still work. Build local presence through the local map apps and directories instead, and track them in the Listings & links tracker.

## Local platforms that host profiles of the business

In every market, directories, booking platforms and map apps may already list the business — unmanaged, sometimes with the wrong category, no site link and rivals promoted. Search them before planning a listing; the task is "claim and correct" (lesson FL-09). Examples by vertical:
- **Health:** Doctify, Zocdoc, Healthgrades, Jameda, Doctolib, Practo — and national equivalents.
- **Local business:** Yelp, Apple Maps, Bing Places, Tripadvisor, Foursquare, delivery apps.
- **Ecommerce:** price-comparison and merchant listings, marketplace storefronts, trust badges the market expects.

## Professional and legal descriptors

Ask the owner what the business legally is before choosing its descriptor — a licensed clinic vs a private practice, a law firm vs a sole practitioner. The wrong word is a trust and regulatory problem, and it spreads into titles, schema and alt text fast (lesson FL-27). Show registration numbers (medical council, dental council, bar number) exactly as registered.

## Language and script

- Search the market's own Google settings: `https://www.google.com/search?q=<q>&hl=<lang>&gl=<country>`. If results look like the wrong country, a VPN is probably on.
- Right-to-left languages (Arabic, Persian, Hebrew, Urdu): normalise letter variants when matching keywords — `gsc_compare.py` merges Arabic/Persian forms of ی/ي and ک/ك, spacing variants and half-spaces — and write alt text in the page's language.
- Non-ASCII slugs: Search Console page filters may need the double-encoded form for "contains"; query filters take single encoding.
- Calendars: if the owner plans in another calendar (Jalali, Hijri, Hebrew), write those dates in the plan with ISO dates alongside.

## Country-code domains

- Some ccTLDs have no public RDAP: use `whois` or the registry's site, and write "expiry: not checkable" if neither answers.
- Local DNS can fail for some ccTLDs on a VPN — resolve with `https://dns.google/resolve?name=<domain>&type=A`.
- Sites behind a regional CDN may need `curl --resolve <domain>:443:<edge IP>` from outside the region.
