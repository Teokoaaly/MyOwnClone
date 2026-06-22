# Plan base: Sistema de Modelos IA Configurables por Tarea

This file is the compact planning source for the resumable Sisyphus execution.
`TASKS.md` is the operational checklist. `.sisyphus/progress.json` is the
canonical milestone state.

## Goal

Replace env-var-driven provider selection with a DB-driven model catalog that
assigns a configurable AI model per task:

- `chat`
- `embedding`
- `email_classification`
- `email_draft`
- `stt`

The system must support hot-swap, encrypted provider keys, provider failover,
cost tracking, admin APIs, admin UI, backfill from legacy env vars, and a safe
VPS deployment path.

## Rules

- Live VPS production base remains `origin/audit/vps-sync-and-docs`.
- Integration work happens in `audit/sisyphus-vps-integration`.
- One task = one commit = one push.
- Do not deploy until rollback scripts are corrected and verified.
- Do not touch the live VPS i18n working tree changes.
- Use `origin/master` only as a selective code source, not as a direct merge
  target for production integration.

## Milestones

- `M4a`: ProviderAdapter base and ProviderRegistry
- `M3`: ModelRegistry with cache, invalidation, and fallback
- `M4b`: six concrete providers
- `M5`: RetryClient
- `M6`: TokenBudgeter
- `M7`: ModelManager task-based runtime and streaming cost tracking
- `M8`: Embeddings registry refactor
- `M9`: Admin AI model REST API
- `M10`: Runtime integrations
- `M11`: Admin UI `/admin/ia-modelos`
- `M12`: Audit, daily cost rollup, key rotation
- `M13`: Defects, backfill, final docs, final verification

## Definition of done

- Every milestone has evidence under `.sisyphus/evidence/`
- `.sisyphus/progress.json` reflects the real state
- Relevant tests pass for the milestone
- Remote SHA is recorded in the evidence file
- Work is resumable without reading the entire chat history
