---
id: 2026-1031-assemblyai-pricing
type: atom
certainty: solid
sources: [sources/2026-10-31-assemblyai-pricing.md]
links: ["[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]", "[[costes-por-categoria-tenant]]"]
---

## Claim
AssemblyAI's pricing is per-minute of transcribed audio with volume-based discounts, similar to Deepgram's usage-based model, where cost scales with audio duration rather than per-user seats.

## Why It Matters
Like Deepgram, AssemblyAI's cost scales with transcribed minutes rather than user count, creating a usage-based cost model for audio transcription. For products with audio transcription needs, the cost depends on average audio duration per user per month. The friction is in comparing against Deepgram and per-seat models: both AssemblyAI and Deepgram charge per-minute, but may have different rate structures, minimums, or feature sets. A product choosing between them must measure the rate per minute and expected minutes per user to determine the most cost-effective option, and compared to the per-seat model from `costes-por-categoria-tenant`, the break-even point depends on the audio-per-user ratio.

## [FRICTION]
> [[2026-1031-deepgram-pricing]] establece Deepgram's per-minute pricing at rates that scale with transcribed minutes, while AssemblyAI offers similar per-minute pricing with potentially different rate tiers. Both cannot simultaneously be the most cost-effective per-minute provider — the choice depends on the specific rate structure, minimum commitments, and feature sets each provides. A product requiring audio transcription must measure the rate per minute for both providers and compare against the per-user cost in the `costes-por-categoria-tenant` framework to determine the most economical option for the expected audio volume per user.

## Nota de extensión 2026-11-03
Las capturas del 2026-11-01 y del 2026-11-02 de `assemblyai.com/pricing` (antes casi vacías: la del 2026-10-31 solo traía la cabecera, un banner de cookies y la tabla de pre-recorded) **revelan la unidad real de precio: la hora, no el minuto**. La página publica **$0,21/hr** para Universal-3.5 Pro y **$0,15/hr** para Universal-2 en pre-recorded, **$0,45/hr** para Universal-3.6 Pro Realtime y **$0,15/hr** para Universal-Streaming, **$0,30/hr** para el Sync API, **$0,62/hr** para el Dictation API, y **$15 por 1M caracteres** para el TTS AssemblyAI-TTS-1. No aparece ninguna cifra por minuto en toda la página. Tampoco aparecen descuentos por volumen publicados: la FAQ solo ofrece *custom pricing* vía equipo de ventas, y el bloque "Looking for volume-based pricing?" remite a hablar con ventas.
Esto deja la afirmación de este átomo —"per-minute of transcribed audio with volume-based discounts, similar to Deepgram's usage-based model"— **sin corroborar y parcialmente desmentida**: la unidad es la hora y los descuentos por volumen no son públicos. La fricción está planteada en [[2026-1101-assemblyai-tarifas-por-hora-no-por-minuto]] y la comparación de unidades con Deepgram en [[2026-1101-assemblyai-vs-deepgram-coste-por-hora-de-streaming]]; no se resuelve aquí para no sobrescribir la creencia previa. Los precios se han mantenido idénticos entre las tres capturas (2026-10-31, 2026-11-01, 2026-11-02), así que el cambio es de **lectura**, no de tarifa.