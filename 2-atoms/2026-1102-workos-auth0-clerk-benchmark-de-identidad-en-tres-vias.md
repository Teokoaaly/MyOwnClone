---
id: 2026-1102-workos-auth0-clerk-benchmark-de-identidad-en-tres-vias
type: atom
certainty: tentative
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-01-workos-pricing.md, sources/2026-11-02-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]", "[[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1031-workos-conexion-por-cliente-corporativo-no-por-usuarios]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]", "[[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]"]
---

## Claim
Las tres capturas de workos.com/pricing de 2026-10-31, 2026-11-01 y 2026-11-02 describen **la misma oferta y los mismos precios** (AuthKit hasta 1M de MAU gratis y $2.500/mes por millón adicional; SSO y Directory Sync a $125/$100/$80/$65 por conexión; Audit Logs $125 por SIEM y $99 por millón de eventos; Radar $100/50k checks; dominio $99/mes), con una **única diferencia entre capturas: la tabla de soporte** (ver [[2026-1102-workos-el-plan-scale-perdio-revision-trimestral-y-configuracion]]). Ninguna de las tres publica un precio por asiento ni por llamada a la API.

## Why It Matters
Con esto el benchmark de identidad del vault queda cerrado en tres vías distintas y comparables, que es lo que pedía el eje abierto "coste por asiento vs coste por infraestructura" ([[2026-1022-costes-por-categoria-tenant]]):
- **Auth0**: cobra **por MAU** (per-seat) *y* el SSO enterprise como add-on de **$100 por conexión** ([[2026-1101-auth0-addon-sso-enterprise-100-usd-por-conexion]]), con topes de conexiones y de tenants.
- **Clerk**: cobra plan base + **sobrecoste por MRU retenidos** y **$75 por conexión SSO** adicional ([[2026-1101-clerk-sso-adicional-desde-75-por-conexion]]).
- **WorkOS**: cobra **$0 por usuarios hasta el millón de MAU** y **$125→$65 por conexión** SSO, con la variable de coste en el **número de clientes enterprise**, no en los usuarios ([[2026-1031-workos-conexion-por-cliente-corporativo-no-por-usuarios]]).

La conclusión operativa para MyOwnClone: para el tramo de un SaaS multi-tenant en beta, **el proveedor más barato de identidad es WorkOS** ($0 sin conexiones) y **el más caro es Auth0** ($35–$150/mes de plan, más $100 por conexión SSO). Pero si el producto llega a vender a empresas, WorkOS sigue siendo el único que **no cobra por asiento**: su coste de identidad es fijo por cliente enterprise, lo que encaja con un producto cuyo coste variable real es la IA por tenant. El átomo se marca `tentative` porque es una síntesis comparativa de tres fuentes distintas y no una afirmación literal de una sola página.

## 2026-11-03 — re-verificación
La **cuarta captura** de workos.com/pricing (2026-11-03, 580 palabras) **no altera ninguno de los precios del benchmark** (SSO y Directory Sync $125/$100/$80/$65 con 20%/36%/48% off; Log streaming $125/mes por SIEM; Event Retention $99/mes por millón de eventos; Radar 1.000 checks gratis y $100/50k; Custom Domain $99/mes; 1M de MAU gratis), por lo que la conclusión comparative del átomo — WorkOS es el único de los tres que **no cobra por asiento** y su variable de coste es el número de clientes enterprise — se mantiene. Matices nuevos que **obligan a matizar** dos puntos del benchmark: (a) la cifra de **$2.500/mes por millón adicional de MAU** que este átomo repite no aparece en el volcado crudo del 11-03, que deriva el volumen a "contact us" (fricción abierta en [[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]); (b) la captura del 11-03 **no incluye la tabla de soporte**, de modo que no confirma ni desmiente la tabla de Scale que este benchmark daba por estable ([[2026-1103-workos-captura-cruda-no-trae-tabla-de-soporte]]). El eje del vault — coste por asiento vs coste por infraestructura — queda por tanto **consolidado**, pero con la partida de AuthKit por encima de 1M de MAU marcada como no verificada.

## Nota de verificación
Las tres fuentes workos son idénticas en precios salvo la tabla de soporte (diff literal entre 11-01 y 11-02). Las cifras de Auth0 y Clerk proceden de sus propios átomos ya existentes, enlazados en el frontmatter.
