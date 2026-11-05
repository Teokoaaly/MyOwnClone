---
id: 2026-1101-clerk-billing-07-por-ciento-encima-de-stripe
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1022-myclone-stripe-connect-monetizacion]]", "[[2026-1022-costes-por-categoria-tenant]]"]
---

## Claim
El add-on **Billing** de Clerk está incluido en todos los planes y se cobra con **0,7% del volumen facturado**, de forma que el coste total de cobro es **"Stripe 2,9% + Stripe transaction charge $0,30 + Clerk Billing 0,7%"**. Incluye todo lo de subscription billing, y **el billing por uso y por asiento está "coming soon"**.

## Why It Matters
Es la única línea de la página de Clerk que **escala con el MRR del cliente, no con el número de usuarios**, y por tanto la única que puede quedarse dormida: 0,7% sobre el volumen facturado es invisible hasta que el producto factura miles de euros. Para MyOwnClone, que ya monetiza vía **Stripe Connect** ([[2026-1022-myclone-stripe-connect-monetizacion]]), el dato relevante es el **stack de cobro completo**: 2,9% de Stripe + $0,30 por transacción + 0,7% de Clerk = **3,6% más $0,30 por cobro**, y una **comisión por cobro** que en un modelo multi-tenant con micro-pagos por clon puede multiplicarse. La conclusión operativa es doble: **Clerk Billing no aporta hoy nada imprescindible (Stripe ya cubre la suscripción) y encarece cada cobro**, así que su uso real solo tiene sentido si la UI de suscripciones ahorra más en churn que lo que cuesta; y para el eje del vault, esta es la línea que **no es ni asiento ni infra, sino un porcentaje sobre el negocio** — una tercera categoría de coste que conviene no mezclar con el TCO de infraestructura al comparar proveedores.

## Nota de verificación
Sección "Billing" de la captura del 2026-11-01: "Included in all plans / 0.7% of billing volume / Stripe 2.9% + Stripe transaction charge $0.30 + Clerk Billing 0.7%" y "usage and per seat billing coming soon". La lectura sobre Connect y el TCO es interpretación de este átomo.
