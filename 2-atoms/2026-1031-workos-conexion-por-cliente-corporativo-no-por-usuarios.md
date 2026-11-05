---
id: 2026-1031-workos-conexion-por-cliente-corporativo-no-por-usuarios
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1103-workos-vs-100-para-construir-sso-o-scim-uno-mismo]]"]
---

## Claim
En WorkOS **una conexión es la relación entre WorkOS y un grupo de usuarios finales**, y **cada cliente enterprise soportado con SSO o Directory Sync cuenta como una conexión**. El número de usuarios finales **no afecta al precio**: "each connection at WorkOS is billed the same, regardless of the identity provider (IdP), directory service used, or the total number of end users".

## Why It Matters
Esta es la definición que decide el eje abierto del vault — **coste por asiento vs coste por infraestructura**. WorkOS no factura por asiento: un cliente enterprise con 50 empleados paga **exactamente lo mismo** que uno con 5, y el coste escala con el **número de clientes corporativos**, no con los usuarios. Para MyOwnClone, que es un SaaS multi-tenant donde cada tenant es una organización con su propio IdP ([[2026-1022-costes-por-categoria-tenant]]), eso significa que la variable a cotizar es el **número de tenants que exigen SSO**, y no el MAU agregado (que en WorkOS es gratis hasta el millón, [[2026-1031-workos-authkit-primer-millon-de-mau-gratis]]). Matiz importante frente a la lectura por asiento: Auth0 también factura el SSO por conexión ($100, [[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]), pero Auth0 cobra además los usuarios por MAU — WorkOS rompe esa doble vara. Para un producto cuyo coste variable real es la IA por tenant, el coste de identidad es **fijo por cliente enterprise**, no marginal por usuario, y por tanto no escala con el uso: es la partida que decide si el modelo B2B tiene margen.

## 2026-11-03 — re-verificación
El FAQ del volcado crudo del 11-03 **confirma literalmente ambas definiciones**: "A connection represents the relationship between WorkOS and any group of end users. Each enterprise customer you support with SSO or Directory Sync is counted as one connection." y "No, each connection at WorkOS is billed the same, regardless of the identity provider (IdP), directory service used, or the total number of end users." Novedad de matiz: en esta versión la FAQ **atribuye la conexión a "each enterprise customer you support with SSO or Directory Sync"**, es decir, la unidad de cobro queda nombrada explícitamente como el **cliente enterprise**, no como un grupo abstracto de usuarios finales — lo que refuerza la lectura operativa de este átomo: la variable a cotizar en MyOwnClone es el número de tenants que exigen SSO, no el MAU.

## Nota de verificación
FAQ "What's a connection?" y "Does the number of end users affect pricing?" de la captura del 2026-10-31, verbatim.
