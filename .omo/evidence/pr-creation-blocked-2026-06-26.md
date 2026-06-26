# PR Creation - Blocked by Expired GitHub Token - 2026-06-26 (update)

## Status

The `fix/ai-costs-missing-rollup-table` branch is fully pushed to
`origin/fix/ai-costs-missing-rollup-table` with all 5 commits. The PR
itself could not be created via `gh pr create` because the local
`GH_TOKEN` (from env) returns HTTP 401 from the GitHub API.

## Exact error observed (re-attempted 2026-06-26)

```
$ gh pr create --base audit/sisyphus-vps-integration-push-sync \
    --head fix/ai-costs-missing-rollup-table \
    --title "fix(ai): costs endpoint 500 - handler tolerates AIInvocation.model vs model_id" \
    --body-file .omo/evidence/pr-body-ai-costs-fix.md

HTTP 401: Bad credentials (https://api.github.com/graphql)
Try authenticating with:  gh auth login
```

```
$ gh auth status
  X Failed to log in to github.com using token (GH_TOKEN)
  - Active account: true
  - The token in GH_TOKEN is invalid.
```

The token is set in the shell environment (`GH_TOKEN` is non-empty) but
the API rejects it. It is expired, revoked, or for the wrong account.

## What to run

After refreshing the GitHub token (one of these, in order of preference):

```bash
# Option A: re-authenticate via gh (interactive)
gh auth login

# Option B: refresh an existing token via gh
gh auth refresh

# Option C: provide a new token via env
export GH_TOKEN=ghp_newtoken...

# Then create the PR
gh pr create \
  --base audit/sisyphus-vps-integration-push-sync \
  --head fix/ai-costs-missing-rollup-table \
  --title "fix(ai): costs endpoint 500 - handler tolerates AIInvocation.model vs model_id" \
  --body-file .omo/evidence/pr-body-ai-costs-fix.md
```

## Alternative: use the web UI

Visit:
`https://github.com/Teokoaaly/MyOwnClone/compare/audit/sisyphus-vps-integration-push-sync...fix/ai-costs-missing-rollup-table?expand=1`

GitHub will pre-fill the target branch and the title. Paste the PR body
from `.omo/evidence/pr-body-ai-costs-fix.md`.

## Branch state (already pushed)

```
$ git log --oneline origin/fix/ai-costs-missing-rollup-table -n 5
ac5906f docs(sisyphus): record PR creation blocked by expired GH token
0d5f2be docs(sisyphus): record VPS deploy evidence for AI costs fix
ed47382 fix(ai): tolerate AIInvocation.model vs model_id column in costs handler
3a1cddc docs(sisyphus): update HANDOFF_LLM with branch state and AI costs fix handoff
b568ca2 fix(ai): handle missing cost_daily_rollup in admin costs endpoint
4a1e252 docs(sisyphus): reconcile VPS and corpus handoff state
```

## Evidence files in this directory

- `fix-ai-costs-missing-rollup-table-2026-06-26.md` — root cause + fix.
- `deploy-ai-costs-fix-vps-2026-06-26.md` — VPS deploy record.
- `backfill-executed-vps-2026-06-26.md` — backfill execution.
- `current-symlink-investigation-2026-06-26.md` — symlink investigation.
- `pr-body-ai-costs-fix.md` — PR body ready to paste.

## Risk

None. The fix is live on the VPS. The PR is a code-archival step, not
a deploy trigger.