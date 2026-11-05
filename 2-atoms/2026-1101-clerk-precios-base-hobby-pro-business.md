---
id: 2026-1101-clerk-precios-base-hobby-pro-business
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1031-clerk-pricing]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Los precios base de Clerk son: **Hobby $0** (sin tarjeta de crédito), **Pro $25/mes o $20/mes facturado anualmente**, **Business $300/mes o $250/mes facturado anualmente**, y **Enterprise "Custom", facturado solo anualmente**. Todos los planes incluyen **aplicaciones ilimitadas**; el salto de Hobby a Pro no es por número de apps sino por cuota de MRU.

## Why It Matters
Coloca a Clerk en la misma escala de coste que Auth0 y muy por encima del presupuesto de infraestructura del vault: **$20/mes es cinco veces el presupuesto entero de ≤ €4/mes** que ya está tensionado por el suelo de €5,99 de Hetzner ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). Es decir, en el eje "identidad vs infraestructura" ([[2026-1022-costes-por-categoria-tenant]]), la identidad es la partida que puede multiplicar por 5 el TCO con un solo proveedor: 8 €/mes de infra barata + 20 $/mes de Clerk > 6x el presupuesto. Para MyOwnClone eso significa que **Clerk solo es viable en el tramo Hobby ($0) o con NextAuth propio**, y que el punto de decisión no es "Clerk vs Auth0" sino "provider vs librería".

## Nota de verificación
Cifras verbatim de la tabla "Full price breakdown" de la captura del 2026-11-01 (fila "Base price"). La comparación con Auth0 es lectura operativa de este átomo a partir de [[2026-1101-auth0-precios-por-mau-no-por-evento]].
