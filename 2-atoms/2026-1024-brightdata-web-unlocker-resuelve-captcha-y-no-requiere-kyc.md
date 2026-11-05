---
id: 2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]"]
---

## Claim
Bright Data recomienda Web Unlocker como la herramienta de scraping en lugar del proxy crudo: *"The Web Unlocker uses either a Datacenter or Residential IP and fully handles all of the unblocking, including CAPTCHA solving and automated retries. Your scraper/crawler simply sends a query to Web Unlocker and all the unblocking is done in the background."* Y añade la frase que la hace comprable sin fricción: *"Using Web Unlocker does not require going through the KYC process."*

## Why It Matters
Es el mismo giro de producto que ya se registró en 2Captcha —el proveedor que vendía eludir controles pasa a vender **el servicio que los elude por ti**, con Browser API, Scraper API, Web Unlocker y servidores MCP para agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]])— y aquí tiene un efecto añadido: **elimina el KYC**, que es la barrera que bloquea el pool residencial ([[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]).
Para el vault esto tiene una consecuencia aritmética directa: si el scraper **no** tiene que resolver el captcha por su cuenta, desaparece una partida del coste por insumo — la de 2Captcha, entre $0.0005 y $0.05 por captcha ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]])— y se reabsorbe en el precio del tráfico. Es decir, **el CAPTCHA puede dejar de ser una línea del modelo de coste** y pasar a ser un recargo implícito del $/GB. Lo que la captura **no** publica es el precio de Web Unlocker, de modo que el ahorro en captcha no se puede cuantificar contra el coste del tráfico.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: el precio de Web Unlocker ni su unidad (por GB, por request o por CAPTCHA resuelto), si es un producto independiente del plan de proxy, ni los reintentos automáticos incluidos.


## Nota de extensión 2026-10-26
La introducción de la documentación sitúa a Web Unlocker dentro de un **catálogo de APIs de extracción** mucho más amplio que el que este átomo recogía. La sección "Data extraction" lista **Web Unlocker API, SERP API, Web Scraper API, Scraper Studio y Browser API**, y la sección "Proxy networks" ofrece las tres redes. Es decir: **Web Unlocker deja de ser "la alternativa al proxy crudo" y pasa a ser una de cinco APIs de datos con igual footing comercial**, lo que refuerza la hipótesis del átomo de que el CAPTCHA se reabsorbe en un recargo del acceso en lugar de ser una línea del modelo de coste del vault ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]).

Dos precisiones que esta fuente añade y que el átomo no tenía:
1. **La afirmación de "no requiere KYC" no se repite en la landing** — el texto exacto "Using Web Unlocker does not require going through the KYC process" sigue siendo solo de la página de precios. La documentación de intro no lo confirma, no lo contradice.
2. **Browser API aparece como "Remote browsers for automation"**, es decir, la externalización de la huella y de la navegación, que es exactamente el producto que 2Captcha había lanado en su giro hacia scraping y agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]) y que Decodo que más tarde apuntó como integración de navegador incluida en cada plan ([[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]). Ver [[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]].

Lo que sigue sin publicarse: el precio de Web Unlocker, su unidad, y si las cinco APIs comparten o no el mismo contador de consumo. La captura del free tier sugiere que comparten pool de créditos, lo que cerraría el círculo.


## Nota de extensión 2026-10-26
Este átomo decía que *"la captura no publica el precio de Web Unlocker"*, de modo que el ahorro en captcha no se podía cuantificar contra el coste del tráfico. La documentación de billing del 2026-10-25 (`sources/2026-10-25-brightdata-free-tier.md`) **cierra ese hueco parcialmente**: el Web Unlocker consume **1 crédito por request** y los **5.000 créditos gratuitos mensuales** cubren *"up to 5,000 requests or records"* en los tres productos de la API, con un valor declarado de **~$7,50/mes** — es decir, **5.000 requests de Web Unlocker a coste cero** en el primer mes de cualquier cuenta nueva. Sigue sin publicarse **el precio en PAYG de un crédito**, que es el dato que haría falta para cotizar el coste marginal del tramo pagado. Pero el dato de estructura que este átomo anticipaba queda confirmado y ampliado: **el captcha desaparece como partida del modelo de coste y se reabsorbe en el precio del tráfico**, y además ese tráfico tiene ahora un tramo gratuito y recurrente. La otra confirmación: el free tier mantiene la **ausencia de KYC** — el acceso a Web Unlocker por créditos gratuitos no exige el proceso de verificación que este átomo describe para las redes Residential y Mobile ([[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]). Ver [[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]] y [[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]].
