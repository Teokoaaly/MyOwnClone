# 🧬 MyOwnClone — Multiply Yourself

<p align="center">
  <strong>Plataforma SaaS multi-tenant para crear, desplegar y escalar clones digitales de IA.</strong>
  <br />
  Los creadores de contenido lanzan un asistente de IA entrenado con su conocimiento
  que atiende consultas, responde correos y reserva reuniones 24/7 en su propio tono.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Next.js_16-000000?logo=next.js&logoColor=white" alt="Next.js 16" />
  <img src="https://img.shields.io/badge/React_19-61DAFB?logo=react&logoColor=black" alt="React 19" />
  <img src="https://img.shields.io/badge/TypeScript_5-3178C6?logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Tailwind_CSS_4-06B6D4?logo=tailwindcss&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Python_3.11-3776AB?logo=python&logoColor=white" alt="Python 3.11" />
  <img src="https://img.shields.io/badge/Flask_3-000000?logo=flask&logoColor=white" alt="Flask 3" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Drizzle_ORM-C5F74F?logo=drizzle&logoColor=black" alt="Drizzle ORM" />
  <img src="https://img.shields.io/badge/NextAuth_v5-000000?logo=auth0&logoColor=white" alt="NextAuth v5" />
  <img src="https://img.shields.io/badge/Stripe-008CDD?logo=stripe&logoColor=white" alt="Stripe" />
  <br />
  <img src="https://img.shields.io/badge/license-Propietaria-red" alt="License" />
  <img src="https://img.shields.io/badge/PRs-bienvenidas-brightgreen" alt="PRs welcome" />
</p>

---

## 📋 Tabla de Contenidos

- [Descripción General](#-descripción-general)
- [Características Principales](#-características-principales)
- [Stack Tecnológico](#-stack-tecnológico)
- [Arquitectura](#-arquitectura)
- [Modelo de Datos](#-modelo-de-datos)
- [Roadmap Técnico](#-roadmap-técnico)
- [Requisitos del Sistema](#-requisitos-del-sistema)
- [Instalación Local](#-instalación-local)
- [Variables de Entorno](#-variables-de-entorno)
- [Comandos de Desarrollo](#-comandos-de-desarrollo)
- [Testing](#-testing)
- [Despliegue en Producción](#-despliegue-en-producción)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API Reference](#-api-reference)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

---

## 📖 Descripción General

**MyOwnClone** es una plataforma SaaS **multi-tenant** que permite a creadores de contenido, educadores y negocios lanzar su propio **clon digital de IA**: un asistente conversacional basado en RAG (Retrieval-Augmented Generation) entrenado con su contenido, que puede operar en tres modos — **pedagogía**, **soporte** y **ventas** — con capacidades de gestión de email, reserva de reuniones y analíticas integradas.

El sistema se compone de un **frontend Next.js 16** (App Router) con autenticación, panel de administración y widget público embedible, y un **backend Flask** con pipeline RAG completo, procesamiento de email, booking y facturación Stripe. Todo sobre **PostgreSQL 15 con pgvector** para búsqueda semántica de embeddings.

---

## ✨ Características Principales

### 🧠 AI Clone Engine

| Característica | Descripción |
|---|---|
| **Modo Pedagogía** | Responde preguntas basándose en el contenido del creador (libros, PDFs, vídeos, web) |
| **Modo Soporte** | Atiende clientes 24/7 con respuestas contextuales |
| **Modo Ventas** | Asesora sobre productos y servicios, con catálogo integrado |
| **Memorias persistentes** | El clon recuerda firmas, templates y preferencias del creador |
| **Silos de conocimiento** | Aísla fuentes por temática (teach, support, sales) |
| **Streaming de respuestas** | Chat en tiempo real con SSE (Server-Sent Events) |
| **Widget embedible** | Script `<script src="widget.js">` para integración en cualquier web |

### 📬 Email Inbox Inteligente

- Recepción de emails via SendGrid Inbound Parse Webhook
- Clasificación automática y generación de borradores con IA
- Respuesta automática en el tono del creador
- Triage de emails entrantes

### 📅 Sistema de Reuniones

- Integración con Whereby para videollamadas
- Gestión de disponibilidad del creador
- Reserva de reuniones por visitantes
- Confirmaciones vía email (Resend)

### 📊 Analytics & Gap Detection

- Seguimiento de conversaciones, mensajes y sesiones activas
- Detección automática de **gaps de conocimiento** (preguntas con baja confianza)
- Sugerencia de nuevas fuentes para cubrir gaps
- Dashboard en tiempo real

### 👑 Platform Admin

- Gestión multi-tenant (crear, suspender, cancelar tenants)
- Panel de impersonación para soporte técnico
- Auditoría de acciones sensibles
- Créditos de cortesía
- Feedback de usuarios

### 💳 Billing & Planes

| Plan | Conversaciones/día | Emails/mes | Fuentes | Almacenamiento | Clones | Miembros |
|---|---|---|---|---|---|---|
| **Trial** | 50 | 20 | 5 | 100 MB | 1 | 1 |
| **Basic** | 200 | 100 | 20 | 1 GB | 1 | 1 |
| **Pro** | 1.000 | 500 | 100 | 5 GB | 3 | 3 |
| **Scale** | 5.000 | 2.000 | 500 | 25 GB | 10 | 10 |
| **Enterprise** | 50.000 | 10.000 | 2.000 | 100 GB | 50 | 50 |

### 🌐 i18n

- Español e Inglés (next-intl)
- Detección de idioma por ruta (`/es/`, `/en/`)
- Ready para expansión a más idiomas

---

## 🛠️ Stack Tecnológico

### Frontend

| Tecnología | Uso |
|---|---|
| **Next.js 16.2** (App Router) | SSR, ISR, API Routes |
| **React 19** | UI declarativa, Server Components |
| **TypeScript 5** | Tipado estático |
| **Tailwind CSS v4** | Estilos utility-first |
| **Drizzle ORM** | Tipado seguro de base de datos desde el frontend |
| **NextAuth v5** (Auth.js) | Autenticación JWT + OAuth |
| **next-themes** | Modo oscuro/claro |
| **next-intl** | Internacionalización |
| **Framer Motion** | Animaciones |
| **Recharts** | Gráficas de analytics |
| **@phosphor-icons/react** | Sistema de iconos |
| **@radix-ui/react-dialog** | Diálogos accesibles |
| **Vitest + Testing Library** | Tests unitarios y de componentes |

### Backend

| Tecnología | Uso |
|---|---|
| **Python 3.11** + **Flask 3** | API REST |
| **Flask-SQLAlchemy 3** | ORM backend |
| **Alembic / Flask-Migrate** | Migraciones |
| **Gunicorn** | WSGI server producción |
| **Flask-RESTX** | API documentation |
| **Redis 7** | Caching, rate limiting |
| **pgvector** (PostgreSQL) | Vector store para RAG |

### LLM & AI

| Servicio | Uso |
|---|---|
| **Anthropic Claude** | Generación de respuestas (chat principal) |
| **OpenAI GPT-4o-mini** | Embeddings (text-embedding-3-small) y Whisper STT |
| **OpenAI** | Fallback de generación |

### Infraestructura & Servicios

| Servicio | Uso |
|---|---|
| **PostgreSQL 15** | Base de datos principal |
| **Upstash Redis** | Rate limiting (fallback a in-memory) |
| **Supabase Storage** | Almacenamiento de archivos (PDFs, imágenes) |
| **Stripe** | Suscripciones, checkout, portal de facturación |
| **Resend** | Emails transaccionales (verificación, confirmaciones) |
| **SendGrid** | Inbound email parse (webhook) |
| **Whereby** | Videollamadas embedidas |
| **PostHog** | Analytics de producto |
| **Sentry** | Error tracking |
| **Docker** | Contenedores de desarrollo y producción |

---

## 🏗️ Arquitectura

### Diagrama de Arquitectura

```mermaid
graph TB
    subgraph "🌐 Client Layer"
        L[Landing Page]
        D[Dashboard SPA]
        W[Widget Embed]
    end

    subgraph "🚀 Next.js 16 (Frontend)"
        N[App Router]
        A[API Routes]
        M[Middleware Proxy]
        I[i18n Routing]
    end

    subgraph "🐍 Flask 3 (Backend)"
        F[Flask App]
        C[Console Blueprint]
        P[Public Blueprint]
        RAG[Core RAG Pipeline]
        E[Email Processor]
    end

    subgraph "🗄️ Data Layer"
        PG[PostgreSQL 15 + pgvector]
        RE[Redis 7]
        SS[Supabase Storage]
    end

    subgraph "🤖 AI Services"
        AN[Anthropic Claude]
        OI[OpenAI]
    end

    subgraph "💳 External Services"
        ST[Stripe]
        RE2[Resend]
        SG[SendGrid]
        WH[Whereby]
        PH[PostHog]
    end

    L --> N
    D --> N
    W --> P
    N --> A
    N --> M
    M --> F
    A --> F
    P --> PG
    C --> F
    F --> PG
    F --> RE
    F --> RAG
    RAG --> AN
    RAG --> OI
    F --> E
    E --> SG
    E --> RE2
    F --> ST
    F --> WH
    N --> SS
    N --> PH
```

### Flujo de una Consulta al Clon

```mermaid
sequenceDiagram
    actor User as 👤 Usuario
    participant FE as Next.js Frontend
    participant MW as Middleware Proxy
    participant BE as Flask Backend
    participant RAG as RAG Pipeline
    participant LLM as Anthropic/OpenAI
    participant DB as PostgreSQL + pgvector

    User->>FE: Escribe pregunta
    FE->>MW: POST /api/clone/{slug}/chat
    MW->>BE: Proxy a Flask
    BE->>RAG: Iniciar pipeline
    RAG->>DB: 1. Buscar fuentes del clon
    RAG->>DB: 2. Buscar memorias
    RAG->>LLM: 3. Generar embedding
    RAG->>DB: 4. Búsqueda semántica (pgvector)
    RAG->>LLM: 5. Generar respuesta con contexto
    LLM-->>RAG: Respuesta + confidence score
    RAG->>DB: 6. Guardar conversación
    RAG->>DB: 7. Detectar gaps (confidence < 0.7)
    RAG-->>BE: PipelineResult
    BE-->>MW: JSON Response
    MW-->>FE: Forward response
    FE-->>User: Render streaming response
```

### Multi-tenancy

El sistema utiliza **subdominios para identificación de tenants**:

```
tenant1.replica.tudominio.com → Tenant A
tenant2.replica.tudominio.com → Tenant B
```

El middleware detecta el tenant desde el hostname, lo inyecta en `x-tenant-slug` header, y cada tenant tiene datos aislados por `tenant_id` en todas las tablas.

---

## 🗄️ Modelo de Datos

### Esquema relacional (Drizzle ORM — 10 tablas principales)

```mermaid
erDiagram
    TENANTS ||--o{ USERS : has
    TENANTS ||--o{ CLONE_CONFIGS : has
    CLONE_CONFIGS ||--o{ CLONE_MODE_PROMPTS : configures
    CLONE_CONFIGS ||--o{ SOURCES : ingests
    SOURCES ||--o{ CHUNKS : chunked
    CHUNKS ||--o{ VECTOR : embeds
    CLONE_CONFIGS ||--o{ CONVERSATIONS : contains
    CONVERSATIONS ||--o{ MESSAGES : contains
    CLONE_CONFIGS ||--o{ MEMORIES : remembers
    CLONE_CONFIGS ||--o{ PRODUCTS : sells
    USERS ||--o{ ACCOUNTS : auth
    USERS ||--o{ SESSIONS : active

    TENANTS {
        text id PK
        text slug UK "unique"
        text name
        enum plan "trial|basic|pro|scale|enterprise"
        enum status "active|suspended|cancelled|trial"
        timestamp trial_ends_at
        text stripe_customer_id
        text stripe_subscription_id
    }

    USERS {
        text id PK
        text tenant_id FK
        text name
        text email UK
        text password_hash
        enum role "owner|admin|member|platform_admin"
        timestamp email_verified
    }

    CLONE_CONFIGS {
        text id PK
        text tenant_id FK
        text name
        text slug UK
        text description
        text avatar_url
        text personality
        text tone
        text language
        json active_modes
        boolean is_active
    }

    CONVERSATIONS {
        text id PK
        text clone_id FK
        text visitor_id
        enum mode "pedagogy|sales|support"
        timestamp created_at
    }

    SOURCES {
        text id PK
        text clone_id FK
        enum type "youtube|pdf|video|text|web|interview"
        text title
        text url
        enum status "uploading|processing|ready|error"
        json metadata
    }
```

**PostgreSQL Extensions:** `pgvector` para embeddings (`vector` cosine distance).

**Nota:** El backend Flask usa SQLAlchemy sobre las mismas tablas (schema compartido), con Alembic para migraciones. Hay tablas gestionadas exclusivamente por el backend (`email_inbound`, `meeting_types`, `impersonation_tokens`, `admin_audit_log`).

---

## 🗺️ Roadmap Técnico

### ✅ Completado (MVP)

- [x] Autenticación NextAuth v5 (credentials + Google + magic link)
- [x] Dashboard con sidebar responsivo y tema oscuro/claro
- [x] Pipeline RAG: ingest → chunk → embedding → pgvector → retrieval → generación
- [x] Chat en tiempo real con streaming SSE
- [x] CRUD de fuentes de conocimiento (PDF, YouTube, web, texto)
- [x] Widget embedible para sitios externos
- [x] Panel de administración multi-tenant
- [x] Sistema de planes y facturación Stripe
- [x] Procesamiento de email inbound con SendGrid
- [x] Booking de reuniones con Whereby
- [x] Detección de gaps de conocimiento
- [x] Internacionalización (ES/EN)

### 🚧 En Progreso

- [ ] Integración con Slack/Messenger para el clon
- [ ] Marketplace de prompts y templates
- [ ] Análisis de sentimiento en conversaciones
- [ ] Webhook API para integraciones externas

### 🔮 Futuro

- [ ] Fine-tuning de modelos con datos del creador
- [ ] Voice agent (inbound/outbound calls)
- [ ] Versión mobile nativa (React Native)
- [ ] AI video avatar synthesis

---

## 📋 Requisitos del Sistema

- **Node.js** 18+ (recomendado 20 LTS)
- **Python** 3.11+
- **Docker** + Docker Compose
- **PostgreSQL** 15+ con extensión pgvector
- **Redis** 7+
- **Git**

---

## 🚀 Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Teokoaaly/MyOwnClone
cd MyOwnClone
```

### 2. Levantar servicios de infraestructura

```bash
cd api
cp .env.example .env
# EDITAR .env: DB_PASSWORD, REDIS_PASSWORD, JWT_SECRET_KEY

docker-compose up -d db_postgres redis
# Verificar estado
docker-compose ps
```

> ⚠️ **Importante:** `DB_PASSWORD` y `REDIS_PASSWORD` son obligatorios y deben ser contraseñas fuertes (mín. 16 caracteres).

### 3. Configurar backend Python

```bash
cd api
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### 4. Instalar pgvector

```bash
docker exec -it myownclone_postgres psql -U postgres -d myownclone \
    -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### 5. Migraciones del backend

```bash
cd api
flask --app app_factory db upgrade

# Verificar tablas
docker exec -it myownclone_postgres psql -U postgres -d myownclone -c "\dt"
```

### 6. Configurar frontend Next.js

```bash
cd MyOwnClone
cp .env.example .env.local
# EDITAR .env.local con tus claves

npm ci
```

### 7. Migraciones Drizzle

```bash
cd MyOwnClone
npm run db:generate
npm run db:push
```

### 8. Arrancar en desarrollo

**Backend** (terminal 1):
```bash
cd api
flask --app app_factory run --host=0.0.0.0 --port=5001
```

**Frontend** (terminal 2):
```bash
cd MyOwnClone
npm run dev
```

Abrir `http://localhost:3000`.

---

## 🔐 Variables de Entorno

### Frontend (`MyOwnClone/.env.local`)

| Variable | Descripción | Obligatoria |
|---|---|---|
| `DATABASE_URL` | URL de PostgreSQL (`postgresql://user:pass@host:5432/db`) | ✅ |
| `NEXTAUTH_URL` | URL base del frontend (`http://localhost:3000`) | ✅ |
| `NEXTAUTH_SECRET` | Secreto para JWT (generar: `openssl rand -base64 32`) | ✅ |
| `AUTH_SECRET` | Mismo valor que NEXTAUTH_SECRET (alias NextAuth v5) | ✅ |
| `ANTHROPIC_API_KEY` | API key de Anthropic (chat principal) | Para LLM |
| `OPENAI_API_KEY` | API key de OpenAI (embeddings + Whisper STT) | Para RAG |
| `MYOWNCLONE_API_URL` | URL del backend Flask (`http://localhost:5001`) | ✅ |
| `DEFAULT_CLONE_ID` | UUID del clon por defecto | ✅ |
| `PLATFORM_ADMIN_EMAIL` | Email del admin global | Para admin |
| `PLATFORM_ADMIN_PASSWORD_HASH` | Hash bcrypt de la contraseña admin | Para admin |
| `AUTH_GOOGLE_ID` | Google OAuth Client ID | Para Google login |
| `AUTH_GOOGLE_SECRET` | Google OAuth Client Secret | Para Google login |
| `STRIPE_SECRET_KEY` | Stripe Secret Key (sk_live_ o sk_test_) | Para billing |
| `STRIPE_WEBHOOK_SECRET` | Stripe Webhook secret | Para billing |
| `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` | Stripe Publishable Key | Para billing |
| `STRIPE_BASIC_PRICE_ID` / `_PRO_` / `_SCALE_` | Price IDs de Stripe | Para billing |
| `RESEND_API_KEY` | API key de Resend | Para emails |
| `RESEND_FROM_EMAIL` | Remitente de emails | Para emails |
| `SENDGRID_INBOUND_WEBHOOK_SECRET` | Secreto webhook SendGrid | Para email inbound |
| `WHEREBY_API_KEY` | API key de Whereby | Para meetings |
| `UPSTASH_REDIS_REST_URL` | URL Upstash Redis | Para rate limiting |
| `UPSTASH_REDIS_REST_TOKEN` | Token Upstash Redis | Para rate limiting |
| `SUPABASE_URL` | URL de Supabase | Para storage |
| `SUPABASE_SERVICE_ROLE_KEY` | Service Role Key de Supabase | Para storage |
| `NEXT_PUBLIC_SENTRY_DSN` | DSN de Sentry | Error tracking |
| `NEXT_PUBLIC_POSTHOG_KEY` / `_HOST` | PostHog credentials | Analytics |

### Backend (`api/.env`)

| Variable | Descripción | Obligatoria |
|---|---|---|
| `DB_PASSWORD` | Contraseña PostgreSQL | ✅ |
| `REDIS_PASSWORD` | Contraseña Redis | ✅ |
| `JWT_SECRET_KEY` | Secreto JWT (≥ 64 chars) | ✅ (producción) |
| `IMPERSONATION_TOKEN_PEPPER` | Pepper para hash de tokens | ✅ (producción) |
| `OPENAI_API_KEY` | API key de OpenAI | Para LLM |
| `ANTHROPIC_API_KEY` | API key de Anthropic | Fallback LLM |
| `STRIPE_SECRET_KEY` | API key Stripe | Para billing |
| `ALLOWED_ORIGINS` | Orígenes CORS (separados por coma) | ✅ (producción) |

Generar claves seguras:
```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

---

## 🧪 Comandos de Desarrollo

### Frontend

```bash
npm run dev          # Servidor de desarrollo (puerto 3000)
npm run build        # Build de producción
npm run start        # Servidor de producción
npm run lint         # ESLint
npm run typecheck    # TypeScript check

# Base de datos
npm run db:generate  # Generar migraciones Drizzle
npm run db:migrate   # Aplicar migraciones (producción)
npm run db:push      # Push directo del schema (desarrollo)
npm run db:studio    # Drizzle Studio UI
```

### Backend

```bash
flask --app app_factory run --host=0.0.0.0 --port=5001
flask --app app_factory db upgrade
flask --app app_factory db downgrade
flask --app app_factory db current
flask --app app_factory seed-demo-data
```

---

## 🧪 Testing

```bash
# Frontend (Vitest)
cd MyOwnClone
npm test              # Todos los tests
npm run test:watch    # Modo watch

# Backend (pytest)
cd api  # O desde la raíz
pytest -v
pytest --tb=short     # Traceback corto
pytest tests/ -v      # Tests específicos
```

---

## 🌐 Despliegue en Producción

Ver scripts en `ops/` y documentación detallada en `.docs_md/`:

```bash
# Backend
bash ops/deploy-backend.sh

# Frontend
bash ops/deploy-frontend.sh
```

### VPS Deployment

El proyecto incluye Dockerfile para el backend (puerto 5001) y scripts de deploy para VPS. Las variables de entorno de producción deben configurarse en el servidor.

**Requisitos de producción:**
- PostgreSQL 15+ con pgvector
- Redis 7+
- Nginx como reverse proxy
- Certificados SSL (Let's Encrypt)
- Monitoreo con Sentry + PostHog

---

## 📁 Estructura del Proyecto

```
MyOwnClone/
├── api/                                 # Backend Flask
│   ├── app_factory.py                  # Application factory
│   ├── commands/
│   │   └── seed.py                     # CLI seed demo data
│   ├── configs/                        # Flask config classes
│   ├── controllers/
│   │   ├── console/                    # API autenticada
│   │   │   ├── auth.py                 # Login API
│   │   │   ├── wraps.py               # Decoradores auth
│   │   │   └── myownclone/            # Módulos de negocio
│   │   │       ├── admin_platform.py  # Admin multi-tenant
│   │   │       ├── analytics.py        # Analíticas
│   │   │       ├── booking.py         # Reservas
│   │   │       ├── clone.py           # CRUD clones
│   │   │       ├── creator_memory.py  # Memorias
│   │   │       ├── feedback.py        # Feedback
│   │   │       ├── inbox.py           # Email inbox
│   │   │       └── stripe_ctrl.py     # Facturación
│   │   └── myownclone_public.py       # API pública (chat, bookings)
│   ├── core/
│   │   ├── ingestion.py               # Procesamiento de fuentes
│   │   ├── model_manager.py           # Façade LLM
│   │   ├── retrieval.py               # Pipeline RAG central
│   │   └── myownclone/
│   │       ├── silos.py               # Silos de conocimiento
│   │       └── email_*.py             # Procesamiento de email
│   ├── extensions/                    # Flask extensions (db, redis)
│   ├── fields/                        # Campos personalizados SQLAlchemy
│   ├── libs/                          # JWT, login, utils
│   ├── migrations/versions/           # Alembic migrations
│   ├── models/                        # SQLAlchemy models
│   ├── docker-compose.yml             # Dev infra (PG + Redis)
│   ├── Dockerfile                     # Production image
│   ├── requirements.txt               # Producción
│   └── requirements-dev.txt           # Desarrollo
│
├── MyOwnClone/                        # Frontend Next.js 16
│   ├── src/
│   │   ├── app/
│   │   │   ├── (dashboard)/           # Dashboard autenticado
│   │   │   │   ├── resumen/           # Overview / Command Center
│   │   │   │   ├── biblioteca/        # Library / Sources
│   │   │   │   ├── cerebro/           # Memory crawl
│   │   │   │   ├── inbox/             # Email inbox
│   │   │   │   ├── productos/         # Product catalog
│   │   │   │   ├── analiticas/        # Usage analytics
│   │   │   │   ├── facturacion/       # Billing
│   │   │   │   ├── configuracion/     # Settings / API Keys
│   │   │   │   ├── reuniones/         # Meetings
│   │   │   │   └── registro/          # Registration
│   │   │   ├── (public)/              # Páginas públicas
│   │   │   │   └── [slug]/            # Clone public chat
│   │   │   ├── admin/                 # Platform admin panel
│   │   │   │   ├── resumen/           # Admin overview
│   │   │   │   ├── tenants/           # Tenant management
│   │   │   │   ├── audit/             # Audit log
│   │   │   │   ├── impersonation/     # User impersonation
│   │   │   │   ├── courtesy/          # Courtesy credits
│   │   │   │   └── feedback/          # User feedback
│   │   │   ├── api/                   # API Routes
│   │   │   │   ├── auth/[...nextauth] # NextAuth endpoint
│   │   │   │   ├── clone/sources/     # Sources CRUD
│   │   │   │   ├── bookings/          # Booking API
│   │   │   │   ├── stt/               # Speech-to-text
│   │   │   │   └── csrf/              # CSRF token
│   │   │   ├── providers.tsx          # Providers (Session, Theme)
│   │   │   ├── layout.tsx             # Root layout
│   │   │   └── page.tsx               # Landing page
│   │   ├── components/
│   │   │   ├── admin/                 # Admin components
│   │   │   │   ├── AdminShell.tsx
│   │   │   │   ├── AdminTopbar.tsx
│   │   │   │   ├── FilterBar.tsx
│   │   │   │   ├── Pagination.tsx
│   │   │   │   ├── Field.tsx
│   │   │   │   └── (buttons)
│   │   │   ├── chat/                  # Chat components
│   │   │   │   ├── ChatPanel.tsx
│   │   │   │   ├── MessageBubble.tsx
│   │   │   │   └── SiloToggle.tsx
│   │   │   ├── dashboard/             # Dashboard components
│   │   │   │   ├── Sidebar.tsx
│   │   │   │   ├── ChatOrb.tsx
│   │   │   │   ├── StatsCard.tsx
│   │   │   │   ├── QuickActionCard.tsx
│   │   │   │   ├── EndpointCard.tsx
│   │   │   │   └── ...
│   │   │   └── ui/                    # Generic UI components
│   │   │       ├── Modal.tsx
│   │   │       ├── Sheet.tsx
│   │   │       ├── ThemeToggle.tsx
│   │   │       ├── SearchCommandBar.tsx
│   │   │       ├── BarChart.tsx
│   │   │       ├── EmptyState.tsx
│   │   │       ├── ErrorState.tsx
│   │   │       ├── LoadingState.tsx
│   │   │       └── MobileNav.tsx
│   │   ├── lib/
│   │   │   ├── auth.ts               # NextAuth configuration
│   │   │   ├── db/
│   │   │   │   ├── index.ts          # Drizzle client & schema export
│   │   │   │   └── schema/           # 9 table modules
│   │   │   ├── rag/                  # RAG pipeline (deprecated)
│   │   │   ├── stripe.ts             # Stripe client
│   │   │   ├── storage.ts            # Supabase storage
│   │   │   ├── email.ts              # Resend emails
│   │   │   ├── video.ts              # Whereby meetings
│   │   │   ├── quotas.ts             # Plan limits
│   │   │   ├── platform-admin.ts     # Admin auth helpers
│   │   │   └── utils.ts              # Utilities
│   │   ├── middleware.ts             # Proxy + tenant detection
│   │   └── i18n/                     # Internationalization
│   ├── drizzle/                      # Drizzle migration files
│   ├── drizzle.config.ts
│   ├── next.config.ts
│   ├── vitest.config.ts
│   └── package.json
│
├── ops/                              # Deployment scripts
├── .docs_md/                         # Documentación técnica
├── conftest.py                       # Pytest config
├── pytest.ini                        # Pytest settings
├── requirements.txt                  # Root requirements
├── Dockerfile                        # Backend Dockerfile
└── README.md                         # ← Este archivo
```

---

## 🔌 API Reference

### Frontend API Routes

| Endpoint | Método | Descripción |
|---|---|---|
| `/api/auth/[...nextauth]` | `*` | NextAuth handlers |
| `/api/clone/sources` | `GET` | Listar fuentes del clon |
| `/api/clone/sources` | `POST` | Crear nueva fuente |
| `/api/clone/analytics/overview` | `GET` | Resumen de analíticas |
| `/api/clone/inbox/list` | `GET` | Listar emails |
| `/api/clone/inbox/{id}/generate-draft` | `POST` | Generar borrador IA |
| `/api/bookings` | `*` | CRUD de reservas |
| `/api/stt` | `POST` | Speech-to-text (Whisper) |
| `/api/csrf` | `GET` | CSRF token |
| `/api/deploy` | `POST` | Trigger deploy frontend |
| `/widget.js` | `GET` | Script widget embedible |

### Backend Console API (proxy via middleware)

| Endpoint Frontend | Backend Mapping |
|---|---|
| `/api/clone/clones` | `/console/api/myownclone/clones` |
| `/api/clone/analytics/*` | `/console/api/myownclone/clones/{id}/analytics/*` |
| `/api/clone/memories` | `/console/api/myownclone/clones/{id}/memories` |
| `/api/clone/plans` | `/console/api/myownclone/plans` |
| `/api/clone/billing` | `/console/api/myownclone/stripe/billing` |
| `/api/admin/*` | `/console/api/myownclone/admin/*` |
| `/api/auth/login` | `/console/api/auth/login` |

### Public API (no auth)

| Endpoint | Método | Descripción |
|---|---|---|
| `/api/public/{slug}/chat` | `POST` | Chat público del clon |

---

## 🤝 Contribuir

1. **Fork** del repositorio
2. Crear rama: `git checkout -b feature/mi-feature`
3. Commit con formato convencional:
   ```bash
   git commit -m "feat(scope): descripción clara del cambio"
   ```
   Tipos: `feat`, `fix`, `chore`, `docs`, `refactor`, `test`, `style`
4. Push: `git push origin feature/mi-feature`
5. Abrir **Pull Request** con descripción clara

### Convenciones de Código

- TypeScript strict mode
- ESLint + Prettier
- Componentes React Server Components por defecto, `"use client"` solo cuando sea necesario
- Nombres de archivos en kebab-case para rutas, PascalCase para componentes
- CSS con Tailwind utility classes + variables CSS para el design system

---

## 📄 Licencia

**Propietaria** — Todos los derechos reservados.

MyOwnClone es un producto comercial. Este repositorio se proporciona para fines de desarrollo y despliegue del equipo autorizado. No está permitido su uso, reproducción o distribución sin autorización expresa.

---

<p align="center">
  <a href="https://myownclone.com">myownclone.com</a> ·
  <a href="mailto:hello@myownclone.com">Contacto</a> ·
  <a href="/.docs_md/DIAGNOSTICO_TECNICO.md">Diagnóstico Técnico</a> ·
  <a href="/.docs_md/IMPLEMENTATION_LOG.md">Changelog</a>
  <br />
  <sub>Built with ❤️ by the MyOwnClone Team</sub>
</p>
