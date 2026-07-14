# SOL-02 — reconciliación backend/ops

Fecha: 2026-07-14. Worktree: `codex/integration-recovery-v1`.

## Entradas fijadas

- Rescate: `f0b14181498d0fa986cd28333348afed8baff087`.
- `origin/master`: `b1b3fa06fd73431e61dafe1d08a45acd07d64da6`.
- HEAD inicial: `cb684c6bb623452db8b4c1dd6d382e37c4bc8758`.
- CodeGraph se descartó porque el índice mezcla un snapshot anidado; se usaron árboles Git fijados.

## Caracterización previa

- `python -m compileall -q api`: PASS.
- `pytest --collect-only -q`: 110 pruebas.
- Alembic: 3 heads y padre ausente `2026_07_09_0001`; migraciones diferidas.
- CI no tenía secret scanning.
- `ops/deploy-backend.sh` estaba colapsado en una línea y no era ejecutable.

## Matriz completa de 59 rutas origin-only

Resumen: excluded-frontend=13, deferred-security-test=1, retain-current=42, port-origin=3.

| Ruta | Decisión | Evidencia/racional |
| --- | --- | --- |
| `MyOwnClone/e2e/security/csrf.spec.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/e2e/security/idor.spec.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/e2e/security/rate-limit.spec.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/e2e/security/xss.spec.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/components/admin/AdminCharts.tsx` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/components/ui/LandingBehavior.tsx` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/components/ui/PublicPricing.tsx` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/hooks/useCloneId.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/lib/csrf.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/lib/public-pricing.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/lib/rate-limit.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/types/drizzle-orm.d.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `MyOwnClone/src/types/security.ts` | excluded-frontend | Frontend congelado por instrucción explícita; no se importa ni ejecuta. |
| `api/api/tests/test_models_smoke.py` | retain-current | Prueba ligada al stack AI alternativo de origin; se conserva como evidencia hasta reconciliar su contrato. |
| `api/commands/ai_backfill_from_env.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/commands/generate_master_key.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/commands/rotate_secrets_key.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/controllers/console/myownclone/admin_ia_models.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/cost_recording.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/feedback_collector.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/ingestion_pipeline.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/metrics_collector.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/moderation.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/myownclone/retrieval.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/providers/anthropic_adapter.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/providers/cloudflare_adapter.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/providers/cohere_adapter.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/providers/ollama_adapter.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/providers/openai_adapter.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/reranking.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/core/smart_router.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/migrations/versions/2026_06_15_0001_add_fk_constraints.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_15_0001_add_frequent_query_indices.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_15_1340-c3d4e6f7a8b9_fix_plan_pricing.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_21_0001_ai_models_catalog.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_21_0002_embedding_outbox.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_21_0003_ai_invocations.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/migrations/versions/2026_06_21_0004_response_feedback.py` | retain-current | Diferido a LUNA-01: los grafos origen y rescate tienen revisiones incompatibles y múltiples heads. |
| `api/models/ai_invocation.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/models/embedding_outbox.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/models/moderation_log.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/models/response_feedback.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/models/routing_log.py` | retain-current | Implementación AI paralela/duplicada; importarla a ciegas crearía dos fuentes de verdad. |
| `api/tests/security/__init__.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/conftest.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/payloads.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/test_admin_invitation_flow.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/test_deploy_rce.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/test_prompt_injection.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/test_rate_limit_fail_closed.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/security/test_xff_validation.py` | retain-current | Evidencia para SOL-03; depende de rutas y contratos todavía no reconciliados. |
| `api/tests/test_embedding_service.py` | retain-current | Prueba ligada al stack AI alternativo de origin; se conserva como evidencia hasta reconciliar su contrato. |
| `api/tests/test_ingestion_pipeline.py` | retain-current | Prueba ligada al stack AI alternativo de origin; se conserva como evidencia hasta reconciliar su contrato. |
| `api/tests/test_metrics_collector.py` | retain-current | Prueba ligada al stack AI alternativo de origin; se conserva como evidencia hasta reconciliar su contrato. |
| `api/tests/test_model_manager.py` | retain-current | Prueba ligada al stack AI alternativo de origin; se conserva como evidencia hasta reconciliar su contrato. |
| `docs/ROLLBACK_PROCEDURES.md` | port-origin | Artefacto autónomo de recuperación o seguridad copiado desde el SHA fijado. |
| `ops/test_docker_security.sh` | port-origin | Artefacto autónomo de recuperación o seguridad copiado desde el SHA fijado. |
| `ops/test_infra_security.sh` | port-origin | Artefacto autónomo de recuperación o seguridad copiado desde el SHA fijado. |
| `tests/security/helpers.ts` | deferred-security-test | Helper de pruebas de seguridad diferido; no es código frontend de producto y requiere su suite contractual. |

## Cambios

- Port de los tres artefactos `port-origin`.
- Restauración del script backend desde el árbol limpio fijado.
- Recuperación de TruffleHog en CI, sin tocar jobs frontend.
- Manifiesto determinista SHA-256 para `api/`, `ops/` y workflows.
- Pruebas de árbol limpio, mutación, manifiesto malformado y traversal.

## Límites

- Cero cambios bajo `MyOwnClone/`.
- Cero acceso al VPS.
- Migraciones y contratos quedan para LUNA-01; seguridad de identidad para SOL-03.

## Verificación final

- Commits: `d85fcdd` (manifiesto), `61f7bc2` (ops/seguridad), `84bc74c` (finales de archivo).
- `python -m pytest -q --tb=short`: 114 passed, 2 warnings.
- `python -m compileall -q api ops/release_manifest.py`: PASS.
- `bash -n` en los tres scripts reconciliados: PASS.
- Parseo YAML de CI: PASS.
- Marcadores de conflicto en backend/ops/tests/workflows: 0.
- Escaneo binario de claves: solo el placeholder documentado de `api/.env.example`; ningún secreto real se imprimió.
- Manifiesto CLI sobre árbol limpio: PASS (201 archivos).
- Copia temporal mutada en `api/app_factory.py`: FAIL esperado por digest; temporal eliminado.
- `git diff f0b1418..HEAD -- MyOwnClone`: vacío.

## Corrección tras verificación independiente

- `7224de7`: valida SHA/digests hexadecimales minúsculos y rechaza rutas extra no manifestadas.
- `996ef75`: pasa rollback por argumentos posicionales citados, integra manifiesto local/remoto y añade gate CI.
- Harness Bash con rutas que contienen espacios y `;`: PASS sin SSH/VPS.
- Suite final: 121 passed, 2 warnings preexistentes.
- Manifiesto limpio: PASS; archivo extra: exit 1; archivo mutado: exit 1; SHA `z...`: exit 2.
- Limpieza temporal con `.git/objects` read-only en Windows: `cleanup=True`.
- Clasificación corregida: 13 rutas `MyOwnClone` excluidas y `tests/security/helpers.ts` diferida como security-test.
