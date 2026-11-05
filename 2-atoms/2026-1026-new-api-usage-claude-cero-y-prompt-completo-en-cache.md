---
id: 2026-1026-new-api-usage-claude-cero-y-prompt-completo-en-cache
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1026-new-api-cache-claude-escritura-no-dividida-se-cobra-como-5-minutos]]"]
---

## Claim
**v1.0.0-rc.45** corrige dos reglas de facturación de Claude:

1. **El 0 que reporta el upstream ya no se descarta**: en un stream de Claude, si el upstream informa **0 tokens**, se cobra **0** (PR #7816, `paopaoandlingyia`).
2. **Si todo el prompt está en caché, la llamada se cobra al precio de lectura de caché**, no al de entrada.

## Why It Matters
La primera corrección es un **fail-safe de facturación**: descartar el 0 del upstream significaba, en la práctica, **cobrar de más** (o de menos, según el motor) en un caso límite; ahora el valor reportado es el que manda. El patrón general del changelog de esta captura es **dejar de normalizar a cero los valores que el upstream reporta** — el mismo criterio que se ve en el arreglo de los campos de usage del streaming ([[2026-1023-new-api-tokenkit-conteo-de-tokens-calibrado]]).
La segunda es la que el vault debe leer con más cuidado: **"el prompt entero está en caché"** es exactamente el caso de un agente de código que repite el mismo contexto en cada turno. En ese caso el gateway **no cobra entrada**, cobra **lectura de caché**. Es la regla que convierte la caché de 12 h en un ingreso recurring en lugar de un coste, y conecta con el orden de cobro de las escrituras de Claude no divididas ([[2026-1026-new-api-cache-claude-escritura-no-dividida-se-cobra-como-5-minutos]]).
El riesgo para un producto de reventa es de **coste**, no de ingreso: si el relay **no aplica** esta regla, cobra la entrada completa de un prompt que el proveedor le da casi gratis; si la aplica mal, **regala margen** en el único escenario de alto volumen. Con una tabla de precios de 0,05x, **la diferencia entre las dos reglas puede ser la diferencia entre profit y pérdida** ([[2026-1023-new-api-precios-por-ratio-y-expresion]]).
