---
id: 2026-1022-admin-bandeja-global-y-spam
type: atom
certainty: solid
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-email-inbound-contacto-sin-dominio-propio]]", "[[2026-1022-inbox-triage-propuestas-ia]]", "[[myownclone]]"]
---
## Claim
El back-office de plataforma de [[myownclone]] incluye un módulo `AdminPlatformInbox`: una bandeja global que captura todo el correo entrante en el dominio `*@myownclone.com` con etiquetas y estados, y un módulo `AdminPlatformSpam` con lista negra de dominios de spam. El resto de módulos de plataforma confirmados en los bundles son `AdminPlatformResumen` (dashboard con MRR, costes Anthropic+OpenAI+email, gráficos y métricas), `AdminPlatformTenants` (CRUD, invitaciones, cortesías, trials Stripe, impersonación de 30 min), `AdminPlatformFeedback`, `AdminPlatformFaqs` y el `AdminImpersonationBanner`.

## Why It Matters
La existencia de un inbox global con etiquetas y estados, más una lista negra manual de dominios, es la infraestructura de moderación centralizada del producto: el correo de todos los tenants aterriza en una bandeja que el operador etiqueta a mano, no en un sistema de clasificación automática por tenant. Es la pieza que convierte el triage por IA en un flujo supervisado (ver [[2026-1022-inbox-triage-propuestas-ia]]) y explica por qué el panel de plataforma necesita MRR y costes a nivel agregado (ver [[2026-1022-platform-admin-tenants-costes-mrr]]).

## [FRICTION]
> [[2026-1022-email-inbound-contacto-sin-dominio-propio]] (escrita hace ~21 semanas) afirma que el **único** destinatario de email entrante en [[myownclone]] es `contacto@myownclone.com`.
> Este átomo presiona esa creencia porque el módulo `AdminPlatformInbox` opera sobre un patrón `*@myownclone.com` —un dominio comodín con múltiples casillas, no una sola dirección genérica— y añade etiquetado y estados, lo que implica más casillas de entrada de las que la nota contempla.
> Ambas no pueden ser completamente correctas: o el comodín cubre en la práctica solo `contacto@`, o la nota de dominio único infrarrepresenta la superficie real de entrada. Marcado para juicio humano, no auto-resuelto.
