---
id: 2026-1026-github-search-suno-noventa-y-ocho-por-ciento-de-las-estrellas-en-cuatro-repos
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1024-github-search-lenguajes-licencias-y-topics-del-corpus]]"]
---

## Claim
Sobre los **8 items legibles** de la consulta `suno openai api` hay **505 estrellas y 81 forks** en total, y la concentración es más extrema que en la consulta de registro de cuentas: `wlhtea/Suno2openai` (275 estrellas, 49 forks) se lleva solo **el 54,5 %** del total, y **`Suno-API/Suno-API` (159, 26) completa un 85,9 % entre los dos**; los tres primeros (añadiendo `whataicc/doc-whataicc-api`, 37 estrellas) suman **471 = 93,3 %** y los cuatro primeros (añadiendo `Token173/doc-token173-api`, 27) suman **498 = 98,6 %**. Los otros cuatro items suman **7 estrellas en total** (6, 1, 0, 0) y **dos repositorios tienen exactamente 0 estrellas** (`sueson/AI-song-generator-app` con 2 forks y `shawnsporter/Open-AI-Suno-Persona-Creator` con 0). Ninguno es un fork, ninguno está archivado, los 8 son `visibility: public` y de `owner.type: "User"`, y `score` vale 1,0 en los 8.

## Why It Matters
La diferencia estructural con el corpus de registro de cuentas ([[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]) no está en el porcentaje final —94,1 % en tres repos allí, 93,3 % en tres aquí— sino en la **forma de la cabeza**. En el corpus de ChatGPT el primer repo tenía el 42 % de las estrellas; aquí `Suno2openai` tiene **más de la mitad del total**. Es un corpus con **un solo proyecto de referencia y una cola de siete**: el segundo-git del sector, `Suno-API/Suno-API`, es un proyecto **distinto en naturaleza** —una API no oficial de Suno en Go que además expone un endpoint de chat OpenAI-compatible— y no una variante del primero.
Eso importa para el vault porque cambia lo que una búsqueda de "la herramienta de referencia" significa: en la categoría de registro de cuentas la pregunta "cuál es el más popular" no tiene respuesta única porque los tres primeros son objetos distintos (bot, gateway, y un tercero no describible); aquí sí la tiene, y **la respuesta es un repo cuya descripción es, literalmente, "guarda las cookies en una base de datos para poder hacer llamadas desde un pool de cookies"**. La cabeza del corpus es el pool, no el proxy.

## Nota de verificación
Sumas y porcentajes calculados por script sobre los 8 `items` parseados del JSON capturado el 2026-10-25 (`stargazers_count`, `forks_count`). El porcentaje de la cola se calculó sobre 505 estrellas, que es la suma **de los items legibles**, no sobre los 18 del índice (véase [[2026-1026-github-search-suno-dieciocho-resultados-pero-solo-nueve-items-en-el-fichero]]). La mención de `Suno2openai` traduce su campo `description`, que es bilingüe (chino e inglés). El nombre completo del tercer repo es `whataicc/doc-whataicc-api` tal y como aparece en el campo `full_name` del JSON.
