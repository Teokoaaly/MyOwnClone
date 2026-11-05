---
id: 2026-1029-resend-scale-plan
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-pro-plan]]", "[[2026-1029-resend-pay-as-you-go]]"]
---

## Claim

The Resend Scale plan at $90/mo includes 100,000 transactional emails monthly, with overage at $0.90 per 1,000 emails, 1,000 domains, Dedicated Slack channel, 10 webhook endpoints, 500 AI credits monthly, and all Pro features plus Dedicated IP with add-on.

## Why It Matters

The Scale plan targets high-volume senders who need 100K included emails monthly. At $90 for 100K emails (effective $0.90/1K included), the per-email cost is higher than Pro on a per-included basis, but the 2x volume increase and feature set (Dedicated Slack channel, 1K domains, 500 AI credits) justify the price for teams requiring those capabilities. The $55/mo jump from Pro to Scale introduces a "feature cliff" at 50K emails/mo ($35/mo), after which the next tier adds real operational capabilities. Teams sending 50K–100K emails/month should model whether the added features (SAML SSO, dedicated IP pools, phone/chat support) are actually used, as switching plans involves not just cost delta but functional capability loss.

## [FRICTION]

> [[2026-1029-resend-pro-plan]] (written today) argues that the $55/mo price jump for 100k vs 50k included emails means the breakeven is at ~417k additional emails/month, and below that volume Foundation (analogous) is the cost-optimal choice. This note presses that the comparison is incomplete: Pro and Scale have the same per-email overage rate ($0.90/1K), but Pro includes only 50K emails while Scale includes 100K. A team sending exactly 50K–100K emails/month could save $55/mo on Pro if they don't need Scale's features, or pay $55/mo more on Scale if they do. The friction is that the price difference does not map linearly to volume — a team at 51K emails pays the same $90 overage threshold on Pro as on Scale, making the "breakeven at 417k" claim misleading for the 50K–100K range where the decision hinges on feature needs, not marginal cost. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`. Corrección aritmética en el texto anterior: el salto de Pro ($20/mes) a Scale ($90/mes) es de **$70/mes**, no de $55/mes — el propio átomo de Pro lo cifra en $70. No se modifica el bloque previo; la cifra correcta queda aquí.

Datos adicionales verificados: 1.000 dominios, canal Slack dedicado, 10 webhook endpoints, 500 créditos de IA/mes, SSO como add-on e IP dedicada como add-on — todos coherentes con el claim. La tabla añade que los dominios custom de Scale son 1.000 y que la retención de datos es de 30 días en Free, Pro y Scale, "Flexible" en Enterprise. Detalle del add-on de IP dedicada en [[2026-1029-resend-add-ons]].