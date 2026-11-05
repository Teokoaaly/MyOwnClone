---
id: 2026-1101-newapi-model-rate-limiting
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-features-introduction.md]
links: ["[[2026-1028-newapi-deployment-methods]]", "[[2026-1028-newapi-api-token]]"]
---
## Claim

New API supports model rate limiting in System Settings - Rate Limit Settings, with two parameters: total request limit and successful request limit per model. These limits govern how many API calls a model can handle within the defined threshold.

## Why It Matters

Rate limiting prevents model overload and ensures fair usage across tenants. The total limit caps all requests regardless of outcome, while the successful limit only counts responses without errors. Operators can configure different thresholds per model, preventing runaway consumption of expensive models while keeping cheaper models available.

## [FRICTION]

> The rate limit settings are applied at the model level but no per-tenant isolation is documented — a single tenant exhausting its rate limit can block other tenants sharing the same model channel, with no weighted or priority-based differentiation.

> No burst-allowance or burst-credit mechanism is described, meaning sudden traffic spikes may immediately trigger rate-limiting errors without a grace period or fallback behavior.

> The distinction between "total request limit" and "successful request limit" is not explained with real-world scenarios: operators may not understand whether failed/retried requests count toward either limit, leading to misconfigured thresholds.

> Rate limits are set globally per model but not per-channel, so a model accessed through multiple channels shares the same quota, which may be invisible to operators managing channel-specific workloads.

---
[[2026-1101-newapi-reasoning-effort-suffix]]
[[2026-1101-newapi-cache-billing]]