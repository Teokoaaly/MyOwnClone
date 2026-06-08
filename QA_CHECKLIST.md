# QA CHECKLIST — MyOwnClone

> Per-screen and per-system checks. Mark `[x]` only after manual verification at the relevant breakpoint.

## 1. Backend

### Smoke tests (must pass after every change)

- [ ] `cd api && python -m pytest` → all green
- [ ] Lint: `cd api && ruff check .` (if ruff is added)
- [ ] App starts: `FLASK_APP=api.api.app_factory flask routes | grep admin` shows the 9 admin endpoints

### Per endpoint

| Endpoint | 401 | 403 | 200 empty | 200 populated | Error format |
|---|---|---|---|---|---|
| GET /admin/overview | [ ] | [ ] | [ ] | [ ] | [ ] |
| GET /admin/tenants | [ ] | [ ] | [ ] | [ ] | [ ] |
| GET /admin/tenants/<id> | [ ] | [ ] | [ ] | [ ] | [ ] |
| PATCH /admin/tenants/<id> | [ ] | [ ] | [ ] | [ ] | [ ] |
| GET /admin/feedback | [ ] | [ ] | [ ] | [ ] | [ ] |
| POST /admin/impersonate | [ ] | [ ] | [ ] | [ ] | [ ] |
| POST /admin/impersonate/stop | [ ] | [ ] | [ ] | [ ] | [ ] |
| GET /admin/audit-log | [ ] | [ ] | [ ] | [ ] | [ ] |
| POST /admin/courtesy | [ ] | [ ] | [ ] | [ ] | [ ] |

### Security

- [ ] No secrets in logs (impersonation tokens logged only as 8-char prefix)
- [ ] `PLATFORM_ADMIN_TOKEN` is required in production
- [ ] `IMPERSONATION_TOKEN_PEPPER` rejects the default in production
- [ ] CORS allowlist is set (not wildcard)
- [ ] `_validate_required_env` refuses weak `DB_PASSWORD`
- [ ] `account_initialization_required` is strict in production
- [ ] `setup_required` is strict in production
- [ ] Impersonation token in DB is SHA-256 hashed
- [ ] All impersonation events appear in audit log
- [ ] All tenant PATCH events appear in audit log
- [ ] All courtesy signups appear in audit log

## 2. Frontend

### Build & types

- [ ] `cd replica && npm run lint` → 0 errors
- [ ] `cd replica && npm run typecheck` → 0 errors
- [ ] `cd replica && npm run test` → all green
- [ ] `cd replica && npm run build` → succeeds
- [ ] No console errors on any page
- [ ] No 404s on any static asset (font, image, icon)

### Design system consistency

- [ ] No `bg-black`/`bg-white` outside the `.btn-primary` rule
- [ ] No `text-purple-600` / `bg-gray-50` outside the new login (after D3)
- [ ] All cards use the `card` class or `rounded-2xl border var(--border-soft)`
- [ ] All badges use `.badge-*` classes
- [ ] All numeric stats use `mono` or `stat-value`
- [ ] No hardcoded gradients in pages (only the shell layer)
- [ ] All hover transitions are 160-220ms
- [ ] `prefers-reduced-motion` honored

### Per-screen checklist

#### Public

- [ ] `/` (landing) — real copy, no fake brand row, no fake notification stack
- [ ] `/login` — uses tokens, no `text-purple-600`, dark-mode aware
- [ ] `/registro` — uses tokens
- [ ] `/es/verificar` — uses tokens
- [ ] `/es/onboarding` — uses tokens
- [ ] `/[slug]` — public clone page uses Institutional Console shell, not a landing

#### Dashboard

- [ ] `/resumen` — stats from real API, no hardcoded "0", "Recent queries" from inbox, "Getting started" tracks real onboarding
- [ ] `/biblioteca` — uses tokens, no hardcoded colors
- [ ] `/cerebro` — uses tokens
- [ ] `/inbox` — uses tokens, list rows on mobile
- [ ] `/productos` — uses tokens
- [ ] `/reuniones` — uses tokens
- [ ] `/analiticas` — uses tokens, charts use `--series-*` palette
- [ ] `/facturacion` — uses tokens, plan + usage + invoices
- [ ] `/configuracion` — uses tokens, dark toggle works

#### Admin

- [ ] `/admin/resumen` — uses real Sidebar, has at least one chart, plan breakdown bar chart
- [ ] `/admin/tenants` — uses real Sidebar, paginated, courtesy button, list rows on mobile
- [ ] `/admin/tenants/[id]` — usage grid, impersonate button (reason modal), plan patch UI
- [ ] `/admin/feedback` — uses real Sidebar, list rows on mobile
- [ ] `/admin/audit` — new page, paginated, action/actor/target filters
- [ ] `/admin/impersonation` — flows from tenant detail
- [ ] `/admin/courtesy` — flows from tenants list

### Responsive sweep

For each screen, verify at 375, 768, 1024, 1440:

- [ ] No horizontal scroll on body
- [ ] No text overflow / cutoff
- [ ] All buttons reachable with thumb on mobile
- [ ] Sidebar becomes drawer (D1) — not stuck off-screen
- [ ] Tables become list rows on mobile (D9)
- [ ] Charts fit in viewport, tooltips scroll horizontally
- [ ] Tabs scroll horizontally, no overflow
- [ ] Topbar is compact and shows hamburger

### Dark mode

- [ ] Toggle works in Sidebar user block
- [ ] Persists across reloads (localStorage)
- [ ] No flash of light theme on initial paint
- [ ] All text is readable (AA contrast minimum)
- [ ] Borders still visible but not heavy
- [ ] Charts re-render with the same palette

### Accessibility

- [ ] All icon-only buttons have `aria-label`
- [ ] All form fields have a `<label>`
- [ ] Tab order is logical (top-to-bottom, left-to-right)
- [ ] Focus visible on every interactive element
- [ ] Modals trap focus and close on Escape
- [ ] No "color-only" signaling (badges have text too)
- [ ] `prefers-reduced-motion` respected
- [ ] Lighthouse a11y score ≥ 95

### Loading / empty / error

For every list page (tenants, feedback, audit, inbox, biblioteca):

- [ ] Loading skeleton (not just a spinner)
- [ ] Empty state with icon, title, microcopy, and a CTA
- [ ] Error state with title, reason, and a "Try again" button
- [ ] 401 redirects to /login (admin) or shows a clean error (dashboard)

## 3. Cross-cutting

- [ ] No mocks where real API exists
- [ ] All forms have a save/submit button that wires to the right endpoint
- [ ] All destructive actions have a confirm step
- [ ] No emoji in the UI
- [ ] No "Click here" or "Read more" — use specific actions
- [ ] All dates are localized (`es-ES` via `toLocaleString` or `Intl.DateTimeFormat`)
- [ ] All money is `Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" })`

## 4. Definition of done (final gate)

A screen is "Implemented" only if:
1. Its tokens match the design system (no hardcoded colors)
2. Loading + empty + error states are visible in dev
3. It is responsive at 375 / 768 / 1024 / 1440
4. It works in dark mode
5. `npm run lint`, `npm run typecheck`, `npm run test`, `npm run build` all pass
6. The QA checklist row for that screen is fully checked
7. The `IMPLEMENTATION_LOG.md` entry has a date and a one-line summary
