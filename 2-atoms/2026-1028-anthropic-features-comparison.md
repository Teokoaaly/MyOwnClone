---
id: 2026-1028-anthropic-features-comparison
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-plans-pricing.md]
links: ["[[2026-1028-anthropic-free-pro-max]]", "[[2026-1028-anthropic-team-plan]]", "[[2026-1028-anthropic-enterprise-plan]]"]
---

## Claim

The feature comparison table across Free, Pro, Max 5x, and Max 20x plans reveals a consistent pattern: features available in Free are marked "Yes" while Pro, Max 5x, and Max 20x all mark "Yes" for the same features, suggesting feature parity that is more apparent than real. Key differentiators include Claude Code (Free: No, Pro/Max: Yes), Claude Science (Free: No, Pro/Max: Yes), Chrome and Microsoft 365 integration (Free: No, Pro/Max: Yes), Dashboards (Free: No, Pro/Max: Yes), and Projects (Free: Up to 5, Pro/Max: Yes). The Team and Enterprise plans add SSO, domain verification, org creation restrictions, central billing, SCIM, audit logs, and enterprise search — features entirely absent from the individual plan tiers.

## Why It Matters

The comparison table is the primary tool users have to evaluate plan differences. However, many features are marked "Yes" with "More information" links across all non-Free plans, meaning the actual capability boundaries are obscured behind additional clicks. This design pattern favors conversion over transparency: users must navigate away from the pricing page to understand what they're buying. For Team and Enterprise, the addition of security and admin features creates a clearer value proposition, but the Free-to-Pro transition relies on feature gaps that are not quantitatively described.

## [FRICTION]

> The comparison table marks "More information" for features like "Create and edit files with code execution," "Research," "Skills," and "Connectors" across all plans — indicating that actual capabilities are limited, gated, or differ in ways not reflected in the yes/no matrix. A user comparing Pro vs Max cannot determine from the table alone whether the difference is quota, performance, or capability.

> Feature availability for Teams and Enterprise is presented in a separate comparison section (starting at line 275) while individual plans use a different table (starting at line 77) — two different visualizations of the same data that may use different granularity or filtering, creating inconsistency when users reference both sections in discussion.

> "Projects" shows "Up to 5" for Free but "Yes" for Pro/Max/Team/Enterprise — the boundary of "Up to 5" (per-project limits, storage, duration) is not defined, and a user with 5 projects hitting the limit has no clear upgrade path or escalation mechanism visible on the pricing page.

> "SkillsMore information" and "ConnectorsMore information" appear as yes/no entries across every plan tier with the same link target, suggesting the "More information" target does not scale across different plan contexts — a single information target cannot adequately explain skills and connectors for Free, Pro, Max, and Team simultaneously.