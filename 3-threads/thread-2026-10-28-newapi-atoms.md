## newapi Project Introduction — 2026-10-28

Created 3 atomic notes from capture `2026-10-28-newapi-project-introduction.md` (sources/2026-10-28-newapi-project-introduction.md).

### Atoms created:

1. **2026-1028-newapi-channel-legal-compliance** — Upstream channels in New API must be legally owned or authorized accounts. Operators must comply with upstream service terms, platform rules, and regulatory requirements. [[2026-1028-newapi-channel-management-execution-order]], [[2026-1028-newapi-api-token]]

2. **2026-1028-newapi-channel-ha-features** — New API's channel system provides high-availability features: load balancing, automatic failover, weighted random selection, and multi-key management for enterprise multi-account management. [[2026-1028-newapi-channel-management-execution-order]], [[2026-1028-newapi-documentation-home]]

3. **2026-1028-newapi-override-compliance-purpose** — The parameter override feature can only be used for compatibility with legal upstream interface formats, enterprise network compatibility, and request normalization. This limitation gates how the 15 operation modes may be applied. [[2026-1028-newapi-channel-management-operation-modes]], [[2026-1028-newapi-channel-management-conditional-logic]]

### Cross-atom tensions:

- **Legal compliance vs. HA features**: Channels legally owned/authorized + HA features (load balancing, failover, multi-key management) assume lawful configuration; misconfigured channels undermine both technical reliability and legal standing.

- **Override purpose gate**: The 15 operation modes (set, delete, move, append, prepend, copy, trim operations, case conversions, replace, regex_replace) are documented in detail, but their permissible use is restricted to compliance purposes. Operators may not clearly understand when a transformation crosses from "compatibility" into "violation" territory.

### Follow-up needed:

- Verify whether New API provides any audit or validation mechanism for channel legal ownership and compliance terms.
- Explore how HA feature interaction works in practice — do load balancing and automatic failover operate simultaneously or sequentially?
- Clarify the boundary between sanctioned "compatibility" use of parameter overrides versus unauthorized transformations that violate upstream terms.