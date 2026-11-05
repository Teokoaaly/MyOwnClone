---
id: 2026-1026-veridrop-deteccion-contexto-completo-modelo
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-probedor-contexto-ventana]]", "[[2026-1026-veridrop-profundidades-deteccion]]"]
---

## Claim
Veridrop realiza detección de contexto completo probeando el límite del contexto del modelo por factores: para un modelo de 1M de tokens, la prueba sigue la progresión 32k → 500k → 950k. Esto detecta fraudes de "anunciar 1M pero entregar solo 200k", que el modo estándar no puede atrapar. El costo varía según el modelo y la precisión del pricing del relay.

## Why It Matters
Esta es la única forma de atrapar relays de nivel empresarial que anuncian contextos enormes pero los reducen silenciosamente. Sin esta prueba, un usuario no tendría manera de saber si está pagando por un modelo de 1M context cuando solo recibe 200k-300k efectivos. Es crítica para cualquier carga de trabajo que dependa de largo contexto pero no quiera pagar precios de modelo de 1M tokens.

## [FRICTION]
> [[2026-1027-veridrop-pesos-de-los-11-detectores-y-el-contexto-largo-de-pago]] (escrita hace ~5 semanas) discute los pesos/costos de los 11 detectores y cómo el contexto largo se factura por separado. Este átomo (2026-1026) coincide en que el costo del contexto largo es una magnitud separada, pero contradece en la conclusión sobre "estándar imposible de detectar": la fuente original (capture 2026-10-26) dice "estándar completo testea 6 items, no alcanza para detectar fraudes de contexto anunciado", mientras que la nota de 2026-1027 dice que el modo estándar "completo totalmente testea" y el modo extremo es el que detecta estas fraudes. La captura original (2026-10-26) es más conservadora: el modo estándar no detecta estas fraudes, solo el modo extremo/límite lo hace. Esta nota (2026-1026) mantiene lealtad al texto de la capture y la de 2026-1027 amplía con casos de uso adicionales. No hay contradicción auto-resuelta: la capture define el alcance mínimo, la nota posterior define casos de uso ampliados.