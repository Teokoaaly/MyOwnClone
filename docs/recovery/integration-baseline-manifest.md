# Integration recovery baseline manifest

Cut-off: 2026-07-14 (Europe/Madrid)

This manifest freezes the source inputs used for Todo 1. It is evidence for a
recovery branch, not a release manifest and not proof that the 59 origin-only
paths are safe to import.

## Selected baseline

| Role | Ref at cut-off | Commit | Tree |
| --- | --- | --- | --- |
| Rescue lineage | `fix/p1-backend-robustez-infra` | `f0b14181498d0fa986cd28333348afed8baff087` | `7d1b00ba60c77f118ee7fe0d5dda6bda6548a6cb` |
| Default remote comparison | live `origin/master` | `b1b3fa06fd73431e61dafe1d08a45acd07d64da6` | `9a346ba03ea3cd6dcf244a1a613a51276a5c345a` |
| VPS-fixes comparison | live `origin/vps-fixes` / local `vps-fixes` | `686774cbbc688a67f7d4b17825265c26e322fcbe` | `719196b64d87d2a5b227c4a231b19b4d7495fe08` |

The integration worktree was created directly from the rescue commit at
`C:\Users\haxth3\Documents\MyOwnClone-integration-v1` on
`codex/integration-recovery-v1`. No unrelated-history merge was performed.
The rescue lineage was selected because it contains release, P0 and P1 changes;
it remains non-deployable until later Todos repair migrations, CI and contracts.

## Ref freshness

`git ls-remote --heads origin` was executed immediately before creating the
worktree. Live heads at the cut-off were:

| Remote head | Live commit |
| --- | --- |
| `audit/sisyphus-vps-integration` | `1fe0ae38b378827080715be02eeb77dae09bfd4c` |
| `audit/vps-sync-and-docs` | `e9b9d89fa75706cf6818f595a062aaacf48c4575` |
| `codex/backend-admin-vps-exec` | `f0418c04cfac21a9a3881459ba2172cc94af6e6d` |
| `codex/vps-deploy-audit-fixes` | `ecc8d9296f191957f3af698d0911fb3f1117e49f` |
| `deploy/maint-mode-plus-wip` | `24e966ac836943b7bd27d483a7a63a41dfebd89c` |
| `docs/planes-maestros` | `e7ad09640210b528413381bd9f9c675e4db9e23c` |
| `docs/vps-deployment-errors` | `bc2f4408e3a1eab78af39db281f55e4cbe5469b4` |
| `evidence/vps-costs-fix-2026-06-26` | `25cd134c4aac072ac3ccbb3a319c9e146b63ef3c` |
| `feature/sisyphus-m1-data-layer` | `afed3331d00498cea5ae4904df5a6ef463abdf4d` |
| `feature/standard-rag-pipeline` | `d783cb960f5a28feb84e827763a7db113a582c3a7c` |
| `fix/ai-costs-missing-rollup-table` | `ac5906fe3b28feb84e827763a7db113a582c3a7c` |
| `i18n/exec-en-es` | `bb143802d93e523f862615f96d8ed7ecdf4d2453` |
| `master` | `b1b3fa06fd73431e61dafe1d08a45acd07d64da6` |
| `rebase/sisyphus-vps` | `dc84fc697cb58c34c7f775f176cf37e5c278de18` |
| `release/sisyphus-incompatible-2026-07-07` | `a85a02fe53eaa3dc94d016f0c2eeba7a61a14229` |
| `sisyphus/anti-forget-layer` | `17e552af22117e12b65b5d1887094b946467bc0c` |
| `vps-fixes` | `686774cbbc688a67f7d4b17825265c26e322fcbe` |
| `wip/sisyphus-m8-m13-preservation` | `67262b6935623654ade53eaa558c8b6515ae4a37` |

The cached `origin/master` and `vps-fixes` objects matched their live heads.
The cached `deploy/maint-mode-plus-wip` was stale and
`rebase/sisyphus-vps` was absent from local tracking refs. Neither was used as
source input.

## Repository topology and exclusions

The repository has four disconnected roots:

- `03891c1c2aeef516a69c0ad94726a7ada194e51c`
- `c057864648d3487ed6f15a225d479acdbc58b333`
- `54e36db73fb94e7fc59f6d984c97b790c3770382`
- `a55884cab286b98e84c05879529e0be2c6fed32a`

The nested worktree/snapshot
`C:\Users\haxth3\Documents\MyOwnClone-admin-vps-exec\686774cbbc688a67f7d4b17825265c26e322fcbe\`
and all paths below it were excluded from discovery, restoration, tests and
graph use. The graph index was not trusted because it mixes that snapshot with
the root checkout. Reindexing must target this isolated checkout and its final
commit only.

## Allowed corruption restoration

Baseline marker counts were `api=0`, `MyOwnClone=113`, `ops=1`,
`tests=0`, and `api/tests=0`. A later user constraint excludes all frontend
changes, so `MyOwnClone/` remains byte-identical to the selected rescue commit.
Its 113 markers are recorded as known frontend debt, not repaired or claimed by
this Todo.

`ops/backup_postgres.sh` does not exist in either pinned comparison tree. Its
single marker replaced `set -euo pipefail`, proven by the clean blob
`4fa419adf9d47deb9493b63fb471f1b661c675d0` at commit
`991a8b284995b9f45f92c3d69049b03f9b009294`. The exact diff is one removed
marker line and one added shell-safety line. No other content from that
unrelated historical commit was imported.

Backend/test scopes contain zero markers and the allowed ops scope contains
zero after restoration. Documentation contains 165 markers outside those
scopes. They are retained because changing historical evidence is outside
scope.

## Origin-only 59-path reconciliation inventory

These paths exist in pinned `origin/master` and are absent in the rescue tree.
Todo 1 freezes the complete inventory. Their disposition is
`DEFERRED_TO_TODO_3`: no path is silently imported, removed, or represented as
validated in this baseline.

1. `MyOwnClone/e2e/security/csrf.spec.ts`
2. `MyOwnClone/e2e/security/idor.spec.ts`
3. `MyOwnClone/e2e/security/rate-limit.spec.ts`
4. `MyOwnClone/e2e/security/xss.spec.ts`
5. `MyOwnClone/src/components/admin/AdminCharts.tsx`
6. `MyOwnClone/src/components/ui/LandingBehavior.tsx`
7. `MyOwnClone/src/components/ui/PublicPricing.tsx`
8. `MyOwnClone/src/hooks/useCloneId.ts`
9. `MyOwnClone/src/lib/csrf.ts`
10. `MyOwnClone/src/lib/public-pricing.ts`
11. `MyOwnClone/src/lib/rate-limit.ts`
12. `MyOwnClone/src/types/drizzle-orm.d.ts`
13. `MyOwnClone/src/types/security.ts`
14. `api/api/tests/test_models_smoke.py`
15. `api/commands/ai_backfill_from_env.py`
16. `api/commands/generate_master_key.py`
17. `api/commands/rotate_secrets_key.py`
18. `api/controllers/console/myownclone/admin_ia_models.py`
19. `api/core/cost_recording.py`
20. `api/core/feedback_collector.py`
21. `api/core/ingestion_pipeline.py`
22. `api/core/metrics_collector.py`
23. `api/core/moderation.py`
24. `api/core/myownclone/retrieval.py`
25. `api/core/providers/anthropic_adapter.py`
26. `api/core/providers/cloudflare_adapter.py`
27. `api/core/providers/cohere_adapter.py`
28. `api/core/providers/ollama_adapter.py`
29. `api/core/providers/openai_adapter.py`
30. `api/core/reranking.py`
31. `api/core/smart_router.py`
32. `api/migrations/versions/2026_06_15_0001_add_fk_constraints.py`
33. `api/migrations/versions/2026_06_15_0001_add_frequent_query_indices.py`
34. `api/migrations/versions/2026_06_15_1340-c3d4e6f7a8b9_fix_plan_pricing.py`
35. `api/migrations/versions/2026_06_21_0001_ai_models_catalog.py`
36. `api/migrations/versions/2026_06_21_0002_embedding_outbox.py`
37. `api/migrations/versions/2026_06_21_0003_ai_invocations.py`
38. `api/migrations/versions/2026_06_21_0004_response_feedback.py`
39. `api/models/ai_invocation.py`
40. `api/models/embedding_outbox.py`
41. `api/models/moderation_log.py`
42. `api/models/response_feedback.py`
43. `api/models/routing_log.py`
44. `api/tests/security/__init__.py`
45. `api/tests/security/conftest.py`
46. `api/tests/security/payloads.py`
47. `api/tests/security/test_admin_invitation_flow.py`
48. `api/tests/security/test_deploy_rce.py`
49. `api/tests/security/test_prompt_injection.py`
50. `api/tests/security/test_rate_limit_fail_closed.py`
51. `api/tests/security/test_xff_validation.py`
52. `api/tests/test_embedding_service.py`
53. `api/tests/test_ingestion_pipeline.py`
54. `api/tests/test_metrics_collector.py`
55. `api/tests/test_model_manager.py`
56. `docs/ROLLBACK_PROCEDURES.md`
57. `ops/test_docker_security.sh`
58. `ops/test_infra_security.sh`
59. `tests/security/helpers.ts`

## Boundary

No frontend file, VPS command, credential read, deployment, migration repair,
CI redesign, contract change, or graphical redesign is part of the final tree.
The branch is an integration recovery baseline, not a production candidate.
