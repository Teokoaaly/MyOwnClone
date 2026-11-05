---
id: 2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]"]
---

## Claim
El commit de publicación de marzo de 2023 enumera seis paquetes con sus versiones, y entre ellos aparecen **dos distintos** para la misma función aparente: **`extract-stealth-evasions@2.7.3`** y, en el badge de descargas, **`puppeteer-extra-plugin-stealth`** (sin versión en la captura). Además, la sección "Development flow" del README incluye un comando que solo tiene sentido si las evasions son unidades testeables por separado: `cd packages/puppeteer-extra-plugin-stealth` y luego `yarn ava -v ./evasions/user-agent-override/index.test.js` — es decir, **cada evasión es un archivo con su propio test**, y la suite se puede lanzar sobre una evasión concreta.

## Why It Matters
La granularidad es la observación: **las evasions no son un bloque monolítico, son unidades con nombre, con ruta y con test propio**. Eso significa que una evasión concreta —aquí la de user-agent override— se puede copiar, versionar, probar y reemplazar de forma independiente del resto. Es la diferencia entre "un plugin de stealth" y "un catálogo de evasions granulares".
Y eso tiene una consecuencia directa sobre el modelo de coste del thread. El vault sostiene que, en un flujo de alta contra OpenAI, **la capa dominante no es una compra sino una construcción**: huella TLS, token sentinel, cabeceras de traza Datadog ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]], [[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]).

## [FRICTION]
> [[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]] afirma que "cambiar de IP no basta si el cliente HTTP sigue siendo el mismo" y que el coste real de un alta a escala no es solo el del proxy, sino el de **construir o untruear un cliente que no se parezca a Go por defecto** —es decir, la huella del cliente "no se compra en ninguna parte" ([[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]).
> Este átomo presiona esa afirmación en un punto de capa: existe un framework MIT que publica **las evasions como piezas granulares y testeadas**, incluida la de user-agent override. Si esa granularidad cubre señales equivalentes, entonces "la huella no se compra" es **una afirmación sobre un nivel concreto** (el transporte HTTP y la instrumentación del cliente, donde el bot Go sí construye a mano) y **no sobre el nivel del navegador**, donde hay commodity publicada.
> Ambas no pueden ser completamente correctas a la vez: o la señal de detección hay que construirla siempre, o hay al menos un nivel en el que es un paquete. Marcado para juicio humano, no auto-resuelto: **la captura no enumera qué evasions existen** —solo la existencia del sub-paquete `extract-stealth-evasions` y de un test de `user-agent-override`— y no publica su contenido ni su cobertura de señales. La comparación capa a capa queda abierta.

Nota de verificación: nombres, versiones y rutas son transcripción literal del commit de publicación, del badge de npm y del bloque de comandos del README. La captura **no** describe qué hace ninguna evasión.


## Nota de extensión 2026-10-26
La captura del 2026-10-25 del **README del propio paquete** `packages/puppeteer-extra-plugin-stealth` (2081 palabras) **convierte la inferencia de este átomo en observación directa**. Este átomo afirmaba, a partir de la captura del monorepo, que "cada evasión es un archivo con su propio test" y que el sub-paquete `extract-stealth-evasions` existe como ciclo de versión aparte. La captura del paquete **nombra las evasions**.

El changelog del README enumera **once evasions con nombre**: `user-agent-override`, `navigator.vendor`, `navigator.webdriver`, `iframe.contentWindow`, `accept-language`, `media.codecs`, `chrome.runtime`, `navigator.plugins`, `webgl.vendor`, `window.outerdimensions` y `defaultArgs` —y declara **eliminadas** `user-agent` y `accept-language` en `v2.4.7` ("now obsolete"). La sección "Modularity" añade el dato que faltaba: **cada evasión es un plugin autónomo de `puppeteer-extra` con ruta de import propia**, y se puede consumir sin el paquete agregador con `puppeteer.use(require('puppeteer-extra-plugin-stealth/evasions/console.debug')())`. El mecanismo de carga es selectivo: "uses `puppeteer-extra`'s dependency system to only require code mods for evasions that have been enabled" ([[2026-1026-stealth-modularidad-por-carga-selectiva-y-require-directo-de-una-evasion]]).

**La extensión es de alcance, y corrige un matiz que este átomo dejaba abierto.** La granularidad por evasión es real, pero **la granularidad no equivale a cobertura**: la lista incluye `webgl.vendor` —que es la *etiqueta* del proveedor WebGL, no la huella de render— y **no incluye `canvas` en ningún punto**, precisamente la señal que rebrowser enumera como faltante junto a WebGL ([[2026-1026-stealth-cobertura-de-canvas-ausente-en-el-changelog-de-evasions]]). Y el changelog se declara truncado ("Older changelog"), de modo que la lista es **un extracto, no un inventario**. Lo que este átomo debe escribir, entonces, es: *las evasions son unidades con nombre, ruta, test propio y versión; el conjunto concreto de nombres está publicado en el changelog y no cubre canvas*. La afirmación "las evasions son granulares" se mantiene; la de "las evasions cubren las señales relevantes" no se puede hacer.
