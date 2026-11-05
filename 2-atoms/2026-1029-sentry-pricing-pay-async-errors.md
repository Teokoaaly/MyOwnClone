---
id: 2026-1029-sentry-pricing-pay-async-errors
type: atom
certainty: solid
sources: [0-raw/2026-10-29-sentry-pricing.md]
links: ["[[2026-1029-sentry-pricing-tiers]]", "[[2026-1029-sentry-pricing-data-retention]]"]
---
## Claim

Sentry's pay-as-you-go error pricing charges per excess error beyond the included quota, with decreasing per-error rates at higher volume tiers: $0.0003625/error (50K–100K), $0.0002188/error (100K–500K), $0.0001875/error (500K–10M), $0.0001625/error (10M–20M), and $0.00015/error (20M+).

## Why It Matters

A team generating 1M errors/mo would pay approximately $187.50/mo in overage on top of the $26 Team tier base, while 5M errors would cost ~$937.50/mo. At 10M+ errors, the per-error cost drops to $0.0001625, making 20M errors cost ~$3,250/mo — but the marginal cost per error continues decreasing beyond 20M.

## [FRICTION]

> The included 50K errors/mo in the Team tier may be insufficient for organizations with widespread SDK coverage, yet the next pricing bracket (100K) more than doubles the included quota while the per-error rate drops only ~40%, creating a perceived misalignment between quota steps and rate steps.

> Users on the Business tier ($80/mo) also receive 50K errors/mo included, meaning two different price points ($26 vs $80) share the same included error quota, while the pay-as-you-go rates are identical across tiers — creating a friction where paying 3× more for Business does not increase the included error bucket.

> The pay-as-you-go rates apply per-organization, not per-project, which can penalize multi-project setups where one high-error project drives up costs for the entire organization.

## Extracted Ideas

- 50K errors/mo included in Team and Business tiers
- Pay-as-you-go tiers: 50K–100K @ $0.0003625, 100K–500K @ $0.0002188, 500K–10M @ $0.0001875, 10M–20M @ $0.0001625, 20M+ @ $0.00015
- Same included quota (50K) across Team and Business, different prices
- Error quota is organization-wide, not project-wide
- 1M errors ≈ $187.50/mo overage; 5M ≈ $937.50/mo; 10M ≈ $1,625/mo; 20M ≈ $3,250/mo