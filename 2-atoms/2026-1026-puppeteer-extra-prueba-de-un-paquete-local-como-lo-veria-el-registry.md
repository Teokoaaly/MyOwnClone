---
id: 2026-1026-puppeteer-extra-prueba-de-un-paquete-local-como-lo-veria-el-registry
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1026-puppeteer-extra-flujo-de-publicacion-por-lerna-con-npm-y-no-yarn]]"]
---

## Claim
El bloque "Development flow" incluye un procedimiento de una sola línea para **probar un paquete del monorepo desde fuera, tal y como se instalaría desde el registry**: `PACKAGE=puppeteer-extra PACKAGE_DIR=/Users/foo/puppeteer-extra/packages && yarn remove … && yarn --cwd $(echo $PACKAGE_DIR)/$(echo $PACKAGE) pack --filename $(pwd)/$(echo $PACKAGE)-latest.tgz && YARN_CACHE_FOLDER=/tmp/yarn yarn add file:$(pwd)/$(echo $PACKAGE)-latest.tgz && rm -rf /tmp/yarn`. Es decir: **empaquetar con `yarn pack` a un `.tgz` e instalarlo como fichero local**, en lugar de enlazar el workspace.

## Why It Matters
Es un detalle de disciplina de release que no aparece en ningún otro repositorio del corpus y que explica la separación entre "el código funciona en el monorepo" y "el paquete funciona para quien lo instala". Un workspace enlazado puede resolver dependencias que el paquete publicado no resuelve: **la prueba del `.tgz` es la única que verifica el artefacto real**, no la carpeta de trabajo. Para un proyecto que publica 559 tags con versionado independiente por paquete ([[2026-1026-puppeteer-extra-flujo-de-publicacion-por-lerna-con-npm-y-no-yarn]]), esa comprobación es la que sostiene que el versionado significa algo.
El contraste con el resto del corpus de herramientas de evasión es instructivo por lo que falta: en `chatgpt-creator` no hay paquete, ni tarball, ni procedimiento de publicación —solo `git clone` + `go run` desde `main`, sin versionado ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]). Y el otro extremo del corpus es Midjourney-Proxy: 5,4k estrellas y un proceso de release congelado desde junio de 2024 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]). La diferencia operativa entre estas herramientas y la de este repositorio no es de potencia sino de **reproducibilidad**: una se puede fijar por versión y la otra no.
Nota de verificación: el comando está transcrito literalmente del README, con una ruta de ejemplo local (`/Users/foo/…`). La captura **no** publica el `files` de `package.json`, ni qué se incluye en el tarball, ni el tamaño de los paquetes.
