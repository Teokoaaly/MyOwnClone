---
id: 2026-1026-new-api-utils-fetch-y-dominios-declarados
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1026-new-api-plugins-leen-cabeceras-del-cliente-sin-authorization-ni-cookie]]", "[[2026-1026-new-api-cve-2026-111943-corregido-con-go-1-26-10]]"]
---

## Claim
**v1.0.0-rc.43** da a los **plugins de tarea** una API de red: **`utils.fetch`**, invocable en los hooks de **submit, query y descarga de contenido**. Alcanza el **Base URL del canal** y **los dominios de request adicionales que el plugin declara**; el diálogo de subida **lista esos dominios**, y el documento **Task Plugin API v1** enumera hooks y límites.

La misma versión abre la puerta a **capacidades sin declarar**: los plugins pueden llamar a `utils.json.clone` y exportar `parseSubmitEventDelta` **sin declaración de capacidad**; los que declaran `json-clone@1` o `submit-sse-delta@1` **siguen cargando**. En **rc.42** se había añadido la capacidad `json-order@1` para preservar el orden de campos JSON del cliente.

## Why It Matters
Es la historia del **modelo de capacidades** del sandbox de plugins, y el vault ya lo tenía solo en su versión más básica: el plugin declara sus hechos de uso y el gateway los acota ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]). Aquí aparece la otra mitad: **el plugin también puede salir a la red**, y el perímetro de esa salida es **declarativo** (el plugin declara dominios; el diálogo de subida los muestra).
Eso es bueno y es un riesgo, y la lección para el vault es de **superficie**: un plugin de tareas es **código de terceros con salida a red y con lectura de cabeceras del cliente** ([[2026-1026-new-api-plugins-leen-cabeceras-del-cliente-sin-authorization-ni-cookie]]), y el gateway lo ejecuta en el mismo proceso que maneja claves upstream y sesiones. La lista de capacidades sin declarar (`utils.json.clone`, `parseSubmitEventDelta`) muestra además que **el perímetro no es fijo**: se amplía por versiones, y cada ampliación es una decisión de confianza. Es el riesgo que ya está registrado para el gateway unificado: **más superficie de protocolo significa más superficie de confianza** ([[2026-1023-new-api-una-sola-api-multiproto]]).
La lección operativa: **cada capacidad que un sandbox obtiene sin declaración reduce el valor de la declaración**. Un producto del vault que autoaloje plugins debería tratar la lista de capacidades como **API pública con versionado y changelog**, no como detalle interno.
