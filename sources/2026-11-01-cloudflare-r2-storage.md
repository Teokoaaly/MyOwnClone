---
url: https://www.cloudflare.com/developer-platform/products/r2/
captured: 2026-11-01
word_count: 1311
status: raw
---
[](https://www.cloudflare.com/)

[Products](https://www.cloudflare.com/products/)[Solutions](https://www.cloudflare.com/solutions/)[Resources](https://www.cloudflare.com/resource-hub/)[Pricing](https://www.cloudflare.com/plans/)

[Login](https://dash.cloudflare.com/login)[Dashboard](https://dash.cloudflare.com/)[Contact sales](https://www.cloudflare.com/resource/contact-enterprise-sales/)

[Start building](https://dash.cloudflare.com/sign-up)[Dashboard](https://dash.cloudflare.com/)

[Login](https://dash.cloudflare.com/login)

R2

[React Flow](https://reactflow.dev/)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

# Scalable, durable, affordable object storage

### Build stateful applications that read and write data globally, integrate directly with Workers, and scale without infrastructure overhead or surprise storage costs.

[Start building for free](https://dash.cloudflare.com/sign-up)[View docs](https://developers.cloudflare.com/r2/)

**Near-infinite scale**

Access data from anywhere, create millions of buckets, and write as much data as you need to run your business.

**Sleep better**

Don't wake up to a huge egress bill overnight: R2 doesn't charge for egress.

**S3-compatible APIs**

R2 exposes S3 compatible APIs: use your existing tools without a rewrite.

**Progressive migration**

R2 can sit in front of your legacy object storage provider and progressively copy objects as they are requested, taking the complexity out of managing data migration.

**R2 Data Catalog**

Use R2's Iceberg-compatible data catalog with your favorite SQL data warehouse to query logs and structured data formats you store in R2.

**Part of Cloudflare Workers**

Access your R2 buckets directly from your Workers code without having to juggle API keys and SDKs with a native Workers API.

![Image 2: Background Pattern](https://www.cloudflare.com/static/pattern.png)

`R2`

#### Store anything, serve everywhere

R2 is globally distributed object storage designed for modern applications. Durable, S3-compatible, and tightly integrated with Workers for building data-driven systems without extra infrastructure.

[See more](https://developers.cloudflare.com/r2/)

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

![Image 3: Background Pattern](https://www.cloudflare.com/static/pattern.png)

 config.py  index.ts  query.sql 

 1  2  3  4  5  6  7 

```
import boto3
s3 = boto3.resource('s3',  endpoint_url = 'https://{your-account-id}.r2.cloudflarestorage.com',  aws_access_key_id = '{access_key_id}',  aws_secret_access_key = '{access_key_secret}')
```

 01  02  03  04  05  06  07  08  09  10  11 

```
export default {  async fetch(request, env) {    let key = new URL(request.url).searchParams.get('key');    // Write an object to R2 directly    await env.MY_BUCKET.put(key, request.body);
    // Fetch an object (or objects!) using the Workers API:    const object = await env.MY_BUCKET.get(key);    return new Response(object);  },};
```

 01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21 

```
-- Install the iceberg DuckDB extension and load the extension.INSTALL iceberg;LOAD iceberg;
-- Create a DuckDB secret to store Basin Catalog credentials.CREATE SECRET r2_secret (    TYPE ICEBERG,    TOKEN '<token>');
-- Attach your Basin CatalogATTACH '<warehouse_name>' AS prod_analytics_data (    TYPE ICEBERG,    ENDPOINT '<catalog_uri>');
-- Show all available tables.SHOW ALL TABLES;
-- Query your Iceberg table.SELECT * FROM prod_analytics_data.default.user_events;
```

S3-compatible

R2's S3 compatible API means that you can easily migrate to R2 without having to rewrite your code or change the tools your team is using.
Build applications using Workers and R2

Straightforward APIs that allow you directly access R2 from Cloudflare Workers.
Query Data in R2

Use R2's native Iceberg-compatible [Data Catalog](https://developers.cloudflare.com/r2/data-catalog/) to manage schemas and query structured data stored in R2 with your favorite query engine or ETL tool, including DuckDB, Spark, Trino or Snowflake.

Character.AI

#### "

#### R2 has been the glue behind our multi-cloud architecture for training and processing requests. We are now able to store our training and production data in R2 for access by any cloud, without egress fees, and get the best prices and performance across multiple cloud providers. "

![Image 4: Myle Ott](https://www.cloudflare.com/people/myle-ott.png)

 Myle Ott  Founding Researcher 

### R2 Pricing

Object storage without egress fees. [View Storage & Data pricing details](https://www.cloudflare.com/plans/#developer-platform/storage)

Component

Free

Paid

Standard Storage

Free

10 GB-month

Paid

$0.015 / GB-month

Standard Class A operations

Free

1 million

Paid

$4.50 / million requests

Standard Class B operations

Free

10 million

Paid

$0.36 / million requests

Infrequent Access Storage

Free

—

Paid

$0.01 / GB-month

Infrequent Access Class A operations

Free

—

Paid

$9.00 / million requests

Infrequent Access Class B operations

Free

—

Paid

$0.90 / million requests

Infrequent Access Data Retrieval

Free

—

Paid

$0.01 / GB

### Powerful primitives, seamlessly integrated

##### Built on systems powering 20% of the Internet, R2 runs on the same infrastructure Cloudflare uses to build Cloudflare. Enterprise-grade reliability, security, and performance are standard.

[Compute](https://www.cloudflare.com/products/#compute)

[Browser Run Automated browsers](https://www.cloudflare.com/products/browser-run/)[Containers Any language, anywhere](https://www.cloudflare.com/products/containers/)[Durable Objects Stateful compute](https://www.cloudflare.com/products/durable-objects/)[Sandboxes Secure code execution](https://www.cloudflare.com/products/sandboxes/)[Workers Global serverless functions](https://www.cloudflare.com/products/workers/)[Workers for Platforms Programmable Platform Solutions](https://www.cloudflare.com/products/workers-for-platforms/)[Workflows Process orchestration](https://www.cloudflare.com/products/workflows/)

[Storage](https://www.cloudflare.com/products/#storage)

[Artifacts Git-native versioned storage](https://www.cloudflare.com/products/artifacts/)[D1 Serverless SQL](https://www.cloudflare.com/products/d1/)[Basin Ingest, catalog & query data](https://www.cloudflare.com/products/data-platform/)[Hyperdrive Global databases](https://www.cloudflare.com/products/hyperdrive/)[K2 Publish and subscribe to durable, ordered event streams](https://www.cloudflare.com/products/k2/)[Queues Message processing](https://www.cloudflare.com/products/queues/)[R2 Egress-free storage](https://www.cloudflare.com/products/r2/)[KV Ultra-fast key-value storage](https://www.cloudflare.com/products/kv/)

[AI](https://www.cloudflare.com/products/#ai)

[Agents Build stateful AI agents](https://www.cloudflare.com/products/agents/)[AI Gateway AI observability](https://www.cloudflare.com/products/ai-gateway/)[AI Search Instant retrieval](https://www.cloudflare.com/products/ai-search/)[Vectorize Vector database](https://www.cloudflare.com/products/vectorize/)[Workers AI Edge AI models](https://www.cloudflare.com/products/workers-ai/)

[SASE / Zero Trust](https://www.cloudflare.com/products/#sase)

[SASE Cloudflare SASE platform](https://www.cloudflare.com/sase/)[Access Zero trust access to private resources](https://www.cloudflare.com/products/access/)[CASB SaaS and cloud posture](https://www.cloudflare.com/products/casb/)[Data Loss Prevention Protect sensitive data](https://www.cloudflare.com/products/dlp/)[Gateway Web filtering](https://www.cloudflare.com/products/gateway/)[Browser Isolation Secure web browsing](https://www.cloudflare.com/products/browser-isolation/)[WAN Cloud-delivered networking](https://www.cloudflare.com/products/wan/)[Email Security Phishing protection](https://www.cloudflare.com/products/email-security/)

[Security](https://www.cloudflare.com/products/#security)

[DDoS Protection Mitigation Solutions](https://www.cloudflare.com/products/ddos/)[Rate Limiting Abuse prevention](https://www.cloudflare.com/products/rate-limiting/)[SSL Secure Your Site with SSL](https://www.cloudflare.com/products/ssl/)[Turnstile A CAPTCHA Replacement Solution](https://www.cloudflare.com/products/turnstile/)[WAF Web Application Firewall](https://www.cloudflare.com/products/waf/)[Magic Transit DDoS Protection for Networks](https://www.cloudflare.com/products/magic-transit/)[Client-Side Security Prevent browser supply chain attacks](https://www.cloudflare.com/products/client-side-security/)[Bot Management Block bad bots](https://www.cloudflare.com/products/bot-management/)

[Network & Content Delivery](https://www.cloudflare.com/products/#network)

[CDN Faster delivery & caching](https://www.cloudflare.com/products/cdn/)[DNS Fast DNS](https://www.cloudflare.com/products/dns/)[Load Balancing Zero downtime](https://www.cloudflare.com/products/load-balancing/)[TURN / SFU Real-time infra](https://www.cloudflare.com/products/turn-sfu/)[Analytics Web Performance & Security](https://www.cloudflare.com/products/analytics/)

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required.

[Start building for free](https://dash.cloudflare.com/sign-up)[View docs](https://developers.cloudflare.com/)

 No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 

 No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet  No cold starts or region complexity  SASE and Zero Trust without the complexity  Deploy to 330+ cities instantly  Defend against the Internet's biggest DDoS attacks  Predictable pricing without surprises  Identity-aware Zero Trust access that retires your VPN  Battle-tested infrastructure powering millions  CDN, WAF, and DNS faster than the public Internet 

 Getting started 

[Plans](https://www.cloudflare.com/plans/)[Contact sales](https://www.cloudflare.com/resource/contact-enterprise-sales/)[Partners](https://www.cloudflare.com/partners/)[Find a partner](https://partnerlocator.cloudflare.com/dashboard)[Startups](https://www.cloudflare.com/startups/)[Under attack?](https://www.cloudflare.com/under-attack-hotline/)[Domain name search](https://www.cloudflare.com/domains/)

 Company 

[About](https://www.cloudflare.com/about/)[Careers](https://www.cloudflare.com/careers/)[Investors](https://cloudflare.net/)[Press](https://www.cloudflare.com/press/)[Press kit](https://www.cloudflare.com/press/press-kit/)[Global network](https://www.cloudflare.com/network/)

 Public interest 

[Project Galileo](https://www.cloudflare.com/galileo/)[Athenian Project](https://www.cloudflare.com/athenian/)[Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/)[Project Fairshot](https://www.cloudflare.com/fair-shot/)[Impact](https://www.cloudflare.com/impact/)

 Compliance 

[Compliance resources](https://www.cloudflare.com/trust-hub/compliance-resources/)[Trust Hub](https://www.cloudflare.com/trust-hub/)[Data Protection](https://www.cloudflare.com/trust-hub/gdpr/)[Responsible AI](https://www.cloudflare.com/trust-hub/responsible-ai/)[Transparency report](https://www.cloudflare.com/transparency/)[Report abuse](https://www.cloudflare.com/trust-hub/abuse-approach/)

 Resources 

[App innovation report](https://www.cloudflare.com/resource/app-innovation-report/)[Cloudflare Radar](https://radar.cloudflare.com/)[Case studies](https://www.cloudflare.com/case-studies/)[Status](https://www.cloudflarestatus.com/)[Support](https://support.cloudflare.com/)[Events](https://www.cloudflare.com/events/)[Blog](https://blog.cloudflare.com/)

 Developers 

[Documentation](https://developers.cloudflare.com/)[Learning center](https://www.cloudflare.com/learning/)[Community](https://www.cloudflare.com/community/)

 Solutions 

[SSE and SASE platform](https://www.cloudflare.com/sase/)[Cloudflare AI Cloud](https://www.cloudflare.com/solutions/ai/)[AI Security](https://www.cloudflare.com/solutions/ai-security/)[Frontend Development Platform](https://www.cloudflare.com/solutions/frontends/)[Multi-Tenant Platform Development](https://www.cloudflare.com/solutions/platforms/)[Web Security Platform](https://www.cloudflare.com/solutions/security/)

[Start Building](https://dash.cloudflare.com/sign-up)[Log In](https://dash.cloudflare.com/login)

© 2026 Cloudflare, Inc.

[Privacy policy](https://www.cloudflare.com/policies/privacy/)|[Report security issues](https://www.cloudflare.com/disclosure/)|[Terms of use](https://www.cloudflare.com/policies/terms/)|[Trademark](https://www.cloudflare.com/trademark/)

|Your privacy choices
