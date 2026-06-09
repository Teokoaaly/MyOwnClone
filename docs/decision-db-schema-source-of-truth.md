# Decisión Arquitectónica: Fuente de Verdad del Esquema DB

> Fecha: 2026-06-09
> Estado: ✅ Decisión tomada — Alembic como fuente de verdad

---

## Problema

El proyecto tiene **dos sistemas de esquema** que apuntan a la misma base de datos:

| Sistema | Ubicación | Alcance |
|---------|-----------|---------|
| **Alembic** (Flask-Migrate) | `api/migrations/` | Backend SQLAlchemy ORM |
| **Drizzle** | `MyOwnClone/src/lib/db/schema/` | Frontend Next.js |

Ambos definen tablas que se superponen parcialmente (`tenants`, `clone_configs`, `clone_mode_prompts`, `bookings`, `analytics_*`, `email_inbound`, etc.) con diferencias de naming, tipos y defaults.

## Decisión

**Alembic es la fuente de verdad del esquema.**

- Las migraciones se definen y versionan en `api/migrations/` (Alembic)
- El backend (SQLAlchemy) es el propietario de la estructura de datos
- Drizzle en el frontend debe **reflejar** el esquema de Alembic, no definirlo
- Las tablas del frontend que ya existen en Alembic deben ser consumidas vía API del backend, no mediante Drizzle directo

## Discrepancias Detectadas

### `tenants`

| Columna | Drizzle | Alembic (Backend) | Resolución |
|---------|---------|-------------------|------------|
| `id` | `text` | `UUID` | Usar UUID |
| `plan` | enum: `basic/pro/scale/enterprise/trial` | `VARCHAR(50)`, default `'básico'` | Unificar a VARCHAR, backend decide |
| `status` | enum: `active/suspended/cancelled/trial` | `VARCHAR(50)`, default `'normal'` | Unificar a VARCHAR, backend decide |
| `trial_ends_at` | `timestamp` | `DateTime` nullable | Compatible |
| `stripe_customer_id` | `text` | `VARCHAR(255)` nullable | Compatible |
| `stripe_subscription_id` | `text` | `VARCHAR(255)` nullable | Compatible |
| `created_at` / `updated_at` | `timestamp defaultNow()` | `DateTime default now()` | Compatible |

### `clone_configs`

| Columna | Drizzle | Alembic (Backend) | Resolución |
|---------|---------|-------------------|------------|
| `id` | `text` | `VARCHAR(36)` / UUID | Usar VARCHAR(36) |
| `personality` / `tone` | Dos campos separados | Un campo `personality_tone` | Usar `personality_tone` (backend) |
| `active_modes` | `json` | `ARRAY(String)` | Compatible |
| `activeModes` vs `active_modes` | camelCase | snake_case | Drizzle usa snake en DB |

## Plan de Acción

### Inmediato (MVP)
1. No modificar el esquema actual — ambas fuentes coexisten temporalmente
2. Las tablas compartidas se gestionan desde Alembic
3. El frontend usa las APIs del backend para leer/escribir datos compartidos (no Drizzle directo)

### Corto plazo
1. Alinear Drizzle schema con las tablas reales de Alembic
2. Eliminar tablas Drizzle que duplican las de Alembic
3. Las únicas tablas Drizzle propias del frontend son las estrictamente locales (caché, estado)

### Medio plazo
1. Evaluar migrar Drizzle a solo cliente (tauri/SQLite local) si se necesita offline
2. O eliminar Drizzle por completo si todo el estado se gestiona via API REST

## Referencias

- [[bootstrap-local-completado]]
- DIAGNOSTICO_TECNICO.md
- MASTER_PLAN.md (TASK-023, TASK-024)
