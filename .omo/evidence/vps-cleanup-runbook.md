# VPS Cleanup Runbook - 2026-06-26

## Status

This runbook is NOT executed in the current session because SSH to
`100.125.128.116` returns `WinError 10013: Permission denied` from
this Windows host's sandbox. Execute it when SSH access returns.

## What to remove (release directories)

`/opt/myownclone/releases/` currently has 8 release directories
(verified 2026-06-26 morning UTC). Of these:

### SAFE TO DELETE (verified)

These are frontend-only releases that have been superseded by the
`/opt/myownclone/current` symlink (which points to
`20260620070304-frontend-dashboard-fix`). Removing them has NO impact
on the running services:

- `20260617135142-frontend-bgfix6`
- `20260617135242-frontend-bgfix7`
- `20260617135429-frontend-bgfix8`
- `20260617185014-frontend-landing-restore`
- `20260619221443-security-fixes`
- `20260619223743-frontend-security-fixes`

### KEEP

- `20260620070304-frontend-dashboard-fix` — referenced by
  `/opt/myownclone/current` and used by `myownclone-frontend.service`.

### CONDITIONAL (verify before delete)

- `20260623000000-M13-defects-backfill` — historical backend release.
  The live backend container does NOT use this directory (the container
  uses the worktree `/opt/myownclone/worktrees/sisyphus-vps-integration`).
  It is dead code as far as the running services are concerned.
  HOWEVER, before deleting, run this check:

  ```bash
  sudo -n grep -rl "20260623000000-M13-defects-backfill" /opt/myownclone/ 2>/dev/null
  sudo -n grep -rl "20260623000000-M13-defects-backfill" /etc/systemd/ 2>/dev/null
  ```

  If any reference appears, update that reference first or skip the
  deletion.

## What to inspect (do NOT delete)

- `/opt/myownclone/backups/` — needs separate investigation; contents
  unknown. Do not touch without inspecting.
- `/opt/myownclone/bootstrap/MyOwnClone` — separate git checkout used
  for deploy audit; may or may not be active. Inspect before action.
- `/opt/myownclone/shared/` — env files used by running services.
  Inspect before action.
- `/opt/myownclone/worktrees/sisyphus-vps-integration/` — ACTIVE
  worktree used by the live backend container. **DO NOT DELETE**.

## Commands to run

### Step 1: dry-run audit

```bash
sudo -n ls -la /opt/myownclone/releases/
sudo -n ls -la /opt/myownclone/worktrees/
sudo -n ls -la /opt/myownclone/backups/ 2>&1 | head -5
sudo -n ls -la /opt/myownclone/bootstrap/ 2>&1 | head -5
sudo -n readlink /opt/myownclone/current
sudo -n systemctl status myownclone-frontend.service --no-pager
sudo -n docker ps --format '{{.Names}} {{.Image}} {{.Status}}'
```

### Step 2: pre-flight grep (M13 conditional delete)

```bash
sudo -n grep -rl "20260623000000-M13-defects-backfill" \
    /opt/myownclone/ /etc/systemd/ /etc/nginx/ 2>/dev/null \
    | grep -v "20260623000000-M13-defects-backfill/" \
    | head -20
```

If output is empty or only contains references to the directory itself
(safe to ignore), proceed to step 3.

### Step 3: delete obsolete frontend releases

```bash
cd /opt/myownclone/releases
for d in \
    20260617135142-frontend-bgfix6 \
    20260617135242-frontend-bgfix7 \
    20260617135429-frontend-bgfix8 \
    20260617185014-frontend-landing-restore \
    20260619221443-security-fixes \
    20260619223743-frontend-security-fixes; do
    if [ -d "$d" ]; then
        sudo -n rm -rf "$d"
        echo "Deleted: $d"
    else
        echo "Not present: $d"
    fi
done
```

### Step 4: conditional delete of M13 release

ONLY if step 2 found no external references:

```bash
sudo -n rm -rf /opt/myownclone/releases/20260623000000-M13-defects-backfill
echo "Deleted M13 release"
```

### Step 5: verify post-cleanup

```bash
sudo -n ls -la /opt/myownclone/releases/
# Expected: only 20260620070304-frontend-dashboard-fix remains

# Smoke test: ensure frontend still serves
curl -sS http://127.0.0.1:3000/api/auth/session -o /dev/null -w "%{http_code}\n"
# Expected: 200

# Smoke test: ensure backend still serves
curl -sS http://127.0.0.1:5001/readyz
# Expected: {"checks":{"database":"ok","redis":"ok"},"status":"ready"}
```

### Step 6: report

After step 5 passes, run:

```bash
sudo -n du -sh /opt/myownclone/releases/
sudo -n du -sh /opt/myownclone/releases/* 2>/dev/null
```

This gives a before/after disk usage report. Save the output as
`.omo/evidence/vps-cleanup-completed-2026-06-26.md` for the record.

## Disk recovery estimate

The 6 obsolete frontend releases are likely 50-200 MB each (Next.js
build artifacts). Total recovery is probably 0.5 - 1.5 GB.

## Rollback

There is no rollback for `rm -rf`. If something goes wrong, the
git objects for those releases are still recoverable from
`/opt/myownclone/worktrees/sisyphus-vps-integration/` if those files
were ever committed (they probably weren't — release directories are
typically not under version control). The frontend service would
restart from `current` (which is untouched) and serve normally.

## Why this is deferred

This session lost SSH access mid-work (sandbox blocked TCP to
`100.125.128.116:22`). The next agent with restored SSH access
should resume from here. The full audit rationale is in
`.omo/evidence/repo-cleanup-plan-2026-06-26.md`.