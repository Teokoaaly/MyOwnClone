--- 
id: 2026-1028-newapi-deployment-methods
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-docs-quickstart.md]
links: ["[[2026-1028-newapi-channel-configuration]]", "[[2026-1028-newapi-api-token]]"]
---

## Claim

New API offers four deployment methods — Docker Compose, Docker single container, management panel, and cluster — letting operators choose based on scale: Docker Compose for small services with MySQL/Redis, Docker image for evaluation or small deployments, a management panel for visual instance control, and a cluster for production-scale workloads.

## Why It Matters

The deployment method dictates what operational capabilities are available out of the box: Docker Compose brings MySQL and Redis integration for stateful workloads, the management panel provides a UI for channel and token management, and cluster mode enables horizontal scaling. Choosing the right method upfront avoids re-architectural changes later.

## [FRICTION]

> The quickstart lists four methods but does not compare their feature parity or migration paths. An operator starting with Docker Compose may later need capabilities only available in cluster mode (e.g., horizontal scaling, multi-node load balancing), but the documentation offers no guidance on how or when to transition.

> The "management panel" method is described functionally but without a link to its actual UI or installation guide, making it difficult for new operators to evaluate whether this is a separate product, a plugin, or an embedded interface within one of the Docker options.

> Docker single container is positioned for "evaluation or small deployments" with no explicit ceiling defined, leaving operators uncertain about when they outgrow it and which method to migrate to next.

---
[[2026-1028-newapi-channel-configuration]]
[[2026-1028-newapi-api-token]]