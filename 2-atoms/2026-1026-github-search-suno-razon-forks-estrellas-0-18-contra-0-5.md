---
id: 2026-1026-github-search-suno-razon-forks-estrellas-0-18-contra-0-5
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]", "[[2026-1026-github-search-suno-noventa-y-ocho-por-ciento-de-las-estrellas-en-cuatro-repos]]"]
---

## Claim
La razón forks/estrellas de los dos repositorios con comunidad de la consulta `suno openai api` es **0,18 y 0,16** —`wlhtea/Suno2openai` 49 forks sobre 275 estrellas, `Suno-API/Suno-API` 26 sobre 159— frente a los **0,51 y 0,50** de los dos primeros del corpus de registro de cuentas de ChatGPT (`AuuCoder/gptGrok2api` 145/285, `wahdalo/chatgpt-account-creator` 69/139) y 0,27 de `verssache/chatgpt-creator`. En el corpus de Suno el total es **81 forks sobre 505 estrellas (0,16)**, frente a **308 sobre 810 (0,38)** en el corpus de ChatGPT. Un repo del corpus de Suno —`ShowSnowBlood/suno-api-plus`— tiene **1 estrella y 1 fork (razón 1,0)** y `sueson/AI-song-generator-app` tiene **0 estrellas y 2 forks**.

## Why It Matters
El vault interpretó la razón forks/estrellas de 0,5 del corpus de registro como "**la mitad de los usuarios no marca la estrella, copia**: el uso dominante de estas herramientas es copiar y modificar, no instalar y mantener" ([[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]). Con 0,16–0,18, la categoría de Suno se comporta al revés: **la estrella domina al fork por cinco veces**, que es la firma de un artefacto que se **despliega y se usa**, no de una plantilla que se fork-ea para adaptar. La razón es estructural y ya está visible en las descripciones: `Suno2openai` es un servicio con base de datos de cookies y pool que se integra con `newapi`/`oneapi` — su valor está en **conectarlo a tu relay**, no en modificar su código; y `Suno-API` es un binario en Go de 357 KB.
El dato de `suno-api-plus` (1 estrella, 1 fork) y de `AI-song-generator-app` (0 estrellas, 2 forks) confirma el borde: en la cola, donde no hay comunidad, **los forks superan a las estrellas**, porque sin visibilidad el único modo de reutilización es la copia. Es un patrón de dos lealtades con valor propio: **forks como señal de invisibilidad en la cola, forks como señal de irrelevancia en la cabeza**.

## [FRICTION]
> [[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]] (escrita el 2026-10-24) afirma, del corpus de registro de cuentas, que "una razón forks/estrellas de **0,5** significa que la mitad de los usuarios no marca la estrella, copia" y lo eleva a regla de uso de la categoría: "**el uso dominante de estas herramientas es copiar y modificar, no instalar y mantener**".
> Este átomo presiona esa lectura como regla general: en la categoría de API no oficial de Suno la razón es **0,16–0,18**, cinco veces menor, y la interpretación se invierte — **se despliega y se conecta, no se copia**. La métrica no dice cómo se usa una categoría; dice cómo se usa *un tipo* de artefacto, y el vault tiene ahora dos tipos medidos en la misma API con razones incompatibles.
> Ambas no pueden ser la misma regla. Marcado para juicio humano, no auto-resuelto: el vault no ha medido la razón forks/estrellas de forma separada por categoría con suficiente población como para decidir cuál generaliza.

## Nota de verificación
Razones forks/estrellas calculadas por script sobre `forks_count` y `stargazers_count` de los 8 `items` legibles del JSON del 2026-10-25; los ratios del corpus de ChatGPT (0,51, 0,50, 0,27) y los totales (308/810) están tomados del átomo existente del 2026-10-24. Las razones no las publica ninguna de las dos fuentes: son cálculo del vault.


## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio, 2026-10-25).

La razón 49/275 = 0,18 que el átomo calcula sobre el JSON queda **confirmada por la página HTML**, que muestra los mismos contadores (275 stars, 49 forks). El README añade la explicación operativa de por qué la estrella domina al fork: **el artefacto se despliega** —imagen de Docker Hub, `docker-compose`, `env.example`, `setup.py`, `start.sh`— y se consume desde un relay, no se modifica ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]).
