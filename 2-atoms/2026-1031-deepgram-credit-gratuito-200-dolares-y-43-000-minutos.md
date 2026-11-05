---
id: 2026-1031-deepgram-credit-gratuito-200-dolares-y-43-000-minutos
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1102-assemblyai-tier-gratuito-185-horas-y-333-streaming]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El arranque de Deepgram incluye **$200 de crédito gratuito sin caducidad y sin tarjeta de crédito**, y la FAQ lo cuantifica: "Roughly 43,000 minutes, over 700 hours, of Nova-3 transcription. It does not expire, so you can prototype without a clock running. No credit card is required to start." El tier "Pay as you go" se define además como "No minimums, no expiration, and no credit card required".

## Why It Matters
Es el equivalente del tier gratuito de AssemblyAI ([[2026-1102-assemblyai-tier-gratuito-185-horas-y-333-streaming]]) pero con una diferencia estructural: los $200 son **un saldo en dólares de un solo proveedor**, no un número de horas protegido — el mismo saldo se puede consumir en STT, TTS o Audio Intelligence, y no se reparte entre tenants. Para MyOwnClone sirve para prototipar el módulo de voz sin gastar contra el presupuesto de ≤ €4/mes ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]), y su caducidad indefinite permite validar el producto antes de comprometerse con el plan Growth de $4.000/año.

## [FRICTION]
> La propia FAQ dice que $200 cubren "43,000 minutes" de Nova-3, pero la tarifa pay-as-you-go publicada para Nova-3 Monolingual es **$0,0077/min** (ver [[2026-1031-deepgram-precios-por-minuto-por-modelo]]), y $200 / $0,0077 = **~25.974 minutos** (≈433 horas), no 43.000 minutos (716 horas). Para que los 43.000 minutos cuadraran, el crédito tendría que estar valorando el minuto a ~$0,00465, es decir una tarifa ~40 % inferior a la de lista, no publicada en ninguna parte.
> Ambas cifras no pueden ser simultáneamente correctas: o los $200 rigen una tarifa de descuento no documentada, o el número de minutos de la FAQ está inflado ~1,65×. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: la FAQ repite literalmente "Roughly 43,000 minutes, over 700 hours, of Nova-3 transcription. It does not expire, so you can prototype without a clock running. No credit card is required to start", y el tier "Pay as you go" sigue definido como "No minimums, no expiration, and no credit card required". La inconsistencia aritmética de este átomo **persiste sin cambios**: $200 / $0,0077 ≈ 25.974 minutos, no 43.000. Lo que se añade es el encaje con la política de reembolso, que solo cubre "unused credits purchased within the last 30 days" ([[2026-1103-deepgram-reembolso-de-creditos-no-usados-en-30-dias]]) — el crédito gratuito no caduca pero tampoco es reembolsable.
