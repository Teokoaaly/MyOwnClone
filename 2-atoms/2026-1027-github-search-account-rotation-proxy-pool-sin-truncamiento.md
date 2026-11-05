---
id: 2026-1027-github-search-account-rotation-proxy-pool-sin-truncamiento
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-account-rotation-proxy-pool.md]
links: ["[[2026-1027-github-search-el-termino-creator-en-la-consulta-es-polisemico-y-no-significa-alta-de-cuentas]]", "[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]"]
---

## Claim

La captura `sources/2026-10-27-github-search-account-rotation-proxy-pool.md` reporta `total_count: 13` y `incomplete_results: false`. Dado que la API de GitHub search usa `per_page=20` por defecto y el parámetro `q=account+rotation+proxy+pool` devolvió exactamente 13 items sin paginación, **el índice no está truncado**: todos los repositoriosindexados para esta consulta aparecen en el resultado. Esto contrasta con capturas previas donde `total_count` excedía `per_page` y la propiedad `incomplete_results: true` indicaba resultados cortados.

## Why It Matters

Para el vault, el hecho de que `incomplete_results: false` y `total_count: 13 ≤ 20` significa que **no hay información perdida** por límite de página en esta captura. Esto valida que cualquier análisis estadístico sobre los 13 items (distribución de lenguajes, recuentos de estrellas, superposición de topics) sea sobre la **población completa indexada** para esta consulta, no una muestra sesgada. La implicación operativa es que se pueden citar con confianza afirmaciones como "el 23% de los repositorios tienen language: Go" o "ningún repositorio tiene license: GPL", sabiendo que la base es el total indexado y no un subconjunto arbitrario.

## Nota de verificación

Conteo confirmado: `total_count: 13` coincide exactamente con la cantidad de `items` en el array JSON de la fuente. El campo `incomplete_results: false` está presente en metadatos. No hay enlace `next` en la respuesta de la API que indicara páginas adicionales.