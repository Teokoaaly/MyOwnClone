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
- Local HEAD when audited: `d189879`
- Remote integration branch: `origin/audit/sisyphus-vps-integration`
- Remote integration HEAD after fetch: `c00612f`
- Refreshed documentation corpus source: `origin/main` at `8b9d3c1`
- Live VPS base branch: `origin/audit/vps-sync-and-docs`
- Production compatibility base SHA: `e9b9d89`

## Current worktree warning

The original local worktree was dirty when audited. The remote integration
branch has since advanced through M14. Do not batch-commit the dirty local tree.

Required discipline:

- Slice the remaining work by milestone.
- One task = one commit = one push.
- Do not mark a milestone `***REMOVED***` until it has:
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

Done and committed/pushed on the integration branch:

- M0
- M1
- M2
- M4a
- M3
- M4b
- M5
- M6
- M7
- M8
- M9
- M10
- M11
- M12
- M13
- M14

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

Next steps:

1. Validate `origin/audit/sisyphus-vps-integration` on VPS without using the
   bootstrap checkout as a scratch area.
2. Confirm admin login, `/admin/ia-modelos`, registry status, embeddings
   status, costs by model, and backfill UI on the running deployment.
3. Start the post-Sisyphus prompt foundation tranche from
   `.omo/evidence/docs-to-backlog-2026-06-26.md`.
