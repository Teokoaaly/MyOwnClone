Context
- User reported the live frontend was using a version they had NOT
  approved. Three commits had been merged to deploy/maint-mode-plus-wip
  that introduced frontend changes (LanguageSelector, /signup, /registro
  redirect, etc.) without explicit approval.

Resolution
- Identified the three unauthorized commits and reverted them in
  deploy/maint-mode-plus-wip:
  - 34afddd  feat(frontend): LanguageSelector + cookie bridge to /me/locale
  - 269a4e5***REMOVED***x(frontend): restore complete JSON response path in proxy.ts
  - 4f60ff2  feat(frontend): unify Spanish/English UX
- Revert chain produced three new commits:
  - de61f0b  Revert "feat(frontend): LanguageSelector + cookie bridge..."
  - bccec61  Revert "fix(frontend): restore complete JSON response path..."
  - 6984c6c  Revert "feat(frontend): unify Spanish/English UX"
- Synced the authorized frontend code from the worktree into the live
  release directory, deleted MyOwnClone/src/components/ui/LanguageSelector.tsx,
  deleted MyOwnClone/src/lib/locale.ts, deleted MyOwnClone/src/app/signup/.
- Rebuilt the frontend with --rm .next so stale chunks are purged.

Authorized version
- Reference: origin/audit/sisyphus-vps-integration @ 1fe0ae3
  "fix(frontend): reserve dashboard route for workspace"

Final state on VPS
- Frontend at /opt/myownclone/releases/20260629144355-frontend-i18n-selector/MyOwnClone
- /opt/myownclone/current -> that release
- Git branch: deploy/maint-mode-plus-wip @ 6984c6c (now back at the
  authorized audit baseline + the backend-only chore commit 196e3a9
  that brought STT + i18n backend files in)

Live verification (HTTPS via nginx)
- GET  /                            -> 200 (no LanguageSelector in HTML)
- GET  /login                       -> 200 (no LanguageSelector in HTML)
- GET  /registro                    -> 200 (Spanish original form, "Crea tu cuenta y empieza a escalarte")
- GET  /signup                      -> 404 page (route no longer exists)
- GET  /api/me/locale               -> 404 page (route no longer exists in proxy.ts)
- LanguageSelector occurrences in /, /login HTML: 0
- /signup HTML contains "404: This page could not be found" (correct)

Backend untouched and still working
- /readyz -> {"checks":{"database":"ok","redis":"ok"},"status":"ready"}
- /console/api/myownclone/me/locale -> 200
    {"locale":"en","supported":["en","es"],"default":"en","cookie_name":"moc_locale"}
- ADAPTER_TYPES includes local_whisper for STT

Note
- The /api/me/locale frontend route was removed together with the
  LanguageSelector. The backend endpoint at /console/api/myownclone/me/locale
  is still operational and accessible to internal services / tests. If
  the manual locale selector is desired in the future it will need
  explicit approval before re-introducing.