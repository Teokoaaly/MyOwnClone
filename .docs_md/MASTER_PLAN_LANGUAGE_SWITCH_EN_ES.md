# Master Plan: English and Spanish Language Switching

## Objective

Give every MyOwnClone client the ability to switch the product UI between English and Spanish without breaking routes, auth flows, dashboard actions, forms, analytics, or embedded widgets.

## Product Rules

- Default language: English.
- Supported languages: English (`en`) and Spanish (`es`).
- Brand names stay unchanged in every language: `MyOwnClone`.
- User-generated content, clone names, uploaded knowledge, and conversation transcripts are never translated automatically.
- Dates, numbers, currencies, and relative time must respect the selected language.
- The selected language must persist across sessions and devices when the user is signed in.

## Architecture

1. Use one translation source of truth:
   - `src/i18n/en.json`
   - `src/i18n/es.json`

2. Introduce a `LanguageProvider` at the app shell level:
   - Reads the initial locale from user profile, cookie, or default `en`.
   - Exposes `locale`, `setLocale`, and typed translation helpers.
   - Loads only `en` and `es` messages.

3. Persist language in this order:
   - Authenticated user preference in the database.
   - Cookie fallback: `myownclone_locale`.
   - Browser language only on the first anonymous visit.
   - Default fallback: `en`.

4. Keep functional dashboard routes stable:
   - Existing routes such as `/resumen`, `/biblioteca`, `/chat`, and `/configuracion` remain valid.
   - The language switch changes rendered copy immediately and does not redirect users away from their current task.
   - Optional localized marketing routes can be added later as `/en` and `/es`.

## Implementation Phases

### Phase 1: Foundation

- Confirm `src/i18n/routing.ts` uses `en` as the default locale.
- Keep all current English dashboard copy as the canonical source.
- Rename every legacy `Réplica`, `OEME`, or demo brand reference to `MyOwnClone`.
- Add a typed translation utility so missing keys fail in development.
- Add namespaces:
  - `common`
  - `auth`
  - `dashboard`
  - `sidebar`
  - `settings`
  - `chat`
  - `knowledge`
  - `analytics`
  - `billing`
  - `admin`
  - `errors`

### Phase 2: Language Switcher

- Add a compact language selector in the dashboard sidebar footer and settings page.
- Labels:
  - `English`
  - `Español`
- On selection:
  - Update provider state.
  - Write cookie.
  - Save to user profile when authenticated.
  - Re-render without losing form state where possible.

### Phase 3: Dashboard Migration

- Move hardcoded dashboard labels into translation keys.
- Cover every visible user-facing string:
  - Navigation labels and tooltips.
  - Empty, loading, and error states.
  - Buttons, forms, placeholders, validation messages.
  - Metrics, cards, chart labels, table headers.
  - Toasts and confirmation dialogs.
- Keep technical identifiers untranslated:
  - API keys.
  - URLs.
  - Webhook names.
  - Database IDs.
  - Model names.

### Phase 4: Auth, Onboarding, and Admin

- Translate login, registration, onboarding, verification, admin, billing, and settings flows.
- Ensure all redirects preserve the selected locale.
- Store the selected locale when a new account is created.
- Add an admin-safe fallback so missing Spanish strings render English instead of blank UI.

### Phase 5: Formatting and Data

- Centralize formatting helpers:
  - `formatDate(locale, value)`
  - `formatRelativeTime(locale, value)`
  - `formatNumber(locale, value)`
  - `formatCurrency(locale, value, currency)`
- Apply helpers to analytics cards, charts, usage history, billing values, and activity feeds.
- Verify that charts update labels and tooltips after language changes.

### Phase 6: QA and Release Gate

- Add automated checks:
  - No legacy brand strings in source.
  - No user-facing Spanish strings in English-only files.
  - No missing `en` or `es` translation keys.
  - `npm run lint`
  - `npm run typecheck`
  - `npm run build`

- Manual QA matrix:
  - Public landing page.
  - Login and registration.
  - Dashboard overview.
  - Knowledge library.
  - Chat.
  - Analytics.
  - Automations.
  - Billing.
  - Settings.
  - Admin pages.
  - Embedded widget.

## Acceptance Criteria

- The app defaults to English.
- Users can switch between English and Spanish from the dashboard.
- The selected language persists after refresh, logout, and login.
- Every primary route remains functional in both languages.
- No visible UI uses `OEME`, `Réplica`, or demo-company copy.
- Charts, cards, forms, tables, errors, and empty states are translated.
- Build, typecheck, and lint pass before release.
