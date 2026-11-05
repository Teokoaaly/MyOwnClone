---
id: 2026-1026-puppeteer-extra-topics-que-declaran-recaptcha-stealth-y-user-preferences
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1026-capsolver-mcp-y-agentes-como-primera-superficie-comercial]]"]
---

## Claim
Los topics declarados en la cabecera del repositorio son trece: `automation`, `chrome`, `headless-browser`, `headless-chrome`, `lerna`, `monorepo`, `puppeteer`, `puppeteer-extra`, `puppeteer-plugins`, **`recaptcha`**, **`stealth`**, **`user-preferences`**, `yarn-workspaces`. Es decir, **la mitad de los topics son de elusión**, no de automatización genérica: recaptcha, stealth y user-preferences. El pie del README es "💯 Teach puppeteer new tricks through plugins" y enlaza a **`extra.community`**, y la etiqueta de licencia es MIT.

## Why It Matters
Los topics de GitHub son la única clasificación que el propio autor publica sobre su repositorio, y aquí son **una declaración de posicionamiento**: este proyecto no se autodescribe como "automatización de navegador" sino como evasión. `recaptcha` y `stealth` son dos de los tres temas no técnicos, y son exactamente las dos piezas que el thread del vault tenía que comprar o construir —el captcha a céntimos ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]) y la huella del cliente ([[2026-1026-capsolver-mcp-y-agentes-como-primera-superficie-comercial]]).
Eso da una lectura que el vault no tenía y que conviene explicitar: **la elusión de navegador es un mercado con dos economías —una de software abierto con licencia MIT y una de servicios comerciales con SLA—** y ambas se presentan al mismo usuario final. El sector comercial ofrece resolvers y APIs de scraping con integraciones MCP; el sector abierto ofrece plugins con número de versión. Elegir entre ellos no es una cuestión de precio del captcha sino de **qué parte del problema decides construir tú**.
Dato fino: `extra.community` aparece como el destino externo de la documentación del proyecto, es decir, **la documentación se ha movido fuera del repositorio** y el README raíz queda como índice. Es un rasgo de maduración, y también una razón por la que la captura de esta fuente tiene menos contenido de producto del que el nombre del repositorio sugiere.
Nota de verificación: la lista de topics es transcripción literal de la cabecera de la página.


## Nota de extensión 2026-10-26
La captura de `sources/2026-10-25-rebrowser-patches.md` sitúa a `puppeteer-extra-plugin-stealth` en el **origen de la línea técnica**: aparece en "Special thanks" como ***"where it all started"***. Y explica por qué el sector se movió del plugin de inyección al parche del código fuente: el README de rebrowser afirma que ***"the less you manipulate browser internals via JS injections, the better"***, porque hay formas de detectar que objetos internos como `console` y `navigator` han sido afectados por `Proxy` o `Object.defineProperty` — ***"it's always a cat-and-mouse game"***. Añadir al *Why It Matters*: **la inyección de JavaScript para disimular el navegador es en sí misma un vector de detección**, y por eso la ruta de maduración del sector es inyectar → parcheear. Ver [[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]] y [[2026-1026-rebrowser-agradece-cinco-proyectos-que-le-abrieron-el-camino]].
