---
id: 2026-1026-stealth-instalacion-en-tres-paquetes-y-uso-como-plugin
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]]", "[[2026-1026-puppeteer-extra-prueba-de-un-paquete-local-como-lo-veria-el-registry]]"]
---

## Claim
El README del plugin da la instalación en dos bloques: `yarn add puppeteer-extra-plugin-stealth` (o `npm install puppeteer-extra-plugin-stealth`) y, "if this is your first puppeteer-extra plugin", `yarn add puppeteer puppeteer-extra puppeteer-extra-plugin-stealth` (o el equivalente npm). El uso es **un `use()` sobre el paquete `puppeteer-extra`**: `const puppeteer = require('puppeteer-extra')`, `const StealthPlugin = require('puppeteer-extra-plugin-stealth')`, `puppeteer.use(StealthPlugin())`, y luego `puppeteer.launch({ headless: true })` como siempre —el README lo describe como "a drop-in replacement for puppeteer, it augments the installed puppeteer with plugin functionality"—. El ejemplo navega a `https://bot.sannysoft.com`, espera 5000 ms y guarda una captura `fullPage` en `testresult.png`. La variante TypeScript es `import puppeteer from 'puppeteer-extra'` + `import StealthPlugin from 'puppeteer-extra-plugin-stealth'`, con `.use(StealthPlugin()).launch({ headless: true })` encadenado.

## Why It Matters
Fija el **modelo de consumo** de esta capa de elusión, que el vault no tenía a nivel de paquete: son **tres paquetes con nombre** (`puppeteer`, `puppeteer-extra`, `puppeteer-extra-plugin-stealth`), no un repositorio que se clona. El contraste con el otro extremo del corpus es exacto: en `verssache/chatgpt-creator` la única forma de consumirlo es `git clone` + `go run` desde `main`, **sin control de versión** ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]); aquí hay una instalación con tres dependencias declaradas y un punto de extensión explícito (`use()`), es decir, una **cadena de dependencias versionable y auditable**.
Y hay un dato operativo que la captura del monorepo no daba: el plugin **se autovalidó contra un banco de pruebas público** —`bot.sannysoft.com`— que es el mismo tipo de detector que el vault ya tenía registrado por otra vía como el "banco de pruebas público" del sector ([[2026-1026-puppeteer-extra-catalogo-de-plugins-numerados-en-la-captura]], [[2026-1026-puppeteer-extra-prueba-de-un-paquete-local-como-lo-veria-el-registry]]). Es decir, el propio plugin trae escrito en su ejemplo de uso **el procedimiento de medición de su eficacia**, lo que es raro y útil: la forma de evaluar esta pieza es ejecutarla contra un detector, no leer una promesa.

Nota de verificación: los bloques de código son transcripción literal del README. La captura **no** publica las versiones resueltas de `puppeteer` ni de `puppeteer-extra` que la instalación arrastraría, ni la versión de Node.
