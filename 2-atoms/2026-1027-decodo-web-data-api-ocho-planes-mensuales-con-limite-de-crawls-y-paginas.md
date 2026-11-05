---
id: 2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]", "[[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]", "[[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]]"]
---

## Claim
La página de precios de la **Web Data API** publica **ocho planes mensuales** (pestaña "Regular"), cada uno con tres cifras: peticiones por segundo, precio y un límite de uso expresado en **crawls o páginas**:

| req/s | $/mes | Límite |
|---|---|---|
| 10 req/s | $0 | Up to 5K crawls or 10K pages scraped |
| 10 req/s | $19 | Up to 19K crawls or 38K pages scraped |
| 25 req/s | $49 | Up to 65K crawls or 122K pages scraped |
| 50 req/s | $99 | Up to 141K crawls or 330K pages scraped |
| 100 req/s | $249 | Up to 383K crawls or 1.2M pages scraped |
| 150 req/s | $499 | Up to 831K crawls or 2.7M pages scraped |
| 200 req/s | $999 | Up to 1.8M crawls or 6.2M pages scraped |
| 200 req/s | $1499 | Up to 2.9M crawls or 9.9M pages scraped |

La página declara además una segunda pestaña **"Enterprise"** (cuyo contenido no aparece en la captura) y un cierre "Need more? Chat with us and we'll find the best solution for you" con "Contact sales".

## Why It Matters
Es el **primer modelo de precio por suscripción con cuota de uso** del corpus de proveedores de acceso a web del vault: hasta ahora todo el sector se medía en **$/GB** ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]) o en **$/IP al mes** ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]), y ninguna página cotizaba el scraping como **un plan con contador de crawls y páginas**. La consecuencia práctica es que **el coste deja de depender de los bytes y pasa a depender de las unidades de trabajo**: el pipeline del vault consume peticiones, no gigabytes.
Y es una respuesta directa a la pregunta que el thread de verificación tiene abierta: cuando el proveedor **mete el proxy dentro de la API**, ya no se puede cotizar el proxy como insumo por separado, porque **el precio del scraper incluye el tráfico**. El coste de la elusión deja de ser una línea del modelo y pasa a estar embebido en la cuota ([[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]).
El punto que el vault tiene que leer con cuidado es que la escalera **no es de $/GB sino de cuota**, y por tanto **no es comparable** con la escalera residencial del mismo proveedor ([[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]): ocho planes, ocho precios, y ninguna cifra que se pueda convertir en $/GB.

## [FRICTION]
> [[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]] documenta que el modo de pago por uso de Decodo es **$4/GB**, que exige Wallet recargado, que se compra de 1 GB en 1 GB y que **excluye la suscripción mensual** ("you can't have a monthly subscription plan and Pay As You Go simultaneously").
> Este átomo presiona ese dato en un punto: **el mismo proveedor vende ahora el acceso a la web con un modelo de suscripción por cuota que no es ni el PAYG por GB ni el proxy residencial**, con planes de $0 a $1499/mes medidos en crawls y páginas, y con un plan gratuito permanente de 10 req/s. Es decir, la incompatibilidad "suscripción o PAYG" **sigue existiendo dentro de la línea de proxy**, pero **la Web Data API abre una tercera vía** — suscripción por uso, sin GB, sin Wallet y sin cuota en bytes — donde el tráfico va incluido.
> Ambas no pueden ser completamente correctas: o Decodo tiene un único modelo de cobro por acceso a la web, o tiene **tres modelos simultáneos e incompatibles** (GB por suscripción, GB por Wallet, y cuota de crawls/páginas) que obligan a leer el precio de cada línea por separado. Marcado para juicio humano, no auto-resuelto: la captura no publica si el tráfico de proxy incluido en la Web Data API cuenta para algún límite, ni si los planes de la API pueden migrarse a proxies.

## Nota de verificación
Precios, límites y req/s transcritos literalmente de la página. La captura **no** publica: qué contiene la pestaña "Enterprise", el precio del excedente, si las cuotas caducan o se acumulan, la política de fair-use, ni si el límite "crawls or pages" aplica a `/scrape` y `/map` igual que a `/crawl`.
