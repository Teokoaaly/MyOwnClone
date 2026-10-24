# Refinery Report — 2026-10-24

Run: 03:00 shift (scheduled cron).

## The anomaly this run had to fix first

The Scout of 2026-10-23 fetched **19 sources** into `sources/` and then **skipped its capture-pointer step**. Result: 19 full sources on disk with **zero atomic notes** and zero provenance pointers in `0-raw/`. The Refinery of the previous night processed 18 captures; this one inherited an empty `0-raw/` and a full set of orphans.

Repair performed before atomization: the 19 missing Scout Step 4 capture pointers were regenerated in `0-raw/` (title + `Source:` path, `Status: ready`), so every new atom has a valid provenance path. Sources themselves were never touched — read-only throughout.

## Captures processed

All 19 orphaned sources were atomized and their pointers archived to `0-raw/archive/2026-10-24-<name>.md`. `0-raw/` now holds only `reading-list.md` and `archive/`.

| # | Source | Atoms referencing it |
|---|---|---|
| 1 | `2026-10-23-evoxt-vps-pricing` | 21 |
| 2 | `2026-10-23-evoxt-vms` | 19 |
| 3 | `2026-10-23-skhron-bitcoin-vps` | 18 |
| 4 | `2026-10-23-hostbrr-vps-pricing` | 17 |
| 5 | `2026-10-23-hostkey-bitcoin-vps` | 16 |
| 6 | `2026-10-23-extravm-vps-pricing` | 16 |
| 7 | `2026-10-23-2captcha-solver` | 15 |
| 8 | `2026-10-23-buyvm-kvm-slices` | 15 |
| 9 | `2026-10-23-hostbrr-home` | 14 |
| 10 | `2026-10-23-lowendbox-2-usd-vps` | 20 |
| 11 | `2026-10-23-lowendbox-1-usd-vps` | 12 |
| 12 | `2026-10-23-extravm-crypto-vps` | 12 |
| 13 | `2026-10-23-dataimpulse-proxies` | 11 |
| 14 | `2026-10-23-veridrop-relays` | 11 |
| 15 | `2026-10-23-noones-limits-and-verification` | 9 |
| 16 | `2026-10-23-notletters-mail` | 7 |
| 17 | `2026-10-23-noones-p2p` | 4 |
| 18 | `2026-10-23-new-api-calcium-ion-redirect` | 3 |
| 19 | `2026-10-23-noones-blocked-jurisdictions` | 3 |

## Totals

| Metric | Count |
|---|---|
| Captures processed | 19 |
| Atoms created | 170 (all prefixed `2026-1024-`) |
| Existing atoms extended | 40+ (patched with `## [NOTA 2026-10-24]` + source refs) |
| Atoms retired to `2-atoms/archive/` | 2 (moved, never deleted) |
| Friction blocks in the vault | 115 atoms carry a `## [FRICTION]` block |
| Threads created | 1 |
| Threads updated | 4 |
| Broken wikilinks (`2-atoms/` + `3-threads/`) | 0 |
| Orphaned sources | 0 |
| Tracked files deleted | 0 |
| Credentials leaked into notes | 0 |

`2-atoms/` went from 299 to **469** notes.

## Threads

- **NEW** `3-threads/escala-de-hosting-barato-y-el-limite-de-4-euros.md` — the cheap-hosting price scale across Hetzner, Evoxt, ExtraVM, HostBrr, Hostkey, Skhron, BuyVM and LowEndBox; what each plan buys and what it silently drops (SLA, egreso, backups, DDoS, IPv4, certificaciones). 9 sections, 75 wikilinks, 9 frictions.
- `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md` — new §7 decomposes the cost of an alta by insumo (email ≪ captcha ≪ proxy ≪ SMS), plus 5 new frictions (now 13 total). Thread grew 56 KB → 78 KB.
- `3-threads/el-agregador-de-precios-como-producto.md` — new §7 on VeriDrop as a second, non-mergeable inventory of the same relay market, plus the new-api owner rename; 5 new frictions (now 10).
- `3-threads/myownclone-platform-architecture.md`, `3-threads/myownclone-vs-myclone-is.md` — extended in earlier batches of this same run (midjourney-proxy editions, deployment cost).

## Frictions raised (24 pairs, for the Editor / for a human)

### Hosting scale
1. **ExtraVM's headline price is not buyable.** "$4.50 starting at" is a Sold Out plan; the cheapest actually purchasable is $8.00/mo. `2026-1024-extravm-stock-casi-todo-agotado-y-solo-cinco-planes-comprables` ↔ `2026-1024-extravm-mismo-precio-que-tarjeta-sin-recargo-cripto`
2. **Skhron hits the €4 budget on price and fails on capacity** — €2.34 but 512 MiB / 0.06 vCPU. `2026-1024-skhron-precios-2-34-a-177-65` ↔ `2026-1023-hetzner-presupuesto-4-euros-no-alcanza`
3. **BuyVM sells "dedicated" with fair-share** in 3 of 4 slices, contradicting "Absolutely no overselling". `2026-1024-buyvm-slices-modelo-dedicado-fraccionado-con-cpu-fair-share` ↔ `2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso`
4. **Hostkey contradicts itself**: body requires KYC and routes through BitPay, FAQ on the same URL says identity verification is usually not required. `2026-1024-hostkey-kyc-obligatorio-y-procesamiento-via-bitpay` ↔ `2026-1024-hostkey-faq-cripto-sin-verificacion-bancaria`
5. **ExtraVM has no legal uptime guarantee** — only credits — against Hetzner's auditable SLA. `2026-1024-extravm-sin-garantia-legal-de-uptime-solo-creditos` ↔ `2026-1023-hetzner-sla-99-9-gdpr-e-iso-27001`
6. **Egress models are not comparable without normalizing direction**: Hetzner bills egress at €1/TB, Skhron counts entry + exit, ExtraVM caps 3–40 TB. `2026-1024-skhron-trafico-contado-en-dos-sentidos` ↔ `2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra`
7. **IPv4 at €0 vs €0.65/month.** `2026-1024-skhron-ipv6-enrutado-64-y-56-gratis-e-ipv4-addon-0-65` ↔ `2026-1023-hetzner-ipv4-primario-incluido-o-costo-cero`
8. **LowEndBox's "$1 VPS" article claims a ~$120/yr floor; the "$2 VPS" article publishes $16.88–$23.88/yr.** `2026-1024-lowendbox-2-usd-escalon-16-88-a-23-88-al-ano` ↔ `2026-1024-lowendbox-vps-anuales-de-10-a-11-dolares-no-mensuales`
9. **The LowEndBox $2 article is dated "Updated September 2026"**, while its $1 twin says "Updated July 2026". `2026-1024-lowendbox-2-usd-articulo-abril-2020-actualizado-septiembre-2026` ↔ `2026-1024-lowendbox-lowend-score-cinco-estrellas-como-filtro`
10. **ExtraVM's 7 of 8 datacenters share one ASN (AS53724)** — facility diversification is not upstream diversification.
11. **Evoxt's "Plans" and "Benchmark Score" tables disagree** (VM-1: $5.99 vs $9.99) and no billing period is published.

### Verification market
12. **NoOnes contradicts itself**: prose says level 2 has "no daily or lifetime limits whatsoever"; the table says Daily Limit = $100K. `2026-1024-noones-nivel-2-sin-limites-diarios-y-100k-por-operacion` ↔ `2026-1024-noones-tabla-de-limites-por-nivel`
13. **NoOnes does not serve Spain** (MiCA, 30 countries removed since July 2026) — the vault operates in ES. `2026-1024-noones-mica-30-paises-no-servidos-desde-julio-2026` ↔ `2026-1022-i18n-es-first-jurisdiccion-es`
14. **NoOnes explicitly forbids the core technique of the SMS playbook** (obfuscating IP / location). `2026-1024-noones-prohibicion-explicita-de-circular-restricciones-por-ip-y-ubicacion` ↔ `2026-1023-hero-sms-ip-y-vpn-coincidentes-con-el-pais-del-numero`
15. **The email floor is not comparable**: ¥0.02 (PriceAI) vs 0.05 ₽ (NotLetters) — different currency and unit.
16. **2Captcha publishes hCaptcha and Geetest as absent from its public catalog**, i.e. the catalog is not exhaustive.

### Relay / counterparty
17. **VeriDrop publishes a denominator where PriceAI left it heterogeneous** — the two inventories are not comparable without a bridge source. `2026-1024-veridrop-concentracion-de-muestras-en-tres-relays` ↔ `2026-1023-priceai-transit-disponibilidad-7d-con-denominadores-heterogeneos`
18. **The `边缘` (edge) state does not exist in PriceAI's binary taxonomy** — metrics do not align. `2026-1024-veridrop-tercer-estado-edge-y-su-dispersion` ↔ `2026-1023-priceai-transit-dispersion-de-multiplicadores`
19. **The PRO badge does not rank by activity** — 4 non-PRO rows outrank `91token.com` on accumulated tests.
20. **new-api's owner rename (`Calcium-Ion` → `QuantumNous`) makes stored `Calcium-Ion/...` paths obsolete** and touches AGPLv3 §7 attribution in the UI. `2026-1024-new-api-redirect-calcium-ion-a-quantumnous` ↔ `sources/2026-10-22-new-api-github.md`
21. **48 of 50 VeriDrop relay domains are low-friction foreign TLDs** with no operator identity — a counterparty-continuity risk for `OPENAI_API_BASE` that is independent of model quality.

### Cost model
22. **Proxy traffic does not fit any of the vault's three cost categories** — it is variable and per-GB. `2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy` ↔ `2026-1022-costes-por-categoria-tenant`
23. **IP rotation has two incompatible fixes**: floating IP on a VPS (fixed cost) vs a proxy pool per GB (variable + per-country geo). `2026-1024-dataimpulse-sesiones-rotating-y-sticky` ↔ `2026-1024-evoxt-ip-management-floating-ip-y-reasignacion`
24. **Captcha is 100–10,000× cheaper than SMS per unit** — a new line item in the alta cost model, and a category the vault did not have.

## Errors and things needing human attention

- **Concurrency incident (repaired):** three subagents patched the shared atom `2026-1023-hetzner-presupuesto-4-euros-no-alcanza.md` concurrently. One agent's patch dropped two sibling source entries; it detected the warning and restored them. Final state verified — the `sources:` list retains all entries.
- **Defects fixed in passing:** two CJK corruptions in Spanish prose in existing NoOnes atoms (`mercado欧美`, `una变量的`), an unbalanced parenthesis and one broken wikilink in the VeriDrop atoms. No content was lost.
- **Duplicate atom retired:** `2026-1024-2captcha-16-y-17-segundos-los-tipos-lentos` duplicated three existing latency atoms; marked `certainty: retired` and moved to `2-atoms/archive/`, links repointed to the survivors.
- **Pre-existing broken links outside the refinery's scope:** 49 broken `[[wikilinks]]` remain in `entities/`, `concepts/`, `comparisons/`, `raw/articles/` and older `briefings/` (mostly `[[delfi]]` and `[[leader-sumaris]]`, which have never existed as notes). `2-atoms/` and `3-threads/` are clean at 0. Left for the Editor — creating those two entity notes is a content decision, not a refinery one.

## Fidelity notes (things the sources do NOT say)

- BuyVM's page does not mention Amsterdam, Miami, Stockholm or Frankfurt; only Las Vegas, New York and Roost/Luxembourg. No SLA, no stock per plan, no payment methods, no crypto.
- Hostkey publishes no VPS price table — only dedicated servers from €23.
- NoOnes' p2p page is a jurisdiction-block page; it yields only the blocking fact, not a catalogue.
- VeriDrop publishes **no prices, no software field** — protocol, verdict, freshness and window only.
- The new-api capture is a verification note about a redirect; it deliberately does not duplicate the README captured on 2026-10-22.
- NotLetters' capture contains no domains, no limits, no retention terms and no SLA; an explicit "absence" atom was written instead of an invented catalogue.

## Method

Five delegated batches, grouped by provider to avoid same-provider filename collisions (the Evoxt pair clashed in batch 1; later batches grouped ExtraVM, HostBrr, Hostkey, Skhron, LowEndBox, NoOnes and VeriDrop). Each subagent received the full house rules, the source path as ground truth, the "extend don't duplicate" protocol, and the instruction to leave genuinely ambiguous merges flagged rather than force resolution. Validation after every batch: Git deletion check, vault-wide wikilink resolution, and per-source atom-reference audit. Final audit: 0 orphans, 0 broken links in `2-atoms/` and `3-threads/`, 0 tracked deletions, `0-raw/` empty except the reading list.
