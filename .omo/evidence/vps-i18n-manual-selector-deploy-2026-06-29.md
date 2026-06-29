Context
- Phase E: deploy the manual locale selector slice.
- Release rebuilt in place from the live backend tree; the api image was
  rebuilt and restarted with the production env sourced before bring-up.

Changes deployed
- api/i18n.py: locale priority is now cookie > X-Locale > ?locale > Accept-Language > default
- api/controllers/console/myownclone/locale.py: new public GET/POST /me/locale
- api/middleware/maintenance.py: uses English msgid; Spanish translation lives in messages.po
- api/locales/{en,es}/LC_MESSAGES/messages.{po,mo}: regenerated via pybabel
- api/tests/test_i18n.py: 23 tests covering cookie priority, endpoint set/get
- Container image: ops-api:latest (rebuilt)
- Backend release path: /opt/myownclone/releases/20260629124000-local-embeddings-dynamic
- Source SHA: deploy/maint-mode-plus-wip @ e16dcda
- Worktree: /opt/myownclone/worktrees/sisyphus-vps-integration

Live verification
- GET /console/api/myownclone/me/locale (no hint) -> 200
    {"locale": "en", "supported": ["en", "es"], "default": "en", "cookie_name": "moc_locale"}
- POST /console/api/myownclone/me/locale {"locale":"es"} -> 200
    {"default":"en","locale":"es","message":"Locale updated","supported":["en","es"]}
    Set-Cookie: moc_locale=es
- GET /console/api/myownclone/me/locale (Cookie: moc_locale=es) -> 200
    {"locale": "es", "supported": ["en", "es"], "default": "en", "cookie_name": "moc_locale"}

Container health
- myownclone_api: Up (healthy)
- /readyz: {"checks":{"database":"ok","redis":"ok"},"status":"ready"}
- env: JWT_SECRET_KEY, REDIS_PASSWORD, DB_PASSWORD all set in container

Rollback target
- /opt/myownclone/releases/20260629123253-local-embeddings-backend (previous known-good)