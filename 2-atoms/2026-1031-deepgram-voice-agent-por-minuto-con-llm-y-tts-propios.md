---
id: 2026-1031-deepgram-voice-agent-por-minuto-con-llm-y-tts-propios
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1022-myclone-voice-clone]]", "[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]"]
---

## Claim
El producto **Voice Agent** de Deepgram se factura por **minuto de conexión WebSocket** con una tarifa única que cubre STT + LLM gestionado + TTS, y bajarla es cuestión de traer los componentes uno a uno: "Standard" $0,075/min (Growth $0,068), "Standard, BYO TTS" $0,065/min (Growth $0,051), "Custom, BYO LLM" $0,065/min (Growth $0,059), "Custom, BYO LLM and TTS" **$0,050/min** (Growth $0,041), "Advanced" $0,163/min (Growth $0,146) y "Advanced, BYO TTS" $0,122/min (Growth $0,110).

## Why It Matters
Es el modelo de precio que más se parece al objetivo de MyOwnClone: **una tarifa por minuto de conversación** que incluye todo el stack de voz, y en la que el cliente puede descontar ~33 % (de $0,075 a $0,050)traendo su propio LLM y su propio TTS. Con BYO TTS el Growth baja a $0,051/min — **$3,06/hr**, un orden de magnitud por encima de la transcripción pura ($0,46/hr), porque el precio real de un clon de voz en vivo está en la TTS y el LLM, no en el reconocimiento. Eso conecta directamente con la decisión ya documentada en [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]: el proveedor de STT es un coste marginal frente a la elección de TTS, y la cifra de $0,050/min con BYO LLM+TTS es el suelo real que hay que comparar con el coste de montar ese pipeline a mano en Flask + Next.js.

## [FRICTION]
> La página ofrece un conmutador de unidad "per minute | **per hour**" sobre la tabla de Voice Agent, pero **la captura no muestra la columna por hora**: todas las cifras están en $/min. Multiplicando por 60, el "Standard" da $4,50/hr y el mínimo BYO LLM+TTS $3,00/hr.
> No se puede saber si la vista por hora que Deepgram ofrece para Voice Agent es la misma tarifa expresada en horas o una tarifa distinta (por ejemplo, por hora de *tiempo de sesión* en lugar de conexión). Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: las seis filas de Voice Agent son idénticas ($0,075 / $0,065 / $0,065 / $0,050 / $0,163 / $0,122 pay-as-you-go y $0,068 / $0,051 / $0,059 / $0,041 / $0,146 / $0,110 en Growth). El pie de la tabla pasa a llevar el dato de concurrencia que hasta ahora solo estaba en la FAQ: "Calculated on WebSocket connection time. Concurrency limits apply per project and differ by plan and region. On Growth, Voice Agent concurrency is up to 60 in North America and up to 45 in Europe, Australia, and India." El conmutador "per minute | per hour" sigue presente y la captura **sigue sin publicar la columna por hora**, de modo que la fricción de unidades de este átomo se mantiene abierta.
