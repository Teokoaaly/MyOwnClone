---
id: 2026-1029-stripe-financial-connections-verification
type: atom
certainty: solid
sources: [0-raw/2026-10-29-stripe-pricing.md]
links: ["[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1022-stripe-webhook-confirmado]]"]
---

## Claim
Stripe Financial Connections charges **$1.50 per successful instant verification** and **$0.10 per successful API call** for retrieving tokenized account numbers, with micro-deposit verifications free.

## Why It Matters
Instant bank verification at $1.50 per check provides a faster alternative to micro-deposit verifications (which are free but slower), enabling real-time underwriting and payment failure prevention. The $0.10 API call fee applies to balance retrieval and other account data queries beyond instant verification.

## [FRICTION]
> [[2026-1022-stripe-planes-trial-30-dias]] requires a card upfront for trial conversions, creating immediate friction for new users. Financial Connections instant verification offers a cardless onboarding path at $1.50 per verification, but this per-check cost can discourage high-frequency verification use cases compared to the free (but slower) micro-deposit alternative.