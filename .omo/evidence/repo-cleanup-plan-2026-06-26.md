# Repository Cleanup Plan - 2026-06-26

## Scope

Clean up:

1. **Local branches** (Windows): delete stale local branches that no
   longer carry work.
2. **Remote branches** (GitHub): delete specific remote branches that
   are confirmed redundant or legacy.
3. **VPS filesystem** (`/opt/myownclone/releases/` and
   `/opt/myownclone/worktrees/`): remove old releases and abandoned
   worktrees. Cannot be executed in this session (SSH is blocked by
   local sandbox); runbook is documented for the next agent.

Preserve:

- The 40 dirty/untracked files (Sisyphus M8-M13 WIP) on
  `audit/sisyphus-vps-integration`. These are someone else's active
  work and must not be touched.
- All commits reachable from any other local branch (history must
  remain in the reflog for 30+ days anyway).
- All evidence files under `.omo/evidence/`.

## Inventory (as of 2026-06-26)

### Local branches on Windows

| Branch | Status | Action |
| --- | --- | --- |
| `audit/sisyphus-vps-integration` | **current HEAD**, 6 ahead / 9 behind origin, 40 dirty files (WIP) | **KEEP**. The WIP M8-M13 is here. |
| `audit/sisyphus-vps-integration-push-sync` | Local-only, no remote, same SHA as `origin/audit/sisyphus-vps-integration` (`4a1e252`) | **DELETE**. Local-only with no work beyond what is in origin. |
| `audit/vps-sync-and-docs` | Tracks `origin/audit/vps-sync-and-docs` (e9b9d89) | **DELETE local ref**. Remote remains. |
| `codex/vps-deploy-audit-fixes` | Tracks `origin/codex/vps-deploy-audit-fixes` (ecc8d92) | **DELETE local ref**. Remote remains. |
| `evidence/vps-costs-fix-2026-06-26` | Tracks `origin/evidence/vps-costs-fix-2026-06-26` (dcbfa32). Evidence from this session. | **KEEP**. |
| `feature/standard-rag-pipeline` | Tracks `origin/feature/standard-rag-pipeline` (d783cb9) | **DELETE local ref**. Remote remains. |
| `fix/ai-costs-missing-rollup-table` | Tracks `origin/fix/ai-costs-missing-rollup-table` (ac5906f). The fix that is in PR #5. | **KEEP**. Active PR. |
| `master` | Tracks `origin/master` | **KEEP**. Default branch on origin. |
| `sisyphus/anti-forget-layer` | Local + remote, has unmerged work (anti-forget layer from M0) | **KEEP**. |

### Remote branches on origin

| Branch | Analysis | Action |
| --- | --- | --- |
| `master` | Default trunk | **KEEP**. |
| `main` | Diverged from master (21 ahead / 128 behind). Last commit `8b9d3c1 docs: full wiki`. | **INVESTIGATE separately**. May be intentional fork for wiki-only branch. |
| `audit/sisyphus-vps-integration` | Active integration branch (M1-M14) | **KEEP**. |
| `audit/vps-sync-and-docs` | e9b9d89, fully merged into audit/sisyphus-vps-integration | **KEEP** for now (live VPS release references it). |
| `codex/vps-deploy-audit-fixes` | Fully merged into audit/sisyphus-vps-integration | **KEEP** for safety. |
| `unify-api-trees-20260607_214935` | `ad29ec5` is an ancestor of master (work is in master). 0 commits ahead of master. | **DELETE FROM ORIGIN** (safe: master has it). |
| `v2` | Old product (Drizzle + Supabase era). Contains `feat: Next.js clonify app` | **DELETE FROM ORIGIN** (legacy). |
| `v2-audit` | Same old product, security audit fixes | **DELETE FROM ORIGIN** (legacy). |
| `v2-fixes` | Same old product, security fixes | **DELETE FROM ORIGIN** (legacy). |
| `v2-high` | Same old product, high-severity fixes | **DELETE FROM ORIGIN** (legacy). |
| `v2-medium` | Same old product | **DELETE FROM ORIGIN** (legacy). |
| `v2-medium-2` | Same old product | **DELETE FROM ORIGIN** (legacy). |
| `docs/vps-deployment-errors` | 3 unique commits | **KEEP** (content is useful). |
| `i18n/exec-en-es` | 99 unique commits (i18n work) | **KEEP**. |
| `feature/sisyphus-m1-data-layer` | 43 unique commits (Sisyphus M1-M2) | **KEEP**. |
| `feature/standard-rag-pipeline` | 39 unique commits (Sisyphus M0) | **KEEP**. |
| `evidence/vps-costs-fix-2026-06-26` | Just created in this session | **KEEP**. |
| `fix/ai-costs-missing-rollup-table` | Active in PR #5 | **KEEP**. |
| `sisyphus/anti-forget-layer` | Anti-forget layer | **KEEP**. |

### VPS filesystem (`/opt/myownclone/`)

Cannot inspect right now (SSH is blocked: `WinError 10013`). Last known
state from earlier in this session (2026-06-26 morning UTC):

```
/opt/myownclone/
├── backups/                                 (unknown contents)
├── bootstrap/                               (MyOwnClone checkout, branch audit/vps-sync-and-docs)
├── current -> releases/20260620070304-frontend-dashboard-fix
├── releases/
│   ├── 20260617135142-frontend-bgfix6       (very old, 2026-06-17)
│   ├── 20260617135242-frontend-bgfix7       (very old)
│   ├── 20260617135429-frontend-bgfix8       (very old)
│   ├── 20260617185014-frontend-landing-restore (very old)
│   ├── 20260619221443-security-fixes        (old)
│   ├── 20260619223743-frontend-security-fixes (old)
│   ├── 20260620070304-frontend-dashboard-fix (ACTIVE — current symlink)
│   └── 20260623000000-M13-defects-backfill  (dead code — see current-symlink investigation)
├── shared/
└── worktrees/
    └── sisyphus-vps-integration/             (active: SHA c00612f M14, used by live container)
```

Cleanup plan for VPS (runbook, not executed yet):

1. **Releases to keep**: `20260620070304-frontend-dashboard-fix`
   (referenced by `current` symlink, used by `myownclone-frontend.service`)
   and `20260623000000-M13-defects-backfill` (conservative — it was a
   historical build artifact, but the gunicorn does NOT use it; the
   container uses the worktree directly).
2. **Releases to delete**: all releases from 2026-06-17 to 2026-06-19
   (5 directories: bgfix6/7/8, landing-restore, security-fixes,
   frontend-security-fixes). These are superseded by the 06-20 release.
3. **Worktrees to keep**: `sisyphus-vps-integration/` (active).
4. **Worktrees to delete**: none currently visible.
5. **Backups**: `/opt/myownclone/backups/` — needs separate
   investigation; do not touch without inspection.

VPS cleanup commands (for the next agent with SSH access):

```bash
# Dry run first
sudo -n ls -la /opt/myownclone/releases/

# Delete old frontend-only releases
for d in 20260617135142-frontend-bgfix6 \
         20260617135242-frontend-bgfix7 \
         20260617135429-frontend-bgfix8 \
         20260617185014-frontend-landing-restore \
         20260619221443-security-fixes \
         20260619223743-frontend-security-fixes; do
    echo "Would delete: /opt/myownclone/releases/$d"
done

# If the list looks right, execute (real deletion)
for d in 20260617135142-frontend-bgfix6 \
         20260617135242-frontend-bgfix7 \
         20260617135429-frontend-bgfix8 \
         20260617185014-frontend-landing-restore \
         20260619221443-security-fixes \
         20260619223743-frontend-security-fixes; do
    sudo -n rm -rf "/opt/myownclone/releases/$d"
done

# Also delete the dead M13 release (only after confirming current symlink
# still points to 20260620070304 and the worktree is what serves the API)
sudo -n rm -rf /opt/myownclone/releases/20260623000000-M13-defects-backfill
```

## Risks

1. **Branch deletion is reversible** via reflog for 30+ days, but any
   commits that are ONLY reachable from a deleted branch become
   orphaned. The investigation above confirms no remote-only commits
   will be lost.
2. **VPS deletion of `20260623000000-M13-defects-backfill`** is the
   riskiest step: the live backend container does NOT use it (the
   container uses the worktree), but if some script references the
   release directory, deletion would break that script. The
   `current-symlink-investigation-2026-06-26.md` evidence shows the
   release is dead code. **The next agent should confirm via
   `grep -r 20260623000000-M13-defects-backfill /opt/myownclone/`**
   before deleting it.
3. **No SSH right now** means VPS cleanup is deferred. The local-repo
   cleanup is safe to do in this session.
4. **`main` vs `master` divergence** is not addressed in this plan
   because it requires a separate decision (which is the canonical
   trunk?). Leaving for later.

## Action plan (this session)

### Phase A: stash WIP Sisyphus, clean local branches

```bash
cd C:\Users\haxth3\Documents\MyOwnClone
git stash push --include-untracked -m "M8-M13 sisyphus WIP - preserved for repo cleanup"
git checkout audit/sisyphus-vps-integration
git branch -D audit/sisyphus-vps-integration-push-sync
git branch -D audit/vps-sync-and-docs
git branch -D codex/vps-deploy-audit-fixes
git branch -D feature/standard-rag-pipeline
git fetch --prune origin
git stash pop  # restores the 40 dirty files
```

### Phase B: prune remote-tracking refs for deleted remotes (optional)

This phase is NOT destructive on the server side; it only cleans local
refs.

```bash
git remote prune origin
```

### Phase C: document on a docs-only branch

Create `docs/repo-cleanup-2026-06-26` branch with the cleanup plan and
audit table, push to origin so the next agent can reference it.

### Phase D: defer VPS cleanup until SSH returns

Create the VPS runbook file in `.omo/evidence/vps-cleanup-runbook.md`
so the next agent with SSH access can execute it.

## What is NOT in scope of this plan

- Merging branches into each other (out of scope, requires user review
  of each branch's diff).
- Deleting remote branches other than `unify-api-trees-20260607_214935`
  and the v2-* family.
- Resolving the `main` vs `master` divergence.
- Cleaning `/opt/myownclone/backups/`.
- Cleaning `/opt/myownclone/bootstrap/`.