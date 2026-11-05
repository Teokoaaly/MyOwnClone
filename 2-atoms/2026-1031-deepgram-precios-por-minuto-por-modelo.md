---
id: 2026-1031-deepgram-precios-por-minuto-por-modelo
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-pricing]]", "[[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]]", "[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]"]
---

## Claim
Deepgram publica su Speech-to-Text **por minuto de audio**, con cuatro tarifas "Pay as you go" distintas según modelo e idioma: **Flux STT English $0,0077/min**, **Flux STT Multilingual $0,0078/min**, **Nova-3 Monolingual $0,0077/min** y **Nova-3 Multilingual $0,0092/min**; las columnas "Growth" bajan a $0,0065, $0,0068, $0,0065 y $0,0078 respectivamente. La columna Enterprise queda como "Contact sales" en todas las filas.

## Why It Matters
Es la tabla que convierte la unidad $/min del vault en cifras comparables con AssemblyAI: multiplicando por 60, el monolingual pay-as-you-go queda en **$0,462/hr** y el multilingüe de Nova-3 en **$0,552/hr**, que es exactamente lo que la FAQ de Deepgram declara en $/hr ("$0.46 an hour… $0.55"), de modo que la página es internamente coherente. La comparación de [[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]] queda así anclada en una cifra de lista, no en una estimación: Deepgram es **~3,1× más caro** que el streaming AssemblyAI de $0,15/hr en monolingual, y solo equiparable en multilingüe de calidad ($0,45/hr AssemblyAI frente a $0,55/hr Nova-3 multilingüe). Para MyOwnClone esto importa en el reparto de costes: la transcripción no es una partida marginal del techo de ≤ €4/mes de [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]], y el multilingüe —imprescindible para los clones con voz en varios idiomas— es la tarifa más cara del catálogo.

## [FRICTION]
> La FAQ de la misma página afirma "Pre-recorded runs lower" y el propio producto ofrece un conmutador "Streaming | Pre-recorded" en la tabla, pero la captura no publica **ninguna cifra de pre-recorded separada**: ambas pestañas comparten el mismo renderizado de tabla. Es decir, la afirmación "el pre-recorded es más barato" no es verificable con las cifras publicadas — ver [[2026-1031-deepgram-prerecorded-mas-barrio-pero-sin-cifra-publicada]].
> Ambas no pueden ser simultáneamente la tabla completa y una lista de precios auditables: o la captura se quedó en la pestaña "Streaming", o Deepgram factura igual en ambas modalidades. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura consecutiva de `deepgram.com/pricing`. La tabla de Speech-to-Text reproduce **exactamente** las mismas cuatro tarifas y la misma columna Growth ($0,0077 / $0,0078 / $0,0077 / $0,0092 pay-as-you-go; $0,0065 / $0,0068 / $0,0065 / $0,0078 en Growth) y la columna Enterprise sigue en "Contact sales" en todas las filas. La FAQ repite los mismos valores en $/hr: "Monolingual streaming is $0.46 an hour on Pay as you go, for either Nova-3 or Flux STT, and $0.39 on Growth. Multilingual is $0.55 for Nova-3 and $0.47 for Flux STT. Pre-recorded runs lower." Lo que **no** cambia es el hueco: sigue sin publicarse ninguna cifra de pre-recorded, ni siquiera en esta cuarta versión de la página. La inestabilidad de la captura es de superficie, no de precio — ver [[2026-1103-deepgram-precios-estables-en-cuatro-capturas-consecutivas]].
