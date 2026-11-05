---
id: 2026-1029-resend-tracking-por-dominio
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-free-plan]]", "[[2026-1029-resend-transactional-marketing]]", "[[2026-1029-resend-pricing]]"]
---

## Claim
El open tracking y el click tracking de Resend son un ajuste por dominio disponible en todos los planes, incluido el Free, y no consumen cuota transaccional; el panel "Marketing analytics" de la página de precios es un dashboard de analítica de broadcasts separado del tracking.

## Why It Matters
Dos consecuencias para el diseño de la plataforma. Primera: el tracking no es un premium que exija pagar, así que no añade coste al TCO de MyOwnClone y se puede activar por dominio sin justificar un plan superior — cada tenant con su propio dominio de envío puede tener su propia configuración de tracking. Segunda, y más fina: los broadcasts no cuentan contra la cuota transaccional ([[2026-1029-resend-transactional-marketing]]), pero los emails enviados vía /emails API —los de onboarding, reset de contraseña o confirmación— sí cuentan, y cada destinatario de un envío por /emails API cuenta como un email. Publicar newsletters por la API equivocada consume la cuota transaccional del plan Free (3.000/mes, 100/día) sin necesidad, y de paso incurre en el riesgo regulatorio de no incluir el unsubscribe gestionado por Broadcasts.

## [FRICTION]
> No conflicting atom found. This is a feature-availability atom with no direct contradiction in the current vault. No [FRICTION] block added.
