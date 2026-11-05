---
id: 2026-1029-resend-add-ons
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-scale-plan]]", "[[2026-1029-resend-pay-as-you-go]]"]
---

## Claim

Resend add-ons cost $20/mo for 100 additional domains, $30/mo for dedicated IPs, and $150/mo for Single Sign-On, available on Pro and Scale plans (SSO as add-on, Dedicated IPs on Scale+).

## Why It Matters

Add-ons let teams scale specific capabilities without upgrading the entire plan. The $20/mo for 100 domains is relevant for SaaS platforms sending from per-customer brand domains — the Free and Pro plans include only 3 and 10 domains respectively, which can be exhausted quickly. At $30/mo, dedicated IPs are available on Scale plan for high-volume senders (>3K emails/day) who need IP reputation control; this is irrelevant for low-volume senders. The $150/mo SSO add-on on Scale plans enables team-wide identity provider integration, closing the gap between self-serve and enterprise SSO inclusion. Teams should evaluate which add-ons map to actual needs, as stacking domains ($20) + IPs ($30) + SSO ($150) = $200/mo in add-ons, which approaches the Scale plan base ($90) and may make a higher tier more cost-effective.

## [FRICTION]

> [[2026-1029-resend-scale-plan]] (written today) includes Dedicated IP "with add-on" suggesting it is not automatically included even at Scale. This note presses that the source states "Available to customers exceeding 3,000 emails sent per day on the Scale plan" — meaning the Dedicated IP add-on is an opt-in cost ($30/mo) even at Scale, not a free benefit. A team exceeding 3K daily emails on Scale must pay extra for IP warming and autoscale, creating a friction point: the $90/mo base + $30/mo IP add-on = $120/mo minimum, which may push teams toward Enterprise pricing sooner than expected. Both notes describe the same source text but emphasize different implications: one treats it as a feature gap, the other as a pricing clarification. Marcado para juicio humano, no auto-resuelto.

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md`: los tres precios del claim son correctos (dominios $20/mes por 100 adicionales, IP dedicada $30/mes, SSO $150/mes). Matices de la misma captura: el add-on de dominios añade **100** dominios sobre los del plan ("This adds 100 more on top of it"), disponible en Pro y Scale y con límite fijado por contrato en Enterprise; el de IP dedicada exige superar 3.000 emails/día en Scale e incluye warming, monitorización y autoescalado; el de SSO está disponible como add-on en Scale e incluido en Enterprise, por lo que en Enterprise su coste efectivo es $0.

Matiz de TCO: el add-on de SSO a $150/mes supera el propio precio del plan Scale ($90/mes) y el de Pro ($20/mes) — para un equipo pequeño, pagar SSO como add-on en Pro no es una opción, solo lo es desde Scale. El nivel Enterprise lo incluye sin coste adicional, lo que hace que $150/mes sea, en la práctica, el precio de acceso real al SSO self-service de Resend. Detalle del nivel en [[2026-1029-resend-plan-enterprise]].