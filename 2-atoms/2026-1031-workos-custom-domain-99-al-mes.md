---
id: 2026-1031-workos-custom-domain-99-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1029-resend-pro-plan]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1103-workos-inventario-de-funciones-de-authkit]]"]
---

## Claim
El **dominio personalizado** de WorkOS cuesta **$99/mes** y cubre a la vez AuthKit, el Admin Portal y la dirección remitente de email ("Custom domain for AuthKit, Admin Portal, and email sender address / $99 / mo"). El Admin Portal, en cambio, **sí está incluido sin coste** en todas las cuentas de WorkOS; solo el branding personalizado y el dominio propio son de pago.

## Why It Matters
Es una línea pequeña pero recurrente que aparece en la cuenta de un producto con marca blanca: $99/mes es **25 veces el presupuesto de ≤ €4/mes** del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), así que la decisión de usar dominio propio en el proveedor de identidad es una decisión de presupuesto, no de branding. Y hay un solapamiento que conviene registrar: el email de MyOwnClone sale por Resend ([[2026-1029-resend-pro-plan]]), de modo que el "email sender address" que WorkOS factura con el dominio propio es **otro remitente** y no el de las notificaciones del producto — dos identidades de dominio que mantener separadas. Para un SaaS en beta, la lectura correcta es: WorkOS sin dominio propio ($0) con Admin Portal incluido, y el dominio se paga solo cuando hay un cliente enterprise que lo exija como requisito de confianza.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma el precio y el alcance: "Custom domain for AuthKit, Admin Portal, and email sender address — $99 / mo", y el FAQ mantiene que "Admin Portal is fully functional without customization and is included in all WorkOS accounts. Custom branding and custom domains can be applied for an additional monthly fee." Matiz nuevo: en el volcado crudo el bloque "Custom Domain" aparece **dentro del calculador de costes**, junto a las líneas de Log streaming y Event Retention, es decir, la página trata el dominio propio como una **partida recurrente más** del producto y no como un extra de "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]". La lectura operativa de este átomo no cambia: $99/mes sigue siendo 25 veces el presupuesto de ≤ €4/mes del vault, así que el dominio propio es una decisión de presupuesto que solo se activa cuando un cliente enterprise lo exige.

## Nota de verificación
Sección "Custom Domain" de la captura del 2026-10-31 y FAQ "Can I use Admin Portal without customizing it?" ("Admin Portal is fully functional without customization and is included in all WorkOS accounts").
