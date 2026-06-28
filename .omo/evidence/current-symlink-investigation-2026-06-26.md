# Current Symlink Investigation - 2026-06-26

## Question

Why does `/opt/myownclone/current` point to a release that contains only the
frontend (`20260620070304-frontend-dashboard-fix/MyOwnClone`) while the live
backend gunicorn runs inside a docker container whose `/app` is bind-mounted
from the worktree `sisyphus-vps-integration` (commit `c00612f`)?

## Short answer

There is no inconsistency. `/opt/myownclone/current` is exclusively a
**frontend** symlink. The backend is containerized and managed by a
different mechanism (docker compose project `ops`), which uses its own
bind mounts and does not consult `current` at all.

## Evidence

### `current` symlink target

```
/opt/myownclone/current ->
  /opt/myownclone/releases/20260620070304-frontend-dashboard-fix
```

### Consumers of `current`

Only two files reference it:

1. `/opt/myownclone/releases/20260623000000-M13-defects-backfill/ops/myownclone-frontend.service`:
   ```ini
   WorkingDirectory=/opt/myownclone/current/MyOwnClone
   EnvironmentFile=/opt/myownclone/shared/frontend.env.production
   ExecStart=/usr/bin/npm run start -- --hostname ${HOSTNAME} --port ${PORT}
   ```
2. `/opt/myownclone/releases/20260623000000-M13-defects-backfill/ops/backup_postgres.sh`:
   ```sh
   #   0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 ...
   ```
   This is only a comment in a cron recipe; the script itself reads from
   `/opt/myownclone/releases/...` directly, not from `current`.

### Frontend systemd unit

`myownclone-frontend.service` is `loaded`, `active (running)` since
2026-06-23, and `enabled`. It is the only `myownclone*` systemd unit on
the host. The frontend Next.js process tree:

```
634841 npm run start --hostname 127.0.0.1 --port 3000
634899 sh -c "next start --hostname 127.0.0.1 --port 3000"
634900 next-server (v16.2.9)
```

`/opt/myownclone/current/MyOwnClone` resolves to
`/opt/myownclone/releases/20260620070304-frontend-dashboard-fix/MyOwnClone`,
which is the cwd of the npm process. **This is correct.**

### Backend (NOT using `current`)

The 4 live containers are part of the docker compose project `ops`:

| Container | Compose project | cwd inside container |
| --- | --- | --- |
| `myownclone_api` | `ops` | `/app` |
| `myownclone_redis` | `ops` | `/data` |
| `myownclone_postgres` | `ops` | `/var/lib/postgresql/data` |
| `myownclone_weaviate` | `ops` | `/var/lib/weaviate` |

The backend gunicorn loads `api.app_factory:app` from `/app/api/...` inside
the container, which is bind-mounted from the worktree
`/opt/myownclone/worktrees/sisyphus-vps-integration/` (commit `c00612f`).

The `ops` compose file (`ops/docker-compose.backend.prod.yml`) is what
defines the bind mount. It does NOT use `/opt/myownclone/current`.

### Why the M13 release directory exists but isn't `current`

`/opt/myownclone/releases/20260623000000-M13-defects-backfill/` is a
historical artifact: the M13 backend fixes were built and tested there,
but the live container image was constructed from the worktree, not from
that release directory. The deploy script `ops/deploy-backend.sh` does
reference it (it expects a docker-compose flow that pins to a release),
but the actual run was a manual `docker exec`-driven path that bypassed
the release symlink.

## Conclusion

The `current` symlink is intentionally a frontend-only artifact. The
backend deploy path does not use it. The user-visible symptom of
"current points to a frontend-only release while the backend is
elsewhere" is correct behavior, not a bug.

## Side notes (worth fixing later)

1. The M13 release directory
   `20260623000000-M13-defects-backfill` is dead code: no systemd unit,
   no compose service, no symlink. Either delete it, or wire it back
   into the deploy pipeline as a fallback for when the worktree is not
   the desired build source.
2. The `ops/deploy-backend.sh` script is out of sync with reality: it
   expects to run against a `docker compose` project but the live
   container was started manually. Either update the script to match
   the manual path or set up a systemd-driven compose that owns the
   container lifecycle.
3. There is no `myownclone-backend.service` systemd unit. If the host
   reboots, the four containers (including the api) come back because
   docker's default restart policy is `unless-stopped` and the containers
   were `docker run`-ed with that policy, NOT because of any unit. Worth
   documenting and adding an explicit `myownclone-backend.service` if
   the user wants declarative restart behavior.

## Risk assessment

No risk to the just-deployed AI costs fix: the fix lives inside the
running container, and the container's restart behavior is independent
of `current`. The symlink investigation is purely documentation.