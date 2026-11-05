## render-pricing-2026-10-29 — Atoms created from Render pricing page capture (2026-10-29)

### Atoms created:
1. **2026-1029-render-hobby-plan** — Hobby plan at $0/mo provides free compute for personal projects with significant limitations: 512 MB RAM, 1 CPU, 5 GB bandwidth, and no custom domains or firewall, suitable only for prototypes and exploration. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

2. **2026-1029-render-compute-per-second** — Render charges compute on a per-second basis, prorating billing to the second for all active services including Cron Jobs and Workflows, meaning users only pay for compute when services are actually running. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

3. **2026-1029-render-postgres-pricing** — Render's managed PostgreSQL service scales from $0 (Free: 256 MB RAM, 100 connections) to $11,000/mo (128 CPU, 1024 GB RAM, 500 connections), with logical backup available only on paid plans and expandable storage at $0.30/GB per month. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

4. **2026-1029-render-keyvalue-pricing** — Render's Key Value (Redis-compatible) service ranges from $0 (Free: 25 MB RAM, 50 connections) to $9,000/mo (50 GB RAM, 768 GB storage, 50,000 connections), with disk-backed persistence available only on paid plans at $0.25 per GB per month. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

5. **2026-1029-render-bandwidth-overage** — Render includes bandwidth with their workspace plans (5 GB/mo for Hobby, 25 GB/mo for Pro, 1 TB/mo for Scale) and charges $0.15 per GB overage thereafter, with Enterprise having custom bandwidth terms. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

6. **2026-1029-render-sandboxes-pricing** — Render Sandboxes (beta) provide isolated microVMs at $0.12 per active CPU hour + memory hourly rates, with a 24-hour maximum session length, 40 GB disk included per sandbox, and snapshot storage available at $0.08/GB per month. Certainty: tentative due to unpublished memory hourly rate. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

7. **2026-1029-render-enterprise-compliance** — Render's Enterprise plan offers HIPAA-compliant workspaces, SAML SSO, SCIM provisioning, and dedicated technical account team at custom pricing, with a 20% compute premium for enabled workspaces and support response SLAs as an add-on. Links to [[2026-1022-admin-bandeja-global-y-spam]] and [[2026-1022-auth-flask-nextauth-desconectados]].

### Cross-atom tensions:
- **Per-second vs. fixed monthly billing**: Atoms 2 (compute per-second) and 5 (bandwidth overage at $0.15/GB) represent different metering models — per-second metering benefits variable workloads while flat-rate bandwidth overage favors predictable high-traffic workloads. Users with consistently running services may find fixed monthly plans more cost-effective than per-second metering combined with bandwidth overage.

- **Free tier limitations across services**: Atoms 1 (Hobby 512 MB RAM), 3 (Postgres Free: 256 MB RAM, 100 connections), and 4 (Key Value Free: 25 MB RAM, 50 connections) all note that Free tiers have severe resource constraints that push users to paid plans quickly. The Hobby plan's 512 MB RAM limit is more restrictive than myownclone's free tier, creating tension for users whose prototypes outgrow Hobby's constraints before justifying Pro's $25/mo cost.

- **Persistence cost differential**: Atoms 4 (Key Value $0.25/GB for disk-backed persistence) and 3 (Postgres $0.30/GB expandable storage) show Render charges a premium for persisted storage compared to specialized providers, creating friction when users compare against dedicated Redis/Postgres hosting at lower per-GB rates, though Render's integrated billing and per-second compute metering may offset this for full-stack Render users.

- **20% compute premium for compliance**: Atom 7 (Enterprise 20% compute premium) versus general per-second billing creates tension for regulated workloads that must pay the premium even for minimal usage, since the 20% applies to the workspace plan plus compute, meaning even a small Hobby workspace with HIPAA enabled pays the premium on top of per-second compute charges.

- **Session duration mismatch**: Atom 6 (Sandboxes 24-hour max) versus Atoms 2 and 3 (per-second billing, always-warm instances) creates friction for development workflows that need longer-lived isolated environments than sandboxes allow, pushing users toward dedicated compute plans or external solutions for extended testing.

### Follow-up needed:
- Monitor whether the $0.15/GB bandwidth overage rate disproportionately affects high-traffic applications compared to flat-rate bandwidth pricing from competitors like Vercel or Netlify.
- Test whether per-second compute billing actually saves costs for consistently running 24/7 services versus fixed monthly compute plans across different CPU/RAM configurations.
- Track user adoption of Sandboxes versus dedicated compute plans for development workflows, particularly whether the 24-hour session limit is a constraint.
- Evaluate whether the 20% Enterprise compute premium is fairly applied across workspace sizes or whether it creates a disincentive for teams to enable HIPAA/SOC 2 compliance on smaller workloads.
- Investigate the unpublished memory hourly rate for Sandboxes and whether it can be derived from the published CPU rate + observed memory usage patterns.