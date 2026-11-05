---
id: 2026-1101-deepgram-concurrencia-y-regiones-por-plan
type: atom
certainty: solid
sources: [sources/2026-11-01-deepgram-pricing.md, sources/2026-11-02-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10]]", "[[2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
Deepgram aplica **límites de concurrencia por proyecto** que dependen del plan y de la región: para streaming de Speech-to-Text, **Pay as you go permite 150 conexiones concurrentes y Growth 225** ("Requests beyond your limit are queued or rejected"), mientras que para **Voice Agent en Growth el límite es de hasta 60 en Norteamérica y hasta 45 en Europa, Australia e India**. Enterprise los fija "to your peak traffic".

## Why It Matters
El dato europeo es el que toca al vault, porque MyOwnClone opera en la UE ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): con Growth, un clon de voz en vivo en la UE tiene **45 sesiones simultáneas** como techo, frente a 60 en Norteamérica. Para una plataforma multi-tenant, ese 45 es un **techo de capacidad por plataforma, no por tenant** — y a diferencia de AssemblyAI, cuyo límite documentado es de 100 sesiones de streaming por minuto ([[2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto]]), el de Deepgram se expresa en conexiones simultáneas, que es un número mucho más restrictivo para un producto con muchos tenants pequeños: 45 conexiones = 45 llamadas de voz a la vez en toda la plataforma. La comparación de límites de concurrencia entre proveedores no es equivalente porque las unidades no lo son, y hay que decirlo antes de usar estos números en un dimensionamiento.

## [FRICTION]
> La página ofrece un conmutador "per minute | **per hour**" en la tabla de Voice Agent, pero la captura solo muestra la columna por minuto. La FAQ de concurrencia (150/225) habla de "concurrent streaming speech-to-text **connections**", mientras que el límite de Voice Agent se expresa en sesiones por región. No hay forma de saber si el conmutador por hora aplica una tarifa distinta o solo reformatea la misma.
> Ambas vistas no pueden estar igualmente disponibles con la misma granularidad: o la columna por hora es una simple conversión de la de minutos, o falta un tramo de pricing real por hora de sesión. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: los límites de concurrencia se repiten sin variación — "Pay as you go allows 150 concurrent streaming speech-to-text connections and Growth 225" y "On Growth, Voice Agent concurrency is up to 60 in North America and up to 45 in Europe, Australia, and India". Novedad de esta captura: el dato de concurrencia de Voice Agent **deja de estar solo en la FAQ** y pasa a figurar también en el pie de la tabla de Voice Agent, junto con la advertencia "Concurrency limits apply per project and differ by plan and region". La fricción de este átomo —el conmutador "per minute | per hour" sin columna por hora publicada— sigue abierta: la captura solo muestra la columna por minuto.
