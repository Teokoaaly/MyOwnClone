# Plan Consolidado de Accion (TASK-360-99)

> Generado: 2026-06-10 | Auditoria 360 completada | 8/8 documentos entregados

---

## Resumen ejecutivo

Auditoria 360 completa. Se revisaron **8 areas** del repositorio, generando **82 hallazgos** (7 P0, 25 P1, 34 P2, 16 P3) y **75 tareas propuestas**. El repositorio esta funcional para MVP pero requiere decisiones arquitectonicas (dual ORM, i18n routing) antes de escalar a produccion real.

**Mayor riesgo:** Dual ORM sin fuente de verdad clara puede causar divergencias silenciosas en datos compartidos entre frontend (Drizzle) y backend (Alembic).

---

## Estado por prioridad

### P0 — Bloqueadores de produccion (7)

| ID | Hallazgo | Area | Fuente | Owner sugerido | Estimacion |
|---|---|---|---|---|---|
| D01-001 | Dual ORM sin fuente de verdad unica | DB | `01-db-architecture.md` | Agent DB | 2-3d |
| D01-002 | Tablas backend sin migracion Drizzle | DB | `01-db-architecture.md` | Agent DB | 1-2d |
| A02-001 | PLATFORM_ADMIN_PASSWORD_HASH vacio | Auth | `02-auth-security.md` | Agent Security | 0.3d |
| A02-002 | Proxy auth usa 'proxy-service' como tenant_id UUID | Auth | `02-auth-security.md` | Agent Backend | 0.5d |
| F05-001 | next-intl no conectado a codigo productivo | i18n | `05-i18n.md` | Agent i18n | 1d |
| F05-002 | Sin ruteo por locale | i18n | `05-i18n.md` | Agent i18n | 1d |
| C00-001 | Dual ORM divergencias en tablas compartidas | DB | `00-coordination.md` | Agent DB | 2-3d |

### P1 — Mejoras criticas (25)

| ID | Hallazgo | Area | Fuente | Owner sugerido | Estimacion |
|---|---|---|---|---|---|
| D01-003 | Indice IVFFlat sin parametros optimos | DB | `01-db-architecture.md` | Agent DB | 0.5d |
| D01-004 | Faltan indices en tenant_id FK | DB | `01-db-architecture.md` | Agent DB | 0.5d |
| D01-005 | CSS muerto (chat-orb, landing-brand-mark) | DB | `01-db-architecture.md` | Agent Frontend | 0.3d |
| A02-003 | Workaround SQL raw en auth.ts | Auth | `02-auth-security.md` | Agent DB | 0.5d |
| A02-004 | Roles no verificados consistentemente | Auth | `02-auth-security.md` | Agent Frontend | 0.5d |
| A02-005 | Sin CSRF en API Routes | Auth | `02-auth-security.md` | Agent Frontend | 1d |
| F03-001 | Cero uso de next-intl en componentes | Frontend | `03-frontend.md` | Agent i18n | 2-3d |
| F03-002 | Sin loading.tsx ni error.tsx | Frontend | `03-frontend.md` | Agent Frontend | 1d |
| F03-003 | Ninguna pagina exporta metadata | Frontend | `03-frontend.md` | Agent Frontend | 0.5d |
| F05-003 | en.json incompleto (~63 de ~500 keys) | i18n | `05-i18n.md` | Agent i18n | 2d |
| F05-004 | Sin LanguageSwitcher UI | i18n | `05-i18n.md` | Agent Frontend | 0.5d |
| F05-005 | Sidebar labels hardcodeadas | i18n | `05-i18n.md` | Agent Frontend | 0.5d |
| B04-001 | Public chat endpoint incompleto | Backend | `04-backend-rag.md` | Agent Backend | 0.5d |
| B04-002 | Weaviate remnants en codigo | Backend | `04-backend-rag.md` | Agent Backend | 0.5d |
| B04-003 | Ingestion no auditada | Backend | `04-backend-rag.md` | Agent Backend | 1d |
| +10 mas de 06-integrations.md y 07-testing-ci-prod.md | Varias | Auditoria | Varios | Varias |

### P2 — Mejoras recomendadas (34)

Hallazgos distribuidos entre todas las areas:
- DB: indices, migraciones versionadas, enum user_role (D01-006 a D01-008)
- Auth: public chat rate limit, secrets en texto plano, webhook Stripe (A02-006 a A02-008)
- Frontend: textos desalineados, sidebar, API routes sin validacion (F03-004 a F03-007)
- i18n: landing/login/admin hardcodeados, RTL, SignOutButton español (F05-006 a F05-010)
- Backend: cost tracking, silo dependency, health endpoint (B04-004 a B04-006)
- Integraciones y Testing: varios hallazgos (06/07)

### P3 — Bajas / mejoras futuras (16)

Hallazgos menores: uuidv7 wrapper, seed con IDs fijos, logout sin invalidacion, etc.

---

## Tareas propuestas por fase

### Fase 7 — Arquitectura DB (P0)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-701 | Decidir y documentar fuente de verdad DB (Drizzle vs Alembic) | P0 | Coordinador | 1d | — |
| T-702 | Unificar esquema Drizzle como fuente de verdad | P0 | Agent DB | 2d | T-701 |
| T-703 | Crear schemas Drizzle para tablas exclusivas backend | P0 | Agent DB | 2d | T-701 |
| T-704 | Añadir indices a columnas tenant_id FK | P1 | Agent DB | 0.5d | — |
| T-705 | Optimizar indice IVFFlat con lists parametrizado | P1 | Agent DB | 0.5d | — |
| T-706 | Migrar de drizzle-kit push a generate+migrate | P2 | Agent DB | 0.5d | — |
| T-707 | Crear enum user_role en BD y eliminar SQL raw en auth.ts | P1 | Agent DB | 0.5d | T-701 |

### Fase 8 — Auth y Seguridad (P0/P1)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-801 | Configurar PLATFORM_ADMIN_PASSWORD_HASH con hash escapado | P0 | Agent Security | 0.3d | — |
| T-802 | Extender parche proxy-service a clone/booking/stripe controllers | P0 | Agent Backend | 0.5d | — |
| T-803 | Añadir guard de roles por ruta en dashboard layout | P1 | Agent Frontend | 0.5d | — |
| T-804 | Implementar CSRF protection en API Routes mutantes | P1 | Agent Frontend | 1d | — |
| T-805 | Añadir rate limiting por IP en middleware para chat publico | P2 | Agent Frontend | 0.5d | — |

### Fase 9 — i18n (P0)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-901 | Conectar next-intl: plugin + middleware i18n | P0 | Agent i18n | 1d | — |
| T-902 | Decidir estrategia de ruteo (cookie vs URL prefix) | P0 | Coordinador | 0.5d | — |
| T-903 | Completar en.json con todas las keys (~500) | P1 | Agent i18n | 2d | T-901 |
| T-904 | Crear LanguageSwitcher component | P1 | Agent Frontend | 0.5d | T-901 |
| T-905 | Migrar Sidebar labels a useTranslations() | P1 | Agent Frontend | 0.5d | T-903 |
| T-906 | Migrar Landing, Login, Register, Admin a useTranslations() | P2 | Agent Frontend | 2d | T-903 |
| T-907 | Añadir soporte RTL en globals.css | P2 | Agent Frontend | 0.5d | — |

### Fase 10 — Frontend/UX (P1)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-1001 | Añadir loading.tsx y error.tsx a dashboard, admin, public | P1 | Agent Frontend | 1d | — |
| T-1002 | Añadir generateMetadata() en landing, login, registro | P1 | Agent Frontend | 0.5d | — |
| T-1003 | Alinear textos del Command Center con el producto | P1 | Agent Frontend | 0.5d | — |
| T-1004 | Migrar dashboard pages a Server Components gradualmente | P2 | Agent Frontend | 2d | — |
| T-1005 | Renombrar sidebar labels (Search→Knowledge, etc.) | P2 | Agent Frontend | 0.5d | T-905 |
| T-1006 | Añadir Zod validation en API Routes | P2 | Agent Frontend | 1d | — |

### Fase 11 — Backend/RAG (P1)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-1101 | Verificar endpoint POST chat publico | P1 | Agent Backend | 0.5d | — |
| T-1102 | Limpiar Weaviate remnants en core/rag/ | P1 | Agent Backend | 0.5d | — |
| T-1103 | Auditar ingestion.py (estados, timeouts, errores) | P1 | Agent Backend | 1d | — |
| T-1104 | Integrar cost tracking por tenant en model_manager | P2 | Agent Backend | 1d | — |
| T-1105 | Añadir endpoint /health | P2 | Agent Backend | 0.5d | — |

### Fase 12 — Testing/CI (P1/P2)

| ID | Tarea | Prioridad | Owner | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-1201 | Ejecutar Playwright E2E con servicios reales | P1 | Agent QA | 1d | — |
| T-1202 | Añadir tests de integracion para flujos criticos | P1 | Agent QA | 2d | T-1201 |
| T-1203 | Configurar coverage minimo en CI | P2 | Agent QA | 0.5d | — |
| T-1204 | Verificar deploy scripts contra estado actual | P2 | Agent QA | 1d | — |

---

## Roadmap de ejecucion recomendado

```
Semana 1 (P0s):
  ├── T-701  Decidir fuente de verdad DB          [Coordinador]
  ├── T-801  PASSWORD_HASH                         [Security]
  ├── T-802  Proxy UUID parche extension           [Backend]
  ├── T-901  Conectar next-intl                    [i18n]
  └── T-902  Decidir i18n routing                  [Coordinador]

Semana 2 (P1s):
  ├── T-702  Unificar Drizzle como fuente verdad   [DB]
  ├── T-703  Schemas Drizzle tablas backend        [DB]
  ├── T-707  Enum user_role + eliminar SQL raw     [DB]
  ├── T-803  Guard de roles en dashboard           [Frontend]
  ├── T-903  Completar en.json                     [i18n]
  ├── T-1001 loading/error states                  [Frontend]
  ├── T-1101 Public chat endpoint                  [Backend]
  └── T-1102 Limpiar Weaviate                     [Backend]

Semana 3 (P1s + P2s):
  ├── T-704/705 Indices DB                         [DB]
  ├── T-804  CSRF protection                       [Frontend]
  ├── T-904  LanguageSwitcher                      [Frontend]
  ├── T-905  Sidebar i18n                          [Frontend]
  ├── T-1003 Textos dashboard                      [Frontend]
  ├── T-1002 Metadata SEO                          [Frontend]
  ├── T-1103 Auditar ingestion                     [Backend]
  └── T-1201 E2E tests                             [QA]

Semana 4 (P2s + P3s):
  ├── T-906  Landing/Login/Admin i18n              [Frontend]
  ├── T-1004 Server Components migration           [Frontend]
  ├── T-1006 Zod validation API Routes             [Frontend]
  ├── T-1104 Cost tracking                         [Backend]
  ├── T-1105 Health endpoint                       [Backend]
  ├── T-1202-1204 Tests + coverage + deploy        [QA]
  └── T-706  Drizzle generate+migrate              [DB]
```

---

## Flujos criticos — matriz frontend-backend-DB

| Flujo | Frontend | Backend | DB/Servicio | Estado | Gaps principales |
|---|---|---|---|---|---|
| Login | ✅ login-form.tsx | ✅ auth.py | ⚠️ users (enum) | 🟡 | i18n, enum user_role, CSRF |
| Chat RAG | ✅ ChatPanel | ✅ retrieval.py | ✅ chunks+pgvector | 🟢 | Public endpoint POST? |
| Fuentes | ⚠️ biblioteca | ⚠️ ingestion.py | ✅ sources | 🟡 | No auditado |
| Email | ⚠️ inbox | ⚠️ email_processor | ✅ emails | 🟡 | No auditado |
| Booking | ⚠️ reuniones | ⚠️ booking.py | ✅ bookings | 🟡 | No auditado |
| Stripe | ⚠️ facturacion | ⚠️ stripe_ctrl | ✅ tenants | 🟡 | stripe.ts eliminado |
| Admin | ✅ admin/* | ✅ admin_platform | ⚠️ logs | 🟢 | — |
| i18n | ❌ No conectado | N/A | ❌ en.json parcial | 🔴 | next-intl desconectado |
| Testing | ✅ 71 vitest | ✅ 26 pytest | N/A | 🟢 | Faltan E2E reales |

---

## Open Questions para el coordinador

1. **Dual ORM**: Se unifica a Drizzle como fuente de verdad o se mantiene dual con documentacion? Desbloquea T-702, T-703, T-707.
2. **i18n routing**: `localePrefix: "never"` (cookie, facil, sin SEO) o `prefix` (URL /en/..., SEO, mas trabajo)? Desbloquea T-902, T-904.
3. **Orden de ejecucion**: P0s primero (DB + i18n + auth) o en paralelo? Se puede correr DB y auth en paralelo, i18n secuencial.
4. **stripe.ts eliminado**: Fue intencional? Si se necesita, restaurar desde git history.
5. **Criterio de cierre**: Que define "listo para produccion"? Sugerencia: DB unificada + i18n conectado + CSRF + E2E pasando + health endpoint.

---

## Metricas de estado

| Metrica | Valor | Nota |
|---|---|---|
| Vitest tests | 71/71 pass | Frontend |
| Pytest tests | 26/26 pass | Backend |
| TypeScript strict | Clean | 0 errores |
| E2E tests | 10 configurados | Playwright |
| CI pipeline | 3 jobs | backend, frontend, e2e |
| Documentos auditoria | 8/8 | Completados |
| Hallazgos P0 | 7 | DB(2), Auth(2), i18n(2), Coord(1) |
| Hallazgos P1 | 25 | Distribuidos |
| Hallazgos P2 | 34 | Distribuidos |
| Hallazgos P3 | 16 | Distribuidos |
| Tareas propuestas | 75 | En 6 fases (7-12) |
| Estimacion total | ~20-25 dias | 4 semanas |
| Servidores | Frontend: 200, Backend: funcional | Ambos operativos |

---

*Fin del plan consolidado de accion — Auditoria 360 completada*
