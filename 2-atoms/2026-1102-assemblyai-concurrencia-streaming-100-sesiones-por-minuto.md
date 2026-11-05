---
id: 2026-1102-assemblyai-concurrencia-streaming-100-sesiones-por-minuto
type: atom
certainty: solid
sources: [sources/2026-11-02-assemblyai-pricing.md]
links: ["[[2026-1022-gap-voz-en-vivo-myownclone]]", "[[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El Realtime/Streaming API de AssemblyAI escala su concurrencia **sin coste y sin techo**, con umbrales explícitos: en plan gratuito se pueden abrir **5 conexiones nuevas de streaming por minuto**; en pay-as-you-go el límite de partida es **100 sesiones por minuto** y "anytime you are utilizing 70% or more of your current limit, the number of new streams able to be opened over the next minute will automatically increase by 10%". Los límites de partida personalizados por encima de 100 también están disponibles "at no additional cost".

## Why It Matters
Es la pieza que hace barato el voz en vivo a escala y la que descarta una objeción habitual: el crecimiento de concurrencia **no se factura**, de modo que no aparece como coste variable en el corte por categoría de [[2026-1022-costes-por-categoria-tenant]]. El umbral del 70 % con incremento del 10 % es un mecanismo de autoscaling por uso real —no por compromiso de gasto— que encaja con un despliegue en el VPS de ≤ €4/mes documentado en [[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]: el cuello de botella del voz en vivo no sería la CPU del VPS sino el número de conexiones simultáneas. Con 100 sesiones/min de partida, un clon con 1.000 llamadas concurrentes necesita 10 minutos de rampa. Y el límite gratuito de 5 conexiones/min explica por qué la voz en vivo sigue siendo una función de pago en la práctica, aunque la barra de entrada sea cero.
