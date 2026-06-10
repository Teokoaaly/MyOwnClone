# Auditoria — DB, Arquitectura y Multi-tenancy (TASK-360-01)

## Resumen
- **Estado:** Amarillo — Drizzle schema bien definido, pero dual ORM (Drizzle + Alembic) sobre mismas tablas sin sincronizacion clara
- **Riesgo principal:** Tablas compartidas entre Drizzle y SQLAlchemy pueden divergir; falta indice en `chunks.embedding` para produccion; algunas tablas SQLAlchemy no tienen equivalente Drizzle
- **Veredicto prod:** Funcional para MVP. Requiere decision sobre fuente de verdad unica antes de escalar

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| Drizzle schema (frontend) | ✅ | ~90% | 10 archivos en `src/lib/db/schema/` — 15 tablas con relaciones FK |
| SQLAlchemy models (backend) | ✅ | ~70% | `api/models/` — 8 archivos, incluye tablas que Drizzle no cubre |
| pgvector extension | ✅ | configurado | `schema/chunks.ts:5-9` customType vector(1536), indice IVFFlat |
| Migraciones Drizzle | ⚠️ | Parcial | `drizzle/` existe, pero `drizzle-kit push` interactivo bloquea CI |
| Migraciones Alembic | ⚠️ | Parcial | `api/migrations/` existe, sincronizacion con Drizzle no validada |
| Indices DB | ⚠️ | Parcial | Solo indice pgvector en chunks; faltan indices en tenant_id FK, email, slug |
| Multi-tenancy por tenant_id | ✅ | ~85% | Todas las tablas principales tienen `tenant_id` FK |
| Seed script | ✅ | Funcional | `src/lib/db/seed.ts` crea tenant, user, clone, mode prompts |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| D01-001 | P0 | Dual ORM sin fuente de verdad unica | `clone_configs`, `bookings` definidas en ambos ORMs con schemas que pueden divergir | `api/models/clone.py:21` (CloneConfig) vs `schema/clones.ts:17` (cloneConfigs) — mismas tablas, definiciones separadas | Elegir Drizzle como fuente de verdad (tiene tipado TS nativo) y hacer que modelos SQLAlchemy reflejen el schema Drizzle, o viceversa |
| D01-002 | P0 | Tablas SQLAlchemy sin migracion Drizzle | `email_inbound`, `impersonation_tokens`, `admin_audit_log`, `cost_tracking` existen solo en SQLAlchemy | `api/models/email.py:23` (EmailInbound), `api/models/account.py` (impersonation, audit) — no estan en `src/lib/db/schema/` | Crear schemas Drizzle para estas tablas o documentar que son de ownership exclusivo del backend |
| D01-003 | P1 | Indice IVFFlat en chunks sin parametros optimos | `lists=100` por defecto; para miles de chunks puede dar resultados imprecisos o lentos | `schema/chunks.ts:28-31` — `index("chunks_embedding_idx").using("ivfflat", ...)` sin configurar `lists` | Parametrizar `lists` basado en el tamano esperado de la tabla (regla: `lists = sqrt(rows)`) |
| D01-004 | P1 | Faltan indices en columnas de busqueda frecuente | Queries por email, slug y tenant_id hacen full scan | `schema/users.ts:24` email UNIQUE sin index explicito (UNIQUE crea index); `schema/tenants.ts:33` slug UNIQUE; pero `tenant_id` FK en users, clones, sources no tienen index | Añadir indices a todas las columnas `tenant_id` FK para evitar seq scans en joins multi-tenant |
| D01-005 | P1 | chat_orb, landing-brand-mark CSS muerto | Clases CSS de componentes antiguos que ya no se usan pero siguen en `globals.css` | `globals.css:176` `.chat-orb`, `globals.css:268-284` `.landing-brand-mark` — reemplazados por React components | Limpiar CSS muerto en Fase de cleanup |
| D01-006 | P2 | Drizzle push interactivo bloquea automatizacion | `drizzle-kit push` pregunta por tablas renombradas en cada ejecucion | Al ejecutar `drizzle-kit push` pregunta sobre `emails` vs tablas legacy de Alembic | Configurar `drizzle.config.ts` con `strict: true` o usar `drizzle-kit push --force` con snapshot |
| D01-007 | P2 | Sin migraciones versionadas en Drizzle | Solo se usa `push` (esquema directo); no hay migraciones SQL revisables | `package.json` — `db:push`, `db:generate` y `db:migrate` existen pero no se usan en CI | Usar `db:generate` + `db:migrate` en lugar de `db:push` para produccion |
| D01-008 | P2 | Tabla `users` usa TEXT para `role` en lugar del enum Drizzle | El enum `user_role` de Drizzle no se creo en la BD, workaround con SQL raw en auth | `auth.ts:60` usa `db.execute(sql\`...\`)` para evitar el enum faltante | Ejecutar `drizzle-kit push` o crear el enum manualmente para usar Drizzle ORM correctamente |
| D01-009 | P3 | Sin cascadas de borrado en SQLAlchemy para algunas tablas | Riesgo de integridad referencial si se elimina un tenant via backend | Verificar `ondelete="CASCADE"` en modelos SQLAlchemy vs Drizzle | Unificar politica de cascadas entre ambos ORMs |
| D01-010 | P3 | Seed script con IDs fijos | IDs hardcodeados pueden colisionar en entornos compartidos | `seed.ts:18-20` — DEMO_TENANT_ID, DEMO_USER_ID, DEMO_CLONE_ID fijos | Usar `crypto.randomUUID()` con validacion de existencia previa |

## Matriz de interconexion

### Tablas Drizzle (frontend) vs SQLAlchemy (backend)

| Tabla | Drizzle | SQLAlchemy | Dual? | tenant_id? | Gaps |
|---|---|---|---|---|---|
| tenants | ✅ `schema/tenants.ts` | ✅ `models/account.py:52` | ✅ SI | N/A (root) | Campos `stripe_customer_id`, `subscription_status` existen en ambos? Drizzle OK |
| users | ✅ `schema/users.ts` | ✅ `models/account.py:99` (Account) | ✅ SI | ✅ | Drizzle usa `users`, SQLAlchemy usa `accounts` — MISMO NOMBRE? No, SQLAlchemy es "accounts" (herencia) |
| clone_configs | ✅ `schema/clones.ts` | ✅ `models/clone.py:21` | ✅ SI | ✅ | Schemas similares pero no identicos |
| clone_mode_prompts | ✅ `schema/clones.ts` | ✅ `models/clone.py:36` | ✅ SI | via clone | Consistentes |
| sources | ✅ `schema/sources.ts` | ❌ Solo en Drizzle | ❌ | via clone | Backend usa API propia |
| chunks | ✅ `schema/chunks.ts` | ❌ Solo en Drizzle | ❌ | via source | Backend usa API propia |
| conversations | ✅ `schema/conversations.ts` | ❌ Solo en Drizzle | ❌ | via clone | Backend usa API propia |
| messages | ✅ `schema/conversations.ts` | ❌ Solo en Drizzle | ❌ | via conversation | Backend usa API propia |
| emails | ✅ `schema/emails.ts` | ❌ Solo en Drizzle | ❌ | via clone | — |
| meeting_types | ✅ `schema/bookings.ts` | ✅ `models/meeting.py:16` | ✅ SI | via clone | Consistentes |
| availability | ✅ `schema/bookings.ts` | ✅ `models/meeting.py:28` | ✅ SI | via clone | Consistentes |
| bookings | ✅ `schema/bookings.ts` | ✅ `models/meeting.py:44` | ✅ SI | via meeting_type | Consistentes |
| memories | ✅ `schema/analytics.ts` | ✅ `models/analytics.py` (CreatorMemory) | ⚠️ Parcial | ✅ | Drizzle usa `memories`, SQLAlchemy usa `creator_memory` — Nombres diferentes! |
| products | ✅ `schema/analytics.ts` | ✅ `models/meeting.py:60` | ✅ SI | via clone | Consistentes |
| impersonation_logs | ✅ `schema/analytics.ts` | ❌ Solo SQLAlchemy | ❌ | ✅ | Solo en backend |
| email_inbound | ❌ Solo SQLAlchemy | ✅ `models/email.py:23` | ❌ | via clone | Solo en backend |
| email_templates | ❌ Solo SQLAlchemy | ✅ `models/email.py:53` | ❌ | via clone | Solo en backend |
| admin_audit_log | ❌ Solo SQLAlchemy | ✅ (en account.py) | ❌ | N/A | Solo en backend |
| impersonation_tokens | ❌ Solo SQLAlchemy | ✅ (en account.py) | ❌ | N/A | Solo en backend |
| cost_tracking | ❌ Solo SQLAlchemy | ✅ (en account.py) | ❌ | ✅ | Solo en backend |

### Flujo: Multi-tenancy por tabla

| Tabla | tenant_id FK | Estrategia | Gap |
|---|---|---|---|
| users | FK → tenants.id | Directo | — |
| clone_configs | FK → tenants.id | Directo | — |
| sources | via clone_configs | 2 hops | Riesgo si clone se elimina |
| chunks | via sources | 3 hops | Riesgo si source se elimina |
| conversations | via clone_configs | 2 hops | — |
| messages | via conversations | 3 hops | — |
| emails | via clone_configs | 2 hops | — |
| memories | via clone_configs | 2 hops | — |
| products | via clone_configs | 2 hops | — |
| bookings | via meeting_types → clone_configs | 3 hops | — |

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| D01-A | P0 | Decidir y documentar fuente de verdad DB: Drizzle vs Alembic | Coordinador | 1d | — |
| D01-B | P0 | Crear schemas Drizzle para tablas backend exclusivas (email_inbound, impersonation, audit, cost_tracking) | Agent DB | 2d | D01-A |
| D01-C | P1 | Añadir indices a columnas `tenant_id` FK en todas las tablas | Agent DB | 0.5d | — |
| D01-D | P1 | Optimizar indice IVFFlat con `lists` parametrizado | Agent DB | 0.5d | — |
| D01-E | P1 | Limpiar CSS muerto (chat-orb, landing-brand-mark) | Agent Frontend | 0.3d | — |
| D01-F | P2 | Migrar de `drizzle-kit push` a `generate + migrate` en produccion | Agent DB | 0.5d | — |
| D01-G | P2 | Crear enum `user_role` en BD y eliminar workaround de SQL raw en auth.ts | Agent DB | 0.5d | D01-A |
| D01-H | P3 | Seed script con UUIDs aleatorios en lugar de fijos | Agent DB | 0.3d | — |

## Open Questions

1. **Dual ORM**: Se decide mantener ambos (Drizzle para frontend, Alembic para backend) o migrar todo a Drizzle? La respuesta condiciona todas las tareas P0.
2. **Tablas compartidas**: `clone_configs`, `bookings`, `memories` existen en ambos ORMs. Si se mantiene dual, quien es la fuente de verdad para writes?
3. **Indices automaticos**: UNIQUE en PostgreSQL crea un index automaticamente. Los `tenant_id` FK no tienen index y en tablas grandes (>100k rows) el join sera lento. Es aceptable para MVP?
4. **enums vs text**: Drizzle define enums PG (`user_role`, `clone_mode`, etc.) pero la BD actual tiene TEXT. Se migra a enums o se queda TEXT?
