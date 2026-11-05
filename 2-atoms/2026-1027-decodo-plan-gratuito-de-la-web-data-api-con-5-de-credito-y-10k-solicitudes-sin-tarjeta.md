---
id: 2026-1027-decodo-plan-gratuito-de-la-web-data-api-con-5-de-credito-y-10k-solicitudes-sin-tarjeta
type: atom
certainty: solid
sources: [sources/2026-10-26-decodo-smartproxy-home.md, sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]]", "[[2026-1026-brightdata-5000-creditos-gratis-al-mes-para-cuentas-nuevas]]", "[[2026-1026-decodo-prueba-de-3-dias-con-100-mb-y-autoactivacion-del-plan]]", "[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]"]
---

## Claim
Decodo tiene **dos Chevron de prueba distintos**, y el segundo no es el primero. Para los proxies: una **prueba de 3 días con 100 MB**. Para la Web Data API: un **plan gratuito permanente** con **"$5 in testing credits (up to 10k requests) with no credit card required to get started"**. La home lo repite en dos sitios más: el FAQ ("You can start using Web Data API with a free starter plan without a credit card. Sign up, test your requests, and upgrade when you need more capacity") y un banner "**Test drive Web Data API with up to 10K free monthly requests**" con los pies "**No credit card required · Cancel anytime**".

En la página de precios de la API, ese mismo plan aparece como el **primer escalón de la escalera de ocho**: **10 req/s, $0/mes, "Up to 5K crawls or 10K pages scraped"** — es decir, los "10k requests" del plan gratuito equivalen **exactamente a las 10K páginas** (o 5K crawls) del plan de $0.

## Why It Matters
Es la **tercera variante de free tier del corpus de acceso a web**, y las tres no son comparables:

- Bright Data da **5.000 créditos** al mes, sin tarjeta, y esos créditos son su **unidad común entre todos los productos** ([[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]], [[2026-1026-brightdata-5000-creditos-gratis-al-mes-para-cuentas-nuevas]]).
- Decodo da **$5 en créditos de prueba, hasta 10k requests**, sin tarjeta — pero **los créditos son una unidad de la API, no del proxy**: es un free tier **de la línea de scraping**, no de la línea de proxy.
- El de proxies de Decodo es un **trial de 3 días con 100 MB** que además **auto-activa el plan de pago** ([[2026-1026-decodo-prueba-de-3-dias-con-100-mb-y-autoactivacion-del-plan]]), lo que además **anula la garantía de 14 días**.

El valor operativo para el vault es que **el plan gratuito de la API es exactamente 10K páginas**: son 5.000 crawls completos de un sitio pequeño, o 10.000 páginas individuales. Con la regla del vault de que una verificación consume **sesiones**, no bytes ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]), 10K páginas alcanzan para **medir la calidad real del scrape en el destino real** — que es justo lo que la prueba de 100 MB de proxy no permite. Es la única muestra gratuita del corpus que **mide la operación completa** (scraping + proxy + sin tarjeta) y no solo la conectividad.

El matiz que hay que cuidar: "10K free monthly requests" (banner) y "$5 in testing credits (up to 10k requests)" (FAQ) **no son necesariamente la misma bolsa**. Si los $5 de crédito se gastan antes, ¿el banner sigue sirviendo? La captura no lo aclara, y por eso el valor de 10K/mes es una lectura optimista, no un hecho.

## Nota de verificación
Cifras y frases transcritas literalmente de las dos fuentes. La equivalencia entre los "10k requests" del FAQ y las "10K pages" del plan de $0 es una **lectura del vault** apoyada en la coincidencia numérica; la captura no declara la conversión. La captura **no** publica: si el free tier es mensual o único, qué ocurre al agotar el crédito, ni si el plan gratuito tiene límite de req/s distinto del publicado (10 req/s).
