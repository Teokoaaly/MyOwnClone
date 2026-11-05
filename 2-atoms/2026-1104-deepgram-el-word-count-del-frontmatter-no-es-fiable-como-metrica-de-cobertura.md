---
id: 2026-1104-deepgram-el-word-count-del-frontmatter-no-es-fiable-como-metrica-de-cobertura
type: atom
certainty: solid
sources: [sources/2026-11-04-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md, sources/2026-11-02-deepgram-pricing.md, sources/2026-11-01-deepgram-pricing.md, sources/2026-10-31-deepgram-pricing.md]
links: ["[[2026-1104-deepgram-bloque-de-compliance-solo-en-tres-de-cinco-capturas]]", "[[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]]", "[[2026-1104-deepgram-renderizado-completo-restaurado-identico-al-11-01]]"]
---

## Claim
El campo `word_count` del frontmatter de las capturas de `deepgram.com/pricing` **no coincide con el recuento real del cuerpo y se desincroniza en ambos sentidos**: la captura del 10-31 declara `word_count: 3125` y su cuerpo tiene **1.350** palabras (`wc -w` sobre el cuerpo, 8.067 bytes); la del 11-03 declara `word_count: 950` y su cuerpo tiene **1.385** palabras (7.985 bytes) — es decir, la captura que el metadato presenta como la más corta es en realidad más larga que la del 10-31. Las del 11-01, 11-02 y 11-04 declaran `word_count: 1560` frente a **1.559** palabras reales (10.239 bytes), un desajuste mínimo pero no nulo. El `word_count` del 11-04 es, por tanto, **idéntico al del 11-01 y el 11-02, que son la misma página** —lo que significa que el metadato es del propio pipeline y no una medida de la página.

## Why It Matters
Este dato desactiva el argumento más fácil —y erróneo— para explicar la diferencia entre capturas: "el 11-04 tiene 1.560 palabras frente a 1.382 del 11-03, luego ha entrado contenido nuevo". La diferencia de recuento no se corresponde con contenido: el 11-04 es **byte a byte el 11-01** y no aporta ni una cifra que no estuviera ya ([[2026-1104-deepgram-renderizado-completo-restaurado-identico-al-11-01]]), y el 11-03, pese a su `word_count: 950`, contiene la tabla de precios completa. La regla operativa para el pipeline: **el `word_count` del frontmatter solo sirve como indicador de extracción, nunca como medida de cobertura de contenido, y jamás debe usarse para afirmar que "apareció" o "desapareció" una sección** — eso solo se puede afirmar contra el material (ver [[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]]). Complementa la lectura de las tres variantes de render en [[2026-1104-deepgram-bloque-de-compliance-solo-en-tres-de-cinco-capturas]]: el metadato es otra capa donde la captura dice menos de lo que la página tiene.

## [FRICTION]
> [[2026-1103-deepgram-captura-11-03-rendering-reducido-y-sin-enlaces]] (escrita hace 2 días) usa el contraste "8.060 bytes y ~950 palabras frente a 8.143 y 10.315-10.316 bytes" como evidencia del carácter reducido del 11-03.
> Los bytes sí son una medida válida de render (el 11-04 tiene 10.315 bytes y el 11-01 10.315), pero **las ~950 palabras no lo son**: el recuento real del cuerpo del 11-03 es 1.385, y el del 10-31 (8.143 bytes) es 1.350, de modo que el orden por longitud real de las cinco capturas es 11-01/11-02/11-04 (1.559) > 11-03 (1.385) > 10-31 (1.350), **no** el inverso que sugiere el metadato. El byte-count que cita el átomo viejo sigue siendo correcto; la palabra-count no. Marcado para juicio humano, no auto-resuelto.
