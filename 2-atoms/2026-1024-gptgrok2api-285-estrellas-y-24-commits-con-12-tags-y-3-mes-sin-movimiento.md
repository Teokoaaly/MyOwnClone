---
id: 2026-1024-gptgrok2api-285-estrellas-y-24-commits-con-12-tags-y-3-mes-sin-movimiento
type: atom
certainty: solid
sources: [sources/2026-10-24-gptgrok2api.md]
links: ["[[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]", "[[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]", "[[2026-1024-gptgrok2api-gateway-unificado-gpt-y-grok-en-api-compatible]]"]
---

## Claim
Los metadatos del repositorio, tal como los renderiza GitHub en la captura: **285 estrellas, 145 forks, 3 watchers**, **1 rama, 12 tags, 24 commits**, licencia **MIT** (GitHub muestra "MIT, MIT licenses found", por los dos ficheros `LICENSE` y `GROK2API_LICENSE`), **sin releases listadas y sin packages**, y topics: `ai-gateway`, `chatgpt`, `docker-compose`, `gpt-image`, `grok`, `grok-api`, `oauth`, `openai-api`, `vue3-typescript`. El último commit es **"Release v1.2.1" del 27 de julio de 2026**, tres meses antes de la captura, y la línea temporal de commits va del 15 de julio (release inicial v1.0.1, con el mensaje "Initial release: GPTGrok2API v1.0.1 — Clean project history owned by AuuCoder") al 27 de julio. El README declara que el proyecto es un **desarrollo secundario (segunda versión, "er kai") de `yukkcat/chatgpt2api`** y que "las licencias y las declaraciones de origen deben conservarse con el contenido distribuido". La comparación con el otro bot ya atomizado es el dato: **145 forks sobre 24 commits**, frente a **90 forks sobre 4 commits** de `verssache/chatgpt-creator`.

## Why It Matters
El vault ya tiene el patrón registrado dos veces —**popularidad sin mantenimiento** — y este repo es el caso más favorable: 285 estrellas y 145 forks son la escala de un proyecto con comunidad real, pero **los 145 forks se han producido sobre una ventana de actividad de 12 días** (15 a 27 de julio de 2026) y **no hay actividad desde entonces**. Es decir, el fork parece ser la vía de consumo real: la gente clona y despliega, y el upstream deja de moverse. El vault ya vio esa dinámica en el bot de Go ([[2026-1024-chatgpt-creator-cuatro-commits-y-338-estars-sin-mantenimiento-visible]]) y en Midjourney-Proxy ([[2026-1023-midjourney-proxy-popularidad-y-actividad-del-repo]]); aquí la diferencia es que **el proyecto tiene releases con tag, CHANGELOG, `VERSION` y un `RELEASE_NOTES.md`**, y que su "release" es literalmente un commit con tag, sin artefactos publicados en la sección Releases de GitHub.
El detalle de la **historia de commits limpia** —"Clean project history owned by AuuCoder"— es un dato que el vault debe registrar por lo que implica: **un repositorio que declara haber reescrito o reiniciado su historial no permite auditar su linaje por `git log`**, sino solo por la declaración de descendencia de `yukkcat/chatgpt2api` y por la coexistencia de dos ficheros de licencia. Es un patrón de **trazabilidad de licencia partida**: `LICENSE` para lo propio y `GROK2API_LICENSE` para lo heredado.
Para el vault, la conclusión operativa no cambia (el producto no debe depender de estos repos sin proveedor de servicio), pero sí el **modo de consumo**: aquí existe `docker compose up -d --build` con imagen y despliegue documentados, lo que lo hace **más fácil de adoptar y más fácil de quedar abandonado**.

## Nota de verificación
Cifras de estrellas, forks, watchers, ramas, tags y commits son metadatos renderizados por GitHub en la captura. La captura **no** publica: la fecha de creación del repositorio, la distribución de estrellas en el tiempo, ni si los 145 forks tienen actividad propia. El vault no ha clonado el repositorio.
