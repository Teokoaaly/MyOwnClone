Context
- The dashboard was missing the LanguageSelector because the
  sisyphus/anti-forget-layer branch (where it was added) had never been
  merged into deploy/maint-mode-plus-wip.
- The deploy branch was running an older frontend without the selector,
  the proxy.ts returned 502 "Backend unavailable" on /api/me/locale due
  to an incomplete cherry-pick that left the JSON branch empty.

Resolution
- Cherry-picked commit 17e552a (LanguageSelector) from sisyphus/anti-forget-layer
  onto deploy/maint-mode-plus-wip; resolved 2 conflicts in
  MyOwnClone/src/app/(dashboard)/layout.tsx and MyOwnClone/src/proxy.ts.
- Restored the full proxy.ts JSON-response block (clones cookie,
  Set-Cookie forwarding) that was truncated by the regex-based conflict
  resolution.

Branch state after the fix
- deploy/maint-mode-plus-wip @ 269a4e5
  - 196e3a9 chore(deploy): bring in STT + i18n changes
  - 34afddd feat(frontend): LanguageSelector + cookie bridge to /me/locale
  - 269a4e5 fix(frontend): restore complete JSON response path in proxy.ts

Live verification on VPS (HTTPS via nginx)
- GET  https://localhost/                  -> 200 (42ms)
- GET  https://localhost/login             -> 200
- GET  https://localhost/console           -> 200
- GET  https://localhost/api/me/locale     -> 200
    {"locale":"en","supported":["en","es"],"default":"en","cookie_name":"moc_locale"}
- POST https://localhost/api/me/locale {"locale":"es"} -> 200
    Set-Cookie: moc_locale=es; Path=/; Secure; SameSite=lax
    {"default":"en","locale":"es","message":"Locale updated","supported":["en","es"]}
- POST https://localhost/api/me/locale {"locale":"fr"} -> 400
    {"error":"unsupported_locale","message":"Unsupported locale","supported":["en","es"]}

Container / service state
- myownclone_api: Up (healthy), /readyz -> ok
- myownclone-frontend (systemd): restarted after rebuild
- nginx: still serving HTTPS as before

Rollback
- /opt/myownclone/releases/20260629124000-local-embeddings-dynamic
  (last known-good backend)
- Frontend service: keep the previous build at .next under the same path
  if needed.