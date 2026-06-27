# Maintenance Mode + WIP Deploy — Design

**Date**: 2026-06-27
**Author**: Claude (ZCode) for Hacchi
**Status**: APPROVED by user, pending implementation plan

## Context

The user wants to apply two changes to the running production system
on the VPS:

1. **Maintenance mode** with admin-only access. Login must remain
   functional for everyone. Non-admin users see a full-screen
   "maintenance" message. Admins see a yellow banner at the top of
   every admin page. All write operations (POST/PUT/DELETE/PATCH) are
   blocked while maintenance is active, even for admins.

2. **Sisyphus M8–M13 WIP** (commit `67262b6` on
   `wip/sisyphus-m8-m13-preservation`) needs to be applied to
   `audit/sisyphus-vps-integration` and deployed to the VPS.

The deployment sequence is:

```
maintenance ON → backup DB + code → apply WIP → run tests →
   if pass → maintenance OFF
   if fail → rollback (git revert + restore DB)
```

## Decisions captured during brainstorming

| Question | Decision |
| --- | --- |
| Maintenance UX | Banner amarillo arriba + bloqueo de funciones |
| Who can use during maintenance | Solo admins (platform_admin role) |
| Scope of changes | PR #5 (already merged) + Sisyphus WIP |
| Banner style | Yellow banner fixed at top, full-width, with countdown |
| Activation mechanism | Flag in DB (`system_settings` table) |
| Rollback strategy | Backup + restore (snapshot before applying) |
| Deploy order | Maintenance ON → backup → apply WIP → tests → Maintenance OFF |

## Architecture

### Backend additions

1. **`api/models/system_settings.py`** — new SQLAlchemy model for
   `system_settings` table:

   ```python
   class SystemSetting(db.Model):
       __tablename__ = "system_settings"
       key = db.Column(db.String(64), primary_key=True)
       value = db.Column(db.Text, nullable=True)
       updated_at = db.Column(db.DateTime, default=datetime.utcnow)
   ```

2. **`api/migrations/versions/2026_06_27_0001_system_settings.py`** —
   new migration:

   ```python
   def upgrade():
       op.create_table(
           "system_settings",
           sa.Column("key", sa.String(64), primary_key=True),
           sa.Column("value", sa.Text, nullable=True),
           sa.Column("updated_at", sa.DateTime, server_default=sa.func.now()),
       )
       op.execute(
           "INSERT INTO system_settings (key, value) VALUES ('maintenance_mode', 'false')"
       )
   ```

3. **`api/core/maintenance.py`** — new module exposing:

   ```python
   def is_maintenance_active() -> bool:
       """Read maintenance flag from DB. Fail-open on DB error."""
       try:
           row = db.session.execute(
               select(SystemSetting.value).where(SystemSetting.key == "maintenance_mode")
           ).scalar_one_or_none()
           return row == "true"
       except Exception:
           logger.exception("Failed to read maintenance flag; failing open")
           return False
   ```

4. **`api/middleware/maintenance.py`** — Flask before_request hook:

   ```python
   @app.before_request
   def enforce_maintenance():
       if not is_maintenance_active():
           return
       # Allow login endpoints
       if request.path.endswith("/auth/login") or "/maintenance-status" in request.path:
           return
       # Allow GET requests for admins
       if request.method == "GET" and _is_admin():
           return
       # Block everything else
       return jsonify({"error": "service_unavailable",
                       "message": "Sistema en mantenimiento"}), 503
   ```

5. **`api/controllers/console/myownclone/maintenance.py`** — new
   controller with two endpoints:

   - `GET /console/api/myownclone/maintenance/status` — public,
     returns `{active: bool, message: str}`
   - `POST /console/api/myownclone/maintenance/toggle` — admin only,
     flips the DB flag.

### Frontend additions

1. **`MyOwnClone/src/app/admin/layout.tsx`** — modify to fetch
   `/maintenance/status` every 60s and render the yellow banner when
   active. Banner has countdown text and a "Mantener sesión" button
   (dismissible for 5 minutes).

2. **`MyOwnClone/src/app/maintenance/page.tsx`** — new full-screen
   page for non-admin users. Shows the same status from
   `/maintenance/status` but does not render the dashboard.

3. **`MyOwnClone/src/middleware.ts`** — modify to redirect non-admin
   users to `/maintenance` when the status endpoint reports
   maintenance active.

### Data flow

```
Client (admin)            Client (non-admin)
   │                            │
   ├─ GET /maintenance/status   ├─ GET /maintenance/status
   │   ← {active: true}         │   ← {active: true}
   │                            │
   ├─ Render banner at top      ├─ Render full-screen page
   │                            │
   ├─ POST /api/anything        ├─ POST /api/anything
   │   ← 503 (blocked)          │   ← 503 (blocked)
```

### Error handling

- **DB read error** in `is_maintenance_active()` → fail-open (return
  `False`). This avoids taking down the site when the DB is having
  problems.
- **Invalid flag value** in DB (not 'true' / 'false') → fail-closed
  (treat as `true`). Safer to assume maintenance is on than off.
- **Banner fetch error** on client → silent retry, banner does not
  show (assume maintenance off).
- **Toggle endpoint** when not admin → 403 (existing auth).

## Files touched

### Backend (new)
- `api/core/maintenance.py`
- `api/models/system_settings.py`
- `api/middleware/maintenance.py`
- `api/controllers/console/myownclone/maintenance.py`
- `api/migrations/versions/2026_06_27_0001_system_settings.py`
- `api/tests/test_maintenance.py`

### Backend (modified)
- `api/app_factory.py` (register middleware)

### Frontend (new)
- `MyOwnClone/src/app/maintenance/page.tsx`

### Frontend (modified)
- `MyOwnClone/src/app/admin/layout.tsx`
- `MyOwnClone/src/middleware.ts`

### Deployment
- `ops/deploy-backend.sh` (verify new migration is auto-applied)
- `ops/deploy-frontend.sh` (verify build includes new page)

### Documentation
- `docs/maintenance-mode.md` (operator runbook)

## Sisyphus WIP contents (commit `67262b6`)

The WIP adds/modifies 14 files vs `audit/sisyphus-vps-integration`:

```
api/controllers/console/myownclone/ai_models.py      +16/-7   (M9 catalog)
api/tests/test_ai_models_endpoints.py                +30/-28  (M9 tests)
docs/model-backfill-and-rollout.md                   -98/-98   (M9 docs cleanup)
tests/test_plan_completion.py                        +8/-9    (M9 test helper)
... (10 more files)
```

Net change: +599/-1172 (mostly deletions — code cleanup + new tests).

The WIP also includes the Sisyphus anti-forget layer which is
preserved on `sisyphus/anti-forget-layer` branch but NOT part of this
deploy.

## Deploy sequence (final)

### Phase 1: Prepare (online, no maintenance)

1. Create branch `deploy/maint-mode-plus-wip` based on
   `audit/sisyphus-vps-integration`.
2. Cherry-pick WIP commit `67262b6` onto it.
3. Add maintenance mode files (per design above).
4. Push branch.
5. Run unit tests locally (no production risk).

### Phase 2: Activate maintenance (online)

1. SSH to VPS.
2. Apply migration `2026_06_27_0001_system_settings` to create the
   flag table.
3. Set flag to `true`:
   `UPDATE system_settings SET value='true' WHERE key='maintenance_mode';`
4. Reload gunicorn workers (SIGHUP) so the middleware picks up the
   flag on next request.
5. Verify: `curl /console/api/myownclone/maintenance/status` returns
   `{active: true}`.

### Phase 3: Backup

1. Snapshot DB:
   `pg_dump myownclone > /opt/myownclone/backups/pre-wip-$(date +%s).sql`
2. Snapshot code: tag current worktree HEAD as
   `pre-wip-deploy-$(date +%Y%m%d-%H%M%S)`.

### Phase 4: Deploy code

1. In the worktree: `git fetch && git checkout deploy/maint-mode-plus-wip`.
2. Rebuild Docker image: `docker compose -f docker-compose.backend.prod.yml build api`.
3. Tag new image as `myownclone_api:v1.1.0-maint-mode-wip`.
4. Stop + remove old container, start new container with same env vars
   from `/opt/myownclone/shared/api_env.json`.
5. Smoke test: `curl /readyz` and `curl /console/api/myownclone/maintenance/status`.

### Phase 5: Apply migrations

1. Inside the new container:
   `flask db upgrade`
2. Verify `system_settings` table exists with
   `maintenance_mode = 'true'`.

### Phase 6: Run integration tests

1. `pytest api/tests/test_maintenance.py` — should pass.
2. `pytest api/tests/test_ai_models_endpoints.py` — should pass.
3. Manual smoke: curl admin endpoints, expect 200/403 patterns as
   designed.

### Phase 7: Deactivate maintenance

1. Set flag to false:
   `UPDATE system_settings SET value='false' WHERE key='maintenance_mode';`
2. Reload gunicorn (SIGHUP).
3. Verify: `/maintenance/status` returns `{active: false}`.

### Phase 8: Rollback procedure (if Phase 6 fails)

1. `git checkout pre-wip-deploy-*` in worktree.
2. Rebuild image tagged as `myownclone_api:rollback`.
3. Stop current container, start container with rollback image.
4. Restore DB: `psql myownclone < /opt/myownclone/backups/pre-wip-*.sql`.
5. Deactivate maintenance (even though site is broken, this lets
   users see what's happening).

## Out of scope

- Hardening improvements from prior session (env vars backup, image
  tags, etc.) — already applied to VPS but not in source.
- Sisyphus anti-forget layer (`sisyphus/anti-forget-layer` branch).
- Cleanup of remaining uncommitted WIP files in
  `audit/sisyphus-vps-integration` working tree.
- Documentation for the 3 remaining remote branches with unique
  content (`i18n/exec-en-es`, `feature/sisyphus-m1-data-layer`,
  `feature/standard-rag-pipeline`).

## Risks

1. **Long deploy window**: The full sequence takes 10-30 minutes
   during which the site is in maintenance mode. Users see a yellow
   banner / full-screen message but no admin actions work.
2. **Rollback complexity**: If Phase 6 fails, the rollback involves
   both image swap AND DB restore, which must happen in the right
   order. Failures here could leave the site broken.
3. **Tenant-level maintenance**: This design is GLOBAL maintenance,
   not per-tenant. If a tenant needs their own maintenance flag,
   that's a future feature.
4. **Banner state on client**: The banner uses client-side polling
   (60s interval). If a tab is in the background, the user may not
   see the maintenance state immediately.
5. **Database migration**: The new `system_settings` migration must be
   applied BEFORE the flag is set to 'true'. If applied out of order,
   the API will throw on first request to `/maintenance/status`.