---
id: 2026-1104-lambda-captura-reducida-a-las-tablas-sin-cromo-ni-pie-de-pagina
type: atom
certainty: solid
sources: [sources/2026-11-04-lambda-gpu-pricing.md, sources/2026-11-01-lambda-gpu-pricing.md]
links: ["[[2026-1031-lambda-h200-en-el-titulo-sin-fila-de-precio]]", "[[2026-1104-lambda-la-tabla-de-precios-nuevos-muestra-las-mismas-cifras-que-las-capturas-anteriores]]", "[[2026-1101-lambda-dos-lineas-de-producto-instances-y-clusters]]"]
---

## Claim
La captura del 2026-11-04 es un **render limpio solo de la zona de precios**: 94 líneas con el H1 "# AI cloud pricing", el H2 "1-Click Clusters pricing", las dos tablas de cluster, el H2 "Instances pricing", el selector de pestañas **"8x4x2x1x" pegado en un solo token** y las cuatro tablas de Instances, y nada más — sin barra de navegación, sin mega-menú, sin footer y sin el bloque de cookies de la captura del 2026-11-01 (295 líneas). Además, el título legible ya no es el de marketing: el 2026-10-31 renderizaba "GPU cloud pricing: rent NVIDIA H100, H200, and B200" y el 2026-11-04 renderiza "# AI cloud pricing", sin mención a H200 ni a H100.

## Why It Matters
Es una segunda fuente de ruido de captura, distinta de la del 2026-11-02 (que renderizaba solo las tablas sin cromo pero **truncadas**): aquí el render es completo en contenido y **mínimo en cromo**. Para el vault esto importa por un lado porque el recorte es total y reproducible — las cuatro pestañas de Instances y las dos de clusters están las dos — y por otro porque explica por qué el H1 de esta captura no puede usarse para el argumento del título con H200 ([[2026-1031-lambda-h200-en-el-titulo-sin-fila-de-precio]]): **el título corto es el que sobrevive al recorte**, así que la ausencia de H200 en él es un artefacto del render, no evidencia de que la página haya dejado de anunciarlo. La regla operativa: **el título de la página no es dato si depende de qué parte del render sobrevive**.

## Nota de método
Conteo de líneas y presencia/ausencia de bloques verificados literalmente en `sources/2026-11-04-lambda-gpu-pricing.md` (94 líneas, frontmatter `word_count: 920`) frente a `sources/2026-11-01-lambda-gpu-pricing.md` (295 líneas, `word_count: 1260`, con navegación y footer) y `sources/2026-10-31-lambda-gpu-pricing.md` (H1 con H100/H200/B200).
