---
id: 2026-1027-2captcha-mcp-camoufox-cuesta-mas-que-el-captcha-que-resuelve
type: atom
certainty: tentative
sources: [sources/2026-10-26-2captcha-pricing-mcp.md]
links: ["[[2026-1027-2captcha-mcp-seis-modos-con-precios-por-llamada]]", "[[2026-1027-2captcha-catalogo-completo-de-48-filas-de-captcha]]", "[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]"]
---
## Claim
Cruzando la tabla del MCP con el catálogo de captchas del mismo proveedor: una llamada en modo **Camoufox** cuesta **$0.0048**, mientras que el peldaño habitual de un captcha ($1.45 por 1.000) equivale a **$0.00145** por captcha. Es decir, **una sola llamada de MCP con navegador antisimulación cuesta ~3,3 veces más que resolver el captcha que la habilita**. En el otro extremo, el modo **API Tier** ($0.0001 por llamada) es ~**14,5 veces más barato** que un captcha, y **Render** ($0.0016) queda apenas por encima del captcha.

## Why It Matters
El vault venía registrando que el captcha era **la partida más barata** de toda la cadena de elusión (correo ≪ captcha ≪ proxy ≪ SMS). Estos precios **reordenan esa tabla** en el extremo de la derecha: la parte cara ya no es "resolver el control", sino **navegar por debajo del control**. Un pipeline que usa el modo Camoufox paga, por llamada, más por la infraestructura de evasión que por el desafío que la habilita.

La consecuencia operativa es un **arbitraje de modo, no de volumen**: si el modo barato (API Tier) basta para el destino, el coste marginal del scraping con MCP es de **una fracción de centavo** y el problema de presupuesto desaparece; si hace falta Camoufox, el scraping con MCP es un producto **de lujo comparado con el captcha** y entra en la misma categoría de decisión que un proxy residencial de $50/GB. Es la primera vez que el vault puede **elegir deliberadamente** el nivel de sigilo en función de un precio explícito, porque el proveedor publica el multiplicador (1 / 1,5 / 16 / 48 créditos).

Y hay una lectura de estrategia del proveedor: **el captcha se ha convertido en el gancho de un catálogo de infraestructura**. 48 captchas a $1.45/1000 es el producto de entrada; el catálogo de agentes monetiza el mismo acceso a un precio que varía en **48×** según el nivel de sigilo. Ver [[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]].

Nota de verificación: el ratio depende de **qué incluye una "llamada"** (¿una navegación? ¿un render completo? ¿un reintento?) y de que el captcha comparable sea el peldaño de $1.45 y no otro; la captura **no** publica esa definición ni el precio del proxy que acompañaría a la llamada. La aritmética es del vault sobre cifras literales de dos capturas distintas.

## [FRICTION]
> [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]] usa el rango **$0.5 — $2.99 por 1000** como "el precio de referencia del mercado de elusión anti-bot" y sostiene que es una "comodity con precio de mercado".
> Este átomo presiona esa cifra en un punto verificable: **el mismo proveedor ya tiene una capa más barata que el captcha**. El Scraper API está a **$0.30 por 1.000 requests** —por debajo del suelo de $0.5 del catálogo de captchas— y el MCP en modo API Tier a **$0.10 por 1.000 llamadas**. Si la unidad de "$0.5–$2.99 por 1000" sirve de referencia de mercado, o el catálogo de captchas ya no es el piso de la elusión, o el rango solo describe una de las cinco líneas de precio que el proveedor publica hoy.
> Marcado para juicio humano, no auto-resuelto: las unidades no son homólogas (captcha resuelto vs request vs llamada de agente), y la comparación depende de qué se considera una unidad de elusión equivalente.
