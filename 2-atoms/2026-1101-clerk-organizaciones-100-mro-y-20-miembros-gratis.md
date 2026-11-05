---
id: 2026-1101-clerk-organizaciones-100-mro-y-20-miembros-gratis
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-addon-b2b-85-o-100-por-mes]]", "[[2026-1022-multi-tenant-slug-unpublished]]", "[[2026-1101-auth0-numero-de-tenants-por-plan]]"]
---

## Claim
El add-on **B2B Authentication** de Clerk es **gratuito en todos los planes** e incluye **100 MRO por app** y **hasta 20 miembros por Organization**, con roles Admin y Member, permisos custom e invitaciones; el límite se define así: una organización es retenida si tiene **al menos 2 miembros y al menos uno de ellos es MRU del mes**. Superar 100 MRO obliga a contratar el add-on de pago.

## Why It Matters
Es el dato más directamente relevante del corpus para MyOwnClone, porque **la organización es la unidad de tenant** del modelo ([[2026-1022-multi-tenant-slug-unpublished]]): el producto es multi-tenant con slug por clon, y Clerk organiza ese concepto como "Organization" con membresía y roles. La lectura operativa: **con 100 MRO gratis, un producto con 100 tenants activos de 2+ usuarios cada uno paga $0 en identidad**, y el límite de **20 miembros por organización** cubre de sobra al caso de uso "un creador + sus colaboradores" que el vault describe en [[2026-1022-myclone-tier-plans-usage-api]]. El punto de fricción está en la definición de MRO (≥2 miembros, uno de ellos retenido): un tenant de un solo usuario **no computa**, lo que en un producto de clones individuales puede dejar fuera precisamente a los usuarios de pago de baja frecuencia.

## Nota de verificación
Sección "B2B Authentication" y tabla "B2B Authentication feature details" (filas "Organization membership limit" y "Monthly retained organizations") de la captura del 2026-11-01, verbatim.
