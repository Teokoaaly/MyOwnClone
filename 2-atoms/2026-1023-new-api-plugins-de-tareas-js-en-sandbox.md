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


## Nota de extensión 2026-10-26
Este átomo describe el sandbox de plugins de tarea (JS en runtime limitado, el plugin declara hechos de uso y el gateway los acota) y lo conecta con la reversibilidad del soporte de proveedores. La captura de releases **cambia la arquitectura del sandbox y amplía su perímetro de forma medible**.

(1) **El runtime cambia y la interfaz no.** En **v1.0.0-rc.41** los plugins de tarea **pasan a ejecutarse sobre `moejs`**, con una **gran mejora de rendimiento** y **sin cambios en la API de plugins**; en **rc.42** las peticiones de task plugin son **substancialmente más rápidas**, incluidas las de tipo passthrough, y el **conteo de tokens es mucho más rápido** (también en texto largo sin puntuación) ([[2026-1026-new-api-plugins-de-tareas-sobre-moejs-y-conteo-de-tokens-mas-rapido]]). La lección de arquitectura es **desacoplar la parte que ejecuta código de terceros sin reescribir la interfaz**, el mismo objetivo que persiguen los módulos `relaykit` y `tokenkit` en el stack ([[2026-1023-new-api-stack-go-gin-react19-y-electron]]).

(2) **El perímetro de red aparece, y es declarativo pero con agenda propia.** En **rc.43** los plugins pueden llamar a **`utils.fetch`** en los hooks de submit, query y descarga de contenido; alcanza la **Base URL del canal** y **los dominios de request adicionales que el plugin declara**, y el diálogo de subida lista esos dominios. En paralelo, **`utils.json.clone` y `parseSubmitEventDelta` se pueden usar sin declarar capacidad**, y los plugins que declaran **`json-clone@1`** o **`submit-sse-delta@1`** siguen cargando ([[2026-1026-new-api-utils-fetch-y-dominios-declarados]]). La observación para el vault es incómoda y valiosa: **cada capacidad que el sandbox obtiene sin declaración reduce el valor de la declaración**. Un producto que autoaloje plugins debería tratar la lista de capacidades como **API pública con versionado y changelog**.

(3) **El plugin de tarea ve cabeceras del cliente, y hay una frontera explícita.** En **rc.47** los task plugins **pueden leer las cabeceras de la petición del cliente**, pero **`Authorization` y `Cookie` no se entregan al plugin**; la misma versión añade **subida de ficheros en las rutas propias del plugin** ([[2026-1026-new-api-plugins-leen-cabeceras-del-cliente-sin-authorization-ni-cookie]]). Es una **frontera de confianza bien puesta** —el plugin necesita el contexto de la petición para reenviarlo, pero no la credencial— y por tanto un buen patrón para el producto del vault.

(4) **La noticia que el átomo no tenía: los plugins de tarea ahora compiten con los canales ordinarios** por prioridad y peso, con **precios separados** ([[2026-1026-new-api-canales-y-plugins-competen-por-prioridad-y-peso]]). Es decir, el plugin de tarea deja de ser un caso especial y pasa a ser **un canal más** del sistema de reparto, lo que refuerza la lectura de reversibilidad: cambiar de proveedor en una capacidad concreta no toca el núcleo porque el soporte está en el plugin, pero **el plugin entra en la misma economía de prioridad, peso y precio** que el resto.

(5) Y hay un movimiento de precio que el átomo no anticipaba: en **rc.42** el soporte de **orden de campos JSON (`json-order@1`)** es una capacidad opcional, y en **rc.41** los **precios ya guardados siguen siendo editables aunque el task plugin haya reducido su conjunto de hechos de uso** ([[2026-1026-new-api-imagenes-seedream-por-task-plugin-y-tarificacion-por-tiers]]). Un motor de precios donde cambiar la definición de un perfil de uso invalida los precios cobrados sería un motor que obliga a reescribir la tabla cada vez que el upstream cambia su API; que no lo haga es una propiedad de confianza, y el vault la necesita ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
