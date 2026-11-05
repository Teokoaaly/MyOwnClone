---
id: 2026-1026-puppeteer-extra-604-commits-559-tags-y-ultimo-commit-en-marzo-de-2023
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]"]
---

## Claim
La cabecera del repositorio da: **7.4k estrellas, 115 watchers, 783 forks, 604 commits, 5 branches, 559 tags**, licencia **MIT**, y el último commit es **"Publish"** (`39248f1`), fechado el **1 de marzo de 2023** —la página lo marca como "3 years ago" en la fecha de captura (2026-10-25). El README en sí lleva el último cambio el **3 de julio de 2022** y `package.json` el **21 de septiembre de 2021** ("feat: Support old and new puppeteer types (#555)"), que incluye el commit "chore: Disable adblocker plugin build in old pptr versions" y "ci: Update puppeteer version matrix".

## Why It Matters
El vault ya tiene registrado el patrón "**popularidad sin mantenimiento**" dos veces, y siempre con la misma lección: en Midjourney-Proxy, 5.4k estrellas con código congelado desde junio de 2024; en `chatgpt-creator`, 338 estrellas, 90 forks y **cuatro commits, cero releases, cero tags** ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]). Aquí la combinación es distinta en un dato que importa: **604 commits y 559 tags frente a 4 commits y 0 tags**. Es decir, este proyecto **sí tuvo ciclo de releases**: 559 tags son 559 versiones publicables, y el commit de publicación es explícito sobre qué se publica y con qué política.
Pero la segunda mitad del patrón se repite: **el código está congelado desde marzo de 2023**, tres años y medio antes de la captura, y el propio mensaje de `package.json` —"Support old and new puppeteer types" con "ci: Update puppeteer version matrix"— indica que la compatibilidad dependía de una **matriz de versiones de Puppeteer**, que es exactamente lo que deja de ser cierto cuando el framework no se toca. La consecuencia operativa es la misma que en los otros casos y conviene no suavizarla: **7.4k estrellas no son mantenimiento, y 559 tags no son compatibilidad con el Puppeteer actual**. Es la forma más fuerte del patrón hasta la fecha, porque es la única que tiene a la vez la escala grande y el proceso de release y aun así está parada.
Y tiene una lectura cuantitativa dentro del corpus: 7.4k estrellas frente a las 810 que suman los 14 repositorios de la búsqueda de "chatgpt account creator" ([[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]) — es decir, **el framework de evasión es un orden de magnitud más popular que la suma de los scripts de alta que el corpus tenía inventariados**, y esa asimetría es un dato sobre qué es lo que la gente realmente reutiliza.
Nota de verificación: la fecha "1 de marzo de 2023" es la que muestra la propia página; "3 years ago" es la etiqueta relativa en la fecha de captura. El vault **no ha clonado ni ejecutado el repositorio**.
