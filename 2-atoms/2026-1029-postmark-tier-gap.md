---
id: 2026-1029-postmark-tier-gap
type: atom
certainty: solid
sources: [sources/2026-10-29-postmark-pricing.md]
links: ["[[2026-1029-postmark-free-tier]]", "[[2026-1029-postmark-pricing-tiers]]"]
---

## Claim
Postmark no ofrece ningún plan intermedio entre el Free (100 emails/month) y el pago más básico (Basic a 10,000 emails/month) — existe un gap enorme de dos órdenes de magnitud sin opciones intermedias.

## Why It Matters
El gap de 100 → 10,000 emails/month obliga a cualquier proyecto que supere el límite del plan Free a comprometerse inmediatamente con un plan pagado de 10,000 mínimo, incluso si su volumen real es de 200 o 500 emails. Esta falta de escalas intermedias hace que Postmark sea poco flexible para proyectos de etapa temprana, freelances con tráfico esporádico, o prototipos que no pueden predecir su volumen de email. Servicios que ofrecen planes "pay-as-you-go" desde volúmenes bajos capturan ese segmento de mercado, mientras que Postmark asume que los usuarios transaccionales ya tienen un caso de uso estable suficiente para comprometerse al plan Basic.

## [FRICTION]
> [[2026-1022-precio-99-mensual]] (escrita hace ~21 semanas) documenta el plan de $99/mo de [[myownclone]] que incluye 1 millón de palabras de entrenamiento y 4,000 respuestas — un modelo de pricing calibrado contra el consumo real de un cliente específico, con una propuesta de valor que conecta directamente con [[emprenda-aprendiendo]]. Este átomo presiona que Postmark's $15/mo Basic plan starting at 10,000 emails es un punto de compromiso fijo, no calibrado contra casos de uso individuales: la diferencia es que Postmark cobra por volumen de email (costo de infraestructura), mientras myownclone cobra por capacidad de entrenamiento (costo de IA). Ambas pueden ser correctas dentro de sus respectivos dominios: el pricing de Postmark refleja costos reales de entrega de email, mientras el de myownclone refleja costos de modelo de IA. Ambas no pueden ser completamente correctas si se evalúa una como sustituta de la otra — son productos de categorías distintas. Marcado para juicio humano, no auto-resuelto.