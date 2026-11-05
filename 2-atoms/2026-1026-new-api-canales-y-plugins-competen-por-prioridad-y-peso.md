---
id: 2026-1026-new-api-canales-y-plugins-competen-por-prioridad-y-peso
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]"]
---

## Claim
**v1.0.0-rc.47** cambia el reparto de tráfico de los endpoints de **imagen, vídeo y Responses**: antes, cuando un modelo podía servirlo tanto un **canal ordinario** como un **plugin de tarea**, **todas las peticiones iban al plugin**; ahora **el canal se elige por prioridad y peso**, con el canal ordinario y el plugin compitiendo en la misma tabla. La **dirección propia del plugin** sigue yendo a ese plugin, y **canal ordinario y plugin usan precios separados**.

El propio release note avisa del hueco: si el precio del modelo está escrito **solo para el plugin de tarea**, el canal ordinario **devuelve un error de precio y no cobra**; hay que **fijar un precio aparte para el canal ordinario**.

## Why It Matters
Es la confirmación, en el changelog, de una regla que el vault solo tenía como **mención en el historial de commits**: el átomo de plugins ya recogía el commit *"let ordinary channels compete on shared plugin endpoints"*, pero sin cifras ni sin el efecto en la facturación. Aquí está el efecto completo: **el routing unificado no es solo selección de proveedor, es reparto de una misma facturable entre dos tipos de canal con dos tablas de precio**.
Eso tiene una consecuencia operativa dura para un relay: **un modelo puede quedar sin precio vendible** si el operador configura el precio del plugin y olvida el del canal ordinario — el canal ordinario **no cobra y falla**. Es un **fail-closed** correcto (no se cobra de más) pero un **fail-silent** desde el punto de vista de los ingresos: el tráfico se pierde, no se factura mal.
Y conecta con el eje de grupos ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]): al haber dos tablas de precio por tipo de canal, el **precio efectivo de un grupo** deja de ser un único número y pasa a ser una función del tipo de canal que gana el reparto por prioridad y peso ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]).
