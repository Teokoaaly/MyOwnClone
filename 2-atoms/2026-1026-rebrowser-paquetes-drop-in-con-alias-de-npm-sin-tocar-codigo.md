---
id: 2026-1026-rebrowser-paquetes-drop-in-con-alias-de-npm-sin-tocar-codigo
type: atom
certainty: solid
sources: [sources/2026-10-25-rebrowser-patches.md]
links: ["[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]", "[[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]"]
---

## Claim
El repo publica **paquetes sustitutos que son exactamente el original con los parches aplicados encima**: *"These packages have simply applied rebrowser-patches on top of the original code, nothing more."* Son **`rebrowser-puppeteer`** y **`rebrowser-puppeteer-core`** (npm), **`rebrowser-playwright`** y **`rebrowser-playwright-core`** (npm, Node.js) y **`rebrowser-playwright`** (PyPI, Python). El mecanismo de integración más barato documentado es el **alias de npm**: en `package.json`, sustituir `"puppeteer": "^23.3.1"` por `"puppeteer": "npm:rebrowser-puppeteer@^23.3.1"` (y el `-core` equivalente) y ejecutar `npm install`, **sin cambiar ni una línea del código de automatización**. La vía alternativa es renombrar las dependencias en `package.json` y hacer find-and-replace de `puppeteer`/`puppeteer-core` en los scripts. El README declara que el objetivo es mantener esos paquetes "with the latest versions", centrándose "mainly on fresh versions", y deja caer que quien siga en una versión antigua "might be a good time to upgrade" porque la API "is quite stable over time".

## Why It Matters
Es la **tercera forma de consumir el mismo producto** que el vault ya tiene registrada para el captcha: 2Captcha ya integraba su API en "4500+ software" con solo teclear una key ([[2026-1024-2captcha-integrado-en-4500-software-con-api-key]]). Aquí la integración es **a nivel de dependencia**, con una propiedad que el vault no tenía: **el nombre del paquete en `package.json` cambia, el código no**. Es decir, la adopción de la evasión es un cambio de una línea de manifiesto, no de una línea de código.

Lo relevante para el thesis del thread es que **el producto abierto tiene su equivalente empaquetado y versionado**, y ese empaquetado lo produce la misma empresa que vende la nube de navegadores. Es el mismo patrón que el proxy de imagen: **núcleo abierto en GitHub + valor comercial en la operación** ([[2026-1023-midjourney-proxy-oferta-comercial-de-api-no-oficial]]). Aquí la monetización no está en un canal privado de WeChat sino en una suscripción de navegador en la nube.

Y hay una observación de coste que conviene no perder: **el parche es gratis, pero el paquete drop-in tiene una dependencia de versión**. El README declara el soporte de versiones probadas (Puppeteer 24.8.1, Playwright 1.52.0) y advierte que los parches se rompen cuando cambia el código de la librería. La adopción "gratuita" en realidad es **una suscripción de mantenimiento** disfrazada de dependencia.
