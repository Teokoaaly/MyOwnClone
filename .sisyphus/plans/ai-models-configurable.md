# Plan: Sistema de Modelos IA Configurables por Tarea (13 fases)

## TL;DR

> **Quick Summary**: Reemplazar la selección fija de LLM por env vars (`_detect_provider()`) con un sistema basado en BD que asigna un modelo distinto a cada una de las 5 tareas (chat, embeddings, clasificación email, borradores email, STT), con hot-swap, multi-key por proveedor, keys cifradas AES-256-GCM, cost tracking real (incluso en streaming) y panel admin completo con playground y gráfico de costos.
>
> **Deliverables**:
> - Catálogo `ai_models` + asignaciones `ai_model_assignments` + auditoría `ai_invocations` + rollup `cost_daily_rollup`
> - `SecretCipher` AES-256-GCM + `flask generate-master-key` / `flask rotate-secrets-key`
> - `ModelRegistry` con cache TTL 60s + invalidación
> - 6 `ProviderAdapter` (OpenAI, Anthropic, MiniMax, Together, OpenAI-compatible, Local) + `ProviderRegistry`
> - `RetryClient` con backoff + failover + circuit breaker
> - `TokenBudgeter` con gpt-tokenizer + dimension guard
> - Refactor `model_manager.py` y `embeddings.py` para usar registry
> - 6 endpoints admin REST + playground
> - Integración en 5 puntos (chat_public, ingestion, classification, draft, STT)
> - UI `/admin/ia-modelos` con 4 componentes + recharts
> - Comando `flask ai-backfill-from-env` (idempotente)
> - Tests incrementales por fase
>
> **Estimated Effort**: Large (13 fases, 25-30 archivos, ~2 migraciones)
> **Parallel Execution**: YES - 5 olas con hasta 7 tareas paralelas
> **Critical Path**: M1 (tablas) → M2 (crypto) → M4a (adapter interface) → M3 (registry) → M4b (adapters) → M5 (retry) → M6 (budget) → M7 (model_manager refactor) → M8 (embeddings refactor) → M9 (API) → M10 (integración) → M11 (UI) → M12 (auditoría+rollup) → M13 (defectos+backfill+tests)

---

## Context

### Original Request
PLAN_MAESTRO.md (versión final del usuario) — 13 fases M1→M13 para implementar sistema de modelos IA configurables por tarea. El usuario subió el plan consolidado y pidió: "Acción inmediata al aprobar: crear PLAN_MAESTRO.md en la raíz del repo con este contenido íntegro (13 fases en orden secuencial M1→M13), luego continuar implementación desde M1."

### Interview Summary
**Key Discussions**:
- Plan final consolidado en 13 fases (M1 a M13). Numeración definitiva según el usuario.
- Cada fase tiene entregables, dependencias y criterios de aceptación definidos.
- M1 crea `ai_models` + `ai_model_assignments` (en el plan original la auditoría `ai_invocations` está en M12, pero Metis recomienda moverla a M7 para verificar el streaming cost tracking).
- M3 (registry) depende de M4a (interface del adapter) — el orden estricto del usuario M1→M13 se mantiene como "orden del plan", pero la ejecución interna reordena: M1→M2→M4a→M3→M4b→M5→M6→M7→M8→M9→M10→M11→M12→M13.
- Tests incrementales por fase (Metis), no todos en M13.
- Backfill es comando separado (ya estaba así).
- UI en M11 solo después de M9 API estable.

**Research Findings** (validado contra código real):
- `api/core/model_manager.py:608` ya tiene `_dispatch` y `_dispatch_stream` separados. Defecto #2 (streaming cost perdido) es real; defecto #3 (literal "clone_response" línea 206) es real.
- `api/core/embeddings.py:305` ya tiene batching con `_OPENAI_BATCH_SIZE=512`. Defecto #4 está en el endpoint público `/api/embed` (probablemente `myownclone_public.py`) que no hace chunking antes de llamar `embed_texts`.
- `api/models/analytics.py`: `CostCategory` ya es StrEnum con `CLONE_RESPONSE`, `CONTENT_INGESTION`, `PLATFORM_OPS`. NO requiere migración.
- `api/libs/security_checks.py`: hay que añadir `MODEL_SECRETS_KEY` a `_REQUIRED_IN_PROD` y `_INSECURE_DEFAULTS`.
- `api/libs/uuid_utils.py` ya tiene `uuidv7()` — REUTILIZAR.
- Migración más reciente: `2026_06_21_0001_align_with_drizzle.py`. Nueva: `2026_06_21_0002_ai_models_catalog.py`.
- 73 tests pytest existentes.
- Frontend STT: `MyOwnClone/src/app/api/stt/route.ts` tiene `OPENAI_API_KEY` directa — REESCRIBIR como proxy a Flask.

### Metis Review
**Identified Gaps** (addressed in plan):
- **Phase ordering**: M4 (ProviderAdapter interface) debe existir antes de M3 (ModelRegistry) porque registry dispatch necesita interface estable. Mover M4a (interface) antes de M3, M4b (implementaciones) después.
- **`ai_invocations` placement**: tabla necesaria en M7 para verificar streaming cost tracking fix. Incluir en migración M1.
- **Test strategy**: incremental per phase, no deferred to M13.
- **Multi-tenant isolation**: tests específicos para "tenant A no ve asignaciones de B".
- **Hot-swap semantics**: solo nuevas requests, in-flight usan asignación al inicio.
- **Fallback chain**: DB down → cache 60s → legacy env vars → error.
- **DB connection loss mid-stream**: stream continúa con cache; cost INSERT falla gracefully.
- **Key rotation mid-request**: streams in-flight terminan con key original.
- **Provider returns 0 usage in stream**: log error + INSERT con cost_cents=0 + flag.
- **Master key loss**: documentar en MANUAL_TECNICO que las keys son irrecuperables sin master.
- **Circuit breaker half-open**: tras 30s abierto, siguiente request prueba; éxito cierra, fallo re-abre.
- **Embedding dim contract**: rechazar != 1536 con HTTP 422, no silenciosamente.

---

## Work Objectives

### Core Objective
Sustituir la selección fija de LLM por env-var priority con un sistema DB-driven que permita asignar un modelo distinto a cada una de las 5 tareas (chat, embeddings, email_classification, email_draft, stt), con hot-swap, multi-key por proveedor, keys cifradas AES-256-GCM, cost tracking real (incluso en streaming), panel admin con playground y gráfico de costos.

### Concrete Deliverables
- **Backend (13 archivos nuevos)**:
  - `api/models/ai_models.py` (AIModel, AIModelAssignment, AIProvider, AICapability, AITask, TASK_CAPABILITY)
  - `api/libs/crypto.py` (SecretCipher)
  - `api/core/model_registry.py` (ModelRegistry con cache)
  - `api/core/providers/base.py` + 6 adapters (`openai`, `anthropic`, `minimax`, `together`, `openai_compatible`, `local`)
  - `api/core/retry_client.py` (backoff + circuit breaker)
  - `api/core/token_budget.py` (truncado + dimension guard)
  - `api/controllers/console/myownclone/ai_models.py` (6 endpoints REST)
  - `api/controllers/console/myownclone/internal_stt.py` (endpoint STT backend)
- **Backend (refactor)**: `api/core/model_manager.py`, `api/core/embeddings.py`
- **Migraciones (1)**: `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py`
- **Frontend (4 componentes)**: `MyOwnClone/src/app/admin/ia-modelos/page.tsx`, `AIModelForm.tsx`, `TaskAssignmentCard.tsx`, `Playground.tsx`, `CostChart.tsx`
- **Frontend (refactor)**: `MyOwnClone/src/app/api/stt/route.ts` (proxy)
- **Comandos CLI (3)**: `flask generate-master-key`, `flask ai-backfill-from-env`, `flask rotate-secrets-key`
- **Tests (~6 archivos)**: test_crypto, test_model_registry, test_provider_adapters, test_retry_client, test_token_budget, test_ai_models_endpoints, test_integration
- **Docs**: sección "Migración al sistema de modelos" en `MANUAL_TECNICO.md`

### Definition of Done
- [ ] `pytest -v` pasa los 73 tests existentes + nuevos tests de cada fase
- [ ] `flask db upgrade` aplica la migración sin errores
- [ ] `flask ai-backfill-from-env` importa env vars como modelos en BD (idempotente)
- [ ] `GET /console/api/myownclone/ai/assignments` devuelve 5 asignaciones activas
- [ ] `POST /console/api/myownclone/ai/playground` ejecuta prompt y devuelve tokens + costo
- [ ] Cambiar asignación vía API afecta la siguiente request (no in-flight)
- [ ] Cost tracking en streaming persiste usage en `cost_tracking` y `ai_invocations`
- [ ] `npm run typecheck` y `npm run lint` pasan en frontend
- [ ] No hay keys en texto plano en BD (verificación SQL)

### Must Have
- Sistema de modelos DB-driven con 5 tareas independientes
- Cifrado AES-256-GCM de api_key con master key en env
- Multi-key por proveedor
- Hot-swap sin reiniciar
- Cost tracking en streaming
- Panel admin con CRUD + playground + cost chart
- 6 defectos corregidos
- Backfill idempotente
- Tests incrementales

### Must NOT Have (Guardrails)
- NO añadir providers fuera de los 6 listados (openai/anthropic/minimax/together/openai_compatible/local)
- NO cambiar cipher format tras M2 (compromete datos en BD)
- NO acceder a `ai_models` sin pasar por `ModelRegistry` tras M3
- NO usar strings literales para provider names; usar enum `AIProvider`
- NO añadir cost categories sin extender el enum `CostCategory` primero
- NO usar `os.environ` para API keys en código nuevo; pasar por `SecretCipher` + BD
- NO incluir reranking con cross-encoder, routing inteligente auto, TTS/moderation tasks
- NO modificar migraciones existentes; solo añadir nuevas
- NO usar `any`/`@ts-ignore` ni `as any` (debe pasar typecheck estricto)
- NO acceptance criteria que requieran "user manually confirms"

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** - TODA la verificación es agent-executed. Cada fase tiene QA Scenarios ejecutables.

### Test Decision
- **Infrastructure exists**: YES (pytest + 73 tests)
- **Automated tests**: YES (incremental per phase)
- **Framework**: pytest (backend), Vitest ya existe (frontend — no se añaden tests nuevos, QA con Playwright)
- **Per-phase TDD**: cada fase M1-M13 incluye tests antes de la siguiente.

### QA Policy
Cada TODO incluye QA Scenarios agent-executed. Evidence guardado en `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Backend/API**: `Bash` con `pytest` y `curl` al endpoint
- **DB migrations**: `Bash` con `flask db upgrade` y queries SQL
- **CLI commands**: `Bash` con `flask <command>`
- **Frontend UI**: `playwright` (skill del ejecutor)
- **Crypto**: tests pytest puros con vectores conocidos
- **Streaming**: tests con mocks de OpenAI/Anthropic que simulan chunks

---

## Execution Strategy

### Parallel Execution Waves

> Las 13 fases se ejecutan en olas según dependencias. M4 dividido en M4a (interface) + M4b (adapters) para evitar bloqueo de M3. Tests incrementales por fase.

```
Wave 1 (Foundation - secuencial, rápida):
├── Task 1: Commit PLAN_MAESTRO.md a la raíz
└── Task 2: M1 — Crear ai_models.py + migración con seed

Wave 2 (Cifrado + Adapter Interface - paralelo):
├── Task 3: M2 — SecretCipher + assert_production_secrets + generate-master-key
└── Task 4: M4a — ProviderAdapter base + ProviderRegistry (interface only)

Wave 3 (Registry + Adapter implementations - paralelo):
├── Task 5: M3 — ModelRegistry (usa interface de M4a)
└── Task 6: M4b — 6 adapters concretos (openai/anthropic/minimax/together/openai_compatible/local)

Wave 4 (Robustez - paralelo):
├── Task 7: M5 — RetryClient (backoff + failover + circuit breaker)
└── Task 8: M6 — TokenBudgeter (gpt-tokenizer + dimension guard)

Wave 5 (Refactor core - secuencial por dependencia):
├── Task 9: M7 — Refactor model_manager.py (usa M3, M4b, M5, M6)
└── Task 10: M8 — Refactor embeddings.py (usa M3, M4b)

Wave 6 (API admin - paralelo):
├── Task 11: M9 — 6 endpoints REST + blueprint
└── Task 12: M13 partial — Defecto #2 (streaming cost) + #3 (enum) verificados vía tests de M7

Wave 7 (Integración 5 puntos - paralelo):
├── Task 13: M10a — chat_public → registry
├── Task 14: M10b — ingestion + embeddings → registry
├── Task 15: M10c — _classify_and_draft → registry (classification + draft)
└── Task 16: M10d — STT: reescribir route.ts como proxy + endpoint Flask

Wave 8 (UI admin - secuencial post-API):
├── Task 17: M11a — Página /admin/ia-modelos (server component)
├── Task 18: M11b — AIModelForm + TaskAssignmentCard (client components)
└── Task 19: M11c — Playground + CostChart (con recharts)

Wave 9 (Auditoría + rollup + rotación - paralelo):
├── Task 20: M12a — Tabla ai_invocations (si no se creó en M1, mover aquí)
├── Task 21: M12b — Vista materializada cost_daily_rollup + trigger + cron
└── Task 22: M12c — flask rotate-secrets-key

Wave 10 (Final wave - fixes, backfill, tests integración, docs):
├── Task 23: M13a — Defectos #4 (batching) + #6 (threshold log)
├── Task 24: M13b — flask ai-backfill-from-env + tests
├── Task 25: M13c — Docs MANUAL_TECNICO.md (sección migración)
└── Task 26: Final Verification — 4 reviews paralelos

Critical Path: Task 2 (M1) → Task 3 (M2) → Task 4 (M4a) → Task 5 (M3) → Task 6 (M4b) → Task 9 (M7) → Task 11 (M9) → Task 13 (M10a chat) → Task 17 (M11a) → Task 26 (Final)
Parallel Speedup: ~65% vs secuencial puro
Max Concurrent: 4 (Wave 7)
```

### Dependency Matrix
- **1**: - → 2
- **2**: 1 → 3, 4
- **3**: 2 → 5
- **4**: 2 → 5
- **5**: 3, 4 → 6, 9
- **6**: 4 → 7
- **7**: 6 → 9
- **8**: - → 9
- **9**: 5, 7, 8 → 11
- **10**: 9 → 13, 14, 15, 16
- **11-12**: 9, 10 → 13
- **13-15**: 10 → 17
- **16**: 10 → 17
- **17**: 13, 14, 15, 16 → 18
- **18**: 17 → 19
- **19**: 18 → 26
- **20-22**: 11, 12 → 26
- **23-25**: 11, 12, 20, 21, 22 → 26
- **26**: ALL → user

### Agent Dispatch Summary
- **Wave 1-2 (3 tasks)**: `quick` para commit y modelos; `deep` para crypto y adapter interface
- **Wave 3-4 (4 tasks)**: `deep` para registry y adapters; `unspecified-high` para retry y budget
- **Wave 5-6 (3 tasks)**: `unspecified-high` para refactors; `quick` para endpoints REST
- **Wave 7 (4 tasks)**: `quick` para integraciones; `unspecified-high` para STT cross-stack
- **Wave 8 (3 tasks)**: `visual-engineering` para UI; `quick` para componentes
- **Wave 9 (3 tasks)**: `unspecified-high` para auditoria/rollup; `quick` para CLI
- **Wave 10 (4 tasks)**: `quick` para fixes; `deep` para backfill y tests integración; `writing` para docs; `oracle/unspecified-high/deep` para final review

---

## TODOs

> Implementation + Test = ONE Task. Never separate.
> **EVERY task MUST have: Recommended Agent Profile + Parallelization info + QA Scenarios.**
> **A task WITHOUT QA Scenarios is INCOMPLETE. No exceptions.**

- [ ] 1. **Commit PLAN_MAESTRO.md a la raíz del repo**

  **What to do**:
  - Crear `PLAN_MAESTRO.md` en `C:\Users\haxth3\Documents\MyOwnClone-vps-fixes\PLAN_MAESTRO.md` con el contenido íntegro que el usuario subió (13 fases M1→M13).
  - Commit con mensaje `docs: add PLAN_MAESTRO.md for configurable AI models system (13 phases)`.
  - Branch actual: `feature/standard-rag-pipeline` (NO crear rama nueva).

  **Must NOT do**:
  - NO añadir nada de contenido al archivo (es referencia, no documentación a expandir).
  - NO crear rama nueva.
  - NO tocar otros archivos en este commit.

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single file commit, contenido predefinido por el usuario.
  - **Skills**: `["git-master"]`
    - `git-master`: Para commit atómico y formato de mensaje conventional.
  - **Skills Evaluated but Omitted**:
    - `frontend-ui-ux`: No aplica (es un .md).

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Task 2)
  - **Blocks**: Nada (es commit inicial de docs).
  - **Blocked By**: None.

  **References**:
  - **External**: Contenido íntegro del usuario en la conversación — copiar literalmente.

  **Acceptance Criteria**:
  - [ ] Archivo `PLAN_MAESTRO.md` existe en la raíz del repo
  - [ ] `git log -1` muestra el commit con el mensaje correcto
  - [ ] `git diff HEAD~1 -- PLAN_MAESTRO.md` muestra las 13 fases M1–M13
  - [ ] Working tree limpio: `git status` sin cambios sin commit

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: PLAN_MAESTRO.md committed correctly
    Tool: Bash
    Preconditions: Branch `feature/standard-rag-pipeline` activo
    Steps:
      1. Test-Path -LiteralPath "PLAN_MAESTRO.md" -PathType Leaf
      2. git log --oneline -3
      3. git show HEAD --stat
    Expected Result: 
      1. True
      2. Última línea contiene "PLAN_MAESTRO.md for configurable AI models system"
      3. Solo PLAN_MAESTRO.md modificado, 1 archivo
    Evidence: .sisyphus/evidence/task-1-plan-committed.txt

  Scenario: Working tree clean
    Tool: Bash
    Steps:
      1. git status
    Expected Result: "nothing to commit, working tree clean" (o solo los cambios no relacionados previos que existían).
    Evidence: .sisyphus/evidence/task-1-clean-tree.txt
  ```

  **Commit**: YES
  - Message: `docs: add PLAN_MAESTRO.md for configurable AI models system (13 phases)`
  - Files: `PLAN_MAESTRO.md`
  - Pre-commit: `git diff --check`

---

- [ ] 2. **M1 — Capa de datos: catálogo y asignaciones (más ai_invocations)**

  **What to do**:
  - Crear `api/models/ai_models.py` con:
    - Enums: `AIProvider` (openai/anthropic/minimax/together/openai_compatible/local), `AICapability` (llm/embedding/stt/tts/reranking), `AITask` (chat/embedding/email_classification/email_draft/stt).
    - `TASK_CAPABILITY` dict mapeando task → capability requerida.
    - Modelo `AIModel`: id (UUIDv7), tenant_id (nullable String(36)), name, provider (String(20) — guard enum), model_id, api_key_encrypted (Text), base_url (nullable), capabilities (JSON array), priority (int default 100), temperature_default (Float nullable), max_tokens_default (Int nullable), max_input_tokens (Int nullable), embedding_dimensions (Int nullable), is_active (Boolean default true), timestamps (created_at, updated_at).
    - Modelo `AIModelAssignment`: id (UUIDv7), tenant_id (nullable), task (String(30) — guard enum), model_id (FK a ai_models.id con ON DELETE RESTRICT), override_params (JSON nullable), is_active (Boolean default true), timestamps.
    - Modelo `AIInvocation` (M7 lo necesita, mejor aquí): id (UUIDv7), tenant_id (String(36)), clone_id (String(36) nullable), task (String(30)), model (String(100)), prompt_hash (String(64)), prompt_tokens (Int), completion_tokens (Int), latency_ms (Int), success (Boolean), error_message (Text nullable), created_at.
  - Crear migración `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py`:
    - Upgrade: CREATE TABLE ai_models + ai_model_assignments + ai_invocations + índices.
    - Índices: `(tenant_id, task, is_active)`, `(tenant_id, provider)`, `(tenant_id, task) WHERE is_active=true` (partial unique), `(created_at)` en ai_invocations.
    - Foreign keys: `ai_model_assignments.model_id REFERENCES ai_models.id ON DELETE RESTRICT`, `ai_invocations.tenant_id REFERENCES tenants.id` (verificar nombre real de tabla tenants en `api/models/account.py`).
    - **NO seed en migración** (eso va en M13 backfill command).
  - Registrar modelos en `api/models/__init__.py` (verificar patrón existente).
  - Crear test `api/tests/test_ai_models_schema.py` que valide:
    - Crear AIModel con cada provider enum.
    - Crear AIModelAssignment con cada task.
    - Insertar 2 AIModelAssignment activos con mismo (tenant, task) debe fallar por partial unique index.
    - Borrar AIModel con assignments debe fallar por FK RESTRICT.

  **Must NOT do**:
  - NO seed de datos en la migración (eso es comando aparte).
  - NO crear trigger en esta fase (trigger de rollup va en M12).
  - NO usar SQLAlchemy `relationship()` complejo; mantener simple (FK explícito + columna `model_id`).
  - NO incluir lógica de cifrado en este task (eso es M2).

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Modelado de datos cuidadoso con constraints específicos (partial unique index, FK, ON DELETE behavior) y migración Alembic.
  - **Skills**: `[]`
    - Sin skills especiales necesarias; lógica SQLAlchemy + Alembic estándar.

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (con Task 1)
  - **Blocks**: Task 3, 4, 5, 9, 11, 20 (todos dependen de que las tablas existan)
  - **Blocked By**: Task 1

  **References** (CRITICAL):
  - **Pattern References**:
    - `api/models/analytics.py:1-50` — Patrón de modelo SQLAlchemy con UUIDv7, mixin `DefaultFieldsDCMixin`, `naive_utc_now`, `func.current_timestamp()`.
    - `api/migrations/versions/2026_06_21_0001_align_with_drizzle.py` — Patrón de migración Alembic reciente.
    - `api/models/account.py:1-30` — Para ver cómo se modela tenant_id (probable FK a tenants).
    - `api/libs/uuid_utils.py` — `uuidv7()` función para default.
    - `api/libs/datetime_utils.py` — `naive_utc_now()` función para timestamps.
  - **API/Type References**:
    - SQLAlchemy `JSON` type para `capabilities` y `override_params`.
    - `String(N)` con longitud generosa (50-100 chars).
  - **Test References**:
    - `api/tests/test_rag_pipeline.py` — Patrón de tests pytest con DB.
    - `api/tests/conftest.py` — Fixtures disponibles (db session, app context).

  **Acceptance Criteria**:
  - [ ] `api/models/ai_models.py` existe con los 3 modelos (AIModel, AIModelAssignment, AIInvocation) y los 3 enums
  - [ ] `api/models/__init__.py` importa los nuevos modelos (verificar patrón)
  - [ ] `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py` existe
  - [ ] `flask --app app_factory db upgrade` aplica la migración sin error
  - [ ] `flask --app app_factory db downgrade -1` revierte sin error
  - [ ] `pytest -v api/tests/test_ai_models_schema.py` → PASS
  - [ ] Los 73 tests existentes siguen pasando: `pytest -v` → PASS

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Migration creates all tables
    Tool: Bash
    Preconditions: DB PostgreSQL corriendo, alembic configurado
    Steps:
      1. cd api && flask --app app_factory db upgrade
      2. psql $DATABASE_URL -c "\dt" | grep -E "ai_models|ai_model_assignments|ai_invocations"
      3. psql $DATABASE_URL -c "\d ai_models" | head -40
    Expected Result: 
      1. Exit 0, "Applying 2026_06_21_0002_ai_models_catalog"
      2. 3 tablas listadas
      3. Columnas id, tenant_id, name, provider, model_id, api_key_encrypted, base_url, capabilities, priority, etc.
    Evidence: .sisyphus/evidence/task-2-migration-up.txt

  Scenario: Partial unique index works
    Tool: Bash
    Preconditions: Migración aplicada
    Steps:
      1. psql $DATABASE_URL -c "INSERT INTO ai_models (id, name, provider, model_id, capabilities, is_active) VALUES (gen_random_uuid()::text, 'Test', 'openai', 'gpt-4o-mini', '[\"llm\"]', true);"
      2. psql $DATABASE_URL -c "INSERT INTO ai_model_assignments (id, tenant_id, task, model_id, is_active) SELECT gen_random_uuid()::text, 't1', 'chat', id, true FROM ai_models WHERE name='Test' LIMIT 1;"
      3. psql $DATABASE_URL -c "INSERT INTO ai_model_assignments (id, tenant_id, task, model_id, is_active) SELECT gen_random_uuid()::text, 't1', 'chat', id, true FROM ai_models WHERE name='Test' LIMIT 1;"
    Expected Result:
      1. INSERT 0 1
      2. INSERT 0 1
      3. ERROR: duplicate key value violates unique constraint "uq_active_assignment_per_tenant_task"
    Evidence: .sisyphus/evidence/task-2-unique-index.txt

  Scenario: Schema tests pass
    Tool: Bash
    Steps:
      1. cd api && pytest -v api/tests/test_ai_models_schema.py
    Expected Result: PASS, 4+ tests passed
    Evidence: .sisyphus/evidence/task-2-schema-tests.txt

  Scenario: Downgrade reverses cleanly
    Tool: Bash
    Steps:
      1. cd api && flask --app app_factory db downgrade -1
      2. psql $DATABASE_URL -c "\dt" | grep -E "ai_models"
    Expected Result: 1. Exit 0. 2. No ai_models listed (reverted).
    Evidence: .sisyphus/evidence/task-2-downgrade.txt
  ```

  **Commit**: YES
  - Message: `feat(db): M1 — ai_models catalog, assignments, and invocations tables`
  - Files: `api/models/ai_models.py`, `api/models/__init__.py`, `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py`, `api/tests/test_ai_models_schema.py`
  - Pre-commit: `pytest -v api/tests/test_ai_models_schema.py`

---

- [ ] 3. **M2 — Cifrado AES-GCM (SecretCipher + generate-master-key)**

  **What to do**:
  - Crear `api/libs/crypto.py` con:
    - Clase `SecretCipher` con métodos estáticos `encrypt(plaintext: str) -> str` y `decrypt(blob: str) -> str`.
    - Usa `cryptography.hazmat.primitives.ciphers.aead.AESGCM`.
    - Master key: `os.environ["MODEL_SECRETS_KEY"]` debe ser base64 de 32 bytes. Validar longitud; raise `ValueError` con mensaje claro si no.
    - Genera nonce aleatorio de 12 bytes por encrypt.
    - Formato: `base64(nonce || ciphertext || tag)` (12 + N + 16 bytes → base64).
    - `generate_master_key()` retorna string base64 de 32 bytes random (para uso en CLI).
    - `is_configured()` retorna bool para usar en asserts de producción.
  - Modificar `api/libs/security_checks.py`:
    - Añadir `MODEL_SECRETS_KEY` a `_REQUIRED_IN_PROD`.
    - Añadir check: si hay modelos activos en BD (verificar con query rápida o flag de config), `MODEL_SECRETS_KEY` es obligatorio en prod.
  - Registrar comando CLI en `api/commands/` (verificar patrón en `api/commands/seed.py` y `api/commands/reindex.py`):
    - `flask generate-master-key`: genera key y la imprime (con aviso de guardar en lugar seguro).
  - Crear test `api/tests/test_crypto.py`:
    - Round-trip: encrypt → decrypt == original.
    - Tampering: modificar 1 byte del blob cifrado → decrypt raises `InvalidTag`.
    - Missing key: si `MODEL_SECRETS_KEY` no está, encrypt raises `ValueError`.
    - Wrong length: si `MODEL_SECRETS_KEY` base64 decode no da 32 bytes, raises `ValueError`.
    - Rotación: cifrar con key A, descifrar con key B falla. Re-cifrar con key B, descifrar con key B funciona.

  **Must NOT do**:
  - NO usar Fernet (es AES-CBC, no GCM).
  - NO guardar la key en BD.
  - NO permitir key vacía o None.
  - NO usar `cryptography.fernet` (deprecated pattern).

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Criptografía — errores sutiles comprometen seguridad. Tests de tampering y rotación son críticos.
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (con Task 4)
  - **Blocks**: Task 5 (ModelRegistry usa cipher), Task 9 (API cifra al crear), Task 22 (rotate)
  - **Blocked By**: Task 2 (M1 — necesita `api_models` table para el check condicional en assert_production_secrets)

  **References**:
  - **Pattern References**:
    - `api/libs/security_checks.py:1-65` — Patrón de validación de secrets en producción.
    - `api/commands/seed.py` — Patrón de Flask CLI command (ver cómo se registra con `@app.cli.command()`).
  - **External References**:
    - `cryptography` library docs: `AESGCM.encrypt(nonce, data, associated_data)` y `AESGCM.decrypt(nonce, data, associated_data)`.
    - URL: `https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM`

  **Acceptance Criteria**:
  - [ ] `api/libs/crypto.py` existe con `SecretCipher`, `generate_master_key`, `is_configured`
  - [ ] `MODEL_SECRETS_KEY` está en `_REQUIRED_IN_PROD` de `security_checks.py`
  - [ ] Comando `flask --app app_factory generate-master-key` imprime key base64
  - [ ] `pytest -v api/tests/test_crypto.py` → PASS (5+ tests)
  - [ ] Los 73 tests existentes siguen pasando

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: Round-trip encryption
    Tool: Bash
    Preconditions: $MODEL_SECRETS_KEY seteada en env (32 bytes base64)
    Steps:
      1. cd api && python -c "import os; os.environ['MODEL_SECRETS_KEY']='$(python -c "import secrets, base64; print(base64.b64encode(secrets.token_bytes(32)).decode())")'; from api.libs.crypto import SecretCipher; ct = SecretCipher.encrypt('sk-test123'); print(SecretCipher.decrypt(ct) == 'sk-test123')"
    Expected Result: True
    Evidence: .sisyphus/evidence/task-3-roundtrip.txt

  Scenario: Tampering detected
    Tool: Bash
    Steps:
      1. cd api && python -c "import os, base64; os.environ['MODEL_SECRETS_KEY']=base64.b64encode(b'a'*32).decode(); from api.libs.crypto import SecretCipher; ct = SecretCipher.encrypt('hello'); tampered = ct[:-4] + 'XXXX'; SecretCipher.decrypt(tampered)"
    Expected Result: Raises `cryptography.exceptions.InvalidTag`
    Evidence: .sisyphus/evidence/task-3-tamper.txt

  Scenario: Missing key raises clear error
    Tool: Bash
    Steps:
      1. cd api && python -c "import os; os.environ.pop('MODEL_SECRETS_KEY', None); from api.libs.crypto import SecretCipher; SecretCipher.encrypt('test')"
    Expected Result: Raises `ValueError` con mensaje "MODEL_SECRETS_KEY not configured"
    Evidence: .sisyphus/evidence/task-3-missing-key.txt

  Scenario: CLI command generates valid key
    Tool: Bash
    Steps:
      1. cd api && flask --app app_factory generate-master-key
    Expected Result: Imprime string base64 de ~44 caracteres (= 32 bytes). Exit 0.
    Evidence: .sisyphus/evidence/task-3-generate-key.txt

  Scenario: Production assertion requires MODEL_SECRETS_KEY
    Tool: Bash
    Preconditions: FLASK_ENV=production
    Steps:
      1. cd api && FLASK_ENV=production python -c "import os; os.environ.pop('MODEL_SECRETS_KEY', None); from api.libs.security_checks import assert_production_secrets; assert_production_secrets()"
    Expected Result: SystemExit(1) con mensaje mencionando MODEL_SECRETS_KEY
    Evidence: .sisyphus/evidence/task-3-prod-assert.txt
  ```

  **Commit**: YES
  - Message: `feat(security): M2 — AES-256-GCM SecretCipher + generate-master-key CLI`
  - Files: `api/libs/crypto.py`, `api/libs/security_checks.py`, `api/commands/crypto.py` (o similar), `api/tests/test_crypto.py`
  - Pre-commit: `pytest -v api/tests/test_crypto.py`

---

- [ ] 4. **M4a — ProviderAdapter interface y ProviderRegistry**

  **What to do**:
  - Crear `api/core/providers/__init__.py` (paquete).
  - Crear `api/core/providers/base.py`:
    - `class ProviderAdapter` (ABC) con métodos abstractos:
      - `invoke(prompt: str, params: GenerationParams, model: AIModel) -> ModelReply`
      - `invoke_stream(prompt: str, params: GenerationParams, model: AIModel) -> Generator[str, None, ModelUsage]`
        - Genera strings (chunks de texto) y al final yields `ModelUsage` con `None` o usa un canal separado.
        - Alternativa: el adapter expone `invoke_stream_with_usage(...)` que retorna `tuple[Generator[str], Callable[[], ModelUsage | None]]`.
        - **Decisión técnica**: usar protocolo de "send final usage via exception or final yield". La implementación más limpia es separar en dos generadores: `chunks_gen` y `usage_provider`.
      - `test_connection(model: AIModel) -> TestResult` (latencia + bool éxito).
    - Clase `TestResult` dataclass: `success: bool`, `latency_ms: int`, `error: str | None`.
    - Constante `class AIModelCapabilities` con sets válidos: `LLM_ONLY`, `EMBEDDING_ONLY`, `STT_ONLY`, etc.
  - Crear `api/core/providers/registry.py`:
    - `class ProviderRegistry` con classmethods:
      - `get_adapter(provider: str) -> ProviderAdapter` (instancia singleton por provider).
      - `register(provider: str, adapter: ProviderAdapter)` (decorador o método).
    - Lazy import de adapters concretos (M4b) para evitar circular imports.
  - Mover `GenerationParams` y `ModelReply` desde `api/core/model_manager.py` a `api/core/providers/base.py` (re-export desde model_manager para backward compat).
  - Crear test `api/tests/test_provider_registry.py`:
    - Mock adapter registrado, `get_adapter("mock")` retorna la instancia.
    - `get_adapter("unknown")` raises `ValueError`.
    - ProviderAdapter abstracto no se puede instanciar directamente.

  **Must NOT do**:
  - NO implementar los 6 adapters concretos en este task (eso es M4b).
  - NO cambiar la interfaz de `ModelManager` aún (eso es M7).
  - NO añadir lógica de retry/circuit breaker aquí (eso es M5).

  **Recommended Agent Profile**:
  - **Category**: `deep`
    - Reason: Definir la interfaz que será la base de 6 adapters y de ModelRegistry. Errores aquí se propagan a todo.
  - **Skills**: `[]`

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (con Task 3)
  - **Blocks**: Task 5 (ModelRegistry usa ProviderRegistry), Task 6 (adapters concretos extienden ProviderAdapter)
  - **Blocked By**: Task 2 (M1 — necesita AIModel para tipado)

  **References**:
  - **Pattern References**:
    - `api/core/model_manager.py:88-110` — `ModelReply` y `GenerationParams` actuales (origen a migrar).
    - `api/libs/uuid_utils.py` — Patrón de módulo con funciones puras.
  - **External References**:
    - Python ABC: `from abc import ABC, abstractmethod`.
    - Python Protocol: alternativa más flexible (usar si se prefiere duck typing).

  **Acceptance Criteria**:
  - [ ] `api/core/providers/__init__.py`, `base.py`, `registry.py` existen
  - [ ] `ProviderAdapter` es abstracta; intentar instanciarla raises `TypeError`
  - [ ] `ProviderRegistry.get_adapter` retorna instancia singleton
  - [ ] `ModelReply` y `GenerationParams` re-exportados desde `model_manager` para backward compat
  - [ ] `pytest -v api/tests/test_provider_registry.py` → PASS
  - [ ] Los 73 tests existentes siguen pasando

  **QA Scenarios (MANDATORY)**:
  ```
  Scenario: ProviderAdapter is abstract
    Tool: Bash
    Steps:
      1. cd api && python -c "from api.core.providers.base import ProviderAdapter; ProviderAdapter()"
    Expected Result: Raises `TypeError: Can't instantiate abstract class ProviderAdapter`
    Evidence: .sisyphus/evidence/task-4-abstract.txt

  Scenario: ProviderRegistry returns singleton
    Tool: Bash
    Steps:
      1. cd api && python -c "from api.core.providers.registry import ProviderRegistry; from api.core.providers.base import ProviderAdapter; class Mock(ProviderAdapter): def invoke(self, p, pr, m): pass; def invoke_stream(self, p, pr, m): yield ''; def test_connection(self, m): pass; ProviderRegistry.register('mock', Mock()); a1 = ProviderRegistry.get_adapter('mock'); a2 = ProviderRegistry.get_adapter('mock'); print(a1 is a2)"
    Expected Result: True
    Evidence: .sisyphus/evidence/task-4-singleton.txt

  Scenario: Unknown provider raises
    Tool: Bash
    Steps:
      1. cd api && python -c "from api.core.providers.registry import ProviderRegistry; ProviderRegistry.get_adapter('does_not_exist')"
    Expected Result: Raises `ValueError: Unknown provider 'does_not_exist'`
    Evidence: .sisyphus/evidence/task-4-unknown.txt

  Scenario: Registry tests pass
    Tool: Bash
    Steps:
      1. cd api && pytest -v api/tests/test_provider_registry.py
    Expected Result: PASS
    Evidence: .sisyphus/evidence/task-4-tests.txt
  ```

  **Commit**: YES
  - Message: `feat(providers): M4a — ProviderAdapter interface and ProviderRegistry`
  - Files: `api/core/providers/__init__.py`, `api/core/providers/base.py`, `api/core/providers/registry.py`, `api/core/model_manager.py` (re-exports), `api/tests/test_provider_registry.py`
  - Pre-commit: `pytest -v api/tests/test_provider_registry.py`

---


