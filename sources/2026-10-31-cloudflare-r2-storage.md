---
url: https://www.cloudflare.com/developer-platform/products/r2/
captured: 2026-10-31
word_count: 1987
status: raw
---
# Cloudflare R2 - Egress-Free Object Storage

## Scalable, durable, affordable object storage

Build stateful applications that read and write data globally, integrate directly with Workers, and scale without infrastructure overhead or surprise storage costs.

[Start building for free](https://dash.cloudflare.com/sign-up) [View docs](https://developers.cloudflare.com/r2/)

### Near-infinite scale

Access data from anywhere, create millions of buckets, and write as much data as you need to run your business.

### Sleep better

Don't wake up to a huge egress bill overnight: R2 doesn't charge for egress.

### S3-compatible APIs

R2 exposes S3 compatible APIs: use your existing tools without a rewrite.

### Progressive migration

R2 can sit in front of your legacy object storage provider and progressively copy objects as they are requested, taking the complexity out of managing data migration.

### R2 Data Catalog

Use R2's Iceberg-compatible data catalog with your favorite SQL data warehouse to query logs and structured data formats you store in R2.

### Part of Cloudflare Workers

Access your R2 buckets directly from your Workers code without having to juggle API keys and SDKs with a native Workers API.

Store anything, serve everywhere

R2 is globally distributed object storage designed for modern applications. Durable, S3-compatible, and tightly integrated with Workers for building data-driven systems without extra infrastructure.

See more

Store application data without egregious egress fees

Download your data from R2 without worrying that your egress bill is scaling 1:1 with your growth. Store and access user content, AI training data, logs and columnar data without breaking the bank.

Store AI datasets and model artifacts

Keep training data, model weights, and analytics datasets accessible from any cloud provider without transfer fees. Data portability enables better infrastructure choices.

Break free from cloud vendor lock-in

Store your data neutrally and access it from any cloud provider for compute workloads. Choose the best tools without being trapped by transfer costs.

Migration without the risk

Configure R2 to pull objects from your existing object storage provider as they are requested, allowing you to switch to R2 without having to manage large-scale data migration and benefit from zero-egress fees immediately.

### Drop-in replacement for existing S3 workflows

Switch your endpoints to R2 and keep using your current tools, SDKs, and pipelines. R2's S3-compatible API makes migration frictionless.

config.py  index.ts  query.sql

1  2  3  4  5  6  7

```import boto3
s3 = boto3.resource('s3',  endpoint_url = 'https://{your-account-id}.r2.cloudflarestorage.com',  aws_access_key_id = '{access_key_id}',  aws_secret_access_key = '{access_key_secret}')
```

01  02  03  04  05  06  07  08  09  10  11

```export default {
  async fetch(request, env) {
    let key = new URL(request.url).searchParams.get('key');
    // Write an object to R2 directly
    await env.MY_BUCKET.put(key, request.body);
    // Fetch an object (or objects!) using the Workers API:
    const object = await env.MY_BUCKET.get(key);
    return new Response(object);
  },
}
```

01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21

```-- Install the iceberg DuckDB extension and load the extension.
INSTALL iceberg;LOAD iceberg;

-- Create a DuckDB secret to store Basin Catalog credentials.
CREATE SECRET r2_secret (
  TYPE ICEBERG,
  TOKEN '<token>');

-- Attach your Basin Catalog
ATTACH '<warehouse_name>' AS prod_analytics_data (
  TYPE ICEBERG,
  ENDPOINT '<catalog_uri>');

-- Show all available tables.
SHOW ALL TABLES;

-- Query your Iceberg table.
SELECT * FROM prod_analytics_data.default.user_events;
```

S3-compatible

R2's S3 compatible API means that you can easily migrate to R2 without having to rewrite your code or change the tools your team is using.

Build applications using Workers and R2

Straightforward APIs that allow you directly access R2 from Cloudflare Workers.

Query Data in R2

Use R2's native Iceberg-compatible Data Catalog to manage schemas and query structured data stored in R2 with your favorite query engine or ETL tool, including DuckDB, Spark, Trino or Snowflake.

Character.AI

"R2 has been the glue behind our multi-cloud architecture for training and processing requests. We are now able to store our training and production data in R2 for access by any cloud, without egress fees, and get the best prices and performance across multiple cloud providers."

Myle Ott

Founding Researcher

### R2 Pricing

Object storage without egress fees. View Storage & Data pricing details

Component | Free | Paid
--- | --- | ---
Standard Storage | Free | 10 GB-month | Paid | $0.015 / GB-month
Standard Class A operations | Free | 1 million | Paid | $4.50 / million requests
Standard Class B operations | Free | 10 million | Paid | $0.36 / million requests
Infrequent Access Storage | Free | — | Paid | $0.01 / GB-month
Infrequent Access Class A operations | Free | — | Paid | $9.00 / million requests
Infrequent Access Class B operations | Free | — | Paid | $0.90 / million requests
Infrequent Access Data Retrieval | Free | — | Paid | $0.01 / GB

### Powerful primitives, seamlessly integrated

Built on systems powering 20% of the Internet, R2 runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard.

Compute | Browser Run | Containers | Durable Objects | Workers | Workers for Platforms | Workflows | Storage | Artifacts | D1 | Basin | Hyperdrive | K2 | Queues | KV | AI | Agents | AI Gateway | AI Search | Vectorize | Workers AI | SASE / Zero Touch | SASE | Access | CASB | DLP | Gateway | Browser Isolation | Bot Management | Network & Content Delivery | CDN | DNS | Load Balancing | TURN / SFU | Analytics | Analytics | Web Performance & Security

Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required.

[Start building for free](https://dash.cloudflare.com/sign-up) [View docs](https://developers.cloudflare.com/)