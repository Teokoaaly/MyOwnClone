---
id: 2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers
type: atom
certainty: solid
sources: [sources/2026-10-25-suno2openai.md]
links: ["[[2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers]]", "[[2026-1026-github-search-suno-razon-forks-estrellas-0-18-contra-0-5]]"]
---

## Claim
La página del repositorio (leída del HTML, no de la API de búsqueda) da **275 stars, 49 forks, 2 watchers**, **464 commits**, **2 branches**, **4 tags**, licencia **MIT**, y un **último commit del 19 de enero de 2025** (*"Enhance Suno API client with new notification and permission check features"*). Las secciones **Releases, Used by, Contributors y Languages aparecen vacías**. La captura es además la primera del vault que trae el **contador real de watchers**: la web muestra **2 watching** frente a **275 estrellas**, confirmando que el `watchers_count` de la API (275) es una copia de las estrellas.

## Why It Matters
El dato de los **2 watchers reales** cierra empíricamente la fricción que el vault tenía abierta: [[2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers]] sugería que el "1 watcher" de la página web de otro repo era el contador real y el de la API una copia; aquí se ve el mismo patrón con una distancia mucho mayor (**2 frente a 275**), y confirma de nuevo la regla operativa del vault: de esta API solo son citable estrellas y forks.
El resto de las cifras encaja con el átomo de razón forks/estrellas ([[2026-1026-github-search-suno-razon-forks-estrellas-0-18-contra-0-5]]): 49/275 = 0,18, la categoría donde la estrella domina al fork porque el artefacto **se despliega** (Docker + `docker-compose`, `env.example`, `setup.py`) en vez de copiarse. Y **Releases vacío** explica por qué el canal de distribución declarado en el README es una **imagen `wlhtea/suno2openai:latest` sin versionar**: no hay tags publicados, luego "latest" es la única versión que un operador puede caracterizar.
Los **464 commits** frente a los 4 de `chatgpt-creator` confirman que la categoría de proxy de plataforma es software de mantenimiento largo, no un volcado de script.
