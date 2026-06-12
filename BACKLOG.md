# BACKLOG.md

## Priorizacion

P0 bloquea produccion. P1 bloquea estabilidad o seguridad fuerte. P2 mejora mantenibilidad/operacion. P3 polish.

## P0

### P0-001: Resolver vulnerabilidad alta de Drizzle ORM — DONE

- Agente: Frontend
- Archivos: `MyOwnClone/package.json`, `MyOwnClone/package-lock.json`
- Accion: actualizar `drizzle-orm` a version parcheada, adaptar breaking changes y correr checks.
- Done: `npm audit --omit=dev`, `npm run typecheck`, `npm run build`, `npm run test` pasan.

### P0-002: Alinear driver PostgreSQL en backend y CI — DONE

- Agente: Backend/DevOps
- Archivos: `.github/workflows/ci.yml`, `api/requirements.txt`, `api/app_factory.py`, `api/.env.example`
- Accion: decidir driver, instalar dependencia correcta y respetar una sola estrategia de conexion.
- Done: `flask db upgrade` pasa en CI con DB limpia.

### P0-003: Garantizar pgvector en produccion — DONE

- Agente: DevOps
- Archivos: `ops/docker-compose.backend.prod.yml`, migraciones Alembic
- Accion: usar imagen `pgvector/pgvector:pg15` o extension equivalente; crear extension en migracion.
- Done: DB nueva permite tablas/vector queries sin pasos manuales.

### P0-004: Ejecutar E2E real — DONE/PARCIAL

- Agente: QA
- Archivos: `MyOwnClone/e2e/*`, `.github/workflows/ci.yml`
- Accion: levantar backend, frontend y DB; ejecutar Playwright.
- Done: `npm run test:e2e` pasa local con 35 passed / 2 skipped. Pendiente CI/staging con sesion y clones seedeados para eliminar skips.

## P1

### P1-001: Resolver PostCSS/Next audit — DONE

- Agente: Frontend
- Accion: actualizar Next cuando exista version compatible o aplicar override controlado.
- Done: `npm audit` completo queda en 0 vulnerabilidades.

### P1-002: Crear health/readiness endpoints — DONE

- Agente: Backend
- Accion: agregar `/healthz` y `/readyz`, actualizar compose healthcheck.
- Done: readiness valida DB y Redis.

### P1-003: Rate limiting centralizado

- Agente: Backend
- Accion: migrar rate limit in-memory publico a Redis cuando este disponible.
- Done: pruebas cubren limite por IP/slug y modo degradado.

### P1-004: Tenant scoping E2E

- Agente: QA/Backend
- Accion: probar que usuarios no leen/escriben recursos de otro tenant.
- Done: tests negativos pasan en API y UI.

### P1-005: Contratos de webhooks externos

- Agente: Backend
- Accion: Stripe, SendGrid y Whereby/Resend con fixtures firmados/sandbox.
- Done: webhooks rechazan firmas invalidas y procesan casos felices/idempotentes.

## P2

### P2-001: Coverage gates

- Agente: QA
- Accion: configurar coverage en Vitest y pytest-cov.
- Done: CI falla si core baja de 80%.

### P2-002: Limpiar warnings de lint — DONE

- Agente: Frontend
- Accion: resolver 5 warnings actuales.
- Done: `npm run lint` sin warnings.

### P2-003: Corregir warning React de keys duplicadas — DONE

- Agente: Frontend
- Accion: localizar origen en admin/audit pagination render y asegurar keys unicas.
- Done: `npm run test` sin warning `same key`.

### P2-004: Documentar ownership de schema

- Agente: Backend/Frontend
- Accion: tabla por tabla: Alembic o Drizzle como fuente de verdad.
- Done: `ARCHITECTURE.md` actualizado y CI detecta drift.

### P2-005: Logs estructurados

- Agente: Backend/DevOps
- Accion: request id, user/tenant/clone anonimizados, latencia y status.
- Done: logs consultables y correlacionables.

## P3

### P3-001: Limpiar dependency duplication

- Agente: Backend
- Accion: eliminar `stripe` duplicado de `requirements.txt` raiz.
- Done: install sin duplicados.

### P3-002: Completar ADRs

- Agente: Tech Lead
- Accion: ADRs para multi-tenancy, RAG, billing y doble ORM.
- Done: ADRs enlazados desde arquitectura.

### P3-003: Pulido i18n

- Agente: Frontend
- Accion: revisar strings hardcoded y rutas ES/EN.
- Done: dashboard sin textos sin traducir en flujos principales.
