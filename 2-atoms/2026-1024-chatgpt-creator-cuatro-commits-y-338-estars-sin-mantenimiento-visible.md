---
id: 2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible
type: atom
certainty: solid
sources: [sources/2026-10-24-chatgpt-creator-verssache.md]
links: ["[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]", "[[2026-1024-chatgpt-creator-token-sentinel-y-cabeceras-de-traza-datadog]]"]
---

## Claim
La cabecera del repositorio da las cifras de comunidad y las de mantenimiento, y son de dos ordenes distintos: **338 stars, 90 forks, 1 watcher**, pero **1 branch, 0 tags, 0 releases y solo 4 commits**. La sección "Releases" y la sección "Packages" están **vacías**. La línea temporal es corta y está cerrada: commit inicial **"Initial commit: ChatGPT Account Registration Bot"** (7 meses atrás, 10 de marzo de 2026) y último commit **"feat: add sentinel token generation for account creation"** (6 meses atrás, 6 de abril de 2026), con un tercer commit intermedio **"feat: Persist domain blacklist to blacklist.json"**. Licencia **MIT**, logo en `LICENSE`, `README.md`, `config.json`, `go.mod` y `go.sum` en la raíz, y un único directorio `internal/` que agrupa seis paquetes: `config`, `register`, `email`, `chrome` y `util`.

## Why It Matters
Es el **precedente directo del patrón "popularidad sin mantenimiento"** que el vault ya había registrado para Midjourney-Proxy —allí, 5,4k stars con código congelado desde junio de 2024 ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]); aquí, 338 stars y **un solo mes de vida de código**. La diferencia de escala de la comunidad (338 frente a 5,4k) y la diferencia de forma son la misma: **estrellas y forks no son mantenimiento**.
El dato duro para el vault es el vacío de releases: **0 releases, 0 tags, 0 packages**. No hay versión, no hay artefacto, no hay changelog. Eso significa que la única forma de consumir esta herramienta es `git clone` + `go run cmd/register/main.go` desde `main`, sin control de versión. Para una herramienta cuyo valor está en replicar el comportamiento de un tercero que cambia sin avisar, **la ausencia de versionado es una fragilidad operativa, no un detalle de repositorio**.
Y hay una lectura de alcance: 90 forks por 4 commits es la proporción de un **proyecto de plantilla**. La comunidad ha forkado mucho y ha modificado poco. Eso dice algo sobre la naturaleza del repositorio: no es una plataforma con extensiones, es un script que la gente copia y adapta —y por tanto un indicio de que la línea de "how to evade" está todavía en fase de manual, no de producto.

## [FRICTION]
> [[2026-1023-5sim-guia-openai-marketing-sin-vinculo-con-openai]] (escrita el 2026-10-23, a partir de la guía de OpenAI de 5sim) afirma que "Is it allowed to use a virtual number for OpenAI / ChatGPT? **Yes**", y el thread lo registra como una declaración comercial del vendedor sin base normativa.
> Este átomo presiona esa creencia desde el lado del fabricante: un bot público de registro masivo de cuentas de ChatGPT, con 338 estrellas y 90 forks, cuyo propio README declara que **el uso para crear cuentas "in violation of OpenAI's Terms of Service" es responsabilidad del usuario**. El README también trae el disclaimer estándar "for educational and research purposes only".
> Ambas no pueden ser completamente correctas. Si la respuesta de 5sim fuera cierta en el sentido que implica (uso permitido), el disclaimer de este repositorio y la existencia misma de la herramienta serían innecesarios. Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Todas las cifras (338, 90, 1, 4 commits, 1 branch, 0 tags, releases y packages vacías) y las tres fechas de commit están leídas de la página del repositorio capturada el 2026-10-24. GitHub muestra las fechas relativas junto a las absolutas; el vault usa las absolutas que la propia página muestra. El vault no ha clonado ni ejecutado el repositorio.

## Nota posterior — 2026-10-24 (API de búsqueda de GitHub)
Una captura posterior de la **API de búsqueda de repositorios** (`sources/2026-10-24-github-search-chatgpt-account-creator.md`) **corrobora las dos cifras de comunidad** de este átomo: `verssache/chatgpt-creator` aparece con `stargazers_count: 338` y `forks_count: 90`, idénticos a los leídos en la página. La captura introduce además un matiz que este átomo no recogía: en la API, `watchers_count` vale **338**, es decir, **copia el valor de las estrellas** en los 14 repositorios devueltos, y la API **no expone `subscribers_count`**. La cifra de "1 watcher" de la cabecera web y la de `watchers_count` de la API no pueden describir la misma magnitud. Fricción registrada en [[2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers]], marcada para juicio humano y **no auto-resuelta**.
