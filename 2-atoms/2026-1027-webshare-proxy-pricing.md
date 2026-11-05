---
id: 2026-1027-webshare-proxy-pricing
type: atom
certainty: solid
sources: [sources/2026-10-27-webshare-proxy-pricing.md]
links: ["[[2026-1027-proxy-cheap-pricing-limitations]]", "[[2026-1027-proxy-cheap-static-residential-pricing]]", "[[2026-1027-proxy-cheap-rotating-residential-pricing]]"]
---
## Claim

Webshare offers four product lines with distinct pricing models:

- **Proxy Server** (datacenter): Shared, private, or dedicated access. 100–100,000 proxy tiers with volume discounts up to 40% ($0.0299–$0.0179/proxy). Includes 250GB bandwidth, unlimited option. Yearly billing saves 30%.
- **Static Residential (ISP)**: Per-proxy pricing. Starts at $6/month for 20 proxies ($0.30/proxy), drops to $0.225/proxy at 10,000. Includes 250GB bandwidth, unlimited option.
- **Rotating Residential**: Per-GB pricing. Starts at $3.50/GB, drops to $1.40/GB at 3,000GB. Billed monthly based on plan size.
- **Free plan**: 10 shared proxies + 1GB bandwidth, no time limit, no credit card required.

Access tiers (shared/private/dedicated) are orthogonal to proxy type (server/residential/rotating).

## Why It Matters

The pricing structure creates several cost-inversion points:

- **Volume discount geometry**: Better unit prices require larger upfront commitments. The free plan gives 10 proxies at $0.00/proxy but only 1GB bandwidth — an asymmetry where the proxy count and bandwidth have different scaling curves.
- **Product-line choice**: Rotating Residential at $0.78–$3.50/GB vs Static Residential at $0.225–$0.30/proxy. For usage beyond ~1 GB, rotating becomes more economical, but the 3GB minimum order and volume thresholds (4GB, 51GB) create step-cost jumps.
- **Shared vs private/dedicated**: These are access options available across all proxy types, not separate product categories. Users must assess whether shared IPs meet their use case or if private/dedicated is required.
- **Yearly vs monthly**: 30% savings on yearly billing, but requires upfront commitment and accurate volume forecasting.

## [FRICTION]

> The volume discount tiers (100, 1,000, 5,000, 60,000, 100,000 proxies) produce unit prices that decrease step-wise, but the jump from 1,000 ($0.0269/proxy) to 5,000 ($0.0239/proxy) — a 11.5% drop — requires a 5x proxy count increase. Users may over-provision to reach a lower tier, creating waste. The 40% max discount at 60,000+ proxies ($0.0179) versus the free plan's effective $0.00/proxy creates a discontinuity: the "best price" is only accessible at a scale that may be unjustified for most use cases.

> Static Residential pricing starts at $6/month for 20 proxies ($0.30/proxy), which is 10x the per-proxy cost of the Proxy Server free plan's 10-proxy allocation. However, Static Residential includes residential IPs and 250GB bandwidth, whereas the free Proxy Server plan includes no bandwidth allocation beyond the implicit limit. The price differential reflects IP type and bandwidth inclusion, not just proxy count.

> Rotating Residential is priced per-GB ($3.50/GB → $1.40/GB) with no proxy count ceiling, creating a different cost model than proxy-count-based pricing. For short, low-volume tasks, a single Static Mobile proxy at $3.50 may undercut many GB of Rotating Mobile, but for high-throughput rotating needs the per-GB model charges per unit of data regardless of session length, creating a cost inversion point that depends on actual GB consumption per session.

> Yearly billing saves 30% compared to monthly, but the discount is applied to the monthly rate. If actual proxy usage varies month-to-month, the yearly commitment creates either underutilization (paying for unused proxies) or the need to downgrade mid-year. The free plan has no yearly option, making the comparison path-dependent.