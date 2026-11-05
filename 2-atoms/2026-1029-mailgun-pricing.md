---
id: 2026-1029-mailgun-pricing
type: atom
certainty: solid
sources: [raw/articles/2026-10-29-mailgun-pricing.md]
links: ["[[2026-10-29-twilio-sendgrid-email-api-pricing]]", "[[2026-1029-resend-pricing]]", "[[2026-1029-twilio-sms-pricing]]"]
---
## Claim

Mailgun offers four tiers (Free, Basic, Foundation, Scale) with progressively lower overage rates: $1.80/1,000 emails for Basic, $1.30/1,000 for Foundation, and $1.10/1,000 for Scale. Validation pricing drops from $1.20/100 to $0.80/100 across the same tiers. Each tier increases the included email quota and adds features (custom domains, log retention, validations, dedicated IPs, SSO), creating a step-function pricing surface where the marginal cost per email decreases as volume increases, but the feature set jumps discretely.

## Why It Matters

The pricing surface rewards volume: at 50k–100k emails/month, the effective cost per 1,000 drops from $1.30 to $1.10, a 15% reduction. However, the feature boundaries are abrupt — SAML SSO, dedicated IP pools, and phone/chat support only appear at the Foundation tier and above. This means a growing business hit a "feature cliff" at 50k emails/mo ($35/mo), after which the next tier adds real operational capabilities but at a 158% price increase ($90/mo). Teams evaluating email infrastructure should model not just the per-email cost but the feature gate positions, because switching plans involves not just cost delta but functional capability loss (e.g., losing 1-day log retention, custom domain limits, or validation quotas).

## [FRICTION]

> The overage rate reduction from $1.30 to $1.10 per 1,000 between Foundation and Scale (15% savings) is attractive, but the $55/mo price jump for 100k vs 50k included emails means the breakeven is at ~417k additional emails/month. Below that volume, Foundation is the cost-optimal choice; above it, Scale saves money but only if the extra features (SAML SSO, dedicated IP pools, phone support) are actually used.

> Mailgun's validations are priced as a separate add-on, but the per-100-rate drops across tiers ($1.20 → $1.20 → $0.80). This creates a friction point: a team sending 50k emails with 5k validations pays $60 (Foundation) vs $40 (Scale), but if they only need 1k validations the cost difference is negligible ($12 vs $8), yet they're forced into the higher tier for the lower per-unit rate.

> The Free plan includes 100 emails/day (≈3,000/mo) with ticket support only, while Basic ($15/mo) gives 10,000 emails/mo with no daily limit but still no validations included. The gap between Free and Basic is a 3.3x volume increase for $15, but the real friction is that validations are not available as a standalone add-on on Free or Basic — they're only included or available as add-on starting at Foundation, meaning teams needing validation must upgrade regardless of email volume.

> Enterprise services (custom features, deliverability services, Rapid Fire Burst SLA) require a sales quote, creating a friction gap between the self-serve Scale plan ($90/mo, 100k emails) and the enterprise tier. There's no published bridge: a team at 100k–250k emails/mo must either stay on Scale (no SAML, no dedicated IP pool included beyond what's already there) or request a quote, introducing sales-cycle delay and potential price uncertainty.