---
id: 2026-1026-puppeteer-extra-readme-de-monorepo-sin-instalacion-ni-catalogo-de-plugins
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]"]
---

## Claim
El README de `berstend/puppeteer-extra` (7.4k estrellas, capturado el 2026-10-25) se declara "the monorepo for `puppeteer-extra`, a modular plugin framework for `puppeteer`" y remite la documentación principal al paquete `packages/puppeteer-extra` ("For the main documentation, please head over to the `puppeteer-extra` package"). El texto capturado **no contiene instrucciones de instalación como dependencia de consumo** (ni `npm install` ni `yarn add puppeteer-extra`) **ni un catálogo de plugins**: los únicos comandos que da son de desarrollo (`yarn`, `yarn bootstrap`, `yarn build`) y de publicación.

## Why It Matters
Fija el **alcance de la fuente** para el vault: esta captura sirve para la arquitectura del repositorio, el flujo de contribución y publicación y los metadatos del proyecto, y **no** para enumerar qué plugins incluye ni cómo se instala el framework como dependencia. Es la diferencia entre "el repo existe y publica paquetes" y "el repo documenta el producto".
El contraste con el resto del corpus de repos es exacto: en `verssache/chatgpt-creator` el README **es** la documentación del producto —features, flujo de nueve pasos, ejemplo de salida— porque el proyecto es un script y no un framework ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]), y en `gptGrok2api` el README es la única especificación de su protocolo de registro sin navegador ([[2026-1024-gptgrok2api-registro-protocolo-sin-navegador-y-captcha-solver-integrado]]). Aquí el README es de **mantenimiento del monorepo**: quien quiera saber qué hace el framework tiene que ir al README del paquete, que no está capturado.
Nota: la captura es la página del repositorio (README, tabla de archivos, cabecera de commits, topics, metadatos), no la página del paquete `puppeteer-extra` ni la de ningún plugin.
