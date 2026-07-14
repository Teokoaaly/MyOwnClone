# Todo 1 evidence: integration recovery baseline

Date: 2026-07-14 (Europe/Madrid)

Result: PASS for the revised Todo 1 scope. Frontend changes and frontend gates
are prohibited and excluded. This branch is not deployable and no later Todo
is claimed.

## Isolation and provenance

- Worktree: `C:\Users\haxth3\Documents\MyOwnClone-integration-v1`
- Branch: `codex/integration-recovery-v1`
- Required starting commit:
  `f0b14181498d0fa986cd28333348afed8baff087`
- Starting tree: `7d1b00ba60c77f118ee7fe0d5dda6bda6548a6cb`
- Live/default comparison:
  `b1b3fa06fd73431e61dafe1d08a45acd07d64da6`
- VPS-fixes comparison:
  `686774cbbc688a67f7d4b17825265c26e322fcbe`
- Nested snapshot `686774cbbc.../`: excluded.
- Wholesale unrelated-history merges: none.
- VPS access or mutation: none.

The main checkout remained on `master` at
`4b3acfefc4feffbc6080195e6b81c4bb708b74ed`. Its before/after
`git status --short` was identical:

```text
?? .mimocode/
?? .omo/
?? 686774cbbc688a67f7d4b17825265c26e322fcbe/
?? PLAN_MAESTRO_AUDITORIA_2026-07-13.md
?? api/tests/test_p1_platform_guard.py
?? context.md
?? myclone_OSINT/
```

## RED baseline

Marker line counts before the revised restoration boundary:

| Scope | Marker lines |
| --- | ---: |
| `api/` | 0 |
| `MyOwnClone/` | 113 |
| `ops/` | 1 |
| `tests/` | 0 |
| `api/tests/` | 0 |

The backend/ops marker gate failed before restoration because `ops/` contained
one hit. Frontend markers were inventoried but are outside the permitted edit
and verification boundary. Python was not itself broken in this rescue tree:

- `python -m compileall -q api`: exit 0.
- `python -m pytest --collect-only -q`: exit 0, 110 tests collected.

The reproducible in-scope corruption failure was the shell source marker. No
graph-only implementation was used.

## Restoration receipt

`MyOwnClone/` is byte-identical to the rescue parent and has no final branch
diff. `ops/backup_postgres.sh` received one token-level repair from clean blob
`4fa419adf9d47deb9493b63fb471f1b661c675d0` at
`991a8b284995b9f45f92c3d69049b03f9b009294`; the only replacement was
`***REMOVED***` to `set -euo pipefail`.

In-scope minimal-diff gate:

```text
REMOVED_LINES=1
REMOVED_MARKER_LINES=1
ADDED_LINES=1
ADDED_MARKER_LINES=0
exit=0
```

The removed ops line contained the corruption marker and the added line does
not. No frontend line is part of the final diff.

Documentation was separate: 165 marker lines remain outside product scopes.
They occur in historical plans, audit/evidence documents, HTML manuals and
`TASKS.md`; they were not changed.

## Verification

| Gate | Command/surface | Raw result |
| --- | --- | --- |
| Backend/ops marker gate | tracked files under `api ops tests api/tests`, binary-capable `Select-String -SimpleMatch` | PASS, 0 hits, exit 0 |
| Frontend exclusion gate | `git diff f0b1418..HEAD -- MyOwnClone` | PASS, empty, exit 0 |
| Marker failure fixture | temporary file containing one marker | PASS, 1 hit, expected exit 7 |
| Minimal restoration | parse in-scope `git diff --unified=0` | PASS, 1/1 removed line marked; 0 added marked; exit 0 |
| Whitespace/error diff | `git diff --check` | PASS, exit 0 |
| Python syntax/import collection | `python -m compileall -q api` | PASS, exit 0 |
| Pytest discovery | `python -m pytest --collect-only -q` | PASS, 110 collected, exit 0 |
| Frontend dependency/typecheck/build | prohibited by revised user boundary | N/A; not part of final verification |
| Manifest tamper check | SHA-256 original versus modified temporary copy | PASS, mismatch rejected, exit 0 |

Manifest SHA-256 before this evidence/commit step:
`736EC49DF81F11B53A3C96C3D1FA81C3FC1A8EA8E1FEDCA68AE103F5260B9C57`.

## Adversarial classes

| Class | Verdict | Evidence |
| --- | --- | --- |
| `stale_state` | PASS | live `ls-remote` compared with cached refs; required master/vps-fixes match; stale deploy head and absent rebase cache recorded and unused |
| `dirty_worktree` | PASS | main checkout branch, SHA and short status are byte-for-byte equivalent before/after |
| `misleading_success_output` | PASS | raw exit codes recorded; marker fixture deliberately exits 7; npm was not called successful |
| `long/hung commands` | PASS | no in-scope backend/ops verification hung |
| `generated artifacts` | PASS | manifest tamper mismatch rejected; temporary fixture/copy, partial node_modules and 25 compile cache directories removed |
| Credential/secret rotation | N/A | Todo 2 and VPS mutation explicitly out of scope |
| Database migration behavior | N/A | Todo 4; no DB or migration changes were made |
| Browser/UI behavior | N/A | frontend explicitly prohibited; graphical work is deferred |
| Network/API failure modes | N/A | no runtime network behavior changed |

## Cleanup receipt

- Temporary marker fixture: removed.
- Temporary tampered manifest copy: removed.
- A partial `MyOwnClone/node_modules` created by a superseded pre-constraint
  attempt was removed; no frontend artifact remains.
- Generated `__pycache__` directories: removed.
- Remaining node/python/docker processes tied to this worktree: none observed.
- Containers started: none.
- VPS sessions opened: none.

## Known risks and gates retained

- The 59 origin-only paths are inventoried in
  `docs/recovery/integration-baseline-manifest.md` and deliberately deferred to
  Todo 3 for path-by-path disposition and tests.
- Alembic remains broken/multi-head and is outside Todo 1.
- Frontend source and verification are intentionally excluded by the latest
  user constraint; the 113 existing frontend markers remain in the rescue tree.
- This commit establishes a source baseline only. It must not be deployed.
