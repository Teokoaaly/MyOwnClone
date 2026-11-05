---
id: 2026-1029-sentry-pricing-tiers
type: atom
certainty: solid
sources: [0-raw/2026-10-29-sentry-pricing.md]
links: ["[[2026-1029-sentry-pricing-pay-async-errors]]", "[[2026-1029-sentry-pricing-included-resources]]"]
---
## Claim

Sentry offers four pricing tiers: **Developer** (free, $0/mo, limited to one user), **Team** ($26/mo annually, unlimited users), **Business** ($80/mo annually, unlimited custom dashboards), and **Enterprise** (custom pricing, technical account manager + dedicated support). The Developer tier includes Error Monitoring and Tracing for one user only.

## Why It Matters

The tier jump from Developer to Team unlocks unlimited users, API & third-party integrations, 20 custom dashboards, and Seer: AI debugging agent (subscription required). Business adds unlimited custom dashboards, advanced quota management, and SAML + SCIM support. Enterprise replaces fixed tiers with a technical account manager and dedicated support, priced via conversation.

## [FRICTION]

> The pricing page lists **$26/mo billed annually** for Team and **$80/mo billed annually** for Business, but also shows the same prices for monthly billing without clarifying the discount magnitude. The "Save with annual" tag suggests a meaningful discount but the exact percentage is not stated on-page, requiring users to inspect the signup flow or docs for the annual vs. monthly rate split.

> The **50K errors/mo** included in Team tier are shared across all projects in the organization; exceeding 50K triggers pay-as-you-go billing at $0.0003625/error (50K–100K), decreasing to $0.00015/error (20M+). Users migrating from other platforms may underestimate error volume and face unexpected overage charges.

> **Session Replay** shows "50 replays" included across all tiers, but the fine print links to separate Session Replay pricing, and the 50-replay quota may be insufficient for high-traffic applications that rely on replay debugging for every crash.

## Extracted Ideas

- Developer tier: one user only, Error Monitoring + Tracing, 10 custom dashboards, MCP access
- Team tier: unlimited users, API integrations, Seer AI debugging agent, 20 custom dashboards, 50K errors/mo, 5GB logs, 5GB app metrics, 50 replays, 5M spans, 1 uptime monitor, 1 cron monitor, 1 GB attachments
- Business tier: unlimited custom dashboards, advanced quota management, SAML + SCIM, 50K errors/mo (same ceiling), +$0.50/GB additional logs, +$0.50/GB additional app metrics
- Pay-as-you-go error rates: $0.0003625 (50K–100K) → $0.0002188 (100K–500K) → $0.0001875 (500K–10M) → $0.0001625 (10M–20M) → $0.00015 (20M+)
- Profiling pay-as-you-go: UI profiling $0.25/hr, Continuous profiling $0.0315/hr
- Annual billing discount tag present but rate not disclosed on-page