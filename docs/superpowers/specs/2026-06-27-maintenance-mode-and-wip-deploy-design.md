# Maintenance Mode + WIP Deploy — Design

**Date**: 2026-06-27
**Author**: Claude (ZCode) for Hacchi
**Status**: APPROVED v1 + CORRECTED v2 (pre-deploy audit found 3 errors)
**Version**: 2 (corrections applied 2026-06-27)

**CORRECTIONS in v2**:
1. WIP file count: was 14, actually 15.
2. Cherry-pick of WIP has add/add conflicts on 4 files with PR #5
   (`f427c53`). Phase 4a added with manual merge resolution strategy.
3. SSH to VPS is blocked by local sandbox. Phase 4d cannot run until
   user re-authorizes Tailscale. Decision: defer VPS phases; do
   code-only work now.

See `.omo/evidence/pre-deploy-audit-errors-found-2026-06-27.md` for
full audit details.

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

**CORRECTED 2026-06-27 (pre-deploy audit found file count was wrong)**.

The WIP adds/modifies **15 files** vs `audit/sisyphus-vps-integration`
(+599/-1467 net, not -1172 as previously stated):

```
.omo/evidence/backfill-executed-vps-2026-06-26.md                       +109  (new)
.omo/evidence/current-symlink-investigation-2026-06-26.md              +117  (new)
.omo/evidence/ssh-access-lost-2026-06-26.md                            +90   (new)
.omo/evidence/deploy-ai-costs-fix-vps-2026-06-26.md                    -137  (removed)
.omo/evidence/fix-ai-costs-missing-rollup-table-2026-06-26.md          -154  (removed)
.omo/evidence/pr-creation-blocked-2026-06-26.md                        +53/-some  (modified)
.omo/evidence/...other 4 evidence files                                 ...
HANDOFF_LLM.md                                                          +.../-113  (modified)
.hermes/plans/2026-06-23_M14-admin-panels.md                            -403  (removed)
docs/model-backfill-and-rollout.md                                     -98   (removed)
MyOwnClone/src/app/api/stt/route.ts                                    +.../-...   (modified)
MyOwnClone/src/components/admin/useAdminFetch.ts                       +.../-...   (modified)
api/controllers/console/myownclone/ai_models.py                        +16/-7   (M9 catalog)
api/tests/test_ai_models_endpoints.py                                  +.../-...  (M9 tests)
tests/test_plan_completion.py                                         +8/-9    (M9 test helper)
```

**CONFLICT WARNING**: 4 files have add/add conflicts with PR #5
(`f427c53`, the AI costs fix that was already merged):

- `MyOwnClone/src/app/api/stt/route.ts` (text conflicts)
- `MyOwnClone/src/components/admin/useAdminFetch.ts` (text conflicts)
- `api/controllers/console/myownclone/ai_models.py` (add/add)
- `api/tests/test_ai_models_endpoints.py` (add/add)

**These conflicts must be resolved manually before the deploy can
proceed.** Resolution strategy: see "Phase 4b: Conflict resolution"
below.

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

### Phase 4a (PRE-DEPLOY): Conflict resolution

**This phase must be done BEFORE Phase 4**. The WIP commit (`67262b6`)
was created before PR #5 was merged, so cherry-picking it onto
`audit/sisyphus-vps-integration` produces add/add conflicts on 4 files.

Manual resolution strategy (decision approved by user 2026-06-27):

1. **Stash current WIP** from `audit/sisyphus-vps-integration` working
   tree (no live WIP currently exists, this is just a precaution).
2. **Create deploy branch**:
   `git checkout -b deploy/maint-mode-plus-wip audit/sisyphus-vps-integration`.
3. **Cherry-pick WIP**:
   `git cherry-pick 67262b6` — will fail with conflicts.
4. **Resolve each conflict manually**:

   For each of the 4 files in conflict, the resolution depends on the
   file:

   - **`MyOwnClone/src/app/api/stt/route.ts`** and
     **`useAdminFetch.ts`**: text conflicts. Open each file, look for
     `<<<<<<<`, `=======`, `>>>>>>>` markers. The WIP version is
     typically MORE recent (improvements to existing API surface).
     Default strategy: take WIP version, then re-run `tsc` to verify
     no type errors.

   - **`api/controllers/console/myownclone/ai_models.py`**:
     add/add conflict. The WIP modifies this file with the M14 catalog
     changes. PR #5 (already merged) modifies it with the costs fix
     (`_invocation_model_key` helper). Both modifications should be
     kept: the file should have BOTH the WIP M14 catalog changes AND
     the costs fix. Resolution: edit the file manually to include
     both sets of changes.

   - **`api/tests/test_ai_models_endpoints.py`**: similar add/add.
     Both branches added test cases. The WIP version contains tests
     for M14 catalog; the PR #5 version contains tests for the
     `_invocation_model_key` helper. Keep both sets of tests.

5. **Mark as resolved**: `git add <file>` for each resolved file.
6. **Continue cherry-pick**: `git cherry-pick --continue`.
7. **Verify**: `git log --oneline -n 3` to see the WIP commit on the
   deploy branch.

### Phase 4b: Add maintenance mode code

After the WIP is applied to `deploy/maint-mode-plus-wip`, add the
maintenance mode files (per design above):

1. Create the new files:
   - `api/core/maintenance.py`
   - `api/models/system_settings.py`
   - `api/middleware/maintenance.py`
   - `api/controllers/console/myownclone/maintenance.py`
   - `api/migrations/versions/2026_06_27_0001_system_settings.py`
   - `api/tests/test_maintenance.py`
   - `MyOwnClone/src/app/maintenance/page.tsx`

2. Modify existing files:
   - `api/app_factory.py` (register middleware)
   - `MyOwnClone/src/app/admin/layout.tsx` (banner)
   - `MyOwnClone/src/middleware.ts` (redirect non-admin)

3. Commit each logical group separately:
   - Commit 1: "feat(api): add maintenance mode middleware and model"
   - Commit 2: "feat(api): add maintenance controller endpoints"
   - Commit 3: "feat(frontend): add maintenance banner and full-screen page"
   - Commit 4: "chore(api): register maintenance middleware in app factory"

### Phase 4c: Local validation

Before deploying to VPS, validate locally:

1. Run unit tests:
   `pytest api/tests/test_maintenance.py api/tests/test_ai_models_endpoints.py`
2. Run frontend build (if Node.js available):
   `cd MyOwnClone && npm run build`
3. If both pass, push the deploy branch.

### Phase 4d: VPS deploy (BLOCKED until SSH restored)

**SSH TO VPS IS CURRENTLY BLOCKED.** This phase cannot run from this
session. Defer until the user re-authorizes Tailscale auth.

Once SSH works:

1. Tag the deploy branch as `v1.1.0-rc1`.
2. `git fetch && git checkout v1.1.0-rc1` in the VPS worktree.
3. Rebuild image.
4. Stop + remove old container, start new container.
5. Smoke test.

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