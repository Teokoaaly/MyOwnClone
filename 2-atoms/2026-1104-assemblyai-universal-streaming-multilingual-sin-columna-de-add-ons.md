---
id: 2026-1104-assemblyai-universal-streaming-multilingual-sin-columna-de-add-ons
type: atom
certainty: solid
sources: [sources/2026-11-04-assemblyai-pricing.md, sources/2026-11-02-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]]", "[[2026-1101-assemblyai-addons-realtime-diarizacion-012-y-pii-012]]", "[[2026-1104-assemblyai-precios-estables-en-las-tres-capturas-completas]]"]
---

## Claim
La sección Realtime de AssemblyAI publica **tres modelos** (Universal-3.6 Pro Realtime $0,45/hr, Universal-Streaming $0,15/hr y **Universal-Streaming Multilingual $0,15/hr**) pero su tabla de **add-ons solo tiene dos columnas**: "| Add-on features | Universal-3.6 Pro Realtime | Universal-Streaming |". **Universal-Streaming Multilingual no tiene columna de add-ons**, es decir, la página **no publica** qué cuesta la diarización ($0,12/hr en los otros dos), el PII Text Redaction ($0,12/hr), el Medical Mode ($0,15/hr) ni el Keyterms Prompting ($0,04/hr) sobre ese modelo. La segunda tabla, "Add-on features" en texto plano, repite solo esos dos modelos ("Universal-3.6 Pro Realtime" / "Universal-Streaming"), confirmando que la omisión no es un fallo de render.

## Why It Matters
Es un hueco de precio, no una ausencia de dato: el modelo existe y tiene tarifa ($0,15/hr, la misma que el streaming monolingüe, "at the speed and cost of Universal-Streaming"), pero su coste total con diarización o redacción de PII **no es calculable desde la página**. Para el vault esto importa porque el multilingüe es, según [[2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015]], la opción que hace viable el clon de voz en español sin disparar la partida de infraestructura; y la diarización en realtime es precisamente la función que duplica el precio del modelo barato ($0,15 → $0,27/hr, ver [[2026-1101-assemblyai-addons-realtime-diarizacion-012-y-pii-012]]). Es decir: **el modelo que el vault elegiría por precio es el único al que no se le puede sumar el add-on más caro de la sección**. Consecuencia práctica: al construir un panel de costes por tenant hay que tratar el precio del multilingüe como "$0,15/hr + add-ons desconocidos" y no como una cifra cerrada, o pedir cotización a ventas. La captura del 11-04 confirma que el hueco es estable en las tres capturas completas.

## [FRICTION]
> La pista del Scout para esta captura daba "realtime Universal-3.6 Pro **$0,12/hr** y Universal-Streaming **$0,04/hr**".
> Los valores literales de la fuente son **$0,45/hr** y **$0,15/hr** para los modelos; **$0,12/hr** es el precio del add-on *Speaker Diarization* (y del *PII Text Redaction*) en realtime, y **$0,04/hr** es el add-on *Keyterms Prompting* en Universal-Streaming. Los precios de modelo y los de add-on conviven en la misma sección y se confunden con facilidad al leerla en bloque. Marcado para juicio humano, no auto-resuelto.
