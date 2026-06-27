# Pre-Deploy Audit Errors Found - 2026-06-27

User requested: "revisa que todo vaya segun lo planeado y no cometas
errores" before proceeding to writing-plans.

Audit performed on the spec at
`docs/superpowers/specs/2026-06-27-maintenance-mode-and-wip-deploy-design.md`
against actual repo state. **Three errors found.**

## Error 1: WIP cherry-pick has real conflicts (BLOCKING)

The spec states "Apply WIP Sisyphus (commit 67262b6)" without noting
that the WIP was committed BEFORE PR #5 (`f427c53`) was merged. Both
the WIP and PR #5 modify the same 4 files, causing add/add conflicts.

Test executed:

```bash
$ git checkout -b test-wip-apply audit/sisyphus-vps-integration
$ git cherry-pick 67262b6
Auto-merging api/tests/test_ai_models_endpoints.py
CONFLICT (add/add): Merge conflict in api/tests/test_ai_models_endpoints.py
error: could not apply 67262b6...

$ git status
UU MyOwnClone/src/app/api/stt/route.ts
UU MyOwnClone/src/components/admin/useAdminFetch.ts
AA api/controllers/console/myownclone/ai_models.py
AA api/tests/test_ai_models_endpoints.py
```

Affected files:
- `MyOwnClone/src/app/api/stt/route.ts`
- `MyOwnClone/src/components/admin/useAdminFetch.ts`
- `api/controllers/console/myownclone/ai_models.py`
- `api/tests/test_ai_models_endpoints.py`

The first two files (`stt/route.ts` and `useAdminFetch.ts`) have
"unmerged" status, meaning text conflicts that must be resolved
manually. The last two (`ai_models.py` and test file) have add/add
status, meaning both branches added the file at different commits
and git needs help deciding which version (or a merge) to keep.

The spec listed these as "no conflict" but reality shows real
conflicts. **The spec's "Phase 4: Deploy code" step will fail.**

## Error 2: Spec file count wrong (DOCUMENTATION ERROR)

The spec says "14 files" in the WIP. Reality:
- Diff shows 15 files in the WIP vs `audit/sisyphus-vps-integration`.
- The spec itself (`docs/superpowers/specs/2026-06-27-maintenance-mode-and-wip-deploy-design.md`)
  appears in the diff with -295 deletions — meaning the WIP commit
  was created AFTER this spec was committed locally, so cherry-picking
  it will delete the spec from the deploy branch.
- The WIP commit ALSO includes some Hermes plan files that are
  unrelated to the actual fix.

The actual content of the WIP (commit message) said "47 files",
which is the count of dirty files at the time of preservation. The
14-file count in the spec was a manual miscount.

## Error 3: SSH to VPS is BLOCKED (BLOCKING)

Phase 2-8 of the spec all require SSH access to the VPS
(`100.125.128.116`). Since the local Windows sandbox started blocking
SSH connections in the previous session (Tailscale auth required),
the deploy phases cannot be executed from this environment.

```bash
$ ssh -o ConnectTimeout=10 myownclone@100.125.128.116 "echo OK"
Command timed out after 5m
```

Earlier in this session the user authorized Tailscale auth and SSH
worked briefly. The connection has since been blocked again by the
local sandbox.

## Root cause of all errors

The spec was written based on assumptions that did not account for:

1. The WIP commit was made BEFORE PR #5 was merged, so the WIP and
   PR #5 share modified files.
2. The user's intent was to "aplicar todo en VPS y Codigo", which
   requires SSH access that is currently unavailable.
3. The WIP commit was created hastily to preserve work, and contains
   some files that should not be in the production code path (e.g.,
   `.hermes/plans/`).

## Options for the user

For Error 1 (conflicts), three approaches:

**A) Manual merge resolution**
After the cherry-pick fails with conflicts, manually merge each of
the 4 files, then `git cherry-pick --continue`. Pros: clean history.
Cons: time-consuming, requires understanding the diff between the
WIP and PR #5 versions of each file.

**B) Squash the WIP into a single new commit**
Create a new commit on the deploy branch that has the final desired
state of each file (manually composed from WIP + integration HEAD).
Pros: simple, no conflicts. Cons: loses granular history of which
change came from which commit.

**C) Three-way merge with explicit resolution**
Use `git merge -X theirs` or `git merge -X ours` and let git pick
one side. Pros: fast. Cons: likely loses code (not recommended for
production code).

For Error 3 (SSH block), two options:

**A) Wait for sandbox to release**
Re-authorize Tailscale again from the user's browser.

**B) Defer the deploy**
Write the code, commit it, document the deploy runbook, and wait
for a future session with working SSH.

## Recommendation

**Defer the entire deploy until SSH is restored** (Error 3 is the
hard blocker). In the meantime:

1. Resolve the WIP conflicts manually on a `deploy/maint-mode-plus-wip`
   branch (option A above) — this CAN be done without SSH.
2. Add the maintenance mode code on the same branch.
3. Run unit tests locally to validate the merged code.
4. Push the deploy branch.
5. Document the deploy runbook in `.omo/evidence/` for the next
   session with SSH access.
6. Defer phases 2-8 (VPS work) until the user can re-authorize
   Tailscale SSH.

This keeps the work moving forward without making changes that
might lock us into a broken state on the VPS.

## Decision needed

User must decide:

1. Conflict resolution approach (A, B, or C).
2. Whether to proceed with code work now (option above) or wait for
   SSH to be restored.