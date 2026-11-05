---
id: 2026-1101-auth0-plan-free-25000-mau-sin-tarjeta
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1031-clerk-pricing]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]", "[[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]", "[[2026-1103-auth0-custom-domain-free-exige-verificacion-de-tarjeta]]", "[[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]]"]
---

## Claim
El plan Free de Auth0 cuesta **$0/mes, sin tarjeta de crédito**, y da soporte hasta **25.000 usuarios activos mensuales**, con 1 dominio personalizado, 5 Organizations, 1 Enterprise Connection, **Self-Service SSO**, **SCIM**, Passwordless Authentication, Unlimited Social Connections, Basic Attack Protection, brand customization y solo Community Support (1 tenant, 3 admin/contributors, retención de logs de 1 día).

## Why It Matters
Es el dato que hace de Auth0 la opción de identidad que cabe — holgadamente — en el presupuesto de ≤ €4/mes del vault: **$0 de coste variable de identidad** mientras el producto no supere 25.000 MAU, contra el suelo de €5,99/mes que ya está documentado en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]] solo para el VPS. MyOwnClone (SaaS multi-tenant con NextAuth 5) tendría entonces el auth como **línea de coste a cero**, como ya hace hoy con la librería propia. La diferencia con Clerk es de estilo de contrato, no de precio: Clerk incluye todas las features en todos los tiers ([[2026-1031-clerk-pricing]]), mientras que Auth0 da un Free generoso pero **degrada hacia abajo al subir de plan** (ver [[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]), lo que obliga a decidir muy pronto entre quedarse en Free (con 1 tenant y 1 día de logs) o pagar.

## Nota de verificación
El contenido del plan Free es lectura literal de la captura del 2026-11-01 (y de la del 2026-10-31, que lista los mismos bullets sin los marcados como NEW). "Sin coste de identidad" es la lectura operativa de este átomo, no una frase de la fuente.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

La tarjeta del plan Free en esta captura vuelve a listar, en el mismo orden, **5 Organizations**, **1 Enterprise Connection**, **Self-Service SSO** (marcado "New"), **SCIM** (marcado "New"), Passwordless Authentication, Unlimited Social Connections, Basic Attack Protection, Brand Customization y Community Support, a **$0/mes y "Up to 25,000 monthly active users"**. Confirma por tanto la lectura de este átomo en todos sus puntos verificables.

Dos matices nuevos que este átomo no recogía:
- La tarjeta del Free incluye **"Secure Agentic AI workflows"** como feature del plan gratuito (ver [[2026-1103-auth0-workflows-agentes-ai-incluidos-en-plan-free]]).
- Los bullets vienen con **notas al pie** que matizan la gratuidad: "1 Custom Domain*" con "* credit card verification required for custom domains" y "Unlimited Social Connections**" con "** subject to system limitations" (ver [[2026-1103-auth0-custom-domain-free-exige-verificacion-de-tarjeta]]).
- La tarjeta muestra además **"5 Organizations"** de forma explícita, lo que abre tensión con la lectura "1 tenant" del feature matrix; el conflicto está documentado en [[2026-1103-auth0-organizaciones-5-en-free-y-10-en-essentials]] contra [[2026-1101-auth0-numero-de-tenants-por-plan]].
