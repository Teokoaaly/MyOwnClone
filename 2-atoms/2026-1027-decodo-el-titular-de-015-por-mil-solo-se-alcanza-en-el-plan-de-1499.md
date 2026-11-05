---
id: 2026-1027-decodo-el-titular-de-015-por-mil-solo-se-alcanza-en-el-plan-de-1499
type: atom
certainty: tentative
sources: [sources/2026-10-26-decodo-smartproxy-home.md, sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1026-decodo-titular-de-2-por-gb-y-entrada-real-de-375]]", "[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]", "[[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]]", "[[2026-1024-iproyal-residencial-175-por-gb-y-pool-de-64m]]"]
---

## Claim
La home de Decodo anuncia la Web Data API con el titular "**Access web data, starting at $0.15/1K requests**" y el panel de precios con "**Web Data API — From $0.15/1K**". Recalculando el precio unitario de los ocho planes publicados a partir de sus límites ("Up to X crawls or Y pages scraped"), **ningún plan por debajo de $1499/mes llega a $0,15 por mil**:

| Plan | $/mes | $/1K crawls | $/1K pages |
|---|---|---|---|
| $19 | 19 | 1,0000 | 0,5000 |
| $49 | 49 | 0,7538 | 0,4016 |
| $99 | 99 | 0,7021 | 0,3000 |
| $249 | 249 | 0,6501 | 0,2075 |
| $499 | 499 | 0,6005 | 0,1848 |
| $999 | 999 | 0,5550 | 0,1611 |
| $1499 | 1499 | 0,5169 | 0,1514 |

El único plan cuyo precio por mil **de páginas** redondea a $0,15 es el de $1499/mes (0,1514); **ningún plan llega a $0,15 por mil de crawls** (el mínimo es 0,5169). El titular es, por tanto, el **mejor precio unitario del catálogo** —el mismo patrón que el vault ya registró en el precio titular residencial de $2/GB, cuyo precio de entrada real era $3,75/GB ([[2026-1026-decodo-titular-de-2-por-gb-y-entrada-real-de-375]])— y además es un titular **condicional a la unidad**: si la operación se factura por crawls, el mejor precio unitario posible es $0,5169 por 1K, **×3,4 el titular**.

## Why It Matters
La diferencia entre titular y entrada es aquí de **×3,3 en precio unitario** ($0,1514 en el mejor caso frente a $0,50 del plan de $19), y el titular solo se alcanza **comprometiendo $1499 al mes** — un gasto que para el vault (techo de ≤ €4/mes) está tres órdenes de magnitud fuera de alcance ([[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]). Cotizar la Web Data API con el titular "$0,15/1K" para un flujo pequeño es un error de un factor 3,3, exactamente como lo era cotizar el proxy a $2/GB.

El segundo punto es más fino y más útil: **el titular está calculado sobre la unidad que sale más cara de cotizar (páginas), no sobre la que el sector usa para Crawl (crawls)**. Es decir, el número con el que se anuncia el producto es el que **excluye** el modo de operación por páginas múltiples, que es el que consume un crawler de verdad. Un pipeline de crawl real —que es lo que el vault hace, recorriendo sitios enteros ([[2026-1022-myclone-scraping-ingestion-pipeline]])— se factura a $0,5169 por 1K de crawls en el mejor caso, y a $1,00 en el plan de $19. El titular no es solo "el mejor caso": es **el mejor caso de la unidad que no se usa**.

De ahí el corolario contable: el **marginal** entre los dos últimos planes es de $500 por **1,1M crawls** o **3,7M pages** adicionales, es decir **$0,1351 por 1K pages** marginal — ligeramente por debajo del propio titular. El precio unitario mejora de forma monótona al subir de plan (de $0,50 a $0,1514 por 1K pages), pero **todo el recorrido de esa mejora está en el tramo alto de la escalera**, el único que el vault no puede pagar.

## [FRICTION]
> [[2026-1026-decodo-titular-de-2-por-gb-y-entrada-real-de-375]] establece el patrón "**precio titular = mejor caso del catálogo, no precio de arranque**" para la línea residencial de Decodo, con un ×1,875 entre titular ($2/GB) y entrada real ($3,75/GB).
> Este átomo presiona ese patrón en dos puntos: (1) en la línea de scraping la distancia es **×3,3** en lugar de ×1,875, y (2) el titular no es siquiera alcanzable en la unidad principal del producto — announced sobre páginas, facturable también sobre crawls a ×3,4. Además, en la línea residencial el titular de $2/GB era alcanzable comprando $2.000/mes, mientras que aquí el titular de $0,15/1K **no es alcanzable en ningún plan** cuyo precio por mil de crawls lo confirme, lo que abre la duda de si el titular es siquiera un precio realizable.
> Ambas no pueden ser completamente correctas: o "from $X" es siempre un precio realizable por algún cliente del catálogo, o es un precio de Better Case cuyo compuesto es otro producto distinto del que se anuncia. Marcado para juicio humano, no auto-resuelto: la captura no publica el precio por excedente ni la definición de la "request" del titular.

## Nota de verificación
Los precios por 1K son **cálculos del vault** sobre los límites y precios publicados; las cifras de titular son literales. `certainty: tentative` porque la atribución del titular a un plan concreto depende de qué sea una "request" (crawl o página) y de si el precio por unidad es lineal dentro de cada plan. La captura **no** publica: precio del excedente, si hay descuento por volumen dentro del plan, ni si existe un plan de pago por uso (PAYG) para la API.
