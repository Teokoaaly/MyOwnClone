---
id: 2026-1029-sentry-pricing-data-retention
type: atom
certainty: solid
sources: [0-raw/2026-10-29-sentry-pricing.md]
links: ["[[2026-1029-sentry-pricing-tiers]]", "[[2026-1029-sentry-pricing-seer-annual]]"]
---
## Claim

Sentry's data retention policies vary by tier: Developer and Team tiers offer a 30-day lookback, Business tier provides up to 90-day lookback, and Enterprise adds "up to 90-day lookback & additional sampled retention." Custom tiers beyond the published brackets have no published retention defaults.

## Why It Matters

Teams investigating incidents over extended periods may find the 30-day limit restrictive, while the jump to 90-day lookback on Business ($80/mo) may be sufficient for most use cases. Enterprise organizations requiring sampled retention beyond 90 days must engage sales, creating a differentiation point between Business and Enterprise.

## [FRICTION]

> The **30-day lookback** is standard across Developer and Team tiers, but Teams running monthly incident reviews or compliance audits may need to extend retention, which is not available as a simple add-on and requires upgrading to Business ($80/mo) or negotiating Enterprise terms.

> The **90-day lookback** on Business tier is a significant improvement, but the fine print specifies "up to 90-day lookback & additional sampled retention" — the "sampled" qualifier means not all events are retained, which may disappoint teams expecting full-event retention beyond 30 days.

> **Custom** retention tiers beyond the published brackets have no disclosed defaults, meaning organizations with specialized compliance requirements (e.g., HIPAA, SOC2, GDPR data residency) must contact sales, creating a friction point for teams that need to plan retention budgets in advance.

> The data retention field does not clearly map to the "lookback" terminology used in other Sentry products (e.g., Session Replay, Tracing), which may cause confusion when correlating retention policies across monitoring types.

## Extracted Ideas

- Developer + Team: 30-day lookback
- Business: up to 90-day lookback
- Enterprise: up to 90-day lookback & additional sampled retention
- Custom: no published defaults, sales engagement required
- Retention maps to compliance needs (HIPAA, SOC2, GDPR data residency)
- "Sampled" qualifier on Enterprise retention means not full-event retention