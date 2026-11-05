---
id: 2026-10-26-mail-tm-no-api-key
type: atom
certainty: solid
sources: ["sources/2026-10-26-mail-tm-api-docs.md"]
links: ["[[2026-10-26-mail-tm-limite-de-8-qps-por-ip-address]]", "[[2026-10-26-mail-tm-prohibicion-de-reventa]]"]
---

## Claim
Mail.tm Temp Mail API does not require an API key for usage.

## Why It Matters
Eliminating the API key requirement lowers the barrier to entry for developers integrating temp mail functionality, making it immediately accessible without authentication overhead or registration friction.

## [FRICTION]
> [[2026-10-26-mail-tm-limite-de-8-qps-por-ip-address]] asserts Mail.tm Temp Mail API has an 8 QPS rate limit per IP. Both statements are compatible — no key is needed but the session is still rate-constrained.