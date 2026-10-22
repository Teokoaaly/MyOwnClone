---
id: 2026-1022-gap-monetizacion-creador-stripe-connect
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-stripe-connect-monetizacion]]", "[[2026-1022-low-ticket-a-high-ticket-con-clon]]", "[[2026-1022-impacto-del-clon-en-ventas]]"]
---
## Claim
[[myownclone]] **no tiene monetización para el creator**: solo planes de plataforma (el usuario paga, el creator no gana). MyClone.is, en cambio, cobra por persona con `POST /stripe/personas/{id}/monetization`, onboarding vía `POST /stripe/personas/{id}/connect/onboard` y pricing models `one_time`, `subscription` y `one_time_duration`.

## Why It Matters
Es la brecha más directamente ligada al modelo de negocio raíz del vault: [[2026-1022-low-ticket-a-high-ticket-con-clon]] define el clon como mecanismo para subir de ticket, y [[2026-1022-impacto-del-clon-en-ventas]] demuestra que un clon concreto ya generó ingresos reales — pero como efecto del negocio del creador, no como pago por el clon. Sin Stripe Connect, la plataforma se queda con el 100% del MRR del creador y solo cobra al suscriptor final.
El plan lo coloca en **Fase 3 (semanas 5-6)**: registrar la app en Stripe Connect, añadir `stripe_account_id` a `CloneConfig`, y exponer `POST /stripe/connect/onboard` y `POST /stripe/checkout/persona-access`. Impacto medio, effort alto — coherente con que requiere abrir onboarding de pagos, no solo código.
