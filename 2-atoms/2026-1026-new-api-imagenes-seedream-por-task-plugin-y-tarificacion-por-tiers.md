---
id: 2026-1026-new-api-imagenes-seedream-por-task-plugin-y-tarificacion-por-tiers
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1026-new-api-facturacion-de-video-por-duracion-y-resolucion-reportadas]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]"]
---

## Claim
**v1.0.0-rc.41** mueve las **imágenes de Doubao Seedream** a las rutas **OpenAI Images del task plugin** (`/v1/images/generations` y `/v1/images/edits`), añade **Seedream 5.0 Flash** y establece que **cada modelo se tarifa por sus propios tiers**. Además, **los precios ya guardados siguen siendo editables** aunque el task plugin haya **reducido su conjunto de hechos de uso** ("narrows its usage facts"), y la **configuración de precios permanece editable** cuando un perfil de uso pierde hechos. En **rc.42** los plugins que declaran **`json-order@1`** conservan **el orden de los campos JSON del cliente** hasta el upstream.

## Why It Matters
Es el mismo movimiento que ya se había visto en vídeo: **una familia de modelos entra en el sistema por el protocolo OpenAI Images y se tarifa por tiers propios**. El efecto para el vault es que **la granularidad de precio del stack aumenta**: ya no hay "un precio para las imágenes de Seedream" sino **un precio por modelo y por tier**, lo que se parece a la lógica de "grupos como eje de precio" que el vault había hypothesized ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]) pero es un eje distinto: **modelo y tier**, no grupo.
El detalle fino que importa es la **estabilidad de los precios guardados** cuando el plugin reduce sus hechos de uso: un motor de precios donde **cambiar la definición de un usage profile invalida los precios ya cobrados** es un motor que obliga a reescribir la tabla cada vez que el upstream cambia su API. El release note tranquiliza: **los precios que quedan, quedan**. Es una propiedad de confianza, y el vault la necesita para su propio modelo de precios ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
Y `json-order@1` es una **capacidad declarada** que preserva el orden de campos: el mismo patrón de **capabilities con nombre y versión** que ya se había visto con `utils.fetch` y los dominios declarados ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]).
