---
id: 2026-1031-workos-directory-sync-misma-escalera-que-sso
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1101-clerk-directory-sync-facturacion-desde-enero-2027]]", "[[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]", "[[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]]"]
---

## Claim
**Directory Sync** de WorkOS (aprovisionamiento y desprovisionamiento de usuarios y mapeo de roles) se factura con **exactamente la misma escalera por conexión que el SSO**: 1–15 a $125/ea, 16–30 a $100/ea, 31–50 a $80/ea, 51–100 a $65/ea, 101+ a consultar. La página añade el argumento de venta "**vs $100 to build it yourself**".

## Why It Matters
Un cliente corporativo que necesita SSO **y** SCIM paga **dos conexiones** en WorkOS, con la misma tabla de precios para ambas: 5 clientes con SSO+Directory Sync son $1.250/mes en el primer tramo. Es el patrón de doble cobro que el vault ya tiene documentado en Clerk, donde Directory Sync se factura aparte y además **empieza el 1 de enero de 2027** ([[2026-1101-clerk-directory-sync-facturacion-desde-enero-2027]]), y que Auth0 resolvió con una degradação: SSO y SCIM presentes en el plan Free pero no en Essentials B2C ([[2026-1101-auth0-sso-scim-en-free-pero-no-en-essentials-b2c]]). WorkOS, en cambio, es explícito y sin fecha: la línea de SCIM es **$125/conexión desde el primer día**. Para MyOwnClone la lectura es directa: el SCIM solo tiene sentido si hay tenants corporativos con varios empleados, y hasta que ese caso exista, la partida de Directory Sync debe estar a $0 en el modelo de costes por tenant, no estimada como "gratis porque es una función más".

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma la escalera **idéntica** para Directory Sync ("0 15 30 50 100+" y la tabla 1-15 $125/ea, 16-30 20% off $100/ea, 31-50 36% off $80/ea, 51-100 48% off $65/ea, y "Need additional scale? Talk to us" por encima de 100), con el descriptor literal "User provisioning, de-provisioning, and role mapping" y el argumento "vs $100 to build it yourself" al pie del bloque. La conclusión de este átomo no cambia: **SCIM cuesta lo mismo que SSO, conexión por conexión**, y el doble cobro para un cliente que necesita ambos sigue siendo real ([[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]]).

## Nota de verificación
Sección Directory Sync de la captura del 2026-10-31: misma tabla "Number of connections" que la de SSO (1-15 $125/ea … 51-100 $65/ea) y el literal "vs $100 to build it yourself" junto al total del calculador.
