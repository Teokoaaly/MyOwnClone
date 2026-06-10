# Auditoria — Coordinacion y consolidacion (TASK-360-00)

## Resumen
- **Estado:** Verde — Repositorio estable, 71/71 tests pass, TS strict clean, CI pipeline configurado
- **Riesgo principal:** Dual ORM (Drizzle + Alembic) sin sincronizacion clara; i18n no conectado; strings hardcodeados en componentes
- **Veredicto prod:** Cercano a MVP funcional. Requiere decision formal sobre fuente de verdad DB y validacion end-to-end con servicios reales

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| Frontend (Next.js 16) | ✅ | ~85% | `MyOwnClone/src/app/` — dashboard, admin, landing, login, onboarding operativos |
| Backend (Flask 3) | ✅ | ~80% | `api/` — blueprints registrados, auth con rate limiting Redis, RAG pipeline |
| DB Drizzle schema | ✅ | ~90% | `MyOwnClone/src/lib/db/schema/` — 10 tablas, relaciones, pgvector, subscriptionStatus |
| DB Alembic models | ✅ | ~70% | `api/models/` — modelos SQLAlchemy, algunas tablas compartidas |
| Auth / NextAuth v5 | ✅ | ~85% | `src/lib/auth.ts` — JWT, 3 providers, forgot/reset password, SignOutButton |
| Middleware proxy | ✅ | ~80% | `src/middleware.ts` — ruteo dinamico, tenant detection, clone cookie, DEFAULT_CLONE_ID fallback |
| RAG pipeline | ✅ | ~70% | `api/core/retrieval.py` — pgvector, Anthropic/OpenAI, confidence scoring |
| i18n | ⚠️ | ~15% | `src/i18n/` — next-intl instalado, solo 2 archivos parciales, no conectado |
| Testing | ✅ | ~60% | 71 vitest tests (10 files), 26 pytest backend, Playwright E2E configurado |
| CI/CD | ✅ | ~70% | `.github/workflows/ci.yml` — 3 jobs: backend, frontend, e2e |
| Documentacion | ✅ | ~90% | `.docs_md/` — README, manuales EN/ES, planes, diagnosticos |
| Seguridad | ✅ | ~75% | Webhook signature, timing-safe compare, Redis rate limiter, env-driven keys |

## Tablero de estado por agente

| TASK | Area | Owner | Archivo | Estado | Hallazgos |
|---|---|---|---|---|---|
| 360-00 | Coordinacion | Codex actual | `00-coordination.md` | ✅ Actualizado | Este documento |
| 360-01 | DB / Arquitectura | Agent DB | `01-db-architecture.md` | ✅ Completado | 10 hallazgos (2 P0, 4 P1, 3 P2, 1 P3), 8 tareas propuestas |
| 360-02 | Auth / Seguridad | Codex Coordinator | `02-auth-security.md` | ✅ Completado | 10 hallazgos (2 P0, 4 P1, 3 P2, 1 P3), 8 tareas propuestas |
| 360-03 | Frontend / UX | Agent Frontend | `03-frontend.md` | ✅ Completado | 10 hallazgos (P1-P3), 9 tareas propuestas |
| 360-04 | Backend / RAG | Codex Coordinator | `04-backend-rag.md` | ✅ Completado | 8 hallazgos (1 P1, 5 P2, 2 P3), 7 tareas propuestas |
| 360-05 | i18n | Agent i18n | `05-i18n.md` | ✅ Completado | 12 hallazgos (2 P0, 5 P1, 4 P2, 1 P3), 12 tareas propuestas |
| 360-06 | Integraciones | Codex Coordinator | `06-integrations.md` | ✅ Completado | 12 hallazgos, 10 tareas propuestas |
| 360-07 | Testing / CI/CD | Codex Coordinator | `07-testing-ci-prod.md` | ✅ Completado | 13 hallazgos, 12 tareas propuestas |
| 360-99 | Plan consolidado | Codex actual | `99-consolidated-action-plan.md` | ✅ Completado | 82 hallazgos, 75 tareas propuestas, 6 fases de ejecucion |

## Fases completadas (Fase 0-6)

| Fase | Commit | Contenido | Estado |
|---|---|---|---|
| Fase 0 | `af9cf6c` | Estabilizacion critica: graphon imports, broken retrieval import, i18n alignment, login callback | ✅ |
| Fase 1 | `3fb50c8` | Seguridad: webhook signature, timing-safe compare, env-driven service key, Redis rate limiter | ✅ |
| Fase 2 | `299cff3` | Auth: SignOutButton, forgot-password, reset-password, magic link verification | ✅ |
| Fase 3 | `409b4ea` | DB: schema unification, dynamic clone resolution, seed script, clone helpers | ✅ |
| Fase 4 | `629eacd` | TS strict, ESLint cleanup, dead files (-847 lines), HTML sanitization | ✅ |
| Fase 5 | `e68ed69` | E2E: Playwright setup, 10 E2E tests, CI 3-job pipeline | ✅ |
| Fase 6 | `cd29fb7` | Test fixes (i18n EN), Stripe webhook, onboarding wizard | ✅ |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| C00-001 | P0 | Dual ORM sin fuente de verdad unica | Tablas compartidas pueden divergir entre Drizzle y Alembic | `src/lib/db/schema/` vs `api/models/` — ambas definen `clone_configs`, `bookings` | Elegir Drizzle como fuente de verdad y migrar modelos SQLAlchemy a reflejar schema Drizzle, o viceversa |
| C00-002 | P1 | next-intl instalado pero no conectado | No hay ruteo por locale ni deteccion de idioma | `next.config.ts` sin plugin, `src/app/layout.tsx:31` hardcodea `locale = "en"` | Activar next-intl/plugin, migrar rutas a `[locale]`, completar `en.json` |
| C00-003 | P1 | Textos del dashboard desalineados con el producto | "build or query / endpoints / schema design" vs clon de IA | `resumen/page.tsx:190-207` — placeholder y ejemplos equivocados | Ver `.docs_md/DASHBOARD_MESSAGING_PLAN.md` Fase 1 |
| C00-004 | P2 | Sidebar labels confusas para el usuario final | Search/Crawl/Extract/Research suenan a scraping, no a clon | `dashboard/layout.tsx:21-29` — labels hardcodeadas | Renombrar a Knowledge/Memories/Inbox/Products |
| C00-005 | P2 | stripe.ts eliminado en Fase 4 | Si se necesita en el futuro hay que restaurarlo | No existen en `src/lib/` — verificacion post-cleanup | Confirmar que no hay imports pendientes; mantener como referencia |
| C00-006 | P2 | Onboarding wizard no auto-redirige nuevos usuarios | Usuarios nuevos van a /resumen sin clone creado | `register-form.tsx` redirige a `/resumen`, no a `/onboarding` | Considerar redirect a `/onboarding` si usuario tiene 0 clones |
| C00-007 | P3 | uuidv7() envuelve uuid4() | No es UUIDv7 real, solo uuid4 con formato | `src/lib/db/schema/helpers.ts` | Aceptar para MVP; considerar `@lukeed/uuid` para v7 real |

## Matriz de interconexion frontend-backend-DB (flujos criticos)

### Flujo: Login / Autenticacion

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | LoginForm | `login/login-form.tsx` | ✅ Funcional | Texto hardcodeado (sin i18n) |
| Frontend | NextAuth route | `app/api/auth/[...nextauth]/route.ts` | ✅ Funcional | — |
| Auth Lib | JWT + authorize | `lib/auth.ts` | ✅ Funcional | Usa raw SQL (workaround para enum faltante) |
| Middleware | Proxy + CSRF | `middleware.ts` | ✅ Funcional | — |
| Backend | Auth blueprint | `api/controllers/console/auth.py` | ✅ Funcional | Rate limiting con Redis + fallback memoria |
| Backend | JWT utils | `api/libs/jwt_utils.py` | ✅ Funcional | — |
| DB | Users | `schema/users.ts` | ⚠️ Parcial | Enum `user_role` no existe en PG (creado como TEXT) |

### Flujo: Chat con clon (RAG)

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | ChatPanel | `components/chat/ChatPanel.tsx` | ✅ Funcional | — |
| Middleware | Proxy | `middleware.ts` | ✅ Funcional | Depende de clone_id cookie |
| Backend | RAG pipeline | `api/core/retrieval.py` | ✅ Funcional | — |
| Backend | LLM model manager | `api/core/model_manager.py` | ✅ Funcional | — |
| DB | Chunks + pgvector | `schema/chunks.ts` | ✅ Funcional | — |
| DB | Clone configs | `schema/clones.ts` | ✅ Funcional | — |

### Flujo: Fuentes de conocimiento

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Biblioteca | `biblioteca/page.tsx` | ⚠️ Parcial | No revisado en profundidad |
| API Route | Sources CRUD | `api/clone/sources/route.ts` | ✅ Funcional | — |
| Backend | Ingestion | `api/core/ingestion.py` | ⚠️ No verificado | — |
| DB | Sources | `schema/sources.ts` | ✅ Funcional | — |

### Flujo: Email inbound

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Inbox | `inbox/page.tsx` | ⚠️ Parcial | No revisado |
| Backend | Email processor | `api/core/myownclone/email_processor.py` | ⚠️ No verificado | — |
| Backend | Email AI | `api/core/myownclone/email_ai.py` | ⚠️ No verificado | — |
| Backend | SendGrid webhook | `api/controllers/myownclone_public.py` | ✅ Firma validada | — |
| DB | Emails | `schema/emails.ts` | ✅ Funcional | — |

### Flujo: Booking / Reuniones

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Reuniones | `reuniones/page.tsx` | ⚠️ No verificado | — |
| API Route | Bookings | `api/bookings/route.ts` | ✅ Existe | No revisado |
| Backend | Booking controller | `api/controllers/console/myownclone/booking.py` | ⚠️ No verificado | — |
| DB | Bookings + Availability | `schema/bookings.ts` | ✅ Funcional | — |

### Flujo: Stripe billing

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Facturacion | `facturacion/page.tsx` | ✅ Funcional | Tests pasan |
| API Route | Stripe webhook | `api/stripe/webhook/route.ts` | ✅ Firma HMAC verificada | — |
| Backend | Stripe controller | `api/controllers/console/myownclone/stripe_ctrl.py` | ⚠️ No verificado | — |
| DB | Tenants (plan/status) | `schema/tenants.ts` | ✅ subscriptionStatus añadido | — |

### Flujo: Impersonacion admin

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | ImpersonateButton | `components/admin/ImpersonateButton.tsx` | ✅ Existe | No revisado |
| Backend | Admin impersonate | `api/controllers/console/myownclone/admin_platform.py:127-185` | ✅ Existe | Token hasheado con SHA-256 + pepper |
| DB | Impersonation logs | Admin model (SQLAlchemy) | ⚠️ No verificado | — |

### Flujo: Onboarding / Creacion de clone

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend | Onboarding wizard | `(dashboard)/onboarding/page.tsx` | ✅ 4 pasos | No auto-redirige desde registro |
| Frontend | OnboardingBanner | `components/dashboard/OnboardingBanner.tsx` | ✅ En resumen | Solo aparece si 0 clones |
| API Route | Clone creation | `api/clone/clones` proxy | ✅ Funcional | — |
| Backend | Clone controller | Flask backend | ✅ Funcional | — |
| DB | Clone configs | `schema/clones.ts` | ✅ Funcional | — |

## Documentos de referencia existentes

| Documento | Contenido | Usar para |
|---|---|---|
| `.docs_md/MASTER_PLAN.md` | Plan maestro original | Comparar avance vs plan inicial |
| `.docs_md/DIAGNOSTICO_TECNICO.md` | Diagnostico tecnico completo | Validar hallazgos de DB, auth, RAG |
| `.docs_md/DESIGN_SYSTEM.md` | Sistema de disenio | Frontend audit reference |
| `.docs_md/I18N_50_LANGUAGES_PLAN.md` | Plan de 50 idiomas | TASK-360-05 input |
| `.docs_md/DASHBOARD_MESSAGING_PLAN.md` | Plan de alineacion de textos | TASK-360-03 input |
| `.docs_md/Task.md` | Checklist de tareas | Validar cobertura |
| `.docs_md/IMPLEMENTATION_LOG.md` | Log de implementacion | Historico de cambios |
| `.docs_md/AUTH_SOURCE_OF_TRUTH.md` | Decision NextAuth vs Flask JWT | Auth audit reference |

## Open Questions

1. **Dual ORM**: Se decidio mantener ambos o migrar a uno solo? La respuesta condiciona P0-C00-001.
2. **next-intl**: Se quiere `localePrefix: "never"` (cookie, facil) o `prefix` (SEO, mas trabajo)? La eleccion condiciona el middleware.
3. **stripe.ts eliminado**: Era intencional o se perdio en la limpieza? Si se necesita, restaurar desde git history.
4. **Orden de ejecucion**: Para implementacion, conviene arrancar por P0 de DB, Auth e i18n; el orden final se decide en el consolidado.
5. **Criterio de "Completo"**: Se adopta como referencia operativa: funcional + testeado + documentado + i18n-ready.

## Notas para agentes

- **Anti-conflicto**: Ejecutar `git status --short` antes de empezar. No revertir cambios ajenos.
- **Evidencias**: Incluir ruta concreta y linea aproximada en cada hallazgo.
- **P0 fuera de area**: Documentar en propio documento y notificar via `Open Questions`.
- **Formato**: Seguir la plantilla de AGENT_AUDIT_TASKS.md estrictamente.
- **Entrega**: Cada agente escribe su documento en `.docs_md/audit/<numero>-<area>.md`.

## Estado operativo

- Protocolo de rama compartida verificado y cerrado: los 8 documentos de auditoria fueron entregados y consolidados.
- `99-consolidated-action-plan.md` ya es la fuente de verdad para la fase siguiente de implementacion.
- `00-coordination.md` queda como snapshot de coordinacion y registro del cierre de auditoria.
