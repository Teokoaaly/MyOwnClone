---
id: 2026-1022-onboarding-cuatro-pasos-encuestas
type: atom
certainty: solid
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-onboarding-manual-sin-self-service]]", "[[2026-1022-auth-magic-link-codigo-seis-digitos]]", "[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1022-myclone-verticalizacion-y-transparencia]]"]
---
## Claim
El flujo de alta de [[myownclone]] diseñado en el código es de cuatro pasos encadenados: `/registro` → Stripe Checkout → `/registro/exito` (código mágico de 6 dígitos) → `/registro/onboarding`. El paso 1 pide email, nombre y **subdominio con validación en tiempo real** (`tunombre.myownclone.com`), aceptación de términos y privacidad, opción de Google OAuth, y muestra los planes Pro, Scale y Enterprise con precios dinámicos (`€{price}`) bajo un badge "Acceso Beta" con precio bloqueado de por vida; el paso 2 exige tarjeta con facturación mensual y sin permanencia; el paso 4 pide nombre del clon y subdominio, más dos encuestas: de dónde te conocieron (X, YouTube, Instagram, LinkedIn, Podcast, Newsletter, Recomendación, Google, Anuncio, Otro) y para qué lo usarás (atender alumnos, capturar leads, recomendar productos, soporte automático, Q&A, Otro).

## Why It Matters
Las dos encuestas del onboarding son la única ventana de datos de cliente que captura el propio producto: origen de descubrimiento y caso de uso hopedado, con la taxonomía de infoproductos del founder (atender alumnos, capturar leads, soporte automático) — es decir, el producto codifica sus propios modos del RAC en el formulario (ver [[2026-1022-myclone-verticalizacion-y-transparencia]]). El badge "Acceso Beta" con precio bloqueado de por vida y la ausencia de permanencia son palancas comerciales explícitas para cerrar la beta (ver [[2026-1022-stripe-planes-trial-30-dias]]).

## [FRICTION]
> [[2026-1022-onboarding-manual-sin-self-service]] (escrita hace ~21 semanas) afirma que el alta **no es self-service** y que el único camino es un formulario de contacto, con incorporación caso por caso.
> Este átomo presiona esa creencia porque describe un funnel de registro completo en cuatro pasos con Stripe Checkout y onboarding instrumentado, lo que implica que el código de alta existe y es funcional aunque hoy esté cerrado al público.
> Ambas no pueden ser completamente correctas: o el funnel es una camino muerto que solo se abre en ventanas de beta, o la incorporan real se hace por la misma ruta y la nota leyó mal la redirección a `/contacto`. Marcado para juicio humano, no auto-resuelto.
