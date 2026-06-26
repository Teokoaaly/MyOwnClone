Create a professional infographic following these specifications:

## Image Specifications

- **Type**: Infographic
- **Layout**: dense-modules
- **Style**: pop-laboratory
- **Aspect Ratio**: 16:9 (landscape)
- **Language**: es (Spanish)

## Core Principles

- Follow the dense-modules layout with 9 typed information modules (SEC-01 through SEC-09)
- Apply pop-laboratory style: blueprint grid texture, coordinate markers (SEC-01, SEC-02...), technical diagrams, teal/sage/pink/yellow palette
- Keep information dense — every corner contains useful metadata or data
- Maintain clear visual hierarchy: bold brutalist headers + small precise annotations
- Minimal whitespace — compact spacing prioritized over breathing room

## Layout Guidelines (dense-modules)

- 9 distinct modules per image, each with alphanumeric coordinate label (SEC-01, SEC-02, etc.)
- Each module contains concrete data: brand names, numbers, endpoints, file paths, parameters
- Module boundary markers: thick coordinate grid lines with ruler/axis aesthetic
- Quality indicators per module: emoji faces, checkmarks, crosses, or crown icons for priority
- Metadata in corners: timestamps, section markers, coordinate labels
- Blueprint grid background: professional grayish-white (#F2F2F2) with faint grid lines
- Numbers highlighted with lemon yellow (#FFF200) or pink (#E91E63) for critical data

## Style Guidelines (pop-laboratory)

- **Background**: #F2F2F2 with faint blueprint grid texture
- **Primary blocks**: Muted teal/sage green (#B8D8BE) for major functional sections
- **High-alert accent**: Vibrant fluorescent pink (#E91E63) for warnings, bugs, critical data, "winner" highlights
- **Marker highlights**: Vivid lemon yellow (#FFF200) as translucent highlighter for keywords
- **Line art**: Ultra-fine charcoal brown (#2D2926) for grids, coordinates, hairlines
- **Typography**: Bold brutalist headers + professional sans-serif body + large highlighted numbers
- **Coordinate labels**: Every module tagged with SEC-XX label in charcoal
- **Cross-hair targets**: Mathematical symbols (Σ, Δ, ∞), directional arrows for flow
- **Corner metadata**: Tiny section markers, timestamps, barcodes

## Content

### SEC-01: MyClone.is — API Descubierta
**Headline**: MyClone.is — 227 Endpoints
**Subhead**: Prompt Versioning + Voice + Embeddings + Stripe

**Content**:
- Base URL: https://api.myclone.is — Python + Uvicorn (ASGI) en AWS
- Auth: POST /api/v1/auth/login → {user_id, token, account_type: "creator"}
- Total: 227 endpoints documentados (OpenAPI 1.0.0)
- Chat: POST /personas/username/{username}/stream-chat — SSE streaming
- Embeddings: Voyage AI con 96,891 vectors
- Prompt Versioning: GET history → POST restore → GET compare → GET timeline
- Servicios: Langfuse, Cartesia AI, ElevenLabs, LiveKit, Stripe Connect
- Tiers: Free (2 personas), Pro (3), Business (30), Enterprise (-1)

### SEC-02: MyClone Prompt System
**Headline**: MyClone Prompt System
**Subhead**: {{variable}} template + versioning completo

**Content**:
- Variables: {name}, {role}, {company}, {description}, {introduction}, {area_of_expertise}, {chat_objective}, {thinking_style}
- Behavioral: Stateful + Progressive Disclosure + Solution Reasoning + Evidence-Based
- Prompt Versioning API: history con change_summary + restore/{version} + compare + timeline
- MyOwnClone FALTAN: role, company, introduction, area_of_expertise, chat_objective
- MyOwnClone TIENE: name, description, personality_tone, language

### SEC-03: MyOwnClone — Arquitectura Real
**Headline**: MyOwnClone — Stack Real
**Subhead**: Flask + Next.js + Drizzle + Dify

**Content**:
- Backend Flask: /home/haxth3/myownclone_local/api/ — controllers + models + core/retrieval.py
- Frontend Next.js: /home/haxth3/MyOwnClone/MyOwnClone/src/ — app/ + lib/db/schema/
- Frontend → Drizzle directo a PostgreSQL (NO pasa por Flask API)
- proxy.ts mapea /api/* a Flask — EXCEPTO /api/clone/memories (Drizzle)
- Chat Pipeline: POST chat → CloneConfig → CloneModePrompt → retrieve_from_silo() → invoke_llm_stream() → SSE
- CloneSilo (Flask): "teach" | "support" | "sales"
- cloneModeEnum (Drizzle): "pedagogy" | "support" | "sales" ⚠️ MISMATCH

### SEC-04: ⚠️ 4 Bugs Críticos
**Headline**: ⚠️ 4 Bugs Críticos
**Subhead**: Resolver ANTES de implementar features

**Content**:
- BUG 1: Enum Mismatch — Flask "teach" vs Drizzle "pedagogy" → datos inconsistentes
- BUG 2: updatedAt faltante — cloneModePrompts Drizzle sin updatedAt (existe en SQLAlchemy)
- BUG 3: title en Memorias — Frontend envía title pero Flask MemoryPayload no lo tiene
- BUG 4: updatedAt memorias — Drizzle tiene updatedAt pero CreatorMemory SQLAlchemy no
- Fix Order: BUG 1 y 3 rompen datos → resolver primero → luego BUG 2 y 4

### SEC-05: Step 1 — Prompt Versioning
**Headline**: Step 1: Prompt Versioning
**Subhead**: Tablas + endpoints + UI diff/restore

**Content**:
- Tabla prompt_versions: clone_id, mode, version_number, system_prompt, change_summary
- Tabla prompt_variables: version_id, variable_name, variable_value
- Modificar CloneModePromptApi.put(): guardar versión anterior antes de actualizar
- Nuevos endpoints: GET /history → POST /restore/{version} → GET /diff
- Función _generate_change_summary(): difflib → líneas añadidas/eliminadas
- Frontend: 4to tab "Historial" en cerebro/page.tsx con diff modal

### SEC-06: Steps 2 & 3 — Visitors + Workflows
**Headline**: Steps 2 & 3: Visitors + Workflows
**Subhead**: Bajo esfuerzo vs Alto esfuerzo

**Content**:
- Visitors — Tabla: visitors (id, clone_id, email, first_name, session_token, metadata)
- Visitors — API: POST /capture-lead + GET /visitors (proxy → Flask)
- Visitors — Frontend: popup post-chat a los 3 mensajes → captura email
- Workflows — Tablas: workflow_templates + persona_workflows + workflow_sessions + workflow_answers
- Workflows — Config: objectives[] con {id, type, question, next_step_on_answer}
- Workflows — Output: lead_summary con sections [profile, situation, need, score]
- Esfuerzo: Visitors = BAJO | Workflows = ALTO

### SEC-07: Steps 4 & 5 — Bug Fixes + Langfuse
**Headline**: Steps 4 & 5: Bug Fixes + Langfuse
**Subhead**: Prerequisitos + Observabilidad

**Content**:
- Fix 1: ALTER TABLE + cambiar enum "pedagogy" → "teach" + UPDATE SQL
- Fix 2: Añadir updatedAt a cloneModePrompts Drizzle + ALTER TABLE
- Fix 3: Añadir title a CreatorMemory SQLAlchemy + MemoryPayload Flask
- Fix 4: Sincronizar updatedAt memories entre Drizzle y SQLAlchemy
- Langfuse: pip install langfuse — LANGFUSE_PUBLIC_KEY + SECRET_KEY
- Tracing: langfuse.trace() envolviendo cada invoke_llm con metadata {clone_id, mode}
- Endpoints opcionales: POST /langfuse/prompts/create, GET /list, PUT /update/{name}

### SEC-08: Glosario de Archivos
**Headline**: Glosario: Archivos + Cambios
**Subhead**: Backend Flask + Frontend Next.js

**Content**:
- api/models/clone.py → Añadir PromptVersion model
- api/controllers/console/myownclone/clone.py → Modificar put() + history/restore/diff
- api/controllers/console/myownclone/creator_memory.py → Bugfix: añadir title
- api/controllers/myownclone_public.py → Añadir capture-lead endpoint
- src/lib/db/schema/clones.ts → Fix enum + promptVersions
- src/lib/db/schema/analytics.ts → Añadir visitors + fix updatedAt
- src/app/(dashboard)/cerebro/page.tsx → Tab historial + diff/restore UI
- src/app/api/clone/memories/route.ts → Bugfix: title field
- src/proxy.ts → Añadir /api/visitors → backend

### SEC-09: MyClone vs MyOwnClone
**Headline**: MyClone vs MyOwnClone
**Subhead**: Variables de prompt + features exclusivas

**Content**:
- MyClone TIENE: role, company, introduction, area_of_expertise, chat_objective, thinking_style
- MyOwnClone TIENE: modes (teach/support/sales), memories/signatures/templates, visitor_id
- MyClone embedding stats: 96,891 vectors en Voyage AI
- MyClone free: 2 personas, 500 mensajes texto, 10 min voz
- MyClone API: 227 endpoints
- MyOwnClone advantage: modo multi-silo + memories completo + visitor tracking
- MyClone advantage: prompt versioning visual + variables estructuradas + workflows

## Text Labels (in Spanish)

Main title: "MyOwnClone — Informe OSINT Completo"
Subtitle: "MyClone.is (227 endpoints) + Código MyOwnClone + Plan de 5 Pasos"
Footer: "Fuente: api.myclone.is + código local | Credenciales: xoyigo3386@disiok.com"

Module labels (each with SEC-XX coordinate):
- SEC-01: "MyClone API"
- SEC-02: "Prompt System"
- SEC-03: "Arquitectura"
- SEC-04: "⚠️ Bugs"
- SEC-05: "Step 1"
- SEC-06: "Steps 2-3"
- SEC-07: "Steps 4-5"
- SEC-08: "Archivos"
- SEC-09: "Comparativa"

Priority indicators:
- 🔴 BUG 1 y BUG 3 = prioridad máxima (rompen datos)
- 🟡 BUG 2 y BUG 4 = prioridad media (drift de schema)
- 🟢 Steps 2-3 = bajo esfuerzo, alto impacto
- 🔵 Step 5 Langfuse = observabilidad (producción)
