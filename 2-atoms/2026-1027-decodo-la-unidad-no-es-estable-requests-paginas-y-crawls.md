---
id: 2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-web-data-api-pricing.md, sources/2026-10-26-decodo-smartproxy-home.md]
links: ["[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]", "[[2026-1027-decodo-concurrencia-por-plan-de-10-a-200-req-s-con-techo-en-los-dos-ultimos]]", "[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]"]
---

## Claim
Las dos capturas de Decodo del 2026-10-26 nombran la unidad del scraping de **cuatro formas distintas**, y ninguna de ellas está definida por el proveedor:

- **En la página de precios de la Web Data API**: el límite de cada plan se expresa en "**crawls** or **pages scraped**" (hasta 5K crawls o 10K pages en el plan gratuito; hasta 2.9M crawls o 9.9M pages en el de $1499), y la concurrencia se expresa aparte en "**req/s**" (10 a 200 req/s).
- **En la home (smartproxy.com)**: el precio se anuncia como "Access web data, starting at **$0.15/1K requests**" y el panel de precios como "Web Data API — From **$0.15/1K**", sin decir si esa "request" es un crawl o una página.
- En la misma home, el plan gratuito de la API se describe como "$5 in testing credits (**up to 10k requests**)" y el banner final como "up to **10K free monthly requests**".
- En el panel de precios de la home, el **Site Unblocker** se cotiza en "$0.95/**1K req.**" y el **Video Downloader** en "$0.08/**GB**", con lo que la misma pantalla mezcla unidades de peticiones, bytes y proxies.

La correspondencia entre "crawl" y "página" **no es constante entre planes**: el cociente páginas/crawl va de **2,0** en los dos primeros planes (5K→10K, 19K→38K), baja a **1,877** en el de $49 (65K→122K) y sube hasta **3,44** en el de $999 (1.8M→6.2M). El proveedor no publica qué significa exactamente un "crawl".

## Why It Matters
Es el mismo problema que el vault ya registró con las unidades de precio del sector —el $/GB, el $/proxy, el $/mes y el $/mil de solicitudes no son la misma magnitud ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]])— pero aquí el problema es **de dentro del mismo producto**: es la misma API, del mismo proveedor, cotizada en cuatro unidades a la vez, con un precio unitario que **depende de cuál se elija**.

La consecuencia aritmética es que el coste de la misma operación de scraping se mueve en un factor **×2 a ×3,4** según la unidad. Con los límites publicados: un plan de $19/mes da 38K páginas ($0,50 por 1K páginas) o 19K crawls ($1,00 por 1K crawls); el plan de $1499/mes da 9,9M páginas ($0,1514 por 1K) o 2,9M crawls ($0,5169 por 1K). Con la misma ejecución, el vault tiene que **elegir la unidad antes de cotizar**, y el proveedor no publica la regla de conversión, solo los dos números.

Y hay una cuarta unidad encima, la de la concurrencia, que **no es una cuota**: los "req/s" limitan peticiones simultáneas, no el total, y el total de la cuota se mide en crawls o páginas. Un pipeline que satura los 200 req/s del plan de $999 **no puede consumir más cuota bajando de plan**, y uno que no llega a 50 req/s **no necesita subir de plan**: son dos ejes distintos que la tabla de precios presenta en la misma columna visual. Esto separa la API de todo el resto del corpus de proxy, donde el único límite publicado era el de tráfico ([[2026-1026-decodo-payg-a-4-por-gb-solo-con-wallet-y-un-gb-a-la-vez]]).

## Nota de verificación
Unidades y cifras transcritas literalmente de las dos fuentes. Los cocientes páginas/crawl y los precios por 1K son **cálculos del vault sobre los límites publicados**. La captura **no** publica: la definición de "crawl", si "request" del titular es crawl o página, cómo se factura el excedente de cuota, ni si los req/s son peticiones concurrentes en curso o peticiones por segundo servidas con cola.
