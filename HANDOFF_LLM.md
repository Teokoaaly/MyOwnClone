# HANDOFF_LLM - resumable Sisyphus execution

This handoff is the fast path for another agent. Read this file first, then:

1. `TASKS.md`
2. `.sisyphus/progress.json`
3. `.omo/plans/sisyphus-system-improvement.md`
4. `.omo/evidence/repo-vps-study-matrix-2026-06-26.md`
5. `.omo/evidence/docs-to-backlog-2026-06-26.md`

## Current local state

- Workspace: `C:\Users\haxth3\Documents\MyOwnClone`
- Local branch for AI costs fix in progress: `fix/ai-costs-missing-rollup-table`
  - HEAD: `4a1e252` (no new commits yet at handoff time; fix is staged)
  - Base: `audit/sisyphus-vps-integration-push-sync` (NOT the `audit/sisyphus-vps-integration` branch this handoff originally assumed).
- Local branch: `audit/sisyphus-vps-integration`
  - HEAD: `9f5c9a6` — this branch is BEHIND the integration branch and
    **does NOT contain M8-M14**. A previous agent believed it was the
    integration lane, but the M8-M14 work lives on
    `audit/sisyphus-vps-integration-push-sync` (HEAD `fa03fea`).
  - The remote `origin/audit/sisyphus-vps-integration` HEAD is `4a1e252`,
    which is the same SHA as the push-sync branch tip — confirming both
    branches converge at the integration SHA, but the M8-M14 series is
    cherry-picked on top of `push-sync` only.
- Remote integration branch: `origin/audit/sisyphus-vps-integration-push-sync`
  - HEAD: `fa03fea` (or current at push time) — contains M1, M2, M3, M4a,
    M4b, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, plus the reconciliation
    commits.
- Refreshed documentation corpus source: `origin/main` at `8b9d3c1`
- Live VPS base branch: `origin/audit/vps-sync-and-docs`
- Production compatibility base SHA: `e9b9d89`

## Current worktree warning

The original local worktree was dirty when audited. The remote integration
branch has since advanced through M14. Do not batch-commit the dirty local tree.

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

## 2026-06-26 handoff: AI costs endpoint 500 fix

Symptom: `GET /console/api/myownclone/ai-models/costs` returns 500 on the live
VPS even when authenticated as `platform_admin`. All sibling AI admin
endpoints (`ai-models`, `assignments`, `registry-status`, `embedding-status`)
return 200.

Investigation summary:

- `audit/sisyphus-vps-integration` HEAD `9f5c9a6` does NOT carry M8-M14;
  M8-M14 live on `audit/sisyphus-vps-integration-push-sync` HEAD `fa03fea`
  / `4a1e252` (the same SHA the remote reports).
- The live backend gunicorn is running code equivalent to M14
  (`api/controllers/console/myownclone/ai_models.py` is byte-identical to
  the M14 commit `c00612f`); the bootstrap checkout has uncommitted drift
  and was NOT used for diagnosis.
- `cost_daily_rollup` table is almost certainly missing in the live DB:
  every other admin query returns 200 with empty data, while `costs` 500s on
  the first `select(CostDailyRollup)` call with no `ProgrammingError`
  guard.

Fix in progress on branch `fix/ai-costs-missing-rollup-table` (based on
`audit/sisyphus-vps-integration-push-sync`):

- Wrap the rollup query in `try/except ProgrammingError` and fall through to
  the existing `AIInvocation` aggregation.
- Wrap the per-model breakdown and the fallback queries similarly so the
  endpoint degrades to empty series instead of 500 if either table is
  missing.
- Add regression tests:
  `test_ai_model_costs_handles_missing_rollup_table`,
  `test_ai_model_costs_handles_both_tables_missing`.
- Fix pre-existing broken test `test_ai_model_costs_aggregates_rows` (the
  M14 baseline already failed this one because `model_id` was missing from
  the mock rows).

Evidence: `.omo/evidence/fix-ai-costs-missing-rollup-table-2026-06-26.md`.

Local verification: 10/10 tests pass in
`api/tests/test_ai_models_endpoints.py`. `git diff --check` is clean.

Deploy is OUT OF SCOPE of this unit. The user explicitly required rollback
+ SHA + explicit approval before any production change. Recommended next
deploy step: cherry-pick or merge this fix into the integration branch and
redeploy the backend release `20260623000000-M13-defects-backfill` (or its
successor).
