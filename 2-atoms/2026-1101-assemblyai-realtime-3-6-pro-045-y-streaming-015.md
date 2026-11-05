---
id: 2026-1101-assemblyai-realtime-3-6-pro-045-y-streaming-015
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1022-gap-voz-en-vivo-myownclone]]", "[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]"]
---

## Claim
El Realtime Speech-to-Text de AssemblyAI publica tres modelos con precios por hora muy separados: **Universal-3.6 Pro Realtime $0.45/hr** ("The most accurate realtime model for high-quality voice agents with built-in context carryover and conversation memory. Supports 32 languages with self-correcting speaker labels, voice isolation, and keyterm prompting"), **Universal-Streaming $0.15/hr** (solo inglés, "Purpose-built for production voice applications") y **Universal-Streaming Multilingual $0.15/hr** (inglés, español, alemán, francés, portugués e italiano, "at the speed and cost of Universal-Streaming").

## Why It Matters
La distancia entre el modelo de voz en directo y el de archivo es de **3×** ($0.45 vs $0.15/hr), y esto decide la arquitectura del módulo de voz en vivo que el vault tiene marcado como gap en [[2026-1022-gap-voz-en-vivo-myownclone]]. Con el mismo presupuesto: 100 horas de realtime con 3.6 Pro cuestan **$45/mes**; 100 horas de streaming cuestan **$15/mes**; 100 horas de pre-recorded con Universal-2 cuestan **$15/mes**. Es decir, la voz en vivo *barata* cuesta lo mismo que transcribir archivos, y la voz en vivo *de calidad* cuesta lo que un hosting VPS completo multiplicado por diez. Para un producto cuyo coste dominante es el SaaS por asiento (ver [[2026-1022-costes-por-categoria-tenant]]), el streaming multilingüe a $0.15/hr es la opción que hace viable un clon de voz en español sin disparar la partida de infraestructura. Nota de modelo: 3.6 Pro aporta "context carryover and conversation memory" y "self-correcting speaker labels" — exactamente las capacidades que LiveKit da en [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]] pero que aquí vienen como sobrecoste de modelo, no de transporte.

## Actualización 2026-11-04 — re-verificación y hueco en la tabla de add-ons
La captura del 2026-11-04 (render completo, idéntico al del 11-02) reproduce sin variación los tres precios de realtime: **Universal-3.6 Pro Realtime $0,45/hr**, **Universal-Streaming $0,15/hr** y **Universal-Streaming Multilingual $0,15/hr**. Matiz nuevo que esta captura deja explícito: la tabla de add-ons de realtime **solo tiene columnas para los dos primeros modelos**, por lo que el precio de los add-ons sobre *Universal-Streaming Multilingual* no está publicado; ver [[2026-1104-assemblyai-universal-streaming-multilingual-sin-columna-de-add-ons]].
