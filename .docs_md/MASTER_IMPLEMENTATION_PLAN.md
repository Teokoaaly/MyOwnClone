# MASTER IMPLEMENTATION PLAN — MyOwnClone

> **Purpose**: single source of truth for the institutional-console redesign + admin/backend hardening. Supersedes any inline task lists. Last updated: 2026-06-05.

## 0. Honest State Assessment

Before doing anything, the audit shows the project is **substantially more advanced** than the original task file implies. This changes the strategy from "build from scratch" to "complete, polish, and unify".

### What is ALREADY implemented and working

**Backend (Flask, `api/api/`)** — ~95% of the admin surface:

| Endpoint | Status | Notes |
|---|---|---|
| `GET /console/api/myownclone/admin/overview` | ✅ done | MRR, plan breakdown, 30d costs, generated_at |
| `GET /console/api/myownclone/admin/tenants` | ✅ done | paginated, search, status, plan, sort, direction |
| `GET /console/api/myownclone/admin/tenants/<id>` | ✅ done | tenant + 30d usage + clones list |
| `PATCH /console/api/myownclone/admin/tenants/<id>` | ✅ done | allowlist, audit, plan+status |
| `GET /console/api/myownclone/admin/feedback` | ✅ done | paginated, rating/clone/tenant/search filters |
| `POST /console/api/myownclone/admin/impersonate` | ✅ done | reason 10-1000 chars, 30 min TTL, hashed token, audit |
| `POST /console/api/myownclone/admin/impersonate/stop` | ✅ done | closes matching log, deletes token, audit |
| `GET /console/api/myownclone/admin/audit-log` | ✅ done | paginated, action/actor/target filters |
| `POST /console/api/myownclone/admin/courtesy` | ✅ done | creates tenant + account, audit |
| Auth: Bearer JWT + `X-Admin-Token` service token | ✅ done | HS256, constant-time compare |
| SQLAlchemy 2.x models with proper Mapped columns | ✅ done | Tenant, Account, CostTracking, Feedback, AnalyticsGap, AnalyticsQuestion, ImpersonationLog, ImpersonationToken, AdminAuditLog |
| 6 Alembic migrations | ✅ done | core tables, plan seeds, indexes, impersonation_tokens, admin_audit_log |
| Plan aliases DB↔API (Spanish↔English) | ✅ done | `PLAN_NAME_ALIASES_DB_TO_API` / `API_TO_DB` |
| `generated_at`, ISO-8601 dates, `{items, pagination}` contracts | ✅ done | consistent across all list endpoints |

**Frontend (Next 16 / React 19, `replica/src/`)** — ~70% of the design system:

| Asset | Status | Notes |
|---|---|---|
| Design tokens (`globals.css`) | ✅ done | light + dark tokens, accent palette, series, surface stack |
| App shell pattern | ✅ done | 220px sidebar + 72px topbar + 24px main, rounded 18-22px, soft shadow |
| `Sidebar` component | ✅ done | nav with sections, search stub, FREE TRAIL card, user block |
| `EndpointCard`, `StatsCard`, `QuickActionCard`, `OnboardingBanner`, `HeaderBreadcrumb`, `ChatOrb` | ✅ done | reusable in dashboard |
| Reusable classes: `card`, `stat-label`, `stat-value`, `table-header`, `table-row`, `badge-active/trial/warning/error`, `btn-primary/secondary`, `mono`, `section-label`, `nav-item-active/normal` | ✅ done | 30+ utility classes |
| Phosphor icons (NavIcons, ShortcutIcons, ContentTypeIcons, SiloIcons, ToneIcons, LanguageIcons, StatusIcons, UiIcons) | ✅ done | 8 icon namespaces |
| DM Sans + JetBrains Mono via `next/font/google` | ✅ done | already wired in `app/layout.tsx` |
| Admin overview, tenants list, tenant detail, feedback pages | ✅ done | 4 working admin pages with loading/error/empty/pagination |
| Next.js proxy `/api/admin/[...path]` | ✅ done | NextAuth + DB role check + X-Admin-Token forwarding + 30s timeout + 502/504 |
| `prefers-reduced-motion` honored | ✅ done | global override in globals.css |
| Drizzle schema (auth/web only, not admin) | ✅ done | users, tenants, sources, emails, conversations, clones, chunks, bookings, analytics |

### What is MISSING or NEEDS POLISH

**Backend**

1. `account_initialization_required` and `setup_required` are **dev stubs** that create dummy objects. Must add production guards.
2. Duplicate tree at `api/` (parallel to `api/api/`) is dead code; needs confirmation and removal.
3. No automated tests (only `seed_demo_data` CLI).
4. `_verify_token` is imported from `api.controllers.console.auth` but lives in the same module — circular import risk.

**Frontend**

5. No **mobile navigation** — the Sidebar is `hidden md:flex`. Need a drawer or bottom nav for <768px.
6. No **dark mode toggle** — dark tokens exist but no UI to activate `.dark`.
7. No **charts** — admin overview is stat cards only. Reference images show line/area charts.
8. **Login page is old style** — uses `text-purple-600 bg-gray-50`, ignores design tokens.
9. **Admin layout is duplicated** — its own sidebar instead of reusing the `Sidebar` component.
10. **Landing page (`page.tsx`) has hardcoded fake content** — notification stack with "Terry approved design", brand names, "200,000+ users".
11. **No audit log UI page** — backend supports it.
12. **No impersonation UI** — backend supports it.
13. **No tenant-create/courtesy UI** — backend supports it.
14. **No Drizzle source of truth conflict** — confirmed Flask is canonical for admin; Drizzle is for auth/web. No fix needed; just document.
15. **Hardcoded mock data in dashboard resumen** — "Recent queries" lists fake strings; "Stats" all default to 0; "Getting started" steps are hardcoded.
16. **The "FREE TRAIL" card in Sidebar** is hardcoded "7 days left" / "Upgrade" with no wiring.
17. **No tests** — vitest configured but no test files.

**Documentation**

18. No `MASTER_IMPLEMENTATION_PLAN.md`, no `DESIGN_SYSTEM.md`, no `BACKEND_ADMIN_CONTRACTS.md`, no `BACKEND_SECURITY_AUDIT.md`, no `FRONTEND_UI_AUDIT.md`, no `ROUTE_AND_COMPONENT_MAP.md`, no `QA_CHECKLIST.md`, no `IMPLEMENTATION_LOG.md` (yet — they are being created as part of this phase).

## 1. Strategy

The original mega-plan's "build from scratch" framing is wrong. The work splits cleanly into:

- **A. Documentation** (zero-risk, unblocks future work)
- **B. Backend hardening** (production guards, remove dead code, document)
- **C. Admin UI completion** (reuse existing Sidebar, add missing pages: audit, impersonation, courtesy)
- **D. Design system polish** (mobile nav, dark toggle, login redesign, landing page cleanup, charts)
- **E. Dashboard polish** (remove hardcoded data, fix inconsistencies)
- **F. QA, tests, build** (vitest, pytest, build verification, responsive sweep)

We execute A first, then B/C in parallel, then D/E, then F. Each phase is independently shippable.

## 2. Stack (confirmed)

| Layer | Tech |
|---|---|
| Frontend | Next.js 16.2.6, React 19.2.4, TypeScript 5, Tailwind 4 (PostCSS plugin), Drizzle 0.38, NextAuth 5.0 beta, next-intl 3.24, framer-motion 12, phosphor-icons |
| Auth (web) | NextAuth + Drizzle adapter |
| Proxy | `/replica/src/app/api/admin/[...path]/route.ts` |
| Backend | Flask 3, Flask-SQLAlchemy 3.1, Flask-Migrate 4, Flask-CORS 4, SQLAlchemy 2.0, psycopg2-binary, flask-restx 1.3, Pydantic 2, gunicorn |
| Auth (API) | JWT HS256 via `Authorization: Bearer`, `X-Admin-Token` for service |
| DB | PostgreSQL (SQLAlchemy) + Drizzle (auth/web only) |
| Tests | vitest (frontend), pytest (backend, configured but no tests yet) |

## 3. Phases

### PHASE A — Documentation (CURRENT)

Goal: ship the 8 master docs so future work has a contract.

- [x] `MASTER_IMPLEMENTATION_PLAN.md` (this file)
- [x] `DESIGN_SYSTEM.md`
- [x] `BACKEND_ADMIN_CONTRACTS.md`
- [x] `BACKEND_SECURITY_AUDIT.md`
- [x] `FRONTEND_UI_AUDIT.md`
- [x] `ROUTE_AND_COMPONENT_MAP.md`
- [x] `QA_CHECKLIST.md`
- [x] `IMPLEMENTATION_LOG.md` (created empty, appended after each phase)

Exit criteria: every doc has sections, every section has content, no `TODO` left.

### PHASE B — Backend hardening

Goal: ship a backend that is safe for production, with no dead code.

- [ ] **B1** Confirm `api/` (root) is dead; document. Do NOT delete until manual review.
- [ ] **B2** Replace dev stub `account_initialization_required` with a real check that:
  - 404s if no session
  - returns proper error if `g.account_id` is missing
  - keeps dev-mode compat behind `FLASK_ENV=development` or similar
- [ ] **B3** Same for `setup_required`.
- [ ] **B4** Fix `_verify_token` import path (currently imported from `api.controllers.console.auth` but defined there).
- [ ] **B5** Add a `conftest.py` and one smoke test per admin endpoint (`tests/test_admin_*.py`).
- [ ] **B6** Document env vars in `.env.example`: `PLATFORM_ADMIN_TOKEN`, `IMPERSONATION_TOKEN_PEPPER`, `JWT_SECRET_KEY`.
- [ ] **B7** Run `python -m pytest`; capture result in `IMPLEMENTATION_LOG.md`.

Exit criteria: backend starts without dev stubs mocking accounts, all tests pass or have explicit "skipped/debt" comment.

### PHASE C — Admin UI completion

Goal: ship a complete admin (Overview + Tenants + Tenant detail + Feedback + Audit log + Impersonation + Courtesy).

- [ ] **C1** Reuse `Sidebar` component in `app/admin/layout.tsx`; remove duplicated sidebar.
- [ ] **C2** Add `/admin/audit/page.tsx` (table with action/actor/target/created_at, pagination, filters).
- [ ] **C3** Add impersonation button on `/admin/tenants/[id]` → modal with reason textarea → POST → show one-time token with copy button.
- [ ] **C4** Add courtesy/signup button on `/admin/tenants` → modal with email/name/plan/duration.
- [ ] **C5** Add a "Plan performance" chart to admin overview (MRR by month, 30d costs) using a lightweight library or SVG.
- [ ] **C6** Add a "Plan distribution" bar chart (using the plan_breakdown data already returned).
- [ ] **C7** Confirm 401/403 handling in all admin pages; show a clean error state, not a blank page.

Exit criteria: every backend admin endpoint has a UI page or button; clicking through every flow works end-to-end.

### PHASE D — Design system polish

Goal: ship a responsive, theme-aware, consistent design language.

- [ ] **D1** Add a `MobileNav` drawer component (slides in from left, same nav items as Sidebar).
- [ ] **D2** Add a dark mode toggle in the Sidebar user block (persists to `localStorage`, applies `.dark` to `<html>`).
- [ ] **D3** Redesign `/login` using the new tokens. Remove `text-purple-600 bg-gray-50`.
- [ ] **D4** Clean up the landing page `app/page.tsx`: remove fake "Trusted by Google/Airbnb/Notion/PayPal/Upwork/Shopify/Stripe/Zoom" row, remove fake notification stack, replace with real product copy.
- [ ] **D5** Replace the hardcoded `7 days left / Upgrade` card with one driven by a `/api/clone/billing` call (or remove if not ready).
- [ ] **D6** Add an `EmptyState` component; replace the ad-hoc empty states in tenants/feedback pages.
- [ ] **D7** Add a `SearchCommandBar` for the admin topbar (⌘K → opens a search dialog).
- [ ] **D8** Wire up the `EndpointCard` and `OnboardingBanner` to real API data (or remove if deprecated).
- [ ] **D9** Make all tables responsive: on <768px, render as list rows/cards with primary action.

Exit criteria: at 375px, 768px, 1024px, 1440px the entire app is usable. Dark mode toggles without flash. Login looks like the rest.

### PHASE E — Dashboard polish

Goal: remove hardcoded mock data and make the dashboard reflect real state.

- [ ] **E1** Replace hardcoded "Recent queries" with real `/api/clone/inbox/list` recent items.
- [ ] **E2** Replace hardcoded "Getting started" with real onboarding-step tracking.
- [ ] **E3** Replace fake "Past 30 days" usage bars with real `/api/clone/analytics/overview` data.
- [ ] **E4** Wire `StatsCard` to real `/api/clone/analytics/overview` (active_sessions, automation_rate, clones count).
- [ ] **E5** Polish inbox, biblioteca, cerebro, analiticas, facturacion, configuracion pages — confirm all use design tokens, no hardcoded colors.
- [ ] **E6** Add loading skeletons (`LoadingState` component) instead of bouncing dots.

Exit criteria: the dashboard tells a true story. No hardcoded "4.6 Google / 4.9 Trustpilot" or "200,000+ users".

### PHASE F — QA, tests, build

Goal: ship proof that the app is correct, accessible, responsive, and buildable.

- [ ] **F1** `cd api && python -m pytest` — all tests pass.
- [ ] **F2** `cd replica && npm run lint` — 0 errors.
- [ ] **F3** `cd replica && npm run typecheck` — 0 errors.
- [ ] **F4** `cd replica && npm run test` — all tests pass.
- [ ] **F5** `cd replica && npm run build` — succeeds.
- [ ] **F6** Manual responsive sweep at 375 / 768 / 1024 / 1440.
- [ ] **F7** Axe/Lighthouse accessibility scan; fix any critical issues.
- [ ] **F8** Final `IMPLEMENTATION_LOG.md` summary with file counts, command outputs.

## 4. Screen checklist (per the spec)

| Screen | Current state | Target state | Phase | Status |
|---|---|---|---|---|
| `/` (landing) | Hardcoded marketing fluff | Real product copy, design tokens | D4 | Not started |
| `/login` | Old purple/gray | Institutional Console, dark-mode-aware | D3 | Not started |
| `/registro` | Unknown | Institutional Console | D3 | Pending review |
| `/onboarding` | Unknown | Institutional Console, mobile nav | C/D | Pending review |
| `/verificar` | Unknown | Institutional Console | D | Pending review |
| `/resumen` | Mostly there, hardcoded "Recent queries" | Real data, no hardcoded stats | E1-E4 | Partial |
| `/inbox` | Unknown (not audited) | Real data, list rows on mobile | E5 | Pending review |
| `/biblioteca` | Unknown (not audited) | Source cards + coverage chart | E5 | Pending review |
| `/cerebro` | Unknown (not audited) | Memory summary + actions | E5 | Pending review |
| `/analiticas` | Unknown (not audited) | Charts with series colors | E5 | Pending review |
| `/facturacion` | Unknown (not audited) | Plan + usage + invoices | E5 | Pending review |
| `/configuracion` | Unknown (not audited) | Form panels + dark toggle | D2 | Pending review |
| `/admin/resumen` | Stat cards only | + charts, + recent activity | C5/C6 | Partial |
| `/admin/tenants` | Done | Reuse Sidebar, add Courtesy | C1/C4 | Partial |
| `/admin/tenants/[id]` | Done | + Impersonate button | C3 | Partial |
| `/admin/feedback` | Done | + filters polish | C | Partial |
| `/admin/audit` | **Missing** | New page | C2 | Not started |
| `/[slug]` (public clone) | Unknown | Institutional Console shell | E5 | Pending review |
| `widget.js` | Unknown | Out of scope (embed script) | — | Pending review |

## 5. Out of scope

- Replacing the database engine (PostgreSQL stays).
- Replacing Drizzle with a different ORM.
- Replacing Flask with a different backend framework.
- Adding new product features (focus is visual + admin).
- Marketing-site redesign beyond the landing page (`/`).
- The `widget.js` embed script.
- Anything requiring paid third-party services (Recharts is MIT; we'll use it for charts).

## 6. Risks

- **R1**: Removing the dead `api/` tree may break local dev if any script imports from it. Mitigation: grep first, only delete if 0 hits outside `api/`.
- **R2**: `account_initialization_required` is currently permissive in dev. Making it strict will block dev unless we keep a `FLASK_ENV=development` bypass.
- **R3**: Adding dark mode toggle can cause a flash-of-wrong-theme on hydration. Mitigation: inject an inline script in `<head>` that reads `localStorage` and sets `.dark` before paint.
- **R4**: Recharts adds ~100KB to bundle. Mitigation: lazy-load charts on admin pages only.
- **R5**: Vitest is configured but no tests exist. We'll add minimum smoke tests in F4.

## 7. Decision: do not delegate everything

Because the existing system is well-structured, blindly delegating to subagents risks them creating parallel components or duplicating work. The right approach:

- Use the audit findings above as the brief.
- Subagents (when used) get told which existing components to reuse.
- Every PR/commit must show the deltas in this file.

## 8. Conditions for "done"

Same as the spec:

- [ ] Backend admin endpoints all work in dev (curl smoke test passes).
- [ ] All admin pages render the new style.
- [ ] Dashboard, inbox, biblioteca, etc. all render the new style.
- [ ] Login, register, onboarding, public clone render the new style.
- [ ] Responsive at 375 / 768 / 1024 / 1440.
- [ ] Dark mode toggle works without flash.
- [ ] `npm run lint`, `npm run typecheck`, `npm run test`, `npm run build` all pass.
- [ ] `python -m pytest` passes.
- [ ] `IMPLEMENTATION_LOG.md` is up to date.
- [ ] No screen is marked "implemented" without a screenshot-equivalent in the QA checklist.
