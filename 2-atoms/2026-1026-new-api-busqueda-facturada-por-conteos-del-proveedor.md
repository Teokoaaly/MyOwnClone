---
id: 2026-1026-new-api-busqueda-facturada-por-conteos-del-proveedor
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-priceai-stepfun-step-plan-prompts-y-llamadas]]"]
---

## Claim
**v1.0.0-rc.42** rehace la **facturación de la función de búsqueda**: los canales pueden **codificar la búsqueda web según la forma del propio upstream**, y la liquidación se hace **con los recuentos de búsqueda que reporta el proveedor** (*"vendor-reported search counts"*). El mecanismo es por canal: cada canal codifica su búsqueda y se liquida con lo que su proveedor devuelve.

En **rc.45** aparece la versión de DeepSeek: se añaden los endpoints **`/v1/tools/search`** y **`/v1/tools/fetch`**, y cuando **Claude Code o Codex** hacen que DeepSeek busque o abra una página, **se cobra por peticiones a $0.75 por 1.000** — un precio por número de peticiones, no por token.

## Why It Matters
Es el caso más claro del vault de **unidad de precio que no es token**: la búsqueda se factura **por recuentos reportados por el proveedor**, es decir, **la cantidad la declara el upstream, no el gateway ni el cliente**. Eso es una cesión de autoridad en la medición, y por tanto un riesgo de ingreso que el vault ya tiene abierto en general: cuando el multiplicador se aplica sobre una base declarada por otro ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]).
El dato duro es que **el precio por 1.000 peticiones de búsqueda es de $0.75**, y que **los agentes de código lo consumen de forma nativa**: si Claude Code o Codex pueden pedir búsqueda a DeepSeek, esa búsqueda entra en el coste del producto sin que el usuario final la pidiera explícitamente. Es exactamente el tipo de consumo **invisible** que un producto de marca blanca debe poder mostrar en su facturación, y el motor de precios del gateway ya lo soporta con precios por número de peticiones ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
La lección de método: para comparar coste real entre herramientas de codificación hay que **añadir el coste de búsqueda del proveedor al coste del modelo**, porque el agente lo provoca por su cuenta — el mismo problema de conversión implícita que ya está catalogado para StepFun ([[2026-1023-priceai-stepfun-step-plan-prompts-y-llamadas]]).
