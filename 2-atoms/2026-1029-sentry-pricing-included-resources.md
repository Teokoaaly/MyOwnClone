---
id: 2026-1029-sentry-pricing-included-resources
type: atom
certainty: solid
sources: [0-raw/2026-10-29-sentry-pricing.md]
links: ["[[2026-1029-sentry-pricing-tiers]]", "[[2026-1029-sentry-pricing-pay-async-errors]]"]
---
## Claim

Sentry's pricing tiers include specific quotas for logs, application metrics, session replays, spans, uptime monitors, cron monitors, and attachments, with additional usage billed at $0.50/GB for logs and app metrics, $1.00 per additional uptime monitor, $0.78 per additional cron monitor, and custom pricing for exceeding build monitor limits.

## Why It Matters

The Team tier includes 5GB logs, 5GB application metrics, 50 session replays, 5M spans, 1 uptime monitor, 1 cron monitor, and 1 GB attachments. Business tier raises the dashboard ceiling but keeps the same included quotas for logs, metrics, replays, and spans, meaning the primary upgrade is advanced quota management, SAML/SCIM, and unlimited custom dashboards rather than larger buckets.

## [FRICTION]

> All three main tiers (Developer, Team, Business) include **5GB logs** and **5GB application metrics** at no additional included quota — overage is $0.50/GB across the board. This means the $54 price difference between Team and Business yields no additional log or metric quota, only dashboard and compliance features.

> **Session Replay** quota is fixed at 50 replays/mo across all tiers; organizations requiring replay-driven debugging at scale must either cap usage or pay add-on costs not explicitly listed on the pricing page, creating a discoverability friction.

> **Tracing/Spans** includes 5M spans across all tiers; teams with high-cardinality tracing (AI agent traces, distributed systems) may exhaust this quota and face unclear upgrade paths, as the next bracket is "Custom" without a published incremental rate.

> The **1 uptime monitor** and **1 cron monitor** included are organizational-level limits; teams managing multiple applications may need to pay $1.00/mo per additional uptime monitor or $0.78/mo per additional cron monitor, but these add-on costs are only visible after selecting a tier or starting signup.

## Extracted Ideas

- Included per tier: 5GB logs, 5GB app metrics, 50 replays, 5M spans, 1 uptime monitor, 1 cron monitor, 1 GB attachments
- Overage: $0.50/GB for logs and app metrics; $1.00/uptime monitor additional; $0.78/cron monitor additional
- All main tiers share the same included quotas for logs, metrics, replays, spans — the differentiators are dashboards, compliance, and AI features
- Session Replay: 50/mo across all tiers, no published add-on rate
- Tracing: 5M spans across all tiers, "Custom" beyond that
- Uptime: 1 monitor included, $1.00/additional; Cron: 1 monitor included, $0.78/additional
- Attachments: 1GB included, custom beyond that
- Build monitors: unlimited build monitors included, custom beyond that