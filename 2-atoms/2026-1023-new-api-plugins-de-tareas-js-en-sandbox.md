---
id: 2026-1023-new-api-plugins-de-tareas-js-en-sandbox
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]"]
---

## Claim
Las **tareas asíncronas** (imagen, vídeo y otros) se extienden en New API mediante **plugins JavaScript**: el directorio `plugins/tasks/` con la **Task Plugin API v1**, y endpoints genéricos `POST /v1/tasks/{pluginKey}` y `GET /v1/tasks/{taskId}`. El commit *"feat(task): replace built-in task adaptors with a sandboxed JS plugin system (#7076)"* (29 de agosto de 2026) documenta la sustitución de los adaptadores de tarea integrados por un sistema de plugins en sandbox.

Dos reglas de governance del mismo historial tienen peso de negocio:
- **Cada plugin valida su propia request y deriva sus propios hechos de uso**: *"The gateway no longer reads billing quantities from the request"*; el gateway solo acota los hechos que el plugin devuelve (segundos ≤ 3600, contadores ≤ 128, tokens y créditos saturados en el límite de cuota).
- **Los precios de plugin y los ordinarios se mantienen separados**: las expresiones de tarea devuelven USD, las ordinarias USD-por-millón, y *"an ordinary request now fails with 400 model_price_error before any quota is reserved"* si la expresión del modelo lee uso de tarea `u()`.

Además, desde el commit *"let ordinary channels compete on shared plugin endpoints"*, un canal ordinario y un canal de plugin **compiten** por la misma request bajo las reglas habituales de grupo, prioridad, peso, afinidad y pin de canal.

## Why It Matters
Es el patrón de **extensibilidad de un gateway comercial**: los proveedores no están en el core, se añaden como plugins, y el core se queda con el routing, la facturación y el control de cuota. El vault ya vio este mismo movimiento en el otro lado: `new-api` aparecía en el README de Midjourney-Proxy como "sistema de gestión y distribución de interfaces que se conecta a MidJourney Proxy" ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]), es decir, el plugin se apoya en otro proyecto abierto y luego se reparte.
La regla de **"el plugin declara sus propios hechos de uso y el gateway los acota"** es la lección de seguridad que el vault debe heredar: un componente externo no decide cuánto cobra, pero tampoco puede reportar cifras arbitrarias — hay un techo por magnitud y por cuota.
Y la separación de precios plugin/ordinarios, con error explícito `400 model_price_error` antes de reservar cuota, es un patrón de **fail-closed**: es preferible rechazar la request a facturar mal.
