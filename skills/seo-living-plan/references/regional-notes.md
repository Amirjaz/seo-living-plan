# Regional notes

Read the section for the site's market. Add a section when you learn a market's specifics.

## Iran (and Persian-language sites)

- **Google Business Profile can't be claimed or verified** for a business in Iran. Build local presence through **Neshan** and **Balad** (map apps) and Iranian directories; reviews on an existing Google Maps place still work.
- **Doctor and clinic platforms** often host unmanaged profiles that rank for the doctor's name: Paziresh24, Nobat, Doctoreto, DrDr, Doctor-Yab and similar. Search them before planning a listing; check the specialty and category on each; claim and correct.
- **Ecommerce trust:** merchant listings (e.g. Torob) and the Enamad trust badge are what shoppers look for.
- **Descriptors matter legally:** «کلینیک» (a licensed facility) and «مطب» (a private practice) are different things. Ask the owner which it is.
- **Searching:** use `https://www.google.com/search?q=<q>&hl=fa&gl=ir`. If results look non-Iranian, a VPN is probably on.
- **`.ir` DNS:** local DNS can fail for `.ir` while a VPN is on — resolve with `https://dns.google/resolve?name=<domain>&type=A`. RDAP doesn't cover `.ir`; use `whois` or nic.ir, and write "expiry: not checkable" if neither answers.
- **Sites behind Iranian CDNs** (e.g. ArvanCloud) may need `curl --resolve <domain>:443:<edge IP>` from outside Iran.
- **Dates:** owners plan in the Jalali (Shamsi) calendar. Write Jalali dates in the plan with ISO dates alongside, e.g. «۱ آبان ۱۴۰۵ (2026-10-23)».
- **Persian slugs** in Search Console page filters need the double-encoded form for "contains"; query filters take single encoding.
- **Content:** use the half-space (نیم‌فاصله) correctly, Persian digits in body copy where the site does, and write alt text in Persian.
