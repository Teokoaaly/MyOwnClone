# Repo / VPS / Study Matrix - 2026-06-26

## Scope

This note reconciles three surfaces:

- local integration branch state
- VPS live/bootstrap state
- external study/document corpus mentioned by the user

It is an audit artifact, not an implementation claim.

## 1) VPS vs repository

### Local repository baseline

- Local branch: `audit/sisyphus-vps-integration`
- Local HEAD: `d189879`
- Remote branch HEAD visible locally: `origin/audit/sisyphus-vps-integration` at `5baa1bc`
- Local worktree is dirty and contains mixed M8-M13 work plus new `.omo/` planning artifacts.

### VPS live release

- `/opt/myownclone/current` is a symlink to:
  - `/opt/myownclone/releases/20260620070304-frontend-dashboard-fix`
- The live release is not a git checkout.
- Frontend service:
  - `myownclone-frontend.service` = `active`
- Backend service:
  - `myownclone-backend.service` does not exist under systemd on this host.
- Docker access from the `myownclone` user is not available:
  - `permission denied while trying to connect to the docker API at unix:///var/run/docker.sock`

### VPS bootstrap checkout

- Bootstrap checkout path:
  - `/opt/myownclone/bootstrap/MyOwnClone`
- Branch:
  - `audit/vps-sync-and-docs`
- SHA:
  - `e9b9d89fa75706cf6818f595a062aaacf48c4575`

### VPS bootstrap drift

Tracked modifications:

- `MyOwnClone/src/i18n/en.json`
- `MyOwnClone/src/i18n/es.json`
- `api/app_factory.py`
- `api/controllers/console/__init__.py`
- `api/controllers/console/myownclone/__init__.py`
- `api/controllers/console/myownclone/analytics.py`
- `api/controllers/console/myownclone/inbox.py`
- `api/controllers/myownclone_public.py`
- `api/core/model_manager.py`
- `api/core/retrieval.py`
- `api/libs/security_checks.py`
- `api/models/__init__.py`

Untracked additions on VPS bootstrap:

- `api/commands/ai_backfill.py`
- `api/commands/crypto.py`
- `api/commands/reindex.py`
- `api/controllers/console/myownclone/ai_models.py`
- `api/controllers/console/myownclone/runtime.py`
- `api/core/ai_audit.py`
- `api/core/embeddings.py`
- `api/core/model_registry.py`
- `api/core/providers/`
- `api/core/retry_client.py`
- `api/core/stt.py`
- `api/core/token_budget.py`
- `api/libs/crypto.py`
- `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py`
- `api/migrations/versions/2026_06_23_0003_cost_daily_rollup.py`
- multiple `api/tests/test_ai_*` and `api/tests/test_*registry*` files
- `ops/backend.env.production`

### Interpretation

- The live release and bootstrap checkout are separated, which is good.
- The bootstrap checkout is already being used as a quasi-development area, which violates the original safety rule.
- The VPS contains a partially ported Sisyphus implementation that is not represented by a clean branch/commit trail on the VPS itself.
- The local branch and the VPS bootstrap are no longer comparable by SHA alone; they must be compared by file surface and milestone intent.

## 2) Study/document corpus

### What was requested

The user reported a pushed corpus with:

- `briefings/`
- `concepts/`
- `entities/`
- `raw/articles/`
- `assets/infographics/`
- `queries/`
- `comparisons/`
- `SCHEMA.md`
- `index.md`

### What is visible after refreshing `origin/main`

After `git fetch origin main`, the corpus is confirmed in `origin/main`
at `8b9d3c1cc7c819831358a3018abd1a28e27a23de`.

Confirmed paths:

- `briefings/` with daily reports from `2026-06-17` through `2026-06-26`
- `concepts/` with 6 concept pages
- `entities/` with 7 entity pages
- `raw/articles/` with 10 OSINT / implementation articles
- `assets/infographics/myownclone-osint-complete-report/`
- `queries/myownclone-blueprint.md`
- `comparisons/`
- `SCHEMA.md`
- `index.md`

Confirmed anchor file:

- `raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md`

### Interpretation

The earlier mismatch was caused by stale local remote state, not by absence of
the documents in GitHub.

The corpus is real and can be used as an input for post-Sisyphus planning, but
it still needs curation before implementation because it mixes:

1. raw competitor OSINT
2. current-state MyOwnClone research
3. implementation proposals
4. wiki taxonomy / provenance rules

### Operational consequence

The OSINT/study corpus **can** now be treated as a verified repo input for
planning from this machine, specifically from `origin/main`.

It should not yet be treated as an implementation spec line-by-line; it needs a
distillation layer first.

## 3) Matrix

| Surface | What exists | What is missing / unclear | Impact |
| --- | --- | --- | --- |
| Local repo | Clean milestone history through M7, plus dirty M8-M13 work and `.omo` plan | M8-M13 not yet reconciled into isolated commits | High |
| VPS live | Running frontend release, not git-backed | Backend service topology and deploy control still opaque from `myownclone` user | High |
| VPS bootstrap | Real branch base `audit/vps-sync-and-docs` with large uncommitted Sisyphus drift | No clean commit trail for what was ported there | High |
| Study corpus | Confirmed in refreshed `origin/main` with wiki + raw OSINT + implementation handoff | Still needs distillation into an implementation-grade backlog | Medium |

## 4) Recommended next actions

1. Reconcile local repo state first:
   - normalize `HANDOFF_LLM.md`
   - normalize `.sisyphus/progress.json`
   - slice M8-M13 into commit-ready milestones
2. Stop treating VPS bootstrap as a development scratch area:
   - keep it for comparison/deploy only
   - port validated commits into a clean integration lane
3. Distill the document corpus:
   - treat `SCHEMA.md` and `index.md` as navigation/provenance rules
   - treat `concepts/`, `entities/`, `comparisons/`, and `queries/` as synthesis
   - treat `raw/articles/` as raw source and proposal material
   - derive a post-Sisyphus implementation backlog from the verified parts only

## 5) Bottom line

The main risk is not lack of code. The main risk is state drift:

- repo drift vs tracker
- VPS drift vs branch history
- study corpus vs implementation-ready backlog

Until those three are aligned, any new implementation wave risks compounding hidden divergence.
