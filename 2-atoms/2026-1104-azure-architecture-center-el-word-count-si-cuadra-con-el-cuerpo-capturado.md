---
id: 2026-1104-azure-architecture-center-el-word-count-si-cuadra-con-el-cuerpo-capturado
type: atom
certainty: solid
sources: [sources/2026-11-04-azure-architecture-center.md]
links: ["[[2026-1102-azure-architecture-center-tres-capturas-con-contenido-distinto]]", "[[2026-1104-azure-architecture-center-cuarta-captura-identica-a-la-del-11-02]]", "[[2026-1031-azure-architecture-center]]"]
---

## Claim
El `word_count` declarado en el frontmatter de las capturas del slug **sí coincide exactamente con el número de palabras del cuerpo capturado**: 11-04 declara `272` y su cuerpo (`tail -n +7 | wc -w`) tiene **272** palabras; 11-02 declara `272` y tiene **272**; 11-01 declara `1162` y tiene **1162**. La **única** excepción es la captura del **2026-10-31**, que declara `word_count: 1123` mientras su cuerpo tiene **238** palabras — y la diferencia tiene causa visible: es la única captura del slug **sin un solo enlace markdown** (0 frente a 20 en el 11-04 y 195 en el 11-01), porque el extractor éliminó los destinos de los enlaces y dejó solo el texto visible.

## Why It Matters
`word_count` es por tanto un **medidor fiel de la riqueza del texto capturado**, que es exactamente la variable que discrimina los modos de render del center (272 en las capturas del 11-02/11-04 frente a 1.162 en la del 11-01 con toda la navegación). La consecuencia práctica para el pipeline del vault: **no hace falta recontar el fichero para saber si una captura traía navegación** — basta leer el frontmatter, y un `word_count` bajo respecto al precedente es la señal barata de "captura reducida, no página cambiada". La excepción del 10-31 sí aporta un matiz útil: un `word_count` **sobrestimado** respecto al cuerpo es la firma de una captura con enlaces desligados, no de una captura más corta.

## [FRICTION]
> [[2026-1102-azure-architecture-center-tres-capturas-con-contenido-distinto]] afirma, en su nota metodológica, que "los `word_count` declarados en el frontmatter (1123 / 1162 / 272) **no coinciden con el tamaño real del archivo** (el del 11-01 tiene 374 líneas de navegación), así que el metadato **no es fiable para medir riqueza**".
> Eso es incorrecto para 2 de las 3 capturas que cita: `1162` y `272` **sí** coinciden exactamente con las palabras del cuerpo, y la comparación que hace —contar palabras contra bytes/líneas— mezcla dos magnitudes. La afirmación **sí acierta** en el fondo para la captura del 10-31, donde el desfase (1.123 declaradas vs 238 reales) tiene una causa concreta y diagnosticable: la captura sin enlaces.
> La conclusión del átomo viejo ("la diferencia entre capturas es qué parte del HTML sobrevive al pipeline, no un cambio de Microsoft") **no se ve afectada** y queda reforzada por la cuarta captura, idéntica a la segunda: ver [[2026-1104-azure-architecture-center-cuarta-captura-identica-a-la-del-11-02]].
> Marcado para juicio humano: no se reescribe el átomo viejo; la corrección vive aquí. La lectura de fondo del center como marco sin precios ([[2026-1031-azure-architecture-center]]) permanece intacta.

## Nota de verificación
Conteo con `tail -n +7 <fichero> | wc -w`: 10-31 → 238, 11-01 → 1.162, 11-02 → 272, 11-04 → 272. `word_count` declarado: 1123, 1162, 272, 272. Enlaces markdown por captura (`grep -c ']('`): 10-31 → 0, 11-01 → 195, 11-02 → 20, 11-04 → 20.
