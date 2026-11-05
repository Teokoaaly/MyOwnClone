---
id: 2026-1029-stripe-metronome-billing
type: atom
certainty: solid
sources: [0-raw/2026-10-29-stripe-pricing.md]
links: ["[[2026-1022-stripe-planes-trial-30-dias]]", "[[2026-1022-stripe-webhook-confirmado]]"]
---

## Claim
Stripe Metronome usage-based billing charges **$0.04 per 1K ingest events** and **0.8% of billing volume**, with data export pricing at $0.03 per 1K standard events and $0.05 per 1K premium events.

## Why It Matters
Metronome's dual pricing model — per-event ingest volume plus a percentage of billing volume — serves different billing paradigms: $0.04 per 1K events suits high-frequency, low-value event streams, while 0.8% of billing volume suits lower-frequency, high-value subscription models. The separate data export pricing ($0.03/$0.05 per 1K) adds cost for businesses needing to move billing data to warehouses.

## [FRICTION]
> [[2026-1022-stripe-planes-trial-30-dias]] requires a card upfront for trial conversions, which creates onboarding friction. Usage-based billing with Metronome cannot be activated until billing information is provided, meaning early-stage businesses must commit to card-on-file before they can iterate on pricing models — locking in a pricing architecture before achieving product-market fit.