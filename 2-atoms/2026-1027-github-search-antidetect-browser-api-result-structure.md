---
id: 2026-1027-github-search-antidetect-browser-api-result-structure
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-antidetect-browser-api.md]
links: ["[[2026-1026-github-search-playwright-stealth-dos-de-ocho-no-son-herramientas-de-evasion.md]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos.md]]"]
---

## Claim

La consulta `GET /search/repositories?q=antidetect+browser+api` devuelve `total_count: 21` y `incomplete_results: false`, lo que significa que el índice de GitHub no truncó los resultados y se exhibieron los 21 repositorios completos en la captura del 2026-10-27.

## Why It Matters

Este dato operativo (21 resultados completos, sin truncado) diferencia esta búsqueda de otras consultas de la misma API donde `total_count` no cabía en una página de 20 ítems o donde `incomplete_results: true` indicaba resultados cortados. Para el vault, esto significa que el corpus de 21 repositorios es la población indexada completa para esta query, sobre la cual pueden calcularse razones y distribuciones sin necesidad de paginación adicional.

## Nota de verificación

Cifras extraídas del JSON de `sources/2026-10-27-github-search-antidetect-browser-api.md`: `total_count: 21` en la línea 9 y `incomplete_results: false` en la línea 10. Estas lecturas son literales del campo JSON, no inferencias.