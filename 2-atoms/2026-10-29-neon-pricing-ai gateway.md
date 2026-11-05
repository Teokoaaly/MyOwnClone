---
id: 2026-10-29-neon-pricing-ai gateway
type: atom
certainty: solid
sources: [sources/2026-10-29-neon-pricing.md]
links: ["[[2026-10-29-neon-pricing-launchplan]]", "[[2026-10-29-neon-pricing-scaleplan]]"]
---

## Claim
AI Gateway pricing matches the model provider's list prices with no markup, and draws down prepaid credits; per-model rates are available per model, and prepaid credits work by deducting from the balance at the listed rate per model invocation.

## Why It Matter
Applications using AI Gateway for LLM routing should understand that costs are passed through directly from model providers, making prepaid credit management the primary cost control mechanism, and that AI Gateway is only available on Launch and Scale plans (not Free).

## [FRICTION]
> [[2026-10-29-neon-pricing-launchplan]] and [[2026-10-29-neon-pricing-scaleplan]] both list AI Gateway as a capability, but the source capture does not specify whether prepaid credits are shared across projects within a database or allocated per-project. If credits are project-level, a team with multiple projects using AI Gateway could deplete credits faster than expected; if database-level, the allocation is more generous for multi-project setups.