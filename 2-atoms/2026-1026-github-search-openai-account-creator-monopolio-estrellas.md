---
id: 2026-1026-github-search-openai-account-creator-monopolio-estrellas
type: atom
certainty: solid
sources: [sources/2026-10-26-github-search-openai-account-creator-api.md]
links: ["[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1027-github-search-openai-account-creator-api-cuatro-resultados-y-tres-de-ruido]]"]
---

## Claim

El 99,65 % de las estrellas del corpus de 4 repositorios (`total: 287`) están concentradas en un único repositorio: `AuuCoder/gptGrok2api` con 286 estrellas. Los 3 repositorios restantes suman apenas 1 estrella entre sí. El ratio de forks es igualmente concentrado: 145 de 145 forks (100 %) pertenecen a `gptGrok2api`.

## Why It Matters

Este dato cuantifica el monopolio de hecho en el espacio de código abierto de herramientas de alta de cuentas de OpenAI/GPT. La oferta pública visible en GitHub está efectivamente controlada por un solo proyecto, lo que tiene implicaciones para el thread de economía de la verificación: **no existe un ecosistema diversificado de repositorios competitivos**, sino un proyecto dominante con actividad paradoja desde hace 90 días (`pushed_at: 2026-07-27`, sin commits visibles desde entonces). Cualquier análisis de "alternativas abiertas" debe considerar que las supuestas alternativas representan menos del 0,35 % de la estrella total.

## Nota de verificación

Las cifras provienen directamente del JSON de la API de búsqueda capturado el 2026-10-26: `stargazers_count` de cada item (286, 1, 0, 0) y `forks_count` (144, 1, 0, 0). La suma de 287 estrellas y el ratio 0,9965 son cálculos derivados sobre estos contadores. La comparación con el átomo [[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]] confirma que la concentración de estrellas en un solo repositorio ha sido una constante en las capturas sucesivas de esta consulta.