---
id: 2026-1101-assemblyai-tts-15-por-millon-de-caracteres
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md, sources/2026-10-31-deepgram-pricing.md]
links: ["[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]", "[[2026-1022-myclone-voice-clone]]", "[[2026-11-01-gemini-tts-models]]"]
---

## Claim
El Text-to-Speech de AssemblyAI, el modelo **AssemblyAI-TTS-1** ("New"), se factura por **caracteres de entrada a $15 por 1M caracteres** ("Billed on input characters"), con ~90 ms de time-to-first-audio, en inglés, español, francés, alemán, italiano y portugués, y con cinco features marcadas "Included": Voice Library (4.000+ voces con nombre, descripción y tags), **Instant Voice Cloning**, Word-Level Timestamps, US y EU processing al mismo precio, y concurrencia sin compromiso de gasto ("No spend commitment to unlock the concurrency you need").

## Why It Matters
Es el dato más accionable de toda la captura para el vault: **la clonación de voz está incluida en la tarifa base**, sin coste adicional por voz clonada ni por procesar en la UE ("Cloned voices and EU processing cost the same"). El competidor que el vault ya documenta mantiene dos proveedores de clonación en paralelo —Cartesia y ElevenLabs— con tres endpoints de ingesta cada uno ([[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]), así que el coste real de clonar una voz en AssemblyAI es $0 de marginal: solo el texto sintetizado. En unidades comparables, $15/1M caracteres equivale a unos **$0,81 por hora de audio sintetizado** (a ~900 caracteres/min de habla), el mismo orden que el TTS de Gemini 3.8 Flash documentado en [[2026-11-01-gemini-tts-models]] (~$0,00225 por 10 s ≈ $0,81/h) y prácticamente idéntico al de Deepgram Aura-1 ($0,0150/1k caracteres = $15/1M, también ≈$0,81/h). Es decir, **el TTS de caracteres no es donde está la ventaja de coste de AssemblyAI: la ventaja está en que clonar voz no se cobra**, lo que encaja con la lógica de activación del wizard de voz que describe [[2026-1022-myclone-voice-clone]].
