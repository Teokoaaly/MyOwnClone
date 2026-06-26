# SSH Access Lost - 2026-06-26

## What happened

Mid-session, `ssh myownclone@100.125.128.116` started returning
`ssh: connect to host 100.125.128.116 port 22: Permission denied` for
all subsequent attempts (retried 3x with `ConnectTimeout=5`).

Verbose SSH shows the connection is rejected BEFORE the handshake:

```
debug1: Connecting to 100.125.128.116 [100.125.128.116] port 22.
debug1: connect to address 100.125.128.116 port 22: Permission denied
ssh: connect to host 100.125.128.116 port 22: Permission denied
```

This pattern is consistent with one of:

1. VPS rebooted and the SSH port is still bound but auth config changed
   (e.g. host key rotation not picked up by local `known_hosts`).
2. Firewall / security group on the VPS started dropping my client IP.
3. Network intermediary (carrier-grade NAT, VPN client reset) is
   intercepting port 22.
4. The VPS is in a transient state (booting, snapshotting, network
   reconfiguring) and SSH is briefly unavailable.

The first 5 successful SSH calls in this session worked fine, which
strongly suggests the VPS itself is still up but the network path is
temporarily broken or rate-limited.

## What this blocks

| Planned step | Affected | Mitigation |
| --- | --- | --- |
| Persist fix in `ops-api` image (rebuild + docker cp + restart gunicorn) | YES — needs `docker cp` into `myownclone_api` | Re-run when SSH is restored. The in-container patch is still in place; if the container has not restarted, the fix is still live. |
| Push 4 evidence commits to `origin/audit/sisyphus-vps-integration` | NO — pure git operation | Can be done from local repo, no SSH needed. |
| Populate `cost_daily_rollup` via `flask ai-rotate-audit` | YES — needs `docker exec` into the container | Re-run when SSH is restored. |

## Live VPS state at time of SSH loss

Just before SSH went down, the live state was verified as:

- `/console/api/myownclone/ai-models/costs` → 200 with `minimax-m2.7` data
- `ai-models` and `assignments` populated (1 model + 3 assignments)
- `/readyz` → ready
- All 5 admin AI endpoints → 200
- `/app/api/controllers/console/myownclone/ai_models.py` patched with
  `_invocation_model_key` helper
- `/app/api/controllers/console/myownclone/ai_models.py.bak` preserved
  inside the container as the rollback target
- `/app/api/controllers/console/myownclone/ai_models.py.bak.pre-fix-20260626-094937`
  preserved as the second backup

If the container has NOT been restarted, the live fix is still active
and the admin panel still works. If it HAS restarted, the fix is lost
and the endpoint returns 500 again (deploy from this branch via PR +
rebuild is the recovery path).

## How to recover

When SSH returns, re-run this session's outstanding steps. The current
working state on the local repo is:

```
audit/sisyphus-vps-integration   HEAD = c1fbcbd (5 ahead, 9 behind origin)
fix/ai-costs-missing-rollup-table  up to date with origin (5 commits)
```

The next SSH agent should:

1. Re-verify SSH access: `ssh myownclone@100.125.128.116 "echo ok"`.
2. Check container state: `sudo -n docker ps -a --filter name=myownclone_api`.
3. If the container was recreated, the fix is lost — restore from
   `fix/ai-costs-missing-rollup-table` by `git checkout` on the host and
   re-applying the in-container patch.
4. Continue with the 3 remaining steps (persist image, push evidence
   commits, populate rollup).

## Risk

- If the container was restarted in the gap: the fix is lost and the
  panel returns 500. Detection: try `GET /console/api/myownclone/ai-models/costs`
  with a Bearer token; non-200 means restart happened.
- The two backups inside the container (`*.bak`, `*.bak.pre-fix-*`) are
  container-local files; they vanish on container recreation.

## No further actions were taken in this session after SSH loss

This file is the last write to the repo from this session. Subsequent
agents should resume from here.