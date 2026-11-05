---
id: 2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers
type: atom
certainty: solid
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
links: ["[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]", "[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]"]
---

## Claim
En los 14 `items` de la respuesta, `watchers_count` es **numéricamente idéntico a `stargazers_count` en los 14 casos** (338/338, 285/285, 139/139, 32/32, 6/6, 5/5, 2/2, 1/1, 1/1, 1/1, 0/0, 0/0, 0/0, 0/0), y el objeto `owner` **no expone ningún campo de seguidores, watchers o suscripciones**. La API de búsqueda, además, **no devuelve el campo `subscribers_count`** (el contador real de watchers de un repositorio) ni ningún otro indicador de comunidad más allá de estrellas y forks. Lo que sí trae es un bloque de metadatos de proyecto: `has_issues` (verdadero en 12 de 14), `has_projects` (verdadero en los 14), `has_wiki` (10 de 14), `has_discussions` (falso en los 14), `has_pages` (falso en los 14), `has_downloads` (falso en los 14), `is_template` (falso en los 14), `archived` y `disabled` (falsos en los 14), `visibility: "public"` en todos, `default_branch` (`main` en 12, `master` en 2) y `open_issues_count` (3 en los tres primeros, 0 en nueve de ellos). El campo `size` va de 7 KB a 22.880 KB, y **no** es comparable entre repositorios como medida de complejidad: `CookieProfileCreator` (22.880 KB, 1 estrella, un gestor de cookies para Roblox) y `gptGrok2api` (4.863 KB, 285 estrellas) están en el mismo orden de magnitud de tamaño pero a escala de comunidad 285:1.

## Why It Matters
Este átomo existe para **cerrar una puerta**: la respuesta de búsqueda **no permite medir el tamaño de la comunidad más allá de dos contadores**. No hay watchers, no hay seguidores, no hay contributors, no hay commits, no hay ramas, no hay tags, no hay releases, no hay issues listadas, no hay README, no hay topics en 11 de los 14 casos y no hay licencia declarada en 6. Todo lo que el vault ha medido sobre repositorios desde la página HTML —los 4 commits y 0 tags de `verssache`, el 1 watcher, los 229 commits y 27 tags de Midjourney-Proxy ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]], [[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]])— **no es recuperable desde la API de búsqueda**. La captura sirve para el orden por estrellas y forks, las fechas de creación y push, y las banderas de proyecto; para todo lo demás hay que ir al repositorio.
La segunda parte tiene una consecuencia práctica que ya está mordiendo en el vault: **`watchers_count` duplica `stargazers_count` y por tanto no es un dato de observadores distintos**. Confundir watchers con stars es un error fácil de cometer leyendo JSON, y un dato que en la interfaz web de GitHub sí tiene un valor distinto y menor. Marcarlo aquí evita que una cifra de 338 "watchers" entre en el vault como si fueran 338 personas siguiendo el proyecto.
Y la lectura sobre `size` es la que más fácilmente se tuerce: 22.880 KB no significa "proyecto grande", significa "muchos archivos", y el corpus contiene un repositorio de 22.880 KB con **una estrella**. El tamaño del repositorio no correlaciona con nada que el vault mida aquí.

## [FRICTION]
> [[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]] (escrita el 2026-10-24 desde la página de HTML del repositorio) afirma para `verssache/chatgpt-creator`: "**338 stars, 90 forks, 1 watcher**".
> Este átomo presiona ese dato desde el lado de la API: en la respuesta de búsqueda, el `verssache/chatgpt-creator` aparece con `watchers_count: 338`, **exactamente el mismo número que las estrellas** —y el mismo fenómeno ocurre en los 14 repositorios, sin una sola excepción. Las dos afirmaciones, leídas como "el repositorio tiene 338 observadores", **no pueden ser correctas a la vez**.
> La explicación más probable es que `watchers_count` sea un alias histórico de `stargazers_count` en la API y que el "1 watcher" de la página web sea el contador real de suscriptores; **pero esa explicación no está en la captura**, que solo muestra la igualdad numérica en 14 casos. Marcado para juicio humano, no auto-resuelto: el vault no debe citar "watchers" desde la API sin verificar la equivalencia contra la interfaz web.

## Nota de verificación
Comprobación campo a campo sobre los 14 `items` del JSON capturado el 2026-10-24: la igualdad `watchers_count == stargazers_count` se verificó en los 14 sin excepción, y la ausencia de `subscribers_count` se verificó sobre el conjunto de claves de cada objeto. Los recuentos de `has_*` e `is_template` y el de `default_branch` son recuentos del vault sobre esos mismos 14 objetos.


## Nota de extensión 2026-10-26
La advertencia queda **confirmada por una segunda consulta independiente**, con otra cadena de búsqueda, otro corpus y otro día: en los 8 objetos íntegros de `q=playwright+stealth+bypass` (2026-10-25), `watchers_count` es **idéntico a `stargazers_count` en los 8 casos sin excepción** (13.165/13.165, 11.947/11.947, 2.520/2.520, 871/871, 408/408, 205/205, 45/45, 5/5), y la API sigue **sin exponer `subscribers_count`**. Eso convierte la conclusión de este átomo en regla general del vault: **ninguna cifra de "observadores" puede citarse desde un JSON de búsqueda de repositorios**. Refuerza además la parte de "la respuesta no permite medir la comunidad más allá de dos contadores": en este corpus nuevo hay `has_discussions: true` en 4 de 8 —una señal de comunidad que sí existe en los metadatos—, pero sigue sin haber ningún contador numérico de esa comunidad. Ver [[2026-1026-github-search-playwright-stealth-la-higiene-de-metadatos-es-mejor-que-en-la-consulta-anterior]].


## Nota de extensión 2026-10-26
Una segunda captura de la misma API, con otra consulta, **confirma la regla en una muestra independiente**. En la consulta `GET /search/repositories?q=suno+openai+api` (2026-10-25), `watchers_count` es **idéntico a `stargazers_count` en los 8 items legibles** (275/275, 159/159, 37/37, 0/0, 27/27, 6/6, 1/1, 0/0), `subscribers_count` **sigue ausente en los 8** y `score` vale **1,0 en los 8** ([[2026-1026-github-search-suno-perfil-tecnico-y-metadatos-del-corpus]]). La confirmación tiene una consecuencia operativa que este átomo ya enunciaba y que ahora es medible: **la única cifra de comunidad publicable de esta API es `stargazers_count`, y el "número de watchers" que devuelve no es un dato de observadores sino la misma estrellas contada dos veces** —de modo que cualquier nota del vault que lo cite como "observadores" está usando un campo que no significa eso.


## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio `wlhtea/Suno2openai`, 2026-10-25).

**Segundo caso empírico de la fricción, con distancia mayor.** La página web del repositorio muestra **275 stars** y **2 watching**, mientras que el `watchers_count` que devuelve la API de búsqueda para este mismo repo es **275**. Es el mismo patrón que el caso de `verssache/chatgpt-creator` (338/1), pero con una separación mucho mayor: **2 observadores frente a 275 estrellas**.

Esto refuerza la regla operativa del átomo —de la API de búsqueda solo son citable estrellas y forks— y añade una precisión: **el "2 watching" de la página web es el contador real de suscriptores**, y para este repo es prácticamente nulo, lo que dice algo sobre la base de usuarios real de un proyecto con 275 estrellas y 49 forks ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]).


## Nota de extensión 2026-10-27
La regla de este átomo queda **confirmada en una muestra independiente de siete items nuevos**: en `q=openai+account+creator+api` (4 items) y `q=claude+account+creator+api` (3 items), `watchers_count` es **idéntico a `stargazers_count` en los 7 de 7** (286/286, 1/1, 0/0, 0/0, 11/11, 3/3, 0/0). Con estas dos capturas, la regla acumula **21 items verificados en tres consultas distintas** (14 + 4 + 3), todos con el par de contadores duplicado.
La extensión aporta un dato de **magnitud** que la regla anterior no tenía: en el corpus de Claude la separación es **11 estrellas frente a 0**, es decir, el único item con comunidad real de esa consulta es un repositorio **pequeño, de 104 KB y sin código de generación de cuentas**. Es decir, **la comunidad de la categoría "Claude + creator" está en la gestión de cuentas de Instagram, no en el alta de cuentas de Claude** ([[2026-1027-dos-mcp-para-cuentas-de-negocio-de-instagram-con-gran-madurez-y-sin-ninguna]]).
