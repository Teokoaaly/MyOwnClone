---
id: 2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1023-priceai-claude-pro-y-max-precios-y-ventanas]]", "[[2026-1023-priceai-transit-dispersion-de-multiplicadores]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]"]
---

## Claim
La tabla **Text-to-Text** de Heroku Managed Inference publica precios **por 1M de tokens, con columnas separadas de entrada y salida**, y para los modelos Anthropic el precio de salida es **exactamente 5× el de entrada** en las ocho filas: **claude-3-haiku $0.25 / $1.25**, **claude-4-5-haiku $1.10 / $5.50**, **claude-4-sonnet $3.00 / $15.00**, **claude-4-5-sonnet $3.30 / $16.50**, **claude-sonnet-4-6 $3.30 / $16.50**, **claude-opus-4-5 $5.00 / $25.00**, y **claude-opus-4-6 / 4-7 / 4-8 $5.50 / $27.50** (los tres últimos con precio idéntico). El más barato es **claude-3-haiku a $0.25/1M de entrada** y el más caro **claude-opus-4-8 a $5.50**, un factor **×22** entre extremos de la misma familia.

## Why It Matters
Es la **primera tabla de precio por token de la familia Claude que el vault tiene verificada contra una fuente primaria**, y llena un hueco que el propio vault había señalado: [[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]] concluye que la captura de PriceAI **no permite derivar un coste por token** porque sus cuotas están en requests, prompts y credits. Aquí sí: es un precio de lista por 1M tokens con entrada y salida separadas, que es exactamente la granularidad que la tabla de ratios de New API ([[2026-1023-new-api-precios-por-ratio-y-expresion]]) necesita como denominador.
Y es la pieza que hace medible el multiplicador de los relays: el vault tiene canales vendiendo Claude entre **0,05× y 2,10×** el "precio oficial" ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]), pero hasta ahora **"el precio oficial" era una magnitud no verificada**. Con esta tabla, el extremo barato del ranking se puede traducir a dólares: 0,05× de $3.30/1M de entrada de Sonnet 4.5 son **$0.165 por millón de tokens de entrada**.
El dato estructural más importante para el producto es la **asimetría 5:1 entre entrada y salida**. Para un clon que genera mucho texto (respuestas de un asistente) frente a uno que ingiere mucho contexto (documentos, historial), **el coste se multiplica por 5 en la salida** — y un relay que no diferencia input de output en su contabilidad está roundando ese 5:1. También separa limpiamente el precio de API del precio de suscripción: la cuota de Claude Pro es $130/mes ([[2026-1023-priceai-claude-pro-y-max-precios-y-ventanas]]) y **no es comparable** a $5.50/1M sin una traducción por consumo, que es la línea que el vault ya marcó en [[2026-1023-priceai-suscripcion-no-es-api-token]].

## [FRICTION]
> [[2026-1023-priceai-claude-pro-y-max-precios-y-ventanas]] (escrita el 2026-10-23) construye una **tabla de equivalencia entre suscripción y cuota** en la que la cobertura del canal Claude incluye **"Claude Opus 4.8"** con las ventanas $130 / $1,300 / $3,200 de cuota, y trata esa cuota como la medida de "cuánto Claude" da un plan.
> Este átomo presiona esa creencia en un punto concreto: **la cuota de la suscripción y el precio por token de la API no son la misma magnitud, y ahora hay un tercero en juego — el precio de un intermediario que revende esos mismos modelos**. La tabla de Heroku da **claude-opus-4-8 a $5.50/1M de entrada y $27.50/1M de salida**. Si la cuota de $130 del plan Pro se gastara **íntegramente** en Opus 4.8 a salida, serían **$4.73 por millón de tokens**; si fuera en entrada, **$23.64 por millón**. **El mismo número de cuota tiene dos precios por token que difieren en ×5**, según la dirección del tráfico.
> Ambas no pueden ser completamente correctas: o la equivalencia suscripción→tokens necesita la mezcla de entrada/salida (y el vault no la tiene publicada), o la cuota de la suscripción mide algo que no es tokens de Opus 4.8. Marcado para juicio humano, no auto-resuelto: la captura de PriceAI no publica la conversión, y la de Heroku no publica la equivalencia con la suscripción.

## Nota de verificación
El cociente 5:1 y el factor ×22 son cálculo de este átomo sobre las dos columnas de precio de la tabla; la fuente no publica agregados ni equivalencias. La columna "Region Provisioned" de estos ocho modelos dice "US | EU".
