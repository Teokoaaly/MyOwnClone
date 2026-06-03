# PLAN MAESTRO UNIFICADO — Clon de Clonify sobre Dify

**Fecha:** 2026-05-26
**Versión:** 2.0 — unifica build from-scratch (PLAN_MAESTRO.md) con build sobre Dify (PROMPT_MAESTRO.md)
**Objetivo:** Tener UN solo plan canónico que resuelva el dilema "Dify vs from-scratch" y dé el camino óptimo.

---

## 0. DECISIÓN DE ARQUITECTURA: ¿POR QUÉ DIFY COMO BASE?

### Lo que Dify ya trae GRATIS (sin escribir una línea)

| Feature | Líneas de código ahorradas | Tiempo ahorrado |
|---|---|---|
| Multi-tenant (workspaces) | ~5,000 | 2 semanas |
| RAG pipeline completo (ingest → embeddings → pgvector → retrieval → chat) | ~8,000 | 3 semanas |
| Chat UI con streaming (SSE) | ~3,000 | 1 semana |
| Admin panel estilo Dify (apps, datasets, billing) | ~6,000 | 2 semanas |
| Auth (email, Google, GitHub OAuth) | ~2,000 | 1 semana |
| API REST pública con API keys | ~4,000 | 1 semana |
| Pipeline de ingestión (documentos, web, texto) | ~3,000 | 1 semana |
| Sistema de billing (Stripe en self-hosted) | ~2,000 | 1 semana |
| Permisos y roles por workspace | ~1,500 | 3 días |
| CI/CD + Docker + tests | ~2,000 | 1 semana |
| **TOTAL** | **~36,500 líneas** | **~10 semanas** |

Dify son **860K líneas de código** (Python Flask + Next.js TypeScript). No tiene sentido reescribir lo que ya está probado, mantenido por ~500 contribuidores, y tiene 142K estrellas en GitHub.

### Lo que Dify NO tiene (lo que tenemos que construir)

1. Sistema de 3 silos con retrieval filtrado (teach/support/sales)
2. Context instances (URL → context_id → retrieval scope)
3. Inbox email triage con LLM
4. Clone personality/voice system prompt
5. Speaker diarization en pipeline de ingestión
6. Booking + videocall (Cal.com + Whereby/Daily.co)
7. Creator memory (brain: frases, políticas, firmas)
8. Dashboard de insights por clon
9. Cost tracking por tenant/categoría
10. White-label con dominio personalizado
11. Widget de chat embebible
12. Onboarding específico para creadores

### El plan: Forkear Dify y modificar/extender, NO reescribir

La arquitectura unificada es:

```
Dify (860K LOC, Apache 2.0)
  │
  ├── Lo que NO se toca (60% del código base)
  │   ├── api/core/         → lógica de Dify apps/workflows
  │   ├── api/models/       → modelos existentes (account, dataset, etc.)
  │   ├── api/controllers/  → API REST de apps
  │   ├── web/app/          → UI de apps/workflows de Dify
  │   └── migrations/       → migraciones base de Dify
  │
  ├── Lo que se MODIFICA (25% del código base)
  │   ├── api/models/       → añadir campos a tablas existentes
  │   ├── api/core/rag/     → modificar retrieval para silos
  │   ├── web/app/components/ → extender chat UI
  │   ├── web/middleware.ts  → contexto por URL
  │   └── migrations/       → nuevas migraciones
  │
  └── Lo NUEVO que se añade (15% nuevo código)
      ├── api/core/myownclone/  → módulo específico de Clonify
      ├── web/app/(myownclone)/ → nuevas páginas (creator dashboard, inbox, etc.)
      └── packages/myownclone/  → SDK/widget emebible
```

---

## 1. VISIÓN DEL PRODUCTO

Plataforma SaaS multi-tenant donde infoproductores crean clones de IA entrenados con su propio contenido (vídeos, PDFs, cursos, emails). El clon atiende 24/7 en 3 modos: Pedagogía, Ventas y Soporte. Diferenciadores: RAG pipeline con anti-alucinación, email triage automático, y booking + videollamada integrados.

**Nombre propuesto:** Réplica ("Multiplícate")

---

## 2. STACK TECNOLÓGICO DEFINITIVO

| Capa | Tecnología | Justificación |
|---|---|---|
| Frontend | Next.js 14 App Router + TypeScript + Tailwind CSS | El stack de Dify; no se cambia |
| Hosting | Vercel (prod) / Docker Compose (dev local) | Vercel para MVP, Docker para dev |
| DB | PostgreSQL + PGvector | Dify ya usa PostgreSQL con pgvector nativo |
| ORM (Python) | SQLAlchemy (ya en Dify) | No se cambia |
| ORM (Next.js) | Drizzle ORM para schemas Clonify | Solo para las tablas nuevas; convive con SQLAlchemy |
| Auth | NextAuth.js v4 + OTP email + Google OAuth | Dify ya tiene esto implementado |
| LLM principal | Anthropic Claude 3.5 Sonnet (chat) | Dify ya soporta Anthropic como provider |
| Embeddings | OpenAI text-embedding-3-small (1536d) | Dify ya soporta OpenAI embeddings |
| Pagos | Stripe (ya integrado en Dify self-hosted) | Extender plan de Dify con planes de Clonify |
| Email outbound | Resend (SDK React) | Mejor DX; añadir al stack |
| Email inbound | SendGrid Inbound Parse → webhook | Única opción sólida para inbound programático |
| Video | Whereby / Daily.co | Embebible, sin SDK pesado |
| TTS/STT | OpenAI Whisper (STT) + ElevenLabs (TTS) | Whisper para transcripción; ElevenLabs para voz |
| Monitoring | Sentry | Ya configurado en Dify |
| Analytics | PostHog | Añadir al stack |
| i18n | next-intl (español prioritario) | Dify usa i18n propio; extender |
| Rate limiting | Vercel KV + @upstash/ratelimit | Ya presente en la replica/ |

### Comparativa con el componente correspondiente de Dify

| Componente Clonify | Cómo lo hace Dify | Qué se modifica |
|---|---|---|
| Multi-tenant | `workspaces` table | Se renombra/acopla a `clone_configs` |
| Vector DB + RAG | `documents` + `embeddings` + pgvector | Se añaden campos `silo`, `context_id`, `speaker` |
| Chat UI | SSE streaming en apps | Se extiende a streaming con silo toggle |
| Auth | Sign-in con email, Google, GitHub | Se añade OTP magic link y se simplifica onboarding |
| Admin | Panel de gestión de apps/datasets | Se añade dashboard de creador Clonify |
| Billing | Stripe en self-hosted | Se extiende con planes Clonify |
| Ingestion | Pipeline de documentos/web/texto | Se añade speaker diarization y entrevista AI |

---

## 3. ARQUITECTURA DEL SISTEMA

```
┌──────────────────────────────────────────────────────────────┐
│                 Vercel (prod) / Docker Compose (dev)           │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐   │
│  │ [slug].repli │  │ api.replica. │  │ admin.replica.tu  │   │
│  │ ca.tudominio │  │ tudominio.co │  │ dominio.com       │   │
│  │ .com         │  │ m (dashboard │  │ (admin plataforma │   │
│  │ (chat públic │  │  creador)    │  │  multi-tenant)    │   │
│  │ o del clon)  │  │              │  │                   │   │
│  └──────┬───────┘  └──────┬───────┘  └────────┬──────────┘   │
│         │                 │                    │              │
│         └─────────────────┼────────────────────┘              │
│                           │                                   │
│              ┌────────────┴────────────┐                      │
│              │ Dify + Clonify Backend  │                      │
│              │ ┌─────────────────────┐ │                      │
│              │ │  api/           Flask│ │                      │
│              │ │  dify_app.py    (Dify│ │                      │
│              │ │  core)              │ │                      │
│              │ │  + api/core/myownclone │ │                      │
│              │ │  (nuevo módulo)     │ │                      │
│              │ └─────────────────────┘ │                      │
│              │ ┌─────────────────────┐ │                      │
│              │ │  web/          Next. │ │                      │
│              │ │  js                │ │                      │
│              │ │  (app/ + components│ │                      │
│              │ │  /)                │ │                      │
│              │ └─────────────────────┘ │                      │
│              └────────────┬────────────┘                      │
│                           │                                   │
│         ┌─────────────────┼─────────────────┐                 │
│         │                 │                 │                 │
│    ┌────▼────┐    ┌───────▼──────┐    ┌─────▼─────┐          │
│    │PostgreSQL│   │  Anthropic   │    │  Stripe   │          │
│    │+pgvector│    │  Claude +    │    │  Payments │          │
│    │         │    │  OpenAI Embed│    │           │          │
│    └─────────┘    └──────────────┘    └───────────┘          │
│                                                               │
│    ┌─────────┐    ┌──────────────┐    ┌─────────────┐        │
│    │ Resend  │    │SendGrid Inb. │    │  Whereby    │        │
│    │(outbound│    │ Parse (inb.) │    │  Daily.co   │        │
│    │ email)  │    │              │    │  (video)    │        │
│    └─────────┘    └──────────────┘    └─────────────┘        │
└──────────────────────────────────────────────────────────────┘
```

### Flujo RAG con 3 Silos (Corazón del producto)

```
Contenido (YouTube, PDFs, texto, vídeos, entrevistas)
    │
    ▼
Transcripción (Whisper) + Speaker Diarization (solo voz del creador)
    │
    ▼
Chunking (500-1000 tokens, overlap 100) + Metadatos (silo + context_id)
    │
    ▼
Embeddings (OpenAI text-embedding-3-small → 1536d)
    │
    ▼
pgvector (index HNSW, cosine similarity)
    │
    ├── Namespace: teach    (pedagogía)
    ├── Namespace: support  (soporte)
    └── Namespace: sales    (ventas)
    │
    ▼
Usuario pregunta + silo activo + context_id (opcional)
    │
    ▼
Retrieval: cosine similarity filtrado por tenant_id + silo + context_id
    │
    ▼
System prompt (personalidad + modo + memorias) + chunks + historial
    │
    ▼
Claude 3.5 Sonnet → respuesta + confidence_score
    │
    ├── confidence ≥ 0.7 → Responde + fuentes citadas
    └── confidence < 0.7 → "No tengo suficiente información para responder"
                           → Registra gap de conocimiento
                           → Notifica al creador
                           → Sugiere añadir contenido
```

---

## 4. MAPA DE MODIFICACIONES SOBRE DIFY

### 4.1 Tablas EXISTENTES de Dify a MODIFICAR

#### `documents` (tabla central de RAG en Dify)
```sql
ALTER TABLE documents ADD COLUMN silo VARCHAR(20) CHECK (silo IN ('teach','support','sales'));
ALTER TABLE documents ADD COLUMN context_id VARCHAR(255);
ALTER TABLE documents ADD COLUMN speaker VARCHAR(100);
ALTER TABLE documents ADD COLUMN source_metadata JSONB DEFAULT '{}';
ALTER TABLE documents ADD COLUMN clone_config_id UUID REFERENCES clone_configs(id);
CREATE INDEX idx_documents_silo ON documents(tenant_id, silo);
CREATE INDEX idx_documents_context ON documents(tenant_id, silo, context_id);
```

#### `messages` (conversaciones en Dify)
```sql
ALTER TABLE messages ADD COLUMN silo VARCHAR(20);
ALTER TABLE messages ADD COLUMN context_id VARCHAR(255);
ALTER TABLE messages ADD COLUMN confidence_score FLOAT;
ALTER TABLE messages ADD COLUMN sources JSONB DEFAULT '[]';
```

#### `workspaces` (tenants en Dify)
```sql
ALTER TABLE workspaces ADD COLUMN slug VARCHAR(100) UNIQUE;
ALTER TABLE workspaces ADD COLUMN plan VARCHAR(20) DEFAULT 'básico';
ALTER TABLE workspaces ADD COLUMN custom_domain VARCHAR(255);
ALTER TABLE workspaces ADD COLUMN subscription_status VARCHAR(20) DEFAULT 'trial';
ALTER TABLE workspaces ADD COLUMN stripe_customer_id VARCHAR(100);
ALTER TABLE workspaces ADD COLUMN stripe_subscription_id VARCHAR(100);
```

#### `accounts` (usuarios en Dify)
```sql
ALTER TABLE accounts ADD COLUMN role VARCHAR(20) DEFAULT 'member' CHECK (role IN ('owner','admin','member','viewer'));
```

### 4.2 Tablas NUEVAS a CREAR

```sql
-- 1. Configuración del clon (personalidad, tono, silos activos)
CREATE TABLE clone_configs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES workspaces(id),
    name VARCHAR(255) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    avatar_url VARCHAR(500),
    personality_tone VARCHAR(50),           -- formal, informal, cercano, técnico
    language VARCHAR(10) DEFAULT 'es',
    active_modes VARCHAR(20)[] DEFAULT '{teach}',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 2. System prompts por modo del clon
CREATE TABLE clone_mode_prompts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    mode VARCHAR(20) NOT NULL CHECK (mode IN ('teach','support','sales')),
    system_prompt TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 3. Memoria del creador (brain: frases, políticas, firmas)
CREATE TABLE creator_memory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    type VARCHAR(20) NOT NULL CHECK (type IN ('memory','signature','template')),
    content TEXT NOT NULL,
    trigger_condition TEXT,                 -- keywords o condiciones para templates
    priority INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- 4. Emails entrantes (inbox triage)
CREATE TABLE email_inbound (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    from_email VARCHAR(255),
    from_name VARCHAR(255),
    subject TEXT,
    body_text TEXT,
    body_html TEXT,
    draft_reply TEXT,                       -- respuesta propuesta por el clon
    status VARCHAR(20) DEFAULT 'pending' CHECK (status IN ('pending','sent','discarded','spam')),
    labels TEXT[] DEFAULT '{}',
    classification VARCHAR(50),             -- consulta, queja, venta, soporte
    thread_id VARCHAR(500),
    received_at TIMESTAMP DEFAULT NOW(),
    responded_at TIMESTAMP
);

-- 5. Templates de email
CREATE TABLE email_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    name VARCHAR(255),
    subject VARCHAR(500),
    body TEXT,
    trigger_keywords TEXT[] DEFAULT '{}',
    created_at TIMESTAMP DEFAULT NOW()
);

-- 6. Tipos de reunión
CREATE TABLE meeting_types (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    name VARCHAR(255),
    duration_minutes INTEGER DEFAULT 30,
    price_cents INTEGER DEFAULT 0,
    description TEXT,
    color VARCHAR(7) DEFAULT '#6366f1',
    active BOOLEAN DEFAULT true
);

-- 7. Disponibilidad semanal
CREATE TABLE availability (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    day_of_week INTEGER CHECK (day_of_week BETWEEN 0 AND 6),
    start_time TIME,
    end_time TIME,
    buffer_minutes INTEGER DEFAULT 15
);

-- 8. Reservas
CREATE TABLE bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    meeting_type_id UUID NOT NULL REFERENCES meeting_types(id),
    visitor_name VARCHAR(255),
    visitor_email VARCHAR(255),
    date DATE,
    start_time TIME,
    end_time TIME,
    status VARCHAR(20) DEFAULT 'confirmed' CHECK (status IN ('confirmed','cancelled','completed')),
    meeting_url VARCHAR(500),
    recording_url VARCHAR(500),
    transcript TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- 9. Productos (para modo ventas)
CREATE TABLE products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    name VARCHAR(255),
    description TEXT,
    price_cents INTEGER,
    url VARCHAR(500),
    image_url VARCHAR(500),
    priority INTEGER DEFAULT 0,
    active BOOLEAN DEFAULT true
);

-- 10. Seguimiento de costes
CREATE TABLE cost_tracking (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES workspaces(id),
    category VARCHAR(20) NOT NULL CHECK (category IN ('clone_response','content_ingestion','platform_ops')),
    operation VARCHAR(100),
    model VARCHAR(50),
    tokens_in INTEGER DEFAULT 0,
    tokens_out INTEGER DEFAULT 0,
    cost_cents INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX idx_cost_tracking_tenant ON cost_tracking(tenant_id, category, created_at);

-- 11. Analytics: preguntas frecuentes
CREATE TABLE analytics_questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    question TEXT,
    count INTEGER DEFAULT 1,
    last_asked_at TIMESTAMP DEFAULT NOW()
);

-- 12. Analytics: gaps de conocimiento
CREATE TABLE analytics_gaps (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clone_id UUID NOT NULL REFERENCES clone_configs(id),
    question TEXT,
    count INTEGER DEFAULT 1,
    suggested_source VARCHAR(500),
    status VARCHAR(20) DEFAULT 'open' CHECK (status IN ('open','resolved')),
    created_at TIMESTAMP DEFAULT NOW()
);

-- 13. Suplantación audit log
CREATE TABLE impersonation_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    admin_id UUID NOT NULL REFERENCES accounts(id),
    tenant_id UUID NOT NULL REFERENCES workspaces(id),
    reason TEXT,
    started_at TIMESTAMP DEFAULT NOW(),
    ended_at TIMESTAMP
);

-- 14. Planes y límites
CREATE TABLE plans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    price_cents INTEGER NOT NULL,
    stripe_price_id VARCHAR(100),
    words_training_limit BIGINT DEFAULT 500000,
    responses_month_limit INTEGER DEFAULT 2000,
    modes_active INTEGER DEFAULT 1,
    email_triage BOOLEAN DEFAULT false,
    booking BOOLEAN DEFAULT false,
    api_access BOOLEAN DEFAULT false,
    multi_clone BOOLEAN DEFAULT false,
    whitelabel BOOLEAN DEFAULT false
);
```

---

## 5. PLAN DE CONSTRUCCIÓN (12 SEMANAS, SOBRE DIFY)

### FASE 0: Fork + Setup (Semana 1)

**Objetivo:** Fork de Dify funcional en local + entender arquitectura interna.

| Día | Tarea | Prioridad |
|---|---|---|
| 1 | `git clone` Dify + instalar dependencias (Python + Node) | Crítica |
| 1 | Levantar entorno dev con docker-compose (PostgreSQL, Redis, pgvector) | Crítica |
| 2 | Mapear estructura de carpetas: `api/`, `web/`, `cli/` | Alta |
| 2 | Identificar punto de entrada: `api/app.py` y `web/app/layout.tsx` | Alta |
| 3 | Correr migraciones base de Dify, testear CRUD de apps | Alta |
| 3 | Testear pipeline de ingestión: upload PDF → chunk → embed → query | Alta |
| 4 | Documentar TODOS los archivos que vamos a tocar (ver sección 8 más abajo) | Alta |
| 5 | Crear branch `myownclone-v1` en el fork | Media |

**Entregable:** Dify corriendo en local, con una app de prueba que responde a preguntas sobre un PDF. Documento de archivos a modificar completado.

---

### FASE 1: Schema + Auth Multi-tenant (Semana 2)

**Objetivo:** Capa de datos Clonify añadida al schema de Dify + sistema de subdominios.

| Tarea | Archivos |
|---|---|
| Crear migraciones SQL con todas las tablas nuevas (sección 4.2) | `api/migrations/versions/` |
| Ejecutar ALTER TABLE en tablas existentes (sección 4.1) | `api/migrations/versions/` |
| Crear modelo SQLAlchemy para `clone_configs` | `api/models/myownclone/` |
| API REST: `POST /api/myownclone/clones` (crear clon) | `api/controllers/myownclone/` |
| API REST: `GET /api/myownclone/clones/:id` (obtener config) | `api/controllers/myownclone/` |
| Middleware Next.js: resolver subdominio [slug] → tenant | `web/src/middleware.ts` |
| Middleware: validar contexto `?context=curso-modulo-video` → `context_id` | `web/src/middleware.ts` |
| Adaptar auth de Dify a flow Clonify: registro → tenant → clon | `web/app/signup/` |
| Onboarding wizard: slug, nombre clon, personalidad, plan | `web/app/(onboarding)/` |

**Entregable:** Usuario se registra, crea tenant con slug, crea su primer clon. Middleware resuelve subdominios. Schema completo en DB.

---

### FASE 2: Silos + RAG Modificado (Semana 3-4)

**Objetivo:** Modificar el pipeline RAG de Dify para soportar 3 silos + contexto.

Este es el **corazón técnico del proyecto**.

| Tarea | Archivos a modificar en Dify |
|---|---|
| Modificar `VectorDB` para filtrar por `silo` | `api/core/rag/vector_db.py` |
| Añadir `context_id` al filtro de retrieval | `api/core/rag/retrieval.py` |
| Crear helper `filter_chunks(silo, context_id)` | `api/core/myownclone/retrieval_filters.py` (NUEVO) |
| Modificar embedding service para añadir metadatos (silo, context_id) | `api/core/rag/embedding.py` |
| Modificar ingestion pipeline: chunk → embedding + metadata | `api/services/document_service.py` |
| API: `POST /api/myownclone/sources/ingest` con `{ silo, context_id }` | `api/controllers/myownclone/sources.py` (NUEVO) |
| API: `POST /api/myownclone/clones/:id/chat` con `{ message, silo, context_id }` | `api/controllers/myownclone/chat.py` (NUEVO) |
| Streaming SSE de respuesta con confidence_score | `api/core/myownclone/chat_stream.py` (NUEVO) |
| UI: toggle de silo en chat (botones teach/support/sales) | `web/app/components/myownclone/chat/SiloToggle.tsx` (NUEVO) |
| Tests: query en teach vs sales con mismo contenido → resultados diferentes | `api/tests/myownclone/test_silos.py` (NUEVO) |

**Entregable:** Clon responde con contenido filtrado por silo activo + contexto. Si estoy en modo "ventas", el clon recomienda productos. Si estoy en modo "pedagogía", enseña.

---

### FASE 3: Chat UI Pública + Widget (Semana 4-5)

**Objetivo:** Página pública del clon con chat completo + widget embebible.

| Tarea | Archivos |
|---|---|
| Página `[slug]/page.tsx` — landing del clon con chat | `web/app/(myownclone)/[slug]/page.tsx` (NUEVO) |
| Componente `ChatPanel` con streaming + markdown | `web/app/components/myownclone/chat/ChatPanel.tsx` |
| Componente `MessageBubble` con citas de fuentes | `web/app/components/myownclone/chat/MessageBubble.tsx` |
| Indicador de confianza en respuestas (% coherence) | `web/app/components/myownclone/chat/ConfidenceBar.tsx` |
| Notas de voz: MediaRecorder API → transcripción Whisper | `web/app/components/myownclone/chat/VoiceInput.tsx` |
| Botón "Nueva conversación" (resetear historial) | `web/app/components/myownclone/chat/NewChat.tsx` |
| Feedback thumbs up/down en cada respuesta | `api/controllers/myownclone/feedback.py` |
| Widget embebible: script + iframe | `web/public/widget.js` (NUEVO) |
| Estados UI: loading, error, empty, success | Todos los componentes |
| Aplicar contexto por URL: `?context=clase-4` → limitar retrieval | Ya desde middleware (Fase 1) |

**Entregable:** Demo funcional en `juanperez.replica.tudominio.com`. Chat responde con silo activo. Widget funciona en HTML externo. Notas de voz funcionales.

---

### FASE 4: Dashboard del Creador (Semana 5-7)

**Objetivo:** Adaptar el panel de Dify para convertirlo en el dashboard del creador de Clonify.

#### 4.1 Biblioteca de Contenido
| Tarea | Descripción |
|---|---|
| Subir PDF, texto, URL, YouTube | Usar pipeline de ingestión de Dify con metadatos Clonify |
| Entrevista AI | Agente Claude que entrevista al creador → chunks con speaker=creator |
| Carpetas de cursos | Extensión sobre el sistema de datasets de Dify |
| Progreso de ingesta SSE | Adaptar el sistema de progreso de Dify |
| Panel de búsqueda y filtrado | Componente nuevo con filtro por silo, tipo, estado |

#### 4.2 Cerebro / Brain
| Tarea | Descripción |
|---|---|
| CRUD de memorias, firmas, plantillas | Componentes nuevos: `BrainMemoryForm`, `SignatureEditor`, `TemplateBuilder` |
| Vista previa del prompt final | Componente que muestra el system prompt ensamblado con todas las memorias |
| Trigger conditions para templates | Motor de matching: keywords → template a usar |

#### 4.3 Gestión del Clon
| Tarea | Descripción |
|---|---|
| Configuración de personalidad y tono | Sliders: formal↔informal, serio↔divertido, cercano↔profesional |
| System prompts editables por modo | Editor de texto con variables: `{{memorias}}`, `{{productos}}`, `{{firmas}}` |
| Configuración de subdominio | Campo slug + vista previa del enlace público |
| Avatar y branding | Upload a storage + preview |

#### 4.4 Analíticas
| Tarea | Descripción |
|---|---|
| Dashboard principal | Widgets: conversaciones, mensajes, preguntas, gaps |
| Top 10 preguntas frecuentes | Agregación de `analytics_questions` con gráfica de barras |
| Gaps de conocimiento | Tabla con preguntas sin respuesta + botón "Añadir contenido" |
| Consumo del plan | Tracking en tiempo real de palabras/respuestas vs límite |
| Costes desglosados | Claude API, OpenAI embeddings, infraestructura |

**Entregable:** Dashboard completo con biblioteca funcional, brain, analíticas y gestión de clon.

---

### FASE 5: Inbox / Email Triage (Semana 7-8)

**Objetivo:** Killer feature — el clon gestiona emails y propone respuestas.

| Tarea | Archivos |
|---|---|
| Configurar SendGrid Inbound Parse → webhook endpoint | `api/controllers/myownclone/inbound_email.py` (NUEVO) |
| Verificar firma SendGrid en webhook | `api/core/myownclone/sendgrid_verify.py` (NUEVO) |
| Procesar email: extraer to/from/subject/body | `api/services/myownclone/email_processor.py` (NUEVO) |
| Clasificar email con LLM (consulta, queja, venta, soporte) | `api/core/myownclone/email_classifier.py` (NUEVO) |
| Generar draft de respuesta con Claude | `api/core/myownclone/email_draft.py` (NUEVO) |
| Guardar en `email_inbound` con estado `pending` | Modelo existente |
| UI del Inbox: vista dividida (lista + preview + draft) | `web/app/(myownclone)/inbox/` (NUEVO) |
| Editor de draft con markdown | Componente `EmailDraftEditor` |
| Botones: Enviar (Resend), Descartar, Editar | API endpoint + UI |
| Auto-guardar como plantilla al enviar | Servicio automático |
| Filtros: pendientes, enviados, descartados, spam | Componente `InboxFilters` |
| Etiquetas manuales y automáticas | CRUD de labels |

**Entregable:** Email recibido → aparece en inbox → clon propone respuesta en el tono del creador → creador revisa y envía con un clic.

---

### FASE 6: Stripe + Planes (Semana 8)

**Objetivo:** Monetización completa heredando el sistema de billing de Dify.

| Tarea | Descripción |
|---|---|
| Planes: Básico(49€), Pro(99€), Escala(199€), Enterprise(499€) | Tabla `plans` + config en Stripe dashboard |
| Adaptar Stripe webhook de Dify | Añadir eventos para planes Clonify |
| Checkout flow: trial 14 días con tarjeta | `api/controllers/myownclone/stripe/` (NUEVO) |
| Customer Portal (cambios de plan, cancelar) | Redirigir a Stripe |
| Cortesías sin tarjeta (admin platform) | `POST /api/admin/myownclone/courtesies` |
| Middleware de cuota: verificar límites antes de operación | `api/core/myownclone/quota_middleware.py` (NUEVO) |
| Banner de cuota en dashboard | Componente `AdminQuotaBanner` |
| Facturas desde Stripe API + descargar PDF | Integración con Stripe Invoice API |

**Entregable:** Registro → trial → pago → acceso Pro. Webhooks actualizan estado automáticamente.

---

### FASE 7: Booking + Videollamada (Semana 9-10)

**Objetivo:** Sistema completo de booking + video + grabación + transcripción.

| Tarea | Archivos |
|---|---|
| CRUD de tipos de reunión (AdminMeetingTypes) | `web/app/(myownclone)/meeting-types/` |
| Configuración de disponibilidad semanal | `web/app/(myownclone)/availability/` |
| API: `GET /api/myownclone/clones/:slug/slots?date=` → slots disponibles | `api/controllers/myownclone/bookings.py` |
| Página pública de reserva: `[slug]/reservar` | `web/app/(myownclone)/[slug]/reservar/page.tsx` |
| Formulario: nombre, email, notas, preguntas personalizadas | Componente `BookingForm` |
| Confirmación: email Resend + ICS adjunto | `api/services/myownclone/booking_email.py` |
| Integración Whereby: crear sala al confirmar | `api/core/myownclone/whereby.py` |
| Integración Daily.co (alternativa) | `api/core/myownclone/daily.py` |
| Página MeetingRoom: iframe + chat contextual | `web/app/(myownclone)/meeting/[id]/page.tsx` |
| Webhook de grabación: descargar → Supabase Storage | `api/controllers/myownclone/recordings.py` |
| Transcripción Whisper de grabación | `api/core/myownclone/whisper_transcribe.py` |
| Indexar transcripción en Vector DB (silo=pedagogía) | Pipeline de ingestión automático |
| Página PublicRecording: grabación + chat post-reunión | `web/app/(myownclone)/recording/[id]/page.tsx` |

**Entregable:** Visitante agenda reunión → videollamada → grabación se transcribe → el clon sabe lo que se habló.

---

### FASE 8: Admin de Plataforma + Insights (Semana 10-11)

**Objetivo:** Panel de administración multi-tenant + dashboard de costes.

| Tarea | Descripción |
|---|---|
| Middleware de admin (role=platform_admin) | Extender middleware de Dify |
| Resumen: MRR, costes, margen, gráficas temporales | `web/app/(admin-myownclone)/resumen/` (NUEVO) |
| Cost tracking por tenant + categoría (clone_response, content_ingestion, platform_ops) | Queries SQL sobre `cost_tracking` |
| Listado de tenants: buscar, filtrar, ordenar | `web/app/(admin-myownclone)/tenants/` |
| Ver detalle de tenant (modo vista del dashboard) | Componente `TenantDetailView` |
| Suplantación: login como tenant con motivo + audit log | `POST /api/admin/myownclone/impersonate` |
| Banner rojo fijo durante suplantación: "Suplantando a X — [motivo] — [temporizador 30min]" | Componente `ImpersonationBanner` |
| Timeout automático a los 30 minutos | Cron job o verificación en middleware |
| Concesión de cortesías (invitar tenant sin Stripe) | `POST /api/admin/myownclone/courtesies` |
| Inbox global (*@replica.tudominio.com) | Vista unificada de `email_inbound` |
| Feedback de plataforma | CRUD de tickets creado por usuarios |
| White-label: dominio personalizado (CNAME) | Configuración en tenant + verificación DNS |

**Entregable:** Admin ve MRR, gestiona tenants, suplanta para soporte, concede cortesías. Panel de control completo del negocio.

---

### FASE 9: White-label + API Pública + Multi-clon (Semana 11-12)

| Tarea | Descripción |
|---|---|
| Dominio personalizado: CNAME → verificación DNS → servir en `customdomain.com` | Middleware + configuración en Vercel |
| CSS custom por tenant (colores, fuentes, logo) | Sistema de theming por tenant |
| API Keys para desarrolladores | CRUD de API keys por tenant |
| Webhooks salientes (eventos) | Sistema de webhooks |
| Multi-clon: un tenant → N clones | Extensión del modelo `clone_configs` |
| Roles de equipo (owner, admin, member, viewer) | Extensión de roles en `accounts` |
| SSO empresarial (SAML/OIDC) | Futuro |

---

### FASE POST-MVP: Marketplace + Integraciones (Semana 13+)

| Feature | Descripción |
|---|---|
| Integraciones: Slack, WhatsApp, Telegram, Messenger | Canales de comunicación adicionales |
| Zapier/Make connector | Webhooks + API pública |
| Marketplace de plantillas de clon por industria | Directorio público de clones pre-configurados |
| Comunidad de creadores | Foro/community |
| Entrevista AI avanzada | Agente que entrevista al creador con preguntas adaptativas |
| Speaker diarization avanzado | Separar voces en entrevistas reales (PyAnnote o similar) |

---

## 6. ORDEN DE PRIORIDAD PARA MVP (LO MÍNIMO PARA LANZAR)

Si el objetivo es lanzar rápido (4 semanas):

| Semana | Fase | Qué se construye |
|---|---|---|
| 1 | Fase 0 + 1 | Fork Dify + schema + auth + multi-tenant |
| 2 | Fase 2 | RAG con 3 silos + retrieval modificado |
| 3 | Fase 3 | Chat UI pública + widget embebible |
| 4 | Fase 6 | Stripe + planes + deploy |

**MVP lanzable: 4 semanas.** El resto (inbox, booking, admin platform, white-label) se añade post-lanzamiento con usuarios reales.

---

## 7. LO QUE YA EXISTE EN EL PROYECTO ACTUAL

### Directorio `replica/` — Proyecto from-scratch (PLAN_MAESTRO.md original)

```
replica/
├── src/
│   ├── app/                      # Next.js App Router
│   ├── components/               # Componentes React
│   ├── lib/                      # Lógica compartida
│   │   ├── rag/                  # Pipeline RAG (ingest, retrieve, generate)
│   │   └── db/                   # Drizzle ORM (schemas, migrations)
│   ├── middleware.ts             # Subdominios + auth
│   └── i18n/                     # next-intl (español)
├── supabase/migrations/          # Migraciones SQL
├── drizzle.config.ts
├── package.json                  # Next.js 16 + Drizzle + NextAuth v5 + Stripe + Resend
└── .env.example
```

**Estado:** Proyecto Next.js funcional con dependencias instaladas, Drizzle ORM configurado, estructura de carpetas lista. **Es el punto de partida ideal para el frontend y las APIs nuevas.**

### Directorio `dify/` — Fork de Dify (860K LOC)

```
dify/
├── api/                          # Backend Python (Flask)
│   ├── core/                     # Lógica central (RAG, modelos, providers)
│   ├── models/                   # Modelos SQLAlchemy
│   ├── controllers/              # Controladores API REST
│   ├── services/                 # Capa de servicios
│   └── migrations/               # Migraciones de base de datos
├── web/                          # Frontend Next.js
│   ├── app/                      # App Router
│   │   ├── (commonLayout)/       # Layout común
│   │   ├── signin/               # Auth
│   │   └── components/           # Componentes compartidos
│   └── middleware.ts             # Middleware de Dify
└── docker/                       # Docker Compose para dev
```

---

## 8. MAPA DE ARCHIVOS A TOCAR — GUÍA RÁPIDA PARA EL DESARROLLADOR

### Archivos de Dify a MODIFICAR

| Archivo | Qué modificar | Fase |
|---|---|---|
| `api/models/model.py` | Añadir columnas a las tablas existentes | 1 |
| `api/core/rag/extractor/extract_processor.py` | Añadir metadatos `silo` y `context_id` | 2 |
| `api/core/rag/embedding/cached_embedding.py` | Indexar en namespace por silo | 2 |
| `api/core/rag/retrieval/dataset_retrieval.py` | Añadir filtros `silo` + `context_id` | 2 |
| `web/middleware.ts` | Resolver contexto por URL | 1 |
| `web/app/signin/` | Adaptar flow a onboarding Clonify | 1 |
| `api/tasks/document_indexing_task.py` | Añadir metadatos Clonify a la cola de ingesta | 2 |
| `api/controllers/console/app/` | Adaptar API de apps al concepto de clones | 3 |

### Archivos NUEVOS a crear

| Archivo | Qué hace | Fase |
|---|---|---|
| `api/models/myownclone/` | Modelos SQLAlchemy para tablas Clonify | 1 |
| `api/core/myownclone/` | Módulo central Clonify (silos, email, booking) | 2-7 |
| `api/controllers/myownclone/` | APIs REST Clonify | 2-7 |
| `web/app/(myownclone)/` | Páginas Clonify (clon público, inbox, etc.) | 3-7 |
| `web/app/components/myownclone/` | Componentes React Clonify | 3-7 |
| `web/public/widget.js` | Widget embebible | 3 |
| `api/migrations/versions/XXXX_add_myownclone.py` | Migraciones Clonify | 1 |

---

## 9. RIESGOS Y MITIGACIONES

| Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|
| Dify cambia su API interna y rompe nuestra capa | Media | Alto | Mantener módulo `myownclone/` aislado del core de Dify; no modificar interfaces internas, solo extender |
| Complejidad de modificar RAG pipeline de Dify | Alta | Alto | Dify ya tiene abstracción de retrievers; añadir un retriever nuevo en vez de modificar el existente |
| Costes Claude API se disparan | Alta | Alto | Límites por plan; caching de respuestas; Claude Haiku para consultas simples; métricas de coste en tiempo real |
| Vendor lock-in con Dify | Media | Medio | Nuestro código Clonify está en módulos separados; si Dify se vuelve inviable, migramos nuestra capa a otro base |
| Conflictos de merge al actualizar Dify upstream | Alta | Medio | Cherry-pick solo features que necesitamos; mantener diff documentado; CI que valide compatibilidad |
| Licencia Apache 2.0 → problemas de marca | Baja | Bajo | Revisar trademark policy; nuestro producto es "Réplica" nombre distinto |
| Supabase/Neon rate limits en pgvector | Media | Medio | Batch inserts + cola de ingesta con backpressure + monitoreo de latencia |

---

## 10. REGLAS DE ORO (APRENDIDAS DE LOS ERRORES DE CLONIFY)

1. **NUNCA servir código admin sin autenticación** → Middleware estricto en TODAS las rutas `/admin/*` y `/api/admin/*`
2. **NUNCA exponer Sentry DSN en meta tags** → Cargar Sentry solo en el cliente, DSN en variable de entorno
3. **NUNCA CORS wildcard en producción** → `Access-Control-Allow-Origin` restringido a dominios conocidos
4. **NUNCA APIs admin sin CSRF** → Tokens CSRF en todas las mutaciones POST/PUT/DELETE
5. **NUNCA sin rate limiting** → Rate limit en auth, API, y endpoints públicos
6. **NUNCA cabeceras de seguridad ausentes** → CSP, X-Frame-Options, X-Content-Type-Options, HSTS desde día 1
7. **NUNCA logs de errores sin filtrar** → Sanitizar datos sensibles antes de enviar a Sentry
8. **NUNCA source maps en producción** → Deshabilitar `productionBrowserSourceMaps`
9. **NUNCA incluir API keys en código** → Variables de entorno ENCRIPTADAS en todos los entornos
10. **NUNCA modificar el core de Dify sin tests** → Cada modificación tiene test unitario + test de integración

---

## 11. MÉTRICAS DE ÉXITO

### Técnicas
- [ ] Time to first response < 3s (con streaming se siente instantáneo)
- [ ] Uptime > 99.5%
- [ ] RAG accuracy > 85% (respuestas correctas basadas en contenido)
- [ ] Anti-alucinación: 0 falsos positivos (nunca inventa)
- [ ] Retrieval por silo: < 200ms para top_k=5 en tabla con 100K chunks
- [ ] Dify upstream merge conflicts < 1 por mes

### Negocio
- [ ] 10 clientes de pago en mes 1 post-lanzamiento
- [ ] MRR > 500€ en mes 2
- [ ] Churn < 5% mensual
- [ ] NPS > 50

### De desarrollo
- [ ] 90% del código Dify NO TOCADO (solo extendido)
- [ ] Modificaciones aisladas en directorio `myownclone/` y `api/core/myownclone/`
- [ ] 100% de las APIs nuevas con tests
- [ ] Documentación de cada modificación sobre Dify

---

## 12. VARIABLES DE ENTORNO UNIFICADAS

```env
# ──── Dify existentes (NO modificar nombres) ────
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
SECRET_KEY=...
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...

# ──── Stripe (Dify ya lo usa, verificar compatibilidad) ────
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...

# ──── Clonify nuevos ────
NEXT_PUBLIC_APP_URL=https://replica.tudominio.com
NEXT_PUBLIC_API_URL=https://api.replica.tudominio.com
NEXT_PUBLIC_ADMIN_URL=https://admin.replica.tudominio.com

# Email
RESEND_API_KEY=re_...
RESEND_FROM_EMAIL=noreply@replica.tudominio.com
SENDGRID_INBOUND_WEBHOOK_SECRET=...

# Video
WHEREBY_API_KEY=...
WHEREBY_BASE_URL=https://api.whereby.dev/v1

# TTS
ELEVENLABS_API_KEY=...

# Stripe Price IDs (planes Clonify)
STRIPE_BASIC_PRICE_ID=price_...
STRIPE_PRO_PRICE_ID=price_...
STRIPE_SCALE_PRICE_ID=price_...
STRIPE_ENTERPRISE_PRICE_ID=price_...

# Monitoring
NEXT_PUBLIC_SENTRY_DSN=https://...
NEXT_PUBLIC_POSTHOG_KEY=phc_...
```

---

## 13. COMANDOS RÁPIDOS DE DESARROLLO

```bash
# Levantar Dify + Clonify en dev
cd dify
docker compose -f docker/docker-compose.yaml up -d

# Ejecutar migraciones Clonify
cd api
flask db upgrade

# Frontend Next.js
cd web
pnpm dev

# Tests
cd api
pytest tests/myownclone/

# Actualizar Dify upstream (cuando haya nueva versión)
git remote add upstream https://github.com/langgenius/dify.git
git fetch upstream
git merge upstream/main   # con cuidado de no sobrescribir nuestros cambios
```

---

## 14. PRÓXIMOS PASOS INMEDIATOS

1. **Levantar Dify en local** con `docker compose up` y verificar que funciona
2. **Mapear los archivos** listados en la sección 8 y documentar el plan de modificación
3. **Crear la primera migración** con las 14 tablas nuevas de la sección 4.2
4. **Modificar el modelo `documents`** de SQLAlchemy para añadir `silo`, `context_id`, `speaker`
5. **Crear el módulo `api/core/myownclone/`** con la estructura base
6. **Testear el pipeline RAG modificado** con un PDF de prueba en 3 silos distintos

---

## 15. ESTRATEGIA DE LANZAMIENTO

### Beta Privada (Semana 6)
- 5-10 early adopters (infoproductores de confianza)
- Plan básico gratuito (cortesía sin Stripe)
- Focus: bug fixing y feedback de UX

### Lanzamiento Público (Semana 8)
- Planes de pago activos (Stripe)
- 3 modos funcionales
- Inbox triage funcional
- Widget embebible

### Post-lanzamiento (Semana 10+)
- Booking + video
- Admin platform
- White-label
- API pública

---

*Este plan maestro unificado es el documento canónico. Reemplaza tanto a PLAN_MAESTRO.md como a PROMPT_MAESTRO.md. Cualquier decisión arquitectónica debe consultarse aquí primero.*
