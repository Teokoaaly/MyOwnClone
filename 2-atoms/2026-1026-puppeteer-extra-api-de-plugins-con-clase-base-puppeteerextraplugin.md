---
id: 2026-1026-puppeteer-extra-api-de-plugins-con-clase-base-puppeterextraplugin
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]"]
---

## Claim
La sección "Contributing" describe la API de extensión en tres frases: "PRs and new plugins are welcome! The plugin API for `puppeteer-extra` is clean and fun to use. Have a look the [`PuppeteerExtraPlugin`](https://github.com/berstend/puppeteer-extra/blob/master/packages/puppeteer-extra-plugin) base class documentation to get going and check out the existing plugins (minimal example is the [anonymize-ua](https://github.com/berstend/puppeteer-extra/blob/master/packages/puppeteer-extra-plugin-anonymize-ua/index.js) plugin) for reference." Es decir: la extensión se hace **heredando de una clase base publicada** (`PuppeteerExtraPlugin`, en el paquete `packages/puppeteer-extra-plugin`), y el README señala un plugin mínimo de ejemplo.

## Why It Matters
El vault no tenía ninguna referencia canónica de **qué es un plugin de navegador** ni de cómo se extiende un framework de automatización. Aquí queda establecido: la superficie de extensión es una clase base con documentación propia, no un parche del binario ni un script suelto.
Eso separa este modelo del corpus de fábricas de cuentas: en `verssache/chatgpt-creator` la única forma de consumir el proyecto es `git clone` + `go run` desde `main`, **sin control de versión** ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]), y en `gptGrok2api` el protocolo de registro está descrito en prosa de README porque no hay nada que extender ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]). Un framework con clase base publicada significa que **la evolución del producto es código con versionado y con frontera de API**, no un monolito que se copia.
Nota de verificación: la captura no incluye el contenido de la clase base ni su API; solo el nombre, la ruta del paquete y la afirmación de que la API es "clean and fun to use", que es una valoración del autor.
