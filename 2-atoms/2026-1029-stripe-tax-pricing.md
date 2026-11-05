---
id: 2026-1029-stripe-tax-pricing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-stripe-pricing.md]
links: ["[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1022-stripe-webhook-confirmado]]"]
---

## Claim
Stripe Tax charges **0.5% per transaction** where the business is registered to collect taxes, or **$0.50 per transaction** for API integration, with each transaction including 10 calculation API calls (5¢ per additional call).

## Why It Matters
The 0.5% per-transaction rate provides a predictable percentage cost for businesses collecting sales tax, VAT, or GST across 100+ countries, while the $0.50 API integration fee suits businesses that need custom tax calculation outside of Stripe's hosted checkout flows — each transaction includes 10 free calculation API calls, making low-volume tax compliance affordable.

## [FRICTION]
> [[2026-1022-stripe-planes-trial-30-dias]] requires a card upfront for trial conversions, which creates immediate friction for new users. Tax registration typically requires a verified business entity and tax ID, meaning the 0.5% per-transaction tax cost cannot be activated until after the card-upfront trial completes — creating a sequencing friction where tax compliance is delayed until billing information is provided.