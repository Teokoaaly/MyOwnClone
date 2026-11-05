---
id: 2026-1101-openai-batch-processing-pricing
type: atom
certainty: solid
sources: [sources/2026-10-28-openai-api-pricing.md]
links: ["[[2026-1101-openai-gpt6-family-pricing]]", "[[2026-1101-openai-prompt-caching-pricing]]", "[[2026-1101-openai-regional-residency-pricing]]"]
---
## Claim
OpenAI's Batch processing tier offers a 50% discount on both input and output compared to the Standard tier, with the same context window and model capabilities. Batch jobs are processed with a 24-hour minimum latency requirement. The Batch tier applies to all gpt-6 family variants and gpt-6.1 models.

## Why It Matters
For workloads that can tolerate 24-hour latency — such as nightly report generation, bulk document processing, or offline analytics — the Batch tier reduces effective cost by half compared to Standard pricing. This makes high-capability models accessible for high-volume, low-urgency use cases. The 50% discount is consistent across all gpt-6 variants, meaning the choice of model variant within Batch tier affects absolute cost but not the discount ratio.

## [FRICTION]
> [[2026-1101-openai-prompt-caching-pricing]] notes that prompt caching carries separate pricing even within Batch tier, which means the 50% Batch discount applies to the base rate, and cached input rates follow the Batch-tier multiplier — but the interaction between Batch discount and cached discount is not explicitly documented as a combined percentage, creating ambiguity about the total effective cost when both Batch and caching are enabled. Users must refer to the individual tier and caching tables and compute the combination manually.