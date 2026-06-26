# MyOwnClone — Informe Completo: MyClone OSINT + Análisis + Plan

## Overview
Informe de OSINT sobre el competidor MyClone.is y análisis profundo del código de MyOwnClone. 5 pasos priorizados de implementación con código y archivos concretos.

## Learning Objectives
1. Entender la arquitectura de MyClone.is (227 endpoints) y MyOwnClone (Flask + Next.js + Drizzle)
2. Conocer los 5 pasos de implementación priorizados con código listo para copiar
3. Identificar los 4 bugs críticos del código actual y su orden de corrección
4. Mapear las variables de prompt entre MyClone y MyOwnClone para expansión futura

---

## SEC-01: MyClone.is — API Descubierta

**Key Concept:** Competidor con 227 endpoints, prompt versioning completo, y servicios de voice/embedding

**Content:**
- **Base URL:** https://api.myclone.is — Stack: Python + Uvicorn (ASGI) en AWS
- **Autenticación:** POST /api/v1/auth/login → {user_id, token, account_type: "creator"}
- **Total endpoints:** 227 (OpenAPI 1.0.0)
- **Chat:** POST /api/v1/personas/username/{username}/stream-chat — SSE streaming con historial
- **Prompt Versioning:** GET history → POST restore/{version} → GET compare → GET timeline
- **Embeddings:** Voyage AI con 96,891 vectors indexados
- **Servicios internos:** Langfuse (tracing), Cartesia AI (voice), ElevenLabs (voice cloning), LiveKit (real-time voice), Stripe Connect (monetización)
- **Tiers verificados:** Free (2 personas máx), Pro (3), Business (30), Enterprise (-1)
- **Workflows:** interview-style con steps secuenciales y lead scoring output

**Visual Element:**
- Type: module array with icons
- Subject: servicios API y sus conexiones
- Treatment: coordinate grid layout con SEC-01 badge

**Text Labels:**
- Headline: "MyClone.is — 227 Endpoints"
- Subhead: "Prompt Versioning + Voice + Embeddings"
- Labels: "Langfuse", "Voyage AI 96K", "LiveKit", "Stripe Connect", "Cartesia AI"

---

## SEC-02: MyClone Prompt System

**Key Concept:** Variables estructuradas para definir comportamiento del clon, con versionado visual

**Content:**
- **Sistema de variables:** {{name}}, {{role}}, {{company}}, {{description}}, {{introduction}}, {{area_of_expertise}}, {{chat_objective}}, {{thinking_style}}, {{objective_response}}, {{example_responses}}
- **Behavioral Framework:** Stateful Interaction + Progressive Disclosure + Solution Reasoning + Evidence-Based Responses
- **Estructura del prompt:** Core Identity → Behavioral Framework → Expertise Boundaries → Communication Style → Response Structure → Conversation Guidelines
- **Prompt Versioning API:** history (versiones numeradas con change_summary) + restore (recupera versión) + compare (diff) + timeline (visual)
- **Variables MyOwnClone existentes:** name, description, personality_tone, language — FALTAN: role, company, introduction, area_of_expertise, chat_objective
- **Gap crítico:** MyClone tiene variables separadas que MyOwnClone guarda en un solo texto libre (system_prompt)

**Visual Element:**
- Type: structured breakdown
- Subject: prompt template con variables marcadas
- Treatment: blueprint grid con SEC-02 badge

**Text Labels:**
- Headline: "MyClone Prompt System"
- Subhead: "{{variable}} template + versioning completo"
- Labels: "Core Identity", "Behavioral Framework", "Expertise Boundaries", "Response Structure"

---

## SEC-03: MyOwnClone — Arquitectura Real

**Key Concept:** Stack híbrido: Flask backend + Next.js frontend + Drizzle ORM directo a DB

**Content:**
- **Backend Flask:** `/home/haxth3/myownclone_local/api/` — controllers, models, core/retrieval.py
- **Frontend Next.js:** `/home/haxth3/MyOwnClone/MyOwnClone/src/` — app/, lib/db/schema/
- **DB Direct:** Frontend usa Drizzle ORM contra PostgreSQL directamente — NO pasa por Flask API
- **Proxy:** `proxy.ts` mapea /api/* a Flask — EXCEPTO /api/clone/memories que usa Drizzle
- **Chat Pipeline:** POST chat → CloneConfig → CloneModePrompt → _add_memories_to_prompt() → retrieve_from_silo() → model_instance.invoke_llm_stream() → SSE
- **CloneSilo (Flask):** "teach" | "support" | "sales"
- **cloneModeEnum (Drizzle):** "pedagogy" | "support" | "sales" — MISMATCH CRÍTICO
- **Retrieval:** SiloRetrievalResult + retrieve_from_silo() → Dify dataset API

**Visual Element:**
- Type: architectural diagram
- Subject: flujo de datos Flask ↔ Drizzle ↔ PostgreSQL
- Treatment: structural breakdown con SEC-03 badge

**Text Labels:**
- Headline: "MyOwnClone — Stack Real"
- Subhead: "Flask + Next.js + Drizzle + Dify"
- Labels: "Flask API :5001", "Next.js :3000", "Drizzle → PostgreSQL", "Dify RAG"

---

## SEC-04: Bugs Críticos Encontrados

**Key Concept:** 4 bugs que deben resolverse antes de implementar features nuevas

**Content:**
- **BUG 1 — Enum Mismatch:** Flask CloneSilo usa "teach" pero Drizzle cloneModeEnum usa "pedagogy" → datos inconsistentes entre backend y frontend
- **BUG 2 — updatedAt faltante:** cloneModePrompts en Drizzle no tiene updatedAt (existe en SQLAlchemy heredado de TypeBase) → drift de schema
- **BUG 3 — title en Memorias:** Frontend envía title en POST pero Flask MemoryPayload no tiene campo title → se pierde el dato
- **BUG 4 — updatedAt en Memorias:** Drizzle tiene updatedAt en memories table pero CreatorMemory SQLAlchemy no lo tiene
- **Orden de fix:** BUG 1 y 3 rompen datos nyata, resolver primero → luego BUG 2 y 4

**Visual Element:**
- Type: warning/pitfall zone
- Subject: 4 bugs con severity indicators
- Treatment: red/pink alert markers en SEC-04

**Text Labels:**
- Headline: "⚠️ 4 Bugs Críticos"
- Subhead: "Resolver ANTES de implementar features"
- Labels: "BUG 1: pedagogy≠teach", "BUG 2: updatedAt drift", "BUG 3: title lost", "BUG 4: memory updatedAt"

---

## SEC-05: Plan — Step 1 Prompt Versioning

**Key Concept:** Implementar versionado de prompts como MyClone — snapshots + diff + restore

**Content:**
- **Nueva tabla prompt_versions:** clone_id, mode, version_number, system_prompt, change_summary, created_by, created_at
- **Nueva tabla prompt_variables:** version_id, variable_name, variable_value
- **Modificar CloneModePromptApi.put():** guardar versión anterior antes de actualizar
- **Endpoints nuevos:** GET /history → POST /restore/{version} → GET /diff
- **Función _generate_change_summary():** usa difflib para resumir líneas añadidas/eliminadas
- **Frontend:** 4to tab "Historial" en cerebro/page.tsx con diff modal
- **Drizzle:** añadir promptVersions + promptVariables schemas
- **Orden:** 1) Crear tablas SQL 2) Añadir modelo Python 3) Modificar put() 4) Añadir endpoints 5) UI frontend

**Visual Element:**
- Type: process/steps
- Subject: 5 pasos del implementation workflow
- Treatment: numbered steps con arrows

**Text Labels:**
- Headline: "Step 1: Prompt Versioning"
- Subhead: "Tablas + endpoints + UI diff/restore"
- Labels: "1. Tablas SQL", "2. Modelo Python", "3. Modificar put()", "4. Endpoints", "5. UI frontend"

---

## SEC-06: Plan — Step 2 Lead Visitor + Step 3 Workflows

**Key Concept:** Visitors (bajo esfuerzo, alto impacto) y Workflows (alto esfuerzo, complejidad media)

**Content:**
- **Visitors — Tabla:** visitors con id, clone_id, email, first_name, last_name, session_token, metadata JSONB, created_at, last_seen_at
- **Visitors — API:** POST /capture-lead + GET /visitors (proxy → Flask)
- **Visitors — Frontend:** popup post-chat a los 3 mensajes → captura email → muestra en /analiticas
- **Workflows — Tablas:** workflow_templates + persona_workflows + workflow_sessions + workflow_answers
- **Workflows — Config:** objectives[] con {id, type, question, required, next_step_on_answer} + output_template para lead scoring
- **Workflows — Esfuerzo:** ALTO — requiere UI builder复杂的, state machine, y session management

**Visual Element:**
- Type: scenario comparison
- Subject: visitors vs workflows effort/impact
- Treatment: comparison matrix

**Text Labels:**
- Headline: "Steps 2 & 3: Visitors + Workflows"
- Subhead: "Bajo esfuerzo vs Alto esfuerzo"
- Labels: "Visitors: 1 tabla + 2 endpoints + popup", "Workflows: 4 tablas + UI builder + state machine"

---

## SEC-07: Plan — Step 4 Bug Fixes + Step 5 Langfuse

**Key Concept:** Bug fixes son prerequisitos — Langfuse es observabilidad de producción

**Content:**
- **Bug Fix 1:** ALTER TABLE clone_mode_prompts ADD COLUMN updated_at TIMESTAMP + cambiar Drizzle enum "pedagogy" → "teach" + UPDATE SQL
- **Bug Fix 2:** Añadir updatedAt a cloneModePrompts Drizzle schema + ALTER TABLE
- **Bug Fix 3:** Añadir campo title a CreatorMemory SQLAlchemy + MemoryPayload Flask
- **Bug Fix 4:** Sincronizar updatedAt de memories entre Drizzle y SQLAlchemy
- **Langfuse — Install:** pip install langfuse
- **Langfuse — Tracing:** langfuse.trace() envolviendo cada invoke_llm con metadata {clone_id, mode}
- **Langfuse — Setup:** LANGFUSE_PUBLIC_KEY + LANGFUSE_SECRET_KEY + host en env
- **Endpoints opcionales:** POST /langfuse/prompts/create, GET /list, PUT /update/{name}

**Visual Element:**
- Type: specification scale
- Subject: 4 bugs + langfuse effort
- Treatment: checklist con priority indicators

**Text Labels:**
- Headline: "Steps 4 & 5: Bug Fixes + Langfuse"
- Subhead: "Prerequisitos + Observabilidad"
- Labels: "Fix 1: enum teach", "Fix 2: updatedAt", "Fix 3: title", "Fix 4: sync", "Langfuse: tracing"

---

## SEC-08: Glosario de Archivos

**Key Concept:** Cada archivo del codebase con su función y cambios requeridos

**Content:**
- **Backend Flask:**
  - `api/models/clone.py` → Añadir PromptVersion model
  - `api/controllers/console/myownclone/clone.py` → Modificar put() + history/restore/diff
  - `api/controllers/console/myownclone/creator_memory.py` → Bugfix: añadir title
  - `api/controllers/myownclone_public.py` → Añadir capture-lead endpoint
- **Frontend Next.js:**
  - `src/lib/db/schema/clones.ts` → Fix enum + promptVersions
  - `src/lib/db/schema/analytics.ts` → Añadir visitors + fix updatedAt
  - `src/app/(dashboard)/cerebro/page.tsx` → Tab historial + diff/restore UI
  - `src/app/api/clone/memories/route.ts` → Bugfix: title field
  - `src/proxy.ts` → Añadir /api/visitors → backend
- **Dev:** Backend :5001 + Frontend :3000 — ejecutar ambos en paralelo

**Visual Element:**
- Type: quick reference table
- Subject: archivos y cambios
- Treatment: compact table con MOD-08 badge

**Text Labels:**
- Headline: "Glosario: Archivos + Cambios"
- Subhead: "Backend Flask + Frontend Next.js"
- Labels: "clone.py: PromptVersion", "clone.py: history/restore/diff", "creator_memory.py: title", "cerebro/page.tsx: historial UI"

---

## SEC-09: Datos Clave — MyClone vs MyOwnClone

**Key Concept:** Comparativa de variables de prompt y capacidades entre ambos sistemas

**Content:**
- **MyClone tiene, MyOwnClone NO:**
  - role (cargo profesional) — campo separado
  - company (empresa) — campo separado
  - introduction (texto introductorio) — campo separado
  - area_of_expertise (áreas de conocimiento) — campo separado
  - chat_objective (objetivo de conversación) — campo separado
  - thinking_style (estilo de comunicación) — campo separado
- **MyClone NO tiene, MyOwnClone SÍ:**
  - Modos "teach" / "support" / "sales" como enum separado
  - Memories / signatures / templates (sistema completo de contexto)
  - conversations.visitor_id (tracking de leads)
- **MyClone embedding stats:** 96,891 vectors en Voyage AI
- **MyClone free tier:** 2 personas máx, 500 mensajes texto, 10 min voz

**Visual Element:**
- Type: venn diagram / comparison
- Subject: features exclusivas de cada plataforma
- Treatment: overlap zones

**Text Labels:**
- Headline: "MyClone vs MyOwnClone"
- Subhead: "Variables de prompt + features"
- Labels: "MyClone: role, company, intro, expertise, chat_objective", "MyOwnClone: modes enum, memories, visitor_id", "OVERLAP: name, description"

---

## Data Points (Verbatim)

### Statistics
- "227 endpoints" en MyClone API
- "96,891" embeddings en Voyage AI
- "500" mensajes límite en free tier MyClone
- "10" minutos voz límite en free tier MyClone
- "2" personas máximo en MyClone free tier
- "3" personas en MyClone Pro
- "30" personas en MyClone Business
- "5" steps de implementación en el plan

### Key Terms
- **CloneSilo:** Enum Flask con valores "teach" | "support" | "sales"
- **cloneModeEnum:** Enum Drizzle con valores "pedagogy" | "support" | "sales" — MISMATCH
- **SiloRetrievalResult:** Dataclass que envuelve resultados RAG con scores
- **retrieve_from_silo():** Función que busca en dataset Dify por clone_id + silo
- **invoke_llm_stream():** Método de ModelManager para streaming SSE
- **creator_memory.py:** Controller Flask para CRUD de memories/signatures/templates
- **creator_memory route.ts:** API route Next.js que usa Drizzle directamente

### Credentials (para referencia, NO incluir en output visual)
- MyClone test: xoyigo3386@disiok.com / 2cji!6Tbhc3RLp@
- MyClone user ID: 2021aa30-cdf1-465b-98d6-03896a252861

---

## Design Instructions

### Style Preferences
- pop-laboratory: blueprint grid, coordinate markers, teal/pink/yellow palette
- Background: #F2F2F2 con grid texture
- High-alert: #E91E63 para bugs y warnings
- Marker: #FFF200 para highlights
- Teal blocks: #B8D8BE para módulos funcionales

### Layout Preferences
- dense-modules: 9 módulos (SEC-01 a SEC-09)
- Cada módulo con coordinate label (SEC-01, SEC-02, etc.)
- Mínima whitespace — máxima densidad de información
- Números grandes con accent color

### Other Requirements
- Idioma: Español
- Dark blueprint aesthetic
- Prioridad: Bugs (rojo) primero, luego features
- Target: Developers/technical team
