---
id: 2026-1026-stealth-modularidad-por-carga-selectiva-y-require-directo-de-una-evasion
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]", "[[2026-1026-puppeteer-extra-lerna-yarn-workspaces-ava-standard-y-jsdoc-para-docs]]", "[[2026-1026-stealth-api-de-evasions-como-sets-de-nombres-y-seleccion-por-constructor]]"]
---

## Claim
La sección "Modularity" declara dos cosas. Primera: "This plugin uses `puppeteer-extra`'s dependency system to **only require code mods for evasions that have been enabled**, to keep things modular and efficient". Segunda: el plugin `stealth` "is a convenience wrapper that requires multiple evasion techniques automatically and comes with defaults", y se puede **saltar el módulo principal** requiriendo una evasión concreta, porque "they're standalone `puppeteer-extra` plugins": `puppeteer.use(require('puppeteer-extra-plugin-stealth/evasions/console.debug')())`. Para contribuir con una evasión nueva, el README remite a la plantilla `evasions/_template`.

## Why It Matters
Da la **granularidad real** de la que la captura del monorepo solo tenía indicios. Aquella fuente decía que cada evasión es un archivo con su propio test; esta dice además que **cada evasión es un plugin autónomo con su propia ruta de import** (`puppeteer-extra-plugin-stealth/evasions/console.debug`). Es decir: la evasión no es un módulo interno, es **una unidad distribuible con nombre propio** que se puede consumir sin el paquete agregador.
Eso explica y precisa el dato del sub-paquete `extract-stealth-evasions` que el vault ya tenía ([[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]): el modelo es **el inverso del monolitismo**, y el mecanismo es la carga selectiva —solo se carga el código de las evasions habilitadas, lo que el README justifica como "modular and efficient".
Para el vault, esto da una **regla de auditoría de dependencias** que es nueva: en esta capa, **la superficie de código que se ejecuta es proporcional al subconjunto de evasiones elegido**, y por tanto una revisión de seguridad o una auditoría de un pipeline tiene que mirar **qué evasiones están habilitadas**, no solo qué paquete está instalado. Es la diferencia entre auditar "tenemos el plugin de stealth" y auditar "tenemos enabledEvasions = {webgl.vendor, navigator.webdriver}". El mecanismo de la documentación generada desde el código (JSDoc + documentation.js) es coherente con que cada unidad sea documentable por separado ([[2026-1026-puppeteer-extra-lerna-yarn-workspaces-ava-standard-y-jsdoc-para-docs]]).

Nota de verificación: las citas son literales de la sección "Modularity". La captura **no** publica el contenido de la plantilla `evasions/_template` ni la implementación del sistema de dependencias de `puppeteer-extra`.
