# AGENT_AUDIT_TASKS.md — Auditoria 360 multiagente
> Creado: 2026-06-10  
> Objetivo: repartir la auditoria de MyOwnClone entre varios agentes sin pisarse.

---

## Regla principal

Esta ronda es de **analisis y plan de accion**, no de implementacion. Ningun agente debe cambiar codigo productivo salvo que el coordinador lo autorice explicitamente.

Cada agente trabaja en su propio documento de hallazgos y solo toca los archivos asignados en este task. Si encuentra un P0 fuera de su area, lo documenta y avisa al coordinador, pero no invade el ownership de otro agente.

---

## Protocolo anti-conflictos

1. Antes de empezar, ejecutar `git status --short` y no revertir cambios ajenos.
2. Cada agente crea o edita solo su documento en `.docs_md/audit/`.
3. No editar `README.md`, `.env*`, migraciones, codigo frontend, codigo backend ni tests durante esta fase.
4. Usar evidencias con rutas concretas y, cuando sea posible, linea aproximada.
5. Clasificar cada hallazgo como `P0`, `P1`, `P2` o `P3`.
6. Registrar dudas o bloqueos en la seccion `Open Questions` del documento propio.
7. El coordinador consolida, deduplica y transforma hallazgos en issues accionables.

---

## Protocolo dinamico en una sola rama

Cuando todos los agentes trabajan sobre el mismo repositorio y la misma rama, se usa este flujo para evitar colisiones:

### 1. Archivos compartidos permitidos

Solo estos archivos pueden recibir escrituras coordinadas:

```text
.docs_md/audit/00-coordination.md
.docs_md/audit/99-consolidated-action-plan.md
.docs_md/audit/_locks.md
.docs_md/audit/_inbox.md
```

Regla: solo el coordinador edita `00-coordination.md` y `99-consolidated-action-plan.md`. Todos los agentes pueden proponer entradas en `_inbox.md`. Para `_locks.md`, cada agente solo edita su propia fila.

### 2. Locks ligeros

Antes de escribir su documento, cada agente registra su lock en `.docs_md/audit/_locks.md`:

```md
| Agent | Task | File | Status | Since | Last heartbeat | Notes |
| Agent DB | TASK-360-01 | 01-db-architecture.md | working | 2026-06-10 13:40 | 2026-06-10 13:55 | Comparando Drizzle/Alembic |
```

Estados validos:

- `working`: esta leyendo o escribiendo su documento.
- `blocked`: necesita decision del coordinador.
- `review-ready`: entrego documento y espera consolidacion.
- `done`: consolidado por coordinacion.

Si un lock lleva mas de 30 minutos sin `Last heartbeat`, otro agente no debe sobrescribirlo: avisa en `_inbox.md` y espera decision del coordinador.

### 3. Inbox de eventos

Cuando un agente detecta algo que afecta a otro owner, lo escribe en `.docs_md/audit/_inbox.md` sin modificar el archivo ajeno:

```md
## 2026-06-10 14:05 — Agent Security -> Agent Integrations
- Tipo: posible P0 cruzado
- Contexto: Stripe webhook parece no validar idempotencia.
- Evidencia: `MyOwnClone/src/app/api/stripe/webhook/route.ts`
- Accion solicitada: confirmar en TASK-360-06.
```

Tipos recomendados:

- `possible-p0`
- `cross-area`
- `needs-decision`
- `duplicate-finding`
- `ready-for-review`

### 4. Ciclo de trabajo de cada agente

1. Leer `AGENT_AUDIT_TASKS.md`.
2. Ejecutar `git status --short`.
3. Revisar `_locks.md`.
4. Anadir o actualizar su fila de lock.
5. Trabajar solo en su archivo asignado.
6. Registrar cruces en `_inbox.md`.
7. Cambiar su lock a `review-ready`.
8. No consolidar su propio trabajo en `99-consolidated-action-plan.md`.

### 5. Ciclo del coordinador

El coordinador revisa periodicamente:

```text
.docs_md/audit/_locks.md
.docs_md/audit/_inbox.md
.docs_md/audit/*.md
```

Y actualiza:

- `00-coordination.md`: estado vivo, owners, bloqueos, duplicados.
- `99-consolidated-action-plan.md`: solo cuando haya documentos `review-ready`.

Cadencia recomendada: cada 15-30 minutos o cuando un agente marque `review-ready`.

### 6. Regla de oro

Si dos agentes necesitan tocar el mismo archivo, gana el owner declarado en este documento. El otro agente deja una entrada en `_inbox.md` con evidencia y recomendacion.

---

## Estructura de entregables

Cada agente debe entregar un Markdown con este formato:

```md
# Auditoria — <area>

## Resumen
- Estado: Verde / Amarillo / Rojo
- Riesgo principal:
- Veredicto prod:

## Mapa de estado actual
| Componente | Existe | Completo | Evidencia |

## Hallazgos priorizados
| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |

## Matriz de interconexion
| Flujo | Frontend | Backend | DB/Servicio | Estado | Gaps |

## Tareas propuestas
| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |

## Open Questions
```

Los documentos viven en:

```text
.docs_md/audit/
├── 00-coordination.md
├── 01-db-architecture.md
├── 02-auth-security.md
├── 03-frontend.md
├── 04-backend-rag.md
├── 05-i18n.md
├── 06-integrations.md
├── 07-testing-ci-prod.md
└── 99-consolidated-action-plan.md
```

---

## TASK-360-00 — Coordinacion y consolidacion

**Owner:** Codex actual  
**Prioridad:** P0  
**Archivo permitido:** `.docs_md/audit/00-coordination.md`, `.docs_md/audit/99-consolidated-action-plan.md`

### Objetivo
Coordinar la auditoria, evitar duplicidades, mantener el mapa de owners y consolidar los resultados finales en un plan accionable.

### Alcance
- Crear el indice de auditoria.
- Mantener el tablero de estado por agente.
- Resolver solapamientos entre areas.
- Consolidar P0/P1 en un roadmap final.
- Comparar los hallazgos contra docs existentes: `.docs_md/Task.md`, `.docs_md/MASTER_PLAN.md`, `.docs_md/DIAGNOSTICO_TECNICO.md`.

### Entregables
- `.docs_md/audit/00-coordination.md`
- `.docs_md/audit/99-consolidated-action-plan.md`
- Lista final de issues ordenados por criticidad.

---

## TASK-360-01 — DB, arquitectura y multi-tenancy

**Owner sugerido:** Agent DB/Architecture  
**Prioridad:** P0  
**Archivo permitido:** `.docs_md/audit/01-db-architecture.md`

### Zonas de lectura
- `MyOwnClone/src/lib/db/schema/`
- `MyOwnClone/drizzle/`
- `api/models/`
- `api/migrations/`
- `api/controllers/**`
- `api/services/`

### Objetivo
Validar consistencia Drizzle vs SQLAlchemy/Alembic, relaciones, indices, pgvector y aislamiento multi-tenant.

### Preguntas clave
- Que schema es fuente de verdad real?
- Que tablas no tienen `tenant_id` y deberian tenerlo?
- Que queries acceden a datos tenant-scoped sin filtro de tenant?
- Faltan indices para RAG, analytics, inbox, billing o bookings?
- Hay cascadas peligrosas o integridad referencial incompleta?

### No tocar
Migraciones, modelos, seed, schema Drizzle.

---

## TASK-360-02 — Auth, autorizacion y seguridad

**Owner sugerido:** Agent Security/Auth  
**Prioridad:** P0  
**Archivo permitido:** `.docs_md/audit/02-auth-security.md`

### Zonas de lectura
- `MyOwnClone/src/lib/auth.ts`
- `MyOwnClone/src/middleware.ts`
- `MyOwnClone/src/app/api/auth/`
- `api/libs/jwt_utils.py`
- `api/libs/login.py`
- `api/libs/security_checks.py`
- `api/controllers/console/wraps.py`
- `api/controllers/console/auth.py`
- `api/controllers/console/myownclone/admin_platform.py`

### Objetivo
Auditar autenticacion, sesiones, roles, permisos, CSRF, rate limiting, impersonation, API keys y fugas de secretos.

### Preguntas clave
- Todas las rutas protegidas exigen sesion o token?
- Los roles `owner`, `admin`, `member`, `platform_admin` tienen checks consistentes?
- Hay escalada de privilegios por parametros manipulables?
- JWT/session incluye datos sensibles?
- Existen rate limits en login, chat publico y endpoints publicos?
- Webhooks validan firma e idempotencia?

### No tocar
Middleware, auth config, env examples, controladores.

---

## TASK-360-03 — Frontend, App Router y UX

**Owner sugerido:** Agent Frontend  
**Prioridad:** P1  
**Archivo permitido:** `.docs_md/audit/03-frontend.md`

### Zonas de lectura
- `MyOwnClone/src/app/`
- `MyOwnClone/src/components/`
- `MyOwnClone/src/hooks/`
- `MyOwnClone/src/lib/`
- `MyOwnClone/src/app/api/`

### Objetivo
Mapear rutas, layouts, loading/error states, API routes, accesibilidad, estados UI y acoplamientos frontend-backend.

### Preguntas clave
- Que rutas del dashboard/admin/public existen y cuales estan incompletas?
- Faltan `loading.tsx`, `error.tsx`, metadata o proteccion?
- Las API routes validan input, errores y auth?
- Hay strings hardcodeadas que pertenecen a i18n?
- Los flujos principales conectan con backend real o usan mocks/stubs?

### No tocar
Componentes, paginas, estilos, API routes.

---

## TASK-360-04 — Backend, RAG y logica de negocio

**Owner sugerido:** Agent Backend/RAG  
**Prioridad:** P0  
**Archivo permitido:** `.docs_md/audit/04-backend-rag.md`

### Zonas de lectura
- `api/app_factory.py`
- `api/controllers/`
- `api/core/`
- `api/services/`
- `api/models/`

### Objetivo
Auditar application factory, blueprints, controladores, pipeline RAG, ingestion, model manager, silos, email processor y booking.

### Preguntas clave
- Todos los blueprints estan registrados y alcanzables?
- Cada endpoint valida auth, tenant y payload?
- RAG usa pgvector de forma consistente o quedan restos de Weaviate?
- Ingestion maneja estados `processing`, `ready`, `failed`?
- Hay timeouts/retries/logging en llamadas LLM?
- Los silos filtran correctamente por modo y tenant?

### No tocar
Controladores, core logic, modelos, requirements.

---

## TASK-360-05 — i18n multilenguaje

**Owner sugerido:** Agent i18n  
**Prioridad:** P1  
**Archivo permitido:** `.docs_md/audit/05-i18n.md`

### Zonas de lectura
- `MyOwnClone/src/i18n/`
- `MyOwnClone/src/middleware.ts`
- `MyOwnClone/src/app/`
- `MyOwnClone/src/components/`
- Plantillas de email en frontend/backend si existen.

### Objetivo
Validar next-intl, routing ES/EN, cobertura de keys, strings hardcodeadas y preparacion para PT/FR/DE.

### Preguntas clave
- El middleware i18n conflictua con auth?
- Existen keys equivalentes en `es.json` y `en.json`?
- Que componentes tienen texto hardcodeado?
- Emails, errores API y SEO estan preparados para traduccion?
- Hay supuestos acoplados a ES/EN?

### No tocar
Archivos de traduccion, middleware, componentes.

---

## TASK-360-06 — Integraciones externas

**Owner sugerido:** Agent Integrations  
**Prioridad:** P0/P1  
**Archivo permitido:** `.docs_md/audit/06-integrations.md`

### Zonas de lectura
- `MyOwnClone/src/app/api/stripe/`
- `api/controllers/console/myownclone/stripe_ctrl.py`
- `api/controllers/console/myownclone/inbox.py`
- `api/core/myownclone/email_processor.py`
- `api/core/myownclone/email_ai.py`
- `MyOwnClone/src/lib/email.ts`
- `MyOwnClone/src/lib/video.ts`
- `.env.example` files

### Objetivo
Auditar Stripe, SendGrid, Resend, Supabase/storage si aplica, Whereby, Anthropic/OpenAI, Sentry/PostHog.

### Preguntas clave
- Stripe sincroniza subscription/plan/cuotas con DB?
- Webhooks validan firma, timestamp e idempotencia?
- SendGrid inbound valida origen/firma y adjuntos?
- Resend tiene plantillas y dominios documentados?
- Whereby maneja ciclo de vida de salas?
- LLM calls tienen fallback, limites y tracking de coste?

### No tocar
Handlers, libs, env examples.

---

## TASK-360-07 — Testing, CI/CD, performance y pre-produccion

**Owner sugerido:** Agent QA/DevOps  
**Prioridad:** P1  
**Archivo permitido:** `.docs_md/audit/07-testing-ci-prod.md`

### Zonas de lectura
- `MyOwnClone/src/__tests__/`
- `MyOwnClone/e2e/`
- `api/tests/`
- `.github/`
- `ops/`
- `Dockerfile`
- `api/Dockerfile`
- `pytest.ini`
- `MyOwnClone/vitest.config.ts`
- `MyOwnClone/playwright.config.ts`

### Objetivo
Auditar cobertura real, calidad de tests, CI/CD, despliegue, observabilidad, performance y checklist prod.

### Preguntas clave
- Que tests existen y que flujos criticos faltan?
- Hay coverage medible o solo tests sueltos?
- CI ejecuta lint, typecheck, tests y build?
- Deploy scripts reflejan el estado actual?
- Hay health checks, logging, monitoring y backups documentados?
- Que performance checks se pueden automatizar?

### No tocar
Tests, workflows, scripts de ops, Dockerfiles.

---

## Orden recomendado

1. `TASK-360-00` crea `.docs_md/audit/00-coordination.md` y la carpeta de auditoria.
2. `TASK-360-01` y `TASK-360-02` arrancan primero porque bloquean seguridad y produccion.
3. `TASK-360-04` corre en paralelo con DB/Auth para verificar endpoints y RAG.
4. `TASK-360-03`, `TASK-360-05` y `TASK-360-06` corren en paralelo despues del primer mapa de endpoints.
5. `TASK-360-07` cierra con validacion de tests, CI y pre-produccion.
6. `TASK-360-00` consolida todo en `99-consolidated-action-plan.md`.

---

## Definition of Done global

- Todos los documentos de auditoria existen.
- Cada P0 tiene evidencia, impacto, recomendacion y owner sugerido.
- Existe una matriz frontend-backend-DB para los flujos criticos:
  - crear fuente de conocimiento
  - chat con clon
  - email inbound
  - reserva de reunion
  - cambio de plan Stripe
  - memoria del creador
  - gap de conocimiento
  - impersonacion admin
  - webhook de invoice
- El plan consolidado separa auditoria de implementacion.
- Ningun agente ha modificado codigo productivo durante la fase de auditoria.
