---
id: 2026-1101-auth0-definicion-de-mau-y-cobro-al-escalon-superior
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-platform-admin-tenants-costes-mrr]]"]
---

## Claim
Auth0 define MAU como "Any non-internal (non-employee) user that authenticated during a given month for a given tenant" y cobra **por escalón superior**: "Pricing is available only at the listed MAU tiers. If your usage falls between tiers, you are billed at the next tier up." El MAU se cuenta **por tenant**, no de forma agregada.

## Why It Matters
Dos consecuencias prácticas para el modelado de coste del vault. Primera: los empleados internos no cuentan como MAU, así que el equipo propio de MyOwnClone no infla el contador — pero cualquier cuenta de cliente que autentique una vez en el mes lo hace. Segunda, y más importante: el cobro al escalón superior crea un **escalón discreto de coste** — pasar de 500 a 1.001 MAU en B2B Essentials salta de $150 a $300/mes aunque solo se tenga un usuario por encima del umbral. Combined con el conteo **por tenant**, esto significa que el agregado de MAU de la plataforma es la suma de los tenants: un solo tenant grande puede empujar a toda la cuenta al siguiente escalón. Es exactamente el tipo de partida que hoy no aparece en el corte de [[2026-1022-costes-por-categoria-tenant]] ni en el panel de MRR de [[2026-1022-platform-admin-tenants-costes-mrr]], y por eso es la línea que hay que medir antes de comprometer un proveedor de identidad para el SaaS multi-tenant.

## Nota de verificación
La definición de MAU y la regla de escalón superior son lectura literal de la tabla de precios del 2026-11-01. La inferencia sobre el efecto de escalón en un entorno multi-tenant es lectura de este átomo, no frase de la fuente.
