---
id: 2026-1022-beta-activo-trafico-real
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-scrape_web-scrape.md]
links: ["[[myownclone]]", "[[eugenio-oller]]", "[[2026-1022-superficie-oculta-robots-txt]]", "[[2026-1022-onboarding-manual-sin-self-service]]", "[[2026-1022-stripe-webhook-confirmado]]"]
---
## Claim
Según el informe, [[myownclone]] está en beta activo con tráfico real: hay signups, MRR, pagos fallidos y cancelaciones en el panel de tenants, y el coste se desglosa por tenant (responses, words, period cost, lifetime cost). El recon de bundles matiza el alcance del onboarding: las rutas de signup (`/registro`, `/en/signup`, `/en/signup/onboarding`, `/en/signup/success`) existen y son rastreables, pero el propio informe las describe como **beta con onboarding manual caso por caso**.
El scrape HTTP del 2026-05-25 corrobora que hay facturación en producción (`/api/webhooks/stripe` → 405, ver [[2026-1022-stripe-webhook-confirmado]]) pero que no hay signup público: `/registro` hace meta-refresh a `/contacto` y el onboarding es caso por caso (ver [[2026-1022-onboarding-manual-sin-self-service]]).

## Why It Matters
Un MRR con cancelaciones y pagos fallidos es la única señal de vida comercial del producto en toda la investigación: distingue "beta cerrada con cero ingresos" de "beta facturando". Es el dato que más pesa frente a las tesis de mercado immature de [[eugenio-oller]] y los competidores. La coexistencia de un signup público y un onboarding manual es el matiz que evita inferir self-service: el funnel existe, la asignación de plan y el alta real los hace una persona — ver el reconocimiento de rutas en [[2026-1022-superficie-oculta-robots-txt]].

## [FRICTION]
> [[myownclone]] (nota de entidad, escrita hace ~21 semanas) afirma en su sección "Traction" que la beta es cerrada y sin self-service, ya que `/registro` redirige a `/contacto`.
> Esta nota presiona eso porque el informe técnico lista `/registro` (signup) como ruta pública, describe el flujo de signup y muestra signup, MRR, pagos fallidos y cancelaciones en el panel de tenants, es decir, señal de onboarding self-service y facturación activa.
> Ambas no pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.
