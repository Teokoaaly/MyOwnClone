---
id: 2026-1026-stealth-evasions-nombradas-en-el-changelog-del-plugin
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]", "[[2026-1026-puppeteer-extra-readme-de-monorepo-sin-instalacion-ni-catalogo-de-plugins]]", "[[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]"]
---

## Claim
El changelog del README nombra **con qué señales trabaja la evasión**, aunque el propio README declara que solo publica un **"Older changelog"** (hasta `v2.4.7`) y que las actualizaciones nuevas hay que buscarlas en el canal `#announcements` de su Discord. Las evasiones nombradas a lo largo de `v2.4.7`, `v2.4.2/v2.4.1`, `v2.4.0` y `v2.1.2` son: **`user-agent-override`**, **`navigator.vendor`**, **`navigator.webdriver`**, **`iframe.contentWindow`**, **`accept-language`**, **`media.codecs`**, **`chrome.runtime`**, **`navigator.plugins`**, **`webgl.vendor`** y **`window.outerdimensions`**; más **`defaultArgs`**, que solo consta por el mensaje del commit de `index.js` ("feat(plugin-stealth): Add defaultArgs evasion (#579)"). El changelog declara además **eliminadas** dos: "`Removed: `user-agent`, `accept-language` (now obsolete)".

## Why It Matters
Es la **primera enumeración con nombre de la superficie de evasión del sector que el vault tiene**, y de ella se lee la estrategia: casi todas las señales son **propiedades de objetos del navegador que un script de la página puede leer** (`navigator.*`, `window.outerWidth`, `chrome.runtime`, `iframe.contentWindow`), más dos excepciones de nivel distinto —`media.codecs` y `webgl.vendor`, que son señales de **render/hardware**—. La lista es además la que permite **auditar qué no se cubre**: el changelog nombra `webgl.vendor` y `media.codecs` pero **no nombra canvas** en ningún punto.
Eso conecta directamente con lo que el vault ya tenía medido en la fuente de rebrowser: que la elusión por parche no basta y hacen falta **canvas y WebGL** ([[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]]). El vault tenía los dos datos —la lista de señales del plugin y la lista de señales que faltan— pero **no podía cruzarlos**, porque la captura del monorepo no enumeraba ninguna evasión ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]).
La consecuencia de método es clara: **el changelog no es el catálogo**. Es un extracto parcial —el README remite al directorio `evasions` como "up to date list"—, de modo que el vault debe registrar la lista como *evasiones conocidas por el changelog truncado*, no como el conjunto de evasiones del plugin ([[2026-1026-puppeteer-extra-readme-de-monorepo-sin-instalacion-ni-catalogo-de-plugins]]).

Nota de verificación: los nombres son transcripción literal de las entradas de changelog del README. La captura **no** incluye el directorio `evasions/`, ni su contenido, ni la lista completa de evasions disponibles ([[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]).
