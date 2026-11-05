---
id: 2026-1026-brightdata-creditos-como-unidad-sin-conversion-publicada
type: atom
certainty: tentative
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]", "[[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]", "[[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]"]
---

## Claim
La **portada de la documentación** presenta el scraping como se cobra en una unidad que **no es $/GB, ni $/IP, ni $/request**: el **crédito**, con un free tier declarado de **"5,000 free credits per month"** y la promesa de **"one API key"**. En la misma página, el lado proxy sí se ofrece con unidades nombradas por producto (residencial "400M+ real-user IPs", datacenter "Fast, low-cost IPs", ISP "Static residential-grade IPs"), pero **la página de documentación no publica ninguna conversión** crédito→dólar, crédito→GB o crédito→request.

## Why It Matters
La tabla de coste por insumo del thread mide el proxy con cuatro unidades distintas porque cada proveedor publica la suya ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]), y concluía que el $/GB es "un parámetro de proveedor, no de mercado" ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]). El crédito es la **quinta unidad**, y aporta una observación que las otras no: **la unidad existe en dos capas del mismo proveedor con visible contradicción** — en la página de precios el proxy se mide en GB y en IPs, y en la página de documentación el producto de datos se mide en créditos, sin puente entre ambas.
La consecuencia práctica es que **el lado API de Bright Data no se puede cotizar con esta captura**: un pipeline que consuma el endpoint de scrape no tiene un $/GB, ni un $/request, ni siquiera un "crédito/precio" interpretable. El valor del átomo es, por eso, **el hueco documental**, no la cifra: marca qué tiene que resolver la página de free tier para que la unidad sea comparable con el resto de la tabla. Ese resolver ya está en [[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]] (1 crédito por request, 5 por MB en Browser API, valor declarado ~$7,50) y en [[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]] (pool compartido por cinco productos, proxies excluidos); la portada, en cambio, sigue sin dar ninguno de los dos datos.
Para el vault esto deja una asimetría incómoda y verificable: **el proveedor con el peor contrato de proxy (PAYG a $4/GB, compromiso de $499) es también el que ofrece la entrada más barata —0 $, sin tarjeta— en la parte del catálogo que el vault todavía no puede medir**.

## Nota de verificación
La captura **no publica**: la equivalencia crédito/dólar, qué productos y endpoints consumen crédito, si el free tier es mensual acumulable o se renueva, ni la política de caducidad del crédito sobrante. El átomo queda en `tentative` porque su claim es sobre un **hueco documental**, no sobre una cifra: la ausencia de conversión en esta página es un hecho verificado, y su resolución está en otra captura.


## Nota de extensión 2026-10-27
El punto que este átomo levanta —que **el crédito es la unidad del sector y que su conversión a dinero no está publicada**— admite ahora su primer contraejemplo verificado, y por tanto la primera excepción del vault. El catálogo de MCP de 2Captcha publica **cuatro columnas** —"Credits per call", "Price per 1,000 calls", "Price per call" y acción— y de ahí se deriva linealmente que **1 crédito = $0.0001 por llamada**, con el rango de **1 crédito** (API Tier) a **48 créditos** (Camoufox) ([[2026-1027-2captcha-mcp-un-credito-vale-0001-y-el-render-y-camoufox-lo-multiplican]]).

**Esto cambia el estado del conocimiento del vault de "crédito no cotizable" a "crédito cotizable en uno de los dos proveedores".** Bright Data sigue sin publicar la conversión de su crédito a dinero en PAYG —solo el valor declarado de los 5.000 créditos gratuitos ("~$7.50 value"), del que este mismo run ya derivó ~$0,0015/request y ~$1,50/1.000 ([[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]])—, mientras que 2Captcha **sí** publica el precio por llamada en dólares junto al número de créditos. La consecuencia práctica: **comparar la capa de scraping entre los dos proveedores ya no exige suponer una equivalencia de crédito**, porque uno de los dos lados es directamente convertible. La comparación posible es ahora **por unidad de producto** (request, MB de tráfico, llamada de MCP), no por crédito.

**La lección de fondo se refuerza, no se debilita**: el crédito sigue siendo una **unidad arbitraria** —en 2Captcha 1 crédito = 1 llamada de API Tier, en Bright Data 1 crédito = 1 request de Web Unblocker y 1/5 de MB de Browser API—, pero el vault puede ahora afirmar que **la opacidad de la conversión de crédito es una característica de Bright Data**, no una propiedad del modelo de créditos como tal.
