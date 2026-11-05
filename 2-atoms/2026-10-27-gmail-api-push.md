---
id: 2026-10-27-gmail-api-push
type: atom
certainty: solid
sources: [sources/2026-10-27-gmail-api-overview.md]
links: ["[[2026-10-27-gmail-api-certificates]]", "[[2026-10-27-gmail-api-delegation]]"]
---

## Claim
Push notifications are a server-side notification system integrating with Google Cloud Pub/Sub; applications can "watch" a mailbox, and the Gmail API sends automatic webhooks or alerts whenever a change occurs (such as a new email arriving), eliminating the need for the app to poll the server for updates.

## Why It Matters
Push notifications reduce latency and server load by delivering real-time event data, making them ideal for applications that need immediate response to new mail rather than periodic polling.

## [FRICTION]
> [[2026-10-27-gmail-api-delegation]] (escrita hoy) afirma que las notifications push solo funcionan para el dueño de la cuenta. Esta nota presiona eso porque las cuentas delegadas también pueden suscribirse a watch y recibir notifications, dependiendo de los permisos OAuth. Ambas pueden ser completamente correctas. Marcado para juicio humano, no auto-resuelto.