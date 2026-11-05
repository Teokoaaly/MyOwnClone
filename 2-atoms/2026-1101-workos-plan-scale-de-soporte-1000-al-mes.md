---
id: 2026-1101-workos-plan-scale-de-soporte-1000-al-mes
type: atom
certainty: solid
sources: [sources/2026-11-01-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]]", "[[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]"]
---

## Claim
WorkOS tiene tres niveles de soporte con precio propio: **Standard (gratis)** con email, web support, notificaciones de estado de API, **Slack privado** y docs; **Scale a $1.000/mes** con videollamadas, onboarding técnico, revisión de arquitectura trimestral, soporte de configuración para end-users, **P1 en 1 hora hábil y P2 en 3 horas hábiles**; y **Enterprise (custom)** con account manager dedicado, revisión de arquitectura trimestral, soporte de configuración end-user y **SLAs 24×7×365**. El horario hábil es **lunes a viernes, 6:00–17:00 Pacific Time**.

## Why It Matters
Es la partida más cara del catálogo de WorkOS para un SaaS pequeño: **$1.000/mes de soporte** son 250 veces el presupuesto de ≤ €4/mes del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y 4 veces lo que cuesta todo el hosting barato del producto. Pero el dato relevante para el eje abierto es otro: **AuthKit, SSO y Directory Sync tienen precio de lista y soporte Standard gratis**, así que el soporte de $1.000 es una compra explícita, no un impuesto oculto — a diferencia de los planes que lo empaquetan todo. Para MyOwnClone la lectura es: **$0 de soporte** es viable mientras el único canal sea el email, y el plan Scale solo tiene sentido si hay SLA de uptime comprometido y un cliente enterprise que lo exija (que es justamente lo que ofrece Annual Credits con su 99,99% de uptime y su SLA de soporte garantizado, [[2026-1031-workos-annual-credits-frente-a-pay-as-you-go]]). Nótese que incluso con $0 en WorkOS, la partida de identidad del producto es $0 solo mientras no haya ninguna conexión SSO de pago ([[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]).

## 2026-11-03 — re-verificación
La captura del 2026-11-03 **no contiene ninguna tabla de soporte** (es un volcado crudo de la página sin la sección "Support Plans"), por lo que **no confirma ni desmiente** el contenido del plan Scale que este átomo documenta: ni la "revisión de arquitectura trimestral" ni el "soporte de configuración para end-users" aparecen en ella. El precio de $1.000/mes y la existencia de los tres niveles (Standard gratis, Scale, Enterprise custom) **no quedan refutados**, pero la composición del plan Scale queda como **dato pendiente de verificación** (ver [[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]). La lectura operativa de este átomo no cambia: $1.000/mes de soporte sigue siendo 250 veces el presupuesto de ≤ €4/mes del vault, así que el plan solo tiene sentido cuando hay un cliente enterprise que exija SLA.

## Nota de verificación
Tabla "Support Plans" de la captura del 2026-11-01, con la columna de precios (Standard free / Scale $1.000 mo / Enterprise custom) y las filas de P1, P2 y 24×7×365, más la nota al pie sobre el horario hábil en Pacific Time. La comparación con el presupuesto del vault es lectura operativa de este átomo.
