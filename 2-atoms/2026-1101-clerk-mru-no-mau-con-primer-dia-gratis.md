---
id: 2026-1101-clerk-mru-no-mau-con-primer-dia-gratis
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1031-clerk-pricing]]", "[[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]"]
---

## Claim
Clerk **no factura por MAU sino por MRU (Monthly Retained Users)**: un usuario solo cuenta como retenido si vuelve a la app **al menos 24 horas después de registrarse** ("First Day Free"), y las organizaciones se cuentan como MRO solo si tienen **≥2 miembros y al menos uno de ellos es un MRU del mes**. Superar **50.000 MRU obliga a subir al plan Pro** (con **un mes de gracia**); superar **100 MRO obliga a comprar el add-on B2B Authentication**.

## Why It Matters
Es la diferencia de métrica que decide el lado del eje abierto del vault (**coste por asiento vs coste por infraestructura**): frente al MAU de Auth0 ([[2026-1101-auth0-precios-por-mau-no-por-evento]], [[2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior]]), Clerk cobra por *retención*, no por actividad. Para MyOwnClone, donde los tenants son clones de IA y muchos usuarios se registran y vuelven al día siguiente para iterar prompts, **la distancia entre MAU y MRU es la variable a medir**: si la app se usa en ráfagas (registro → varias sesiones en 24 h → abandono), el MRU puede estar muy por debajo del MAU y el coste efectivo de Clerk baja; si el churn es bajo, MRU≈MAU y se paga lo mismo. El "primer día gratis" también elimina el peaje típico del signup masivo por referidos, que en Auth0 sí computa desde el primer día.

## Nota de verificación
Definiciones verbatim de la sección "Questions & answers about our pricing" de la captura del 2026-11-01: "Clerk pricing is based on Monthly Retained Users (MRU), not traditional MAU" y "you will be required to upgrade to the Pro plan... You'll be given a one-month grace period".
