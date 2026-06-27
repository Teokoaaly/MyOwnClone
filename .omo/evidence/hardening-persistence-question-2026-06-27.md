# Hardening Persistence Question - 2026-06-27

## Question

User asked: "esas mejoras resten en la implementacion original?"
(English: "Did these improvements persist in the original implementation?")

## Short answer

No. The hardening operations performed on 2026-06-27 are VPS-runtime
adjustments only. None of them touched the project's source code:

1. `/opt/myownclone/shared/api_env.json` — VPS-only file, not in repo.
2. `chmod +x` on `/opt/myownclone/current/ops/backup_postgres.sh` —
   VPS-only filesystem permission change.
3. Docker image tags `myownclone_api:v1.0.0-costs-fix` —
   VPS-only Docker metadata.
4. `docker builder prune` — Docker cache cleanup, no persistent effect.
5. `post-deploy-hardening-2026-06-27.md` — documentation only.

None of these are present in any branch of the repo. The repo HEAD on
`audit/sisyphus-vps-integration` is `f427c53` (PR #5 merge).

## Risk discovered during the audit

When verifying which file path the `chmod +x` actually modified, I
found that the cron `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh`
points to the symlinked release directory:

```
/opt/myownclone/current -> /opt/myownclone/releases/20260620070304-frontend-dashboard-fix
```

That release directory was NOT deleted in the cleanup (only the 2026-06-17
to 2026-06-19 frontend-only releases and the 2026-06-23 M13 backend
release were deleted). So the `chmod +x` change SHOULD have persisted
on the file at:
`/opt/myownclone/releases/20260620070304-frontend-dashboard-fix/MyOwnClone/ops/backup_postgres.sh`

This is acceptable for now. But the deploy pipeline should fix this in
source: the script should be `chmod +x` in the deploy script (e.g.,
in `ops/deploy-backend.sh` or a dedicated `ops/bootstrap-backend.sh`).

## SSH connection loss at the end

After the hardening operations, the SSH session from the local machine
to the VPS (via Tailscale) became unresponsive. Connection attempts
timed out at 5 minutes.

This is the same pattern observed on 2026-06-26 (sandbox / firewall
restriction on the local Windows host). Operations completed BEFORE
the timeout:

- `/opt/myownclone/shared/api_env.json` was created and verified.
- `/opt/myownclone/current/ops/backup_postgres.sh` had `chmod +x`
  applied.
- A manual backup run via `sudo -n /opt/myownclone/current/ops/backup_postgres.sh 7`
  completed successfully and produced
  `/opt/myownclone/backups/myownclone_20260627_085126.sql.gz` (9.7 KB,
  22 tables).
- Docker image tags were applied.

Operations NOT verified after the timeout:

- Whether the `chmod +x` change persists across container restarts
  (it should, because the file is on the host filesystem, not inside
  the container).
- Whether the new container is still healthy.
- Whether the daily cron (next run at 03:00 UTC) succeeds.

## Recommendation

The hardening SHOULD be persisted in the project source via a small
follow-up commit that:

1. Adds `chmod +x` to the file mode in the deploy script (or in a
   pre-deploy hook).
2. Documents the `api_env.json` durable location in
   `ops/README.md` or similar.
3. Adds an off-host backup copy step (e.g., `aws s3 sync` or
   equivalent) so a single disk failure does not lose all backups.

These would require a new commit on `audit/sisyphus-vps-integration-push-sync`
or a PR against `master`, plus a fresh deploy to apply them.

For now, the hardening lives only on the live VPS filesystem. If the
host is re-imaged, the changes are lost.

## Commits in this session that touched repo code

- `b568ca2` — defensive try/except (M14 handler) — also via PR #5
- `3a1cddc` — HANDOFF_LLM update
- `ed47382` — actual fix (via PR #5, merged)
- `0d5f2be` — VPS deploy evidence
- `ac5906f` — PR blocker note
- `63453a8` — backfill evidence
- `ea9f5e8` — current symlink investigation
- `1848359` — PR creation blocker update
- `9cc95c7` — SSH access loss
- `01e4456` — final session summary 2026-06-26
- `8de59bb` — repo cleanup plan + VPS runbook
- `69b4424` — WIP recovery incident
- `f427c53` — PR #5 merge (the actual code change)
- `dcbfa32` — PR #5 success
- `8b18bea` — final cleanup report 2026-06-27
- `8f73137` — final VPS deploy
- `2c0c0fb` — post-deploy hardening

All of these are documentation or the single `ed47382` / `f427c53` code
change. The hardening changes themselves are not in any commit.