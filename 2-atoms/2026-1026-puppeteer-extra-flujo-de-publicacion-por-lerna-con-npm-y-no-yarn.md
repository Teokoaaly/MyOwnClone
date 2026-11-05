---
id: 2026-1026-puppeteer-extra-flujo-de-publicacion-por-lerna-con-npm-y-no-yarn
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]", "[[2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023]]"]
---

## Claim
La sección "Publishing" documenta un flujo de publicación por paquetes, no por repositorio: `npm whoami` primero ("make sure you're signed into npm before publishing"), luego `yarn`, `yarn bootstrap`, `yarn lerna link`, `yarn build`, `yarn test` y **`yarn lerna publish`**, cuyo comentario de tres líneas precisa que "**Will publish all changed packages**", que "**Will ask for new pkg version per package**" y que "**Will updated inter-package dependency versions automatically**". Añade un comentario explícito de fricción operativa: "**yarn publishing is broken so lerna uses npm**", y un paso de reparación posterior ("Fix new dependency version symlinks" con `yarn bootstrap && yarn lerna link`). El commit de publicación de la cabecera es coherente con esto: se titula "Publish" y enumera seis paquetes con versión.

## Why It Matters
Es la explicación de por qué un monorepo de 559 tags produce un resultado que el vault no había visto en ningún otro repo del corpus: **la publicación es por paquete y con versión independiente por paquete**. Cada plugin se versiona por separado y las dependencias inter-paquete se actualizan solas. Eso es exactamente lo que le falta a `verssache/chatgpt-creator`, donde la única forma de consumirlo es `git clone` + `go run` desde `main`, **sin control de versión** ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]).
La comparación de los dos vocabularios de consumo es la que importa para un vault que documenta herramientas de evasión: **"instalar un paquete versionado" y "clonar un script" son dos formas incompatibles de depender de una herramienta**, y tienen consecuencias distintas de mantenimiento, de auditoría y de superficie de ataque. Un paquete publicado en npm se puede fijar por versión; un script clonado se queda en `main`.
El dato fino que no hay que pasar por alto es el reconocimiento explícito de una rotura en la cadena de herramientas ("yarn publishing is broken so lerna uses npm") más un paso de reparación manual de symlinks tras cada publicación. Es un recordatorio de que **la operación de publicar herramientas propias es trabajo de infraestructura, no un comando** — el mismo tipo de coste invisible que el vault ya había registrado en Midjourney-Proxy, donde 5,4k estrellas convivían con un proceso de release congelado desde junio de 2024 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]).
Nota de verificación: la captura es la sección "Publishing" del README; no incluye `package.json`, ni los scripts de `lerna.json`, ni los nombres de los seis paquetes con sus versiones (esas solo aparecen en el mensaje del commit de publicación).
