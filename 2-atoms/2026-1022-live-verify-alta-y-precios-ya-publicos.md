---
id: 2026-1022-live-verify-alta-y-precios-ya-publicos
type: atom
certainty: solid
sources: [0-raw/archive/2026-10-23-2026-10-22-myownclone-live-reverification.md]
links: ["[[myownclone]]", "[[2026-1022-onboarding-manual-sin-self-service]]", "[[2026-1022-onboarding-cuatro-pasos-encuestas]]", "[[2026-1022-sin-pagina-precios-ni-docs]]", "[[2026-1022-stripe-planes-trial-30-dias]]"]
---

## Claim
El alta de [[myownclone]] es **self-service y visible** en la versión viva del 2026-10-22: `/registro` ya no hace meta-refresh a `/contacto` sino que sirve un formulario real ("Crea tu cuenta y empieza a escalarte", Full name, Email address, Create account, Continue with Google, "Already have an account? Sign in"), con el bundle de i18n incluyendo magic link, verificación por código, recuperación de contraseña (enlace válido 30 minutos) y requisitos de contraseña (mín. 12 caracteres, mayúscula, minúscula, número y símbolo). El paso de onboarding incluye los campos `name`, `personality` (tono: formal/informal/friendly/technical), `language` (Spanish/English) y `confirm`. La landing **tiene sección de precios** — "Pick your plan.", planes `basic`, `pro`, `scale`, `enterprise`, "Free", `trialDaysLeft`, `trialEnded`, `currentPlan`, `upgrade`, `manageBilling` — aunque sin importes `€` en el HTML de servidor. `/contacto` sigue existiendo. El webhook `/api/webhooks/stripe` devuelve **404**, ya no `405`.

## Why It Matters
Resuelve el nudo más caro del corpus: durante cuatro meses el vault osciló entre "el alta es manual caso por caso" y "hay un funnel de 4 pasos". La respuesta verificada es que **ambos existen y el funnel está desplegado y abierto**. El único dato que no se puede resolver sin sesión es si de verdad se cobra (no hay importes en el HTML de servidor y el webhook no responde 405), pero la infraestructura de planes, trial y checkout está en el bundle.

## [FRICTION]
> [[2026-1022-onboarding-manual-sin-self-service]] afirma que "el alta en [[myownclone]] no es self-service" y que `/registro` hace meta-refresh a `/contacto`; [[2026-1022-sin-pagina-precios-ni-docs]] afirma que `/pricing` devuelve 404 y que no se publica precios ni documentación; [[2026-1022-stripe-webhook-confirmado]] afirma que `/api/webhooks/stripe` devuelve `405 Method Not Allowed`, lo que "confirma en el sitio público que Stripe está integrado para pagos".
> Este átomo presiona las tres creencias porque hoy `/registro` sirve formulario, la landing tiene precios, y el webhook devuelve 404 en lugar de 405.
> La explicación más consistente para las tres a la vez es un **redespliegue completo del producto** entre mayo y octubre de 2026 — coherente con [[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]. La consecuencia práctica: el corpus atomizado describe una versión anterior y no debe usarse para decidir sobre GTM ni sobre Stripe.
> Marcado para juicio humano, no auto-resuelto.

## Extensión (re-verificación 2026-10-22, detalle de la landing)
La sección de precios vive **en la landing `/`**, no en una ruta `/pricing`: los encabezados observados son `h2: "Everything your clone can handle."`, `h2: "Real-time dashboard"`, `h2: "Structured knowledge"`, `h2: "AI-powered inbox"`, `h2: "Four steps to your clone."` y `h2: "Pick your plan."`, con `h3: "Free"` y `h3: "Enterprise"` como tarjetas visibles. Matiz importante: **`/pricing` como ruta devuelve la página de chat del clon** (catch-all de slug único, ver [[2026-1022-live-verify-robots-sitemap-y-404-como-catchall]]), no la sección de precios — es decir, los precios son públicos pero **no tienen URL propia**. Tampoco aparece ningún importe con `€` en el HTML de servidor: los precios se renderizan en cliente o no se publican.
