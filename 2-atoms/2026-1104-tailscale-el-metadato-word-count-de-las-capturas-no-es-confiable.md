---
id: 2026-1104-tailscale-el-metadato-word-count-de-las-capturas-no-es-confiable
type: atom
certainty: solid
sources: [sources/2026-11-04-tailscale-docs.md]
links: ["[[2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02]]", "[[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]]", "[[2026-1103-tailscale-cuarta-captura-del-kb-sin-frase-zero-trust-ni-urls]]"]
---

## Claim
El campo `word_count` del frontmatter de las capturas de `tailscale.com/kb` **no es fiable como indicador del contenido**: comparando el valor declarado con el recuento real de palabras del cuerpo (líneas 6 en adelante), el 11-04 declara **316** y tiene **317** reales, pero la captura del **11-03 declara 420 con solo 301 palabras reales**, y la del **10-31 declara 1452 con 317 palabras reales** — casi cinco veces la cuenta real, porque el contador incluye el bloque de navegación y los banners. En la quinta captura el valor declarado (316) coincide con el real salvo en uno, porque el cuerpo es un índice limpio sin navegación; en las capturas con navegación completa el contador **se infla**. Es decir: el metadato mide lo que el fetcher capturó, no lo que la página contiene.

## Why It Matters
Corrige una herramienta de medida que el pipeline estaba usando sin verificar. La comparación de capturas del corpus de Tailscale no puede apoyarse en `word_count` para decidir si dos capturas "traen lo mismo" o si una "trae más": el 11-03 (420 declaradas / 301 reales) parecía *más rico* que el 11-02 y el 11-04 (316 declaradas / 317 reales), cuando en realidad **tenía menos contenido** — le faltaban la frase de Zero Trust y los 18 destinos de enlace. Con ese metadato, "el 11-03 es más largo" y "el 11-03 es una variante distinta" son la misma conclusión, y por eso la cuarta captura se interpretó como una versión distinta de la página ([[2026-1103-tailscale-cuarta-captura-del-kb-sin-frase-zero-trust-ni-urls]]) en vez de como una captura degradada ([[2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02]]). Regla operativa para el pipeline: **comparar hashes del cuerpo, no metadatos** — `md5` de las líneas 4+ discrimina las capturas correctamente (el 11-02 y el 11-04 comparten `dfd19d3b301aeb651e1567b1b8d728c4`), mientras que `word_count` y el recuento de líneas no. Es la misma lección de fondo del vault: el índice de la KB promete el mapa de la documentación, y el fetcher decide cuánto de ese mapa llega al fichero ([[2026-1101-tailscale-kb-captura-26-lineas-utiles-y-340-de-navegacion-duplicada]]).
