---
id: 2026-1101-auth0-m2m-tokens-5k-incluidos-en-professional
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-auth0-addon-agentes-ai-suma-50-por-ciento]]", "[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1103-auth0-professional-4-features-de-seguridad-enterprise]]", "[[2026-1103-auth0-captura-reducida-sin-tablas-ni-feature-matrix]]"]
---

## Claim
Los tokens M2M se cobran por escalones **independientes del número de usuarios**: Free y Essentials incluyen 1.000 tokens M2M, Professional incluye 5.000, y el add-on empieza en $30/mes por 7.500 tokens, $40 por 10.000, escalando linealmente hasta $1.200/mes por 300.000 tokens (en B2C; en B2B el add-on arranca en $10 por 2.500 tokens).

## Why It Matters
Es la línea de coste que el vault no tenía y que el producto **sí** genera: un SaaS multi-tenant con NextAuth 5 hace llamadas machine-to-machine entre el frontend y su backend (y hacia APIs de terceros por tenant), y esos tokens M2M son una partida que escala con el tráfico *entre* tenants, no con los usuarios que se autentican. El coste unitario es de **$0,004 por token** en toda la escalera ($30/7.500 = $40/10.000 = ... = $1.200/300.000), lo que significa que el gasto en M2M es una variable lineal que el founder tiene que vigilar aparte del MAU. Crucialmente, **los tokens M2M no se comparten entre tenants**: el Multi-Tenant Access de MyOwnClone está hoy desconectado entre Flask y Next.js ([[2026-1022-auth-flask-nextauth-desconectados]]) y su JWT lleva el rol en claro ([[2026-1022-myclone-auth-jwt-account-type-creator]]), así que cualquier migración a un proveedor con tenants separados multiplica los M2M por el número de tenants, no solo por el tráfico.

## Nota de verificación
Cifras leídas literalmente de las tablas "M2M Token Add-On (monthly)" y de la tabla comparativa de features. El ratio unitario de $0,004/token es un cálculo de este átomo sobre las cifras de la fuente.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

Dos confirmaciones en el render reducido: (1) la tarjeta de **Professional ($240/mes)** lista explícitamente "**M2M Tokens Add-on**" entre sus features, lo que confirma que el add-on de tokens M2M es la vía de ampliación sobre los tokens incluidos; (2) la sección de add-on enterprise reitera que "M2M add-ons are also available on Professional self-service plans".

La captura **no** publica los precios del add-on M2M ni las cifras de tokens incluidos por plan, de modo que no re-verifica los escalones de $30/7.500 … $1.200/300.000 ni los 1.000/5.000 tokens Free/Professional del Claim de este átomo. Lo que sí añade es una pista de uso: la página presenta el add-on M2M como feature visible de Professional sin coste adjunto publicado en la tarjeta (ver [[2026-1103-auth0-professional-4-features-de-seguridad-enterprise]]).
