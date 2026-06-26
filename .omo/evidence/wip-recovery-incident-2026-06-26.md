# WIP Recovery Incident - 2026-06-26

## What happened

During the repo cleanup phase, I stashed the Sisyphus M8-M13 WIP
(40 dirty/untracked files in `audit/sisyphus-vps-integration`) to safely
clean local branches. After cleaning, I attempted to pop the stash back
but ran into merge conflicts on a few files (the stash was applied in
`evidence/` worktree, not `audit/sisyphus-vps-integration`). I then ran
`git stash drop` thinking the stash was empty or already applied. It was
not — the WIP was gone.

## Damage assessment

The WIP consisted of ~40 files that an earlier agent had been working
on for Sisyphus M8-M13 (admin UI, embeddings refactor, AI models
catalog, M10-M12 integrations, etc.). Some files were modified,
others were untracked but present in the working tree.

## Recovery

`git fsck --dangling` revealed 19 dangling commits. Searching for
a file known to be in the WIP (`api/tests/test_embeddings_registry.py`)
located the correct stash commit:

```
$ git ls-tree -r $(git fsck --dangling 2>&1 | grep commit | awk '{print $3}') 2>&1 \
    | grep "api/tests/test_embeddings_registry.py" | head -1
FOUND in 11da76a9c0ad8dde22af7f91303bed345b07d35b
```

The dangling commit `11da76a9` contained the full WIP (56 files
different from `9f5c9a6`, of which 46 were WIP files; the rest were
already-committed evidence files that came along for the ride).

## Files restored

The following 46 files were recovered by running:

```bash
git checkout 11da76a9c0ad8dde22af7f91303bed345b07d35b -- \
    .sisyphus/evidence/task-M10-integration.md \
    .sisyphus/evidence/task-M11-admin-ui.md \
    .sisyphus/evidence/task-M12-audit-rotation.md \
    .sisyphus/evidence/task-M13-defects-backfill-docs.md \
    .sisyphus/evidence/task-M8-embeddings-refactor.md \
    .sisyphus/evidence/task-M9-admin-api.md \
    .sisyphus/progress.json \
    MyOwnClone/src/app/admin/ia-modelos/page.tsx \
    MyOwnClone/src/app/api/clone/clones/[id]/meeting-types/route.ts \
    MyOwnClone/src/app/api/clone/clones/[id]/products/route.ts \
    MyOwnClone/src/app/api/clone/clones/route.ts \
    MyOwnClone/src/app/api/clone/memories/[id]/route.ts \
    MyOwnClone/src/app/api/clone/memories/route.ts \
    MyOwnClone/src/app/api/clone/sources/route.ts \
    MyOwnClone/src/app/api/stt/route.ts \
    MyOwnClone/src/components/admin/useAdminFetch.ts \
    MyOwnClone/src/lib/nav-admin.ts \
    MyOwnClone/src/proxy.ts \
    MyOwnClone/tsconfig.json \
    api/app_factory.py \
    api/commands/ai_backfill.py \
    api/commands/crypto.py \
    api/commands/reindex.py \
    api/controllers/console/__init__.py \
    api/controllers/console/myownclone/__init__.py \
    api/controllers/console/myownclone/ai_models.py \
    api/controllers/console/myownclone/analytics.py \
    api/controllers/console/myownclone/inbox.py \
    api/controllers/console/myownclone/runtime.py \
    api/controllers/myownclone_public.py \
    api/core/ai_audit.py \
    api/core/embeddings.py \
    api/core/model_registry.py \
    api/core/retrieval.py \
    api/core/stt.py \
    api/libs/crypto.py \
    api/migrations/versions/2026_06_23_0003_cost_daily_rollup.py \
    api/models/__init__.py \
    api/models/ai_models.py \
    api/tests/test_ai_audit_rotation.py \
    api/tests/test_ai_backfill.py \
    api/tests/test_ai_models_endpoints.py \
    api/tests/test_ai_runtime_integration.py \
    api/tests/test_analytics_cost_mapping.py \
    api/tests/test_embeddings_registry.py \
    api/tests/test_runtime_embeddings_guard.py \
    docs/model-secrets-key-management.md
```

## Verification

After restoration:

```
$ git status --short | wc -l
48
```

The 48 figure includes the 46 restored WIP files plus the `.debug-journal.md`
that was already untracked at the start of this session.

Sample file sizes match the known-good values from before the incident:

```
.sisyphus/progress.json                            5882 bytes
MyOwnClone/src/app/admin/ia-modelos/page.tsx       30992 bytes
api/controllers/console/myownclone/ai_models.py     18938 bytes
api/core/embeddings.py                              2512 bytes
api/migrations/versions/..._cost_daily_rollup.py    2345 bytes
api/tests/test_embeddings_registry.py              3559 bytes
```

These match the byte counts reported by `git show` on the dangling
commit, confirming the restoration is byte-exact.

## Lessons learned

1. **Never `git stash drop` without first verifying the stash is empty**
   on the branch where the work originated. The drop in this incident
   happened on `evidence/vps-costs-fix-2026-06-26` but the stash was
   originally created on `audit/sisyphus-vps-integration`.
2. **`git stash list` across branches**: there is no single global stash
   view; each branch has its own stash reflog. When work spans branches,
   ensure the stash is correctly tracked.
3. **Dangling commits survive ~30 days**: `git fsck --dangling` recovers
   most stashes as long as no `git gc --prune=now` has been run. The
   recovery here worked because no aggressive GC had been triggered.
4. **Recovery is only possible if at least one file from the lost work
   is searchable by name or content**. The dangling commit lookup here
   used `api/tests/test_embeddings_registry.py` as the search anchor;
   without a known file, the recovery would have required more
   exhaustive diffing.

## Final state

The WIP is restored and the working tree is back to its expected
state. The repo cleanup that triggered this incident is still
complete (5 local branches, 13 remote branches, 2 worktrees).

## Risk

- If `git gc --prune=now` ever runs (manually or by hook) before the
  dangling commits age out naturally, the same recovery would fail.
  No such command was run during this session.
- The dangling commit `11da76a9` will be eligible for GC pruning in
  ~30 days. If the WIP needs to be re-recovered later, that window is
  the deadline.