---
id: 2026-1026-new-api-plugins-de-tareas-sobre-moejs-y-conteo-de-tokens-mas-rapido
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]", "[[2026-1023-new-api-stack-go-gin-react19-y-electron]]"]
---

## Claim
Dos cambios de rendimiento en versiones consecutivas:

- **rc.41**: los **plugins de tarea pasan a ejecutarse sobre `moejs`**, con una **gran mejora de rendimiento**; la **interfaz de plugin no cambia**.
- **rc.42**: las peticiones de **task plugin** son **substancialmente más rápidas**, incluidas las de tipo passthrough; y el **conteo de tokens es mucho más rápido**, incluido el **texto largo sin puntuación**.

## Why It Matters
El cambio de runtime de los plugins es una pieza de arquitectura que el vault no tenía: el sandbox de plugins deja de ser un intérprete de JS embarcado en el proceso Go y pasa a ser **otro runtime**, sin que la API cambie. Es un patrón de **desacoplar la parte que ejecuta código de terceros sin reescribir la interfaz** — el mismo objetivo que persiguen los módulos independientes `relaykit` y `tokenkit` ([[2026-1023-new-api-stack-go-gin-react19-y-electron]]).
Y la mejora del **conteo de tokens** no es trivial: es la parte del sistema que más CPU consume en tráfico de agentes, porque el estimador tiene que contar tools, esquemas y bloques `tool_use` de Claude, y hasta ahora devolvía estimaciones **31–93 % bajas** frente al uso real medido en 54 conversaciones reales ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]). Un contador más rápido y más preciso es **margen no fugado**, y es la diferencia entre un multiplicador 0.05x "honesto" y uno "truncado" ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]).
La lección para el vault: **la rendimiento de la capa de medición es una decisión de negocio**. En un gateway de reventa, cada milisegundo de conteo es latencia que el cliente final paga y cada punto de desvio es margen.
