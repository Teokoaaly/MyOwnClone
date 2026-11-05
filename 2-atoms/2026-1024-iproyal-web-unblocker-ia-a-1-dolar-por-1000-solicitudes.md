---
id: 2026-1024-iproyal-web-unblocker-ia-a-1-dolar-por-1000-solicitudes
type: atom
certainty: solid
sources: [sources/2026-10-24-iproyal-pricing.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]", "[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]"]
---

## Claim
La quinta línea de IPRoyal es **Web Unblocker**, etiquetada **"AI"**, y se vende a **"from $1.00/1000 requests"**: *"Gather data without worrying about blocks. Our **AI-driven solution manages locations, rotation, and fingerprints in the background**, keeping your workflows reliable."*

## Why It Matters
Es el **mismo producto con el mismo precio** que 2Captcha publica desde su giro hacia scraping, pero en un proveedor de proxy: 2Captcha vende su Web Unlocker como "automatically handles blocks, captchas, and proxy rotation, **so you pay only for successful data extraction**" ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]), y IPRoyal lo formula como gestión en segundo plano de "locations, rotation, and fingerprints". El precio de catálogo de 2Captcha va de **$0.5 a $2.99 por 1000** ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]), de modo que el **$1.00/1000** de IPRoyal cae dentro de ese rango: es una **comodity de elusión con precio de mercado**, no un producto premium.
La diferencia de fondo es la **unidad**: "requests" no es "captchas resueltos". Un Web Unblocker cobra por **petición intentada**, mientras que 2Captcha cobra por **captcha efectivamente resuelto** ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]). Eso es una diferencia de riesgo que el vault debe tener presente: en el modelo por "successful data extraction" el proveedor asume el riesgo de que su propia elusión falle; en el modelo por "requests" ese riesgo lo asume el cliente, y el proveedor gana igual.

## [FRICTION]
> [[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]] establece que el proveedor "paga solo por captchas resueltos" y "the server load does not affect the price", es decir, que el contrato económico **traslada al proveedor el riesgo de su propia elusión**.
> Este átomo presiona ese principio en un punto: el Web Unblocker de IPRoyal es **la misma capacidad conceptual** —proxy + rotación + fingerprints + evasión de bloqueos— cobrada **por 1000 requests**, es decir por la unidad de entrada y no por el resultado. Si las dos cosas son comparables, entonces "pagar por el resultado" no es una propiedad técnica del producto sino una **elección de empaque comercial** que cada proveedor hace por su cuenta, y el vault no puede inferirla del tipo de producto: tiene que leer la unidad de la tabla de precios de cada proveedor por separado.
> Ambas no pueden ser completamente correctas: o la unidad de cobro refleja necesariamente una asimetría de riesgo real (el proveedor solo puede vender "por resultado" si su elusión es fiable y su carga es estable), o es un factor comercial negociable y dos proveedores con la misma tecnología pueden trasladar la misma asimetría. Marcado para juicio humano, no auto-resuelto: la captura de IPRoyal no publica si las peticiones fallidas también se facturan.

## Nota de verificación
Precio transcrito literalmente. La captura **no** publica: qué es una "request" (¿una petición HTTP, una URL, un intento?), si se factura lo fallido, número de IPs, ni SLA. El rótulo "AI" es marketing sin detalle de modelo.


## Nota de extensión 2026-10-26
La documentación de Bright Data del 2026-10-25 introduce en el corpus un **precio efectivo de $0** para la misma capacidad que este átomo sitúa en **"from $1.00/1000 requests"**: el free tier de Bright Data da *"5,000 free credits per month (~$7.50 value)"* y el Web Unlocker consume **1 crédito por request**, es decir ~5.000 requests de Web Unlocker **gratis al mes** en toda cuenta nueva ([[2026-1026-brightdata-5000-creditos-gratis-al-mes-para-cuentas-nuevas]] y [[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]). Consecuencia para la lectura de este átomo: el "$1,00/1000" es **el precio de reposición**, no el coste de entrada; y el valor declarado de "~$7,50" implica un precio unitario derivado de ~$1,50/1.000 requests, dentro del mismo orden de magnitud que el de IPRoyal y **por debajo** del rango $0,5–$2,99/1000 de 2Captcha ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]). El razonamiento del átomo sobre la **diferencia de unidad** (request intentada vs captcha resuelto) **se mantiene intacto** —el free tier no cambia qué es una "request"— pero el vault tiene que **distinguir precio de catálogo de precio efectivo** al comparar proveedores de elusión.


## Nota de extensión 2026-10-27
Este átomo afirma que el **"from $1.00/1000 requests"** del Web Unblocker de IPRoyal "cae dentro del rango $0.5 — $2.99 por 1000" de 2Captcha y es por tanto "una **comodity de elusión con precio de mercado**". La captura del Scraper API de 2Captcha del 2026-10-26 **reajusta ese precio de mercado en un 3,3×**: el Scraper API publica **$0.3 por 1.000 requests** en sus cinco planes (1.000 → $0.3; 10.000 → $3; 100.000 → $30; 1.000.000 → $300; 10.000.000 → $3.000), con precio unitario **invariante al volumen** ([[2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes]]).

**La conclusión del átomo no se cae, pero su cifra de referencia queda desactualizada.** Con $0,30/1.000 requests en el mismo sector y con la misma unidad nominal, el "$1,00/1.000" de IPRoyal **ya no es el piso del mercado**: es **3,3 veces más caro que la alternativa del mismo proveedor rival**, y el vault tiene ahora un intervalo real de **$0,30 — $1,00 por 1.000 requests** para la extracción con evasión. La lectura correcta pasa de "el precio de mercado del sector es ~$1/1000" a "**el precio de mercado del sector está entre $0,30 y $1,00 por 1.000 requests, y el proveedor que publica el precio más bajo es también el que publica una escalera de cinco planes sin descuento**".

**La diferencia de unidad que este átomo sitúa en el eje de su lectura (requests intentadas vs captchas resueltos) se refuerza con un dato nuevo del mismo proveedor.** El Scraper API se cobra por **request intentada**, mientras que 2Captcha cobra por **captcha resuelto** ([[2026-1024-2captcha-solo-se-paga-por-captcha-resuelto]]). La consecuencia es que el vault puede ahora afirmar algo más fuerte que antes: **el mismo proveedor, en dos líneas de producto del mismo giro hacia el scraping, aplica las dos unidades opuestas**. "Pagar por el resultado" queda demostrado como **elección de empaque por línea**, no como rasgo del proveedor ni del producto.

Nota de verificación: la comparación asume que una "request" del Scraper API y una "request" del Web Unblocker son unidades homologables; **ninguna de las dos capturas define qué es una request** (petición HTTP, URL, intento, registro), así que el factor 3,3× es aritmética sobre cifras transcritas, no una comparación de valor de mercado.
