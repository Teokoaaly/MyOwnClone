# Evidence Branch Pushed + Outstanding Blockers - 2026-06-26

## Evidence branch created and pushed

A new branch `evidence/vps-costs-fix-2026-06-26` was created from
`origin/audit/sisyphus-vps-integration` (HEAD `4a1e252`) and pushed
to `origin/evidence/vps-costs-fix-2026-06-26` (HEAD `9cc95c7`).

The branch contains 4 cherry-picked evidence commits from this
session:

```
9cc95c7 docs(sisyphus): record SSH access loss mid-session 2026-06-26
1848359 docs(sisyphus): record exact HTTP 401 error from re-attempted PR creation
ea9f5e8 docs(sisyphus): investigate current symlink - it is frontend-only
63453a8 docs(sisyphus): record VPS backfill execution for AI models registry
4a1e252 docs(sisyphus): reconcile VPS and corpus handoff state (base)
```

These are pure documentation commits under `.omo/evidence/`. No
source code changes.

## Why a separate branch instead of a push to `audit/sisyphus-vps-integration`

The local `audit/sisyphus-vps-integration` HEAD `c333fa5` is 5
commits ahead of `origin/audit/sisyphus-vps-integration` HEAD
`4a1e252`, BUT the remote is 9 commits ahead of the local
(M8/M9/M10/M11/M12/M13/M14 + reconciliation + M1 fix).

Attempting `git pull --rebase` produced content conflicts in
`HANDOFF_LLM.md` and `.sisyphus/progress.json`, both of which are
files that were modified by both this session and prior sessions in
ways that would require human review to merge safely.

Cherry-picking the evidence commits onto a branch that tracks
`origin/audit/sisyphus-vps-integration` avoids those conflicts and
gets the documentation to the remote immediately.

## Outstanding items after this session

| Item | Status | Why blocked |
| --- | --- | --- |
| Persist AI costs fix in `ops-api` image | Blocked | SSH to `100.125.128.116` returns `Permission denied` (see `ssh-access-lost-2026-06-26.md`). |
| Populate `cost_daily_rollup` via `flask ai-rotate-audit` | Blocked | Same SSH outage. |
| Create PR for `fix/ai-costs-missing-rollup-table` | Blocked | `GH_TOKEN` env var returns HTTP 401 from `api.github.com`. `git push` works via Git Credential Manager. PR must be created via web UI or after re-authenticating `gh` interactively. |
| Push evidence commits to `audit/sisyphus-vps-integration` | Soft blocked | The rebase conflicts are in `HANDOFF_LLM.md` and `.sisyphus/progress.json`. Easier to leave the separate evidence branch as the source of truth. |

## Branch state

```
* audit/sisyphus-vps-integration            # local, 6 commits ahead, 9 behind origin
  evidence/vps-costs-fix-2026-06-26         # NEW, pushed, 4 evidence commits
  fix/ai-costs-missing-rollup-table         # up to date with origin
  master
  ... (other unrelated branches)
```

## Last known VPS state (before SSH outage)

```
GET /console/api/myownclone/ai-models/costs           -> HTTP 200
GET /console/api/myownclone/ai-models                 -> HTTP 200 (1 row)
GET /console/api/myownclone/ai-models/assignments     -> HTTP 200 (3 rows)
GET /console/api/myownclone/ai-models/registry-status -> HTTP 200
GET /console/api/myownclone/ai-models/embedding-status -> HTTP 200
GET /readyz                                            -> HTTP 200
```

In-container patch (commit `ed47382`) is in place. Backups
`ai_models.py.bak` and `ai_models.py.bak.pre-fix-20260626-094937`
are preserved.

## Risk if SSH outage persists into a container restart

The in-container patch is lost on container recreate. Recovery
paths:

1. `docker cp` from `fix/ai-costs-missing-rollup-table` (needs SSH).
2. Rebuild `ops-api` image with the fix baked in (needs SSH + docker).
3. Merge the fix into the integration branch and trigger a redeploy.

## Session end

No further actions were taken after the SSH outage. The next agent
should resume from here, starting with re-verifying SSH access.