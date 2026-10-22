---
id: 2026-1022-ausencia-csp-xss-sin-mitigacion
type: atom
certainty: solid
sources: [raw/articles/myownclone-vulnerabilities-confirmed.md]
links: ["[[myownclone]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---
## Claim
[[myownclone]] sirve **cero** `Content-Security-Policy` en sus respuestas: no existe CSP en ninguna página. La consecuencia reportada es XSS sin mitigación y dependencias de terceros sin restricción de origen.

## Why It Matters
Una app que renderiza en servidor y muta por Server Actions, como describe [[2026-1022-mutaciones-rsc-sin-api-rest]] y [[2026-1022-ia-y-auth-totalmente-servidor]], no tiene ninguna barrera de contenido que impida la ejecución de un payload inyectado en el DOM: sin `script-src`, cualquier origen puede servir scripts y las integraciones de terceros (Sentry, PostHog, Intercom, Crisp, Stripe) cargan sin `default-src` que las acote. Combinado con la fuga del payload admin de [[2026-1022-admin-p2-fuga-codigo-panel-sin-auth]] y con la ausencia de headers defensivos, el hardening de la capa HTTP del producto está directamente ausente en el stack identificado en [[2026-1022-frontend-nextjs-vercel-sentry-posthog]].

## [FRICTION]
> La nota de entidad [[myownclone]] describe el producto con "aislamiento completo entre tenants" y un stack serverless gestionado.
> Esta nota presiona eso porque el aislamiento se observa a nivel de datos pero no a nivel de superficie HTTP: sin CSP ni headers defensivos, la frontera entre el navegador de un visitante y cualquier third-party cargada en la página es difusa.
> Ambas no pueden ser completamente correctas: o "aislamiento completo" se refiere exclusivamente al aislamiento de datos entre tenants, o la ausencia de CSP es un descuido de hardening y no una decisión. Marcado para juicio humano, no auto-resuelto.
