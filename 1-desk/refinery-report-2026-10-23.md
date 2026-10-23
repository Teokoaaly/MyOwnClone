# Refinery Report — 2026-10-23

Run: 03:00 shift (scheduled cron).

## Captures processed

`0-raw/` contained **18 unhandled captures**: 17 marked `Status: ready` (the Scout run of 2026-10-22 had fetched a full set of sources that night) plus `2026-10-22-myownclone-live-reverification.md`, which had already been atomized in the previous run but had never been archived.

All 18 are now in `0-raw/archive/2026-10-23-*.md`. `0-raw/` now holds only `reading-list.md` and `archive/`.

## Totals

| Metric | Count |
|---|---|
| Captures processed | 18 |
| Atoms created | 183 |
| Atoms extended | 11 (existing atoms patched with nuance + new source refs) |
| Atoms retired to `2-atoms/archive/` | 3 (merged into sibling atoms; nothing deleted) |
| Friction blocks | 44 across 44 atoms |
| Threads created | 1 |
| Threads updated | 5 |
| Broken wikilinks | 0 |
| Unresolvable source paths | 0 |
| Credentials leaked into notes | 0 (grep verified) |
| Tracked files deleted | 0 |

`2-atoms/` went from 116 to 299 notes.

## Atoms by source

| Source | Atoms | Notes |
|---|---|---|
| `2026-10-22-5sim-home.md` | 22 | Catalog depth, price floors, delivery rates, the three contradictory country counts |
| `2026-10-22-5sim-prices.md` | 15 | Per-country CSV: the measured price floor, dispersion, delivery-rate tables |
| `2026-10-22-5sim-products-catalog.md` | 9 | The full service catalog (1221 names), AI share 2.3 % |
| `2026-10-22-5sim-openai-chatgpt-pricing.md` | 11 | The OpenAI product page: $0.01 vs $0.05, 56 % delivery ceiling |
| `2026-10-22-hero-sms-home.md` | 11 | The 5-service visible catalog, pay-per-use, physical vs virtual stock |
| `2026-10-22-hero-sms-chatgpt-verification.md` | 10 | The five-step verification flow, VoIP blocking, 1-minute retry |
| `2026-10-22-sms-activate-closed.md` | 4 | The closure notice: 22 Dec shutdown, name retired as scam marker |
| `2026-10-22-lzt-market-home.md` | 6 | A failed capture — the market's listings were never rendered; the `LLM Accounts` category and the 10 % top-up fee |
| `2026-10-22-priceai-home.md` | 13 | Four modules, three buyer personas, the QQ channel, the disclaimer |
| `2026-10-22-priceai-official-prices.md` | 12 | Regional subscription arbitrage: ChatGPT Go Egypt −56 %, Gemini Ultra 5× Turkey −70 % |
| `2026-10-22-priceai-official-api.md` | 14 | Token Plans, Coding Plans, quotas, the aggregation categories |
| `2026-10-22-priceai-channels.md` | 13 | The 卡网 table: 53 products, 39 shops, ¥0–¥1027.94, four orders of magnitude |
| `2026-10-22-priceai-api-transit.md` | 10 | The relay ranking: 0.01×–7.00× multipliers, the compound formula, the three limits |
| `2026-10-22-hetzner-cloud.md` | 15 | Plan prices, hourly billing, 20 TB, SLA, regions |
| `2026-10-22-new-api-github.md` | 14 | The gateway stack: channel groups, ratio pricing, token counting, AGPLv3 |
| `2026-10-22-midjourney-proxy-github.md` | 10 | "No official API → unofficial bridge", the same gap as `myownclone_public_bp` |
| `2026-10-22-awesome-ai-security-tools.md` | 15 | The field's taxonomy and what of it actually applies to this product |
| `2026-10-22-myownclone-live-reverification.md` | 6 new + 5 extended | Coverage audit of the live verification, not a re-atomization |

## Frictions raised — 44

These are the ones that matter; the full list is in the atoms themselves, each with a `## [FRICTION]` block naming the older note it presses against. The Editor should read these.

### The verification market contradicts itself in nine places

1. **Countries: 153 vs 180 vs 111.** 5sim's home says "more than 180 countries"; its own country selector says "Show all 153"; the prices CSV covers 111. Three figures, one site.
2. **Service count: 1329 vs 1221.** The home claims 1329 services; the catalog body only enumerates 1221 unique names.
3. **Price floor: $0.008 vs $0.1026.** The home anchors at "$0.008"; the measured Telegram floor in the CSV is $0.1026 — 12.8× higher.
4. **Stock counters exceed the global claim.** "Over 500,000 numbers" on the same page as per-service counters in the hundreds of millions.
5. **OpenAI floor: $0.01 vs $0.05.** The generic selector says "from $0.01"; the OpenAI product page says "Price from $0.05".
6. **Three incompatible refund promises.** 5sim home: "Instant refunds". 5sim service page: "up to 15 minutes". HeroSMS: 20 minutes. At most one can be true.
7. **HeroSMS reproduces 5sim's exact marketing numbers** — "500K+ numbers", "180 countries" — for a different brand. Either a shared source (SMS-Activate's) or a copy.
8. **SMS-Activate's closure contradicts the "HeroSMS is a facade" reading.** If SMS-Activate ceased all activity on 22 December, there is no live operator behind the facade.
9. **OpenAI's IA category is 28 services at 5sim and 1 at HeroSMS.** The same category cannot have two different depths; either the catalogs differ or one is a marketing artifact.

### Against the vault's own beliefs

10. **The cost model has no infrastructure line and no per-signup line.** [[2026-1022-costes-por-categoria-tenant]] splits spend into tenant-billable inference and platform-absorbed ops. Hetzner's cheapest viable plan is €5.99/month — above the vault's ≤ €4/month budget — and a verification step, if added, is a marginal cost per signup. Neither fits the model as written.
11. **The per-provider cost panel only measures API-by-token.** A flat subscription (ChatGPT Plus, a Token Plan, OpenCode Go at $10/mo) is a different unit, and the panel cannot see it.
12. **"Isolation" is not what the field means by isolation.** The curated tooling list routinely qualifies agent runtimes as *not* providing complete isolation; the entity note claims "aislamiento completo entre tenants". At most one is right.
13. **Telemetry on by default with a persistent ID is now normal practice** — which reframes the public Sentry DSN as either a configuration slip or a real unauthenticated write channel.
14. **The AI-triage layer presupposes the observability the product does not have.** The gap may be smaller than it looks, or larger — the vault cannot resolve it from here.
15. **"分组" means two different things** — PriceAI's monitoring grouping vs new-api's routing group. The multiplier comparison is only valid if the measurement base is comparable; it may not be.
16. **The legal notice still declares Vercel and Neon** while the site is self-hosted on nginx. Identity was updated; the hosting declaration was not.
17. **The copy says "recomienda productos"; the code calls it `sales`.** Both can be true — and the mismatch is the finding.
18. **The onboarding offers a `.myownclone.yourdomain.com` suffix** with no visible resolution path, against a field the vault recorded as inactive.

### Between the new material and the old live state

19–44. The remaining 26 are narrower: the relay's legal posture for public resale (AGPLv3 §7 attribution, upstream ToS), the midjourney-proxy ecosystem's captcha-circumvention apps against the vault's own legal-surface atom, the priceai sponsored placement sitting in the same table as the ranking (neutrality claim vs. shared content), the six dead products in the 卡网 table, the token-counting drift in new-api's `tokenkit` (31–93 % undercount against 54 real windows), the lzt capture being a failed fetch, the Hetzner €4 budget gap, and the security-surface items listed in the thread.

## Threads

**Created:** `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` — the market's shape, unit economics, reliability, what it means for the product, Hetzner as the one clean anchor, and eight unresolved frictions. It states plainly that the vault *records* this market and does not endorse it.

**Updated:**
- `myownclone-estado-live-2026-10.md` — six new rows in the delta table, a section on what the re-verification added, four new frictions (#6–#9).
- `myownclone-platform-architecture.md` — new section "La capa de inferencia: entre API propia, gateway y relay": the current single-pointer `OPENAI_API_BASE`, the anatomy of a gateway, the relay market from the aggregator's side, the midjourney-proxy archetype, and the build-vs-buy reading.
- `myownclone-security-surface.md` — new section "El mapa del campo": the 15-category taxonomy, which categories apply to a multi-tenant AI SaaS, the three frictions, the honest limits of the source.
- `myownclone-gtm-monetization-roadmap.md` — new section "El coste real de un alta y de un mes de servicio" with a cost-line table, the live onboarding (no SMS step; domain suffix template), four stale claims corrected, seven new frictions.
- `myownclone-vs-myclone-is.md` — what the product already has that the competitor comparison does not capture.

## Errors and deviations

- **No capture was edited.** All 18 were moved intact to `0-raw/archive/2026-10-23-*.md`.
- **Three atoms were retired mid-run** (`new-api-control-de-acceso-y-autenticacion`, `new-api-ecosistema-proveedores-y-herramientas-derivadas`, `new-api-flujo-de-alta-canal-test-precio-y-key`) because a later sibling atom covered the same idea better. They were merged, marked `[RETIRED]` and moved to `2-atoms/archive/` — not deleted, per house rule #5.
- **No atom was deleted at any point.** `git status` shows zero deleted tracked files.
- **One subagent initially deleted two atoms it had just created.** The content was recovered and merged into sibling atoms before the run ended; final state is `2-atoms/archive/` with the content preserved. Flagging it because the house rule forbids deletion and the subagent should have merged instead.
- **The `sources:` paths of the 15 live-verification atoms were updated** to the archived capture path (`0-raw/archive/2026-10-23-…`) so that every source reference resolves. Verified: 0 unresolvable source paths vault-wide.
- **Counts quoted in the AI-security atoms** (377 tools, 15 categories, 61 runtime entries) are the reader's own counts of the README, not published metrics. The atoms say so explicitly.

## Needing human attention

1. **The price AI would actually pay.** Hetzner's cheapest shared plan is €5.99/month; the vault's stated budget is ≤ €4/month. Either the budget moves or the architecture changes. This is a decision, not a research question.
2. **Whether phone verification is ever wanted.** The live `/registro` has no SMS step. If that is deliberate, the whole verification market is adjacent background. If it is accidental, this thread becomes a roadmap input — and it comes with ToS exposure, VoIP blocking, and scam-brand baggage.
3. **The `myownclone_public_bp` chat endpoint is still 404.** The midjourney-proxy atoms make the same structural point from the outside: when there is no official API, someone builds an unofficial bridge. Either the blueprint is registered or the public chat surface stays dead.
4. **The legal notice's hosting declaration.** It names Vercel and Neon; the site is nginx on `212.227.169.99`. A compliance document that misstates the processor is a small but real liability.
5. **The 44 frictions.** They are grouped in the atoms by pair. The Editor run should triage them; a few (the three country counts, the three refund promises) are the same underlying marketing-vs-measurement gap and can be resolved together.
