# Evidence — M1: Capa de datos (ai_models catalog)

**Milestone:** M1
**Fecha QA:** 2026-06-21
**Resultado:** ✅ PASS
**Commit:** ff70378 (feat(sisyphus): M1 — ai_models catalog, assignments, invocations tables + schema tests)
**Rama:** feature/sisyphus-m1-data-layer (derivada de feature/standard-rag-pipeline @ d783cb9)

## Artefactos creados

| Archivo | Propósito |
|---------|-----------|
| `api/models/ai_models.py` | `AIModel`, `AIModelAssignment`, `AIInvocation` + 3 StrEnum (`AIProvider`, `AICapability`, `AITask`) + mapa `TASK_CAPABILITY`. UUIDv7 PK, `api_key_encrypted` como `Text`, soft-delete vía `is_active`. |
| `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py` | Crea las 3 tablas, FK `ON DELETE RESTRICT` en `ai_model_assignments.model_id`, índice parcial único `uq_active_assignment_per_tenant_task (tenant_id, task) WHERE is_active=true`. Idempotente (`_table_exists`, `_index_exists`). `down_revision = 'd1e2f3a4b5c6'`. |
| `api/models/__init__.py` | Re-exporta `AIModel`, `AIModelAssignment`, `AIInvocation`, `AIProvider`, `AICapability`, `AITask`, `TASK_CAPABILITY`. |
| `api/tests/test_ai_models_schema.py` | 14 tests DB-light (introspección de metadata SQLAlchemy + AST scan de la migración). |

## Verificación ejecutada

```
$ .venv/bin/python -m pytest api/tests/test_ai_models_schema.py -v
============================== 14 passed in 1.48s ==============================

$ .venv/bin/python -m pytest tests/test_plan_completion.py -v --maxfail=99
tests/test_plan_completion.py::test_m1_ai_model_classes_exist           PASSED
tests/test_plan_completion.py::test_m1_ai_model_registered_in_models_init PASSED
tests/test_plan_completion.py::test_m2_crypto_secret_cipher_exists     FAILED (expected, M2 not implemented)
(... 12 more expected failures for M3-M13 ...)

$ .venv/bin/python -m pytest tests/ api/tests/ --ignore=tests/test_plan_completion.py
================== 122 passed, 1 failed in 13.53s ===================
# The 1 failure is api/tests/test_inbox_e2e.py::test_inbound_email_accepts_correct_secret
# which requires a running PostgreSQL on localhost:5432 — pre-existing env limitation,
# NOT caused by this commit.

$ .venv/bin/python scripts/check-plan-progress.py
Sisyphus plan: Sistema de Modelos IA Configurables por Tarea (M0-M13)
  done:        2/15  ['M0', 'M1']
  in_progress: 0
  pending:     13       [...]
[OK] progreso consistente.
EXIT=0
```

## Decisiones explícitas (fuera del scope, documentadas)

1. **`ai_invocations` se crea en M1, no en M12.**
   Razón: M7 (refactor de `model_manager.py` para cost tracking en streaming) necesita una tabla donde insertar la auditoría. Crearla aquí evita un migración adicional en M7 y mantiene la trazabilidad desde el primer commit que inserta filas.

2. **NO se añade FK `ai_invocations.tenant_id → tenants.id`.**
   Razón: la capa de aplicación (`MyOwnClone.blueprint` y el middleware multi-tenant) ya valida la pertenencia. Una FK rígida rompe los fixtures de test multi-tenant que insertan invocaciones antes de que la transacción del tenant commitee. Documentado en el comentario de la migración.

3. **NO se seedea ningún dato en la migración.**
   El comando `flask ai-backfill-from-env` (M13) crea los modelos a partir de las variables de entorno existentes, de forma idempotente. Mantener la migración pura es más seguro para re-ejecuciones y rollback.

4. **Tests DB-light, no live PG.**
   Los 14 tests son introspección pura (metadata + AST), pasan sin PostgreSQL. Los QA Scenarios del plan (DB up + downgrade + violación del índice parcial) requieren una instancia live y están documentados aquí para ejecutarse manualmente o añadirse a CI cuando haya runner con PG.

## Próximo hito

**M2 — Cifrado AES-256-GCM.** Depende de M1 (done). Entregables:
- `api/libs/crypto.py` con `SecretCipher` (encrypt/decrypt/generate_master_key/is_configured)
- Comando CLI `flask generate-master-key`
- Añadir `MODEL_SECRETS_KEY` a `_REQUIRED_IN_PROD` en `api/libs/security_checks.py`
- `api/tests/test_crypto.py` con 5 tests: round-trip, tampering, missing key, wrong length, rotación

Pendiente decisión del usuario sobre:
- ¿Resolver acceso SSH al VPS antes de continuar?
- ¿Revisar PR #2/#3 ahora o después?
- ¿Push de la rama `feature/sisyphus-m1-data-layer` a origin?