---
id: 2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos
type: atom
certainty: solid
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
links: ["[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]"]
---

## Claim
La comunidad de los 14 repositorios está **concentrada en tres**: las estrellas suman 810 en total y los tres primeros —`verssache/chatgpt-creator` (338), `AuuCoder/gptGrok2api` (285) y `wahdalo/chatgpt-account-creator` (139)— se llevan **762, el 94,1 %**; los cinco primeros se llevan **800, el 98,8 %**. Los cuatro repositorios restantes con al menos una estrella suman 10 estrellas en total (32, 6, 5, 2, 1, 1, 1) y **cuatro repositorios tienen exactamente 0 estrellas**. La razón forks/estrellas separa los dos primeros: `gptGrok2api` acumula **145 forks sobre 285 estrellas (0,51)**, casi el doble que `verssache/chatgpt-creator` (**90 sobre 338, 0,27**), y `wahdalo` va a **69 sobre 139 (0,50)**. Los 308 forks del corpus se concentran en esos mismos tres (304 de 308).

## Why It Matters
La curva de popularidad de esta categoría tiene la misma forma que la del vault ya registrada en Midjourney-Proxy —5,4k estrellas con el código congelado desde junio de 2024 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]])— y en este caso el dato es más duro porque **está medido sobre la población completa**, no sobre un repo: con 14 elementos y un 94 % en tres, se puede decir que la categoría tiene **tres proyectos visibles y una cola de once repositorios huérfanos** (cuatro con cero estrellas, y siete con menos de 10). Cualquier lectura de "hay muchos proyectos de registro de cuentas" queda desmentida por el propio índice.
El segundo dato, el de los forks, es el que tiene consecuencia operativa. Una razón forks/estrellas de **0,5** significa que **la mitad de los usuarios no marca la estrella, copia**: `gptGrok2api` y `wahdalo` están en ese nivel, muy por encima del 0,27 de `verssache`. El ratio de `verssache` es el de un proyecto que la gente consulta; el de los otros dos es el de una **plantilla que la gente fork-ea para adaptar**. Es la misma forma que el vault ya había leído en el 90-forks-por-4-commits de `verssache` ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]), pero aquí con la población completa: **el uso dominante de estas herramientas es copiar y modificar, no instalar y mantener**.

## Nota de verificación
Todas las cifras proceden de `stargazers_count` y `forks_count` de los 14 `items` del JSON capturado el 2026-10-24, sumados y ordenados por el propio `sort=stars` de la consulta. Las razones forks/estrellas son un cálculo del vault sobre esos contadores; el JSON no las publica. La concentración de stars/forks incluye los tres falsos positivos de la consulta en el total de 810 estrellas (aportan 4), por lo que la concentración sobre el corpus depurado de 11 es ligeramente mayor.
