# ARCHITECTURE.md

## Vision general

MyOwnClone es una plataforma SaaS multi-tenant para crear clones digitales de IA. Combina frontend Next.js, backend Flask y una base PostgreSQL compartida con capacidades vectoriales.

## Componentes

### Frontend `MyOwnClone/`

- Next.js 16 App Router.
- React 19 y TypeScript.
- NextAuth/Auth.js para sesion.
- Drizzle para acceso tipado a DB en rutas Next/Auth.
- API routes para auth, Stripe webhook, STT, sources y bookings.
- Proxy en `src/proxy.ts` para enrutar `/api/*` al backend Flask.
- UI de dashboard, admin, landing, widget y paginas publicas de clon.

### Backend `api/`

- Flask application factory en `api/app_factory.py`.
- SQLAlchemy models y Alembic migrations.
- Blueprints:
  - Auth console.
  - Admin platform.
  - Clone CRUD.
  - Analytics.
  - Inbox.
  - Booking.
  - Stripe.
  - Public clone chat.
- Core RAG y email AI en `api/core/`.

### Datos

- PostgreSQL como base principal.
- pgvector para busqueda semantica.
- Redis para rate limiting/cache/sesion operativa.
- Weaviate aparece en compose y requirements, pero debe confirmarse si sigue siendo componente activo o legado.
- Produccion usa `pgvector/pgvector:pg15`; Alembic habilita `CREATE EXTENSION IF NOT EXISTS vector`.

## Flujo de request autenticado

1. Usuario entra en dashboard Next.js.
2. NextAuth emite token/sesion.
3. `src/proxy.ts` valida ruta protegida.
4. Proxy agrega `X-API-Key` y headers de identidad.
5. Flask `login_required` valida JWT o service API key.
6. Controlador ejecuta logica de negocio con tenant/user context.
7. Respuesta vuelve al frontend.

## Flujo de chat publico

1. Visitante abre pagina publica o widget.
2. Frontend llama `/api/clone/{slug}/chat`.
3. Proxy enruta a endpoint publico Flask.
4. Backend aplica rate limit, resuelve clone y fuentes.
5. RAG recupera contexto, llama LLM y persiste conversacion.
6. Respuesta vuelve como JSON o SSE.

## Multi-tenancy

- El tenant puede detectarse por subdominio `tenant.replica.domain`.
- Los datos se aislan por `tenant_id` y `clone_id`.
- Riesgo clave: cada query admin/console debe validar tenant scoping. Debe existir test negativo por recurso sensible.

## Migraciones y schema ownership

Estado actual:

- Frontend usa Drizzle migrations en `MyOwnClone/drizzle`.
- Backend usa Alembic migrations en `api/migrations`.
- Ambos conocen tablas compartidas.

Riesgo:

- Drift si Drizzle y Alembic modifican la misma tabla sin regla clara.

Decision recomendada:

- Alembic como fuente de verdad para schema runtime compartido.
- Drizzle como cliente tipado y migraciones solo si se define ownership explicito.
- CI debe comparar schema o ejecutar migraciones desde DB vacia.

## Seguridad

Controles existentes:

- Secret checks en produccion.
- CORS configurable.
- `/healthz` para liveness y `/readyz` para DB/Redis readiness.
- Password hashing.
- Impersonation token hasheado con pepper.
- Stripe webhook separado en Next.js.
- Service-to-service key entre proxy y backend.

Pendiente:

- Threat model.
- CSP y security headers.
- Rate limiting Redis para rutas publicas.
- Tests de no aceptacion de dev key en prod.
- Auditoria de permisos por endpoint.

## Operacion

Pendiente para produccion:

- `healthz` y `readyz` base implementados.
- Logs estructurados.
- Metricas de latencia, errores e integraciones.
- Runbooks de rollback, migraciones y webhooks.
