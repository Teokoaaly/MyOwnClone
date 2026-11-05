---
id: 2026-1031-auth0-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-auth0-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Auth0's pricing is per-authentication-event with volume-based tiers, where cost scales with the number of authentication transactions rather than per-user seats, creating a different cost structure than per-seat SaaS tools.

## Why It Matters
Auth0's event-based pricing means costs can compound unpredictably as authentication volume grows, unlike per-seat models where cost scales linearly with user count. For products with high authentication frequency per user, Auth0 can become more expensive than per-user alternatives. This friction is relevant when comparing against the per-seat dominance model validated in `costes-por-categoria-tenant`, since Auth0's cost depends on transaction volume rather than user count alone.

## [FRICTION]
> [[2026-1024-protonvpn-plus-3-49-al-mes-65-de-descuento]] observes that protonvpn-plus pricing includes a 65% discount that changes the cost structure significantly. While Auth0's event-based pricing scales with volume, Proton's per-user pricing scales with user count. Both cannot be the dominant cost model for the same product — the choice between event-based vs. per-seat pricing depends on whether authentication events per user are high or low, which requires measuring the events-per-user ratio before committing to a pricing model.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-11-01-auth0-pricing.md` y `sources/2026-11-02-auth0-pricing.md` (capturas más completas de auth0.com/pricing, con tablas de precios por MAU y feature matrix B2C/B2B). El **Claim** de este átomo no se corrige aquí: se deja tal cual y el conflicto queda documentado en [[2026-1101-auth0-precios-por-mau-no-por-evento]], que lleva un bloque [[FRICTION]] contra este átomo.

Dato nuevo y verificable: la página de precios de Auth0 **tarifa explícitamente por MAU** ("Paid plans are priced by Monthly Active Users (MAUs)"), con Free hasta 25.000 MAU a $0, Essentials B2C desde $35/mes y B2B desde $150/mes en el escalón de 500 MAU, Professional B2C desde $240/mes y B2B desde $800/mes, y cobro por escalón superior ("you are billed at the next tier up"). Los precios son idénticos en las capturas del 2026-11-01 y del 2026-11-02.

Consecuencia para el vault: si la afirmación de "event-based pricing" de este átomo se sostiene, no describe el modelo de Auth0 (que es per-MAU, como el de [[2026-1022-costes-por-categoria-tenant]]) sino, como mucho, el de [[2026-1031-workos-pricing]] (por producto y llamada API) o el de [[2026-1031-clerk-pricing]] (per-seat sin gating). Marcado para juicio humano, no auto-resuelto.