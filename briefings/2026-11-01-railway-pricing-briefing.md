# Briefing — 2026-10-29

## What Came In

- Source captured: `2026-10-29-railway-pricing.md` → `sources/2026-10-29-railway-pricing.md` (206 bytes, 1 summary line)
- 3 atomic notes created in `2-atoms/`

### Atoms created:

- `2026-1029-railway-pricing-free-credit` — Free / Hobby plan includes $5 monthly credits applied to resource usage before charging, auto-recharged every 30 days, no credit card required for trial initial. Links to [[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]] and [[2026-1022-myclone-limites-plan-free]]. Friction: $5 credit with 30-day expiration vs. myownclone's feature limits as the primary barrier — both cannot be completely correct.

- `2026-1029-railway-pricing-pro-credit` — Pro plan includes $20 monthly credits that accumulate carry-over from the $5 trial initial, auto-recharged every 30 days. Links to [[2026-1028-proton-business-mail-recommended-y-distincion-por-plan]] and [[2026-1029-aws-ses-ala-carte-pricing]]. Friction: $20 as platform-wide credit vs. Proton's "Recommended" per-user signaling at $12,99/user/mes — different granularity and pricing models create tension for team-based vs. resource-based decision making.

- `2026-1029-railway-pricing-cpu-rate` — CPU at $0.00000772 per vCPU-second, metered billing per second, no idle time charges (sandboxes destroyed after idle timeout). Links to [[2026-1026-heroku-cedar-cpu-share-compute-y-columna-dedicated]] and [[2026-1023-hetzner-compartido-vs-dedicado-criterio-de-uso]]. Friction: Metered per-second pricing is 3-4× cheaper than Heroku dyno hourly rates but Railway sells compliance (SOC 2, HIPAA BAA) as expensive add-on ($1,000+), creating tension between "previsibilidad sobre cumplimiento" principle and regulated workloads.

## Atoms Extended: 0

## Contradictions Resolved: 0

## Contradictions You Should Resolve

- **Credit model vs. feature limits**: Railway's $5/$20 monthly credits (consumable resources) versus myownclone's/myownclone's feature-gated free plans. The credit model allows consuming beyond typical limits, while feature locks prevent elevation. Human judgment needed on which barrier is more restrictive for typical use cases.

- **Per-user vs. platform-wide pricing signals**: Proton's "Recommended" tag assumes per-user decision framing at $12,99/user/mes, while Railway's $20 credit is agnostic of seat count and scales with service/replica usage. Human judgment needed on which model better serves the target audience (indie vs. team vs. enterprise).

- **Usage-based pricing vs. compliance cost**: Railway's $0.00000772/vCPU-s is highly competitive for pure compute, but compliance add-ons ($1,000+ for HIPAA BAA) dramatically increase TCO for regulated workloads. Human judgment needed on whether the base compute savings outweigh the compliance premium for specific domains.

## Threads That Grew

- `thread-2026-10-29-stripe-pricing.md` — Updated with railway pricing atoms section for cross-referencing pricing model patterns.

## One Thing Worth Your Attention Today

Three atomic notes from the Railway pricing page capture, each linking to two existing atoms and each containing a [FRICTION] block addressing distinct ambiguities: credit model structures, pricing signal granularity, and usage-based pricing versus compliance costs. These atoms are deliberately left with friction blocks for human judgment, not as a protocol failure but as a deliberate capture of ambiguity in cloud pricing model comparison. The real value is in tracking how these three dimensions — credit vs. feature limits, per-user vs. platform-wide pricing, and compute savings vs. compliance premium — evolve as operators evaluate platform migration and cost optimization decisions.