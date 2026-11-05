---
id: 2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02
type: atom
certainty: solid
sources: [sources/2026-11-04-tailscale-docs.md]
links: ["[[2026-1103-tailscale-cuarta-captura-del-kb-sin-frase-zero-trust-ni-urls]]", "[[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]]", "[[2026-1103-tailscale-kb-control-ask-ai]]"]
---

## Claim
La quinta captura de `tailscale.com/kb` (`sources/2026-11-04-tailscale-docs.md`, 2779 bytes, 55 líneas, `word_count: 316`) es **byte a byte idéntica a la del 2026-11-02**: el `diff` entre ambas devuelve una sola línea distinta — el campo `captured:` del frontmatter — y el hash del cuerpo a partir de la línea 4 es el mismo en los dos ficheros (`md5 dfd19d3b301aeb651e1567b1b8d728c4`, 2779 bytes en ambos). Es decir, el índice **no ha cambiado ni un byte** entre el 11-02 y el 11-04: 18 entradas con enlace markdown relativo `/docs/...`, la frase de autodescripción de Zero Trust, la fecha "Last validated Feb 4, 2026" y cero cifras de precio. La captura del 2026-11-03 (420 palabras, 107 líneas), que había perdido la frase y los destinos de enlace, queda así probada como **un render degradado y puntual**, no como una versión distinta de la página.

## Why It Matters
Invierte la lectura de [[2026-1103-tailscale-cuarta-captura-del-kb-sin-frase-zero-trust-ni-urls]]: aquel átomo describía la cuarta captura como "una variante renderizada distinta" frente a las tres anteriores, y de ahí salió la hipótesis de que el índice "no es una fuente estable de rutas". La quinta captura demuestra que la variante era del **fetcher**, no del contenido: 4 de las 5 capturas (11-02, 11-04, y el mismo bloque de 26 líneas en 10-31 y 11-01) comparten el mismo cuerpo, y el 11-03 es el único que se desvía. Consecuencia operativa para el vault: el índice **sí** es una fuente reproducible de las 18 rutas `/docs/...` siempre que se capture con el modo que ya se conoce (markdown relativo), así que la lista de páginas a capturar para el eje de red de [[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]] no hay que reconstruirla, basta con reintentar la captura si sale sin enlaces. Y la tercera vía del patrón "Ask AI" (ver [[2026-1103-tailscale-kb-control-ask-ai]]) también queda reclasificada como artefacto de render, no rasgo de la KB.
