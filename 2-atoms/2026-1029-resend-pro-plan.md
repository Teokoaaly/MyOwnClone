---
id: 2026-1029-resend-pro-plan
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-free-plan]]", "[[2026-1029-resend-scale-plan]]"]
---

## Claim

The Resend Pro plan at $20/mo includes 50,000 transactional emails monthly, with overage at $0.90 per 1,000 emails, 10 domains, no daily email limit, 5 webhook endpoints, 100 AI credits monthly, and all Free features plus SSO.

## Why It Matters

The Pro plan bridges the gap between the restrictive Free tier and the high-volume Scale plan. At $20/mo for 50K emails (effective $0.40/1K included, $0.90/1K overage), it offers a 10x volume increase over Free for $20/mo. The absence of a daily email limit makes it suitable for growing applications, while the 10-domain limit and 5 webhook endpoints keep it appropriate for small teams. The 100 AI credits monthly add value for teams using AI-assisted email features. Teams evaluating cost per email should note that the per-email cost drops significantly only at higher volumes, making Pro most attractive for moderate, steady senders.

## [FRICTION]

> [[2026-1029-resend-scale-plan]] (written today) claims that at 50k–100k emails/month the effective cost per 1,000 drops and teams should model feature gates, but the Pro plan charges the same $0.90/1K overage rate as Scale while offering only 50K included emails vs Scale's 100K. This note presses that a team sending ~75K emails/month pays $20 on Pro but would need $90 on Scale — yet Scale adds Dedicated Slack channel, 1K domains, and 500 AI credits. If the extra features are unused, Pro is the cost-optimal choice; if they are needed, Scale's $70 premium buys real operational capabilities. Both can be correct depending on feature usage, but the cost differential without feature utilization creates a friction point for volume modeling. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`: las cifras del claim son correctas ($20/mes, 50.000 emails, $0,90/1.000 de excedente, 10 dominios, sin límite diario, 5 webhook endpoints, 100 créditos de IA). Salvedad: el claim cierra diciendo "plus SSO" siguiendo la tarjeta de la página, pero la tabla comparativa marca Single Sign-On como "–" tanto en Free como en Pro y "With add-on" solo en Scale — la propia captura se contradice en este punto. El add-on de SSO cuesta $150/mes y está documentado en [[2026-1029-resend-add-ons]].

Costo efectivo verificado: los 50.000 emails incluidos de Pro cuestan $20/mes, es decir $0,40/1.000, la mitad del precio del excedente de $0,90/1.000; los 100.000 incluidos de Scale cuestan $90/mes, es decir $0,90/1.000, exactamente el precio del excedente de Pro. Por tanto el coste de envío bruto de Pro siempre es menor o igual que el de Scale para el mismo volumen (a 51.000 emails, Pro cuesta $20,90 y Scale $90), y la diferencia entre ambos planes es de features, no de margen. Detalle del nivel siguiente en [[2026-1029-resend-scale-plan]].