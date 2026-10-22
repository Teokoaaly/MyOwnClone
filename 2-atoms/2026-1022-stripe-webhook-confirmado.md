---
id: 2026-1022-stripe-webhook-confirmado
type: atom
certainty: solid
sources: [raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1022-beta-activo-trafico-real]]"]
---
## Claim
El endpoint `/api/webhooks/stripe` de [[myownclone]] existe y devuelve **HTTP 405 Method Not Allowed** (solo acepta POST), lo que confirma en el sitio público que Stripe está integrado para pagos aunque no haya página de precios. En el bundle solo aparecen rutas de API propias del SDK de PostHog (`/e/`, `/decide/`, `/array/`, `/replay/`…), no endpoints REST de negocio expuestos al cliente.

## Why It Matters
Es la única prueba directa y falsable de que la facturación existe en producción, y la respalda el dato de Stripe de [[2026-1022-stripe-planes-trial-30-dias]] y el MRR de [[2026-1022-beta-activo-trafico-real]] con un artefacto verificable, no con una afirmación. Al mismo tiempo, muestra que la capa de negocio no es consumible desde fuera: la monetización existe pero es opaca.
