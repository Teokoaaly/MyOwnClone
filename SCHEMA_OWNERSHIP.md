# SCHEMA_OWNERSHIP.md — Regla de oro del esquema de base de datos

> Estado: **vigente desde 2026-06-21**.
> Problema que resuelve: el proyecto tiene DOS herramientas de migración
> (Alembic en `api/migrations` para Flask/SQLAlchemy, y Drizzle en
> `MyOwnClone/drizzle` para Next.js) que históricamente han modificado las
> mismas tablas, generando *drift* (enum con nombres distintos, índices en
> un lado y no en el otro, columnas renombradas a medias).

## Regla de oro

**Alembic es la única fuente de verdad del esquema en producción.**

- Toda creación/modificación/borrado de tablas, columnas, índices, enums y
  constraints se hace mediante una migración Alembic nueva en
  `api/migrations/versions/`.
- Drizzle se usa **solo como cliente tipado de lectura/escritura** desde
  Next.js. NO genera migraciones aplicables a producción.

## Qué se permite con cada herramienta

| Acción | Alembic | Drizzle Kit |
|---|---|---|
| Crear tabla/columna/índice/enum en prod | ✅ Sí, migración nueva | ❌ Nunca |
| Aplicar migraciones en prod | ✅ `flask db upgrade` | ❌ `db:push` prohibido |
| Aplicar migraciones en dev local | ✅ | ⚠️ Solo `db:migrate` con archivos SQL revisados |
| Regenerar tipos/schema.ts tras cambio Alembic | N/A | ✅ `db:generate` para sincronizar el snapshot |
| Inspeccionar datos | ✅ vía SQLAlchemy | ✅ vía Drizzle ORM |

## Por qué `db:push` es peligroso en producción

`drizzle-kit push` compara el schema declarado con la DB y aplica ALTER/CREATE
**automáticamente sin generar archivo SQL revisable**. En producción esto puede:

- Recrear una tabla si detecta diferencias de tipo → **pérdida de datos**.
- Crear índices con `CONCURRENTLY` incorrecto → bloqueos largos.
- Dejar la DB en estado intermedio si falla a mitad.

**Comando seguro en prod**: siempre `flask --app app_factory db upgrade`.

## Workflow para añadir una columna (ejemplo)

1. Escribir migración Alembic nueva en `api/migrations/versions/` con
   `upgrade()` y `downgrade()` explícitos.
2. Probar en DB staging vacía: `flask --app app_factory db upgrade`.
3. Actualizar el modelo SQLAlchemy en `api/models/`.
4. Actualizar el schema Drizzle en `MyOwnClone/src/lib/db/schema/`.
5. Regenerar snapshot Drizzle: `cd MyOwnClone && npm run db:generate`.
6. Tests: `pytest -q` (backend) y `npm run test` (frontend).
7. Deploy: migración Alembic primero, luego código.

## Estado de alineación (post-migración 2026-06-21)

La migración `2026_06_21_align_with_drizzle` (Alembic) corrige:

- Crea el enum PG `clone_feedback_rating` (Drizzle lo declaraba, Alembic usaba `String(20)`).
- Crea el enum PG `cost_category`, `inbound_email_status` (Drizzle los declaraba).
- Añade índices `cost_tracking_tenant_category_ts_idx` y `email_inbound_clone_status_idx`.
- Añade `clone_mode_prompts.temperature` (FASE 3 — parámetros de IA por modo).

## Checks de CI recomendados (siguiente ciclo)

- Comparar `information_schema` de la DB vs metadata SQLAlchemy tras `db upgrade`
  en una DB ephemeral.
- Comparar `drizzle/meta/*.snapshot.json` vs schema real y fallar si hay drift.
- Test negativo: intentar `db:push` en CI debe fallar o advertir.
