=== EXTEND 2-atoms/2026-1024-brightdata-cuatro-tipos-de-red-y-solo-tres-pestanas-de-precio.md
## Nota de extensión 2026-10-26
La página de introducción de la documentación (`docs.brightdata.com/introduction`) reinforce la inconsistencia que este átomo ya registraba, y la desplaza un eje. Su bloque **"Proxy networks"** declara **"Five network types for routing traffic at scale"** y lista **cinco** entradas: *Residential* ("400M+ real-user IPs"), *Datacenter* ("Fast, low-cost IPs"), *ISP* ("Static residential-grade IPs"), *Proxy Manager* ("Open-source proxy routing") y *Browser Extension* ("Proxies in Chrome").

Las dos últimas no son redes de IP sino **herramientas de cliente**, y **Mobile** —que sí es una red de IP según el FAQ registrado en este átomo— no aparece en la lista. De ahí la lectura que propone [[2026-1026-brightdata-cinco-tipos-de-red-en-docs-contra-cuatro-en-faq]]: el «5» no es un quinto tipo de red, es un conteo de **entidades de catálogo** (3 redes + 2 herramientas) mientras el FAQ cuenta **redes** (4, con móvil). La cifra "400M+ real-user IPs" que aparece aquí es además la que ya figura en [[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]], y esta página no añade ni el desglose por 195 países ni el targeting gratuito, es decir, la landing no sustituye a la ficha de producto.

Valor para el átomo: la taxonomía de 4 redes del FAQ sigue siendo la correcta para el modelo de coste; el "cinco" de la docs es un artefacto de navegación y no una quinta red cotizable. El recuento de 3 pestañas de precio sin móvil continúa sin resolver con esta fuente.
=== END

=== EXTEND 2-atoms/2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc.md
## Nota de extensión 2026-10-26
La introducción de la documentación sitúa a Web Unlocker dentro de un **catálogo de APIs de extracción** mucho más amplio que el que este átomo recogía. La sección "Data extraction" lista **Web Unlocker API, SERP API, Web Scraper API, Scraper Studio y Browser API**, y la sección "Proxy networks" ofrece las tres redes. Es decir: **Web Unlocker deja de ser "la alternativa al proxy crudo" y pasa a ser una de cinco APIs de datos con igual footing comercial**, lo que refuerza la hipótesis del átomo de que el CAPTCHA se reabsorbe en un recargo del acceso en lugar de ser una línea del modelo de coste del vault ([[2026-1024-dataimpulse-precios-de-entrada-por-tipo-de-proxy]]).

Dos precisiones que esta fuente añade y que el átomo no tenía:
1. **La afirmación de "no requiere KYC" no se repite en la landing** — el texto exacto "Using Web Unlocker does not require going through the KYC process" sigue siendo solo de la página de precios. La documentación de intro no lo confirma, no lo contradice.
2. **Browser API aparece como "Remote browsers for automation"**, es decir, la externalización de la huella y de la navegación, que es exactamente el producto que 2Captcha había lanado en su giro hacia scraping y agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]) y que Decodo que más tarde apuntó como integración de navegador incluida en cada plan ([[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]). Ver [[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]].

Lo que sigue sin publicarse: el precio de Web Unlocker, su unidad, y si las cinco APIs comparten o no el mismo contador de consumo. La captura del free tier sugiere que comparten pool de créditos, lo que cerraría el círculo.
=== END

=== EXTEND 2-atoms/2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes.md
## Nota de extensión 2026-10-26
La documentación de Bright Data documenta el **mismo giro de categoría** desde el lado del proveedor de red, y añade el dato que faltaba en este átomo: **el MCP de Bright Data está documentado con comandos concretos por cliente** —Claude Code, Cursor, Codex CLI y el propio Bright Data CLI— lo que lo convierte en una **superficie de acceso a web en vivo para agentes** (`"Bright Data MCP — Live web access for agents"`). Ver [[2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente]].

El elemento nuevo y más relevante para el vault es que Bright Data publica además **`/llms.txt`**, *"the complete documentation index"*, con la instrucción *"Use this file to discover all available pages before exploring further"*, y un panel **"You're an agent? Start here"**. Es decir, el proveedor no solo expone datos vía MCP: **expone su propia documentación a los agentes**, lo que convierte a la docs en un recurso consultable por la misma maquinaria que consume los datos. Ver [[2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes]].

La comparación de riesgo que este átomo abrió se mantiene y se refuerza: [[2026-1023-ai-security-tools-mcp-as-superficie-de-ataque]] describe el MCP como vector; aquí hay **dos proveedores de elusión** (2Captcha y Bright Data) publicando servidores MCP para agentes, lo que confirma que el vector ya tiene oferta comercial de primer nivel y no es un artefacto experimental. Y hay un dato de coste que este átomo no tenía: el MCP de Bright Data **no crea cuota nueva**, consume el pool de créditos compartido porque el servidor MCP corre sobre Web Unlocker ([[2026-1026-brightdata-mcp-consume-el-mismo-pool-de-creditos]]), de modo que la decisión "MCP o HTTP" es de ergonomía y no de precio.
=== END
