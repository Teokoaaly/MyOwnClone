---
id: 2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-precios-base-hobby-pro-business]]", "[[2026-1101-clerk-mru-no-mau-con-primer-dia-gratis]]", "[[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]"]
---

## Claim
El plan gratuito Hobby de Clerk da **50.000 MRU por app**, **hasta 3 asientos de dashboard**, **aplicaciones ilimitadas**, **hasta 5 impersonaciones de usuario**, dominio propio, **duración de sesión fija de 7 días** y Application Logs con **retención de 1 día**; además limita las **conexiones sociales a 3** en Hobby.

## Why It Matters
Define la ventana de gratuidad real de la opción "Clerk como auth de MyOwnClone": **$0 de coste de identidad mientras el producto no supere 50.000 usuarios retenidos por app**, lo que es muy holgado para un SaaS multi-tenant en fase beta. Pero los límites no son solo de cuota: **3 asientos de dashboard** significan que solo el founder y dos colaboradores pueden operar el panel de tenants, y la **retención de logs de 1 día** deja sin trazabilidad de accesos —relevante cuando el vault ya tiene "[[2026-1022-auth-otp-impersonacion-30min]]" y superficie de impersonación documentada. Frente al Free de Auth0 (25.000 MAU, 1 solo tenant en B2C, 3 admins, [[2026-1101-auth0-plan-free-25000-mau-sin-tarjeta]]), Clerk da **el doble de cuota de usuarios y apps ilimitadas**, pero pierde SSO/SCIM y añade gating de features (ver [[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]).

## Nota de verificación
Bullets verbatim de la tarjeta "Hobby" y filas de la tabla "Full price breakdown" de la captura del 2026-11-01. El wikilink a [[2026-1022-auth-otp-impersonacion-30min]] se inserta por contexto de vault (impersonación), no como afirmación de la fuente.
