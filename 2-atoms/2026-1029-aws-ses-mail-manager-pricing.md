---
id: 2026-1029-aws-ses-mail-manager-pricing
type: atom
certainty: solid
sources: [sources/2026-10-29-aws-ses-pricing.md]
links: ["[[2026-1029-aws-ses-ala-carte-pricing]]", "[[2026-1029-aws-ses-three-pricing-plans]]"]
---

## Claim
Mail Manager add-on pricing: email processing $0.15 per 1,000 emails ($0.10/1K beyond the first recipient when using Send to Internet rule), archiving $2 per GB of emails ingested plus $0.19 per GB per month for storage and search, Open ingress endpoint $50 per month per endpoint (charged even when status is "Closed"), and mTLS ingress endpoint $50 per month per endpoint with Trend Micro ($0.1875/1K) or SpamHaus ($0.125/1K) or Abusix Guardian ($0.125/1K) or Vade ($0.415/1K) email add-ons.

## Why It Matters
Mail Manager costs are separate from plan-level per-1K rates and can dominate total spend at high inbound volumes; the $50/month charge per ingress endpoint persists even when the endpoint is closed, which is a critical cost-avoidance consideration.

## [FRICTION]
> No friction detected. Mail Manager pricing detail with no contradicting prior atoms.