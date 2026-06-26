# PR Creation - Blocked by Expired GitHub Token - 2026-06-26

## Status

The `fix/ai-costs-missing-rollup-table` branch is fully pushed to
`origin/fix/ai-costs-missing-rollup-table` with all 4 commits. The PR
itself could not be created via `gh pr create` because the local
`GH_TOKEN` is reported as invalid:

```
$ gh auth status
  X Failed to log in to github.com using token (GH_TOKEN)
  - Active account: true
  - The token in GH_TOKEN is invalid.
```

## What to run

After running `gh auth login` (or `gh auth refresh`) successfully, run
this from the repo root:

```bash
gh pr create \
  --base audit/sisyphus-vps-integration-push-sync \
  --head fix/ai-costs-missing-rollup-table \
  --title "fix(ai): costs endpoint 500 - handler tolerates AIInvocation.model vs model_id" \
  --body-file .omo/evidence/pr-body-ai-costs-fix.md
```

A complete PR body is saved at
`.omo/evidence/pr-body-ai-costs-fix.md` for copy-paste.

## Alternative: use the web UI

Visit:
`https://github.com/Teokoaaly/MyOwnClone/compare/audit/sisyphus-vps-integration-push-sync...fix/ai-costs-missing-rollup-table?expand=1`

GitHub will pre-fill the target branch and the title. Paste the PR body
from the file referenced above.

## Branch state (already pushed)

```
$ git log --oneline origin/fix/ai-costs-missing-rollup-table -n 4
0d5f2be docs(sisyphus): record VPS deploy evidence for AI costs fix
ed47382 fix(ai): tolerate AIInvocation.model vs model_id column in costs handler
3a1cddc docs(sisyphus): update HANDOFF_LLM with branch state and AI costs fix handoff
b568ca2 fix(ai): handle missing cost_daily_rollup in admin costs endpoint
```

All evidence lives under `.omo/evidence/`:

- `fix-ai-costs-missing-rollup-table-2026-06-26.md` — root cause + fix description.
- `deploy-ai-costs-fix-vps-2026-06-26.md` — VPS deploy record.
- `backfill-executed-vps-2026-06-26.md` — backfill execution record.
- `current-symlink-investigation-2026-06-26.md` — symlink investigation.
- `pr-body-ai-costs-fix.md` — PR body ready to paste.

## Risk

None. The fix is already live on the VPS (in-container patch with backup
preserved). The PR is a code-archival step, not a deploy trigger.