---
id: 2026-1026-new-api-uso-en-stream-y-costo-de-generaciones-completadas
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-usage-claude-cero-y-prompt-completo-en-cache]]"]
---

## Claim
Dos correcciones de contabilidad en **v1.0.0-rc.42**:

1. El **uso del stream de Gemini ya no se multiplica por el número de frames** (PR #7687).
2. Las **generaciones de imagen ya completadas se siguen cobrando** aunque la petición de Responses **falle o se cancele** después.

## Why It Matters
La primera es un **error de multiplicación en la facturación**: si el uso de un stream de Gemini se multiplicaba por el número de frames, el gateway **facturaba varias veces la misma llamada** al proveedor de vídeo. Es un error de escala, no de detalle: el factor puede ser de 2 a 10, y el error va **contra el operador** (sobrevfacturación al cliente) o **a su favor** (fuga de margen) según el signo con el que el motor lo aplicase. El vault ya tiene un precedente del mismo tipo con la conversión implícita de StepFun (~15 llamadas por prompt) ([[2026-1026-new-api-busqueda-facturada-por-conteos-del-proveedor]]).
La segunda es una regla de **fail-closed del lado del coste**: el trabajo ya se hizo y ya lo pagó el operador al upstream, así que **se cobra igual**. Es la misma lógica del reintento que pre-autoriza la diferencia ([[2026-1026-new-api-reintento-de-tarea-reserva-el-sobrante-y-no-sale-si-no-alcanza]]): el principio de que **el coste ya incurrido no se pierde porque el cliente cancele**.
Y para el producto del vault hay un efecto directo sobre el **precio de lista**: si el motor de precios del gateway tiene un error de multiplicación, **todo el catálogo de precios queda mal calibrado en la misma proporción** ([[2026-1023-new-api-precios-por-ratio-y-expresion]]). Por eso estas correcciones no son "chores": son la condición para que un multiplicador declarado sea defendible.
Y hay una lectura de negocio que importa para un producto de reventa: la combinación de "**el uso en streaming se corrige**" y "**el 0 del upstream se respeta**" ([[2026-1026-new-api-usage-claude-cero-y-prompt-completo-en-cache]]) indica que en esta versión **la facturación del streaming se está alineando con la realidad medible**. Eso es exactamente lo que hace que un multiplicador declarado como 0,05x sea **defendible ante un cliente que audita** ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
