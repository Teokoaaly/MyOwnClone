---
id: 2026-1022-mapa-modulos-internos-desde-bundles-js
type: atom
certainty: solid
sources: [raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[2026-1022-platform-admin-tenants-costes-mrr]]", "[[2026-1022-inbox-triage-propuestas-ia]]", "[[2026-1022-modulo-reuniones-booking-video]]", "[[2026-1022-feedback-widget-screenshots]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---
## Claim
El análisis de 15 bundles JS de [[myownclone]] (~1,2 MB) permite reconstruir el mapa completo de módulos internos del producto, en dos capas: **Admin Platform** (`AdminPlatformResumen`, `AdminPlatformTenants`, `AdminPlatformInbox`, `AdminPlatformSpam`, `AdminPlatformFeedback`, `AdminPlatformFaqs`, `AdminImpersonationBanner`) y **Tenant App**, lo que ve cada creador (`Onboarding`, `Brain`, `Triage`, `PublicBooking`, `MyBooking`, `PublicRecording`, `FeedbackWidget`, `PublicFooter`, `CookieBanner`).

## Why It Matters
Es la diferencia entre "no hay código" y "no hay API": el nombre de los módulos es la nomenclatura real del producto y nombra capacidades concretas que elsewhere se inferían. `Brain` aparece explícitamente como CRUD de memorias, firma de email, plantillas, dominios spam y dominio inbound (ver [[2026-1022-email-inbound-contacto-sin-dominio-propio]]); `Triage` como lectura del inbox con drafts en la voz del creador, voice-to-text y envío en un clic (ver [[2026-1022-inbox-triage-propuestas-ia]]); `PublicBooking`/`MyBooking`/`PublicRecording` como calendario público, vista de reserva con videollamada en myownclone y grabación con transcripción y chat contextual (ver [[2026-1022-modulo-reuniones-booking-video]]); `FeedbackWidget` con capturas pegadas con Ctrl+V (ver [[2026-1022-feedback-widget-screenshots]]). Al confirmar que la nomenclatura vive en el bundle cliente, queda explícito que la opacidad del núcleo es deliberada: los módulos se nombran, el servidor no (ver [[2026-1022-ia-y-auth-totalmente-servidor]]).

## [FRICTION]
> [[2026-1022-ia-y-auth-totalmente-servidor]] (escrita hace ~21 semanas) afirma que en ningún bundle JS de [[myownclone]] aparecen claves o endpoints de LLM, y que las únicas salidas a terceros son PostHog y Sentry.
> Este átomo presiona esa creencia porque la presencia de 15 bundles con nomenclatura interna completa implica que la opacidad total del núcleo no es total: el cliente sí nombra los módulos del producto (Brain, Triage, PublicRecording…), aunque no exponga el proveedor de IA que los ejecuta.
> Ambas no pueden ser completamente correctas: o la opacidad se refiere solo a los proveedores de IA y no a la estructura funcional, o el recon previo llegó a los bundles sin listar los módulos. Marcado para juicio humano, no auto-resuelto.
