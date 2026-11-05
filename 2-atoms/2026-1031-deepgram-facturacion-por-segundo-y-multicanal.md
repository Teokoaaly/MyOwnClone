---
id: 2026-1031-deepgram-facturacion-por-segundo-y-multicanal
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1102-assemblyai-multicanal-se-cobra-por-canal]]", "[[2026-1031-deepgram-credit-gratuito-200-dolares-y-43-000-minutos]]"]
---

## Claim
Deepgram factura el STT **por segundo de audio procesado, sin redondeo a bloques y sin mínimo de duración** ("a 14-second file bills as 14 seconds. There is no minimum duration and no rounding up to the next block") y **el audio multicanal se cobra por la duración total sumada entre canales**: "A ten-minute stereo file contains twenty minutes of audio across two channels, so it bills as twenty minutes."

## Why It Matters
Son dos reglas de facturación que hay que conocer antes de cotizar el pipeline de entrevistas del vault, y que también explican parte del desfase con el crédito gratuito. El cobro por segundo sin redondeo favorece el audio ya cortado en frases (pipeline STT→LLM→TTS con chunks, que es justo la arquitectura de MyOwnClone): no se paga penalización por segmentar. El multicanal al doble es la trampa: una grabación estéreo de una entrevista de 10 minutos cuesta **$0,154** en Nova-3 monolingual (0,0077 × 20), no $0,077, porque los dos canales se facturan íntegros. Es el mismo tipo de coste que ya está documentado para AssemblyAI ([[2026-1102-assemblyai-multicanal-se-cobra-por-canal]]) y funciona como aviso de que el mono/stereo debe ser una decisión de producto, no un detalle de la captura.

## [FRICTION]
> Esta regla de "sin redondeo, por segundo" no concilia con la afirmación de la FAQ de que el crédito de $200 cubre "43,000 minutes" de Nova-3: a $0,0077/min, $200 dan ~25.974 minutos (ver [[2026-1031-deepgram-credit-gratuito-200-dolares-y-43-000-minutos]]).
> Ambas no pueden ser del todo correctas: o el crédito tiene una tarifa interna de descuento no publicada, o el número de minutos de la FAQ está inflado. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: las dos reglas de facturación se enuncian igual — "Billed per second, with no block-based rounding for normal audio requests. Multichannel audio bills by total processed duration across channels" y "A ten-minute stereo file contains twenty minutes of audio across two channels, so it bills as twenty minutes". Se mantiene, por tanto, la fricción ya abierta entre el cobro por segundo y la cifra de "43,000 minutes" del crédito gratuito: la aritmética no cambia ($200 / $0,0077 ≈ 25.974 minutos).
