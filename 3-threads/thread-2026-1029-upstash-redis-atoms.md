## upstash-redis-pricing-2026-10-29 — Atoms created from Upstash Redis pricing page capture (2026-10-29)

### Atoms created:

1. **2026-1029-upstash-free-tier** — Upstash Free tier: $0/month, 250 MB data, 10 GB bandwidth, 500K commands. Suitable for prototypes and hobby projects. Links to [[2026-1029-upstash-paygo-model]] and [[2026-1029-upstash-fixed-plans]].

2. **2026-1029-upstash-paygo-model** — Pay as You Go: $0.20 per 100K commands, unlimited commands, 100 GB data, unlimited bandwidth (free up to 200 GB/month, then $0.03/GB). AWS/GCP/FLY/Vercel platforms. Links to [[2026-1029-upstash-free-tier]] and [[2026-1029-upstash-command-billing]].

3. **2026-1029-upstash-fixed-plans** — Fixed plans: $10/month (250 MB, 50 GB) to $1500/month (500 GB, 20 TB), predictable pricing by data size, +$5/+$10/+$50/+$100/+$200/+$400/+$750 per read region. Includes SLA, multi-zone HA, SOC-2. Links to [[2026-1029-upstash-free-tier]] and [[2026-1029-upstash-read-regions]].

4. **2026-1029-upstash-command-billing** — Command billing: $0.20/100K for Pay as You Go; operational commands (AUTH, HELLO, SELECT, COMMAND, CONFIG, INFO, PING, RESET, QUIT) not charged; Fixed plans have no command-count billing. Links to [[2026-1029-upstash-paygo-model]] and [[2026-1029-upstash-storage-bandwidth]].

5. **2026-1029-upstash-storage-bandwidth** — Storage & bandwidth: $0.25/GB beyond first 1 GB free; bandwidth free up to 200 GB/month on pay as you go, then $0.03/GB; Fixed plans include 50 GB–20 TB depending on tier; max data 250 MB–500 GB. Links to [[2026-1029-upstash-command-billing]] and [[2026-1029-upstash-enterprise]].

6. **2026-1029-upstash-read-regions** — Read regions: Fixed plans charge +$5/+$10/+$50/+$100/+$200/+$400/+$750 per read region; provides HA with primary + read replicas across zones; command replication adds to bandwidth usage. Links to [[2026-1029-upstash-fixed-plans]] and [[2026-1029-upstash-enterprise]].

7. **2026-1029-upstash-enterprise** — Enterprise: Custom pricing for 10 TB+ data, unlimited bandwidth; includes all Prod Pack features, dedicated professional support, dedicated technical account manager, unlimited databases, HIPAA compliance, VPC peering, SSO integration, custom contracts. Links to [[2026-1029-upstash-storage-bandwidth]] and [[2026-1029-upstash-prod-pack]].

8. **2026-1029-upstash-prod-pack** — Prod Pack: +$200/month per database; adds uptime SLA, SOC 2 Type 2 report, Prometheus/Grafana/Datadog insights, Insights console, multi-zone high availability, encryption at rest. Available for any plan except Free. Links to [[2026-1029-upstash-enterprise]] and [[2026-1029-upstash-fixed-plans]].

### Cross-atom tensions:

- **Free vs. Pay Go scale**: The free tier's 500K commands vs. Pay as You Go's $0.20/100K creates a dramatic scale difference — the free tier is genuinely only for prototipado, not a soft upgrade path ([[2026-1029-upstash-free-tier]] friction vs. [[2026-1029-upstash-paygo-model]]).

- **Two billing regimes**: Fixed plans bill by data size + bandwidth; Pay as You Go bills by commands. Changing plans mid-month means switching between fundamentally different cost models, and the budget feature on Pay as You Go doesn't impose a hard cost ceiling ([[2026-1029-upstash-command-billing]] friction vs. [[2026-1029-upstash-storage-bandwidth]] vs. [[2026-1029-upstash-paygo-model]]).

- **Read region cost vs. value**: +$5/+$750 per region significantly increases fixed plan costs for multi-region HA, while Enterprise includes multi-zone HA in custom pricing — the per-region add-on may be redundant for users who could move to Enterprise instead ([[2026-1029-upstash-read-regions]] friction vs. [[2026-1029-upstash-enterprise]]).

- **Prod Pack redundancy in Enterprise**: Prod Pack costs +$200/db on Fixed plans, but Enterprise includes "all Prod Pack features" plus dedicated support — paying extra for Prod Pack on Fixed may be unnecessary if Enterprise is an option ([[2026-1029-upstash-prod-pack]] friction vs. [[2026-1029-upstash-enterprise]]).

- **Storage cost universality**: $0.25/GB beyond 1 GB free appears across storage cost discussions, but it's unclear whether Enterprise negotiates exentions or applies the same rate — the cost structure may not be comparable across plan types ([[2026-1029-upstash-storage-bandwidth]] friction vs. [[2026-1029-upstash-enterprise]]).

### Follow-up needed:

- Evaluate whether the per-region add-on on Fixed plans is economically justified vs. moving to Enterprise custom pricing for multi-region workloads.
- Test the budget feature's effectiveness at preventing bill shock on Pay as You Go plans with unpredictable traffic.
- Assess if the command billing distinction (charged vs. not charged) affects real-world optimization strategies for different workload patterns.
- Determine whether the Friction entries between Prod Pack and Enterprise should prompt a consolidation of the two pathways or keep them as distinct user paths.
- Monitor whether the free tier's 500K command limit is sufficient for the intended "prototype only" use case, or if users consistently hit the limit and upgrade.