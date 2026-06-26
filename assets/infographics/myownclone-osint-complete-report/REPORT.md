# MyOwnClone — Informe OSINT Completo
## MyClone.is (227 endpoints) + Código MyOwnClone + Plan de 5 Pasos

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  MyOwnClone — Informe OSINT Completo                                       ║
║  MyClone.is (227 endpoints) + Código MyOwnClone + Plan de 5 Pasos          ║
║  Fecha: 2026-06-24 | Fuente: api.myclone.is + código local                ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## SEC-01 │ MyClone.is — API Descubierta

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-01                              MyClone.is — 227 Endpoints              │
│ pop-laboratory · blueprint grid     Prompt Versioning + Voice + Embeddings  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BASE URL        https://api.myclone.is                                     │
│  STACK           Python + Uvicorn (ASGI) · AWS                              │
│  ENDPOINTS       227 (OpenAPI 1.0.0)                                       │
│  AUTH            POST /api/v1/auth/login → {user_id, token, account_type}  │
│                                                                             │
│  SERVICES ─────────────────────────────────────────────────────────────────│
│  ▸ Voyage AI     Embeddings: 96,891 vectors indexados                      │
│  ▸ Langfuse      Prompt engineering + observabilidad                        │
│  ▸ Cartesia AI   Voice cloning                                             │
│  ▸ ElevenLabs    Voice cloning                                             │
│  ▸ LiveKit       Voz real-time                                             │
│  ▸ Stripe Conn.  Monetización por persona                                  │
│  ▸ Vercel AI SDK Streaming SSE                                             │
│                                                                             │
│  KEY ENDPOINTS ───────────────────────────────────────────────────────────│
│  ▸ POST /personas/username/{username}/stream-chat    SSE streaming         │
│  ▸ POST /personas/username/{username}/init-session   Inicia sesión        │
│  ▸ GET  /knowledge-library/users/{user_id}            Biblioteca completa  │
│  ▸ GET  /prompt/persona-prompts/{id}/history         Versiones prompt    │
│  ▸ POST /prompt/persona-prompts/{id}/restore/{v}     Restaurar versión    │
│  ▸ GET  /embeddings/stats                             Stats: 96,891       │
│  ▸ POST /workflows/sessions/{id}/answer              Responder step       │
│  ▸ POST /livekit/connection-details                  Credenciales voice   │
│  ▸ POST /stripe/personas/{id}/monetization           Activar pago        │
│                                                                             │
│  TIERS ────────────────────────────────────────────────────────────────────│
│  ┌───────────┬────────────┬──────────────────┐                              │
│  │ FREE      │ 2 personas │ 500 msg · 10min  │                              │
│  │ PRO       │ 3 personas │ —                │                              │
│  │ BUSINESS  │ 30 personas│ —                │                              │
│  │ ENTERPRISE│ ∞ personas │ custom domains   │                              │
│  └───────────┴────────────┴──────────────────┘                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**CREDENCIALES TEST:** `xoyigo3386@disiok.com` / `2cji!6Tbhc3RLp@` — User ID: `2021aa30-cdf1-465b-98d6-03896a252861` — account_type: `creator`

---

## SEC-02 │ MyClone Prompt System

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-02                              MyClone Prompt System                    │
│ pop-laboratory · blueprint grid     {{variable}} template + versioning      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  VARIABLE TEMPLATE ────────────────────────────────────────────────────────│
│  # Expert Digital Persona System Instructions                               │
│                                                                             │
│  You are {name}, {role} at {company}, {description}...                     │
│                                                                             │
│  ## Core Identity & Expertise                                               │
│  Professional Background: {introduction}                                    │
│  Primary Expertise Areas: {area_of_expertise}                              │
│  Communication Objective: {chat_objective}                                 │
│                                                                             │
│  ## Behavioral Framework                                                   │
│  ▸ Stateful Interaction (historial completo)                               │
│  ▸ Progressive Disclosure (preguntas de evaluación primero)                │
│  ▸ Solution Reasoning (recolecta datos antes de recomendar)               │
│  ▸ Evidence-Based Responses (referencia contexto pasado)                  │
│                                                                             │
│  ## Communication Style                                                    │
│  {thinking_style: practical+authentic | systems thinking | story-driven}  │
│                                                                             │
│  ## Response Structure                                                     │
│  1. Assessment Phase   → preguntas targeted                                │
│  2. Information Gathering → progressive disclosure                         │
│  3. Solution Reasoning  → análisis                                          │
│  4. Recommendation     → advice actionable                                  │
│  5. Experience Integration → analogías                                       │
│                                                                             │
│  ## Conversation Guidelines                                                │
│  ▸ Single discovery question al inicio                                     │
│  ▸ Follow-ups building on previous answers                                 │
│  ▸ NO markdown en responses                                                │
│  ▸ Tone: human-like, friendly, casual                                      │
│                                                                             │
│  PROMPT VERSIONING API ──────────────────────────────────────────────────│
│  GET  /prompt/persona-prompts/{id}/history    → [{version, change_summary}] │
│  POST /prompt/persona-prompts/{id}/restore/{v} → restaura versión          │
│  GET  /prompt/persona-prompts/{id}/compare?v1=X&v2=Y → diff               │
│  GET  /prompt/persona-prompts/{id}/timeline  → línea temporal visual       │
│  GET  /prompt/persona-prompts/{id}/versions   → todas las versiones        │
│                                                                             │
│  VARIABLES MYCLONE vs MYOWNCLONE ────────────────────────────────────────│
│  ┌──────────────────────┬───────────────┬────────────────────────────────┐│
│  │ Variable              │ MyClone       │ MyOwnClone                     ││
│  ├──────────────────────┼───────────────┼────────────────────────────────┤│
│  │ name                 │ ✅            │ ✅ (clone.name)                 ││
│  │ description          │ ✅            │ ✅ (clone.description)           ││
│  │ role                 │ ✅            │ ❌ FALTA                       ││
│  │ company              │ ✅            │ ❌ FALTA                       ││
│  │ introduction         │ ✅            │ ❌ FALTA                       ││
│  │ area_of_expertise    │ ✅            │ ❌ FALTA                       ││
│  │ chat_objective       │ ✅            │ ❌ FALTA                       ││
│  │ thinking_style       │ ✅            │ ❌ (similar: personality_tone)  ││
│  │ language             │ ❌            │ ✅ (clone.language)            ││
│  │ modes enum           │ ❌            │ ✅ (teach/support/sales)       ││
│  │ memories/templates   │ ❌            │ ✅ (CreatorMemory)             ││
│  └──────────────────────┴───────────────┴────────────────────────────────┘│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-03 │ MyOwnClone — Arquitectura Real

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-03                              MyOwnClone — Stack Real                 │
│ pop-laboratory · blueprint grid     Flask + Next.js + Drizzle + Dify       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BACKEND FLASK ───────────────────────────────────────────────────────────│
│  /home/haxth3/myownclone_local/api/                                       │
│  ▸ controllers/                   REST API (Flask-RESTX)                   │
│  ▸ models/                        SQLAlchemy ORM                          │
│  ▸ core/retrieval.py              SiloRetrievalResult + retrieve_from_silo│
│  ▸ core/myownclone/email_ai.py    classify_email() + generate_draft_reply()│
│  ▸ core/myownclone/silos.py       CloneSilo enum ("teach"/"support"/"sales")│
│                                                                             │
│  FRONTEND NEXT.JS ───────────────────────────────────────────────────────│
│  /home/haxth3/MyOwnClone/MyOwnClone/src/                                  │
│  ▸ app/api/clone/memories/       Route TS → Drizzle directo a PostgreSQL  │
│  ▸ app/(dashboard)/cerebro/       Editor memories/signatures/templates      │
│  ▸ lib/db/schema/                 Drizzle ORM (TypeScript)                │
│  ▸ proxy.ts                       Mapeo /api/* → Flask :5001              │
│                                                                             │
│  DATABASE LAYER ──────────────────────────────────────────────────────────│
│  PostgreSQL ← Drizzle ORM (frontend directo, NO pasa por Flask)            │
│       ↑                                                                   │
│  PostgreSQL ← SQLAlchemy (backend Flask)                                   │
│                                                                             │
│  ⚠️  ARCHITECTURAL DRIFT: Frontend y Backend escriben a la misma DB      │
│      pero con schemas desconectados → inconsistencia de enums y campos    │
│                                                                             │
│  CHAT PIPELINE ───────────────────────────────────────────────────────────│
│  POST /api/myownclone/public/clones/{slug}/chat                           │
│       │                                                                    │
│       ▼                                                                    │
│  1. CloneConfig lookup (por slug)                                          │
│       │                                                                    │
│       ▼                                                                    │
│  2. CloneModePrompt lookup (clone_id + modo activo)                       │
│       │                                                                    │
│       ▼                                                                    │
│  3. _add_memories_to_prompt() → append memories al system prompt         │
│       │                                                                    │
│       ▼                                                                    │
│  4. retrieve_from_silo() → RAG búsqueda en dataset Dify                    │
│       │  SiloRetrievalResult {segments, scores, context_id}               │
│       ▼                                                                    │
│  5. Construye full_prompt = system_prompt + [CONTEXT: sources] + message  │
│       │                                                                    │
│       ▼                                                                    │
│  6. model_instance.invoke_llm_stream() → streaming SSE response          │
│       │                                                                    │
│       ▼                                                                    │
│  7. SSE: data: {content: chunk} → data: [DONE]                           │
│                                                                             │
│  CLONE SILO ENUM MISMATCH ───────────────────────────────────────────────│
│  ┌────────────────────┬───────────────────────────────────────────────┐   │
│  │ Flask (CloneSilo)  │ "teach" | "support" | "sales"                │   │
│  │ Drizzle (enum)     │ "pedagogy" | "support" | "sales"  ⚠️ MISMATCH│   │
│  └────────────────────┴───────────────────────────────────────────────┘   │
│  Conversión requerida: "teach" ↔ "pedagogy"                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-04 │ ⚠️ 4 Bugs Críticos

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-04                              ⚠️ 4 Bugs Críticos                      │
│ pop-laboratory · #E91E63 alert    Resolver ANTES de implementar features   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  🔴 BUG-01 │ Enum Mismatch — PRIORIDAD MÁXIMA                              │
│  ─────────────────────────────────────────────────────────────────────────│
│  Flask CloneSilo usa "teach"                                               │
│  Drizzle cloneModeEnum usa "pedagogy"                                      │
│                                                                             │
│  CONSECUENCIA: Al sincronizar datos entre Flask y Drizzle, los modos        │
│  no coinciden → clone_mode_prompts pueden tener "teach" en Flask pero       │
│  "pedagogy" en Drizzle → comportamiento errático del chat                  │
│                                                                             │
│  FIX: 1) Cambiar Drizzle enum a "teach"                                    │
│       2) UPDATE clone_mode_prompts SET mode='teach' WHERE mode='pedagogy'  │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────│
│  🔴 BUG-02 │ updatedAt faltante en cloneModePrompts (Drizzle)             │
│  ─────────────────────────────────────────────────────────────────────────│
│  El schema Drizzle de cloneModePrompts NO tiene updatedAt                 │
│  Pero SQLAlchemy SÍ lo tiene (heredado de DefaultFieldsDCMixin → TypeBase)│
│                                                                             │
│  CONSECUENCIA: Drift de schema entre Drizzle y SQLAlchemy                  │
│  FIX: ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP       │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────│
│  🔴 BUG-03 │ Campo title se PIERDE en Memorias — PRIORIDAD MÁXIMA         │
│  ─────────────────────────────────────────────────────────────────────────│
│  Frontend cerebro/page.tsx envía title en POST:                           │
│    body: { ..., title: String(payload.title) }                             │
│                                                                             │
│  Pero MemoryPayload en Flask creator_memory.py NO tiene campo title:       │
│    class MemoryPayload(BaseModel):                                         │
│        clone_id: str                                                        │
│        type: str                                                            │
│        content: str                                                         │
│        trigger_condition: str | None                                        │
│        priority: int                                                        │
│        # ❌ title NO ESTÁ                                                  │
│                                                                             │
│  El schema Drizzle memories SÍ tiene title:                                │
│    title: text("title").notNull()                                          │
│                                                                             │
│  CONSECUENCIA: El título que el usuario escribe en el frontend se pierde   │
│  completamente. El contenido existe en la DB vía Drizzle pero la API      │
│  Flask no puede crear/editar esos registros correctamente.                  │
│                                                                             │
│  FIX: 1) Añadir title: str a MemoryPayload en creator_memory.py           │
│       2) Asegurar sincronización bidireccional entre Drizzle y SQLAlchemy  │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────│
│  🟡 BUG-04 │ updatedAt en memories (Drizzle vs SQLAlchemy)                │
│  ─────────────────────────────────────────────────────────────────────────│
│  Drizzle: memories.updatedAt EXISTS (timestamp, notNull, defaultNow)        │
│  SQLAlchemy CreatorMemory: NO updatedAt field                              │
│                                                                             │
│  CONSECUENCIA: Drift de schema. Si el frontend usa Drizzle y el backend    │
│  usa SQLAlchemy, las actualizaciones pueden perder el updatedAt.             │
│                                                                             │
│  FIX: Añadir updated_at a CreatorMemory en SQLAlchemy                      │
│                                                                             │
│  ─────────────────────────────────────────────────────────────────────────│
│  ORDEN DE RESOLUCIÓN                                                      │
│  ┌─────────┬────────────────────────────────────────────────────────────┐ │
│  │ FASE 1  │ BUG-01 (enum) + BUG-03 (title) → rompen datos nyata       │ │
│  │ FASE 2  │ BUG-02 (updatedAt prompts) + BUG-04 (updatedAt memories)  │ │
│  └─────────┴────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-05 │ Step 1: Prompt Versioning

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-05                              Step 1: Prompt Versioning               │
│ pop-laboratory · teal/sage       Tablas + endpoints + UI diff/restore      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ARQUITECTURA: 2 tablas nuevas + 4 endpoints + UI frontend                 │
│                                                                             │
│  SQL: prompt_versions ────────────────────────────────────────────────────│
│  CREATE TABLE prompt_versions (                                            │
│      id TEXT PRIMARY KEY,                                                  │
│      clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE, │
│      mode TEXT NOT NULL,                        -- "teach"|"support"|"sales"│
│      version_number INTEGER NOT NULL,                                       │
│      system_prompt TEXT NOT NULL,                                          │
│      change_summary TEXT,                     -- "+N líneas añadidas, -M..." │
│      created_by TEXT,                         -- tenant_id o user_id        │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW(),                          │
│      UNIQUE(clone_id, mode, version_number)                                │
│  );                                                                        │
│  CREATE INDEX prompt_versions_clone_idx ON prompt_versions(clone_id);       │
│  CREATE INDEX prompt_versions_clone_mode_idx ON prompt_versions(clone_id,mode);│
│                                                                             │
│  SQL: prompt_variables ───────────────────────────────────────────────────│
│  CREATE TABLE prompt_variables (                                            │
│      id TEXT PRIMARY KEY,                                                  │
│      version_id TEXT NOT NULL REFERENCES prompt_versions(id),               │
│      variable_name TEXT NOT NULL,  -- "introduction", "thinking_style"...  │
│      variable_value TEXT,                                                      │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW()                            │
│  );                                                                        │
│                                                                             │
│  DRIZZLE SCHEMA ──────────────────────────────────────────────────────────│
│  // En src/lib/db/schema/clones.ts                                         │
│  export const promptVersions = pgTable("prompt_versions", {                 │
│    id: text("id").primaryKey(),                                            │
│    cloneId: text("clone_id").notNull().references(() => clones.id),        │
│    mode: cloneModeEnum("mode").notNull(),                                  │
│    versionNumber: integer("version_number").notNull(),                      │
│    systemPrompt: text("system_prompt").notNull(),                          │
│    changeSummary: text("change_summary"),                                  │
│    createdBy: text("created_by"),                                          │
│    createdAt: timestamp("created_at").notNull().defaultNow(),              │
│  }, (table) => [                                                           │
│    uniqueIndex("prompt_versions_clone_mode_version_idx")                   │
│      .on(table.cloneId, table.mode, table.versionNumber),                 │
│    index("prompt_versions_clone_idx").on(table.cloneId),                  │
│  ]);                                                                       │
│                                                                             │
│  export const promptVariables = pgTable("prompt_variables", {               │
│    id: text("id").primaryKey(),                                            │
│    versionId: text("version_id").notNull()                                 │
│      .references(() => promptVersions.id),                                 │
│    variableName: text("variable_name").notNull(),                          │
│    variableValue: text("variable_value"),                                  │
│    createdAt: timestamp("created_at").notNull().defaultNow(),              │
│  });                                                                       │
│                                                                             │
│  PYTHON MODEL ────────────────────────────────────────────────────────────│
│  # En api/models/clone.py — AÑADIR antes de CloneModePrompt                │
│  class PromptVersion(DefaultFieldsDCMixin, TypeBase):                      │
│      __tablename__ = "prompt_versions"                                     │
│      clone_id: Mapped[str] = mapped_column(String(36), nullable=False)     │
│      mode: Mapped[str] = mapped_column(String(20), nullable=False)         │
│      version_number: Mapped[int] = mapped_column(sa.Integer, nullable=False)│
│      system_prompt: Mapped[str] = mapped_column(LongText, nullable=False) │
│      change_summary: Mapped[Optional[str]] = mapped_column(LongText)        │
│      created_by: Mapped[Optional[str]] = mapped_column(String(36))          │
│                                                                             │
│  MODIFICAR CloneModePromptApi.put() ─────────────────────────────────────│
│  # En api/controllers/console/myownclone/clone.py                          │
│  def put(self, clone_id: str):                                            │
│      # ... código existente de fetch + validation ...                      │
│                                                                             │
│      # ANTES de actualizar, guardar versión anterior                        │
│      if prompt.system_prompt != data.system_prompt:                        │
│          _save_prompt_version(                                            │
│              session=db.session,                                           │
│              clone_id=clone_id,                                            │
│              mode=data.mode,                                               │
│              system_prompt=prompt.system_prompt,  # versión anterior       │
│              change_summary=_generate_change_summary(                       │
│                  prompt.system_prompt, data.system_prompt),                │
│          )                                                                 │
│      # ... resto del update ...                                            │
│                                                                             │
│  NUEVOS ENDPOINTS ────────────────────────────────────────────────────────│
│  GET  /console/api/myownclone/clones/{id}/prompts/history                 │
│       → Lista todas las versiones, agrupadas por modo                     │
│                                                                             │
│  POST /console/api/myownclone/clones/{id}/prompts/restore/{version}       │
│       → Copia system_prompt de la versión al CloneModePrompt activo       │
│       → Crea nueva versión registrando el restore                          │
│                                                                             │
│  GET  /console/api/myownclone/clones/{id}/prompts/diff?v1=X&v2=Y&mode=Y  │
│       → {old: "...", new: "...", diff: [...]}                             │
│                                                                             │
│  HELPER: _generate_change_summary() ─────────────────────────────────────│
│  import difflib                                                             │
│                                                                             │
│  def _generate_change_summary(old: str, new: str) -> str:                  │
│      old_lines = old.split('\\n')                                           │
│      new_lines = new.split('\\n')                                          │
│      diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=''))   │
│      if not diff:                                                          │
│          return "Sin cambios"                                              │
│      added = sum(1 for l in diff if l.startswith('+')                    │
│                  and not l.startswith('+++'))                              │
│      removed = sum(1 for l in diff if l.startswith('-')                   │
│                    and not l.startswith('---'))                            │
│      return f"+{added} líneas añadidas, -{removed} líneas eliminadas"       │
│                                                                             │
│  FRONTEND: cerebro/page.tsx ─────────────────────────────────────────────│
│  1. Añadir TAB en TABS array:                                             │
│     { id: "history", label: "Historial", singular: "Historial",            │
│       desc: "Versiones anteriores del prompt" }                            │
│                                                                             │
│  2. Nuevo tab content:                                                     │
│     - Lista de versiones agrupadas por modo                               │
│     - Cada versión: número, fecha, change_summary, botón "Ver diff"        │
│     - Botón "Restaurar" en cada versión                                    │
│     - Modal de diff (usar lib `diff` de npm)                             │
│                                                                             │
│  ARCHIVOS A MODIFICAR ──────────────────────────────────────────────────│
│  ▸ api/models/clone.py                  → Añadir PromptVersion           │
│  ▸ api/controllers/console/myownclone/   → Modificar put() + history/     │
│      clone.py                             restore/diff endpoints         │
│  ▸ src/lib/db/schema/clones.ts          → promptVersions + promptVariables│
│  ▸ src/app/(dashboard)/cerebro/page.tsx → Tab historial + UI             │
│                                                                             │
│  ORDEN DE IMPLEMENTACIÓN ────────────────────────────────────────────────│
│  1. Crear tablas SQL (prompt_versions + prompt_variables)                  │
│  2. Añadir PromptVersion model en Python                                  │
│  3. Modificar CloneModePromptApi.put() para snapshot                      │
│  4. Añadir 3 nuevos endpoints (history/restore/diff)                      │
│  5. Añadir Drizzle schemas                                               │
│  6. Implementar UI en cerebro/page.tsx                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-06 │ Steps 2-3: Visitors + Workflows

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-06                              Steps 2 & 3: Visitors + Workflows       │
│ pop-laboratory · teal/sage       BAJO esfuerzo vs ALTO esfuerzo            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  VISITORS ─────────────────────────────────────────────────────────────────│
│  ▸ PRIORIDAD: 🟢 ALTA — bajo esfuerzo, alto impacto                      │
│  ▸ MyOwnClone YA tiene visitorId en conversations (Drizzle)               │
│  ▸ FALTA: tabla visitors + API capture + UI                                │
│                                                                             │
│  SQL: visitors ───────────────────────────────────────────────────────────│
│  CREATE TABLE visitors (                                                     │
│      id TEXT PRIMARY KEY,                                                   │
│      clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE, │
│      email TEXT,                                                           │
│      first_name TEXT,                                                      │
│      last_name TEXT,                                                       │
│      session_token TEXT,                      -- último token de sesión    │
│      metadata JSONB DEFAULT '{}',                -- datos extra             │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW(),                          │
│      last_seen_at TIMESTAMP NOT NULL DEFAULT NOW()                         │
│  );                                                                        │
│  CREATE INDEX visitors_clone_idx ON visitors(clone_id);                     │
│  CREATE INDEX visitors_email_idx ON visitors(email);                        │
│                                                                             │
│  DRIZZLE SCHEMA ──────────────────────────────────────────────────────────│
│  export const visitors = pgTable("visitors", {                             │
│    id: text("id").primaryKey(),                                           │
│    cloneId: text("clone_id").notNull().references(() => clones.id),        │
│    email: text("email"),                                                   │
│    firstName: text("first_name"),                                         │
│    lastName: text("last_name"),                                           │
│    sessionToken: text("session_token"),                                   │
│    metadata: json("metadata").$type<Record<string,any>>().default({}),     │
│    createdAt: timestamp("created_at").notNull().defaultNow(),             │
│    lastSeenAt: timestamp("last_seen_at").notNull().defaultNow(),           │
│  }, (table) => [                                                          │
│    index("visitors_clone_idx").on(table.cloneId),                        │
│    index("visitors_email_idx").on(table.email),                            │
│  ]);                                                                      │
│                                                                             │
│  API ENDPOINTS ───────────────────────────────────────────────────────────│
│  POST /api/myownclone/public/clones/{slug}/capture-lead                    │
│       Body: {session_token, email, first_name, last_name}                  │
│       → Crea/actualiza visitor + asocia a conversación                    │
│                                                                             │
│  GET  /api/visitors   (proxy → /console/api/myownclone/visitors)         │
│       → Lista visitors para clone activo                                   │
│                                                                             │
│  FRONTEND: resumen/page.tsx ──────────────────────────────────────────────│
│  - Contador de mensajes del usuario en la sesión                          │
│  - Después de 3 mensajes del usuario: mostrar popup de captura           │
│  - POST a /capture-lead con session_token + email                         │
│  - Mostrar en /analiticas (nuevo tab "Visitors")                         │
│                                                                             │
│  WORKFLOWS ───────────────────────────────────────────────────────────────│
│  ▸ PRIORIDAD: 🟡 MEDIA — ALTO esfuerzo, complejidad alta                 │
│  ▸ MyClone tiene: interview-style workflows con steps secuenciales        │
│  ▸ MyOwnClone NO tiene → implementar si hay demanda                      │
│                                                                             │
│  SQL: 4 tablas ──────────────────────────────────────────────────────────│
│  workflow_templates     → templates predefinidos por industria            │
│  persona_workflows      → workflow activo por clone                       │
│  workflow_sessions      → sesión activa de un workflow                    │
│  workflow_answers       → respuestas a cada paso                         │
│                                                                             │
│  workflow_config example (MyClone):                                        │
│  {                                                                          │
│    "objectives": [                                                         │
│      { "id": "step-1", "type": "question",                               │
│        "question": "¿Cuál es tu situación fiscal?",                        │
│        "required": true, "next_step_on_answer": "step-2" },               │
│      { "id": "step-2", "type": "question",                               │
│        "question": "¿Tienes empleados o eres freelancer?",               │
│        "required": true, "next_step_on_answer": "step-3" },              │
│      { "id": "step-3", "type": "advice",                                 │
│        "objective": "Generar recomendación fiscal personalizada" }        │
│    ],                                                                      │
│    "output_template": {                                                    │
│      "format": "lead_summary",                                             │
│      "sections": ["profile", "situation", "need", "score", "follow_up"]  │
│    }                                                                       │
│  }                                                                          │
│                                                                             │
│  ESFUERZO COMPARATIVO ───────────────────────────────────────────────────│
│  ┌──────────────┬──────────────┬─────────────────────────────────────────┐ │
│  │ Feature      │ Esfuerzo     │ Notas                                   │ │
│  ├──────────────┼──────────────┼─────────────────────────────────────────┤ │
│  │ Visitors     │ BAJO (1 día) │ 1 tabla + 2 endpoints + popup frontend  │ │
│  │ Workflows    │ ALTO (1 sem) │ 4 tablas + UI builder + state machine  │ │
│  └──────────────┴──────────────┴─────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-07 │ Steps 4-5: Bug Fixes + Langfuse

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-07                              Steps 4 & 5: Bug Fixes + Langfuse       │
│ pop-laboratory · teal/sage       Prerequisitos + Observabilidad            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BUG FIXES (STEP 4) ──────────────────────────────────────────────────────│
│                                                                             │
│  FIX-01: Enum Mismatch "pedagogy" → "teach"                                │
│  ─────────────────────────────────────────────────────────────────────────│
│  SQL:                                                                      │
│    ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP;          │
│    UPDATE clone_mode_prompts SET mode = 'teach' WHERE mode = 'pedagogy';  │
│                                                                             │
│  TypeScript (src/lib/db/schema/clones.ts):                                 │
│    export const cloneModeEnum = pgEnum("clone_mode", [                     │
│      "teach",    // ✅ Corregido (era "pedagogy")                          │
│      "support",                                                              │
│      "sales",                                                               │
│    ]);                                                                      │
│                                                                             │
│  FIX-02: updatedAt en cloneModePrompts (Drizzle)                           │
│  ─────────────────────────────────────────────────────────────────────────│
│  TypeScript:                                                                │
│    updatedAt: timestamp("updated_at").notNull().defaultNow(),              │
│                                                                             │
│  SQL:                                                                       │
│    ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP;         │
│                                                                             │
│  FIX-03: Campo title en Memorias                                           │
│  ─────────────────────────────────────────────────────────────────────────│
│  Python (api/controllers/console/myownclone/creator_memory.py):             │
│    class MemoryPayload(BaseModel):                                          │
│        clone_id: str                                                        │
│        type: str = Field(..., pattern="^(memory|signature|template)$")    │
│        title: str = Field(..., min_length=1)        # ✅ AÑADIR           │
│        content: str = Field(..., min_length=1)                             │
│        trigger_condition: str | None                                       │
│        priority: int = Field(default=0)                                    │
│                                                                             │
│  También actualizar _serialize_memory() para incluir title en response.    │
│                                                                             │
│  FIX-04: updatedAt en memories (Drizzle vs SQLAlchemy)                     │
│  ─────────────────────────────────────────────────────────────────────────│
│  SQLAlchemy (api/models/myownclone/__init__.py → CreatorMemory):          │
│    # Verificar que CreatorMemory hereda updated_at de DefaultFieldsDCMixin │
│    # Si no lo tiene, añadir: updated_at: Mapped[datetime]                   │
│                                                                             │
│  LANGFUSE (STEP 5) ───────────────────────────────────────────────────────│
│  ▸ PRIORIDAD: 🔵 MEDIA — Observabilidad de producción                     │
│  ▸ Install: pip install langfuse                                           │
│  ▸ ENV: LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY + LANGFUSE_HOST         │
│                                                                             │
│  INTEGRACIÓN ─────────────────────────────────────────────────────────────│
│  # En api/core/myownclone/email_ai.py y retrieval.py                       │
│  from langfuse import Langfuse                                             │
│                                                                             │
│  langfuse = Langfuse(                                                      │
│      public_key=os.environ["LANGFUSE_PUBLIC_KEY"],                          │
│      secret_key=os.environ["LANGFUSE_SECRET_KEY"],                        │
│      host=os.environ.get("LANGFUSE_HOST", "https://cloud.langfuse.com")    │
│  )                                                                          │
│                                                                             │
│  # Tracing de cada prompt:                                                 │
│  langfuse.trace(                                                           │
│      name="clone-chat",                                                     │
│      metadata={"clone_id": clone_id, "mode": silo.value, "tenant": tenant} │
│  ) as trace:                                                               │
│      span = trace.span(name="llm-inference")                               │
│      response = model_instance.invoke_llm(prompt=full_prompt)              │
│      span.end(output=response)                                             │
│                                                                             │
│  ENDPOINTS OPCIONALES ────────────────────────────────────────────────────│
│  POST /api/v1/langfuse/prompts/create    → crear prompt en Langfuse       │
│  GET  /api/v1/langfuse/prompts/list       → listar prompts                │
│  PUT  /api/v1/langfuse/prompts/update/{name} → actualizar                 │
│  GET  /api/v1/langfuse/prompts/get/{name} → obtener con versión           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-08 │ Glosario de Archivos

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-08                              Glosario: Archivos + Cambios            │
│ pop-laboratory · charcoal brown    Backend Flask + Frontend Next.js        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  BACKEND FLASK ───────────────────────────────────────────────────────────│
│  /home/haxth3/myownclone_local/api/                                        │
│                                                                             │
│  api/models/clone.py                                                        │
│  ▸ Define: CloneConfig, CloneModePrompt, CloneSilo                        │
│  ⚠️  Cambios: +PromptVersion model +PromptVariable model                   │
│                                                                             │
│  api/controllers/console/myownclone/clone.py                                 │
│  ▸ CRUD clones + CloneModePrompt (GET/POST/PUT)                            │
│  ⚠️  Cambios: +history endpoint, +restore endpoint, +diff endpoint        │
│              +_save_prompt_version(), +_generate_change_summary()          │
│                                                                             │
│  api/controllers/console/myownclone/creator_memory.py                       │
│  ▸ CRUD memorias/signatures/templates                                       │
│  ⚠️  Cambios: +campo title a MemoryPayload +_serialize_memory title       │
│                                                                             │
│  api/controllers/myownclone_public.py                                       │
│  ▸ Chat público (POST /public/clones/{slug}/chat)                         │
│  ▸ Inbound email, booking                                                  │
│  ⚠️  Cambios: +POST /public/clones/{slug}/capture-lead                    │
│                                                                             │
│  api/core/retrieval.py                                                     │
│  ▸ SiloRetrievalResult + retrieve_from_silo()                              │
│  ⚠️  Probablemente NO tocar                                                 │
│                                                                             │
│  api/core/myownclone/email_ai.py                                            │
│  ▸ classify_email() + generate_draft_reply()                               │
│  ⚠️  Cambios: +Langfuse tracing                                            │
│                                                                             │
│  FRONTEND NEXT.JS ────────────────────────────────────────────────────────│
│  /home/haxth3/MyOwnClone/MyOwnClone/src/                                  │
│                                                                             │
│  src/lib/db/schema/clones.ts                                               │
│  ▸ cloneConfigs + cloneModePrompts (Drizzle)                               │
│  ⚠️  Cambios: +promptVersions, +promptVariables, fix enum "teach"         │
│              +updatedAt en cloneModePrompts                                │
│                                                                             │
│  src/lib/db/schema/analytics.ts                                            │
│  ▸ memories, analyticsQuestions, products, visitors                        │
│  ⚠️  Cambios: +visitors, +updatedAt en cloneModePrompts                   │
│                                                                             │
│  src/app/(dashboard)/cerebro/page.tsx                                      │
│  ▸ Editor memories/signatures/templates + tab Historial                     │
│  ⚠️  Cambios: +4to tab "Historial", +diff modal, +restaurar UI            │
│                                                                             │
│  src/app/api/clone/memories/route.ts                                      │
│  ▸ GET/POST memories (usa Drizzle directo — NO pasa por proxy.ts)        │
│  ⚠️  Cambios: +campo title en POST body validation                        │
│                                                                             │
│  src/proxy.ts                                                              │
│  ▸ Mapeo /api/* → Flask backend                                           │
│  ⚠️  Cambios: +"/api/visitors" → "/console/api/myownclone/visitors"       │
│              +"/api/clone/memories/{id}" → Drizzle route ya existe        │
│                                                                             │
│  ORDEN DE IMPLEMENTACIÓN COMPLETO ────────────────────────────────────────│
│  ┌────┬────────────────────────────────────┬────────────────────────────┐  │
│  │    │ Paso                              │ Archivos                   │  │
│  ├────┼────────────────────────────────────┼────────────────────────────┤  │
│  │ 0  │ Bug Fixes (Step 4)                │ clone.py, creator_memory,  │  │
│  │    │ ⚠️ Ejecutar PRIMERO               │ analytics.ts, clones.ts    │  │
│  ├────┼────────────────────────────────────┼────────────────────────────┤  │
│  │ 1  │ Prompt Versioning (Step 1)        │ clone.py, clones.ts,       │  │
│  │    │                                  │ cerebro/page.tsx           │  │
│  ├────┼────────────────────────────────────┼────────────────────────────┤  │
│  │ 2  │ Visitors (Step 2)                 │ analytics.ts,              │  │
│  │    │                                  │ myownclone_public.py,      │  │
│  │    │                                  │ proxy.ts, resumen/page.tsx │  │
│  ├────┼────────────────────────────────────┼────────────────────────────┤  │
│  │ 3  │ Workflows (Step 3)               │ 4 tablas nuevas + UI       │  │
│  │    │                                  │ builder complejo            │  │
│  ├────┼────────────────────────────────────┼────────────────────────────┤  │
│  │ 4  │ Langfuse (Step 5)                │ email_ai.py, retrieval.py  │  │
│  └────┴────────────────────────────────────┴────────────────────────────┘  │
│                                                                             │
│  DEV ENVIRONMENT ──────────────────────────────────────────────────────────│
│  Backend:  cd /home/haxth3/myownclone_local/api && python -m api.app_factory │
│             → http://127.0.0.1:5001                                         │
│  Frontend: cd /home/haxth3/MyOwnClone/MyOwnClone && npm run dev            │
│             → http://localhost:3000                                         │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-09 │ MyClone vs MyOwnClone — Comparativa Final

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-09                              MyClone vs MyOwnClone                    │
│ pop-laboratory · teal/pink         Variables + Features Exclusivas          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  FEATURES EXCLUSIVAS MYCLONE ─────────────────────────────────────────────│
│  ▸ Prompt versioning visual con timeline + compare + restore               │
│  ▸ Variables de prompt estructuradas: role, company, introduction, etc.    │
│  ▸ Workflows interview-style con steps secuenciales y lead scoring        │
│  ▸ 227 endpoints de API documentados                                      │
│  ▸ Voice cloning con Cartesia + ElevenLabs + LiveKit                       │
│  ▸ Monetización Stripe Connect por persona                                │
│  ▸ Langfuse integrado para tracing de prompts                              │
│  ▸ 96,891 embeddings en Voyage AI                                         │
│                                                                             │
│  FEATURES EXCLUSIVAS MYOWNCLONE ──────────────────────────────────────────│
│  ▸ Modos "teach" / "support" / "sales" como enum separados               │
│  ▸ Memories / signatures / templates (CRUD completo — MyClone NO tiene)    │
│  ▸ conversations.visitor_id (tracking de leads —MyClone tiene visitors)    │
│  ▸ Persona como "clone" con tono y comportamiento configurable            │
│  ▸ email inbound AI (classify + draft reply)                              │
│  ▸ Retrieve from silo con post-filter por context_id                      │
│  ▸ SiloRetrievalResult con scores de relevancia                            │
│                                                                             │
│  VENTAJAS COMPETITIVAS MYOWNCLONE ───────────────────────────────────────│
│  ▸ Modo multi-silo (pedagógico/soporte/ventas) → mayor flexibilidad      │
│  ▸ Memories completo → contexto persistente sin reentrenamiento            │
│  ▸ Visitor tracking → leads sin necesidad de CRM externo                   │
│  ▸ Email AI → automatización de respuesta inbound                          │
│  ▸ Arquitectura abierta (Dify como RAG) → no lock-in de proveedor         │
│                                                                             │
│  GAPS A CERRAR EN MYOWNCLONE ────────────────────────────────────────────│
│  ▸ Prompt versioning (Step 1) → igualar MyClone                          │
│  ▸ Variables estructuradas (futuro) → role, company, introduction...     │
│  ▸ Workflows (Step 3) → feature diferenciador de MyClone                │
│  ▸ Visitor UI (Step 2) → hacer usable el visitor tracking existente     │
│                                                                             │
│  DATOS CLAVE MYCLONE ────────────────────────────────────────────────────│
│  ▸ 227 endpoints de API                                                   │
│  ▸ 96,891 embeddings en Voyage AI                                         │
│  ▸ Free tier: 2 personas máx, 500 mensajes, 10 min voz                    │
│  ▸ Pro: 3 personas | Business: 30 personas | Enterprise: ∞               │
│  ▸ Servicios: Langfuse + Cartesia + ElevenLabs + LiveKit + Stripe        │
│                                                                             │
│  STACK TECNOLÓGICO ──────────────────────────────────────────────────────│
│  ┌───────────────┬─────────────────────┬─────────────────────────────────┐ │
│  │ Componente    │ MyClone             │ MyOwnClone                      │ │
│  ├───────────────┼─────────────────────┼─────────────────────────────────┤ │
│  │ Backend       │ Python + Uvicorn    │ Python Flask                    │ │
│  │ Frontend      │ ?                   │ Next.js + TypeScript            │ │
│  │ ORM           │ ?                   │ Drizzle (frontend) + SQLAlchemy │ │
│  │ RAG           │ Voyage AI          │ Dify (vector DB)                │ │
│  │ Voice         │ Cartesia + ElevenLabs│ Por implementar                │ │
│  │ Observabilidad│ Langfuse            │ Por implementar (Step 5)        │ │
│  │ Payments      │ Stripe Connect      │ Stripe Checkout (existente)     │ │
│  │ Streaming     │ Vercel AI SDK (SSE)│ model_instance.invoke_llm_stream│ │
│  └───────────────┴─────────────────────┴─────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## SEC-10 │ Migration SQL — Script Completo

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SEC-10                              Migration SQL Completa                 │
│ pop-laboratory · #FFF200 highlight   Ejecutar en orden — 5 fases           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  -- ─────────────────────────────────────────────────────────────────────── │
│  -- FASE 0: Bug Fixes (Step 4) — EJECUTAR PRIMERO                         │
│  -- ─────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  -- Fix BUG-01: Enum mismatch "pedagogy" → "teach"                        │
│  -- ⚠️  CRÍTICO: Hacer ANTES de cualquier sync entre Drizzle y SQLAlchemy │
│  ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP;           │
│  UPDATE clone_mode_prompts SET mode = 'teach' WHERE mode = 'pedagogy';   │
│  UPDATE clone_mode_prompts SET updated_at = COALESCE(updated_at, created_at)│
│   WHERE updated_at IS NULL;                                                │
│                                                                             │
│  -- Fix BUG-02: updatedAt ya añadido arriba                               │
│  -- Fix BUG-04: updatedAt en memories (verificar que existe)              │
│  ALTER TABLE memories ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP;       │
│                                                                             │
│  -- ─────────────────────────────────────────────────────────────────────── │
│  -- FASE 1: Prompt Versioning (Step 1)                                     │
│  -- ─────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS prompt_versions (                               │
│      id TEXT PRIMARY KEY,                                                  │
│      clone_id TEXT NOT NULL,                                               │
│      mode TEXT NOT NULL,                                                   │
│      version_number INTEGER NOT NULL,                                       │
│      system_prompt TEXT NOT NULL,                                          │
│      change_summary TEXT,                                                   │
│      created_by TEXT,                                                       │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW(),                           │
│      CONSTRAINT prompt_versions_clone_mode_version_uniq                     │
│          UNIQUE (clone_id, mode, version_number)                           │
│  );                                                                        │
│                                                                             │
│  CREATE INDEX IF NOT EXISTS prompt_versions_clone_idx                       │
│      ON prompt_versions(clone_id);                                         │
│  CREATE INDEX IF NOT EXISTS prompt_versions_clone_mode_idx                 │
│      ON prompt_versions(clone_id, mode);                                   │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS prompt_variables (                              │
│      id TEXT PRIMARY KEY,                                                   │
│      version_id TEXT NOT NULL,                                             │
│      variable_name TEXT NOT NULL,                                          │
│      variable_value TEXT,                                                   │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW()                            │
│  );                                                                        │
│                                                                             │
│  -- Migrar prompts existentes a versión 1                                   │
│  INSERT INTO prompt_versions                                               │
│      (id, clone_id, mode, version_number, system_prompt, created_at)        │
│  SELECT                                                                      │
│      uuid_generate_v4(),                                                   │
│      clone_id,                                                             │
│      mode,                                                                 │
│      1,                                                                    │
│      system_prompt,                                                         │
│      COALESCE(updated_at, created_at)                                      │
│  FROM clone_mode_prompts                                                   │
│  WHERE is_active = TRUE                                                   │
│  ON CONFLICT (clone_id, mode, version_number) DO NOTHING;                  │
│                                                                             │
│  -- ─────────────────────────────────────────────────────────────────────── │
│  -- FASE 2: Visitors (Step 2)                                               │
│  -- ─────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS visitors (                                       │
│      id TEXT PRIMARY KEY,                                                   │
│      clone_id TEXT NOT NULL,                                               │
│      email TEXT,                                                           │
│      first_name TEXT,                                                      │
│      last_name TEXT,                                                       │
│      session_token TEXT,                                                   │
│      metadata JSONB DEFAULT '{}',                                           │
│      created_at TIMESTAMP NOT NULL DEFAULT NOW(),                           │
│      last_seen_at TIMESTAMP NOT NULL DEFAULT NOW()                          │
│  );                                                                        │
│                                                                             │
│  CREATE INDEX IF NOT EXISTS visitors_clone_idx                              │
│      ON visitors(clone_id);                                                 │
│  CREATE INDEX IF NOT EXISTS visitors_email_idx                               │
│      ON visitors(email);                                                    │
│                                                                             │
│  -- ─────────────────────────────────────────────────────────────────────── │
│  -- FASE 3: Workflows (Step 3) — OPCIONAL                                  │
│  -- ─────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS workflow_templates (                             │
│      id TEXT PRIMARY KEY,                                                   │
│      template_key TEXT NOT NULL UNIQUE,                                     │
│      template_name TEXT NOT NULL,                                           │
│      template_category TEXT NOT NULL,                                        │
│      workflow_type TEXT NOT NULL,                                           │
│      minimum_plan_tier_id INTEGER DEFAULT 0,                                 │
│      workflow_config JSONB NOT NULL,                                        │
│      output_template JSONB,                                                 │
│      is_active BOOLEAN DEFAULT TRUE,                                        │
│      created_at TIMESTAMP DEFAULT NOW(),                                     │
│      updated_at TIMESTAMP DEFAULT NOW()                                      │
│  );                                                                        │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS persona_workflows (                              │
│      id TEXT PRIMARY KEY,                                                   │
│      clone_id TEXT NOT NULL,                                               │
│      template_id TEXT,                                                      │
│      workflow_config JSONB NOT NULL,                                        │
│      is_customized BOOLEAN DEFAULT FALSE,                                   │
│      published_at TIMESTAMP,                                                │
│      synced_version INTEGER DEFAULT 1,                                      │
│      created_at TIMESTAMP DEFAULT NOW(),                                     │
│      updated_at TIMESTAMP DEFAULT NOW()                                      │
│  );                                                                        │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS workflow_sessions (                              │
│      id TEXT PRIMARY KEY,                                                   │
│      workflow_id TEXT NOT NULL,                                             │
│      visitor_id TEXT,                                                       │
│      status TEXT DEFAULT 'active',                                          │
│      current_step INTEGER DEFAULT 0,                                        │
│      session_data JSONB DEFAULT '{}',                                       │
│      created_at TIMESTAMP DEFAULT NOW(),                                     │
│      updated_at TIMESTAMP DEFAULT NOW()                                      │
│  );                                                                        │
│                                                                             │
│  CREATE TABLE IF NOT EXISTS workflow_answers (                               │
│      id TEXT PRIMARY KEY,                                                   │
│      session_id TEXT NOT NULL,                                              │
│      step_index INTEGER NOT NULL,                                           │
│      question TEXT NOT NULL,                                                │
│      answer TEXT,                                                           │
│      created_at TIMESTAMP DEFAULT NOW()                                      │
│  );                                                                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Resumen Ejecutivo

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  RESUMEN                                                                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  INVESTIGACIÓN                                                               ║
║  ▸ MyClone.is: 227 endpoints, prompt versioning completo, 96,891 embeddings ║
║  ▸ Credenciales: xoyigo3386@disiok.com / 2cji!6Tbhc3RLp@                    ║
║                                                                              ║
║  BUGS CRÍTICOS (resolver primero)                                            ║
║  🔴 BUG-01: "pedagogy" ≠ "teach" — enum mismatch Flask/Drizzle               ║
║  🔴 BUG-03: title en memorias se pierde — Flask ignora el campo             ║
║  🟡 BUG-02: updatedAt faltante en cloneModePrompts (Drizzle)                ║
║  🟡 BUG-04: updatedAt drift entre Drizzle y SQLAlchemy                      ║
║                                                                              ║
║  PLAN DE 5 PASOS                                                              ║
║  Step 1 (🔴 ALTA):  Prompt Versioning — snapshots + diff + restore          ║
║  Step 2 (🟢 ALTA):  Visitors — tabla + capture-lead + popup post-chat       ║
║  Step 3 (🟡 MEDIA): Workflows — 4 tablas + UI builder (si hay demanda)      ║
║  Step 4 (🔴 CRÍTICO): Bug Fixes — enum + title + updatedAt (ejecutar 1ro)   ║
║  Step 5 (🔵 MEDIA):  Langfuse — tracing de prompts en producción            ║
║                                                                              ║
║  ARCHIVOS PRINCIPALES                                                        ║
║  ▸ api/models/clone.py           → PromptVersion model                      ║
║  ▸ api/controllers/.../clone.py  → history/restore/diff endpoints           ║
║  ▸ api/controllers/.../creator_memory.py → +campo title                     ║
║  ▸ src/lib/db/schema/clones.ts  → fix enum + promptVersions                ║
║  ▸ src/app/(dashboard)/cerebro/page.tsx → Tab historial + diff/restore UI  ║
║                                                                              ║
║  FUENTE                                                                     ║
║  ▸ api.myclone.is (OpenAPI + curl testing)                                  ║
║  ▸ /home/haxth3/myownclone_local/api/ (Flask backend)                       ║
║  ▸ /home/haxth3/MyOwnClone/MyOwnClone/src/ (Next.js frontend)              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

*Documento preparado para handover a otro LLM implementador.*
*No requiere acceso a internet ni credenciales adicionales.*
*Toda la información está en el código local y en la API de MyClone ya explorada.*
*Fecha: 2026-06-24*
