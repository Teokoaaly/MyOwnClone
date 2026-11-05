---
id: 2026-1101-auth0-precios-por-mau-no-por-evento
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1031-auth0-pricing]]", "[[2026-1031-clerk-pricing]]", "[[2026-1031-workos-pricing]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
Los planes de pago de Auth0 se cobran **por usuarios activos mensuales (MAU)**, no por evento de autenticación: "Paid plans are priced by Monthly Active Users (MAUs) and differ between B2C and B2B", con cuatro niveles (Free, Essentials, Professional, Enterprise), el Free idéntico para B2C y B2B hasta 25.000 MAU y los pagados tarifados por tramos de MAU (500, 1.000, 2.500, 5.000, 7.500, 10.000, 20.000, 30.000+).

## Why It Matters
Esto fija el modelo de coste con el que hay que comparar al resto de candidatos del vault: Auth0 es **per-seat por MAU**, igual que el modelo de referencia de [[2026-1022-costes-por-categoria-tenant]], y no un modelo por uso como el híbrido de [[2026-1031-workos-pricing]] ni el modelo "todo incluido sin gating" de [[2026-1031-clerk-pricing]]. La consecuencia práctica para MyOwnClone (SaaS multi-tenant con NextAuth 5): el coste de identidad escala con los usuarios activos reales de los tenants, no con los eventos de login, así que un tenant con 50 usuarios que hace 500 logins al mes paga lo mismo que uno con 50 usuarios que hace 50 logins — y por eso el eje relevante para el budget de ≤ 4 EUR/mes es el **número de MAU agregados**, que es el que se tiene que medir antes de elegir proveedor.

## [FRICTION]
> [[2026-1031-auth0-pricing]] (escrita el 2026-10-31) afirma que "Auth0's pricing is per-authentication-event with volume-based tiers, where cost scales with the number of authentication transactions rather than per-user seats, creating a different cost structure than per-seat SaaS tools".
> Este átomo presiona esa creencia porque la página de precios de Auth0 —tanto en la captura del 2026-10-31 ("How many monthly active users?", "Up to 25,000 monthly active users", "Up to 500 monthly active users") como en la del 2026-11-01 ("Paid plans are priced by Monthly Active Users (MAUs)")— **tarifa explícitamente por MAU**. No hay ninguna tabla de precios por evento de autenticación en ninguna de las dos fuentes.
> Ambas no pueden ser completamente correctas: o el átomo anterior leyó mal la página y confundió el contador de MAU con un contador de eventos, o existe una métrica de eventos (M2M, CIBA, llamadas API) que se factura aparte y no aparece en la página de precios. Marcado para juicio humano, no auto-resuelto.
