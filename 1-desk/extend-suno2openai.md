=== EXTEND 2-atoms/2026-1026-github-search-suno-pool-de-cookies-y-relay-newapi-oneapi.md
## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (README de `wlhtea/Suno2openai`, página del repositorio, capturada el 2026-10-25).

Esta nota atomizada a partir de la sola `description` bilingüe queda **verificada en su parte operacional** por el README, que documenta lo que el átomo tenía como claim del autor:

- **Pool de cookies en base de datos**: confirmado literalmente — *"save the cookie as a database to realize the cookie pool call"*; los prerrequisitos exigen **MySQL >= 5.7** y el despliegue pasa por `SQL_NAME`, `SQL_PASSWORD`, `SQL_IP` y `SQL_DK` (3306). No hay modo en memoria ([[2026-1026-suno2openai-el-pool-de-cookies-exige-mysql-como-requisito]]).
- **Rotación de cookies**: confirmada como capacidad ya implementada — *"Multiple Cookie Management: Implements rotation of multiple cookies"*, con cuatro endpoints REST de administración del pool (`PUT`/`POST`/`DELETE` sobre `/<COOKIES_PREFIX>/cookies` y `GET` sobre `/<COOKIES_PREFIX>/refresh/cookies`) ([[2026-1026-suno2openai-cuatro-endpoints-de-gestion-de-cookies]]).
- **Integración con `newapi`/`oneapi` y adapters para `chat-next-web`**: la `description` china lo afirma y el README lo confirma como compatibilidad declarada con front-ends de chat, pero **no documenta cómo se configura la conexión a un relay** —ni URL, ni canal, ni tipo de modelo. Sigue siendo claim, ahora con detalle de contrato: el único endpoint de generación es `POST /v1/chat/completions` en formato OpenAI, con `model` de ejemplo `gpt-3.5-turbo` ([[2026-1026-suno2openai-el-contrato-publico-es-el-formato-de-chat-con-streaming]]).
- **Dato nuevo que el átomo no tenía**: la sección *Future Plans* incluye **"Introduce request queueing optimizations"**, es decir, **la rotación está implementada y la cola de peticiones no** ([[2026-1026-suno2openai-rotacion-de-cookies-declarada-sin-cola-de-peticiones]]).
- **Aprovisionamiento de la credencial**: el apartado *"How to get cookie"* es una captura de pantalla con la instrucción *"copy all content about the cookie"* — la credencial **se recoge a mano**, no se fabrica ni se compra ([[2026-1026-suno2openai-la-cookie-se-copia-a-mano-del-navegador]]).

=== END

=== EXTEND 2-atoms/2026-1026-github-search-suno-ventanas-de-desarrollo-largas-y-no-volcadas.md
## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio, 2026-10-25).

El átomo calculará las ventanas sobre `created_at`/`pushed_at` del JSON de la API de búsqueda. La página HTML del repositorio **confirma y afina** la cifra con datos que el JSON no expone:

- **464 commits**, **2 branches**, **4 tags**, último commit **19 de enero de 2025** (*"Enhance Suno API client with new notification and permission check features"*). El `pushed_at` que el átomo situaba el 2025-01-19 queda corroborado directamente por la cabecera del repo.
- **Dato nuevo: la guía de despliegue por `docker-compose` lleva su propia marca temporal — *"Update Time: 2024/4/7 18:18"* —, anterior al último commit.** Es decir, en este repo el README es **más viejo que el código**, al revés que en `midjourney-proxy` (README de agosto de 2025 sobre código congelado en junio de 2024). La regla operativa que se sigue: **un README auto-declarado con fecha hay que contrastarlo con `pushed_at` antes de tratarlo como procedimiento vigente** ([[2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija]]).
- **Ausencia de releases**: la sección *Releases* de la página está vacía, de modo que la distribución es **una imagen `wlhtea/suno2openai:latest` sin versión fijable** —a diferencia de `new-api`, donde el README sí obliga a fijar versión desde Releases ([[2026-1026-suno2openai-imagen-docker-sin-versionar-y-documentacion-fija]]).

=== END

=== EXTEND 2-atoms/2026-1024-github-search-watchers-count-de-la-api-es-copia-de-stargazers.md
## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio `wlhtea/Suno2openai`, 2026-10-25).

**Segundo caso empírico de la fricción, con distancia mayor.** La página web del repositorio muestra **275 stars** y **2 watching**, mientras que el `watchers_count` que devuelve la API de búsqueda para este mismo repo es **275**. Es el mismo patrón que el caso de `verssache/chatgpt-creator` (338/1), pero con una separación mucho mayor: **2 observadores frente a 275 estrellas**.

Esto refuerza la regla operativa del átomo —de la API de búsqueda solo son citable estrellas y forks— y añade una precisión: **el "2 watching" de la página web es el contador real de suscriptores**, y para este repo es prácticamente nulo, lo que dice algo sobre la base de usuarios real de un proyecto con 275 estrellas y 49 forks ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]).

=== END

=== EXTEND 2-atoms/2026-1026-github-search-suno-razon-forks-estrellas-0-18-contra-0-5.md
## Nota de extensión 2026-10-26
Fuente adicional: `sources/2026-10-25-suno2openai.md` (página del repositorio, 2026-10-25).

La razón 49/275 = 0,18 que el átomo calcula sobre el JSON queda **confirmada por la página HTML**, que muestra los mismos contadores (275 stars, 49 forks). El README añade la explicación operativa de por qué la estrella domina al fork: **el artefacto se despliega** —imagen de Docker Hub, `docker-compose`, `env.example`, `setup.py`, `start.sh`— y se consume desde un relay, no se modifica ([[2026-1026-suno2openai-metricas-de-la-pagina-464-commits-y-dos-watchers]]).

=== END
