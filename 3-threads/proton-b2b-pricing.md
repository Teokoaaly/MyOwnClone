# Proton B2B Pricing Plans
*Last updated: 2026-10-31*

## Overview
Proton has expanded its B2B offering with three new plan tiers — VPN Essentials, VPN Professional, and Workspace Standard — each targeting different segments of the business market while maintaining a minimum 2-user entry barrier. The plans span from pure VPN connectivity (Essentials/Professional) to a full productivity suite (Workspace Standard), reflecting Proton's strategy to capture the identity-and-collaboration market beyond just VPN connectivity. A key pattern across all plans is the per-user pricing model, where the marginal cost of capacity is a price per seat rather than per gigabyte, making the number of users the dominant cost variable.

## Key Ideas

### VPN Essentials ($6.99/user/mo, min 2 users)
VPN Essentials is the entry point into Proton's B2B model. At $6.99 per user per month with a minimum of 2 users, the initial cost for a small team is $13.98/month. The plan includes connectivity across 140+ countries with NetShield ad/malware blocking, centralized user management, 2FA, kill switch, always-on VPN, and split tunneling. It also includes the same 14-day/30-day risk-free guarantees as higher-tier plans, suggesting Proton's intent to eliminate adoption risk for new business customers regardless of price point. The plan establishes the **price base per user** for the B2B VPN line, serving as the reference point for calculating marginal costs when adding features in upper tiers.

[[2026-1031-proton-business-vpn-essentials-6-99-minimo-2-usuarios]]

### VPN Professional ($9.99/user/mo, min 2 users)
VPN Professional sits as the first tier with organizational-grade features. The $3/user/mo jump from Essentials adds Single Sign-On (SSO) and SCIM for provisioning, dedicated IPs in 20+ countries, network segmentation, advanced access policies, network monitoring, and Proton Sentinel account protection. The minimum 2-user requirement keeps the entry barrier low for teams, while the addition of SSO/SCIM shifts the model from "user isolated" to "corporate identity management." The key marginal addition here is not connectivity but **identity governance and compliance capabilities**, representing a fundamental change in the cost structure per user.

[[2026-1031-proton-business-vpn-professional-9-99-minimo-2-usuarios]]

### Workspace Standard ($12.99/user/mo, features per user)
Workspace Standard is the top-tier B2B plan at $12.99/user/month, combining VPN connectivity with Pass, Mail, Calendar, Drive, Docs, Sheets, and Meet. Crucially, it includes **1 TB of storage per user** — the variable cost shifts from gigabytes to seats. For a multi-tenant environment, this validates the pattern that capacity is a function of the number of asements with an admin panel distributing resources. By including Pass, Mail, and Calendar under a single seat, Workspace Standard resolves the "one identity per tenant without per-tenant domains" problem that VPN Essentials/Professional only address at the network level.

[[2026-1031-proton-business-workspace-standard-12-99]]

### Cross-Plan Frictions and Observations

1. **Capacity vs. Cost Perspective** — The Workspace Standard atom notes that the marginal cost of capacity is "a price per seat, not a price per gigabyte," while an earlier atom observes that "storage grows with the number of seats: adding users buys capacity, and reasignment is done from the admin panel." Both describe the same mechanism from different angles (capacity mechanics vs. cost implications), but the differing emphasis — one on reasignment logistics, the other on cost dominance — could confuse readers unfamiliar with the thread `costes-por-categoria-tenant`. No technical contradiction exists, but the differential focus merits clarification.

2. **Kill Switch Labeling Discrepancy** — VPN Essentials asserts the kill switch is "Included" at $6.99, while an earlier atom on the consumer line labels it a "Premium feature" unavailable on the free plan. These cannot both be completely correct. The essential distinction is whether the kill switch is a standard B2B feature at the entry tier or a premium add-on, which has direct implications for compliance and security purchasing decisions.

3. **SSO/SCIM Provider Compatibility** — VPN Professional claims to include both SSO and SCIM, while an earlier atom states that SSO supports "any SAML 2.0 provider" (Okta, Google Workspace, Microsoft Entra ID) but SCIM is limited to only Okta and Microsoft Entra ID. This is a genuine factual discrepancy: the professional plan's documentation either overstates SCIM compatibility or the earlier atom imposes artificial limitations. This requires human judgment to resolve.

## Open Questions
- [ ] **Kill switch status in VPN Essentials**: Is it truly included at the $6.99 price point, or is it a premium feature as the consumer-line atom suggests? This affects the security baseline for new B2B customers.
- [ ] **SCIM compatibility in VPN Professional**: Does the plan support SCIM beyond Okta and Microsoft Entra ID? The discrepancy with the "any SAML 2.0 provider" SSO claim needs resolution.
- [ ] **Workspace Standard storage model**: In a multi-tenant deployment, how does the 1 TB/user storage interact with tenant isolation and per-tenant quotas? The thread `costes-por-categoria-tenant` may have relevant prior art.
- [ ] **Pricing consistency across regions**: The atoms reference USD pricing, but the vault's cost-tracking model uses Euros as the primary currency. How do exchange rate fluctuations and regional pricing tiers affect the per-seat cost model?