---
id: 2026-10-26-mail-tm-limite-de-8-qps
type: atom
certainty: solid
sources: ["sources/2026-10-26-mail-tm-api-docs.md"]
links: ["[[2026-10-26-mail-tm-no-api-key]]", "[[2026-10-26-mail-tm-prohibicion-de-reventa]]"]
---

## Claim
Mail.tm Temp Mail API enforces an 8 queries per second (QPS) rate limit per IP address.

## Why It Matters
The 8 QPS limit constrains the volume of requests a single IP can make within a given timeframe, requiring implementations to incorporate caching, batching, or queuing strategies when integrating with the API at scale.

## [FRICTION]
> [[2026-10-26-mail-tm-no-api-key]] asserts Mail.tm Temp Mail API does not require an API key. Both statements are compatible — no key is needed but the session is still rate-constrained per IP.