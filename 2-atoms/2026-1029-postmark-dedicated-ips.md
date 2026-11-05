---
id: 2026-1029-postmark-dedicated-ips
type: atom
certainty: solid
sources: [sources/2026-10-29-postmark-pricing.md]
links: ["[[2026-1029-postmark-pricing-tiers]]", "[[2026-1029-postmark-tier-gap]]"]
---

## Claim
Los IPs dedicados de Postmark comienzan en $50/mes y solo están disponibles en planes Pro o superior — una capa de costo adicional requerida para enviadores de 300,000 emails/mes o más.

## Why It Matters
El requisito de IP dedicada a partir del umbral de 300,000 emails/month, combinado con el costo adicional de $50/mes, crea un umbral financiero y operativo para equipos medianos y grandes. Este costo separado de los planes de email transforma el total mensual efectivo: el plan Platform a $18/mo más un IP dedicado a $50/mo resulta en $68/mo minimum para alta capacidad de envío. Esta separación de costos permite a Postmark cobrar por estabilidad de entrega (IPs dedicados) de forma desglosada, pero también significa que el costo total de ownership puede duplicarse o triplicarse respecto al precio de lista del plan base. Para start-ups en crecimiento, este salto de costo inesperado es un punto de fricción notable al momento de presupuestar infraestructura de email transaccional a escala.

## [FRICTION]
> [[2026-1029-postmark-tier-gap]] (escrita hace pocas semanas) afirma que Postmark no tiene planes intermedios entre Free (100 emails) y Basic (10,000 mínimo), y este átomo presiona que el requisito de IP dedicada a $50/mo añade otra barrera de costo antes incluso de alcanzar el umbral de 300,000 emails/month. Ambas pueden ser correctas: el gap de planes afecta el ingreso inicial al plataforma, mientras que el costo de IP dedicada afecta el escalado a alta capacidad. Ambas no pueden ser completamente correctas si se evalúa el costo total de ownership a partir del plan base — el plan Platform a $18/mo más IP dedicada a $50/mo = $68/mo minimum, lo que cambia radicalmente la ecuación de costo versus alternativas como AWS SES o SendGrid que incluyen IPs en sus planes base. La intersección de estos two friction points (gap de planes + costo de IP dedicada) crea un cuello de botella de costo para teams en crecimiento. Marcado para juicio humano, no auto-resuelto.