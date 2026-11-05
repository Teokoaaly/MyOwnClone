---
id: 2026-1027-2captcha-mcp-un-credito-vale-0001-y-el-render-y-camoufox-lo-multiplican
type: atom
certainty: tentative
sources: [sources/2026-10-26-2captcha-pricing-mcp.md]
links: ["[[2026-1027-2captcha-mcp-seis-modos-con-precios-por-llamada]]", "[[2026-1026-brightdata-creditos-como-unidad-sin-conversion-publicada]]", "[[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]"]
---
## Claim
La columna "**Credits per call**" de la tabla del MCP de 2Captcha funciona como **clave de precio lineal**: el precio por 1.000 llamadas es exactamente **0,1 × los créditos** (1 → $0.1; 1,5 → $0.15; 16 → $1.6; 48 → $4.8) y el precio por llamada es **0,0001 × los créditos** ($0.0001; $0.00015; $0.0016; $0.0048). Derivación: **1 crédito = $0.0001 por llamada**.

## Why It Matters
Es la **única conversión crédito→dólar publicada en todo el corpus de scraping y elusión**. El otro proveedor de crédito del vault, Bright Data, publica créditos **sin conversión**: "5,000 free credits per month (~$7.50 value)" y 1 crédito por request o 5 por MB, pero **ninguna página declara cuánto vale un crédito en PAYG** ([[2026-1026-brightdata-creditos-como-unidad-sin-conversion-publicada]], [[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]). Aquí la unidad **sí** es convertible, con lo que la comparación entre ambos proveedores deja de ser un problema de unidades y pasa a ser un problema de **qué consume el crédito**: una llamada de MCP en modo API Tier, o un request de Web Unlocker.

La lectura estructural es que **los seis modos de la tabla son el mismo producto con distinto multiplicador**: API Tier es el modo base (1 crédito) y Camoufox es el mismo producto con **48×** el coste. Es un patrón de pricing por **nivel de sigilo** disfrazado de catálogo de seis productos: el vault ve aquí el mismo eje que en los tipos de captcha de 2Captcha, donde el precio y la latencia se solapan y obligan a elegir por el tipo que aparece en el destino ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]).

Y hay una consecuencia operativa: **si el crédito es convertible y el modo Camoufox cuesta 48 créditos por llamada, el dimensionamiento de una flota de agentes deja de ser una caja negra** — el coste por llamada de cada modo se lee directamente en la tabla y se multiplica por el número de llamadas. Eso es una ventaja operacional real de un catálogo de agentes con precios públicos frente a la opacidad de los proveedores de servicios sin SLA.

Nota de verificación: la tabla es una transcripción literal; la linealidad y el valor del crédito son **derivación aritmética del vault** (las seis filas son consistentes con la regla), y la captura **no** publica el precio del paquete de créditos, la validez del saldo, ni si existe descuento por volumen.
