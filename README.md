# MyOwnClone

**Plataforma SaaS multi-tenant para desplegar clones de IA personalizados.**

Permite a creadores de contenido lanzar su propio asistente de IA (chatbot RAG) con:
- 📚 **Enseñanza** — responde preguntas basándose en tu contenido
- 🛠️ **Soporte** — atiende clientes 24/7
- 💼 **Ventas** — asesora sobre productos y servicios
- 📧 **Email triage** — clasifica y redacta borradores automáticamente
- 📅 **Reuniones** — gestión de disponibilidad y bookings
- 📊 **Analíticas** — preguntas frecuentes, gaps de conocimiento, costes
- 💳 **Facturación** — planes Stripe integrados

---

## Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 16 (App Router) + React 19 + TypeScript |
| Estilos | Tailwind CSS v4 |
| Auth | NextAuth v5 (JWT) |
| ORM Frontend | Drizzle ORM |
| Backend | Flask 3 + SQLAlchemy 2 |
| ORM Backend | Flask-Migrate (Alembic) |
| Base de datos | PostgreSQL 15 + pgvector |
| Cache | Redis 7 |
| Vector DB | Weaviate 1.24 |
| LLM | OpenAI (GPT-4o-mini) / Anthropic (Claude) |
| Pagos | Stripe |
| Email outbound | Resend |
| Email inbound | SendGrid Inbound Parse |
| Tests Frontend | Vitest + Testing Library |
| Tests Backend | pytest |

---

## Requisitos del Sistema

- **Node.js** 18+
- **Python** 3.11+
- **Docker** + Docker Compose
- **Git**

---

## Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Teokoaaly/MyOwnClone
cd MyOwnClone
```

### 2. Levantar servicios de infraestructura

```bash
cd api
# Copiar y configurar variables de entorno del backend
cp .env.example .env
# EDITAR api/.env: rellenar DB_PASSWORD, REDIS_PASSWORD, JWT_SECRET_KEY, etc.

# Levantar PostgreSQL + Redis (Weaviate es opcional para MVP)
docker-compose up -d db_postgres redis

# Verificar que están sanos
docker-compose ps
```

> ⚠️ **IMPORTANTE:** `DB_PASSWORD` y `REDIS_PASSWORD` son OBLIGATORIOS y deben ser contraseñas fuertes (mín. 16 caracteres). La aplicación no arrancará sin ellas.

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

### 4. Instalar extensión pgvector

```bash
# Necesaria para embeddings RAG
docker exec -it myownclone_postgres psql -U postgres -d myownclone \
    -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### 5. Ejecutar migraciones del backend

```bash
cd api
flask --app app_factory db upgrade

# Verificar tablas creadas
docker exec -it myownclone_postgres psql -U postgres -d myownclone -c "\dt"
```

### 6. Configurar frontend Next.js

```bash
cd MyOwnClone
cp .env.example .env.local
# EDITAR .env.local: DATABASE_URL, NEXTAUTH_SECRET, AUTH_SECRET, claves LLM, etc.

npm ci
```

### 7. Ejecutar migraciones del frontend (Drizzle)

```bash
cd MyOwnClone
npm run db:generate  # Genera archivos de migración SQL
npm run db:push      # Aplica cambios a la DB
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

Abrir `http://localhost:3000` en el navegador.

---

## Variables de Entorno

### Backend (`api/.env`)

| Variable | Descripción | Obligatoria |
|----------|-------------|-------------|
| `DB_PASSWORD` | Contraseña PostgreSQL | ✅ Sí |
| `REDIS_PASSWORD` | Contraseña Redis | ✅ Sí |
| `JWT_SECRET_KEY` | Secreto JWT (≥64 chars) | ✅ Sí (prod) |
| `IMPERSONATION_TOKEN_PEPPER` | Pepper para hash de tokens | ✅ Sí (prod) |
| `OPENAI_API_KEY` | API key de OpenAI | Para LLM |
| `ANTHROPIC_API_KEY` | API key de Anthropic | Fallback LLM |
| `STRIPE_SECRET_KEY` | API key Stripe | Para billing |
| `ALLOWED_ORIGINS` | Orígenes CORS (comma-separated) | ✅ En prod |

Generar claves seguras:
```bash
python -c "import secrets; print(secrets.token_urlsafe(64))"
```

### Frontend (`MyOwnClone/.env.local`)

| Variable | Descripción | Obligatoria |
|----------|-------------|-------------|
| `DATABASE_URL` | URL de PostgreSQL | ✅ Sí |
| `NEXTAUTH_SECRET` / `AUTH_SECRET` | Secreto NextAuth | ✅ Sí |
| `MYOWNCLONE_API_URL` | URL del backend Flask | ✅ Sí |
| `OPENAI_API_KEY` | Para embeddings | Para RAG |
| `ANTHROPIC_API_KEY` | Para generación LLM | Para chat |
| `DEFAULT_CLONE_ID` | UUID del clone por defecto | Sí |
| `PLATFORM_ADMIN_EMAIL` | Email del admin global | Para admin |
| `PLATFORM_ADMIN_PASSWORD_HASH` | Hash bcrypt de la contraseña admin | Para admin |

---

## Comandos de Desarrollo

### Backend
```bash
# Arrancar servidor desarrollo
flask --app app_factory run --host=0.0.0.0 --port=5001

# Migraciones
flask --app app_factory db upgrade      # Aplicar migraciones pendientes
flask --app app_factory db downgrade    # Revertir última migración
flask --app app_factory db current      # Ver migración actual
flask --app app_factory db history      # Ver historial

# Datos de prueba
flask --app app_factory seed-demo-data
```

### Frontend
```bash
npm run dev          # Servidor de desarrollo
npm run build        # Build de producción
npm run start        # Servidor de producción (requiere build previo)
npm run lint         # ESLint
npm run typecheck    # TypeScript sin compilar

# Base de datos
npm run db:generate  # Generar archivos de migración Drizzle
npm run db:migrate   # Aplicar migraciones (producción controlada)
npm run db:push      # Push directo del schema (desarrollo)
npm run db:studio    # Abrir Drizzle Studio (UI para explorar la DB)
```

---

## Comandos de Tests

### Frontend
```bash
cd MyOwnClone
npm test              # Ejecutar todos los tests (Vitest)
npm run test:watch    # Modo watch
```

### Backend
```bash
cd api  # O desde la raíz con pytest.ini
pytest api/tests/ -v
pytest tests/ -v
pytest --tb=short     # Traceback corto
```

---

## Estructura del Proyecto

```
MyOwnClone/
├── api/                        # Backend Flask
│   ├── app_factory.py          # Factory principal Flask
│   ├── commands/               # CLI commands (seed-demo-data)
│   ├── configs/                # Configuración de la app
│   ├── controllers/
│   │   ├── console/            # API autenticada (dashboard)
│   │   │   └── myownclone/     # Módulos de la app
│   │   └── myownclone_public.py # API pública (chat, bookings)
│   ├── core/
│   │   ├── model_manager.py    # Façade LLM (OpenAI/Anthropic)
│   │   └── myownclone/         # Lógica de email IA, RAG
│   ├── extensions/             # Flask extensions (db, redis)
│   ├── libs/                   # JWT, login, UUID utils
│   ├── migrations/
│   │   └── versions/           # Archivos Alembic
│   ├── models/                 # Modelos SQLAlchemy
│   ├── services/               # Capa de servicios
│   ├── tests/                  # Tests pytest
│   ├── docker-compose.yml      # Docker dev (PG + Redis + Weaviate)
│   ├── Dockerfile              # Imagen del backend
│   ├── requirements.txt        # Dependencias producción
│   └── requirements-dev.txt    # Dependencias desarrollo
│
├── MyOwnClone/                 # Frontend Next.js
│   ├── src/
│   │   ├── app/                # Next.js App Router
│   │   │   ├── (dashboard)/    # Rutas autenticadas del dashboard
│   │   │   ├── (public)/       # Páginas públicas (chat del clone)
│   │   │   ├── admin/          # Panel de administración
│   │   │   └── api/            # API Routes (proxies al backend)
│   │   ├── components/         # Componentes React
│   │   │   ├── admin/          # Componentes del admin
│   │   │   ├── chat/           # Componentes del chat
│   │   │   ├── dashboard/      # Componentes del dashboard
│   │   │   └── ui/             # Componentes UI genéricos
│   │   ├── lib/
│   │   │   ├── auth.ts         # Configuración NextAuth
│   │   │   ├── db/             # Schema y cliente Drizzle
│   │   │   └── rag/            # Pipeline de RAG (ingest + retrieve)
│   │   └── __tests__/          # Tests Vitest
│   ├── .env.example            # Template de variables de entorno
│   ├── drizzle.config.ts       # Configuración Drizzle ORM
│   ├── next.config.ts          # Configuración Next.js
│   └── package.json
│
├── ops/                        # Scripts de despliegue VPS
│   ├── deploy-backend.sh
│   ├── deploy-frontend.sh
│   └── docker-compose.backend.prod.yml
│
├── MASTER_PLAN.md              # Plan maestro de implementación
├── Task.md                     # Checklist de tareas
└── DIAGNOSTICO_TECNICO.md     # Diagnóstico técnico completo
```

---

## Arquitectura de Base de Datos

El proyecto usa **dos sistemas ORM paralelos sobre la misma instancia PostgreSQL**:

| Sistema | Framework | Gestiona |
|---------|-----------|---------|
| **Drizzle** (frontend) | Next.js/TypeScript | users, tenants, clone_configs, sources, chunks, conversations, messages, emails, bookings, memories, analytics |
| **Alembic** (backend) | Flask/Python | clone_configs, email_inbound, meeting_types, bookings, cost_tracking, admin_audit_log, impersonation_tokens |

> ⚠️ Hay tablas compartidas (`clone_configs`, `bookings`, etc.) con esquemas ligeramente diferentes. Ver `DIAGNOSTICO_TECNICO.md` para el detalle completo.

---

## Despliegue en Producción

Ver los scripts en `ops/`:

```bash
# Backend
bash ops/deploy-backend.sh

# Frontend
bash ops/deploy-frontend.sh
```

Ver `ops/DEPLOY_VPS.md` para instrucciones detalladas.

---

## Contribuir

1. Fork del repositorio
2. Crear rama: `git checkout -b feature/mi-feature`
3. Commit: `git commit -m "feat: descripción clara del cambio"`
4. Push: `git push origin feature/mi-feature`
5. Pull Request con descripción clara

---

## Licencia

Propietaria — ver LICENSE para detalles.
