---
id: 2026-1102-azure-architecture-center-tres-capturas-con-contenido-distinto
type: atom
certainty: solid
sources: [sources/2026-10-31-azure-architecture-center.md, sources/2026-11-01-azure-architecture-center.md, sources/2026-11-02-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-cuatro-puntos-de-entrada]]", "[[2026-1031-azure-architecture-center]]", "[[2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro]]"]
---

## Claim
Tres capturas consecutivas (2026-10-31, 2026-11-01, 2026-11-02) de la **misma URL** `learn.microsoft.com/en-us/azure/architecture/` producen contenidos distintos: la del 10-31 declara `word_count: 1123` y lista **5 áreas de diseño**; la del 11-01 declara `word_count: 1162`, incluye la sección **"Get started"** con sus 4 puntos de entrada, la **6ª área** ("Secure and connect workloads", con hub-spoke y DMZ segura) y toda la navegación de Learn; la del 11-02 declara `word_count: 272` y vuelve a listar **solo las 5 áreas** sin Get started ni seguridad.

## Why It Matters
El sitio es **estable en contenido pero inestable en extracción**: la diferencia entre las tres capturas no es un cambio de Microsoft, es qué parte del HTML sobrevive al pipeline de captura (la del 11-01 conserva navegación y breadcrumbs, la del 11-02 solo el cuerpo). Consecuencia operativa para el vault: **una captura delgada de este tipo no es evidencia de que un área no exista** — el área de seguridad no aparece en 10-31 ni en 11-02, pero sí en 11-01 (ver [[2026-1101-azure-architecture-center-hub-spoke-y-dmz-para-hibrido-seguro]]). Y para el criterio de "una idea por átomo": obliga a no generar átomos por día para la misma página, sino a extraer claims únicos y citar la captura donde la afirmación es literal — lo que es justamente lo que ocurre con los claims de este lote, todos salen de la captura del 11-01 salvo la comparación entre las tres.
Nota metodológica: los `word_count` declarados en el frontmatter (1123 / 1162 / 272) **no coinciden con el tamaño real del archivo** (el del 11-01 tiene 374 líneas de navegación), así que el metadato no es fiable para medir riqueza.

## Actualización 2026-11-04 (cuarta captura del slug)
Fuente: `sources/2026-11-04-azure-architecture-center.md`. La cuarta captura del slug es **byte a byte idéntica a la del 11-02** (única diferencia: el campo `captured:` y el salto de línea final), de modo que el modo de render "cuerpo limpio con 5 áreas y 15 enlaces relativos" queda **repetido dos veces** y no fue un artefacto de un único día. Ver [[2026-1104-azure-architecture-center-cuarta-captura-identica-a-la-del-11-02]] y [[2026-1104-azure-architecture-center-la-captura-renderiza-urls-relativas-y-no-absolutas]].

Matiz que **corrige la nota metodológica de arriba** (sin reescribirla): el `word_count` declarado **sí coincide exactamente** con el número de palabras del cuerpo en las capturas del 11-01 (1.162), 11-02 (272) y 11-04 (272); el único desfase real es el del **10-31** (1.123 declaradas frente a 238 palabras del cuerpo), y su causa es visible: es la única captura **sin enlaces markdown**, porque el extractor eliminó los destinos y dejó solo el texto visible. Detalle en [[2026-1104-azure-architecture-center-el-word-count-si-cuadra-con-el-cuerpo-capturado]].
