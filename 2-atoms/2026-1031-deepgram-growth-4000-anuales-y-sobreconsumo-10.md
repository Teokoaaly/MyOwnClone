---
id: 2026-1031-deepgram-growth-4000-anuales-y-sobreconsumo-10
type: atom
certainty: solid
sources: [sources/2026-10-31-deepgram-pricing.md, sources/2026-11-03-deepgram-pricing.md]
links: ["[[2026-1031-deepgram-precios-por-minuto-por-modelo]]", "[[2026-1031-deepgram-pricing]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
El plan comprometido de Deepgram es **Growth**: "Pre-paid credits for the year, redeemed against actual usage", **$4.000+/año**, con "**Save up to 20%**" sobre el pay-as-you-go. El excedente se factura a la tarifa Growth **+10 %**, semanalmente los lunes por la semana previa, y sin tarjeta en archivo las peticiones devuelven **402** al agotarse el crédito. El FAQ lo resume: "Pay as you go has no commitment and bills against credits as you use them. Growth starts at $4,000 a year in pre-paid annual credits for up to 20% off and higher streaming concurrency."

## Why It Matters
El compromiso mínimo de $4.000/año es **mil veces** el presupuesto de infraestructura de ≤ €4/mes del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]): Growth es una opción para un producto con tráfico de voz agregado, no para MyOwnClone en su fase actual. Por eso la comparación de la web tiene que hacerse contra el "Pay as you go" sin compromiso, tal y como resume [[2026-1031-deepgram-precios-por-minuto-por-modelo]] y [[2026-1031-deepgram-pricing]]. Lo que sí es copiable como patrón de producto es la mecánica del sobreconsumo: un recargo del 10 % sobre la tarifa del plan committed es exactamente el tipo de salvaguarda que MyOwnClone necesitaría si vendiera transcripción por uso dentro de sus tiers, porque el 402 sin tarjeta es un corte de servicio duro — en un clon de voz, un 402 en mitad de una llamada es peor que un 429.

## [FRICTION]
> El titular de la web anuncia "**Save up to 20%**" en Growth, pero en las tarifas publicadas el descuento real es **~15,6 %** en Nova-3 Monolingual ($0,0077 → $0,0065), ~13 % en Flux Multilingual ($0,0078 → $0,0068) y ~15 % en Nova-3 Multilingual ($0,0092 → $0,0078). Además, la FAQ de los modelos antiguos afirma "Growth is about 12.5% lower" (ver [[2026-1031-deepgram-modelos-legacy-nova2-enhanced-base-por-hora]]), otra cifra distinta.
> El "20 %" del titular solo se alcanza en algún producto no tabulado (TTS Flux no baja: $0,0450 en ambos planes), de modo que el titular y la tabla no pueden ser ambos la medida del descuento aplicable a STT. Marcado para juicio humano, no auto-resuelto.

## 2026-11-03 — re-verificación
Cuarta captura: el tier Growth sigue en "$4,000+/ year" con "Save up to 20%", y la FAQ sobre el sobreconsumo se mantiene sin cambios ("Exceeding your credits bills at your Growth rate plus 10%, charged weekly on Mondays for the prior week. A card must stay on file; without one, requests return a 402 once credits run out"). Dos matices nuevos que este átomo no recogía: (1) existe una **vía documentada para evitar el recargo** — la renovación anticipada en Console ([[2026-1103-deepgram-renovacion-anticipada-growth-resetea-creditos]]); y (2) existe una **ventana de reembolso de 30 días** para créditos no usados ([[2026-1103-deepgram-reembolso-de-creditos-no-usados-en-30-dias]]). Ambos quedan fuera del encabezado "Save up to 20 %" y no cambian la fricción del descuento real (~15,6 % en STT).
