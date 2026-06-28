# Maintenance + WIP Deploy - Completed 2026-06-28

## Summary

Full maintenance mode + Sisyphus M8-M13 WIP deployment completed end-to-end.
All 17 tasks from the implementation plan executed.

## Final VPS State

- Container `myownclone_api` UP, healthy, image `myownclone_api:v1.1.0-maint-mode-wip`
- Tag `v1.1.0-rc1` pushed to origin
- Maintenance flag: `false` (inactive)
- Backup DB: `/opt/myownclone/backups/pre-maintenance-20260628-092803.sql.gz`
- Git backup tag: `pre-maintenance-deploy-20260628-092812`
- Env vars durable: `/opt/myownclone/shared/api_env.json`

## Commits Deployed (deploy/maint-mode-plus-wip branch)

```
2d2eacc fix: resolve merge conflict in ai_models.py after deploy
76ab692 fix: register maintenance controller and use JWT decode for admin bypass
091b2b3 test: fix test mocks to work with maintenance middleware
efe1de1 merge WIP Sisyphus M8-M13 into deploy/maint-mode-plus-wip
a9496f0 feat(frontend): redirect non-admin to /maintenance during active mode
3d3d516 feat(frontend): add yellow maintenance banner to admin layout
b3738ca feat(frontend): add maintenance full-screen page
88d84bc chore(app): register maintenance middleware in app factory
+ Tasks 1-5 (model, migration, helper, middleware, controller)
```

## Issues Encountered & Resolved

1. **alembic.ini missing from image**: alembic command failed. Workaround:
   applied migration directly via `psql` to create `system_settings` table.

2. **maintenance controller not registered**: The new
   `api/controllers/console/myownclone/maintenance.py` was not in the
   controllers `__init__.py` imports list. Patched manually in container,
   then committed to worktree and rebuild.

3. **Admin blocked by middleware**: `_is_admin()` initially looked at
   `g.current_user` and `g.user`, but the middleware runs BEFORE
   `login_required` decorator populates those. Patched to:
   - Check `g.account_role` (set by login_required)
   - Check `X-User-Role` header (set by Next.js proxy)
   - Fallback: direct JWT decode from Authorization Bearer

4. **JWT decode NameError**: `name 'json' is not defined` because
   `maintenance.py` didn't import `json` and `base64`. Fixed by adding
   imports.

5. **Test mocks broken**: WIP merge caused test mocks for
   `db.session.execute` to fail because the maintenance middleware
   also uses the same DB session. Fixed by detecting `system_settings`
   queries in the mocks and returning `scalar_one_or_none()=None`.

## Live Validation (2026-06-28 09:43 UTC)

| Endpoint | Status | Response |
| --- | --- | --- |
| `/readyz` | 200 | `{db: ok, redis: ok}` |
| `/console/api/myownclone/maintenance/status` | 200 | `{"active": false}` |
| `/console/api/myownclone/ai-models` (admin) | 200 | 1 row |
| `/console/api/myownclone/ai-models/costs` (admin) | 200 | real data |
| `/console/api/myownclone/admin/overview` (admin) | 200 | OK |
| Same with maintenance active | 200 | admin bypassed |

## Maintenance Mode Tested and Working

Test sequence executed:
1. Activate flag → `true`
2. Reload gunicorn (SIGHUP)
3. Non-admin request → 503 (correctly blocked)
4. Admin request → 200 (correctly bypassed)
5. Deactivate flag → `false`
6. Reload → all 200

## Rollback Procedure (if needed)

```bash
ssh myownclone@100.125.128.116
cd /opt/myownclone/worktrees/sisyphus-vps-integration
sudo -n -u myownclone git checkout pre-maintenance-deploy-20260628-092812
cd ops
sudo -n docker compose -f docker-compose.backend.prod.yml build api
sudo -n docker tag ops-api:latest myownclone_api:rollback
sudo -n docker stop myownclone_api && sudo -n docker rm myownclone_api
# Use the env file at /opt/myownclone/shared/api_env.json
python3 /tmp/gen_docker_run.py
# Edit the script to use the rollback tag, then run it
bash /tmp/run_cmd.sh
```

## Next Steps

- The WIP work (commit `67262b6` on `wip/sisyphus-m8-m13-preservation`)
  was preserved and is now merged into the deploy branch.
- The WIP can now be integrated into the main line via PR from
  `deploy/maint-mode-plus-wip` to `audit/sisyphus-vps-integration`.
- The maintenance mode feature is production-ready. Admins can toggle
  the flag with a manual SQL update:

  ```sql
  UPDATE system_settings
  SET value = 'true'
  WHERE key = 'maintenance_mode';
  ```
