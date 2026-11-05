---
id: 2026-1031-deepgram-addons-por-minuto-sobre-transcripcion
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1101-assemblyai-addons-prerecordado-diarizacion-keyterms-medical]]", "[[2026-1022-separacion-de-hablantes-en-entrevistas]]"]
---

## Claim
Los add-ons de Speech-to-Text de Deepgram se cobran **por minuto encima de la transcripción** y solo uno va incluido: **Redaction $0,0020/min** (Growth $0,0017), **Speaker Diarization $0,0020/min** (Growth $0,0017), **Entity Detection $0,0017/min** (sin descuento en Growth), **Keyterm Prompting $0,0013/min** (Growth $0,0012) y **Smart Formatting "Included"** sin coste. La página lo dice literalmente: "Optional features billed on top of transcription. Smart formatting is included at no cost."

## Why It Matters
Coincide en estructura con los add-ons de AssemblyAI ([[2026-1101-assemblyai-addons-prerecordado-diarizacion-keyterms-medical]]), pero el orden de magnitud es otro: la diarización de Deepgram cuesta **$0,0020/min = $0,12/hr**, seis veces la de AssemblyAI ($0,02/hr). Sobre el monolingual de lista ($0,0077/min) eso es un **+26 %** sobre el precio del minuto, de modo que un pipeline con diarización + entity detection se acerca a $0,0114/min y la cifra "de entrada" que se comunica al cliente nunca es la real. El flujo de entrevistas del vault ([[2026-1022-separacion-de-hablantes-en-entrevistas]]) necesita diarización sí o sí, así que ese +26 % es la línea que hay que cotizar; y ojo al detalle de Entity Detection, que es la única feature cuyo precio **no baja** en Growth, lo que hace el plan comprometido menos rentable si la feature está activa.

## [FRICTION]
> La página ofrece un conmutador "Streaming | Pre-recorded" en la tabla de add-ons, pero la captura **solo muestra una tabla** y la FAQ no publica ninguna cifra de pre-recorded para estos add-ons. No es posible saber si la diarización de Deepgram cuesta $0,12/hr también en pre-recorded o si baja ahí (como afirma la FAQ con "Pre-recorded runs lower" para la transcripción base, ver [[2026-1031-deepgram-prerecorded-mas-barrio-pero-sin-cifra-publicada]]). Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: la tabla de add-ons reproduce las mismas cinco líneas sin variación — Redaction $0,0020 (Growth $0,0017), Speaker Diarization $0,0020 (Growth $0,0017), Entity Detection $0,0017 (sin descuento en Growth), Keyterm Prompting $0,0013 (Growth $0,0012) y Smart Formatting "Included". El conmutador "Streaming | Pre-recorded" sigue presente y la página sigue publicando **una sola tabla** para ambas pestañas, de modo que el hueco de la cifra de pre-recorded se mantiene abierto por cuarta vez.
