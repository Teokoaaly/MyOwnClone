---
id: 2026-10-29-posthog-billing-limits
type: atom
certainty: solid
sources: [sources/2026-10-29-posthog-pricing.md]
links: ["[[2026-10-29-posthog-free-tier]]", "[[2026-10-29-posthog-data-retention]]"]
---

## Claim
Billing limits: can set billing limits on most products separately in organization billing. If usage hits the limit, additional events are dropped and feature flags return default quota-limited response. PostHog will never charge more than the set billing limit (except Logs custom retention, which the limit doesn't cap).

## Why It Matters
Billing limits are the primary risk-mitigation feature — they prevent surprise bills from viral growth or tracking mistakes. The ability to set per-product limits means organizations can be aggressive with analytics while keeping logs or other expensive products conservative. This is the safety valve that makes the pay-as-you-go model practical for production use.

---