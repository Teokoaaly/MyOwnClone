# HANDOFF_LLM - resumable Sisyphus execution

This handoff is the fast path for another agent. Read this file, then
`TASKS.md`, then `.sisyphus/progress.json`.

## Current local state

- Workspace: `C:\Users\haxth3\Documents\MyOwnClone`
- Local branch: `master`
- Remote branch with M0-M2: `origin/feature/sisyphus-m1-data-layer`
- Live VPS base branch: `origin/audit/vps-sync-and-docs`
- Live VPS checkout has uncommitted i18n changes and must not be used as a work
  area

## Current VPS facts

- Bootstrap checkout branch: `audit/vps-sync-and-docs`
- Bootstrap SHA: `e9b9d89`
- Release symlink: `/opt/myownclone/current -> /opt/myownclone/releases/20260620070304-frontend-dashboard-fix`
- Containers healthy: `myownclone_api`, `myownclone_postgres`,
  `myownclone_redis`, `myownclone_weaviate`

## Execution rules

- Create a separate VPS worktree or checkout from `origin/audit/vps-sync-and-docs`
- Work branch: `audit/sisyphus-vps-integration`
- Integrate `M0-M2` first from `origin/feature/sisyphus-m1-data-layer`
- One task = one commit = one push
- Update `.sisyphus/progress.json` and evidence on every milestone
- Correct rollback scripts before any deployment attempt

## What is already prepared locally

- `TASKS.md` contains the M3-M13 checklist
- `.sisyphus/progress.json` contains the resumable milestone state
- `.sisyphus/evidence/` contains templates for pending milestones
- `.sisyphus/plans/ai-models-configurable.md` contains the compact plan source

## Next recommended step

- Create the VPS integration worktree
- Bring `M0-M2` into that lane
- Fix rollback scripts
- Record evidence in `.sisyphus/evidence/task-preflight-rollback.md`
