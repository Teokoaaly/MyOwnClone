---
url: https://www.aiven.io/pricing
captured: 2026-10-31
word_count: 2847
status: raw
---
# Plans & Pricing

Aiven's pricing is all-inclusive and transparent, providing you with the confidence and ease to forecast monthly expenses without any surprises from variable costs.

[Find the right plan](https://aiven.io/pricing/calculator)

[Get building](https://console.aiven.io/signup)

[PostgreSQL®](https://aiven.io/pricing/postgresql) [MySQL](https://aiven.io/pricing/mysql) [Valkey™](https://aiven.io/pricing/valkey) [OpenSearch®](https://aiven.io/pricing/opensearch) [Apache Kafka®](https://aiven.io/pricing/kafka) [Apache Kafka® Connect](https://aiven.io/pricing/kafka_connect) [Apache Kafka® MirrorMaker 2](https://aiven.io/pricing/kafka_mirrormaker) [ClickHouse®](https://aiven.io/pricing/clickhouse) [Aiven DataHub](https://aiven.io/pricing/datahub) [Aiven Runtime](https://aiven.io/pricing/runtime) [Metrics](https://aiven.io/pricing/metrics) [Grafana®](https://aiven.io/pricing/grafana)

## PostgreSQL®

Amazon Web Services DigitalOcean Google Cloud Microsoft Azure OVH UpCloud

Region

Asia, Bangalore (blr) Asia, Singapore (sgp) Canada, Toronto (tor) Europe, Frankfurt (fra) Europe, London (lon) Europe, Amsterdam (ams) Australia, Sydney (syd) United States, New York (nyc) United States, San Francisco (sfo)

- ### Free

$0/month

1 dedicated VM

1 CPU per VM

1 GB RAM per VM

1 GB total storage

Cannot select a specific cloud or region

No integrations or connection pooling

- ### Developer

$5/month

1 dedicated VM

1 CPU per VM

1 GB RAM per VM

8 GB total storage

Cannot select a specific cloud or region

No integrations or connection pooling

- ### Hobbyist

starting from

$12/month

$0.02/hour

1 dedicated VM

1 CPU per VM

1 GB RAM per VM

8 GB total storage

- ### Startup

starting from

$75/month

$0.10/hour

1 dedicated VM

2-32 CPU per VM

4-192 GB RAM per VM

80 GB-11 TB total storage

99.99% uptime SLA

- ### Business

starting from

$180/month

$0.25/hour

2 dedicated VM

2-32 CPU per VM

4-192 GB RAM per VM

80 GB-11 TB total storage

Everything in Startup, plus high availability

- ### Premium

starting from

$270/month

$0.37/hour

3 dedicated VM

2-32 CPU per VM

4-192 GB RAM per VM

80 GB-11 TB total storage

Everything in Business, plus a second standby node

Data retention is only limited by storage, with the exception of Free plan. For information about annual discount or plan capacity beyond the listed plans, please contact us.

| PostgreSQL® | Free<br>$0/month | Developer<br>$5/month | Hobbyist<br>starting from<br>$12/month | Startup<br>starting from<br>$75/month | Business<br>starting from<br>$180/month | Premium<br>starting from<br>$270/month |
| --- | --- | --- | --- | --- | --- | --- |
| Dedicated VMs | 1 | 1 | 1 | 1 | 2 | 3 |
| CPU per VM | 1 | 1 | 1 | 2-32 | 2-32 | 2-32 |
| RAM per VM | 1 GB | 1 GB | 1 GB | 4-192 GB | 4-192 GB | 4-192 GB |
| Total storage | 1 GB | 8 GB | 8 GB | 80 GB-11 TB | 80 GB-11 TB | 80 GB-11 TB |
| Clouds | Limited | Limited | DigitalOcean, Google Cloud, OVH | Amazon Web Services, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud | Amazon Web Services, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud | Amazon Web Services, DigitalOcean, Google Cloud, Microsoft Azure, OVH, UpCloud |
| All networking cost included | | | | | | |
| Seamless upgrade/downgrade to other plans | | | | | | |
| One-click version upgrade | | | | | | |
| Extensions (PostGIS, PL/v8, etc) | | | | | | |
| Performance graphs | | | | | | |
| Data encrypted on disk and network | | | | | | |
| Real-time backups to a remote location | | | | | | |
| Restore to any point in time (PITR) | Single backup only for disaster recovery | Single backup only for disaster recovery | Single backup only for disaster recovery | 2 days | 14 days | 30 days |
| VPC peering in AWS, GCP, and Microsoft Azure | | | | | | |
| Multiple logical databases per instance | | | | | | |
| Database forks | | | | | | |
| Connection pooling | | | | | | |
| 99.99% availability | | | | | | |
| High availability | Automatic failover to another node in case of a node failure | | | | | |
| Read-only access to DB replica nodes | | | | | | |
| Dynamic disk sizing | Not available | Not available | Not available | Available at an additional cost | Available at an additional cost | Available at an additional cost |
| Support | Offers three additional support tiers with separate charge that include faster response times and phone support | Support via documentation | Support through email with best-effort responses during the same or next business day | Support through email with best-effort responses during the same or next business day | Support through email with best-effort responses during the same or next business day | Support through email with best-effort responses during the same or next business day |

Bring Your Own Cloud (BYOC) available for larger setups

Run Aiven services in your own cloud account to achieve lower TCO. Our self-service BYOC automation simplifies deployment. Contact us for more information.

### Available marketplaces

![AWS marketplace](https://aiven.io/remix-assets/aws-market-place-DEW6ad2P.avif)![Google marketplace](https://aiven.io/remix-assets/google-market-place-UkcZfndq.avif)![Microsoft marketplace](<Base64-Image-Removed>)![Oracle marketplace](<Base64-Image-Removed>)

## Frequently asked questions

### How does Aiven pricing work?

You pay an hourly rate per service. That rate covers the managed data service itself, the underlying cloud infrastructure, and everything Aiven does to keep it running: provisioning, monitoring, local backups, version upgrades, security patching, and 24/7 reliability operations.

There are no separate line items for high availability, or routine maintenance. What you see on the plan card is what you pay.

Your bill changes only when you change something: choose a larger plan, add extra storage, spin up additional services, upgrade your support tier, or enable BYOC. Services are billed by the hour and invoiced monthly, so you only pay for what you actually run.

### Why does Aiven have different pricing plans?

Aiven pricing is designed to make production data infrastructure performant and predictable. Instead of paying separately for infrastructure and managing operations yourself, you choose the service, cloud/region, and plan size that fits your workload, and Aiven manages the operational work behind that service.

We recognize that buyers are often in a different stage of adoption or maturity. For example, a developer experimenting with PostgreSQL does not need the same availability, backup retention, capacity, and support as a bank running Kafka for critical production workloads.

General plan guidance:

| Environment or workload | Recommended plan type | When to select |
| --- | --- | --- |
| Learning, demos, tutorials | Free | A real Aiven experience at no cost. |
| Development | Developer | Affordable, non-production managed service. Ideal for experimenting and prototyping. |
| Production | Startup | Best for lightweight staging or smaller workloads. |
| Production | Business | Choose the Business plan when high availability and greater throughput matter. |
| Production | Premium | Optimized performance, speed, and availability for enterprise-grade work. |

### How does Aiven pricing compare to similar services offered by hyperscalers?

Many organizations focus only on the infrastructure bill and miss the costs associated with engineering labor, manual maintenance, and incident response. While a hyperscaler's raw compute might appear cheaper on a list price, they typically meter networking, backups, data writes and reads, and high availability separately, which can lead to unpredictable monthly expenses and "bill shock."

When you add those costs up, plus the ongoing cost of your team managing it, the gap closes quickly, and often inverts.

Aiven bundles the software, infrastructure, and the operational expertise into a single, predictable hourly rate. High availability, security hardening, and version upgrades are standard — not add-ons. Your engineers focus on building products and data pipelines, not on running infrastructure or maintaining open source software.

### How does Aiven pricing compare to service-specific vendors?

Service-specific vendors often go deep on one technology. Aiven goes broad across the full data stack, and prices it more transparently.

The key differences:

Feature gating. Service-specific vendors often tier their pricing by feature access: connectors, audit logs, role-based access, or advanced security are locked to higher tiers. On Aiven, operational features like monitoring, backups, and access controls are standard across plans, not premium add-ons.

Consumption-based compounding. Vendors often charge by ingest volume, partition count, or connector usage, costs that are hard to predict and compound as your usage grows. Aiven's plan-based pricing makes your bill reflect the size of your workload, not the granularity of how you use the service.

Single-service lock-in. If you use Confluent for Kafka, you still need a separate contract for your database, your search layer, and your caching layer, each with its own support line, pricing model, and renewal cycle. Aiven gives you Kafka, PostgreSQL, OpenSearch, ClickHouse, Valkey, and more under one platform, one contract, and one invoice.

Multi-cloud and portability. Most service-specific vendors are tied to one or two clouds. Aiven runs on AWS, Google Cloud, Azure, and others, in 100+ regions — with the same operational experience everywhere.

How is Aiven Runtime billed?

Aiven Runtime bills like every other Aiven service: an hourly rate for your plan, starting when your app is created and running until you power it off or delete it. There's no separate charge for build time or idle periods.

What future price changes are planned?

Billing will move to usage-based, including active app runtime, plus applicable storage and network egress costs.

Can I change my application plan later?

Yes. You can scale your application by changing the application plan directly in the Aiven Console.

STOP MANAGING, START BUILDING

[Get building](https://console.aiven.io/signup)