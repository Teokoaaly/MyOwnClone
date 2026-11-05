---
id: 2026-1029-resend-pricing
type: atom
certainty: solid
sources: [sources/2026-10-29-resend-pricing.md]
links: ["[[2026-1029-resend-free-plan]]", "[[2026-1029-resend-pro-plan]]", "[[2026-1029-resend-scale-plan]]", "[[2026-1029-resend-pay-as-you-go]]", "[[2026-1029-resend-add-ons]]", "[[2026-1029-resend-transactional-marketing]]", "[[2026-1029-resend-ai-credits]]", "[[2026-1029-resend-inboxes-model]]"]
---

## Claim

Resend offers four pricing tiers (Free, Pro, Scale) plus pay-as-you-go add-ons, with a clear gradient from $0/mo to $90/mo and overage at $0.90 per 1,000 emails, designed for individuals to enterprise teams.

## Why It Matters

Resend's pricing structure creates a funnel: the Free plan ($0) caps at 3,000 monthly emails with 100/day limit and 3 inboxes, pushing users toward Pro ($20/mo, 50K emails) when volume or feature needs increase. The Pro-to-Scale jump ($90/mo, 100K emails) introduces a "feature cliff" at 50K emails where Dedicated Slack channel, 1K domains, and phone/chat support become available, but at a 355% price increase. Pay-as-you-go ($0.90/1K overage, $1/inbox/mo) extends paid plans without upgrades, but is unavailable to Free plan users. The transactional vs marketing email distinction affects quota counting, and AI credits (5/100/500 across tiers) are a non-trivial differentiator for AI-dependent workflows. Three included inboxes at $1/mo each add modest but cumulative cost. This gradient means platform choice hinges on volume thresholds, feature requirements, and whether the AI and inbox costs align with actual usage patterns.

## Links

- [[2026-1029-resend-free-plan]] — Free tier constraints and daily limit friction
- [[2026-1029-resend-pro-plan]] — Pro vs Scale cost-per-email and feature-gate modeling friction
- [[2026-1029-resend-scale-plan]] — Scale plan volume features and breakeven analysis friction
- [[2026-1029-resend-pay-as-you-go]] — Free-plan overage eligibility and paid-subscription boundary
- [[2026-1029-resend-add-ons]] — Domain, IP, and SSO add-on cost accumulation
- [[2026-1029-resend-transactional-marketing]] — API distinction and quota implications
- [[2026-1029-resend-ai-credits]] — AI credit allocation across tiers
- [[2026-1029-resend-inboxes-model]] — Recurring inbox cost accumulation

## Nota de extensión 2026-11-03
Verificado contra `sources/2026-10-29-resend-pricing.md` (captura archivada el 2026-11-03 en `0-raw/archive/2026-11-03-2026-10-29-resend-pricing.md`). Matiz: el claim de este átomo dice "four pricing tiers (Free, Pro, Scale)" nombrando tres — el cuarto nivel es Enterprise, con precio "Custom" y SLA de 99,99% de uptime; está documentado en [[2026-1029-resend-plan-enterprise]]. El precio de Scale es $90/mes, es decir 4,5× el de Pro ($20/mes).

Átomos nuevos derivados de la misma captura y que amplían este hub:
- [[2026-1029-resend-plan-enterprise]] — nivel Enterprise, SLA 99,99%, CSM dedicado, límites flexibles
- [[2026-1029-resend-solo-mensual-y-descuento-nonprofit]] — sin plan anual, sin trial, 50% para nonprofits
- [[2026-1029-resend-rate-limit-por-equipo]] — el límite de API no mejora al subir de plan
- [[2026-1029-resend-tracking-por-dominio]] — open/click tracking disponible en todos los planes, incluidos Free

Dato de la FAQ que cambia el TCO: no existe plan entre Free y Pro, y si no se habilita pay-as-you-go, al superar la cuota el sistema notifica y ofrece subir de plan en lugar de cobrar excedente.