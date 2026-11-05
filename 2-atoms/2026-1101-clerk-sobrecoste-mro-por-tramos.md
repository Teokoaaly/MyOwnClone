---
id: 2026-1101-clerk-sobrecoste-mro-por-tramos
type: atom
certainty: solid
sources: [sources/2026-11-01-clerk-pricing.md]
links: ["[[2026-1101-clerk-organizaciones-100-mro-y-20-miembros-gratis]]", "[[2026-1101-clerk-addon-b2b-85-o-100-por-mes]]", "[[2026-1101-auth0-numero-de-tenants-por-plan]]"]
---

## Claim
El sobrecoste por **MRO (organizaciones retenidas)** de Clerk también es volumétrico y decreciente, en cuatro tramos sobre los 100 MRO incluidos por app: **101–1.000 a $1/mes cada uno**, **1.001–10.000 a $0,90/mes**, **10.001–100.000 a $0,75/mes**, **100.001+ a $0,60/mes**.

## Why It Matters
Es el vector de coste **por tenant**, no por usuario, y por tanto el que se alinea con el eje abierto del vault: para MyOwnClone, la unidad de negocio es el tenant/clon, así que el coste relevante es **$1/mes por organización retenida a partir de la centésima**. Traducido: **1.000 tenants activos = 900 MRO × $1 = $900/mes**, una cifra que domina cualquier comparación con la infraestructura. Esto hace que la pregunta "asiento o infra" se resuelva aquí de forma bastante nítida: **la infra (Hetzner/HostBrr/BuyVM, ver [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) es una línea plana de ≤ €6/mes; el asiento de identidad es una línea creciente en el número de tenants**, así que en cualquier escenario con más de unos pocos cientos de tenants activos, el coste por asiento domina el TCO con holgura. La comparación con el "1 tenant" del Free de Auth0 ([[2026-1101-auth0-numero-de-tenants-por-plan]]) muestra el patrón inverso: Auth0 cobra por tenant de forma restrictiva en los planes bajos, Clerk da 100 organizaciones gratis.

## Nota de verificación
Tramos verbatim de la fila "Monthly retained organizations (MROs)" de la tabla "B2B Authentication feature details" de la captura del 2026-11-01. La aritmética de 1.000 tenants y la conclusión sobre el eje del vault son lectura operativa de este átomo.
