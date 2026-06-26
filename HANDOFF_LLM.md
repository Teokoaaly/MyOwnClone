# HANDOFF_LLM - resumable Sisyphus execution

This handoff is the fast path for another agent. Read this file first, then:

1. `TASKS.md`
2. `.sisyphus/progress.json`
3. `.omo/plans/sisyphus-system-improvement.md`
4. `.omo/evidence/repo-vps-study-matrix-2026-06-26.md`
5. `.omo/evidence/docs-to-backlog-2026-06-26.md`

## Current local state

- Workspace: `C:\Users\haxth3\Documents\MyOwnClone`
- Local branch: `audit/sisyphus-vps-integration`
- Local HEAD: `d189879`
- Remote integration branch: `origin/audit/sisyphus-vps-integration`
- Remote integration HEAD visible locally: `5baa1bc`
- Refreshed documentation corpus source: `origin/main` at `8b9d3c1`
- Live VPS base branch: `origin/audit/vps-sync-and-docs`
- Production compatibility base SHA: `e9b9d89`

## Current worktree warning

The local worktree is dirty. It contains mixed work from M8-M13 plus planning
artifacts under `.omo/`. Do not batch-commit the whole tree.

Required discipline:

- Slice the remaining work by milestone.
- One task = one commit = one push.
- Do not mark a milestone `done` until it has:
  - evidence file updated
  - tests executed
  - commit SHA recorded
  - remote push confirmed

## Current VPS facts

- Tailscale SSH worked for audit with user `myownclone`.
- Live release symlink:
  - `/opt/myownclone/current -> /opt/myownclone/releases/20260620070304-frontend-dashboard-fix`
- The live release is not a git checkout.
- Frontend:
  - `myownclone-frontend.service` is active.
- Backend:
  - `myownclone-backend.service` is not present as a systemd unit.
- Docker:
  - user `myownclone` cannot access `/var/run/docker.sock`.
- Bootstrap checkout:
  - path: `/opt/myownclone/bootstrap/MyOwnClone`
  - branch: `audit/vps-sync-and-docs`
  - SHA: `e9b9d89fa75706cf6818f595a062aaacf48c4575`
- Bootstrap checkout has local drift, including i18n changes and partially
  ported Sisyphus files. Treat it as audit/deploy context, not a development
  work area.

## Current Sisyphus state

Done and committed:

- M0
- M1
- M2
- M4a
- M3
- M4b
- M5
- M6
- M7

Not yet closed cleanly:

- M8: embeddings refactor
- M9: admin API
- M10: runtime integrations
- M11: admin UI
- M12: audit / rollup / key rotation
- M13: defects / backfill / final docs

The repo already contains code/evidence fragments for M8-M13, but they are not
yet safe to treat as complete until they are sliced, verified, committed, and
pushed.

## Documentation corpus status

The OSINT/wiki corpus is confirmed in `origin/main` after `git fetch origin main`.

Confirmed paths include:

- `briefings/`
- `concepts/`
- `entities/`
- `raw/articles/`
- `assets/infographics/myownclone-osint-complete-report/`
- `queries/myownclone-blueprint.md`
- `comparisons/`
- `SCHEMA.md`
- `index.md`

The corpus has already been distilled into:

- `.omo/evidence/docs-to-backlog-2026-06-26.md`

Do not use raw OSINT as a direct implementation spec. Use the distilled backlog.

## Execution rules

- Do not edit the live VPS release as a dev workspace.
- Do not use the VPS bootstrap checkout as a scratch area.
- Do not merge `origin/master` or `origin/main` into the integration branch as a
  shortcut.
- Port only specific, reviewed files or commits when needed.
- Preserve the current admin-login hotfix in `MyOwnClone/src/lib/auth.ts` unless
  tests prove a better replacement.
- Preserve unrelated user/i18n changes.

## Next recommended step

Start with Todo 1 from `.omo/plans/sisyphus-system-improvement.md`:

- reconcile `.sisyphus/progress.json`
- finish milestone slicing plan for M8-M13
- commit only documentation/tracker reconciliation first

Then continue with:

1. M8 + M10 runtime slice
2. M9 admin API slice
3. M11 admin UI / visibility slice
4. M12 + M13 operational closure
5. VPS validation
6. post-Sisyphus prompt foundation plan
