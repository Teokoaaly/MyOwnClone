---
id: 2026-1101-clerk-gating-por-plan-contradice-atom-1031
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md, sources/2026-10-31-clerk-pricing.md]
links: ["[[2026-1031-clerk-pricing]]", "[[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]", "[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]"]
---

## Claim
La tabla completa de features de Clerk **sí tiene gating por plan**, y es sustancial: en Hobby están "Not included" **Remove Clerk branding, passkeys, biometría, requisitos de contraseña custom, plantillas de email custom, MFA, conexiones SSO, conexiones Directory Sync, restricciones de IP de la Secret Key, user bans, blocklist, sesiones simultáneas, dominios satélite, Admin Logs y SOC2**; el **SMS** tampoco está incluido en Hobby, y las **conexiones sociales están limitadas a 3** en Hobby frente a ilimitadas en Pro y Business.

## Why It Matters
Este átomo corrige la creencia central que el vault tenía registrada sobre Clerk, y por eso es el más importante del lote. El modelo real **no es "todo incluido sin gating"**: Clerk tiene exactamente el patrón que el átomo original atribuía a los demás proveedores — funciones avanzadas (MFA, passkeys, bans, blocklist, admin logs, SOC2) reservadas a planes de pago — con la diferencia de que la **frontera Hobby/Pro es de precio bajo ($20/mes)** y la de **Business ($250/mes)** es donde aparece lo empresarial (SOC2, Admin Logs, IP restrictions, protecciones avanzadas). Eso reordena la comparación del vault: **Clerk se parece a Auth0 en la forma (gating) y no en la cifra**, con la ventaja de que el primer escalón de pago ($20) es mucho más barato que el de Auth0 ($35 Essentials, $150/$240 B2B). Para MyOwnClone la consecuencia práctica es que **Hobby sirve para el producto actual y Pro es barato de digerir**, pero que SSO/Enterprise SSO, SCIM, MFA, bans y logs de admin —justo lo que necesita un producto multi-tenant que venda a empresas— están todos fuera del tramo gratuito.

## [FRICTION]
> [[2026-1031-clerk-pricing]] afirma que "Clerk includes all authentication and user management features across every pricing tier without feature gating, unlike typical auth providers that lock advanced features (SMS, social connections, usernames) behind higher plans".
> Este átomo presiona esa creencia porque **la propia fuente del átomo viejo lo contradice**: la tabla "Full price breakdown" de la captura del 2026-10-31 (sources/2026-10-31-clerk-pricing.md) ya marcaba "Remove Clerk branding | **Not included**", "Social connections | **Up to 3** | Unlimited | Unlimited" y "SMS codes | **Not included**" en la columna Hobby, y la captura del 2026-11-01 amplía la lista de features ausentes en Hobby.
> Ambas no pueden ser completamente correctas: o el átomo del 2026-10-31 leyó solo las viñetas de las tarjetas de plan (que dicen "+ most authentication features") y no la tabla, o leyó mal las celdas "Not included". Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Filas "Remove Clerk branding", "Social connections", "SMS codes", "Passkeys", "Biometric sign-in", "Multifactor authentication (MFA)", "SSO connections", "Directory Sync connections", "Secret Key IP restrictions", "User bans", "Blocklist", "Advanced protections", "Simultaneous sessions", "Satellite domains", "Admin Logs" y "SOC2 report" de la tabla "Full price breakdown" (captura del 2026-11-01), contrastadas con las mismas filas de la captura del 2026-10-31.
