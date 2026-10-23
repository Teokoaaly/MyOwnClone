---
id: 2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-new-api-stack-go-gin-react19-y-electron]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]"]
---

## Claim
El historial de commits de la página documenta el módulo **`tokenkit`**, nacido de un problema de contabilidad: *"Token estimates badly undercounted agent requests"*. Concretamente, las definiciones de tools de Claude, las function calls de Responses y sus salidas, las tool calls de Chat y las instrucciones/function calls/tools de Gemini **nunca llegaban al contador**; los schemas de tools de Chat se contaban como sintaxis de mapa de Go y los resultados de tools de Claude como JSON escapado. Medido contra el uso real de **54 ventanas de conversación reales de Claude Code y Codex**, las estimaciones nativas de prompt eran **31–93 % bajas**, y los fallbacks de completion de Claude y Gemini **≈90 % bajos** porque las tool calls en streaming no se contaban.

El arreglo: el fallback cuenta ahora nombres y argumentos de tools **más 40 tokens por bloque `tool_use` de Claude**; los pesos del estimador se **reajustan por tokenizer** (Claude antes de Opus 4.7, Claude 4.7+ que usa ~30 % más tokens, GPT, Gemini); el resultado es **≤1 % de sesgo y 3–4 % de error medio** por familia. Además sustituye la estimación plana de **520 tokens por imagen** por las reglas de dimensionado de cada proveedor (patch/tile de OpenAI por modelo y nivel de detalle, dos niveles de resolución en Claude, media resolution de Gemini 3 y tiles de Gemini 2.x). `tokenkit` es, como `relaykit`, un **módulo independiente** para que otros gateways lo usen.

## Why It Matters
Es el **error de medición del que dependen todos los precios del sector**: si el conteo de tokens se desviaba un 31–93 % en tráfico de agentes, cualquier multiplicador RELATIVO al precio oficial heredaba ese error. Es decir, un relay que cobra 0.05x podría estar cobrando 0.05x de una base mal medida — y el desajuste no se ve comparando multiplicadores entre canales, sino comparando con el upstream.
Para el vault, que ya tiene el problema de unidades heterogéneas abierto (requests, prompts, credits, dólares ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]])), esto añade la pieza que faltaba: **la normalización por tokens es en sí misma un producto**, con su propio módulo y su propio modelo de error, y es donde un gateway puede vender un 0.05x "honesto" o un 0.05x "truncado".
El dato de las 54 ventanas reales es método, no marketing: es la clase de verificación que el vault no puede hacer con fuentes de precio declarativo.

## [FRICTION]
> [[2026-1023-priceai-transit-dispersion-de-multiplicadores]] usa el multiplicador como **comparador entre canales** (de 0.01x a 7.00x en la misma familia de modelos) y concluye que el multiplicador es "una variable de negocio con dispersión real", no marketing.
> Este átomo presiona esa creencia en un punto: **el multiplicador se aplica a una base de medición que, en tráfico de agentes, estaba desviada hasta un 31–93 %** — y el desvío depende del tráfico de cada canal. Dos canales con el mismo software, el mismo modelo y multiplicadores 0.05x y 0.10x **no son necesariamente comparables** si uno sirve tráfico de codificación con tools y el otro chat corto: la diferencia puede ser el error del contador, no el margen.
> Ambas no pueden ser completamente correctas en su lectura general: o el multiplicador es comparable porque todos los despliegues miden igual (y entonces el error de conteo es uniforme y no afecta al ranking relativo), o cada despliegue mide con su propio sesgo y la dispersión observada mezcla margen y error de medición. Marcado para juicio humano, no auto-resuelto: la fuente no dice qué versión de `tokenkit` usa cada canal del ranking, ni si los multiplicadores se aplican sobre el conteo estimado o sobre el uso real reportado por el upstream.
