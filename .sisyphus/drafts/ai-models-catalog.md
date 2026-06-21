# Draft: PLAN_MAESTRO.md — Sistema de Modelos IA Configurables (13 fases)

## Plan maestro confirmado (versión final del usuario)
13 fases M1–M13 en orden secuencial. Diferencias vs versión anterior:
- **M4 = ProviderAdapter** (antes M10). Renumeradas: M4 adapters, M5 retry, M6 token budget, M7 refactor model_manager, M8 refactor embeddings, M9 API admin, M10 integración, M11 UI, M12 auditoría+rollup+rotación, M13 fixes+backfill+tests.
- M11 UI incluye playground + CostChart con recharts (lee cost_daily_rollup).
- M12 incluye `ai_invocations` + `cost_daily_rollup` + `flask rotate-secrets-key`.
- M13 agrupa los 6 defectos, el backfill y los tests.

## Requirements (confirmados)
### Tablas
- `ai_models`: id (UUIDv7), tenant_id (nullable), name, provider (AIProvider), model_id, api_key_encrypted (TEXT), base_url (nullable), capabilities (array), priority (int), temperature_default, max_tokens_default, max_input_tokens, embedding_dimensions, is_active, timestamps.
- `ai_model_assignments`: id, tenant_id (nullable), task (AITask), model_id FK, override_params JSON, is_active, timestamps. Partial unique index "una activa por (tenant, task)".
- `ai_invocations` (M12): tenant_id, clone_id, task, model, prompt_hash, prompt_tokens, completion_tokens, latency_ms, success, error_message, created_at.
- `cost_daily_rollup` (M12): tenant_id, model, day, tokens_in, tokens_out, cost_cents, calls. Vista materializada refrescada por trigger/cron.

### Enums
- `AIProvider`: openai / anthropic / minimax / together / openai_compatible / local
- `AICapability`: llm / embedding / stt / tts / reranking
- `AITask`: chat / embedding / email_classification / email_draft / stt
- `TASK_CAPABILITY` map: chat→llm, embedding→embedding, email_classification→llm, email_draft→llm, stt→stt

### Componentes backend
- `api/libs/crypto.py`: SecretCipher AES-256-GCM, master key desde `MODEL_SECRETS_KEY` (32 bytes base64).
- `api/core/model_registry.py`: get_model_for_task, list_available, test_model, cache TTL 60s + invalidación.
- `api/core/providers/base.py` + 6 adapters (openai, anthropic, minimax, together, openai_compatible, local).
- `api/core/retry_client.py`: backoff exponencial 3 intentos, failover por priority, circuit breaker 3 fallos/60s → abierto 30s.
- `api/core/token_budget.py`: gpt-tokenizer, truncar RAG, enforce responses_month_limit, guard embedding_dimensions=1536.
- Refactor `model_manager.py`: invoke_for_task(tenant_id, task, prompt, ...), streaming cost tracking con `stream_options={"include_usage": True}`.
- Refactor `embeddings.py`: embed_texts acepta AIModel opcional.

### API admin
- GET/POST `/console/api/myownclone/ai/models`
- GET/PUT/DELETE `/console/api/myownclone/ai/models/<id>` (nunca devuelve key descifrada)
- POST `/console/api/myownclone/ai/models/<id>/test`
- POST `/console/api/myownclone/ai/playground`
- GET `/console/api/myownclone/ai/assignments`
- PUT `/console/api/myownclone/ai/assignments/<task>`
- Validación: capability match task. Auditoría en impersonation_log-style.

### Integración (5 puntos)
- chat_public: `ModelRegistry.get_model_for_task(task=CHAT)`
- ingestion + embeddings: `task=EMBEDDING`
- _classify_and_draft: `task=EMAIL_CLASSIFICATION` y `task=EMAIL_DRAFT`
- STT: `MyOwnClone/src/app/api/stt/route.ts` reescrito como proxy a `/api/myownclone/internal/stt` Flask.

### UI admin
- `/admin/ia-modelos/page.tsx` (server component): tabla modelos + 5 dropdowns asignaciones + playground + cost chart.
- Componentes: AIModelForm.tsx, TaskAssignmentCard.tsx, Playground.tsx, CostChart.tsx (recharts).

### Comandos CLI
- `flask generate-master-key`
- `flask ai-backfill-from-env` (idempotente, cifra keys)
- `flask rotate-secrets-key --new <key>` (re-cifra todas las api_key_encrypted)

## Technical Decisions (definitivas)
- **Master key**: 32 bytes base64 desde `MODEL_SECRETS_KEY`. AES-256-GCM. Nonce 12 bytes.
- **Cipher format**: base64(nonce || ciphertext || tag). 12 + N + 16 bytes.
- **Cache TTL**: 60s, key `(tenant_id, task)` → `AIModel`. Invalidación: `ModelRegistry.invalidate(tenant_id, task=None)` (None = todas las tareas del tenant).
- **Streaming cost**: pasar `stream_options={"include_usage": True}` a OpenAI; Anthropic reporta en `message_delta` final; MiniMax via `usage` field. Acumular en `ModelUsage` y hacer INSERT al cerrar el stream.
- **Pricing**: extender `api/core/pricing.py` con lookup por `(provider, model_id)`. Modelo sin precio → log warning + cost_cents=0 (no rompe el chat).
- **Migration**: `2026_06_21_0002_ai_models_catalog.py`. Partial unique index: `CREATE UNIQUE INDEX uq_active_assignment_per_tenant_task ON ai_model_assignments(tenant_id, task) WHERE is_active = true`.
- **Frontend STT**: reescribir `route.ts` como proxy mínimo que hace `fetch` al endpoint Flask. Conserva la API pública del cliente (multipart audio).
- **M12 rollup**: trigger AFTER INSERT en `cost_tracking` + cron diario (defensa en profundidad). Refresco concurrente (no lockean lecturas).
- **Audit log**: usar tabla `impersonation_log` style (no crear tabla nueva, extender uso o crear `admin_audit_log` si ya existe).
- **Test infrastructure**: pytest existe. 73 tests actuales. Comando canónico: `pytest -v`. Frontend usa Vitest pero el plan no pide tests frontend nuevos.
- **Idempotencia backfill**: si ya hay asignaciones activas para una tarea, no las toca. Solo crea modelos faltantes desde env vars.
- **Soft-delete**: DELETE → `is_active=false`. Si hay asignaciones activas apuntando al modelo, se desactivan también (cascada lógica).
- **Embedding dim guard**: validación al crear/editar AIModel con capability embedding. Si `embedding_dimensions != 1536` y la BD tiene `chunks.embedding vector(1536)`, rechazar.

## Codebase state (validado)
- `api/core/model_manager.py:608 líneas`: tiene `_dispatch` y `_dispatch_stream`. Bug #2 (streaming cost) real; bug #3 (literal "clone_response" línea 206) real.
- `api/core/embeddings.py:305 líneas`: tiene batching `_OPENAI_BATCH_SIZE=512`. Defecto #4: el endpoint público `/api/embed` (en `myownclone_public.py`) probablemente no hace chunking antes de llamar `embed_texts`. Fix: añadir wrapper que trocea en chunks de 512.
- `api/core/retrieval.py`: threshold 0.25 silencioso (defecto #6).
- `api/models/analytics.py`: `CostCategory` ya es StrEnum. NO requiere migración.
- `api/libs/security_checks.py`: ampliar con `MODEL_SECRETS_KEY`.
- Migraciones: última `2026_06_21_0001_align_with_drizzle.py`.
- `api/libs/uuid_utils.py` ya tiene `uuidv7()` — REUTILIZAR.
- Tests: 73 tests pytest existentes.
- Frontend STT: `MyOwnClone/src/app/api/stt/route.ts` con `OPENAI_API_KEY` directa — REESCRIBIR como proxy.

## Defaults to apply (sin preguntar al usuario)
- UUID v7 (ya disponible).
- Cache TTL: 60s.
- Backoff base: 1s, max 3 retries, delays 1-2-4s.
- Circuit breaker: 3 fallos en 60s → abierto 30s.
- Max batch OpenAI: 512 (preservar constante actual).
- Default embedding dimensions: 1536 (preservar contrato con `chunks.embedding vector(1536)`).
- Migration timestamp: `2026_06_21_0002_ai_models_catalog.py`.

## Scope Boundaries
### INCLUDE
- 13 fases completas (M1–M13)
- Tests para todas las capas nuevas
- Docs en MANUAL_TECNICO.md (sección "Migración al sistema de modelos")
- Commit inicial: crear PLAN_MAESTRO.md en la raíz

### EXCLUDE (siguiente ciclo)
- Reranking con cross-encoder (Cohere rerank)
- Routing inteligente automático por costo/latencia
- Proveedores no OpenAI-compatible nativos fuera de los listados
- TTS y moderation tasks (enums reservados, sin implementación)
- Tests Vitest para componentes UI (QA con Playwright del agente)

## Metis Review (Gaps Found — Addressed)
### Critical Adjustments
1. **M4 antes de M3**: dividir M4 en M4a (interface) + M4b (implementaciones). M3 importa de M4a. Esto rompe la numeración secuencial estricta del usuario — la ejecución interna es M1→M2→M4a→M3→M4b→M5→M6→M7→M8→M9→M10→M11→M12→M13.
2. **`ai_invocations` se crea en M7**, NO en M12. M7 necesita la tabla para verificar que el streaming cost tracking funciona. Se incluye en la migración M1.
3. **Tests incrementales por fase**: cada fase M1-M13 incluye sus tests antes de la siguiente. M13 NO es el lugar de escribir tests.
4. **Backfill es comando separado** (`flask ai-backfill-from-env --dry-run` / ejecutar), NO parte de la migración. Ya está así.
5. **M11 UI solo después de M9 API estable** + tests pasando.

### New edge cases a cubrir en los TODOs
- **Multi-tenant isolation**: tenant A no ve asignaciones de tenant B. Constraint SQL + test de aislamiento.
- **Hot-swap semantics**: cambio de asignación afecta solo NUEVAS requests, no in-flight. Documentar en M3.
- **Fallback chain explícito**: si DB inalcanzable → usar cache (60s TTL) → si no, legacy env vars → si no, error claro.
- **DB connection loss mid-stream**: stream continúa con la asignación cacheada al inicio; INSERT de cost puede fallar gracefully.
- **Embedding dim contract**: rechazar `!= 1536` con error claro. NO rechazar silenciosamente. `text-embedding-3-small` por defecto 1536.
- **Key rotation mid-request**: streams in-flight terminan con la key original. Nueva asignación usa nueva key.
- **Provider returns 0 usage in stream**: log error + INSERT con cost_cents=0 + flag para investigación. NO silenciar.
- **Master key loss recovery**: documentar en MANUAL_TECNICO que si se pierde, todas las api_key_encrypted son irrecuperables. Backfill desde env vars es la única salida.
- **Circuit breaker half-open**: tras 30s abierto, siguiente request prueba. Si éxito → cerrado. Si fallo → abierto otros 30s.

### Guardrails Must NOT
- NO añadir providers fuera de los 6 sin nueva fase.
- NO cambiar cipher format tras M2 (compromete datos en BD).
- NO acceder a `ai_models` sin pasar por ModelRegistry tras M3.
- NO usar strings literales para provider names; usar enum AIProvider.
- NO añadir cost categories sin extender el enum primero.
- NO usar `os.environ` para API keys en código nuevo; pasar por SecretCipher + BD.

### Preguntas que debería haber hecho (ahora documentadas en plan como defaults)
- Q1: Multi-tenant model isolation → Default: cada tenant ve solo sus modelos + globales (tenant_id=NULL).
- Q2: Multi-key strategy → Default: por-request random entre keys activas del mismo provider.
- Q3: Hot-swap scope → Default: solo nuevas requests; in-flight usan la asignación al inicio.
- Q4: STT client API change → Default: route.ts reescrito como proxy. Cliente Next.js no cambia (sigue POST multipart al mismo endpoint).
- Q5: Embedding dim guard strict → Default: rechazar != 1536 con HTTP 422 + mensaje claro.

## Plan Generation Strategy
- 13 fases en orden del usuario M1→M13, pero la ejecución interna reordena: M1→M2→M4a→M3→M4b→M5→M6→M7→M8→M9→M10→M11→M12→M13.
- Cada fase con tests antes de la siguiente.
- Estructura: 1 Write (skeleton) + múltiples Edits (tasks en batches de 2-4).
- Tamaño manejable para incremental write protocol.
