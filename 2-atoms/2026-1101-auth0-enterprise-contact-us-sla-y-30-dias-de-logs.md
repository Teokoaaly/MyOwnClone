---
id: 2026-1101-auth0-enterprise-contact-us-sla-y-30-dias-de-logs
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-numero-de-tenants-por-plan]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1031-workos-pricing]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]", "[[2026-1103-auth0-lista-de-clientes-enterprise-en-la-pagina-de-precios]]", "[[2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios]]"]
---

## Claim
El plan Enterprise de Auth0 no tiene precio público ("Contact us") e incluye **SLA 99,99 %**, tenants ilimitados, **30 días de retención de logs**, 8 event streams, 30 Actions + Forms, Auth0 Dashboard SSO, Home Realm Discovery, Long Lived Sessions, Continuous Session Protection y Private Key JWT; sus add-on son **Advanced Security Features** y **Private Deployment** (este último también como Private Cloud, despliegue dedicado).

## Why It Matters
El tier Enterprise es exactamente el que un SaaS multi-tenant B2B necesitaría para vender a clientes enterprise — y es el único del que **no se puede derivar un número de coste**, lo que rompe la certeza de presupuesto que el vault intenta construir. Para MyOwnClone, esto significa que la alternativa real a Auth0 no es "Free vs $35/mes" sino "Free vs precio oculto": no hay forma de cotizar el tier que cubre SLA, auditoría y aislamiento por tenant sin hablar con ventas. La comparación con WorkOS es reveladora: WorkOS también es un producto cuyo coste se conoce por producto y por llamada ([[2026-1031-workos-pricing]]), pero al menos publica su escalera; Auth0 publica hasta el umbral en el que deja de publicar. Para el founder con un presupuesto duro de ≤ 4 EUR/mes, la lectura es que cualquier dependencia de identidad que escalarice hacia Enterprise es un riesgo de coste **no acotable**, y por eso conviene que el auth propio con NextAuth 5 siga siendo el camino por defecto mientras el producto es pequeño.

## Nota de verificación
La lista de features de la columna Enterprise y los add-on son lectura literal de las tablas del 2026-11-01; "Contact us" aparece en las tablas de precios tanto para B2C como para B2B a partir de 20.000-30.000 MAU.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

La tarjeta **Enterprise** de esta captura sigue sin precio ("Contact us") y describe el plan como "For enterprises that need to scale. Top-tier SLAs, advanced security, white-glove support and more." Sus bullets visibles son: "Everything in Professional plus…", **Custom User & SSO Tiers**, **99.99% SLA**, **Enterprise Rate Limits**, **Enterprise Administration & Support**, **Private Deployment Add-on** y **Advanced Security Features Add-on**.

Confirma el Claim en el SLA del 99,99 % y en los dos add-on (Private Deployment / Advanced Security Features). Lo que esta captura **no** muestra, y por tanto no puede re-verificar, es la lista completa de features de la columna Enterprise del feature matrix del 2026-11-01 (30 días de logs, 8 event streams, Home Realm Discovery, etc.), porque este render no incluye el feature matrix (ver [[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]). La franja de logos de clientes enterprise que precede a los add-on funciona como argumento de venta de este tier sin precio (ver [[2026-1103-auth0-lista-de-clientes-enterprise-en-la-pagina-de-precios]]).
