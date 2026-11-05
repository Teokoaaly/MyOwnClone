---
id: 2026-1026-brightdata-5000-creditos-gratis-al-mes-para-cuentas-nuevas
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]", "[[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]", "[[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]]"]
---

## Claim
La documentación de Bright Data declara: *"Every new Bright Data account gets **5,000 free credits per month** (~$7.50 value), usable across the Web Unlocker API, SERP API, Web Scraper API, Scraper Studio and Browser API. No credit card, no promo code, no commitment."* Los créditos se renuevan **el primer día de cada mes** y proceden de un **pool único y compartido**. La elegibilidad es automática: *"The free tier is available to **all new accounts** and is applied automatically at signup."* **No** son elegibles las cuentas *"on custom PAYG pricing plans"* ni *"on pre-commit (subscription) plans"*.

## Why It Matters
Es un dato que el vault no tenía: el único punto de entrada de **cero desembolso** del corpus de scraping, y con un valor declarado de **~$7,50/mes** — una cifra dos órdenes de magnitud por debajo del compromiso mínimo de $499/mes del que vive el resto del catálogo de Bright Data ([[2026-1024-brightdata-compromiso-mensual-minimo-499-y-suspension-por-saldo]]). La gratis no es una promoción con cupón (RESIGB50) sino un derecho de alta: la página del 2026-10-24 solo ofrecía el botón "Start free trial" y el cupón, sin créditos ([[2026-1024-brightdata-cupon-50-off-y-match-del-primer-deposito]]).
La consecuencia operativa es que **existe un modo de coste cero para la capa de scraping** que no es el proxy: el Web Unlocker es lo que se paga aquí, y ese producto es justamente el que resuelve captcha sin KYC ([[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]). Es decir, el captcha deja de ser una partida de coste comprable y pasa a ser un recargo de tráfico — pero ese tráfico ahora tiene una versión gratuita y mensual.
Y la restricción de elegibilidad es operativa, no legal: al no ser elegibles los planes pre-commit, **el free tier solo existe dentro del PAYG**, es decir, en el único plan sin compromiso de $499 ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]).

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: cuánto se descuenta un crédito en PAYG, ni el desglose del "~$7.50 value", ni si el valor difiere por producto.

## Nota de extensión 2026-11-03
La página de precios del hub (`sources/2026-11-01-brightdata-pricing.md`, `sources/2026-11-02-brightdata-pricing.md`, `sources/2026-10-31-brightdata-pricing.md`) añade un matiz de **alcance del free tier que este átomo no recogía**: la landing **solo publica "Free tier pricing available" en la ficha de Scraper Studio**, y **ninguna de las otras siete** fichas del catálogo (Proxy Networks, Web Scraper API, Scraping Browser, SERP API, Web Unlocker, Datasets, Bright Insights) lo menciona. Es decir, **la puerta de entrada a coste cero se anuncia únicamente en el producto que el vault no usa**, mientras que la documentación sí describe los 5.000 créditos como aplicables a cinco productos por igual. La lectura operativa para el vault es que **el free tier existe en la documentación y se comercializa en un solo sitio del catálogo**: quien entre por la landing de Web Unlocker o de SERP API no ve la existencia de los créditos gratuitos, y quien entra por la de Scraper Studio puede inferir que el gratis es exclusivo suyo. El detalle del producto que sí lo anuncia —"Only pay for successful requets"— está en [[2026-1101-brightdata-scraper-studio-cobra-solo-por-requests-exitosos]].

Nota de verificación: la captura **no** publica la cifra de 5.000 créditos, ni su unidad, ni la lista de productos elegibles; el "free tier" de la landing es una mención sin detalle.
