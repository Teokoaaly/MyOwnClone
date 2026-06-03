# PLAN MAESTRO — Clon de IA para Infoproductores (Réplica de Clonify.com)

**Fecha:** 2026-05-26
**Basado en:** Ingeniería inversa completa de Clonify.com (2.6MB de RSC payloads + 10 rutas admin + i18n completo)
**Objetivo:** Construir un SaaS multi-tenant funcional que compita con Clonify.com en el mercado hispanohablante.

---

## 1. VISIÓN DEL PRODUCTO

Plataforma SaaS multi-tenant donde infoproductores crean clones de IA entrenados con su propio contenido (vídeos, PDFs, cursos, emails). El clon atiende 24/7 en 3 modos: Pedagogía, Ventas y Soporte. El diferenciador frente a chatbots genéricos: RAG pipeline con anti-alucinación, email triage automático, y booking + videollamada integrados.

**Nombre propuesto:** Réplica ("Multiplícate")

---

## 2. STACK TECNOLÓGICO DEFINITIVO

| Capa | Tecnología | Justificación |
|------|-----------|---------------|
| Frontend | Next.js 14 App Router + TypeScript + Tailwind CSS | Clonify usa esto. RSC + App Router es el estándar. |
| Hosting | Vercel (prod) / Coolify (VPS propio para reducir costes) | Vercel para MVP rápido, migrar a Coolify cuando escale. |
| DB | Supabase (PostgreSQL + pgvector) | Neon es alternativo; Supabase ofrece auth + storage + realtime en un solo servicio. |
| Auth | NextAuth.js v4 + OTP email + Google OAuth | Clonify usa esto. OTP sin contraseña reduce fricción. |
| LLM principal | Anthropic Claude 3.5 Sonnet (chat) | Clonify usa Claude. Mejor anti-alucinación que GPT-4 para RAG. |
| Embeddings | OpenAI text-embedding-3-small (1536d) | Mejor relación calidad/precio para español. |
| Pagos | Stripe Checkout + Customer Portal + Webhooks | Estándar. Soportado por Vercel. |
| Email outbound | Resend (SDK React) | Mejor DX que SendGrid, mismo precio. |
| Email inbound | SendGrid Inbound Parse → webhook | Única opción sólida para recibir emails programáticamente. |
| Video | Whereby (embeddable, sin SDK pesado) | Alternativa a Daily.co. Iframe embed es trivial. |
| TTS/STT | OpenAI Whisper (STT) + ElevenLabs (TTS) | Whisper para transcripción; ElevenLabs para voz del clon. |
| Monitoring | Sentry | Clonify expuso su DSN; nosotros lo configuraremos correctamente. |
| Analytics | PostHog (self-hosted o cloud) | Alternativa open-source a Mixpanel/Amplitude. |
| i18n | next-intl | Clonify tiene /es y /en. Empezamos solo con español, i18n desde día 1. |
| ORM | Drizzle ORM + drizzle-kit | Tipado completo, mejor DX que Prisma para PostgreSQL. |
| Rate limiting | Vercel KV + @upstash/ratelimit | Protege APIs sin Redis propio. |

---

## 3. ARQUITECTURA DEL SISTEMA

```
┌──────────────────────────────────────────────────────────────┐
│                     Vercel Edge / Coolify                     │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  [slug].tudom │  │  api.tudomin │  │  admin.tudominio  │  │
│  │  inio.com     │  │  io.com      │  │  .com             │  │
│  │  (chat público│  │  (dashboard  │  │  (admin plataforma│  │
│  │   del clon)   │  │   creador)   │  │   multi-tenant)   │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬──────────┘  │
│         │                 │                    │              │
│         └─────────────────┼────────────────────┘              │
│                           │                                   │
│              ┌────────────┴────────────┐                      │
│              │    Next.js API Routes   │                      │
│              │   + Server Actions      │                      │
│              └────────────┬────────────┘                      │
│                           │                                   │
│         ┌─────────────────┼─────────────────┐                 │
│         │                 │                 │                 │
│    ┌────▼────┐    ┌───────▼──────┐    ┌─────▼─────┐          │
│    │Supabase │    │  Anthropic   │    │  Stripe   │          │
│    │PostgreSQL│   │  Claude +    │    │  Payments │          │
│    │+pgvector│    │  OpenAI Embed│    │           │          │
│    └─────────┘    └──────────────┘    └───────────┘          │
│                                                               │
│    ┌─────────┐    ┌──────────────┐    ┌─────────────┐        │
│    │ Resend  │    │SendGrid Inb. │    │  Whereby    │        │
│    │(outbound│    │ Parse (inb.) │    │  (video)    │        │
│    │ email)  │    │              │    │             │        │
│    └─────────┘    └──────────────┘    └─────────────┘        │
└──────────────────────────────────────────────────────────────┘
```

### Flujo RAG (Corazón del producto)

```
Contenido (YouTube, PDFs, texto, vídeos)
    │
    ▼
Transcripción (Whisper para audio/vídeo)
    │
    ▼
Chunking (500-1000 tokens, overlap 100 tokens)
    │
    ▼
Embeddings (OpenAI text-embedding-3-small → 1536d)
    │
    ▼
pgvector (índice IVFFlat/HNSW, cosine similarity)
    │
    ▼
Usuario pregunta → Embedding query → top_k=5 chunks
    │
    ▼
System prompt (modo: pedagogía/ventas/soporte) + chunks + historial
    │
    ▼
Claude 3.5 Sonnet → respuesta + confidence_score
    │
    ├── confidence ≥ 0.7 → Responde
    └── confidence < 0.7 → "No tengo suficiente información"
                           → Notifica al creador (gap de conocimiento)
                           → Sugiere añadir contenido relacionado
```

### Modelo de datos principal

```
tenants
  id, slug, name, plan, status, created_at

users
  id, tenant_id, email, name, role (owner/admin/member), created_at

clones
  id, tenant_id, name, personality, tone, language, active, created_at

clone_modes
  id, clone_id, mode (pedagogy/sales/support), system_prompt, active

sources
  id, clone_id, type (youtube/pdf/video/text/web), title, url, status, created_at

chunks
  id, source_id, content, embedding (vector 1536d), token_count, metadata

memories (brain)
  id, clone_id, content, type (memory/signature/template), trigger_condition, created_at

conversations
  id, clone_id, visitor_id, mode, created_at

messages
  id, conversation_id, role (user/assistant), content, confidence, sources (json)

emails (inbox)
  id, clone_id, from, subject, body, draft_reply, status (pending/sent/discarded), created_at

meeting_types
  id, clone_id, name, duration, price, description, active

availability
  id, clone_id, day_of_week, start_time, end_time

bookings
  id, meeting_type_id, visitor_name, visitor_email, date, time, status, meeting_url

products
  id, clone_id, name, description, price, url, active

analytics_questions
  id, clone_id, question, count, last_asked_at

analytics_gaps
  id, clone_id, question, count, suggested_source
```

---

## 4. PLAN DE CONSTRUCCIÓN (8 FASES, 6 SEMANAS)

### FASE 0: Setup del Proyecto (Día 1)

**Tareas:**
- [ ] `npx create-next-app@latest replica --typescript --tailwind --eslint --app --src-dir`
- [ ] Configurar ESLint + Prettier + Husky pre-commit hooks
- [ ] Configurar `tsconfig.json` strict, path aliases (`@/components`, `@/lib`, etc.)
- [ ] Crear proyecto Supabase + obtener connection string
- [ ] Configurar Drizzle ORM + drizzle-kit + schema inicial
- [ ] Configurar variables de entorno (`.env.example`)
- [ ] Configurar Sentry + PostHog
- [ ] Configurar next-intl con locale `es`
- [ ] Desplegar en Vercel (dominio: replica.tudominio.com)
- [ ] Configurar GitHub Actions CI/CD (lint, typecheck, build)

**Entregables:** Repo funcional en Vercel con /, /es/hello mostrando datos desde Supabase.

---

### FASE 1: Auth + Multi-tenant (Semana 1)

**Objetivo:** Sistema completo de autenticación y gestión de tenants con subdominios.

**Tareas:**
- [ ] Configurar NextAuth.js con:
  - [ ] Email provider (OTP magic link vía Resend)
  - [ ] Google OAuth provider
  - [ ] JWT strategy (no base de datos de sesiones)
  - [ ] Cookies HttpOnly + SameSite=Strict
- [ ] Schema Drizzle: `tenants`, `users`, `accounts`, `verification_tokens`
- [ ] Crear tenant en registro (slug único, validación)
- [ ] Middleware.ts: validar subdominio + redirigir según auth
- [ ] Flujo de registro en `/es/registro`:
  - [ ] Email + nombre → OTP → verificar → crear tenant + user
  - [ ] O "Continuar con Google" → crear tenant con slug=[nombre]
- [ ] Flujo de login en `/es/login`
- [ ] Página de onboarding post-registro:
  - [ ] Elegir slug (ej: `juanperez.replica.tudominio.com`)
  - [ ] Elegir nombre del clon
  - [ ] Seleccionar plan (trial 14 días con Stripe)
- [ ] Protección de rutas: `/api/*` solo autenticado + mismo tenant
- [ ] Rate limiting en /api/auth/* (5 intentos/min por IP)

**Entregables:** Usuario puede registrarse, verificar email, crear tenant con slug, login/logout, ver dashboard vacío en `api.tudominio.com`.

---

### FASE 2: Vector DB + RAG Pipeline (Semana 1-2)

**Objetivo:** Pipeline completo de ingesta → embeddings → búsqueda → respuesta con un solo modo (pedagogía).

**Tareas:**
- [ ] Habilitar extensión pgvector en Supabase
- [ ] Schema Drizzle: `sources`, `chunks` (con columna `embedding vector(1536)`)
- [ ] Índice IVFFlat/HNSW en `chunks.embedding` para cosine similarity
- [ ] Módulo `lib/rag/ingest.ts`:
  - [ ] `chunkText(text, maxTokens=800, overlap=100)` — sliding window con tiktoken
  - [ ] `generateEmbeddings(chunks[])` — OpenAI text-embedding-3-small (batch de 20)
  - [ ] `storeChunks(sourceId, chunksWithEmbeddings)` — insert en Supabase
- [ ] Módulo `lib/rag/retrieve.ts`:
  - [ ] `searchSimilar(query, cloneId, topK=5)` — cosine similarity via pgvector
  - [ ] Umbral de similitud mínima (0.75)
- [ ] Módulo `lib/rag/generate.ts`:
  - [ ] `buildSystemPrompt(clone, mode, memories)` — armar prompt desde DB
  - [ ] `generateResponse(query, chunks, systemPrompt, history)` → Anthropic Claude
  - [ ] `extractConfidence(response)` — parsear confidence_score del output
- [ ] Módulo `lib/rag/pipeline.ts`:
  - [ ] Función orquestadora: embed query → search → build prompt → generate → check confidence → respond or fallback
- [ ] Endpoint: `POST /api/clone/[slug]/chat` (público, sin auth)
  - [ ] Acepta `{ message, conversationId?, context? }`
  - [ ] Contexto opcional por URL: `?context=clase-4` limita búsqueda a esa fuente
- [ ] Test unitario con contenido de ejemplo (PDF de prueba)

**Entregables:** Se puede hacer curl a `/api/clone/test/chat` con `{"message": "¿De qué trata el curso?"}` y obtener respuesta basada en contenido ingerido.

---

### FASE 3: Chat UI Pública (Semana 2)

**Objetivo:** Widget de chat embebible + página pública del clon con interfaz completa.

**Tareas:**
- [ ] Página pública del clon: `[slug].tudominio.com` (middleware routing)
  - [ ] UI: avatar del clon (gradiente animado), nombre, descripción
  - [ ] Chat en tiempo real (WebSocket o SSE para streaming de respuesta)
- [ ] Componente `ChatWidget`:
  - [ ] Lista de mensajes con scroll automático
  - [ ] Input de texto + botón enviar
  - [ ] Indicador "escribiendo..." con animación de puntos
  - [ ] Soporte para markdown en respuestas (código, listas, negritas)
  - [ ] Botón "Nueva conversación" (resetea historial)
  - [ ] Estados: loading, error, empty, success
- [ ] Notas de voz:
  - [ ] Botón micrófono → MediaRecorder API → blob webm
  - [ ] Enviar blob a `/api/stt` → Whisper → texto
  - [ ] Mostrar transcripción + enviarla al chat
- [ ] Widget embebible:
  - [ ] Script `<script src="https://replica.tudominio.com/widget.js" data-clone="slug"></script>`
  - [ ] Botón flotante en esquina inferior derecha
  - [ ] Iframe o Shadow DOM para aislamiento de estilos
- [ ] Persistencia de conversaciones (localStorage para visitantes, DB para usuarios)
- [ ] Feedback en respuestas (👍/👎) → guardar para analytics

**Entregables:** Demo funcional: visitar `juanperez.replica.tudominio.com` y chatear con el clon. Widget funciona en un HTML externo.

---

### FASE 4: Dashboard del Creador (Semana 2-3)

**Objetivo:** Panel completo donde el creador gestiona contenido, brain, y ve analíticas. 36 secciones agrupadas en módulos.

**Tareas:**

#### 4.1 Layout + Navegación
- [ ] Layout `DashboardLayout` con sidebar colapsable (móvil: drawer)
- [ ] Breadcrumbs dinámicos
- [ ] Avatar + menú de usuario (perfil, billing, logout)
- [ ] Selector de clon (si multi-clon en plan Enterprise)

#### 4.2 Biblioteca de Contenido (AdminBiblioteca)
- [ ] Subir PDF: drag & drop → Supabase Storage → extraer texto (pdf-parse)
- [ ] Subir YouTube: pegar URL → ytdl-core o youtube-transcript → extraer transcripción
- [ ] Subir vídeo: Supabase Storage → Whisper transcripción
- [ ] Subir texto: textarea, markdown
- [ ] Subir URL: scraping server-side (cheerio)
- [ ] Entrevista AI: agente Claude que entrevista al creador para extraer conocimiento
- [ ] Carpeta de cursos (módulos con vídeos)
- [ ] Estados: uploading → processing → ready → error → reprocess
- [ ] Progreso de ingesta en tiempo real (SSE)
- [ ] Panel de búsqueda y filtrado por tipo/estado

#### 4.3 Cerebro / Brain (AdminCerebro)
- [ ] CRUD de Memorias (fragmentos de texto inyectados en el prompt)
- [ ] CRUD de Firmas (HTML para cierre de emails)
- [ ] CRUD de Plantillas (respuestas reutilizables con trigger)
  - [ ] Condición "cuándo usar": palabras clave, tipo de consulta, etc.
- [ ] Vista previa de cómo afecta cada memoria al prompt final

#### 4.4 Gestión del Clon (AdminClon, AdminIdentidad, AdminEstilo, AdminProposito)
- [ ] Nombre, descripción, avatar (upload a Supabase Storage)
- [ ] Personalidad y tono (sliders: formal↔informal, serio↔divertido, etc.)
- [ ] Propósito principal (pedagogía/ventas/soporte)
- [ ] Configuración de modos activos
- [ ] System prompts editables por modo
- [ ] Configuración de subdominio (AdminTenantSlug)
- [ ] Vista previa del clon en tiempo real (iframe)

#### 4.5 Productos (AdminProductos)
- [ ] CRUD de productos/servicios
- [ ] Campos: nombre, descripción, precio, URL de venta, imagen
- [ ] Activar/desactivar para recomendación
- [ ] Prioridad de recomendación (drag & drop)

#### 4.6 Analíticas (AdminResumen, AdminAprendizajes, AdminUso)
- [ ] Dashboard principal (AdminResumen):
  - [ ] Widgets: conversaciones totales, mensajes, preguntas respondidas, gaps
  - [ ] Gráfica de actividad (últimos 7/30/90 días)
  - [ ] Top 10 preguntas frecuentes
- [ ] Aprendizajes (AdminAprendizajes):
  - [ ] Tabla de gaps de conocimiento (preguntas sin respuesta)
  - [ ] Acción rápida: "Añadir contenido" para tapar cada gap
  - [ ] Análisis del avatar de audiencia
- [ ] Uso (AdminUso):
  - [ ] Consumo actual vs límite del plan: palabras training, respuestas, emails
  - [ ] Costes desglosados: Claude API, OpenAI embeddings, Supabase, etc.
  - [ ] Proyección mensual

#### 4.7 Contactos + Conversaciones (AdminContactos, AdminConversaciones)
- [ ] Lista de contactos con historial de conversaciones
- [ ] Búsqueda y filtrado
- [ ] Vista de conversación individual (transcripción completa)
- [ ] Exportar conversación (PDF/JSON)

#### 4.8 Facturación (AdminFacturas, AdminPlan)
- [ ] Plan actual + límites
- [ ] Historial de facturas (Stripe)
- [ ] Cambiar de plan (redirigir a Stripe Customer Portal)
- [ ] Cancelar suscripción
- [ ] Método de pago

**Entregables:** Dashboard completo con sidebar, biblioteca funcional, brain, analíticas básicas, gestión de clon. Creador puede subir contenido y ver resultados.

---

### FASE 5: Inbox / Email Triage (Semana 3-4)

**Objetivo:** El clon recibe emails, propone respuestas, el creador las revisa y envía. Killer feature de Clonify.

**Tareas:**
- [ ] Configurar SendGrid Inbound Parse:
  - [ ] MX records apuntando a SendGrid
  - [ ] Webhook endpoint: `POST /api/inbound-email`
  - [ ] Verificar firma de SendGrid (seguridad)
- [ ] Procesar email entrante:
  - [ ] Extraer `from`, `subject`, `body` (texto plano + HTML)
  - [ ] Detectar tenant por dominio (configurable en dashboard)
  - [ ] Guardar en `emails` table con estado `pending`
- [ ] Generar draft de respuesta (Claude):
  - [ ] Prompt: "Eres el clon de [nombre]. Responde a este email en su tono. Contexto: [memorias+firmas+plantillas]. Email original: [contenido]"
  - [ ] Aplicar firma configurada
  - [ ] Guardar draft en `emails.draft_reply`
- [ ] UI del Inbox (AdminInbox):
  - [ ] Vista dividida: lista de emails | vista previa + draft
  - [ ] Filtros: pendientes, enviados, descartados
  - [ ] Búsqueda por asunto/remitente
  - [ ] Editor de draft (textarea con markdown)
  - [ ] Botones: "Enviar" (vía Resend), "Descartar", "Editar y enviar"
  - [ ] Al enviar, guardar como plantilla automáticamente
- [ ] Configuración de inbox por clon:
  - [ ] Email address a monitorizar
  - [ ] Firma personalizada
  - [ ] Auto-responder (on/off)

**Entregables:** Email recibido en `juan@clon.tudominio.com` → aparece en inbox → clon propone respuesta → creador envía con un clic.

---

### FASE 6: Stripe + Planes (Semana 4)

**Objetivo:** Monetización completa con planes, trials, webhooks y gestión de suscripciones.

**Tareas:**
- [ ] Configurar Stripe:
  - [ ] Productos + precios en dashboard Stripe:
    - Básico: 49€/mes
    - Pro: 99€/mes
    - Escala: 199€/mes
    - Enterprise: 499€/mes (custom quote)
  - [ ] Stripe Checkout Session (modo suscripción)
  - [ ] Customer Portal (para cambios de plan, cancelación, facturas)
- [ ] Flujo de pago:
  - [ ] Trial 14 días con tarjeta → `POST /api/stripe/checkout`
  - [ ] Cortesías sin tarjeta (admin platform) → `POST /api/admin/platform/courtesies`
  - [ ] Redirigir a Stripe Checkout
  - [ ] Success/cancel URLs → actualizar tenant plan
- [ ] Webhooks Stripe (endpoint: `/api/stripe/webhook`):
  - [ ] `checkout.session.completed` → activar tenant
  - [ ] `customer.subscription.updated` → actualizar plan/límites
  - [ ] `customer.subscription.deleted` → downgrade a plan básico
  - [ ] `invoice.payment_failed` → notificar usuario (email Resend)
- [ ] Planes y límites:
  - [ ] Tabla `plans` con límites por recurso
  - [ ] Middleware de cuota: verificar antes de cada operación
  - [ ] Banner de cuota en dashboard (AdminQuotaBanner)
  - [ ] Tracking de uso en tiempo real vía Supabase counters
- [ ] UI de facturación:
  - [ ] Historial de facturas desde Stripe API
  - [ ] Descargar PDF de factura

**Entregables:** Flujo completo: registro → trial Stripe → pago → acceso Pro. Webhooks actualizan estado automáticamente.

---

### FASE 7: Booking + Videollamada (Semana 5)

**Objetivo:** Sistema de reserva de reuniones con videollamada integrada y grabación.

**Tareas:**
- [ ] Gestión de tipos de reunión (AdminMeetingTypes):
  - [ ] CRUD: nombre, duración (15/30/60 min), precio (0 = gratis), descripción
  - [ ] Color/branding por tipo
  - [ ] Preguntas personalizadas para el formulario de reserva
- [ ] Disponibilidad (AdminAvailability):
  - [ ] Selector semanal: días + horas (ej: Lun-Vie 9:00-18:00)
  - [ ] Múltiples franjas por día
  - [ ] Timezone del creador
  - [ ] Días bloqueados (vacaciones, festivos)
  - [ ] Buffer entre reuniones (ej: 15 min)
- [ ] Página pública de reserva (PublicBooking):
  - [ ] URL: `[slug].tudominio.com/reservar`
  - [ ] Selector de tipo de reunión
  - [ ] Calendario con slots disponibles (usando la configuración de disponibilidad)
  - [ ] Deshabilitar slots pasados
  - [ ] Formulario: nombre, email, notas, respuestas a preguntas personalizadas
  - [ ] Confirmación: "Reunión agendada" + email de confirmación (Resend) + ICS
- [ ] Videollamada (Whereby):
  - [ ] Crear sala al confirmar booking (Whereby API: `POST /meetings`)
  - [ ] URL de sala guardada en `bookings.meeting_url`
  - [ ] Página MeetingRoom: iframe de Whereby + chat contextual con el clon
  - [ ] Verificar que la sala funciona
- [ ] Post-reunión:
  - [ ] Grabación de Whereby → webhook → descargar → Supabase Storage
  - [ ] Transcripción con Whisper
  - [ ] Indexar transcripción en Vector DB (se convierte en fuente de conocimiento)
  - [ ] Página PublicRecording: grabación + chat con el clon (sabe lo que se dijo)
- [ ] Gestión de reservas (AdminReuniones, AdminAgenda, AdminLlamada):
  - [ ] Vista de calendario (react-big-calendar o similar)
  - [ ] Lista de próximas reservas
  - [ ] Cancelar/reprogramar
  - [ ] Ver grabaciones pasadas

**Entregables:** Visitante agenda reunión con el creador → videollamada en Whereby → grabación se transcribe y alimenta al clon → el clon ahora sabe lo que se habló.

---

### FASE 8: Admin de Plataforma (Semana 6)

**Objetivo:** Panel de administración multi-tenant para gestionar toda la plataforma.

**Tareas:**
- [ ] Middleware de admin (solo usuarios con role=platform_admin)
- [ ] Resumen de plataforma (AdminPlatformResumen):
  - [ ] MRR total desglosado por plan
  - [ ] Costes de plataforma (Claude, OpenAI, Supabase, etc.)
  - [ ] Margen = MRR - costes
  - [ ] Gráficas temporales (Chart.js o Recharts)
  - [ ] Widgets: tenants activos, trials activos, churn rate
- [ ] Gestión de tenants (AdminPlatformTenants):
  - [ ] Tabla paginada con búsqueda y filtros (plan, estado, fecha)
  - [ ] Columnas: nombre, slug, plan, MRR, costes, conversaciones, emails, última actividad
  - [ ] Ordenación por cualquier columna
  - [ ] Ver detalle de tenant (dashboard del creador en modo vista)
  - [ ] Suspender/activar tenant
- [ ] Suplantación (Impersonation):
  - [ ] Botón "Suplantar" → modal con motivo
  - [ ] Login como el usuario del tenant
  - [ ] Banner rojo fijo: "Suplantando a [tenant] — [motivo] — [temporizador 30min]"
  - [ ] Audit log: quién, a quién, cuándo, motivo
  - [ ] Timeout automático a los 30 minutos
- [ ] Concesión de cortesías:
  - [ ] Invitar nuevo tenant sin Stripe (cortesía)
  - [ ] Seleccionar plan, duración de cortesía
  - [ ] Email de invitación personalizado
- [ ] Inbox global (AdminPlatformInbox):
  - [ ] Todos los emails de *@replica.tudominio.com
  - [ ] Filtro por tenant
  - [ ] Gestión de spam: dominios bloqueados (AdminPlatformSpam)
- [ ] Feedback de plataforma (AdminPlatformFeedback):
  - [ ] Ver errores/sugerencias de usuarios
  - [ ] Estados: pendiente, en progreso, resuelto
  - [ ] Responder al usuario desde el panel

**Entregables:** Admin puede ver MRR, gestionar tenants, suplantar para soporte, conceder cortesías, y revisar feedback. Panel de control completo del negocio.

---

## 5. FASES POST-MVP (Semana 7+)

### FASE 9: Whitelabel + API Pública
- Dominios personalizados (CNAME → nuestro servidor)
- CSS custom por tenant (colores, fuentes, logos)
- API REST para desarrolladores (generar API keys, documentación)
- Webhooks salientes (eventos: conversación.creada, email.recibido, etc.)

### FASE 10: Multi-clon + Enterprise
- Un tenant → múltiples clones (ej: uno por producto)
- Roles de equipo (owner, admin, member, viewer)
- SSO empresarial (SAML/OIDC)
- SLA + soporte prioritario

### FASE 11: Marketplace + Integraciones
- Integraciones nativas: Slack, WhatsApp, Telegram, Messenger
- Zapier/Make connector
- Marketplace de plantillas de clon (por industria)
- Comunidad de creadores

---

## 6. RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Costes Claude API se disparan | Alta | Alto | Límites por plan + caching de respuestas frecuentes + Claude Haiku para consultas simples |
| Supabase rate limits en pgvector | Media | Medio | Batch inserts + cola de ingesta (BullMQ/Upstash) + monitoreo de uso |
| Complejidad multi-tenant demasiado pronto | Alta | Alto | Empezar con single-tenant en Fase 1, añadir multi-tenant en Fase 2 |
| Stripe complejidad fiscal (UE VAT) | Media | Medio | Usar Stripe Tax (automático) desde día 1 |
| Seguridad (vulnerabilidades Clonify) | Alta | Crítico | NO cometer los mismos errores: CSRF tokens, CSP headers, rate limiting, auth en todas las rutas admin desde día 1 |
| Donde compite Clonify directamente | Alta | Medio | Diferenciarnos: mejor UX, onboarding más rápido, precios en €, foco en español, email triage mejorado |
| Supabase vendor lock-in | Baja | Alto | Schema Drizzle portable, pgvector es estándar PostgreSQL, migración posible a Neon/RDS |

---

## 7. MÉTRICAS DE ÉXITO

### Técnicas
- [ ] Time to first response < 3s (con streaming se siente instantáneo)
- [ ] Uptime > 99.5% (Vercel/Coolify)
- [ ] Embedding generation < 1s por chunk
- [ ] RAG accuracy > 85% (respuestas correctas basadas en contenido)
- [ ] Anti-alucinación: 0 falsos positivos (nunca inventa)

### Negocio
- [ ] 10 clientes de pago en mes 1
- [ ] MRR > 500€ en mes 2
- [ ] Churn < 5% mensual
- [ ] NPS > 50

---

## 8. ORDEN DE PRIORIDAD PARA MVP (LO MÍNIMO PARA LANZAR)

Si el objetivo es lanzar rápido, reducir a:

1. **Fase 0-1**: Setup + Auth + Tenant (1 semana)
2. **Fase 2**: Vector DB + RAG pipeline (3 días)
3. **Fase 3**: Chat UI + widget (3 días)
4. **Fase 4 parcial**: Solo biblioteca (YouTube + PDF) + analíticas básicas (4 días)
5. **Fase 6**: Stripe + planes (2 días)
6. **Deploy**: Lanzamiento con early adopters (1 día)

**Total MVP: ~2 semanas para un producto funcional que ya se puede vender.**

Características que pueden esperar a post-lanzamiento:
- Email triage (Fase 5)
- Booking + video (Fase 7)
- Admin platform (Fase 8)
- Notas de voz
- Entrevista AI
- Whitelabel

---

## 9. REGLAS DE ORO (APRENDIDAS DE LOS ERRORES DE CLONIFY)

> **NUNCA** cometas estos errores:

1. ❌ **Servir código admin sin autenticación** → ✅ Middleware estricto en TODAS las rutas `/admin/*` y `/api/admin/*`
2. ❌ **Exponer Sentry DSN en meta tags** → ✅ Cargar Sentry solo en el cliente, DSN en variable de entorno
3. ❌ **CORS wildcard en producción** → ✅ `Access-Control-Allow-Origin` restringido a dominios conocidos
4. ❌ **APIs admin sin CSRF** → ✅ Tokens CSRF en todas las mutaciones POST/PUT/DELETE
5. ❌ **Sin rate limiting** → ✅ Rate limit en auth, API, y endpoints públicos (Vercel KV + Upstash)
6. ❌ **Cabeceras de seguridad ausentes** → ✅ CSP, X-Frame-Options, X-Content-Type-Options, HSTS desde día 1
7. ❌ **Logs de errores sin filtrar** → ✅ Sanitizar datos sensibles antes de enviar a Sentry
8. ❌ **Source maps en producción** → ✅ Deshabilitar `productionBrowserSourceMaps` en Next.js

---

## 10. ESTRUCTURA DEL PROYECTO

```
replica/
├── src/
│   ├── app/                          # Next.js App Router
│   │   ├── (public)/                 # Rutas públicas (sin auth)
│   │   │   ├── [slug]/               # Chat público del clon
│   │   │   │   ├── page.tsx
│   │   │   │   └── reservar/page.tsx
│   │   │   └── widget.js/route.ts    # Script embebible
│   │   ├── (dashboard)/              # Rutas del creador (auth required)
│   │   │   ├── (main)/               # Layout con sidebar
│   │   │   │   ├── biblioteca/
│   │   │   │   ├── cerebro/
│   │   │   │   ├── inbox/
│   │   │   │   ├── productos/
│   │   │   │   ├── reuniones/
│   │   │   │   ├── analiticas/
│   │   │   │   ├── facturacion/
│   │   │   │   └── configuracion/
│   │   │   ├── login/page.tsx
│   │   │   └── registro/page.tsx
│   │   ├── (admin)/                  # Rutas admin plataforma
│   │   │   ├── tenants/
│   │   │   ├── resumen/
│   │   │   └── feedback/
│   │   └── api/
│   │       ├── auth/[...nextauth]/   # NextAuth
│   │       ├── clone/[slug]/chat/    # Chat RAG público
│   │       ├── stt/                  # Whisper STT
│   │       ├── stripe/               # Checkout + webhooks
│   │       ├── inbound-email/        # SendGrid webhook
│   │       ├── bookings/             # CRUD reservas
│   │       └── admin/                # APIs admin plataforma
│   ├── components/
│   │   ├── ui/                       # Componentes genéricos (shadcn/ui)
│   │   ├── chat/                     # ChatWidget, MessageBubble, etc.
│   │   ├── dashboard/                # Sidebar, Shell, breadcrumbs
│   │   ├── clone/                    # Configuración del clon
│   │   ├── inbox/                    # Email list, draft editor
│   │   ├── booking/                  # Calendar, slot picker
│   │   └── admin/                    # Impersonation banner, MRR charts
│   ├── lib/
│   │   ├── rag/                      # Pipeline RAG
│   │   │   ├── ingest.ts
│   │   │   ├── retrieve.ts
│   │   │   ├── generate.ts
│   │   │   └── pipeline.ts
│   │   ├── db/                       # Drizzle ORM
│   │   │   ├── schema/
│   │   │   │   ├── tenants.ts
│   │   │   │   ├── users.ts
│   │   │   │   ├── clones.ts
│   │   │   │   ├── sources.ts
│   │   │   │   ├── chunks.ts
│   │   │   │   ├── conversations.ts
│   │   │   │   ├── emails.ts
│   │   │   │   ├── bookings.ts
│   │   │   │   └── analytics.ts
│   │   │   ├── index.ts              # db connection + client
│   │   │   └── migrate.ts
│   │   ├── auth.ts                   # NextAuth config
│   │   ├── stripe.ts                 # Stripe client + helpers
│   │   ├── email.ts                  # Resend + SendGrid helpers
│   │   ├── storage.ts                # Supabase Storage helpers
│   │   ├── video.ts                  # Whereby API helpers
│   │   ├── stt.ts                    # Whisper API helpers
│   │   ├── quotas.ts                 # Límites por plan
│   │   └── utils.ts                  # Utilidades generales
│   ├── middleware.ts                 # Subdominios + auth redirects
│   └── i18n/
│       ├── es.json                   # Español (prioritario)
│       └── en.json                   # Inglés (futuro)
├── supabase/
│   └── migrations/                   # Migraciones SQL
├── public/
│   ├── widget.js                     # Script del widget embebible
│   └── favicon.ico
├── .env.example
├── drizzle.config.ts
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
├── package.json
└── README.md
```

---

## 11. VARIABLES DE ENTORNO (.env.example)

```env
# Supabase
DATABASE_URL=postgresql://...
SUPABASE_URL=https://...
SUPABASE_ANON_KEY=...
SUPABASE_SERVICE_ROLE_KEY=...

# NextAuth
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=

# Anthropic
ANTHROPIC_API_KEY=sk-ant-...

# OpenAI (embeddings + Whisper)
OPENAI_API_KEY=sk-...

# Stripe
STRIPE_SECRET_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_live_...
STRIPE_BASIC_PRICE_ID=price_...
STRIPE_PRO_PRICE_ID=price_...
STRIPE_SCALE_PRICE_ID=price_...

# Resend (email outbound)
RESEND_API_KEY=re_...
RESEND_FROM_EMAIL=noreply@replica.tudominio.com

# SendGrid (email inbound)
SENDGRID_INBOUND_WEBHOOK_SECRET=...

# Whereby (video)
WHEREBY_API_KEY=...

# Sentry
NEXT_PUBLIC_SENTRY_DSN=https://...
SENTRY_ORG=...
SENTRY_PROJECT=...

# PostHog
NEXT_PUBLIC_POSTHOG_KEY=phc_...
NEXT_PUBLIC_POSTHOG_HOST=https://...

# App
NEXT_PUBLIC_APP_URL=https://replica.tudominio.com
NEXT_PUBLIC_API_URL=https://api.replica.tudominio.com
NEXT_PUBLIC_ADMIN_URL=https://admin.replica.tudominio.com
```

---

## 12. SIGUIENTES PASOS INMEDIATOS

1. Crear el proyecto Next.js con `create-next-app`
2. Crear proyecto Supabase y configurar pgvector
3. Configurar Drizzle ORM con los schemas de la Fase 0-1
4. Implementar NextAuth.js con OTP email
5. Configurar el pipeline de CI/CD en GitHub Actions

---

*Este plan maestro es el documento canónico. Cualquier decisión arquitectónica debe consultarse aquí primero.*
