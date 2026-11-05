---
id: 2026-10-29-workers-ai
type: atom
certainty: solid
sources: ["0-raw/2026-10-29-cloudflare-workers-pricing.md"]
links: ["[[2026-10-29-browser-rendering]]", "[[2026-10-29-vectorize]]"]
---

## Claim

Workers AI charges $0.011 per thousand neurons after 10,000 neurons per day are free.

## Why It Matters

Workers AI provides edge AI model inference. The 10K/day free neuron tier covers light usage, and at $0.011/K the cost is very low for moderate AI workloads. This makes on-edge AI inference accessible for personal projects, with costs scaling linearly with model size (neurons) and query volume.

## [FRICTION]

> [[2026-10-29-browser-rendering]] costs $0.09/hr for edge browsers, while [[2026-10-29-workers-ai]] charges $0.011/K neurons for AI inference. Both are edge-priced services but serve different purposes: browsers provide headless rendering Automation, while Workers AI provides model inference. A workload using both would pay $0.09/hr for browser access plus $0.011/K neuron queries, with no direct cost overlap but potential integration synergy.