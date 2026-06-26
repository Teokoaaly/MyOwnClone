# MyOwnClone — Informe Completo de OSINT e Implementación
## Basado en investigación profunda de MyClone.is + análisis del código existente

**Fecha:** 2026-06-24  
**Investigación:** MyClone.is API (api.myclone.is) + código MyOwnClone  
**Credenciales test MyClone:** xoyigo3386@disiok.com / 2cji!6Tbhc3RLp@  
**Repo MyOwnClone local:** `/home/haxth3/myownclone_local/` (Flask) + `/home/haxth3/MyOwnClone/MyOwnClone/` (Next.js)

---

## PARTE 1: Análisis de MyClone.is (Competidor)

### 1.1 API Pública — Endpoints Descubiertos

**Base URL:** `https://api.myclone.is`  
**Total endpoints documentados:** 227 (OpenAPI 1.0.0)  
**Stack:** Python + Uvicorn (ASGI) en AWS

#### Autenticación (funcionando)
```bash
# Login — SUCCESS
curl -X POST https://api.myclone.is/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"xoyigo3386@disiok.com","password":"2cji!6Tbhc3RLp@"}'

# Response:
{
  "message": "Login successful",
  "user_id": "2021aa30-cdf1-465b-98d6-03896a252861",
  "token": "eyJhbGc...",
  "account_type": "creator"
}
```

#### Endpoints más importantes

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/v1/personas/username/{username}/stream-chat` | Bearer | Chat SSE streaming |
| POST | `/api/v1/personas/username/{username}/init-session` | Bearer | Inicia sesión chat |
| GET | `/api/v1/personas/{persona_id}` | Bearer | Detalles persona |
| GET | `/api/v1/personas/{persona_id}/knowledge-sources` | Bearer | Fuentes de conocimiento |
| GET | `/api/v1/knowledge-library/users/{user_id}` | Bearer | Biblioteca completa |
| GET | `/api/v1/prompt/persona-prompts/{persona_id}/history` | Bearer | Historial versiones prompt |
| POST | `/api/v1/prompt/persona-prompts/{persona_id}/restore/{version}` | Bearer | Restaurar versión |
| GET | `/api/v1/prompt/persona-prompts/{persona_id}/compare` | Bearer | Comparar versiones |
| GET | `/api/v1/prompt/persona-prompts/{persona_id}/timeline` | Bearer | Línea temporal |
| GET | `/api/v1/prompt/persona-prompts/{persona_id}/versions` | Bearer | Todas las versiones |
| POST | `/api/v1/prompt-templates/` | Bearer | Crear template |
| GET | `/api/v1/embeddings/stats` | Bearer | Stats embeddings: 96,891 |
| GET | `/api/v1/personas/{id}/visitors` | Bearer | Lista de leads |
| POST | `/api/v1/sessions/{token}/capture-lead` | Bearer | Capturar email post-chat |
| POST | `/api/v1/workflows` | Bearer | Crear workflow |
| POST | `/api/v1/workflows/sessions` | Bearer | Iniciar sesión workflow |
| POST | `/api/v1/workflows/sessions/{id}/answer` | Bearer | Responder paso workflow |
| POST | `/api/v1/stripe/personas/{id}/monetization` | Bearer | Activar monetización |
| POST | `/api/v1/livekit/connection-details` | Bearer | Credenciales LiveKit |
| GET | `/api/v1/tier/plans` | No | Planes y límites |
| GET | `/api/v1/workflow-templates` | No | Templates workflow |

#### Plans/Tiers verificados
```json
{
  "free":    { "max_personas": 2, "max_custom_domains": 0 },
  "pro":     { "max_personas": 3, "max_custom_domains": 10 },
  "business":{ "max_personas": 30, "max_custom_domains": 10 },
  "enterprise": {"max_personas": -1, "max_custom_domains": -1 }
}
```

#### Free tier limits (verificados)
```json
{
  "personas": { "used": 1, "limit": 2 },
  "text": { "messages_limit": 500 },
  "voice": { "minutes_limit": 10 }
}
```

### 1.2 Sistema de Prompts de MyClone

#### Prompt Template Structure (extraído completo)
El prompt de MyClone usa variables tipo `{{variable}}` y tiene:

```
# Expert Digital Persona System Instructions

You are {name}, {role} at {company}, {description}...

## Core Identity & Expertise
**Professional Background:** {introduction}
**Primary Expertise Areas:** {area_of_expertise}
**Communication Objective:** {chat_objective}

## Behavioral Framework
- Stateful Interaction (usa historial de conversación completo)
- Progressive Disclosure (comienza con preguntas de evaluación)
- Solution Reasoning (recolecta datos antes de recomendar)
- Evidence-Based Responses (referencia contexto pasado)

## Expertise Boundaries
{area_of_expertise + trigger topics + out-of-scope}

## Communication Style
{thinking_style: practical + authentic | systems thinking | story-driven}

## Response Structure
1. Assessment Phase: targeted questions
2. Information Gathering: progressive disclosure
3. Solution Reasoning: analysis
4. Recommendation Delivery: actionable advice
5. Experience Integration: analogies

## Conversation Guidelines
- Start with single discovery question
- Ask follow-up questions building on previous answers
- NO markdown formatting in responses
- Human-like, friendly, casual tone
```

#### Variables del Prompt System
- `{name}` — nombre del experto
- `{role}` — cargo profesional
- `{company}` — empresa
- `{description}` — descripción general
- `{introduction}` — texto de introducción
- `{area_of_expertise}` — áreas de conocimiento
- `{chat_objective}` — objetivo de la conversación
- `{thinking_style}` — estilo de comunicación
- `{objective_response}` — patrones de buena respuesta
- `{example_responses}` — ejemplos

#### Prompt Versioning API (el más importante)
```
GET  /api/v1/prompt/persona-prompts/{persona_id}/history
     → [{version_number, created_at, change_summary, created_by}]

POST /api/v1/prompt/persona-prompts/{persona_id}/restore/{version}
     → restaura versión específica

GET  /api/v1/prompt/persona-prompts/{persona_id}/timeline
     → línea temporal visual

GET  /api/v1/prompt/persona-prompts/{persona_id}/compare?v1=X&v2=Y
     → diff entre versiones
```

### 1.3 Servicios Internos Descubiertos

| Servicio | Evidencia en API | Notas |
|----------|-----------------|-------|
| **Voyage AI** | `/embeddings/stats` → 96,891 | Embeddings de conocimiento |
| **Langfuse** | `/langfuse/prompts/*` | Prompt engineering y observabilidad |
| **Cartesia AI** | `/cartesia/*` | Voice cloning |
| **ElevenLabs** | `/eleven_labs/*` | Voice cloning |
| **LiveKit** | `/livekit/*` | Voz real-time |
| **Stripe Connect** | `/stripe/*` | Monetización por persona |
| **Vercel AI SDK** | SSE stream-chat | Streaming de respuestas |

---

## PARTE 2: Código MyOwnClone — Estado Actual

### 2.1 Estructura de Archivos

```
/home/haxth3/myownclone_local/api/api/
├── controllers/
│   ├── myownclone_public.py        ← público: inbound-email, chat, booking
│   └── console/myownclone/
│       ├── clone.py                ← CRUD clones + prompts (Flask)
│       ├── creator_memory.py       ← CRUD memories/signatures/templates
│       └── inbox.py
├── models/
│   ├── clone.py                    ← CloneConfig, CloneModePrompt, CreatorMemory
│   └── analytics.py                ← Feedback, CostTracking, Plan, AnalyticsQuestion
└── core/
    ├── retrieval.py                ← retrieve_from_silo() + SiloRetrievalResult
    └── myownclone/
        ├── email_ai.py             ← classify_email(), generate_draft_reply()
        └── silos.py                ← CloneSilo enum + helpers

/home/haxth3/MyOwnClone/MyOwnClone/src/
├── app/
│   ├── api/clone/memories/route.ts ← API route memories (Next.js → Drizzle)
│   └── (dashboard)/
│       ├── cerebro/page.tsx        ← Editor memories/signatures/templates (FRONTEND)
│       ├── resumen/page.tsx        ← Dashboard + chat
│       └── biblioteca/page.tsx     ← Gestión de conocimiento
└── lib/db/schema/
    ├── clones.ts                   ← cloneConfigs, cloneModePrompts (Drizzle)
    ├── analytics.ts                ← memories, analyticsQuestions, products
    └── conversations.ts            ← conversations, messages
```

### 2.2 Modelos de Datos — Estado Real

#### CloneConfig (Flask SQLAlchemy)
```python
# /home/haxth3/myownclone_local/api/api/models/clone.py
class CloneConfig(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "clone_configs"
    tenant_id: Mapped[str]            # UUID
    name: Mapped[str]
    slug: Mapped[str]                  # unique
    description: Mapped[Optional[str]]
    avatar_url: Mapped[Optional[str]]
    personality_tone: Mapped[Optional[str]]  # "friendly", "formal", etc.
    language: Mapped[str]              # default "es"
    custom_domain: Mapped[Optional[str]]
    active_modes: Mapped[Optional[str]]  # ARRAY de modos
    is_active: Mapped[bool]
```

#### CloneModePrompt (Flask SQLAlchemy)
```python
# /home/haxth3/myownclone_local/api/api/models/clone.py
class CloneModePrompt(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "clone_mode_prompts"
    clone_id: Mapped[str]
    mode: Mapped[str]                  # "teach" / "support" / "sales"
    system_prompt: Mapped[str]         # PROMPT ACTUAL — SIN HISTORIAL
    is_active: Mapped[bool]
```

#### CloneModePrompt (Drizzle — FRONTEND)
```typescript
// /home/haxth3/MyOwnClone/MyOwnClone/src/lib/db/schema/clones.ts
export const cloneModePrompts = pgTable("clone_mode_prompts", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id").notNull().references(() => clones.id),
  mode: cloneModeEnum("mode").notNull(),  // "pedagogy" | "support" | "sales"
  systemPrompt: text("system_prompt").notNull(),
  isActive: boolean("is_active").notNull().default(true),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  // NOTE: NO updatedAt field! Missing compared to SQLAlchemy version
});
```

### ⚠️ BUGS CRÍTICOS ENCONTRADOS

#### BUG 1: Inconsistencia de Enum de Modos
- **Flask (`clone.py`):** usa `CloneSilo.TEACH = "teach"`, `"support"`, `"sales"`
- **Drizzle (`clones.ts`):** usa `"pedagogy"`, `"support"`, `"sales"`
- **Conversión necesaria** al sincronizar entre ambos

#### BUG 2: Campo `updatedAt` faltante en `cloneModePrompts` (Drizzle)
- El schema Drizzle no tiene `updatedAt` en `cloneModePrompts`
- El SQLAlchemy sí lo tiene (heredado de `TypeBase`)
- Causa: drift entre base de datos y schema Drizzle

#### BUG 3: Campo `title` faltante en API de Memorias
- Frontend `creator_memory.py` envía `title` en POST (línea 53: `title: String(payload.title)`)
- Pero `MemoryPayload` en Flask (línea 21-26) NO tiene campo `title`
- El campo existe en Drizzle schema (`memories.title`)
- El modelo SQLAlchemy `CreatorMemory` NO tiene `title`
- **El campo se pierde en algún lugar del pipeline**

#### BUG 4: Campo `updatedAt` faltante en `memories` (Drizzle)
```typescript
// analytics.ts: memories table
updatedAt: timestamp("updated_at").notNull().defaultNow(),
```
- Existe en Drizzle pero NO en el modelo SQLAlchemy `CreatorMemory`
- Drift de schema

### 2.3 Pipeline de Chat Actual

```
1. POST /api/myownclone/public/clones/{slug}/chat
       ↓
2. Busca CloneConfig por slug
       ↓
3. Busca CloneModePrompt por clone_id + modo activo
       ↓
4. _add_memories_to_prompt() → append memories al system prompt
       ↓
5. retrieve_from_silo() → RAG búsqueda en dataset (Dify)
       ↓
6. Construye full_prompt = system_prompt + CONTEXT + user_message
       ↓
7. model_instance.invoke_llm_stream() → streaming SSE response
       ↓
8. SSE: data: {content: chunk} → data: [DONE]
```

### 2.4 Sistema de Modes (CloneSilo)

```python
# Flask — CloneSilo (myownclone_local/api/api/models/clone.py)
class CloneSilo(enum.StrEnum):
    TEACH   = "teach"    # Modo pedagógico
    SUPPORT = "support"  # Soporte técnico
    SALES   = "sales"   # Ventas

# Drizzle — cloneModeEnum (MyOwnClone/MyOwnClone/src/lib/db/schema/clones.ts)
export const cloneModeEnum = pgEnum("clone_mode", [
  "pedagogy",  # ≠ "teach"!
  "support",
  "sales",
])
```

**Conversión necesaria al sincronizar:**
```python
MODE_MAP = {
    "teach": "pedagogy",   # Flask → Drizzle
    "pedagogy": "teach",   # Drizzle → Flask
    "support": "support",
    "sales": "sales",
}
```

### 2.5 Default Prompts Actuales (Flask)
```python
DEFAULT_PROMPTS = {
    CloneSilo.TEACH: (
        "Eres un asistente pedagógico amable y paciente. Tu objetivo es ayudar a los "
        "estudiantes a comprender el contenido del curso. Explica los conceptos de forma "
        "clara, usa ejemplos y anima a hacer preguntas. Basa tus respuestas ÚNICAMENTE "
        "en el contenido proporcionado."
    ),
    CloneSilo.SUPPORT: (
        "Eres un agente de soporte eficiente y resolutivo. Tu objetivo es resolver dudas "
        "y problemas de los clientes de forma rápida y profesional."
    ),
    CloneSilo.SALES: (
        "Eres un asesor de ventas entusiasta pero no agresivo. Tu objetivo es ayudar a "
        "los clientes a encontrar el producto o servicio que mejor se adapte a sus necesidades."
    ),
}
```

---

## PARTE 3: Plan de Implementación Completo

### Step 1: Prompt Versioning — CRÍTICO

**Prioridad:** 🔴 ALTA  
**Esfuerzo:** Medio  
**Arquitectura:** 2 tablas nuevas + 4 endpoints + UI

#### Tabla 1: `prompt_versions` (snapshot completo)
```sql
CREATE TABLE prompt_versions (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE,
    mode TEXT NOT NULL,                        -- "teach" / "support" / "sales"
    version_number INTEGER NOT NULL,
    system_prompt TEXT NOT NULL,
    change_summary TEXT,                        -- descripción del cambio
    created_by TEXT,                           -- tenant_id o user_id
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    UNIQUE(clone_id, mode, version_number)
);
CREATE INDEX prompt_versions_clone_idx ON prompt_versions(clone_id);
CREATE INDEX prompt_versions_clone_mode_idx ON prompt_versions(clone_id, mode);
```

#### Tabla 2: `prompt_variables` (metadata del prompt)
```sql
CREATE TABLE prompt_variables (
    id TEXT PRIMARY KEY,
    version_id TEXT NOT NULL REFERENCES prompt_versions(id) ON DELETE CASCADE,
    variable_name TEXT NOT NULL,               -- "introduction", "thinking_style", etc.
    variable_value TEXT,                        -- valor de la variable
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

#### Drizzle Schema (frontend)
```typescript
// En src/lib/db/schema/clones.ts
export const promptVersions = pgTable("prompt_versions", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id").notNull().references(() => clones.id),
  mode: cloneModeEnum("mode").notNull(),
  versionNumber: integer("version_number").notNull(),
  systemPrompt: text("system_prompt").notNull(),
  changeSummary: text("change_summary"),
  createdBy: text("created_by"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
}, (table) => [
  uniqueIndex("prompt_versions_clone_mode_version_idx").on(table.cloneId, table.mode, table.versionNumber),
  index("prompt_versions_clone_idx").on(table.cloneId),
]);

export const promptVariables = pgTable("prompt_variables", {
  id: text("id").primaryKey(),
  versionId: text("version_id").notNull().references(() => promptVersions.id),
  variableName: text("variable_name").notNull(),
  variableValue: text("variable_value"),
  createdAt: timestamp("created_at").notNull().defaultNow(),
});
```

#### Archivos a Modificar

**1. `/home/haxth3/myownclone_local/api/api/models/clone.py`**
```python
# Añadir ANTES de CloneModePrompt:
class PromptVersion(DefaultFieldsDCMixin, TypeBase):
    __tablename__ = "prompt_versions"

    clone_id: Mapped[str] = mapped_column(String(36), nullable=False)
    mode: Mapped[str] = mapped_column(String(20), nullable=False)
    version_number: Mapped[int] = mapped_column(sa.Integer, nullable=False)
    system_prompt: Mapped[str] = mapped_column(LongText, nullable=False)
    change_summary: Mapped[Optional[str]] = mapped_column(LongText, nullable=True)
    created_by: Mapped[Optional[str]] = mapped_column(String(36), nullable=True)
```

**2. `/home/haxth3/myownclone_local/api/api/controllers/console/myownclone/clone.py`**

Modificar `CloneModePromptApi.put()` (línea 184-212) para:
```python
def put(self, clone_id: str):
    # ... código existente ...
    # ANTES de actualizar, guardar versión anterior
    if prompt.system_prompt != data.system_prompt:
        _save_prompt_version(
            db.session,
            clone_id=clone_id,
            mode=data.mode,
            system_prompt=prompt.system_prompt,
            change_summary=_generate_change_summary(prompt.system_prompt, data.system_prompt),
        )
    # ... resto igual ...
```

Nuevos endpoints:
```python
@console_ns.route("/myownclone/clones/<string:clone_id>/prompts/history")
class ClonePromptHistoryApi(Resource):
    def get(self, clone_id: str):
        """Lista todas las versiones de prompt para cada modo."""
        # SELECT * FROM prompt_versions
        # WHERE clone_id = clone_id ORDER BY mode, version_number DESC

@console_ns.route("/myownclone/clones/<string:clone_id>/prompts/restore/<int:version>")
class ClonePromptRestoreApi(Resource):
    def post(self, clone_id: str, version: int):
        """Restaura una versión específica."""
        # Busca prompt_versions WHERE clone_id=clone_id AND version_number=version
        # Copia system_prompt de esa versión al CloneModePrompt actual
        # Crea nueva versión con la copia (para mantener historial de restores)

@console_ns.route("/myownclone/clones/<string:clone_id>/prompts/diff")
class ClonePromptDiffApi(Resource):
    def get(self, clone_id: str):
        """Diff entre dos versiones."""
        # Params: ?v1=1&v2=3&mode=teach
        # Retorna: {old: "...", new: "...", diff: [...]}
```

**3. `/home/haxth3/MyOwnClone/MyOwnClone/src/lib/db/schema/clones.ts`**
```typescript
// Añadir promptVersions y promptVariables al export
export { cloneConfigs, cloneModePrompts, promptVersions, promptVariables, cloneModeEnum } from "./clones";
```

**4. `/home/haxth3/MyOwnClone/MyOwnClone/src/app/(dashboard)/cerebro/page.tsx`**
- Añadir 4to tab "Historial" en TABS array
- Mostrar lista de versiones agrupadas por modo
- Botón "Restaurar" en cada versión
- Modal de diff (puede usar library como `diff` de npm)

#### Función auxiliar de diff (backend)
```python
import difflib

def generate_change_summary(old: str, new: str) -> str:
    """Genera resumen de cambios entre dos versiones de prompt."""
    old_lines = old.split('\n')
    new_lines = new.split('\n')
    diff = list(difflib.unified_diff(old_lines, new_lines, lineterm=''))
    if not diff:
        return "Sin cambios"
    added = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    removed = sum(1 for l in diff if l.startswith('-') and not l.startswith('---'))
    return f"+{added} líneas añadidas, -{removed} líneas eliminadas"
```

---

### Step 2: Lead / Visitor Management — ALTA

**Prioridad:** 🔴 ALTA  
**Esfuerzo:** Bajo  

MyOwnClone YA tiene `visitorId` en la tabla `conversations` (schema Drizzle). Solo falta:

#### Tabla: `visitors`
```sql
CREATE TABLE visitors (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clone_configs(id) ON DELETE CASCADE,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    session_token TEXT,                        -- último session token usado
    metadata JSONB DEFAULT '{}',               -- cualquier dato extra
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    last_seen_at TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX visitors_clone_idx ON visitors(clone_id);
CREATE INDEX visitors_email_idx ON visitors(email);
```

#### Drizzle Schema
```typescript
// En src/lib/db/schema/analytics.ts
export const visitors = pgTable("visitors", {
  id: text("id").primaryKey(),
  cloneId: text("clone_id").notNull().references(() => clones.id),
  email: text("email"),
  firstName: text("first_name"),
  lastName: text("last_name"),
  sessionToken: text("session_token"),
  metadata: json("metadata").$type<Record<string, any>>().default({}),
  createdAt: timestamp("created_at").notNull().defaultNow(),
  lastSeenAt: timestamp("last_seen_at").notNull().defaultNow(),
}, (table) => [
  index("visitors_clone_idx").on(table.cloneId),
  index("visitors_email_idx").on(table.email),
]);
```

#### API Endpoints
```
POST /api/myownclone/public/clones/{slug}/capture-lead
     Body: {session_token, email, first_name, last_name}
     → Crea/actualiza visitor + asocia a conversación

GET  /api/visitors  (proxy → /console/api/myownclone/visitors)
     → Lista de visitors para el clone activo
```

#### Frontend: Post-Chat Lead Capture
En `resumen/page.tsx` (ChatPanel):
- Después de 3 mensajes del usuario, mostrar popup "Ingresa tu email para continuar"
- POST a `/api/myownclone/public/clones/{slug}/capture-lead`
- Mostrar en `/analiticas` tab de visitors

---

### Step 3: Workflows BETA — MEDIA

**Prioridad:** 🟡 MEDIA  
**Esfuerzo:** Alto  

Este es el feature más complejo de MyClone. Estructura:

#### Tablas
```sql
-- workflow_templates: templates predefinidos por industria
CREATE TABLE workflow_templates (
    id TEXT PRIMARY KEY,
    template_key TEXT NOT NULL UNIQUE,   -- "cpa-tax-workflow"
    template_name TEXT NOT NULL,         -- "CPA Tax Advisor"
    template_category TEXT NOT NULL,      -- "tax", "legal", "insurance"
    workflow_type TEXT NOT NULL,          -- "interview", "consultation"
    minimum_plan_tier_id INTEGER DEFAULT 0,
    workflow_config JSONB NOT NULL,        -- {objectives: [...], steps: [...]}
    output_template JSONB,                -- para lead scoring
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- persona_workflows: workflow activo por persona/clone
CREATE TABLE persona_workflows (
    id TEXT PRIMARY KEY,
    clone_id TEXT NOT NULL REFERENCES clone_configs(id),
    template_id TEXT REFERENCES workflow_templates(id),
    workflow_config JSONB NOT NULL,        -- copia del template
    is_customized BOOLEAN DEFAULT FALSE,
    published_at TIMESTAMP,
    synced_version INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- workflow_sessions: sesión activa de un workflow
CREATE TABLE workflow_sessions (
    id TEXT PRIMARY KEY,
    workflow_id TEXT NOT NULL REFERENCES persona_workflows(id),
    visitor_id TEXT REFERENCES visitors(id),
    status TEXT DEFAULT 'active',          -- "active" | "completed" | "abandoned"
    current_step INTEGER DEFAULT 0,
    session_data JSONB DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- workflow_answers: respuestas a cada paso
CREATE TABLE workflow_answers (
    id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL REFERENCES workflow_sessions(id),
    step_index INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

#### Workflow Config Structure (MyClone)
```json
{
  "objectives": [
    {
      "id": "step-1",
      "type": "question",
      "question": "¿Cuál es tu situación fiscal actual?",
      "required": true,
      "next_step_on_answer": "step-2"
    },
    {
      "id": "step-2",
      "type": "question", 
      "question": "¿Tienes empleados o eres freelancer?",
      "required": true,
      "next_step_on_answer": "step-3"
    },
    {
      "id": "step-3",
      "type": "advice",
      "objective": "Generar recomendación fiscal personalizada"
    }
  ],
  "output_template": {
    "format": "lead_summary",
    "sections": ["profile", "situation", "need", "score", "follow_up_questions"]
  }
}
```

---

### Step 4: Bug Fixes — CRÍTICO (Hacer primero!)

**Fix 1: Consistencia de Enum de Modos**
```typescript
// src/lib/db/schema/clones.ts — cambiar:
export const cloneModeEnum = pgEnum("clone_mode", [
  "teach",    // Era "pedagogy" — corregir a "teach"
  "support",
  "sales",
]);
```
⚠️ **WARNING:** Esto requiere migrate la base de datos:
```sql
UPDATE clone_mode_prompts SET mode = 'teach' WHERE mode = 'pedagogy';
```

**Fix 2: Campo `updatedAt` en `cloneModePrompts` (Drizzle)**
```typescript
// En src/lib/db/schema/clones.ts — cloneModePrompts:
updatedAt: timestamp("updated_at").notNull().defaultNow(),
// Añadir a la tabla existente — requiere ALTER TABLE
```

**Fix 3: Campo `title` en Memorias**
El frontend envía `title` pero la API no lo procesa. Opciones:
- Opción A (recomendada): Añadir `title` a `CreatorMemory` SQLAlchemy + `MemoryPayload`
- Opción B: Quitar `title` del frontend

---

### Step 5: Langfuse Integration — MEDIA

**Prioridad:** 🟡 MEDIA  
**Esfuerzo:** Medio  

Langfuse permite observar prompts en producción. Integración:

```python
# Install
pip install langfuse

# En api/core/myownclone/email_ai.py y retrieval.py:
from langfuse import Langfuse
langfuse = Langfuse(
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    host="https://cloud.langfuse.com"  # o self-hosted
)

# Tracing de cada prompt:
langfuse.trace(
    name="clone-chat",
    metadata={"clone_id": clone_id, "mode": silo.value}
) as trace:
    span = trace.span(name="llm-inference")
    response = model_instance.invoke_llm(prompt=full_prompt)
    span.end()
```

Endpoints para management:
```
POST /api/v1/langfuse/prompts/create    → crear prompt en Langfuse
GET  /api/v1/langfuse/prompts/list       → listar prompts
PUT  /api/v1/langfuse/prompts/update/{name} → actualizar
GET  /api/v1/langfuse/prompts/get/{name} → obtener con versión
```

---

## PARTE 4: Glosario de Archivos para el LLM Implementador

### Backend Flask — Archivos que tocarás

| Archivo | Qué hace | Cambios |
|---------|---------|---------|
| `api/models/clone.py` | Define `CloneConfig`, `CloneModePrompt` | Añadir `PromptVersion` |
| `api/controllers/console/myownclone/clone.py` | CRUD clones + prompts | Modificar `put()` prompts, añadir history/restore/diff |
| `api/controllers/console/myownclone/creator_memory.py` | CRUD memorias | Bugfix: añadir `title` |
| `api/controllers/myownclone_public.py` | Chat público + lead capture | Añadir `capture-lead` endpoint |
| `api/core/retrieval.py` | RAG retrieval service | Probablemente no tocar |
| `api/core/myownclone/email_ai.py` | Clasificación email + draft | Añadir tracing Langfuse |

### Frontend Next.js — Archivos que tocarás

| Archivo | Qué hace | Cambios |
|---------|---------|---------|
| `src/lib/db/schema/clones.ts` | Schema Drizzle clones | Fix modes enum, añadir promptVersions |
| `src/lib/db/schema/analytics.ts` | Schema Drizzle analytics | Añadir visitors, fix updatedAt |
| `src/app/(dashboard)/cerebro/page.tsx` | Editor memories + prompts | Añadir tab Historial + UI diff/restore |
| `src/app/api/clone/memories/route.ts` | API memories | Bugfix: title field |
| `src/proxy.ts` | Proxy rutas al backend | Añadir `/api/visitors` → backend |

### Migración de Base de Datos

```sql
-- 1. Añadir prompt_versions
ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP DEFAULT NOW();

-- 2. Fix mode enum inconsistency
UPDATE clone_mode_prompts SET mode = 'teach' WHERE mode = 'pedagogy';

-- 3. Crear visitors
CREATE TABLE visitors (...);

-- 4. Crear prompt_versions
CREATE TABLE prompt_versions (...);

-- 5. Migrar prompts existentes a versiones
INSERT INTO prompt_versions (id, clone_id, mode, version_number, system_prompt, created_at)
SELECT
    uuid_generate_v4(),
    clone_id,
    mode,
    1,
    system_prompt,
    COALESCE(updated_at, created_at)
FROM clone_mode_prompts
WHERE is_active = TRUE;
```

---

## PARTE 5: Notas Importantes para el LLM

### No reinventar la rueda
- MyOwnClone YA tiene modo "pedagogy/teach/support/sales" — esto MyClone NO lo tiene, es ventaja competitiva
- MyOwnClone YA tiene memories/signatures/templates — MyClone NO lo tiene
- MyOwnClone YA tiene visitor tracking en `conversations.visitor_id` — solo falta la UI y capture
- NO copies el prompt system de MyClone tal cual — adapta las variables `{name}`, `{role}`, etc. a los campos existentes de `CloneConfig`

### API Routes existentes del frontend (proxy.ts)
El proxy.ts en frontend mapea rutas `/api/*` a Flask:
```
/api/clones          → /console/api/myownclone/clones
/api/clone/memories  → (route.ts propio, Drizzle directo)
/api/feedback        → /console/api/myownclone/feedback
/api/inbox           → /console/api/myownclone/inbox
```

### Auth
- Backend Flask: usa `@login_required`, `@account_initialization_required`, `@setup_required` decorators
- Frontend Next.js: usa `auth()` de `@/lib/auth` (NextAuth)
- Los dos systems están desconectados actualmente — el frontend usa Drizzle directo

### Entorno local de desarrollo
```bash
# Backend
cd /home/haxth3/myownclone_local/api
python -m api.app_factory
# → http://127.0.0.1:5001

# Frontend
cd /home/haxth3/MyOwnClone/MyOwnClone
npm run dev
# → http://localhost:3000
```

### Test credentials MyClone (para referencia)
```
Email: xoyigo3386@disiok.com
Password: 2cji!6Tbhc3RLp@
User ID: 2021aa30-cdf1-465b-98d6-03896a252861
Account: creator (acceso completo)
```

### Orden de implementación recomendado
1. **Step 4 (Bug Fixes)** — Resolver inconsistencies antes de añadir features
2. **Step 1 (Prompt Versioning)** — Mayor impacto, código existente ya tiene el put()
3. **Step 2 (Lead/Visitor)** — Bajo esfuerzo, alto impacto
4. **Step 3 (Workflows)** — Solo si hay demanda de usuarios
5. **Step 5 (Langfuse)** — Producción / observabilidad

---

## PARTE 6: Inventario de Variables MyClone vs MyOwnClone

### MyClone Persona Variables
| Variable | Descripción |
|----------|-------------|
| `name` | Nombre del experto |
| `role` | Cargo profesional |
| `company` | Empresa |
| `description` | Descripción general |
| `introduction` | Texto de introducción personal |
| `area_of_expertise` | Áreas de conocimiento |
| `chat_objective` | Objetivo de la conversación |
| `thinking_style` | Estilo de comunicación |
| `objective_response` | Patrones de buena respuesta |
| `example_responses` | Ejemplos de respuestas |

### MyOwnClone CloneConfig Fields
| Campo | Tipo | Mapeo MyClone |
|-------|------|---------------|
| `name` | string | ✅ `name` |
| `description` | text | ✅ `description` |
| `role` | — | ❌ Falta |
| `company` | — | ❌ Falta |
| `personality_tone` | string | ❌ (similar a `thinking_style`) |
| `language` | string | ❌ (MyClone no tiene) |

**Gap:** MyOwnClone no tiene `role`, `company`, `introduction`, `area_of_expertise`, `chat_objective` como campos separados en `CloneConfig`.

---

*Documento preparado para handover a otro LLM. No requiere acceso a internet ni credenciales adicionales. Toda la información está en el código local y en la API de MyClone ya explorada.*
