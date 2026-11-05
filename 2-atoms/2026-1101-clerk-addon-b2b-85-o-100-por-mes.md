---
id: 2026-1101-clerk-addon-b2b-85-o-100-por-mes
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-organizaciones-100-mro-y-20-miembros-gratis]]", "[[2026-1101-clerk-sobrecoste-mro-por-tramos]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]"]
---

## Claim
Los **add-ons mejorados** de Clerk cuestan **$100/mes o $85/mes facturado anualmente**, y ese precio es el mismo para los dos: **B2B Authentication Enhanced** (miembros ilimitados por organización, enlace de conexiones Enterprise con organizaciones, Verified Domains & Automatic Invitations, roles y rolesets custom) y **Administration Enhanced** (impersonaciones ilimitadas frente a 5 gratis al mes).

## Why It Matters
Fija el precio de la **capa de gestión de tenants**, que es exactamente la función que MyOwnClone necesita para operar un panel de tenants ([[2026-1022-platform-admin-tenants-costes-mrr]]): límites de miembros, dominios verificados, roles custom e invitaciones. **$85-100/mes es 21-25x el presupuesto de hosting de ≤ €4/mes**, así que el add-on B2B queda descartado por precio mientras el producto sea pequeño, y la consecuencia es que **la gestión de organizaciones quedaría en el nivel gratuito**: 20 miembros por organización, roles Admin/Member, sin Verified Domains ni auto-invitaciones. Eso es un límite de producto, no solo de presupuesto: sin Verified Domains el alta multi-tenant exige invitación manual, que es fricción operativa real en la conversión de clientes B2B.

## Nota de verificación
Precios verbatim de las tarjetas "Enhanced add-on" de las secciones B2B Authentication y Administration de la captura del 2026-11-01 ("$100/mo or $85/mo billed annually"). La comparación con el presupuesto de €4/mes es lectura operativa del átomo.
