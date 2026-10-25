---
id: 2026-10-25-refinery-github-search
type: briefing
date: 2026-10-25
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
---

# Briefing — Refinery: captura GitHub Search API (chatgpt account creator)

**Captura procesada:** `0-raw/2026-10-24-github-search-chatgpt-account-creator.md` (movida a `0-raw/archive/2026-10-25-2026-10-24-github-search-chatgpt-account-creator.md`)
**Fuente:** `sources/2026-10-24-github-search-chatgpt-account-creator.md` — respuesta JSON de `GET /search/repositories?q=chatgpt+account+creator&sort=stars&order=desc&per_page=20`, 94 KB, capturada el 2026-10-24.

## Qué es esta captura

No es un artículo: es el **índice completo de repositorios de GitHub** que GitHub devuelve para la frase "chatgpt account creator". Es la primera captura del vault que **cuantifica un corpus** en vez de describir un repositorio suelto, y por eso su valor es más de contexto que de detalle.

## Hallazgos principales

1. **El corpus es de 14 repositorios, entero y cerrado.** `total_count: 14`, `incomplete_results: false`, 14 < `per_page`. No hay cola truncada. Suman 810 estrellas y 308 forks. Ninguno es un fork, ninguno está archivado, todos públicos y de autor individual.
2. **3 de los 14 son falsos positivos** (Instagram Reels, gestor de cookies de Roblox, servidor MCP de Gumroad): coinciden por las palabras "creator" y "ChatGPT" en su texto. El corpus real es de 11, y **4 de esos 11 van sin `description`**.
3. **94,1 % de las estrellas en tres repositorios**; los cinco primeros se llevan el 98,8 %. Cuatro repositorios tienen cero estrellas. El ratio forks/estrellas de `gptGrok2api` (0,51) y `wahdalo` (0,50) dice que el uso dominante es **copiar y adaptar**, no instalar y mantener.
4. **La categoría entera lleva parada.** 10 de 14 publicaron su primer push dentro de las 24 horas de crearse; en la fecha de captura **ninguno había hecho push en los últimos 88 días**, once llevaban más de 180 días sin push. El mercado (5sim, HeroSMS, PriceAI, lzt.market) sigue vivo; el código que lo implementa, no.
5. **Dos correcciones de método, que son el valor real de la captura:**
   - `watchers_count` es **numéricamente idéntico a `stargazers_count` en los 14 casos**, y la API **no expone `subscribers_count`**. La API no mide comunidad más allá de dos contadores.
   - `updated_at` **no es actividad de código** sino metadato: los 14 lo tienen posterior a `pushed_at`; `verssache` lo tiene en la misma madrugada de la captura, seis meses y medio después de su último push. Para mantenimiento, hay que leer `pushed_at`.
6. **Higiene pobre del corpus**: 6 de 14 sin licencia declarada, 11 de 14 sin topics, 4 sin descripción. Stack disperso entre JavaScript, Python, Go y TypeScript. Solo tres publican homepage, y el único con homepage de negocio real es `gptGrok2api` (`muyuai.top`) — **el segundo escalón de la categoría ya es un servicio, no una herramienta**.

## Lo que la captura **no** permite concluir

- **No es un censo de herramientas de registro.** 14 es el tamaño del índice para esa consulta concreta, no el número de herramientas que existen. Repositorios con otros nombres (registro en chino, forks, repos privados) quedan fuera.
- **No hay mantenimiento por repositorio**: la API no expone commits, ramas, tags, releases, contributors ni README.
- **No hay watchers reales** (ver punto 5) ni tamaño de comunidad más allá de estrellas y forks.
- **No se puede clasificar herramientas** a partir de ella: 3 falsos positivos, 4 descripciones nulas, 11 topics vacíos. Sirve para contar y ordenar, no para clasificar.
- `size` (7 KB – 22.880 KB) **no es comparable** entre repositorios: el mayor del corpus es un gestor de cookies de Roblox con una estrella.
- El vault **no ha hecho ninguna búsqueda web adicional ni ha clonado ningún repositorio**. La captura es la verdad de referencia.

## Fricción levantada (1)

- `watchers_count: 338` (API) frente al "1 watcher" del átomo [[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]] (página web). Ambas cifras no pueden describir la misma magnitud. La explicación probable —alias histórico en la API— **no está en la captura**. Marcada en el átomo nuevo para juicio humano, **no auto-resuelta**.

## Atomos creados (8)

- `2-atoms/2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta.md`
- `2-atoms/2026-1024-github-search-tres-de-catorce-son-falsos-positivos-de-la-consulta.md`
- `2-atoms/2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos.md`
- `2-atoms/2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas.md`
- `2-atoms/2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers.md`
- `2-atoms/2026-1024-github-search-lenguajes-licencias-y-topics-del-corpus.md`
- `2-atoms/2026-1024-github-search-el-tercer-puesto-no-es-describible-desde-el-json.md`
- `2-atoms/2026-1024-github-search-updated-at-no-es-actividad-de-codigo.md`

**Atomos extendidos (1, sin sobrescribir nada):**
- `2-atoms/2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible.md` — se le ha añadido un bloque final **"Nota posterior — 2026-10-24 (API de búsqueda de GitHub)"** que corrobora sus cifras de comunidad (338 estrellas / 90 forks, idénticas en la API) y remite a la fricción de `watchers_count`. Las afirmaciones previas del átomo **no se han tocado**.

## Propuesta de thread (aplicada el 2026-10-25)

`1-desk/thread-addition-github-search.md` — propone una **§7.5 "El corpus público de herramientas de registro: 14 repositorios, tres con comunidad"** para `3-threads/economia-de-la-verificacion-y-reventa-de-cuentas.md`, más **dos fricciones nuevas (§18 y §19)** para la sección de fricciones de ese thread. La propuesta se aplicó a `3-threads/` el 2026-10-25 (§7.5 + fricciones 34–35, numeración final).

## Para la persona

- **Decisión pendiente 1:** ¿se acepta que `watchers_count` de la API se cite como alias de estrellas y se prohíba usar "watchers" desde la API? La fricción queda abierta en el átomo.
- **Decisión pendiente 2:** ¿interesa capturar `wahdalo/chatgpt-account-creator` (139 estrellas, 69 forks, sin descripción) desde su página de repositorio? Es el tercer más popular del corpus y el vault no sabe qué hace.
- **Decisión pendiente 3:** la categoría lleva tres meses sin push y el corpus público es de 14 repositorios. Si el market sigue vivo, está en otro sitio —y el vault no tiene ninguna fuente que lo cubra. ¿Vale la pena una captura del circuito cerrado en la próxima tanda?

## Nota de método

Cifras leídas del JSON capturado y recalculadas sobre los 14 objetos `items` (sumas, ratios forks/estrellas, diferencias temporales, recuentos de campos ausentes). La distinción medición/claim del thread se mantiene: aquí **todo es medición**, y se añade una tercera categoría propia de esta fuente: **lo que la API no expone**.
