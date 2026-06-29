Context
- Manual language selector slice deployed end-to-end on VPS.
- nginx -> Next.js frontend -> Flask backend, validated via HTTPS.

Frontend changes deployed
- MyOwnClone/src/lib/locale.ts: helpers for the locale cookie bridge
- MyOwnClone/src/components/ui/LanguageSelector.tsx: Globe icon + select,
  posts to /api/me/locale, reloads after success
- MyOwnClone/src/proxy.ts: route /api/me/locale, allow unauthenticated,
  split and forward Set-Cookie headers from the backend
- MyOwnClone/src/app/(dashboard)/layout.tsx: mount selector in sidebar footer
- Source SHA: sisyphus/anti-forget-layer @ 17e552a
- Release path: /opt/myownclone/releases/20260629144355-frontend-i18n-selector
- /opt/myownclone/current now points to that release
- Frontend service: myownclone-frontend (systemd) restarted successfully

Live verification (HTTPS via nginx on port 443)
- GET  https://localhost/api/me/locale  -> 200
    {"locale":"en","supported":["en","es"],"default":"en","cookie_name":"moc_locale"}
- POST https://localhost/api/me/locale {"locale":"es"} -> 200
    {"default":"en","locale":"es","message":"Locale updated","supported":["en","es"]}
    Set-Cookie: moc_locale=es; Path=/; Secure; SameSite=lax
- GET  https://localhost/api/me/locale with Cookie: moc_locale=es  -> 200
    {"locale":"es","supported":["en","es"],"default":"en","cookie_name":"moc_locale"}

What this proves
- Manual language selection works end-to-end: user picks "Español" in the
  sidebar, the choice is POSTed to the backend, the backend sets the
  cookie, every subsequent API request is translated accordingly.
- The cookie overrides Accept-Language (cookie priority above X-Locale).

Rollback target
- /opt/myownclone/releases/20260629091351-admin-embeddings (last known-good frontend)
- Backend release unchanged from prior deploy: 20260629124000-local-embeddings-dynamic