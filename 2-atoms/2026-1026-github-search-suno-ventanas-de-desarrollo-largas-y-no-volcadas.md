---
id: 2026-1026-github-search-suno-ventanas-de-desarrollo-largas-y-no-volcadas
type: atom
certainty: solid
sources: [sources/2026-10-25-github-search-suno-openai.md]
links: ["[[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]]", "[[2026-1024-github-search-updated-at-no-es-actividad-de-codigo]]"]
---

## Claim
El patrón de mantenimiento de la consulta `suno openai api` es **el inverso** del que el vault midió en el corpus de registro de cuentas de ChatGPT. Aquí **solo 1 de los 8 items legibles hizo su primer push dentro de las 24 horas siguientes a crearse** (`ShowSnowBlood/suno-api-plus`, 14 h 23 min), y **ninguno** de los ocho publica un push anterior a su creación en menos de un día: el caso extremo es `shawnsporter/Open-AI-Suno-Persona-Creator` (64 KB, 0 estrellas, 0 forks), cuyo `pushed_at` es **anterior** a `created_at` en 7,82 días. Las ventanas de desarrollo reales son largas: `wlhtea/Suno2openai` **296,18 días** entre creación (2024-03-29) y push (2025-01-19), `whataicc/doc-whataicc-api` **245,23 días** (2025-09-10 → 2026-05-13), `Suno-API/Suno-API` **208,01 días** (2024-06-02 → 2024-12-27), `wesleysimplicio/PiAPI-Skills` 75,79 días y `Token173/doc-token173-api` 30,29 días. Al momento de la captura (2026-10-25) el `pushed_at` más reciente de todo el corpus era el del 2026-07-21 (`PiAPI-Skills`), **95,5 días antes**: **tres repositorios llevaban más de 640 días sin push** —`Suno-API/Suno-API` **666,9 días**, `sueson/AI-song-generator-app` **643,5** y `wlhtea/Suno2openai` **643,3**—; `updated_at` es posterior a `pushed_at` en los 8 casos, con desfases de hasta 650 días. Los tres repositorios más nuevos del corpus se crearon en 2026 (`Token173` el 2026-05-27, `PiAPI-Skills` el 2026-05-06, `suno-api-plus` el 2026-07-19).

## Why It Matters
El corpus de registro de cuentas dejó al vault una regla que parecía general —"se sube el código de una vez y no se vuelve a tocar" ([[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]])— y esta captura muestra que **no es una regla del sector sino de ese sector**: un repo que expone una API de terceros se desarrolla durante meses, porque tiene que **seguir el ritmo del proveedor** y mantener parsers, cookies y formatos de respuesta que cambian sin avisar. La distancia entre creación y push es la firma de esa dependencia externa: `Suno2openai` vivió 296 días de desarrollo frente a los 22 minutos de `chatgpt-account-creator`.
El segundo dato, más accionable, es que la categoría **no está muerta pero está congelada en una ventana concreta**: hay repositorios creados en mayo y julio de 2026 —o sea, la categoría recibió contribuciones nuevas hasta hace pocos meses— pero **el push más reciente del corpus entero es del 2026-07-21**, hace 95 días. Es un mercado que **empezó a crecer en 2026 y se detuvo en verano de 2026**; el corpus de ChatGPT muestra **el mismo congelamiento estival** —su `pushed_at` más reciente es del 2026-07-27, 88 días antes de su captura—, pero con repositorios de creación más temprana. Es la diferencia entre un mercado **que ya no se toca** y uno **que se acaba de tocar y lleva un trimestre sin tocarse**, y solo la segunda admite que el próximo movimiento sea de vuelta.

## [FRICTION]
> [[2026-1024-github-search-diez-de-catorce-se-pushearon-en-las-veinticuatro-horas]] (escrita el 2026-10-24) afirma, del corpus de registro de cuentas, que "**10 de los 14 repositorios publicaron su primer push dentro de las 24 horas siguientes a su creación o incluso antes**" y generaliza que la categoría "es el volcado de un script".
> Este átomo presiona esa generalización desde la otra categoría: en `suno openai api` **solo 1 de 8** cumple el patrón de las 24 horas, y los dos repositorios más populares **se contradicen**: `Suno2openai` 296 días y `Suno-API` 208 días entre creación y primer push. La regla "subir y olvidar" **no es una ley de las categorías de API no oficial**: describe mejor a los scripts de evasión, que no dependen de ningún proveedor externo, que a los proxies de una plataforma que cambia.
> Ambas no pueden ser la misma regla general. Marcado para juicio humano, no auto-resuelto: son **dos consultas distintas con dos dominios distintos**, y el vault no puede saber todavía cuál de las dos formas generaliza a qué.

## Nota de verificación
Todas las cifras se calcularon por script sobre los `created_at`, `pushed_at` y `updated_at` de los 8 `items` legibles del JSON capturado el 2026-10-25, con fecha de captura 2026-10-25T00:00:00Z como referencia. El noveno item truncado (`mmmbankton/sunog-telegram-bot`, push 2,9 minutos después de crearse) queda fuera de los recuentos y se menciona solo como dato aislado; sus contadores no son recuperables.


## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio, 2026-10-25).

El átomo calculará las ventanas sobre `created_at`/`pushed_at` del JSON de la API de búsqueda. La página HTML del repositorio **confirma y afina** la cifra con datos que el JSON no expone:

- **464 commits**, **2 branches**, **4 tags**, último commit **19 de enero de 2025** (*"Enhance Suno API client with new notification and permission check features"*). El `pushed_at` que el átomo situaba el 2025-01-19 queda corroborado directamente por la cabecera del repo.
- **Dato nuevo: la guía de despliegue por `docker-compose` lleva su propia marca temporal — *"Update Time: 2024/4/7 18:18"* —, anterior al último commit.** Es decir, en este repo el README es **más viejo que el código**, al revés que en `midjourney-proxy` (README de agosto de 2025 sobre código congelado en junio de 2024). La regla operativa que se sigue: **un README auto-declarado con fecha hay que contrastarlo con `pushed_at` antes de tratarlo como procedimiento vigente** ([[2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija]]).
- **Ausencia de releases**: la sección *Releases* de la página está vacía, de modo que la distribución es **una imagen `wlhtea/suno2openai:latest` sin versión fijable** —a diferencia de `new-api`, donde el README sí obliga a fijar versión desde Releases ([[2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija]]).
