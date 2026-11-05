---
id: 2026-1104-clerk-la-faq-dice-una-conexion-enterprise-pero-la-tabla-dos
type: atom
certainty: solid
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]", "[[2026-1101-clerk-directory-sync-facturacion-desde-enero-2027]]", "[[2026-1104-clerk-cuarta-captura-identica-byte-a-byte-a-la-del-11-01]]"]
---

## Claim
La FAQ de `clerk.com/pricing` describe el plan Pro de Clerk como si incluyera **una sola conexión enterprise** —"Clerk Pro is $20/mo billed annually and includes 50K MRUs plus **1 Enterprise connection**" y "Clerk includes **one Enterprise connection** on Pro with published pricing for additional connections"— mientras que la **tabla "Full price breakdown" de la misma página** otorga a Pro **dos conexiones incluidas de distinto tipo**: "SSO connections: **1 connection included per app**" y "Directory Sync connections: **1 connection included per app**". El término "Enterprise connection" no aparece en la tabla: el único uso de "Enterprise" en la página es "Enterprise SSO for workspace" en la tarjeta Business y "Enterprise" como nombre del plan custom.

## Why It Matters
Es una **contradicción interna de la misma página** que el vault no tenía registrada, y no es cosmética: la diferencia entre "1 conexión incluida" y "2 conexiones incluidas de tipo distinto" es exactamente la línea que decide cuánto cuesta vender a un cliente corporativo. Con la lectura de la tabla, un cliente que quiere **SAML + SCIM** consume **las dos** conexiones incluidas de Pro (una de cada tipo) sin coste adicional, mientras que con la lectura de la FAQ solo habría una conexión gratis y la segunda (SCIM) entraría en la escalera de $75/mes — que es justamente el precio que empieza a facturarse el 1 de enero de 2027 ([[2026-1101-clerk-directory-sync-facturacion-desde-enero-2027]]). La consecuencia operativa para MyOwnClone es que **el presupuesto de identidad para un tenant corporativo se puede montar con dos conexiones gratis hasta 01-01-2027 y con dos conexiones de pago ($75/mes cada una) a partir de esa fecha**, si la lectura de la tabla es la buena; si la lectura de la FAQ es la buena, el sobrecoste llega antes. No se puede resolver desde el texto: la página usa dos convenciones incompatibles para la misma entitlement.

## [FRICTION]
> [[2026-1101-clerk-sso-adicional-desde-75-por-conexion]] afirma, citando la tabla, que "Pro y Business incluyen **1 conexión por app**, y las adicionales se cobran por tramo de volumen" — una formulation que no distingue SSO de Directory Sync y, leída junto a la FAQ, sugiere que el plan incluye una sola conexión.
> Este átomo presiona esa lectura porque **la página concede una conexión incluida por cada tipo** (una SSO + una Directory Sync), de modo que el umbral de "la segunda conexión cuesta $75" **no se alcanza** en el caso más habitual (SAML + SCIM en el mismo tenant) hasta la tercera conexión de cualquier tipo. Ambas no pueden ser completamente correctas: o la entitlement es "1 conexión total de cualquier tipo" y la tabla duplica la fila por claridad de columnas, o la entitlement es "1 por tipo" y la FAQ simplifica de más. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Frases verbatim de la sección "Questions & answers about our pricing" ("Is Clerk cheaper than Auth0?") y filas "SSO connections" y "Directory Sync connections" de la tabla "Full price breakdown", ambas de `sources/2026-11-04-clerk-pricing.md` (idéntico a las del 11-01 y del 11-02). La implications de presupuesto es lectura operativa de este átomo.
