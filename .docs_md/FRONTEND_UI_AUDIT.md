# FRONTEND UI AUDIT — MyOwnClone

> Per-page status against the Institutional Console target. "Pending review" means we have not yet read the file in this audit cycle.

## 1. Routes (app router)

### Public

| Path | File | Status | Notes |
|---|---|---|---|
| `/` | `app/page.tsx` | NEEDS REWORK | Landing with hardcoded "Trusted by Google/Airbnb/...", "4.6 Google / 4.9 Trustpilot", rotated fake notification stack, brand names. Replace with real product copy. |
| `/login` | `app/login/page.tsx` | NEEDS REWORK | Uses `text-purple-600 bg-gray-50`. Ignores design tokens. The form component (`login-form.tsx`) is not yet read. |
| `/registro` | `app/(dashboard)/registro/page.tsx` | Pending review | — |
| `/es/verificar` | `app/es/verificar/page.tsx` | Pending review | — |
| `/es/onboarding` | `app/es/onboarding/page.tsx` | Pending review | — |
| `/[slug]` | `app/(public)/[slug]/page.tsx` | Pending review | Public clone page — should use the same shell, not be a landing. |

### Dashboard (auth required)

| Path | File | Status | Notes |
|---|---|---|---|
| `/resumen` | `app/(dashboard)/resumen/page.tsx` | PARTIAL | Stats are hardcoded to 0. "Recent queries" are fake strings. "Getting started" is hardcoded. EndpointCard data is fake. OnboardingBanner hardcoded. |
| `/biblioteca` | `app/(dashboard)/biblioteca/page.tsx` | Pending review | — |
| `/biblioteca/nuevo` | `app/(dashboard)/biblioteca/nuevo/page.tsx` | Pending review | — |
| `/cerebro` | `app/(dashboard)/cerebro/page.tsx` | Pending review | — |
| `/inbox` | `app/(dashboard)/inbox/page.tsx` | Pending review | — |
| `/productos` | `app/(dashboard)/productos/page.tsx` | Pending review | — |
| `/reuniones` | `app/(dashboard)/reuniones/page.tsx` | Pending review | — |
| `/analiticas` | `app/(dashboard)/analiticas/page.tsx` | Pending review | — |
| `/facturacion` | `app/(dashboard)/facturacion/page.tsx` | Pending review | — |
| `/configuracion` | `app/(dashboard)/configuracion/page.tsx` | Pending review | — |

### Admin (platform_admin only)

| Path | File | Status | Notes |
|---|---|---|---|
| `/admin` | (no index — redirects via layout) | — | — |
| `/admin/resumen` | `app/admin/resumen/page.tsx` | PARTIAL | Stat cards + margin block + plan breakdown list. No charts yet. Loading/error/empty handled. |
| `/admin/tenants` | `app/admin/tenants/page.tsx` | PARTIAL | Paginated, search/plan/status filters, badges. No courtesy button yet. No row actions. |
| `/admin/tenants/[id]` | `app/admin/tenants/[id]/page.tsx` | PARTIAL | Usage grid, billing dl, clones table. No impersonate button yet. No plan patch UI. |
| `/admin/feedback` | `app/admin/feedback/page.tsx` | PARTIAL | Paginated, rating/search filters, badges, empty state. |
| `/admin/audit` | **MISSING** | NEEDS CREATE | Backend endpoint exists; no UI. |
| `/admin/impersonation` | **MISSING** | NEEDS CREATE | Backend endpoints exist; no UI. The start flow should be a button on tenant detail. |
| `/admin/courtesy` | **MISSING** | NEEDS CREATE | Backend endpoint exists; no UI. The start flow should be a button on tenants list. |

## 2. Layouts

| File | Status | Notes |
|---|---|---|
| `app/layout.tsx` | DONE | DM Sans + JetBrains Mono via `next/font/google`, sets `lang="es"`, `colorScheme: "light"`. |
| `app/(dashboard)/layout.tsx` | DONE | Sidebar + topbar + main, rounded shell, soft shadow. Uses `Sidebar` component. |
| `app/(public)/layout.tsx` | Pending review | — |
| `app/admin/layout.tsx` | NEEDS REWORK | Has its own duplicated sidebar instead of reusing `Sidebar` component. Uses inline `style` instead of CSS class. No nav section headers. No user block. No dark mode toggle. |

## 3. Reusable components (`replica/src/components/`)

| File | Status | Notes |
|---|---|---|
| `dashboard/Sidebar.tsx` | DONE | 220px, with sections (Root, API PLAYGROUND, MANAGEMENT), search stub, FREE TRAIL card, user block, sign-out. |
| `dashboard/HeaderBreadcrumb.tsx` | DONE | — |
| `dashboard/StatsCard.tsx` | DONE | — |
| `dashboard/QuickActionCard.tsx` | DONE | — |
| `dashboard/OnboardingBanner.tsx` | DONE | — |
| `dashboard/EndpointCard.tsx` | DONE | With pastel gradients (lavender, rose, sky, amber, mint). |
| `dashboard/ChatOrb.tsx` | DONE | The decorative orb. |
| `chat/ChatPanel.tsx`, `MessageBubble.tsx`, `SiloToggle.tsx` | Pending review | — |
| `ui/dashboard-icons.tsx` | DONE | 8 icon namespaces, ~40 icons. |

## 4. Design system classes (in `globals.css`)

| Class | Status |
|---|---|
| `.app-shell` | DONE |
| `.card` | DONE |
| `.section-label` | DONE |
| `.endpoint-card` + variants | DONE |
| `.nav-item-active`, `.nav-item-normal` | DONE |
| `.badge-active`, `.badge-trial`, `.badge-warning`, `.badge-error` | DONE |
| `.btn-primary`, `.btn-secondary` | DONE |
| `.tab-active` | DONE |
| `.table-header`, `.table-row` | DONE |
| `.stat-label`, `.stat-value` | DONE |
| `.mono`, `.text-accent` | DONE |
| `prefers-reduced-motion` override | DONE |
| `EmptyState`, `LoadingState`, `ErrorState` | **MISSING** — Phase D6 |
| `MobileNav` (drawer) | **MISSING** — Phase D1 |
| `SearchCommandBar` (⌘K) | **MISSING** — Phase D7 |

## 5. Dark mode

- Dark tokens defined in globals.css under `.dark` and `@media (prefers-color-scheme: dark)`.
- `<html>` is hardcoded to `colorScheme: "light"`. So dark mode is currently opt-in via OS preference only, with no in-app toggle.
- No `useTheme` hook. No `localStorage` persistence.
- Phase D2: add a toggle in the Sidebar user block, persist to `localStorage`, inject an inline `<head>` script to set `.dark` before paint (avoids flash).

## 6. Mock data and hardcoded content

| Location | Issue | Phase |
|---|---|---|
| `app/page.tsx` | "Trusted by 200,000+ users", brand names (Google, Airbnb, Notion, PayPal, Upwork, Shopify, Stripe, Zoom), "4.6 Google / 4.9 Trustpilot", fake notification stack with Terry/Matthew/María | D4 |
| `app/(dashboard)/resumen/page.tsx` | "Recent queries" hardcoded strings; "Getting started" hardcoded steps; "Past 30 days" usage bars hardcoded; `ChatOrb` and `EndpointCard` data fake | E1-E4 |
| `Sidebar.tsx` | "7 days left / Upgrade" hardcoded; progress bar at 14% | D5 |

## 7. Hardcoded colors outside tokens

Found by grep — these should be moved to tokens (Phase D polish):

- `text-purple-600` in `app/login/page.tsx`
- `bg-gray-50 dark:bg-gray-950` in `app/login/page.tsx`
- `bg-black text-white` in `app/(dashboard)/resumen/page.tsx`, `app/page.tsx` (used for the "M" logo and primary buttons — keep but ensure dark mode contrast)

## 8. What is missing (priority order)

1. **Mobile navigation** — drawer for <768px (D1)
2. **Dark mode toggle** with persistence (D2)
3. **Charts** for admin overview and analytics (C5/C6, E5)
4. **Audit log UI** (C2)
5. **Impersonation UI** as a button on tenant detail (C3)
6. **Courtesy signup UI** as a button on tenants list (C4)
7. **EmptyState / LoadingState / ErrorState** shared components (D6)
8. **SearchCommandBar** for ⌘K (D7)
9. **Login redesign** to use design tokens (D3)
10. **Landing page cleanup** to remove fake social proof (D4)
11. **Dashboard resumen real data** (E1-E4)
12. **Responsive table → list rows** for tenants/feedback/audit (D9)
13. **Polish remaining dashboard pages** — inbox, biblioteca, etc. (E5)

## 9. Test coverage

- `vitest` configured in `package.json` but no test files.
- Phase F4: add minimum smoke tests for admin pages (render with no data, render with mock fetch, navigation).
