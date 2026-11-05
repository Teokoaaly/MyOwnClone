---
id: 2026-1026-stealth-user-agent-override-y-navigator-vendor-como-capa-de-identidad
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]", "[[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]]", "[[2026-1026-stealth-accept-language-en-mayusculas-porque-setextrahttpheaders-es-detectable]]", "[[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]"]
---

## Claim
El changelog describe **la identidad declarada del navegador como una pieza configurable, en tres ejes separados**. `v2.4.7` añade `user-agent-override` —"Used to set a stealthy UA string, language & platform" (PR #104, kudos a @Niek)— y `navigator.vendor` —"Makes it possible to optionally override navigator.vendor" (PR #110, mismo autor)—, y declara **obsoletas y eliminadas** las evasions antiguas `user-agent` y `accept-language`. `v2.4.2`/`v2.4.1` añade que `accept-language` "it's now possible to set a custom locale if needed". `v2.1.2` añade `webgl.vendor` con la explicación del valor por defecto —"is otherwise set to 'Google' in headless"— y `window.outerdimensions` para "fix missing window.outerWidth/outerHeight and viewport".

## Why It Matters
El vault tiene registrado que el plugin `anonymize-ua` es el **ejemplo mínimo** de la API de plugins del ecosistema ([[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]). Esta captura da por qué ese ejemplo existe: **la identidad del cliente es la primera y más básica evasión, y hay que poder fijarla por eje** —idioma, plataforma, `vendor`, locale— porque cada uno de esos valores es un `tell` en sí mismo.
Y aporta un dato que el vault no tenía, y que es una observación de diseño más que de técnica: **los valores por defecto de headless no son valores neutros, son valores de marca**. `webgl.vendor` sale como `"Google"` y `navigator.plugins` no emula nada —"we fully emulate plugins/mimetypes in headless now" (`v2.1.2`)—, es decir, el navegador sin headless **delata su condición por defecto**, y por eso hay que taparlo. La lección general: **en el navegador headless la señal por defecto no es "no hay dato", es "hay el dato de otro producto"**.
Eso tiene una consecuencia operativa para el vault: **la identidad del cliente se puede fijar por configuración**, y eso es una partida de coste distinto de la huella de red. El vault ya midió que el `Accept-Language` se puede escribir mal y delatar automatización ([[2026-1026-stealth-accept-language-en-mayusculas-porque-setextrahttpheaders-es-detectable]]); aquí está la pieza que lo hace configurable en tres ejes. Y encaja con el aviso del otro sector del vault: **"proper user-agent and fingerprints (canvas, WebGL)"** son partidas que hay que tener aparte, porque **el user-agent se puede fijar gratis y la huella de render no** ([[2026-1026-rebrowser-el-fix-solo-no-basta-y-hacen-falta-canvas-y-webgl]]).

Nota de verificación: las citas son literales del changelog. La captura **no** publica los valores concretos que toma la evasión por defecto, ni la documentación de directorio de `user-agent-override`.
