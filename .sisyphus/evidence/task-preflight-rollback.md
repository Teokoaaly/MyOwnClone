# Preflight rollback

## Context
- Date: 2026-06-23
- Branch: `audit/sisyphus-vps-integration`
- Production compatibility base: `origin/audit/vps-sync-and-docs` at `e9b9d89`
- Integration branch prepared outside the live checkout:
  `/opt/myownclone/worktrees/sisyphus-vps-integration`
- Live VPS checkout remains untouched on `audit/vps-sync-and-docs` with local
  i18n changes preserved in `src/i18n/en.json` and `src/i18n/es.json`

## Changes

- Audited the VPS state before any deploy-path change:
  - active release symlink under `/opt/myownclone/current`
  - live checkout branch `audit/vps-sync-and-docs`
  - healthy API/frontend services
- Integrated `M1` and `M2` into the integration branch/worktree so the new
  branch now contains the Sisyphus baseline without modifying the live release.
- Hardened `ops/deploy-backend.sh`:
  - capture the previous release symlink before switching `current`
  - add an `EXIT` trap that restores the previous release if build/health fails
  - remove `eval`-based compose execution in favor of argv-safe arrays
  - record deploy metadata in `${REMOTE_RELEASE_DIR}/.deploy-backend-meta`
- Hardened `ops/deploy-frontend.sh`:
  - capture the previous release before activation
  - add rollback trap that restores the prior symlink and restarts systemd
  - record deploy metadata in `${REMOTE_RELEASE_DIR}/.deploy-frontend-meta`

## Verification

- `git diff --check`: passed; only CRLF conversion warnings from the local
  Windows checkout
- shell syntax check:
  - `bash -n ops/deploy-backend.sh`
  - `bash -n ops/deploy-frontend.sh`
- rollback dry verification:
  - backend: inspect that `PREVIOUS_RELEASE="$(readlink -f "${REMOTE_CURRENT_LINK}" ...)"`
    is captured before `ln -sfn "${REMOTE_RELEASE_DIR}" "${REMOTE_CURRENT_LINK}"`
    and restored inside `rollback()`
  - frontend: same ordering and restore path, plus service restart during rollback
- VPS inspection:
  - live branch untouched
  - integration worktree isolated

## Open risks

- Rollback logic is script-level verified first; it still needs one controlled
  deploy rehearsal before production use.
- Backend rollback currently rebuilds from the restored release. That is safe
  for compatibility, but slower than a pure container restart.
- `progress.json` intentionally does not mark a new milestone ***REMOVED*** because this
  is preflight infrastructure, not M3+ feature delivery.

## Remote SHA

- Branch remote before this preflight patch: `0432796cb7239903106060461ddc3ea88d0bedd4`
