---
id: 2026-1029-sendgrid-sin-precios-publicados
type: atom
certainty: solid
sources: [sources/2026-10-29-sendgrid-pricing.md]
links: ["[[2026-10-29-sendgrid-twilio-merger]]", "[[2026-10-29-twilio-sendgrid-email-api-pricing]]", "[[2026-1029-resend-pricing]]"]
---

## Claim
La página sendgrid.com/en-us/pricing ya no publica ninguna cifra: solo ofrece "Free trial", "No credit card required" y "Flexible pricing", y remite el precio a dos páginas distintas de Twilio — twilio.com/en-us/products/email-api/pricing para el Email API/SMTP y twilio.com/en-us/products/marketing-campaigns/pricing para las campañas de email.

## Why It Matters
Es un hueco de precio, no una ausencia de precio: SendGrid sigue vendiendo, pero el precio solo existe en las páginas de Twilio, con dos tablas separadas (transaccional vs campañas). Para el vault esto tiene dos consecuencias. Primera, cualquier comparación de TCO entre SendGrid y Resend tiene que capturar dos URLs en lugar de una, así que el coste demonitorización de precios de SendGrid es mayor que el de Resend, que publica una sola página completa. Segunda, y más relevante para el eje "coste por asiento frente a coste de infraestructura": SendGrid ha convertido su pricing page en un embudo de cualificación hacia Twilio, lo que refuerza la hipótesis de que en la banda enterprise el precio deja de ser un dato público y verificable — el mismo patrón que [[2026-1029-resend-plan-enterprise]] documenta en Resend y que el vault ya vio en Render Enterprise.

## [FRICTION]
> [[2026-10-29-sendgrid-twilio-merger]] afirma que tras la fusión "los productos (Free trial, Essentials, Pro, Premier)" siguen accesibles en Twilio. Esta captura de sendgrid.com/en-us/pricing no menciona en ningún momento Essentials, Pro ni Premier: solo nombra "Free trial", "No credit card required" y "Flexible pricing", y delega los precios en twilio.com. Ambas no pueden ser completamente correctas: o esos nombres de plan vienen de otra captura (la de twilio.com/en-us/products/email-api/pricing), o se han añadido tras la fusión. Marcado para juicio humano, no auto-resuelto.
