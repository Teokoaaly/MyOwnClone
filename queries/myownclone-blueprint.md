---
title: myownclone Blueprint — Cómo Replicarlo
created: 2026-05-25
updated: 2026-05-25
type: query
tags: [architecture, implementation, saas, llm, blueprint]
sources: [raw/articles/myownclone-technical-research.md, raw/articles/myownclone-frontend-recon-2026-05-25.md, raw/articles/myownclone-web-scrape-2026-05-25.md, raw/articles/myownclone-founder-transcript.md]
confidence: high
---

# myownclone Blueprint — Cómo Replicarlo

Guía técnica para construir un clon de myownclone desde cero. Basada en todo lo extraído de la investigación: web scraping, JS bundles, transcript del founder y análisis de infraestructura.

---

## 1. Arquitectura General

```
┌─────────────────────────────────────────────────────┐
│                    Vercel Edge                       │
│  ┌───────────────────────────────────────────────┐  │
│  │         Next.js 16 App Router (monorepo)      │  │
│  │                                               │  │
│  │  myownclone.com  =  app.myownclone.com  =  api.     │  │
│  │  (misma app, routing interno)                 │  │
│  │                                               │  │
│  │  / (landing)   /admin/*   /api/webhooks/*     │  │
│  │  Server Components + Server Actions           │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐      │
│  │  Neon DB │  │  Stripe  │  │ Anthropic/    │      │
│  │(Postgres)│  │          │  │ OpenAI APIs   │      │
│  └──────────┘  └──────────┘  └───────────────┘      │
└─────────────────────────────────────────────────────┘
```

**Principio clave**: todo serverless/managed. Cero servidores propios. Next.js monorepo único para landing + app + API.

---

## 2. Stack Tecnológico — Capa por Capa

### 2.1 Frontend

| Componente | Tecnología | Notas |
|-----------|-----------|-------|
| Framework | Next.js 16.2.4 (App Router) | Turbopack, React Server Components |
| Lenguaje | TypeScript (inferido) | Strict mode probable |
| Estilos | CSS Modules + CSS custom properties | Design system con variables --bg, --fg, --accent, etc. |
| Fuentes | Poppins + JetBrains Mono | Cargadas vía next/font como woff2 |
| i18n | next-intl | Routing por locale: / (es), /en |
| Tema | Dark/Light toggle | localStorage key: "myownclone-theme" |
| Estado | React 19 (inferido) | Server Components para datos, Client Components para interactividad |

### 2.2 Backend / API

| Componente | Tecnología | Notas |
|-----------|-----------|-------|
| Runtime | Vercel Serverless Functions | Next.js API Routes + Server Actions |
| API Pattern | RSC (React Server Components) | Sin REST tradicional, sin GraphQL, sin tRPC |
| Mutaciones | Server Actions | Form submissions, data mutations |
| Auth | Server-side sessions (JWT/cookies) | Sin Auth0, Clerk, Supabase Auth visibles |
| Email | SMTP/API integrado | Contacto inbound, dominio personalizado "próximamente" |

### 2.3 Base de Datos

| Componente | Tecnología | Notas |
|-----------|-----------|-------|
| DB Principal | Neon (PostgreSQL serverless) | Serverless, branching, conexiones HTTP |
| Vector DB | PGvector (extension Neon) | Embeddings en la misma DB PostgreSQL |
| ORM | Prisma o Drizzle (inferido) | No visible en cliente, server-side |

### 2.4 AI/LLM

| Componente | Tecnología | Notas |
|-----------|-----------|-------|
| LLM principal | Anthropic Claude + OpenAI | Ambos en uso, visibles en cost tracking |
| Embeddings | OpenAI (text-embedding-3-small/large) | Inferido, estándar del mercado |
| RAG Framework | Propio (RAC) | No usa LangChain ni LlamaIndex visibles |
| TTS/STT | Browser nativo | MediaRecorder API + Web Speech API |

### 2.5 Infraestructura

| Componente | Tecnología | Notas |
|-----------|-----------|-------|
| Hosting | Vercel Pro/Enterprise | Multi-region (cdg1 Paris, iad1 US) |
| CDN/WAF | Vercel Edge Network | Automático |
| Dominios | Vercel DNS | *.myownclone.com, dominios personalizados |
| CI/CD | Vercel Git Integration | Deploy ID: dpl_8jxBD8eEioaPmHarRs3eofX1Ks3S |

### 2.6 Terceros

| Servicio | Uso |
|----------|-----|
| Stripe | Pagos (checkout, webhooks, trials, subscriptions) |
| Sentry | Error tracking (client + server) |
| PostHog | Analytics, feature flags, session recording, surveys |
| Intercom | Chat de soporte |
| Crisp Chat | Chat alternativo/de respaldo |

---

## 3. El Corazón: RAC (Retrieval Augmented Cognition)

Esto es lo que diferencia a myownclone de un chatbot RAG genérico.

### 3.1 Flujo de Ingestión

```
Contenido del creador (vídeos, PDFs, cursos, web)
        │
        ▼
┌──────────────────────────┐
│   Pipeline de Ingestión  │
│                          │
│  1. Transcripción (si    │
│     es vídeo/audio)      │
│  2. Chunking             │
│  3. Embedding (OpenAI)   │
│  4. Almacenamiento en    │
│     PGvector             │
│                          │
│  Metadatos por chunk:    │
│  - source (curso/vídeo)  │
│  - silo (teach/support/  │
│    sales)                │
│  - speaker_id (creador   │
│    vs entrevistador)     │
│  - module/class          │
└──────────────────────────┘
```

### 3.2 Flujo de Chat

```
Usuario pregunta
        │
        ▼
┌──────────────────────────┐
│  Determinar contexto     │
│  - ¿De qué enlace viene? │
│  - ¿Qué instancia?       │
│  - ¿Modo activo?         │
└──────────────────────────┘
        │
        ▼
┌──────────────────────────┐
│  Retrieval               │
│  - Buscar en namespace   │
│    del silo activo       │
│  - Filtrar por contexto  │
│    (curso/clase/vídeo)   │
│  - Solo voz del creador  │
│  - Calcular similitud    │
└──────────────────────────┘
        │
        ├── similitud > umbral ──▶ Generar respuesta
        │                          (Claude/OpenAI + system prompt
        │                           con personalidad del creador
        │                           + chunks recuperados)
        │
        └── similitud < umbral ──▶ "No tengo conocimiento
                                     sobre eso" + notificar
                                     al creador (gap)
```

### 3.3 Los Tres Silos (Namespaces Vectoriales)

Cada clon tiene 3 namespaces separados en la DB vectorial:

| Silo | Tabla/Namespace | Modo | Comportamiento |
|------|----------------|------|---------------|
| Pedagogía | `clone_teach` | Enseñar | Explica, contextualiza, responde dudas del curso |
| Soporte | `clone_support` | Ayudar | FAQs, problemas técnicos, escala a humano |
| Ventas | `clone_sales` | Vender | Recomienda productos, comparte ofertas, convierte |

El retrieval busca SOLO en el namespace del silo activo. Si el usuario pregunta sobre un curso y el clon está en modo soporte, el retrieval path es diferente.

---

## 4. Multi-Tenant — Cómo Aísla Clientes

### 4.1 Modelo de Datos

```sql
-- Tabla principal de tenants
CREATE TABLE tenants (
  id UUID PRIMARY KEY,
  slug TEXT UNIQUE,           -- nombre en URL: slug.myownclone.com
  name TEXT,
  email TEXT,
  plan TEXT,                  -- pro, scale, enterprise, complimentary
  subscription_status TEXT,   -- active, trialing, past_due, etc.
  stripe_customer_id TEXT,
  custom_domain TEXT,         -- dominio propio (opcional)
  created_at TIMESTAMPTZ,
  updated_at TIMESTAMPTZ
);

-- Todo lo demás referencia al tenant
CREATE TABLE clone_configs (
  id UUID PRIMARY KEY,
  tenant_id UUID REFERENCES tenants(id),
  personality TEXT,           -- system prompt
  voice_settings JSONB,       -- tono, velocidad, estilo
  active_silos TEXT[],        -- ['teach', 'support', 'sales']
  ...
);

-- Chunks de conocimiento con tenant + silo
CREATE TABLE knowledge_chunks (
  id UUID PRIMARY KEY,
  tenant_id UUID REFERENCES tenants(id),
  silo TEXT,                  -- 'teach', 'support', 'sales'
  source_type TEXT,           -- 'video', 'pdf', 'course', 'interview'
  source_id TEXT,             -- curso/módulo/clase
  speaker TEXT,               -- 'creator' o nombre del entrevistador
  content TEXT,
  embedding VECTOR(1536),     -- PGvector
  metadata JSONB,
  created_at TIMESTAMPTZ
);

-- Índice vectorial por tenant + silo
CREATE INDEX ON knowledge_chunks 
  USING ivfflat (embedding vector_cosine_ops)
  WHERE tenant_id = $1 AND silo = $2;
```

### 4.2 Aislamiento

- **Row-Level Security (RLS)** en PostgreSQL: cada query va scoped al `tenant_id` de la sesión
- **Dominios**: `[slug].myownclone.com` mapea a tenant automáticamente vía middleware de Next.js
- **Cost tracking**: cada operación (chat, ingestion, platform) se registra con `tenant_id` y `category`

---

## 5. Sistema de Instancias Contextuales

El feature más diferenciador: cada enlace del clon tiene un contexto.

```
Creador sube Curso "Fitness" → Módulo 3 → Vídeo "Nutrición"
                                          │
                                          ▼
                                 Genera enlace:
                                 clon.com/c/fitness-m3-nutricion
                                          │
                                          ▼
                                 Usuario abre enlace
                                          │
                                          ▼
                          ┌──────────────────────────┐
                          │  Middleware de Next.js    │
                          │  - Lee slug del tenant    │
                          │  - Lee context_id         │
                          │  - Lo pasa al RSC payload │
                          └──────────────────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────┐
                          │  Chat Component          │
                          │  - Silo activo: teach     │
                          │  - Filtro: módulo 3 +     │
                          │    vídeo "Nutrición"      │
                          │  - Retrieval limitado a   │
                          │    esos chunks            │
                          └──────────────────────────┘
```

**Implementación**:

```typescript
// app/[slug]/page.tsx (Server Component)
export default async function ClonePage({ params, searchParams }) {
  const tenant = await getTenantBySlug(params.slug);
  const contextId = searchParams.ctx; // contexto opcional
  
  // El RSC ya tiene el contexto resuelto
  return <CloneChat tenant={tenant} contextId={contextId} />;
}

// lib/retrieval.ts
async function retrieve(tenantId, query, silo, contextId?) {
  let sql = `
    SELECT content, 1 - (embedding <=> $1) AS similarity
    FROM knowledge_chunks
    WHERE tenant_id = $2 AND silo = $3
  `;
  const params = [queryEmbedding, tenantId, silo];
  
  if (contextId) {
    sql += ` AND metadata->>'context_id' = $4`;
    params.push(contextId);
  }
  
  sql += ` AND 1 - (embedding <=> $1) > $${params.length + 1}
           ORDER BY similarity DESC LIMIT 5`;
  params.push(THRESHOLD);
  
  return await db.query(sql, params);
}
```

---

## 6. Funcionalidades Clave — Cómo Implementarlas

### 6.1 Inbox Triage con IA

```
Email entrante → contacto@creador.com
        │
        ▼
┌──────────────────────────────┐
│  1. Recibir email (SMTP)     │
│  2. Crear ticket en DB       │
│  3. Clasificar con LLM:      │
│     - Tipo: soporte/ventas/  │
│       consulta                │
│     - Prioridad: baja/media/  │
│       alta                    │
│  4. Proponer acciones:       │
│     - Draft de respuesta     │
│     - Memoria nueva/update   │
│     - Template reusable      │
│     - Label/asignar tag      │
│  5. Creador revisa en        │
│     /admin/inbox/triage      │
│  6. Click = enviar/guardar   │
└──────────────────────────────┘
```

**Stack**: SMTP relay (Resend/SendGrid) → Webhook → Server Action → Anthropic (para drafts) → UI

### 6.2 Videollamadas Integradas

```
Stack inferido:
- Booking: Cal.com API o similar (ICS export)
- Video: Daily.co, Whereby, o WebRTC propio
- Grabación: transcripción vía Whisper API
- Chat post-grabación: clon disponible en página de recording
```

### 6.3 Separación de Hablantes (Entrevistas)

```
Entrevista subida (audio/vídeo)
        │
        ▼
┌──────────────────────────────┐
│  1. Transcripción (Whisper)  │
│  2. Speaker diarization      │
│     (identificar hablantes)  │
│  3. El creador marca "yo     │
│     soy el speaker 1"        │
│  4. Solo los chunks del      │
│     speaker 1 van al RAC     │
│  5. Los chunks del speaker 2 │
│     (entrevistador) se       │
│     guardan como contexto    │
│     pero no se usan en       │
│     retrieval                │
└──────────────────────────────┘
```

---

## 7. Plan de Implementación — MVP a Producción

### Fase 0: Fundación (Semana 1-2)

```
□ Next.js 14+ App Router + TypeScript + Tailwind
□ Neon PostgreSQL + PGvector
□ Auth (NextAuth.js con email/password + OTP)
□ Stripe (checkout + webhooks)
□ Multi-tenant middleware (slug routing)
```

### Fase 1: El Clon Básico (Semana 3-4)

```
□ Pipeline de ingestión (chunking + embeddings OpenAI)
□ Retrieval básico (PGvector cosine similarity)
□ Chat UI con streaming (Vercel AI SDK)
□ System prompt con personalidad del creador
□ Umbral anti-alucinación ("no tengo conocimiento")
□ Admin dashboard básico (/admin/clone, /admin/brain)
```

### Fase 2: Los Tres Silos (Semana 5-6)

```
□ Namespaces separados por silo en PGvector
□ Toggle de modo en chat (teach/support/sales)
□ Retrieval path condicionado por silo activo
□ Entrenamiento por silo en /admin/brain
```

### Fase 3: Instancias Contextuales (Semana 7-8)

```
□ Sistema de context_id en URLs
□ Filtrado de retrieval por contexto
□ UI para crear/editar instancias
□ Estadísticas por instancia
```

### Fase 4: Funcionalidades Avanzadas (Semana 9-12)

```
□ Inbox triage con IA
□ Videollamadas + booking
□ Speaker diarization
□ Feedback widget
□ Insights dashboard (FAQs, gaps, audiencia)
□ Impersonation mode
□ PostHog + Sentry
□ Intercom/Crisp
```

---

## 8. Estimación de Costes (MVP)

| Servicio | Plan | Coste mensual |
|----------|------|--------------|
| Vercel | Pro | €20 |
| Neon | Scale | €25+ |
| OpenAI (embeddings + chat) | Pay-as-you-go | €50-200 |
| Anthropic Claude | API | €30-150 |
| Stripe | Pay-as-you-go | 2.9% + 0.30€ |
| Sentry | Free tier | €0 |
| PostHog | Free tier (1M events) | €0 |
| Dominio | .com | €15/año |
| **Total MVP** | | **~€125-400/mes** |

---

## 9. Lo que NO Hace myownclone (Oportunidades)

1. **No tiene API pública** — oportunidad para diferenciarse con API-first
2. **No tiene self-service** — onboarding es manual (beta), oportunidad para automatizar
3. **No tiene móvil nativa** — solo web responsive
4. **No tiene integración con WhatsApp/Telegram** del clon
5. **No tiene fine-tuning real** — solo RAG, no modelos fine-tuneados con la voz del creador
6. **No es open-source** — oportunidad de comunidad/open-core
7. **No tiene marketplace de clones** — solo B2B2C

---

## 10. Referencias

- [[myownclone]] — página principal de la empresa
- [[retrieval-augmented-cognition]] — deep dive del RAC
- [[ai-clones-market]] — panorama competitivo
- [[ai-clones]] — concepto general
- [[multi-tenant-saas]] — arquitectura multi-tenant

---

## Anexo: Estructura de Archivos Inferida

```
/
├── app/
│   ├── (marketing)/
│   │   ├── page.tsx              # Landing ES
│   │   ├── layout.tsx
│   │   ├── contacto/page.tsx
│   │   ├── login/page.tsx
│   │   └── en/
│   │       ├── page.tsx          # Landing EN
│   │       └── ...
│   ├── (app)/
│   │   └── [slug]/
│   │       ├── page.tsx          # Chat del clon
│   │       └── layout.tsx
│   ├── admin/
│   │   ├── page.tsx              # Dashboard
│   │   ├── clone/page.tsx
│   │   ├── brain/page.tsx
│   │   ├── inbox/
│   │   │   └── triage/page.tsx
│   │   ├── meetings/page.tsx
│   │   ├── platform/
│   │   │   ├── page.tsx
│   │   │   └── tenants/page.tsx
│   │   └── ...
│   └── api/
│       ├── webhooks/stripe/route.ts
│       ├── chat/route.ts         # Streaming chat
│       └── ...
├── lib/
│   ├── db.ts                     # Neon connection
│   ├── auth.ts                   # NextAuth config
│   ├── retrieval.ts              # RAC logic
│   ├── embeddings.ts             # OpenAI embeddings
│   ├── llm.ts                    # Claude + OpenAI clients
│   ├── stripe.ts                 # Stripe SDK
│   └── tenant.ts                 # Multi-tenant middleware
├── components/
│   ├── chat/
│   │   ├── chat-interface.tsx
│   │   ├── message-bubble.tsx
│   │   └── silo-toggle.tsx
│   ├── admin/
│   │   ├── sidebar.tsx
│   │   ├── impersonation-banner.tsx
│   │   └── ...
│   └── ui/                       # Design system
├── middleware.ts                  # Tenant routing + auth
├── next.config.ts
├── tailwind.config.ts
└── package.json
```
