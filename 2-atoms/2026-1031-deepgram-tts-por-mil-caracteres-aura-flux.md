---
id: 2026-1031-deepgram-tts-por-mil-caracteres-aura-flux
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-voice-agent-por-minuto-con-llm-y-tts-propios]]", "[[2026-1101-assemblyai-tts-15-por-millon-de-caracteres]]", "[[2026-1022-myclone-voice-providers-cartesia-elevenlabs]]"]
---

## Claim
El TTS de Deepgram se factura **por 1.000 caracteres de texto de entrada**: **Aura-1 $0,0150/1k** (Growth $0,0135), **Aura-2 $0,030/1k** (Growth $0,027) y **Flux TTS $0,0450/1k**, que **no baja en Growth** ($0,0450 en ambos planes). Hay además una promoción temporal: "For Flux TTS, $1 in credits for every $1 spent, up to $500, through **Dec. 31, 2026**".

## Why It Matters
Aura-1 a $0,0150/1k caracteres equivale exactamente a **$15 por 1M de caracteres**, la misma cifra que publica AssemblyAI para su TTS ([[2026-1101-assemblyai-tts-15-por-millon-de-caracteres]]): empate técnico en el precio del texto sintetizado, lo que deja la elección de TTS en el terreno de la calidad de voz y del control de la latencia, no del coste. El detalle que importa para el vault es que **Flux TTS no se abarata con Growth**: si el clon usa el modelo de mayor calidad (Flux es el que la propia FAQ recomienda para "real-time voice agents"), el plan comprometido no aporta nada en esa línea. Y la promoción de crédito 1:1 hasta $500 tiene fecha de caducidad (31-12-2026), así que es un ahorro con caducidad que conviene registrar antes de que desaparezca.

## [FRICTION]
> La página ofrece el conmutador "Streaming | Pre-recorded" para TTS, pero publica **una sola tabla** y ninguna cifra distinta para TTS en streaming; la FAQ solo dice "Per 1,000 characters of input text, across Flux TTS, Aura-2, and Aura-1".
> No es una contradicción, pero deja sin cotizar el caso de TTS en streaming frente a batch, que es precisamente el modo de un clon de voz en vivo (ver [[2026-1031-deepgram-voice-agent-por-minuto-con-llm-y-tts-propios]]). Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: los tres precios de TTS no cambian — Aura-1 $0,0150/1k (Growth $0,0135), Aura-2 $0,030/1k (Growth $0,027) y Flux TTS $0,0450/1k **sin descuento en Growth**. La novedad de esta captura es de **ubicación textual**: la promoción "For Flux TTS, $1 in credits for every $1 spent, up to $500, through Dec. 31, 2026" ha salido de la respuesta de la FAQ ("How is text-to-speech billed?", que ahora termina en "the table above carries the current figures") y aparece **en el pie de la tabla** de Text-to-speech. La oferta es la misma; lo que cambia es dónde hay que buscarla, lo que confirma la regla de citar siempre la fecha junto a la cifra. La captura también añade a este pie la frase "Concurrency limits apply per project and differ by plan and region", ya aplicada al TTS y no solo al Voice Agent.
