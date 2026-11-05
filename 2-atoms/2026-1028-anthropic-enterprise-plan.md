---
id: 2026-1028-anthropic-enterprise-plan
type: atom
certainty: solid
sources: [raw/2026-10-28-anthropic-plans-pricing.md]
links: ["[[2026-1028-anthropic-team-plan]]"]
---

## Claim

The Anthropic Enterprise plan is built for large businesses operating at scale, priced at **US$20/seat/month billed annually** (20-seat minimum) plus usage at API rates. It includes all Team plan features plus admin controls for user and org spend limits, role-based access with fine-grained permissioning, SCIM, audit logs, compliance API, custom data retention controls, network-level access control, IP allowlisting, HIPAA-ready offering (available), and Claude Security (beta). Admins can set user and organizational level spend controls, and the plan offers up to $500 per month in pooled API credits. Enterprise is billed annually only, with self-serve and sales-assisted acquisition paths.

## Why It Matters

Enterprise addresses the security, compliance, and administrative needs of large organizations that require fine-grained control, auditing, and integration capabilities (SCIM, audit logs, IP allowlisting). The $20/seat annual base price with usage-based API costs makes it predictable for seat count but variable for usage patterns. The HIPAA-ready offering and Claude Security beta expand its addressable market into regulated industries.

## [FRICTION]

> The 20-seat minimum creates a high barrier for midsize organizations: a 10-user team must pay for 20 seats at $400/month minimum, even if they only need 10. This forces premature scaling to a plan that may be overprovisioned, or requires workarounds like shared accounts that undermine the admin controls the plan provides.

> Usage cost "scales with model and task" without a public pricing table or calculator. A team planning API budget cannot accurately forecast costs without running test queries or contacting sales, creating uncertainty in budgeting and making the $20/seat base price insufficient for total cost estimation.

> Role-based access with "fine grained permissioning" is listed as a feature but the comparison table shows it as "No" for Team and "Yes" for Enterprise — yet Team already includes "Admin controls for remote and local connectors" and "Central billing and administration." The functional distinction between Team's admin controls and Enterprise's RBAC is not delineated, leaving admins unsure what they gain by upgrading.

> HIPAA-ready offering is available but not elaborated: there is no public description of what HIPAA controls are included, what certifications exist, or how a customer enables the offering. "Available" without specifications creates a checkbox claim rather than a actionable capability.