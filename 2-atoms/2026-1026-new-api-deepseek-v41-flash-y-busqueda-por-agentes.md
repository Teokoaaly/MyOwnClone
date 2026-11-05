---
id: 2026-1026-new-api-deepseek-v41-flash-y-busqueda-por-agentes
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1026-new-api-busqueda-facturada-por-conteos-del-proveedor]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]"]
---

## Claim
**v1.0.0-rc.45** añade el soporte de **DeepSeek V4.1 Flash** (`deepseek-flash`) y de **`deepseek-v4-pro`**, con los sufijos **`-none`, `-low` y `-max`** y con los modificadores **`@thinking` y `@effort`** funcionando. La misma versión añade los endpoints de **Search** y **Fetch** en **`/v1/tools/search`** y **`/v1/tools/fetch`**: cuando **Claude Code o Codex** hacen que DeepSeek busque o abra una página, **se cobra $0.75 por 1.000 peticiones**.

## Why It Matters
El detalle de la facturación es lo que importa, y no el lanzamiento del modelo: **una herramienta de codificación puede provocar peticiones de búsqueda facturables sin que el usuario las pida**. El vault ya tiene el precedente de la conversión implícita en StepFun (~15 llamadas por prompt) ([[2026-1026-new-api-busqueda-facturada-por-conteos-del-proveedor]]), y aquí el caso es más limpio porque **la búsqueda es un endpoint del propio proveedor** y su precio es un número del changelog, no una estimación.
El otro ángulo es el de los **sufijos de esfuerzo** (`-none`, `-low`, `-max`, `@thinking`, `@effort`): el vault ya sabe que **"el nivel de razonamiento" es una palanca de coste** y que el gateway tiene que traducir esos modificadores al upstream correcto ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]). Que un proveedor chino exponga el mismo eje de esfuerzo que los proveedores occidentales es lo que hace comparables los precios de un producto de codificación: sin eso, un "0.2x" de un modelo con effort bajo **no** es comparable con un "0.2x" de un modelo con effort alto. Y con precios de lista como el **$0.75 por 1.000 peticiones de búsqueda**, el vault tiene ya **coste variable por uso de herramienta** documentado con fecha, que es el tipo de número que un producto de reventa necesita para cotizar un plan de codificación sin regalarlo ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
Y con esto el vault tiene ya un **precio de lista de búsqueda con fecha** ($0.75 por 1.000, 2026-10-25), que es un dato de coste que no aparece en ningún ranking de agregadores.
