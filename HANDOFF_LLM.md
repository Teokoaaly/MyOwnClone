# HANDOFF_LLM — Implementación del Plan Sisyphus (M0→M13)

> **Documento de transferencia para otro LLM/agente.** Contiene: estado real del repo, todos los errores encontrados y sus fixes, la mecánica de auto-verificación (M0), y el plan completo M1→M13 listo para ejecutar.
>
> **Fecha:** 2026-06-21 · **Rama:** `audit/vps-sync-and-docs` (worktree de `MyOwnClone`) · **Autor:** agente anterior (sesión actual)

---

## 0. CÓMO EMPEZAR (lectura obligatoria)

1. **Lee primero `.sisyphus/plans/ai-models-configurable.md`** y `.sisyphus/drafts/ai-models-catalog.md` — son el diseño original del usuario (M1→M13 con esquema de tablas, rutas, tests).
2. **El plan vive en `.sisyphus/progress.json`** (estado canónico, 15 tareas). NO edites su schema sin actualizar `scripts/check-plan-progress.py`.
3. **Mecánica anti-olvido (ya implementada en M0):**
   - `python scripts/check-plan-progress.py` → exit 0 = progreso consistente.
   - `pytest tests/test_plan_completion.py` → 15 tests, **1 por milestone**, en ROJO hasta que el símbolo canónico del hito sea importable.
   - Pre-commit hook en `C:/Users/haxth3/Documents/MyOwnClone/.git/hooks/pre-commit` bloquea commits si progress.json es inconsistente.
4. **Orden de ejecución obligatorio** (dependencias reales): `M0(***REMOVED***) → M1 → M2 → M4a → M3 → M4b → M5 → M6 → M7 → M8 → M9 → M10 → M11 → M12 → M13`.
5. **Para cada hito:** marca `status:"in_progress"` al empezar → codea → `pytest` verde → crea `.sisyphus/evidence/task-M<N>-*.md` → `git add` + `git commit` → captura SHA con `git rev-parse HEAD` → escribe SHA en `progress.json` → marca `status:"***REMOVED***"` → commit final.

---

## 1. ESTADO ACTUAL (verificado 2026-06-21)

### Git
```
HEAD: ca26b1f  feat(sisyphus): M0 — capa anti-olvido
       (commit anterior: 41b3ef3 feat(rag): standard pipeline ...)
```
**Worktree:** el repo físico está en `C:\Users\haxth3\Documents\MyOwnClone-vps-fixes`, pero `.git` apunta a `C:\Users\haxth3\Documents\MyOwnClone\.git\worktrees\MyOwnClone-vps-fixes`. **Git-common-dir:** `C:\Users\haxth3\Documents\MyOwnClone\.git` (ahí viven los hooks).

### Working tree SIN commitear (debes commitear esto primero)
```
M  .sisyphus/progress.json          # SHA corregido a ca26b1f + PENDING validation
M  scripts/check-plan-progress.py   # 2 bugfixes (ver §3.1 y §3.2)
M  scripts/pre-commit-hook.sh       # resolver python robusto (ver §3.3)
```
> `git add` hizo staging selectivo. Los archivos `.sisyphus/drafts/`, `.sisyphus/plans/`, `MyOwnClone/nul`, `nul`, y los `M  MyOwnClone/src/...` **NO son del plan** — no los toques.

### Tests
```
pytest (baseline, sin plan_completion): 96 passed ✅
pytest tests/test_plan_completion.py:     1 failed (test_m1_ai_model_classes_exist) ✅ esperado
check-plan-progress.py:                   [OK] progreso consistente ✅
```

### Implementación del plan M1→M13
**0% implementado.** Solo existe M0 (la infraestructura de verificación). Las búsquedas de `AIModel`, `model_registry`, `invoke_for_task`, `SecretCipher`, `AESGCM`, `ia-modelos` en `api/` y `MyOwnClone/src/` devuelven **0 coincidencias en código** (solo aparecen en `.sisyphus/*.md`).

---

## 2. ERRORES DEL REPO PREEXISTENTES (detectados durante la auditoría)

### 2.1 ✅ YA CORREGIDO — `_EMBEDDING_DIMENSIONS` inexistente
- **Síntoma:** `tests/test_local_knowledge_retrieval.py` fallaba al importar: `ImportError: cannot import name '_EMBEDDING_DIMENSIONS' from 'api.core.retrieval'`.
- **Causa:** el test importaba `_EMBEDDING_DIMENSIONS` (privado, con guion bajo) pero `retrieval.py:28` importa `EMBEDDING_DIMENSIONS` (público, sin guion bajo) desde `embeddings.py`.
- **Fix aplicado (commit ca26b1f):** en `tests/test_local_knowledge_retrieval.py`, cambiar `_EMBEDDING_DIMENSIONS` → `EMBEDDING_DIMENSIONS` en 2 sitios (línea 5 del import y línea 343 del assert).
- **Estado:** corregido. Baseline recuperada a 96 passed.

### 2.2 ⏳ PENDIENTE — Defecto #2: cost tracking ausente en streaming
- **Dónde:** `api/core/model_manager.py`, funciones `_invoke_openai_stream` (254-279), `_invoke_anthropic_stream` (317-339), `_invoke_together_stream` (379-407), `_invoke_minimax_stream` (447-475).
- **Síntoma:** los 4 backends streaming **NO llaman a `_record_llm_cost`**. Solo los no-streaming lo hacen. Resultado: cada chat streaming consume tokens sin contabilizar coste.
- **Fix (parte de M7):**
  - OpenAI/Together/MiniMax: pasar `stream_options={"include_usage": True}` al `create(...)`, y en el bucle capturar el `usage` del último chunk (donde `choices` viene vacío pero `chunk.usage` está). Llamar `_record_llm_cost(...)` tras el yield.
  - Anthropic: con `client.messages.stream(...)`, leer `stream_ctx.final_message().usage` al cerrar (campos `input_tokens`/`output_tokens`).
- **Lo cubre el hito M7 del plan.**

### 2.3 ⏳ PENDIENTE — Defecto #3: string literal `"clone_response"`
- **Dónde:** `api/core/model_manager.py:206` — `category="clone_response"` hardcodeado en `_record_llm_cost`.
- **Fix (parte de M13):** usar `CostCategory.CLONE_RESPONSE.value` (el enum ya existe en `api/models/analytics.py:16-19`).
- **Lo cubre el hito M13 del plan.**

### 2.4 ⏳ PENDIENTE — Defecto #4: sin batching en `/api/embed` público
- **Dónde:** `api/controllers/myownclone_public.py` (endpoint `/api/embed`).
- **Síntoma:** pasa la lista entera a `embed_texts` sin respetar `_OPENAI_BATCH_SIZE=512`.
- **Fix (parte de M13):** trocear input en chunks de 512 antes de llamar `embed_texts`.
- **Lo cubre M13.**

### 2.5 ⏳ PENDIENTE — Defecto #6: threshold silencioso en retrieval
- **Dónde:** `api/core/retrieval.py`, umbral `0.25`.
- **Síntoma:** cuando el score cae bajo el umbral, el sistema degrada a léxico sin loggear warning → invisible para ops.
- **Fix (parte de M13):** añadir `logger.warning(...)` explícito en la rama de fallback.
- **Lo cubre M13.**

### 2.6 NOTA — Weaviate posiblemente legacy
- **Dónde:** `requirements.txt` + `docker-compose.backend.prod.yml`.
- `ARCHITECTURE.md` lo marca "posiblemente legacy". El RAG usa **pgvector** (`chunks.embedding vector(1536)` + ivfflat). Confirmar con `api/core/retrieval.py` antes de eliminarlo. **No es bloqueante para el plan.**

---

## 3. BUGS DE MI PROPIA IMPLEMENTACIÓN DE M0 (ya fixados en working tree, falta commitear)

### 3.1 Bug en `check-plan-progress.py`: `lstrip("./")` destruía paths
- **Síntoma:** el checker reportaba "evidence_file NO commiteado" aunque `git ls-files` confirmaba que sí lo estaba.
- **Causa raíz:** `path.lstrip("./")` NO elimina el literal `"./"` — elimina **cualquier combinación de los caracteres `.` y `/`** del inicio. Como `.sisyphus/evidence/...` empieza con `.`, `lstrip("./")` eliminaba el `.` inicial → convertía `.sisyphus/...` en `sisyphus/...`, que no existe en git.
- **Fix aplicado (working tree):**
  ```python
  # ANTES (roto):
  rel = path.lstrip("./")
  # DESPUÉS (correcto):
  rel = path[2:] if path.startswith("./") else path
  ```
- **Lección para el siguiente LLM:** `str.lstrip(chars)` trata `chars` como un **set de caracteres**, no como un prefijo literal. Para quitar un prefijo usa `str.removeprefix()` (3.9+) o slicing.

### 3.2 Bug en `check-plan-progress.py`: SHA `"PENDING"` no validado
- **Síntoma:** el checker aceptaba `committed_sha: "PENDING"` y luego fallaba confusamente.
- **Fix aplicado:** tratar `"PENDING"` y `""` como inválidos, con mensaje claro:
  ```python
  if not sha or sha == "PENDING":
      errors.append(f"{tid}: marcada '***REMOVED***' con committed_sha vacio/PENDING...")
  ```

### 3.3 Hook pre-commit no encontraba `python` en Windows
- **Síntoma:** el hook fallaba con `Python was not found; run without arguments to install from the Microsoft Store` — el stub de WindowsApps intercepta `python` cuando el hook corre bajo `sh`.
- **Causa:** `command -v python` encuentra el alias de Microsoft Store (que no es un intérprete real).
- **Fix aplicado:** el hook ahora prueba candidatos ejecutando `--version` real, con fallbacks `python3 → python → py → python.exe → py.exe`, más override vía `git config sisyphus.python <path>` o `$SISYPHUS_PYTHON`.
- **Si persiste:** ejecutar `git config sisyphus.python "C:/Users/haxth3/AppData/Local/Programs/Python/Python312/python.exe"` (o el venv del hermes-agent: `C:/Users/haxth3/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe`).

### 3.4 Estado de los fixes de §3
Los 3 fixes están en el **working tree sin commitear** (ver §1). Commit sugerido:
```
git add scripts/check-plan-progress.py scripts/pre-commit-hook.sh .sisyphus/progress.json
git commit -m "fix(sisyphus): M0 — bugfixes checker (lstrip, PENDING sha) + hook python resolver"
```

---

## 4. PATRONES DE CÓDIGO REALES (para que cada archivo nuevo sea consistente)

### 4.1 Modelos SQLAlchemy — `api/models/analytics.py` es el patrón a imitar
```python
import enum
from datetime import datetime
from typing import Optional
from sqlalchemy import DateTime, Integer, String, func, text
from sqlalchemy.orm import Mapped, mapped_column
from api.libs.datetime_utils import naive_utc_now
from api.libs.uuid_utils import uuidv7
from ..base import DefaultFieldsDCMixin, TypeBase

class CostCategory(enum.StrEnum):            # StrEnum, NO Enum plano
    CLONE_RESPONSE = "clone_response"

class CostTracking(TypeBase):                # hereda TypeBase (DeclarativeBase)
    __tablename__ = "cost_tracking"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True,
        insert_default=lambda: str(uuidv7()), default=lambda: str(uuidv7()),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False,
        insert_default=naive_utc_now, default=naive_utc_now,
        server_default=func.current_timestamp(),
    )
```
- **Base:** `api/base.py` define `TypeBase(DeclarativeBase)` (abstract) y `DefaultFieldsDCMixin` (id/created_at/updated_at).
- **ID:** UUIDv7 vía `str(uuidv7())` de `api/libs/uuid_utils.py` (time-ordered, 36 chars, `String(36)`).
- **Timestamps:** `naive_utc_now()` de `api/libs/datetime_utils.py` (UTC sin tzinfo) + `server_default=func.current_timestamp()`.
- **Enums:** `enum.StrEnum` (no `Enum`).
- **Registro:** los modelos se re-exportan en `api/models/__init__.py` (import explícito).

### 4.2 Migraciones Alembic — patrón idempotente en `2026_06_21_0001`
- Helpers: `_enum_exists`, `_index_exists`, `_column_exists` (consultan `pg_type`/`pg_indexes`/`information_schema`).
- `CREATE ... IF NOT EXISTS` en todo para re-runs seguros.
- **Fallback SQLite/test:** `if conn.dialect.name != "postgresql": pass` (solo aplica columnas portables).
- **down_revision actual (HEAD):** `d1e2f3a4b5c6`. La nueva migración de M1 debe usar `down_revision = 'd1e2f3a4b5c6'` y un `revision` nuevo (ej: `e2f3a4b5c6d7`).
- **NUNCA modificar migraciones existentes** — solo añadir nuevas.

### 4.3 Cost tracking — `_record_llm_cost` en `model_manager.py:183`
```python
def _record_llm_cost(*, tenant_id, model, usage: ModelUsage | None, operation="invoke_llm"):
    if not tenant_id or not usage or usage.total_tokens == 0:
        return
    cost_cents = estimate_llm_cost_cents(model=model, tokens_in=..., tokens_out=...)
    db.session.add(CostTracking(tenant_id=..., category="clone_response", ...))
    db.session.commit()   # best-effort, envuelto en try/except
```
- `estimate_llm_cost_cents` vive en `api/core/pricing.py`.
- **Defecto #3:** usar `CostCategory.CLONE_RESPONSE.value` en vez del literal.

### 4.4 Generación LLM — `GenerationParams` / `ModelReply` / `ModelUsage`
Viven en `api/core/model_manager.py:62-138`. **M4a los mueve** a `api/core/providers/base.py` y los re-exporta desde `model_manager` para back-compat.
- `GenerationParams.from_env()` lee `LLM_TEMPERATURE`/`LLM_MAX_TOKENS`/`LLM_TOP_P`.
- `ModelReply{text, usage}`, `ModelUsage{prompt_tokens, completion_tokens, total_tokens}`.

### 4.5 Endpoints admin — `api/controllers/console/myownclone/admin_platform.py`
```python
from api.controllers.console import console_ns
from api.controllers.console.wraps import account_initialization_required, setup_required
from api.libs.login import login_required
from api.extensions.ext_database import db
from pydantic import BaseModel, Field

class CreateTenantPayload(BaseModel):
    name: str = Field(..., min_length=1)

register_schema_models(console_ns, CreateTenantPayload)

@console_ns.route("/tenants")
class TenantList(Resource):
    @login_required
    def get(self): ...
```
- Namespace: `console_ns`. Auth: `@login_required`. Schemas: Pydantic v2 + `register_schema_models`.

### 4.6 Embeddings — `api/core/embeddings.py`
- `EMBEDDING_DIMENSIONS = 1536` (fijo, coincide con `vector(1536)` de pgvector).
- `_OPENAI_BATCH_SIZE = 512`.
- Fallback léxico (`_lexical_embedding`) si no hay `OPENAI_API_KEY` — **debe preservarse** en M8.
- **M8** añade parámetro `model: AIModel | None = None` a `embed_texts`; si llega modelo, usa su adapter; si no, fallback a env actual.

### 4.7 `assert_production_secrets` — `api/libs/security_checks.py`
- `_REQUIRED_IN_PROD` tupla de vars obligatorias en prod.
- `_INSECURE_DEFAULTS` dict de valores prohibidos.
- **M2 añade** `MODEL_SECRETS_KEY` a `_REQUIRED_IN_PROD`.

---

## 5. PLAN DE EJECUCIÓN M1→M13 (detallado, verificable)

Cada hito = 1 commit atómico `feat(<scope>): M<n> — <resumen>`.

### M1 — Capa de datos
**Nuevos:**
- `api/models/ai_models.py`: enums `AIProvider` (openai/anthropic/minimax/together/openai_compatible/local), `AICapability` (llm/embedding/stt/tts/reranking), `AITask` (chat/embedding/email_classification/email_draft/stt); mapa `TASK_CAPABILITY`; modelos:
  - `AIModel`: id, provider, model_id, base_url, api_key_encrypted (Text), capabilities (JSON/ARRAY), input_price_cents_per_mtok, output_price_cents_per_mtok, priority, is_active, created_at.
  - `AIModelAssignment`: id, task (unique partial WHERE is_active), model_id (FK→ai_models ON DELETE RESTRICT), tenant_id (nullable=global), priority, is_active.
  - `AIInvocation`: id, tenant_id, model_id, task, prompt_tokens, completion_tokens, cost_cents, latency_ms, created_at (se adelanta desde M12 para el cost en streaming de M7).
- `api/migrations/versions/2026_06_21_0002_ai_models_catalog.py` (`down_revision='d1e2f3a4b5c6'`): 3 tablas + **partial unique index** `CREATE UNIQUE INDEX ... ON ai_model_assignments(tenant_id, task) WHERE is_active=true` + FK `ON DELETE RESTRICT`.
- `api/tests/test_ai_models_schema.py`: enums, violación del partial-unique, FK RESTRICT.
**Edita:** `api/models/__init__.py` (registrar los 3 modelos).
**Símbolo canónico (smoke test):** `api.models.ai_models.AIModel`, `.AIModelAssignment`, `.AIInvocation`.

### M2 — Cifrado AES-256-GCM
**Nuevos:**
- `api/libs/crypto.py`: clase `SecretCipher` (métodos estáticos) usando `cryptography.hazmat.primitives.ciphers.aead.AESGCM` (**NO Fernet** — el smoke test lo verifica leyendo el fuente). Master key desde env `MODEL_SECRETS_KEY` (base64 de 32 bytes). Nonce 12 bytes random por encrypt. Formato: `base64(nonce ‖ ciphertext ‖ tag)`. Métodos: `encrypt(str)->str`, `decrypt(str)->str`, `generate_master_key()->str`, `is_configured()->bool`.
- `api/commands/crypto.py`: `flask generate-master-key` (imprime base64-32), `flask rotate-secrets-key --new <key>` (cuerpo en M12, stub aquí).
- `api/tests/test_crypto.py`: round-trip, **tampering→InvalidTag**, missing key→ValueError, wrong length→ValueError, rotación A→B falla (descifrar con B lo que cifró A lanza error).
**Edita:** `api/libs/security_checks.py` → añadir `"MODEL_SECRETS_KEY"` a `_REQUIRED_IN_PROD`.
**Símbolo canónico:** `api.libs.crypto.SecretCipher`.

### M4a — Interface de providers (va ANTES que M3)
**Nuevos:** `api/core/providers/{__init__,base,registry}.py`.
- `base.py`: ABC `ProviderAdapter` con `invoke(prompt, *, model, params)->ModelReply`, `invoke_stream(...)->Generator[str]`, `test_connection(model)->TestResult`. Dataclasses `TestResult{ok, latency_ms, error}`.
- **Mover** `GenerationParams`, `ModelReply`, `ModelUsage`, `ModelInvocationError` de `model_manager.py` a `providers/base.py`. Re-exportarlos desde `model_manager` para back-compat (el smoke test lo verifica).
- `registry.py`: `ProviderRegistry` con `_adapters: dict[str, type[ProviderAdapter]]`, registro decorador `@register("openai")`, getter `get(provider_name)->AdapterClass`.
- `api/tests/test_provider_registry.py`.
**Símbolo canónico:** `api.core.providers.ProviderAdapter`, `.ProviderRegistry`.

### M3 — ModelRegistry (resolver + cache)
**Nuevo:** `api/core/model_registry.py`.
- `ModelRegistry.get_model_for_task(tenant_id, task) -> AIModel`:
  - **Cache TTL 60s** por clave `(tenant_id, task)`. Implementar con dict de `(key -> (timestamp, model))`.
  - **Fallback chain:** DB (tenant + globales `tenant_id IS NULL`, orden por priority) → cache → legacy env (`_detect_provider`) → `raise`.
  - Descifra `api_key_encrypted` vía `SecretCipher.decrypt` (import de M2).
- `ModelRegistry.invalidate(tenant_id, task=None)`: borra la entrada de cache.
- `api/tests/test_model_registry.py`: resolución, expiración TTL, invalidación manual, aislamiento multi-tenant (tenant A no ve modelos de B).
**Símbolo canónico:** `api.core.model_registry.ModelRegistry` con `get_model_for_task` e `invalidate`.

### M4b — 6 adapters concretos
**Nuevos:** `api/core/providers/{openai,anthropic,minimax,together,openai_compatible,local}.py`.
- Cada uno extiende `ProviderAdapter` y **reutiliza la lógica** de `model_manager.py:222-507` (`_invoke_openai`, etc.) pero leyendo `model.api_key` (ya descifrado por el registry), `model.model_id`, `model.base_url` en vez de `os.environ`.
- Auto-registro: `@register("openai")` al inicio de cada clase.
- `openai_compatible.py`: genérico para DeepSeek/Ollama/etc (cualquier endpoint OpenAI-compatible con base_url custom).
- `local.py`: stub para modelos locales (Ollama) — puede `raise NotImplementedError` si no hay demanda, pero la clase debe existir y registrarse.
**Símbolo canónico:** `api.core.providers.OpenAIAdapter` (o `_adapters` poblado con los 6 nombres).

### M5 — RetryClient
**Nuevo:** `api/core/retry_client.py`.
- `RetryClient.invoke(adapter, prompt, model, params, ...)`: 3 retries con backoff exponencial (1s, 2s, 4s). Failover al siguiente modelo por `priority` si el adapter agota retries.
- **Circuit breaker:** 3 fallos en 60s → estado OPEN 30s → half-open (1 petición de prueba) → CLOSE si éxito.
- `api/tests/test_retry_client.py` con mock adapter que falla N veces.
**Símbolo canónico:** `api.core.retry_client.RetryClient`.

### M6 — TokenBudgeter
**Nuevo:** `api/core/token_budget.py`.
- Usa `gpt-tokenizer` (añadir a `requirements.txt`) para contar/truncar tokens del contexto RAG.
- `enforce responses_month_limit`: consulta `count_responses_this_month(tenant_id)` vs `Plan.responses_month_limit`.
- **Guard `embedding_dimensions == 1536`:** al crear/editar un `AIModel` con capability `embedding`, rechazar si las dims ≠ 1536 (lanzar `ValueError` claro, no silent).
- `api/tests/test_token_budget.py`.
**Símbolo canónico:** `api.core.token_budget.TokenBudgeter`.

### M7 — Refactor `model_manager.py` ⭐ (punto crítico)
**Edita:** `api/core/model_manager.py`.
- Nuevo método: `ModelManager.invoke_for_task(tenant_id, task, prompt, *, params=None, stream=False)`:
  - `ModelRegistry.get_model_for_task(tenant_id, task)` → `ProviderRegistry.get(model.provider)` → `RetryClient.invoke(...)`.
- **Corrige Defecto #2** (ver §2.2): los `_invoke_*_stream` ahora persisten cost. Patrón:
  ```python
  def _invoke_openai_stream(prompt, *, model, params, tenant_id, task):
      client = openai.OpenAI(api_key=model.api_key, base_url=model.base_url)
      response = client.chat.completions.create(
          ..., stream=True, stream_options={"include_usage": True},
      )
      usage = None
      for chunk in response:
          if chunk.usage:                      # último chunk
              usage = ModelUsage(chunk.usage.prompt_tokens, ...)
          elif chunk.choices and chunk.choices[0].delta.content:
              yield chunk.choices[0].delta.content
      if usage:
          _record_llm_cost(tenant_id=tenant_id, model=model.model_id, usage=usage)
          _record_ai_invocation(tenant_id, model.id, task, usage)  # INSERT ai_invocations
  ```
- `invoke_non_streaming` / `invoke_streaming` quedan como wrappers delgados que llaman a `invoke_for_task` (back-compat con los call sites actuales).
**Símbolo canónico:** `api.core.model_manager.ModelManager.invoke_for_task`.

### M8 — Refactor `embeddings.py`
**Edita:** `api/core/embeddings.py`.
- Cambiar firma: `embed_texts(self, texts: list[str], *, model: AIModel | None = None)`.
- Si `model` llega: usar `ProviderRegistry.get(model.provider)` para obtener el cliente (decrypt ya hecho por registry). Respeta `model.model_id`.
- Si `model` es None: comportamiento actual (env vars).
- **Preservar** `_OPENAI_BATCH_SIZE=512`, `EMBEDDING_DIMENSIONS=1536`, y el fallback léxico.
**Símbolo canónico:** `EmbeddingService.embed_texts` con param `model`.

### M9 — API admin REST
**Nuevo:** `api/controllers/console/myownclone/ai_models.py` en `console_ns` + `login_required` + check `platform_admin` (patrón `admin_platform.py`).
- `GET /console/api/myownclone/ai/models` — lista (sin api_key).
- `POST /console/api/myownclone/ai/models` — crea (cifra api_key vía `SecretCipher`).
- `GET/PUT/DELETE /console/api/myownclone/ai/models/<id>` — **nunca** devuelve key descifrada; DELETE = soft `is_active=false`.
- `POST /console/api/myownclone/ai/models/<id>/test` — llama `adapter.test_connection(model)`.
- `POST /console/api/myownclone/ai/playground` — ejecuta prompt, devuelve text+tokens+costo.
- `GET /console/api/myownclone/ai/assignments` — las 5 tareas.
- `PUT /console/api/myownclone/ai/assignments/<task>` — reasigna + `ModelRegistry.invalidate(...)`.
- Validación capability↔task; **embedding-dim guard HTTP 422**.
- `api/tests/test_ai_models_endpoints.py`.
**Símbolo canónico:** `api.controllers.console.myownclone.ai_models` (con `ns`/`ai_models_ns`/`register_routes`).

### M10 — Integración en 5 puntos de consumo
- **chat:** `task=AITask.CHAT` en `api/services/clone_service.py` / controladores de clone.
- **ingestion + embeddings:** `task=AITask.EMBEDDING` en `api/core/ingestion_pipeline.py`.
- **email:** `task=AITask.EMAIL_CLASSIFICATION` + `EMAIL_DRAFT` en `api/core/myownclone/email_ai.py`.
- **STT:** mover lógica de `MyOwnClone/src/app/api/stt/route.ts` a un proxy que llame a nuevo `api/controllers/console/myownclone/internal_stt.py` (Flask resuelve modelo vía catálogo). API pública del cliente Next.js sin cambios (multipart).

### M11 — UI `/admin/ia-modelos`
**Nuevos en `MyOwnClone/src/app/admin/ia-modelos/`:**
- `page.tsx` (server component): tabla de modelos + 5 dropdowns de asignaciones + playground + cost chart.
- `AIModelForm.tsx`, `TaskAssignmentCard.tsx`, `Playground.tsx`, `CostChart.tsx` (con `recharts`, ya en deps).
- Máscara del campo `api_key` (tipo password, mostrar solo `••••` + últimos 4).
- QA con Playwright (`npm run test:e2e`).
- `npm run typecheck && npm run lint` deben pasar (sin `any`/`@ts-ignore`).

### M12 — Auditoría + rollup + rotación
- `ai_invocations` ya creada en M1; aquí se **usa** + se añade **vista materializada `cost_daily_rollup`**: refresh por trigger `AFTER INSERT` en `cost_tracking` + cron diario de defensa.
- Migración `api/migrations/versions/2026_06_21_0003_cost_rollup.py` (`down_revision = <revision de M1>`).
- `flask rotate-secrets-key --new <key>`: doble-clave (vieja descifra, nueva cifra); re-cifra todas las `ai_models.api_key_encrypted` en una transacción.

### M13 — Defectos restantes + backfill + docs
- **Defecto #3** (§2.3): eliminar literal `"clone_response"` → `CostCategory.CLONE_RESPONSE.value`.
- **Defecto #4** (§2.4): batching en `/api/embed` — trocear en 512.
- **Defecto #6** (§2.5): threshold `retrieval.py:0.25` → `logger.warning(...)`.
- **Backfill:** `flask ai-backfill-from-env` — idempotente (solo crea modelos faltantes desde `OPENAI_API_KEY`/`ANTHROPIC_API_KEY`/etc.; cifra keys; no toca asignaciones activas existentes).
- **Docs:** sección "Migración al sistema de modelos" en `MANUAL_TECNICO.md` — **aviso crítico: pérdida de master key = claves irrecuperables**, backfill es la única salida.

---

## 6. DEFINITION OF DONE (verificable sin intervención humana)
- [ ] `pytest -v` verde: 96 existentes + ~9 nuevos + `tests/test_plan_completion.py` (15 tests).
- [ ] `python scripts/check-plan-progress.py` → exit 0 (15/15 ***REMOVED*** con evidence+SHA).
- [ ] `flask --app app_factory db upgrade` limpio; `downgrade -1` reversible.
- [ ] `flask generate-master-key` imprime base64-32.
- [ ] `GET /console/api/myownclone/ai/assignments` devuelve las 5 tareas.
- [ ] `POST /console/api/myownclone/ai/playground` devuelve tokens+costo.
- [ ] Cambiar asignación vía API afecta la **siguiente** request (cache invalidado).
- [ ] Cost tracking en streaming persiste en `cost_tracking` + `ai_invocations`.
- [ ] `npm run typecheck && npm run lint` verde.
- [ ] SQL: `SELECT count(*) FROM ai_models WHERE api_key_encrypted NOT LIKE 'gAAAA%'` = total (ninguna en texto plano).

---

## 7. GUARDRAILS (no negociables)
- NO providers fuera de los 6 listados.
- NO cambiar el cipher format tras M2 (rompe todas las keys).
- NO acceder a `ai_models` sin `ModelRegistry` tras M3.
- NO strings literales para providers (usar `AIProvider` enum).
- NO `os.environ` para api keys en código nuevo (solo en `model_registry` fallback legacy).
- NO `any` / `@ts-ignore` en frontend.
- NO modificar migraciones existentes (solo añadir nuevas con `down_revision` correcto).
- NO Fernet (smoke test lo verifica leyendo el fuente de `crypto.py`).

---

## 8. STACK CONFIRMADA
- **Backend:** Flask 3 + flask-restx + SQLAlchemy 2.0 + Alembic + PostgreSQL 15/pgvector + Redis. Python 3.11/3.12.
- **Frontend:** Next.js 16.2.9 + React 19.2.4 + Tailwind 4 + recharts + drizzle-orm + next-auth.
- **Tests:** pytest (backend) + vitest/playwright (frontend).
- **Interpreter en Windows:** `C:/Users/haxth3/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe` (3.11.15) o `py` (3.12.10).

## 9. PRIMER PASO DEL SIGUIENTE LLM
```bash
# 1. Commitear los fixes pendientes de M0 (§3):
cd C:/Users/haxth3/Documents/MyOwnClone-vps-fixes
git add scripts/check-plan-progress.py scripts/pre-commit-hook.sh .sisyphus/progress.json
git commit -m "fix(sisyphus): M0 — bugfixes checker (lstrip, PENDING sha) + hook python resolver"

# 2. Verificar baseline:
python -m pytest -q --ignore=tests/test_plan_completion.py   # 96 passed
python scripts/check-plan-progress.py                          # [OK]

# 3. Empezar M1: marcar in_progress en progress.json, crear api/models/ai_models.py
```
