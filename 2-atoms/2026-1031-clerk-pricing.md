---
id: 2026-1031-clerk-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-clerk-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
Clerk includes all authentication and user management features across every pricing tier without feature gating, unlike typical auth providers that lock advanced features (SMS, social connections, usernames) behind higher plans.

## Why It Matters
Most auth providers use tiered feature gating where SMS, social connections, and advanced usernames are restricted to Pro/Business plans. Clerk's universal feature inclusion across Hobby, Pro, and Business tiers simplifies cost modeling for SaaS products, since the per-user cost is predictable regardless of feature adoption. This validates the per-seat cost model when auth is a core dependency, as there's no need to budget for feature-tier upgrades as the user base grows.

## [FRICTION]
> [[2026-1027-proton-business-vpn-descuentos-por-plan-sin-precio-de-renovacion-publicado]] notes that discount availability may vary by plan without published renewal pricing. While Clerk includes all features at all tiers, the lack of published renewal-rate discounts could create budgeting uncertainty for long-term deployments, unlike plans that advertise locked-in pricing periods.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-11-01-clerk-pricing.md` y `sources/2026-11-02-clerk-pricing.md` (capturas completas de clerk.com/pricing, con la tabla "Full price breakdown" y la FAQ de precios). El **Claim** de este átomo no se reescribe aquí: el conflicto queda documentado en [[2026-1101-clerk-gating-por-plan-contradice-atom-1031]], que lleva un bloque `## [FRICTION]` contra este átomo.

Dato nuevo y verificable: la página de precios **sí** publica una matriz de features por plan con gating explícito, y los precios base son **Hobby $0, Pro $25/mes o $20/mes anual, Business $300/mes o $250/mes anual, Enterprise custom (solo anual)** ([[2026-1101-clerk-precios-base-hobby-pro-business]]). Clerk **no factura por MAU sino por MRU** (usuario que vuelve ≥24 h después del alta, "First Day Free") y por **MRO** en las organizaciones ([[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]], [[2026-1101-clerk-organizaciones-100-mro-y-20-miembros-gratis]]). El add-on B2B Authentication y el Administration cuestan **$100/mes o $85/mes anual** ([[2026-1101-clerk-addon-b2b-85-o-100-por-mes]]), las conexiones SSO adicionales **$75/mes** la segunda y el Directory Sync empieza a facturarse el **1 de enero de 2027** ([[2026-1101-clerk-sso-adicional-desde-75-por-conexion]], [[2026-1101-clerk-directory-sync-facturacion-desde-enero-2027]]). El SMS cuesta **$0,01 en US/CA** y "market rate" en internacional, sin cifra publicada ([[2026-1101-clerk-sms-001-dolar-por-sms]]), y la duración de sesión en Hobby está **fijada a 7 días** ([[2026-1101-clerk-sesion-fija-7-dias-en-hobby]]).

Consecuencia para el eje abierto del vault: **Clerk tiene el mismo tipo de gating por plan que Auth0** (contra lo que afirmaba este átomo), pero con un **primer escalón de pago mucho más barato** ($20 vs $35/$150 de Auth0). En coste, sus líneas variables son por **MRU** y por **MRO** —es decir, por usuario retenido y por organización retenida—, y solo una línea es porcentaje sobre el negocio (Billing, 0,7%). Las capturas del 2026-11-01 y del 2026-11-02 son idénticas salvo la fecha ([[2026-1102-clerk-precios-sin-cambios-en-48-horas]]).