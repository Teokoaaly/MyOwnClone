---
id: 2026-1031-workos-authkit-primer-millon-de-mau-gratis
type: atom
certainty: solid
sources: [sources/2026-10-31-workos-pricing.md, sources/2026-11-03-workos-pricing.md]
links: ["[[2026-1031-workos-pricing]]", "[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-clerk-escalera-de-sobrecoste-mru-por-tramos]]", "[[2026-1103-workos-inventario-de-funciones-de-authkit]]", "[[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]"]
---

## Claim
La gestión de usuarios de WorkOS (**AuthKit**) se factura por usuarios activos mensuales: **hasta 1.000.000 de MAU gratis** y **$2.500/mes por cada millón adicional de MAU** ("Up to 1 million users: Free / Per additional 1M users: $2,500 / mo"). La página no publica ningún cargo por encima de 1M de MAU más allá de ese bloque de $2.500/mes.

## Why It Matters
La variable de coste del *user management* de WorkOS es tan plana que es prácticamente irrelevante para MyOwnClone: con el presupuesto de ≤ €4/mes de infraestructura ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]) y una base de tenants en beta, **AuthKit cuesta $0**. Incluso el primer escalón de $2.500/mes exigiría un millón de usuarios activos, una escala inalcanzable para un SaaS multi-tenant que factura por cloning de IA. Es decir, en WorkOS el coste de identidad **no** está en los usuarios sino en las conexiones SSO/Directory Sync ([[2026-1031-workos-sso-escalera-de-conexiones-125-100-80-65]]). Esto invierte la lectura de Auth0, que también tarifa por MAU pero con precios de entrada de $35-$150/mes ([[2026-1101-auth0-precios-por-mau-no-por-evento]]), y deja a Clerk con sobrecoste por MRU en el mismo tramo de escala ([[2026-1101-clerk-escalera-de-sobrecoste-mru-por-tramos]]): WorkOS es el único de los tres cuya partida de usuarios no puede dominar el TCO.

## [FRICTION]
> [[2026-1031-workos-pricing]] afirma que "WorkOS pricing is per-API-call or per-product with tiered plans, creating a hybrid cost model where cost depends on API usage volume and selected products rather than per-user seats".
> Este átomo presiona esa creencia porque la página de precios de WorkOS **no contiene ninguna unidad de facturación por llamada a la API**: las unidades publicadas son MAU (AuthKit), conexiones (SSO y Directory Sync), conexiones SIEM y eventos retenidos (Audit Logs) y checks (Radar). El propio átomo viejo reconoce un "per-product" que la página no separa por producto facturable sino por unidad medida.
> Ambas no pueden ser completamente correctas: o la página tiene una tabla de precios por llamada no capturada, o el modelo real es "por unidad de producto medida" y no "por llamada API". Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
La captura del 2026-11-03 confirma el umbral gratuito de **1 millón de MAU** por dos vías: la lista de "Pay as you go" ("First 1 million active users free") y el FAQ ("WorkOS User Management is free for up to 1 million monthly active users. ... Contact us to learn more about volume pricing"), con el bloque de AuthKit mostrando "$0 /month $0.00 — Free" y un deslizador que llega hasta "0 1M 2M 3M 4M 5M+". **La cifra de $2.500/mes por millón adicional de MAU que afirma este átomo no aparece en el volcado crudo del 11-03** (ver la fricción abierta en [[2026-1103-workos-calculadora-interactiva-y-cta-schedule-a-call]]); se deja el enunciado original intacto a la espera de juicio humano. Novedad de matiz: el propio FAQ deriva el **volumen a "contact us"**, lo que refuerza que la partida de usuarios es irrelevante frente a la partida de conexiones ([[2026-1031-workos-conexion-por-cliente-corporativo-no-por-usuarios]]).

## Nota de verificación
Filas "Up to 1 million users / Free" y "Per additional 1M users / $2,500 / mo" de la sección AuthKit de la captura del 2026-10-31.

## Actualización 2026-11-04
La quinta captura (2026-11-04, volcado crudo) **vuelve a imprimir literalmente las dos filas** que el volcado del 11-03 no traía: "Up to 1 million users — Free" y "Per additional 1M users — **$2,500 / mo**". La cifra queda por tanto **confirmada en la página real** y no solo en las capturas condensadas del 10-31, 11-01 y 11-02. La tabla de AuthKit publica **únicamente** ese bloque (1M gratis + $2.500 por cada millón adicional), sin filas intermedias, aunque el deslizador del calculador llega hasta "5M+". Ver [[2026-1104-workos-authkit-vuelve-a-publicar-2500-por-millon-adicional]].
