---
id: 2026-1026-puppeteer-extra-lerna-yarn-workspaces-ava-standard-y-jsdoc-para-docs
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]"]
---

## Claim
El README describe la cadena de herramientas del monorepo en una frase: "We use a [monorepo](…) powered by [Lerna](…) (and yarn workspaces), [ava](https://github.com/avajs/ava) for testing, the [standard](https://standardjs.com/) style for linting and [JSDoc](http://usejsdoc.org/about-getting-started.html) heavily to auto-generate markdown [documentation](https://github.com/documentationjs/documentation) based on code." Es decir: Lerna + yarn workspaces para los paquetes, **ava** como runner de tests, **standard** como estilo de linting y **JSDoc + documentation.js** para generar la documentación en markdown **a partir del código**.

## Why It Matters
Tres consecuencias para el vault. La primera es de documentación: **la documentación de cada paquete es un artefacto generado**, no un texto mantenido a mano — y por eso el README raíz puede remitir a "the `puppeteer-extra` package" sin duplicar nada. Es un patrón de mantenibilidad que el corpus del vault no tenía para código de automatización.
La segunda es de estructura: el vault tiene un dato propio y **contrario** para el producto propio — MyOwnClone **no** es un monorepo, son dos bases de código con procesos de arranque separados ([[2026-1022-myownclone-dos-repos-flask-nextjs]])—, mientras que el framework de referencia del corpus mantiene N paquetes en un solo árbol con `yarn bootstrap` y `yarn lerna link`.
La tercera es de despliegue: el único proyecto del corpus de evasión con versión mantenida era un despliegue Java 17 en PaaS sin servidor ([[2026-1023-midjourney-proxy-despliegue-java17-y-paas-sin-servidor]]); aquí el equivalente es un monorepo JS/TS publicado como paquetes npm.
Nota de verificación: la captura no publica la versión de Node, ni la de Puppeteer soportada, ni el contenido de `package.json` (solo el mensaje de su último commit), ni la matriz de versiones.
