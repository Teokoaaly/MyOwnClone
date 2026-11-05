---
id: 2026-1104-azure-architecture-center-cuarta-captura-identica-a-la-del-11-02
type: atom
certainty: solid
sources: [sources/2026-11-04-azure-architecture-center.md]
links: ["[[2026-1102-azure-architecture-center-tres-capturas-con-contenido-distinto]]", "[[2026-1031-azure-architecture-center]]", "[[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]]"]
---

## Claim
La captura del **2026-11-04** de `learn.microsoft.com/en-us/azure/architecture/` (59 líneas, `word_count: 272`, 2.616 bytes) es **byte a byte idéntica a la del 2026-11-02** en todo su cuerpo: el `diff` entre `sources/2026-11-04-azure-architecture-center.md` y `sources/2026-11-02-azure-architecture-center.md` devuelve **una sola diferencia de contenido** — el campo `captured:` del frontmatter — más el salto de línea final que el fichero del 11-04 no lleva. No hay ningún área nueva, ningún artefacto nuevo y ninguna URL nueva respecto al 11-02: siguen siendo las **mismas 5 áreas de diseño** ("Design for the cloud", "Learn about AI and Machine Learning solutions", "Learn about Azure compute solutions", "Learn about Azure data solutions", "Operationalize application and AI workloads") con sus **15 enlaces de contenido** y sus 5 iconos.

## Why It Matters
Es la **cuarta captura del slug** (10-31, 11-01, 11-02, 11-04 — el 2026-11-03 no capturó esta URL) y aporta **cero novedad de contenido**, pero eso mismo es el dato: el modo de captura "cuerpo limpio, sin navegación" que el vault vio por primera vez el 11-02 **no fue un glitch de un día**, sino un modo de render **repetido**. La captura del 11-02 y la del 11-04 forman un par idéntico, de modo que cualquier afirmación del vault que cite "la captura del 11-02" puede citar indistintamente la del 11-04 sin pérdida de trazabilidad, y a partir de ahora la pregunta relevante no es si la página cambió sino si **el fetcher vuelve a renderizar en modo completo** (con "Get started", el área de seguridad y la navegación, como en [[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]] y [[2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro]]). El precedente del vault con la misma conclusión es [[2026-1104-tailscale-quinta-captura-byte-identica-a-la-del-11-02]], donde un render "diferente" del 11-03 resultó ser también un artefacto del fetcher y no del contenido. La lectura del center como catálogo de marcos sin precios ([[2026-1031-azure-architecture-center]]) queda por tanto **confirmada sin novelty** en esta ventana del 1 al 4 de noviembre.

## Nota de verificación
`diff` entre ambos ficheros: única diferencia de contenido en la línea 3 del frontmatter (`captured: 2026-11-02` → `captured: 2026-11-04`) y el marcador `\ No newline at end of file` en la última línea. md5 de los ficheros completos: 11-02 `37a042c2bf4d86bfb9cde5ef66f0b1d7`, 11-04 `3445549fd2e7bd457bd33ccebcfafa96` (difieren solo por esas dos razones). Conteo de palabras del cuerpo (`tail -n +7 | wc -w`): **272 en ambos**, igual que el `word_count` declarado. Enlaces markdown en el cuerpo: **20 en ambos** (15 de contenido + 5 iconos).
