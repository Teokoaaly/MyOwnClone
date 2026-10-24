---
id: 2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta
type: atom
certainty: tentative
sources: [sources/2026-10-22-5sim-prices.md, sources/2026-10-23-2captcha-solver.md]
links: ["[[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]", "[[2026-1022-auth-magic-link-codigo-seis-digitos]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1022-precio-99-mensual]]"]
---

## Claim
El precio de una activación SMS de `telegram` en 5sim (2026-10-22) es de **$0.1026 a $8.8897 la unidad**, con una mediana de $0.8942 en las 175 filas y **98 filas a $1 o menos** y 44 a $0.5 o menos; el stock agregado del catálogo es de 128.999.730 unidades. Interpretación (no afirmada por la fuente, sino leída desde ella): una verificación por SMS de alta cuesta entre **0.1 % y 9 %** del precio mensual de 99 del plan más barato de [[2026-1022-precio-99-mensual]] y entre $0.1026 y $8.8897 por alta, es decir un coste marginal frente al modelo de [[2026-1022-costes-por-categoria-tenant]] — pero solo si se elige el par país-operador correcto.

## Why It Matters
El vault documenta que la autenticación actual es **email con código mágico de 6 dígitos** ([[2026-1022-auth-magic-link-codigo-seis-digitos]]), sin ningún canal de SMS. Este átomo cuantifica la alternativa: añadir SMS como canal de verificación (o como paso de antifraude antes de crear el tenant) es aritméticamente viable a escala — el coste por alta baja de diez céntimos si se compra en los países del extremo barato ([[2026-1023-5sim-piso-de-precio-telegram-01026-usd]]) — pero **solo si la elección de país se hace explícitamente**, porque el mismo producto cuesta 86 veces más en Italia que en Colombia.

## [FRICTION]
> [[2026-1022-costes-por-categoria-tenant]] afirma que la estructura de coste del producto separa `categoryCloneResponses` y `categoryIngestion` (facturables al tenant) de `categoryPlatformOps` (memoria, embeddings, clasificadores internos) **absorbidos por la plataforma**, y que "el consumo del tenant escala linealmente pero la operación interna no se traslada".
> Este átomo presiona esa creencia porque un coste de verificación SMS escala **una vez por alta de tenant**, es decir linealmente con el número de tenants, y no es ni `cloneResponses` ni `ingestion`: sería una cuarta categoría no contemplada en el desglose actual.
> Ambas no pueden ser completamente correctas: o la verificación SMS entra como coste variable por tenant facturable (rompiendo la asunción de "operación interna no trasladable"), o se asume absorbida por la plataforma (con lo que su crecimiento lineal erosiona el margen de forma invisible en el panel de [[2026-1022-platform-admin-tenants-costes-mrr]]).
> Marcado para juicio humano, no auto-resuelto.

## [NOTA 2026-10-24]
Añadido a partir de `sources/2026-10-23-2captcha-solver.md`. La verificación SMS no es la única barrera de alta de una identidad: existe un segundo mercado, el de **resolución de captchas**, con precios de lista públicos por 1000 unidades de **$0.5 a $2.99** en los tipos estándar (reCAPTCHA v2, Image Captcha, Cloudflare Turnstile, reCAPTCHA v3, reCAPTCHA Enterprise, Amazon) y hasta **$50** por mil en Arkose/FunCaptcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). Puesto en las mismas unidades del átomo: un reCAPTCHA v2 cuesta entre **$0.001 y $0.00299**, es decir entre una diezmilésima y una centésima parte del precio mínimo del plan de $99/mes ([[2026-1022-precio-99-mensual]]) — **entre 100 y 10.000 veces más barato que un SMS**. Esto no contradice el planteo del átomo, lo dimensiona: el coste marginal de una alta con verificación SMS sigue siendo el SMS porque el captcha es una fracción milésima; pero introduce una categoría nueva en el desglose de [[2026-1022-costes-por-categoria-tenant]] — **captcha resuelto**, coste variable por alta de tenant que no es `categoryCloneResponses` ni `categoryIngestion`, y que además es pagable a un proveedor con SLA (99.9% uptime) en lugar de construirse.
