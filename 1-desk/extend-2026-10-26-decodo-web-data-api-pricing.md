# Extensiones a átomos existentes — captura 2026-10-26-decodo-web-data-api-pricing

Fuente: `sources/2026-10-26-decodo-web-data-api-pricing.md` (captura `0-raw/2026-10-26-decodo-web-data-api-pricing.md`).
Ninguno de los átomos siguientes se ha modificado: las extensiones se proponen para el Editor.

=== EXTEND 2-atoms/2026-1026-decodo-todos-los-precios-mas-vat-no-incluido
## Nota de extensión 2026-10-27
La página de precios de la **Web Data API** (`decodo.com/web-data-api/pricing`) rompe el patrón que este átomo establece para la línea residencial: sus ocho precios —**$0, $19, $49, $99, $249, $499, $999 y $1499**— **no llevan ninguna marca "+ VAT"**, y el bloque de pago de la página muestra **"SSL Secure Payment"**, **"Your information is protected by 256-bit SSL"** y el icono de **PayPal**, sin mención alguna a **Paddle** ni a "Merchant of Record".

Es decir: **la fiscalidad no es una propiedad de la marca, es una propiedad de cada página**. La página de proxies de Decodo (captura del 2026-10-25) marca los ocho precios "+ VAT" y explica en el FAQ que las órdenes pasan por Paddle como Merchant of Record; la página de la API, del mismo proveedor y del mismo mes, **no marca fiscalidad y no menciona Paddle**. Con un IVA del 21 %, el plan de entrada de $19/mes de la API pasa a **$22,99** si el precio es neto, o se queda en $19 si es bruto — y **la captura no permite decidirlo**, porque no hay nota fiscal que lo diga.

Consecuencia para el modelo de coste: **toda comparación entre la línea de proxies y la línea de scraping de Decodo está incompleta por el lado fiscal**, y el vault tiene que leer el "+ VAT" como un atributo de la página, no del proveedor. Ver [[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]] y [[2026-1026-decodo-paddle-como-merchant-of-record-y-cripto-excepto-isp-y-datacenter]].
=== END

=== EXTEND 2-atoms/2026-1027-2captcha-scraper-api-030-por-mil-de-requests-en-los-cinco-planes
## Nota de extensión 2026-10-27
La Web Data API de Decodo da **un segundo precio de catálogo por 1.000 requests** en el corpus, y **es la mitad**: el titular es **"From $0.15/1K"** —"Access web data, starting at $0.15/1K requests"— frente a los **$0,30 por 1.000 requests** del Scraper API de 2Captcha, cuyo precio unitario además es **invariante al volumen** en los cinco planes.

El contraste de estructura es lo que importa para el thread: 2Captcha cotiza **un único precio unitario en cinco tamaños de precarga** (nunca mejora por volumen), mientras que Decodo publica **una escalera de ocho planes** en la que el precio efectivo por mil **cae de forma monótona**: **$0,5000/1K páginas** en el plan de $19, **$0,3000** en el de $99, **$0,2075** en el de $249, **$0,1848** en el de $499, **$0,1611** en el de $999 y **$0,1514** en el de $1499. Es decir, **el titular de $0,15/1K solo es alcanzable en el plan más caro**, y su equivalente por crawls es $0,5169/1K.

El dato que el vault debe registrar para el agregador: **el precio por 1.000 requests del sector está entre $0,15 y $0,30**, y **el mismo número en dos proveedores significa dos cosas distintas** — en 2Captcha es el precio único del producto; en Decodo es el mejor caso de una escalera de suscripción con cuota. Ver [[2026-1027-decodo-el-titular-de-015-por-mil-solo-se-alcanza-en-el-plan-de-1499]] y [[2026-1027-decodo-la-unidad-no-es-estable-requests-paginas-y-crawls]].
=== END

=== EXTEND 2-atoms/2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes
## Nota de extensión 2026-10-27
La captura de la Web Data API de Decodo **confirma la dirección del giro que este átomo describe para 2Captcha, pero desde un proveedor que viene del proxy**, y añade dos superficies que el corpus no tenía en ningún proveedor de acceso a web: **CLI** ("Run any endpoint from your terminal or a shell script. Good for quick tests, CI jobs, and coding agents with shell access") y **agent skills** ("Drop a skill file into your coding assistant so it calls the API correctly, with the right endpoint, parameters, and output format, **instead of guessing from docs**"). La lista completa de la home es **MCP Server + CLI + Agent Skills + SDKs**, con **n8n, LangChain, LlamaIndex y OpenClaw** como integraciones declaradas, y el servidor MCP **"Officially listed in GitHub's MCP Registry"**.

El ángulo que este átomo abre y la captura confirma: **el giro hacia agentes ya no es de un proveedor de captcha, es de todo el sector de acceso a web**. Y la frase de justification de las skills —"instead of guessing from docs"— identifica **la partida que el vault no había cotizado**: el **coste del error de invocación**, que en un producto facturado por mil de requests **se paga como cuota consumida**. Ver [[2026-1027-decodo-mcp-oficial-en-el-registro-de-github-con-cli-y-agent-skills]].
=== END

=== EXTEND 2-atoms/2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente
## Nota de extensión 2026-10-27
Decodo publica **su propio servidor MCP y lo lista en el registro oficial de MCP de GitHub** ("Officially listed in GitHub's MCP Registry"), lo que abre una diferencia de **distribribución** frente al patrón de Bright Data que este átomo documenta: aquí el MCP es **una entrada de catálogo de un registro público** (descubrible por un agente que busca herramientas), no un repositorio propio que hay que conocer de antemano.

La otra diferencia es que **Decodo llega al MCP desde el proxy y reutiliza su pool de 125M+**, con las cuatro superficies de integración en el mismo bloque: **MCP Server + CLI + Agent Skills + SDKs** (Python y TypeScript), más **n8n, LangChain, LlamaIndex y OpenClaw**. El vault puede registrar que la **superficie de agente ya está completa en Decodo** y que **ninguna de las cuatro se cotiza por separado**: la página de precios declara las mismas features en todos los planes, incluido el gratuito. Ver [[2026-1027-decodo-mcp-oficial-en-el-registro-de-github-con-cli-y-agent-skills]] y [[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]].
=== END

=== EXTEND 2-atoms/2026-1026-decodo-reembolso-14-dias-con-limite-del-20-y-10-de-trafico
## Nota de extensión 2026-10-27
La página de precios de la Web Data API incluye entre las features de **todos** los planes la línea **"14-day money-back"**, y el FAQ de la home confirma que la API **no exige tarjeta** ("You can start using Web Data API with a free starter plan without a credit card. Sign up, test your requests, and upgrade when you need more capacity"). Es decir: **la línea de scraping hereda la etiqueta de garantía de la línea de proxy, pero las condiciones de esa garantía no se trasladan** — este átomo documenta que la garantía de proxies está condicionada a **primera compra, no haber usado la prueba de 3 días, 20 % del tráfico residencial o 10 % del Enterprise, cuenta no suspendida y sin contracargo**, condiciones pensadas para un consumo medido en gigabytes.

En la línea de scraping, donde la unidad es **crawl o página**, **ninguna de esas condiciones tiene equivalente**: ¿qué sería el "20 % del tráfico" de un plan cuyo límite son 9,9M páginas? La captura **no** publica las condiciones aplicables a la API, solo la etiqueta. El vault debe citar **"14-day money-back" como etiqueta sin condiciones para la API**, y no extenderle por analogía las de la línea residencial. Ver [[2026-1027-decodo-plan-gratuito-de-la-web-data-api-con-5-de-credito-y-10k-solicitudes-sin-tarjeta]].
=== END

=== EXTEND 2-atoms/2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio
## Nota de extensión 2026-10-27
Decodo publica en su home un tablero de **ocho líneas con cinco unidades de precio** —Web Data API **$0.15/1K**, Video Downloader **$0.08/GB**, Residential **$2/GB**, ISP **$0.27/IP**, Mobile **$2.25/GB**, Datacenter **$0.02/IP**, Site Unblocker **$0.95/1K req** y High-Speed **"Price on request"**—, más **tres herramientas gratuitas** (Chrome Proxy Extension, Firefox Add-on, Proxy Checker). Es el **segundo tablero del corpus con unidades mezcladas**, y el que más unidades añade por línea.

Tres datos que este átomo deja ahora disponibles para la tabla de coste por insumo, y que **no aparecen en ningún otro proveedor medido**: **datacenter a $0,02/IP** (×25 más barato que el $1,39/IP de IPRoyal), **ISP a $0,27/IP** (×6,7 más barato que el $1,80/IP de IPRoyal) y **móvil a $2,25/GB** (la primera vez que el móvil de un proveedor se cotiza **en la misma unidad que el residencial**, lo que hace comparables las dos líneas internas de Decodo; en IPRoyal el móvil era $/mes fijo, [[2026-1024-iproyal-movil-117-al-mes-y-45m-de-ips]]).

Y un patrón que el tablero hace explícito: **la línea de empresa vuelve a quedar fuera del catálogo**. "High-Speed Proxies — Price on request" es la segunda partida no cotizable de Decodo, después del Enterprise de la API — el mismo hueco que este átomo ya detectara en Proton ([[2026-1024-proton-ofrece-vpn-para-empresas-sin-precio-publicado]]). Ver [[2026-1027-decodo-tablero-de-precios-de-la-home-con-ocho-lineas-y-cinco-unidades]].
=== END
