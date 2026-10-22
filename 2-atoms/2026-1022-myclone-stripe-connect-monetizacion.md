---
id: 2026-1022-myclone-stripe-connect-monetizacion
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-verticalizacion-y-transparencia]]", "[[2026-1022-myclone-widget-embed-modos]]", "[[myownclone]]", "[[2026-1022-gap-monetizacion-creador-stripe-connect]]"]
---
## Claim
MyClone.is monetiza con **Stripe en dos niveles**: suscripción a la plataforma (`POST /stripe/checkout/platform-subscription`) y **monetización por persona** vía Stripe Connect (`POST /stripe/checkout/persona-access` para comprar acceso a un clon concreto, `POST /stripe/personas/{persona_id}/connect/onboard` para que el creator entre en Connect, `GET/PUT/DELETE /stripe/personas/{persona_id}/monetization` y `PATCH .../monetization/status` para cambiar el estado). Hay además dashboard de Connect (`.../connect/dashboard`) y consulta de acceso (`GET /stripe/personas/{persona_id}/access`).

## Why It Matters
Es el endpoint que convierte un clon en un producto de pago: el mismo widget embebido ([[2026-1022-myclone-widget-embed-modos]]) puede estar abierto, ser de pago único o exigir suscripción por persona. Nadie de la lista de competidores registrada en el vault ([[myownclone-competitors]]) ofrece esto con granularity por clon — es el gap de monetización más grande que MyClone.is tiene cerrado.
Para [[myownclone]], esto activa un pathway de "low-ticket → high-ticket" mucho más directo: cobrar por acceso a un clon concreto en lugar de solo por la suscripción global de la plataforma (ver [[2026-1022-myclone-verticalizacion-y-transparencia]]).

## Extensión (Plan de implementación 2026-06-24)
El plan añade los **modelos de pricing** del competidor: `one_time`, `subscription` y `one_time_duration` (pago único con ventana de acceso). Y confirma el hueco de nuestro lado: [[myownclone]] solo tiene planes de plataforma — el usuario paga, el creator no gana. La propuesta es registrar la app en Stripe Connect, añadir `stripe_account_id` a `CloneConfig` y exponer `POST /stripe/connect/onboard` y `POST /stripe/checkout/persona-access`. Ver [[2026-1022-gap-monetizacion-creador-stripe-connect]].
