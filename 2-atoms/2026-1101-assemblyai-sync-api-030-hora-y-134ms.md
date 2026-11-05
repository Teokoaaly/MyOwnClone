---
id: 2026-1101-assemblyai-sync-api-030-hora-y-134ms
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]]", "[[2026-1101-assemblyai-dictation-api-062-hora-y-120s]]", "[[2026-1022-gap-voz-en-vivo-myownclone]]"]
---

## Claim
El Sync Speech-to-Text API de AssemblyAI ("New") cobra **$0.30/hr** y entrega transcripción en una sola llamada: "Universal-3.5 Pro accuracy delivered in a single call. Process up to 20 minutes per request, get results back in ~134 ms (p50). Includes per-word timing and confidence across 18 languages". Sus add-ons: **Keyterms Prompting "Included"**, **Conversation Context "Included"** ("Supply prior dialogue to give the model conversational continuity") y **Prompting $0.05/hr**.

## Why It Matters
Es la modalidad que encaja con la arquitectura que ya tiene el vault: una llamada HTTP que devuelve el texto, sin WebSocket, sin polling y sin job que gestionar — el mismo patrón que el endpoint de respuesta ya existente en el clon, en lugar del transporte en vivo que [[2026-1022-gap-voz-en-vivo-myownclone]] señala como gap pendiente. El coste es el más alto de las tres modalidades de archivo (0.30 vs 0.21 vs 0.15/hr) pero sigue siendo bajo en términos absolutos: un minuto de audio cuesta $0.005, y con el límite de 20 minutos por petición una subida de una hora se procesa en 3 llamadas. Que **Keyterms y Conversation Context estén incluidos** importa más que el precio: son precisamente las dos features que la tabla de pre-recorded cobra aparte ([[2026-1101-assemblyai-addons-prerecordado-diarizacion-keyterms-medical]]), así que el Sync API es la opción "todo incluido" para clips cortos y la opción barata para clips largos, justo al revés de lo que sugiere el precio por hora.
