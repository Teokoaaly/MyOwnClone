---
id: 2026-1029-resend-free-plan
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-pro-plan]]", "[[2026-1029-resend-scale-plan]]"]
---

## Claim

The Resend Free plan at $0/mo includes 3,000 transactional emails monthly, limited to 100 emails per day, 3 domains, 3 inboxes, ticket support, 10,000 automation runs, and 30-day data retention.

## Why It Matters

The Free plan serves as the entry point for developers and small projects to evaluate Resend without cost. Its strict daily limit of 100 emails (≈3,000/mo) and lack of a no-daily-limit policy means it suits low-volume use cases like onboarding emails or personal projects. The 3-domain limit and ticket-only support further constrain its use for growing teams, making it a funnel into paid plans when volume or feature needs increase.

## [FRICTION]

> [[2026-1029-resend-pro-plan]] (written today) claims the overage rate of $0.90 per 1,000 emails is only available on paid plans. This note presses that the Free plan's 3,000 email monthly quota may still incur overage charges if pay-as-you-go is enabled and the 3,000 threshold is exceeded, since the source states overage applies "to paid subscriptions" — yet the Fine print on inbox pricing ($1/inbox/mo on paid plans) suggests pay-as-you-go can be enabled on paid plans only, leaving ambiguity about whether Free-plan overage is permitted at all. Both cannot be completely correct: either the Free plan permits pay-as-you-go overage, or it does not. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`: todas las cifras del claim son correctas ($0/mes, 3.000 emails/mes, 100 emails/día, 3 dominios, 3 inboxes, ticket support, 10.000 automation runs, 30 días de retención). La FAQ resuelve la ambigüedad del bloque anterior: sin pay-as-you-go, al superar la cuota "you will be notified and given the option to upgrade to a higher plan", no se cobra excedente — es decir, el Free plan **no** permite exceeded silently.

Confirmado además: no hay trial (solo plan free-forever), el plan Free incluye 1 webhook endpoint y todos los eventos, y la retención de datos es de 30 días. Detalle de la política de descuentos en [[2026-1029-resend-solo-mensual-y-descuento-nonprofit]] y del tracking en [[2026-1029-resend-tracking-por-dominio]].