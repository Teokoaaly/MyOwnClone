---
id: 2026-1029-resend-pay-as-you-go
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-scale-plan]]", "[[2026-1029-resend-inboxes-model]]"]
---

## Claim

Resend's pay-as-you-go pricing charges $0.90 per 1,000 emails over the plan quota, $1 per additional inbox per month, and $0.0015 per automation run beyond free limits, available only to paid subscriptions.

## Why It Matters

Pay-as-you-go extends paid plans beyond their included quota without requiring plan upgrades. At $0.90/1K, a team sending 10K overage emails pays $9; at 100K overage, $90 — equal to a full Scale plan tier. The $1/inbox/mo charge applies to additional inboxes beyond the 3 included on paid plans, with inbox emails counting against the transactional quota. At $0.0015 per automation run, the free 10K monthly runs provide a meaningful buffer for light users. Critically, pay-as-you-go is available only to paid subscriptions (Pro or Scale), meaning Free plan users cannot enable it — if they exceed 3K emails, they must upgrade or stop sending. This creates a hard boundary between Free and paid plans that does not exist self-serve for overage.

## [FRICTION]

> [[2026-1029-resend-free-plan]] (written today) states the Free plan includes 3,000 emails/mo with no mention of pay-as-you-go eligibility. This note presses that the source explicitly says pay-as-you-go is "Available to paid subscriptions," yet the Fine print on inbox pricing implies pay-as-you-go can be enabled on paid plans only, leaving open whether Free-plan users who exceed 3K simply lose service or are blocked entirely. Both cannot be completely correct: either Free plan users can enable pay-as-you-go (contradicting the source's explicit limitation), or they cannot (leaving no path past the 3K quota without upgrading). Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`: las tres cifras del claim son correctas ($0,90/1.000 emails, $1/inbox/mes, $0,0015 por automation run) y la limitación a suscripciones de pago queda confirmada en los tres bloques de la página.

Dato adicional: los excedentes se facturan en cubos de 1.000 emails al precio de excedente del plan, y se habilitan en los ajustes del equipo bajo "Transactional Overages". La FAQ añade que si no se habilita pay-as-you-go y se supera el límite, se notifica y se ofrece subir de plan — se cierra así la ambigüedad del bloque anterior en el sentido de que el Free plan no admite excedente. Detalle del nivel Enterprise en [[2026-1029-resend-plan-enterprise]].