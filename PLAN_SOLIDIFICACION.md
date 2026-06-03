# PLAN DE SOLIDIFICACIÓN — Réplica sobre Dify

**Fecha:** 2026-05-27
**Objetivo:** Transformar el scaffolding acelerado (52 archivos, 0 tests) en un sistema funcional para producción.

---

## FASE A: CORRECCIÓN DE BUGS CRÍTICOS (rompen en runtime)

### A.1 — `clone.py:109-115`: CloneModePrompt nunca se persiste

**Archivo:** `dify/api/controllers/console/myownclone/clone.py`
**Bug:** Las instancias `CloneModePrompt(...)` se crean pero nunca se llaman con `db.session.add()`. Los prompts de modo se pierden silenciosamente al crear un clon.
**Fix:** Añadir `db.session.add(prompt_obj)` dentro del loop.

```python
# Línea 109-115, cambiar:
for silo in CloneSilo:
    CloneModePrompt(
        clone_id=clone.id,
        ...
    )
# Por:
for silo in CloneSilo:
    prompt = CloneModePrompt(
        clone_id=clone.id,
        mode=silo.value,
        system_prompt=DEFAULT_PROMPTS.get(silo, ""),
        is_active=silo in (data.active_modes or []),
    )
    db.session.add(prompt)
```

### A.2 — `email_ai.py`: `_get_clone_context` importado de módulo equivocado

**Archivo:** `dify/api/controllers/myownclone_public.py:251`
**Bug:** `from core.myownclone.email_ai import _get_clone_context as get_ctx` — pero `_get_clone_context` está definido en `controllers/console/myownclone/inbox.py:236`, no en `email_ai.py`. Esto produce `ImportError` en runtime.
**Fix:** Mover `_get_clone_context` a `core/myownclone/email_ai.py` (donde pertenece lógicamente) o corregir el import.

### A.3 — `email_processor.py:126`: `CloneConfig.custom_domain` no existe

**Archivos:** `dify/api/core/myownclone/email_processor.py:126` + `dify/api/migrations/versions/2026_05_26_1648-*.py:86`
**Bug:** La migración añade `custom_domain` a la tabla `tenants`, pero `resolve_clone_by_domain()` consulta `CloneConfig.custom_domain`. El modelo `CloneConfig` no tiene ese campo → `AttributeError`.
**Fix (opción recomendada):** Añadir `custom_domain` al modelo `CloneConfig` (tabla `clone_configs`) y crear migración que lo añada. La resolución por dominio es más natural a nivel de clon que de tenant. Alternativa: resolver via `Tenant.custom_domain` y luego buscar clone por `tenant_id`.

### A.4 — `booking.py`: Sin verificación de tenant

**Archivo:** `dify/api/controllers/console/myownclone/booking.py`
**Bug:** Todos los endpoints (GET/POST meeting-types, availability, products) operan solo con `clone_id` sin verificar que el usuario autenticado pertenezca al tenant dueño del clon. Cualquier usuario puede leer/escribir datos de cualquier clon.
**Fix:** Añadir verificación de tenant en cada endpoint, igual que en `clone.py` y `creator_memory.py`:
```python
account, tenant_id = current_account_with_tenant()
_verify_clone_access(clone_id, tenant_id)  # helper ya existe en creator_memory.py
```

### A.5 — `admin_platform.py:157-163`: `_is_platform_admin()` incorrecto

**Archivo:** `dify/api/controllers/console/myownclone/admin_platform.py`
**Bug:** La función comprueba `TenantAccountJoin.role == TenantAccountRole.ADMIN` sin filtrar por tenant — cualquier admin de cualquier tenant pasa como platform admin.
**Fix:** Añadir campo `is_platform_admin` al modelo `Account` (ya existe la migración en `accounts.role`). Usar un rol específico o un flag booleano dedicado. Mientras tanto, hardcodear una lista de account_ids de confianza o añadir `is_platform_admin` al modelo.

---

## FASE B: BUGS DE INTEGRIDAD Y RENDIMIENTO

### B.1 — Eliminar duplicación `CloneSilo`

**Archivos:** `dify/api/core/myownclone/silos.py:26` y `dify/api/models/myownclone/clone.py:15`
**Fix:** Eliminar la definición en `core/myownclone/silos.py`. Importar desde `models.myownclone`:
```python
from models.myownclone.clone import CloneSilo
```
Actualizar `core/myownclone/__init__.py` para re-exportar desde models.

### B.2 — Eliminar duplicación `ClassificationResult` / `DraftResult`

**Archivos:** `dify/api/core/myownclone/email_processor.py:39-50` y `dify/api/core/myownclone/email_ai.py:15-27`
**Fix:** Eliminar las definiciones duplicadas en `email_processor.py`. Mantener solo las de `email_ai.py`. Actualizar imports.

### B.3 — N+1 en `filter_segments_by_context()`

**Archivo:** `dify/api/core/myownclone/silos.py:61-82`
**Bug:** Itera segment_ids con una query individual por cada segmento. Con 5 resultados y 100 peticiones/segundo, esto genera 500 queries/segundo innecesarias.
**Fix:** Query única con `IN`:
```python
def filter_segments_by_context(session, segment_ids, context_id, tenant_id):
    if not segment_ids:
        return []
    stmt = (
        select(DocumentSegment.id)
        .where(
            DocumentSegment.id.in_(segment_ids),
            DocumentSegment.tenant_id == tenant_id,
            DocumentSegment.doc_metadata["context_id"].astext == context_id,
        )
    )
    rows = session.execute(stmt).fetchall()
    return [row[0] for row in rows]
```
Nota: el path JSON `doc_metadata['context_id']` requiere PostgreSQL >= 12 con operador `->>`.

### B.4 — Analytics sin tenant scoping

**Archivo:** `dify/api/controllers/console/myownclone/analytics.py:84-145`
**Bug:** `TopQuestionsApi` y `AnalyticsGapsApi` consultan solo por `clone_id`, sin verificar tenant ownership.
**Fix:** Añadir `_verify_clone_access(clone_id, tenant_id)` en cada endpoint.

### B.5 — Stripe usa `os.getenv` en vez del sistema de config

**Archivos:** `dify/api/controllers/console/myownclone/stripe_ctrl.py:24` y `dify/api/controllers/stripe_webhook.py:15-16`
**Fix:** Usar `configs.dify_config` (Dify ya tiene `STRIPE_SECRET_KEY` y `STRIPE_WEBHOOK_SECRET` en su config).

### B.6 — Replica `billing/route.ts` no reenvía cookies

**Archivo:** `replica/src/app/api/clone/billing/route.ts:18`
**Bug:** `cookieHeader` está hardcodeado a `""`. Las peticiones al backend Dify se hacen sin cookies de sesión.
**Fix:** Leer cookies del request entrante.
```typescript
const cookieHeader = request.headers.get('cookie') || ''
```

---

## FASE C: CIERRE DE GAPS FUNCIONALES

### C.1 — Páginas dashboard estáticas → funcionales

**Archivos afectados (3):**

| Página | Estado actual | Trabajo necesario |
|--------|---------------|-------------------|
| `configuracion/page.tsx` | Form vacío, sin backend | Conectar a `PUT /myownclone/clones/{id}/prompts` y campos del clon |
| `reuniones/page.tsx` | Empty state sin acciones | Conectar a `GET/POST /myownclone/clones/{id}/meeting-types` y `availability` |
| `productos/page.tsx` | Empty state sin acciones | Conectar a `GET/POST /myownclone/clones/{id}/products` |

**`biblioteca/page.tsx`**: `getSources()` está definida pero nunca llamada. Conectar al endpoint de fuentes.
**`resumen/page.tsx`**: Stats hardcodeados a 0/`--`. Conectar a `analytics/overview`.

### C.2 — Chat SSE: devolver confidence y sources

**Archivos:** `replica/src/app/api/clone/[slug]/chat/route.ts` + `dify/api/controllers/myownclone_public.py:186-208`
**Estado actual:** El backend Dify ya emite `{'done': True, 'context_found': ..., 'silo': ...}` en el último chunk (línea 201), pero no incluye `confidence_score` ni `sources`.
**Fix:** Añadir confidence_score y sources al evento final:
```python
yield f"data: {json.dumps({'content': '', 'done': True, 'confidence': result.scores[0] if result.scores else 0, 'sources': [{'content': c[:200], 'score': s} for c, s in zip(result.contents, result.scores)], 'context_found': result.found, 'silo': silo.value})}\n\n"
```
Del lado Next.js, parsear el evento final en `ChatPanel.tsx` y popular `confidence` y `sources` en `ChatMessage`.

### C.3 — Impersonation: implementar cambio real de sesión

**Archivo:** `dify/api/controllers/console/myownclone/admin_platform.py:128-154`
**Estado actual:** Solo escribe un log. No hay mecanismo para que el admin "se convierta" en el tenant.
**Fix:** Añadir endpoint `POST /myownclone/admin/impersonate/start` que devuelva un token JWT firmado con claims `{sub: admin_id, imp_tenant: tenant_id, exp: now+30min}`. El middleware debe reconocer el claim `imp_tenant` y usarlo como `tenant_id` efectivo. Añadir endpoint `POST /impersonate/stop` para salir.

### C.4 — Booking: detección de conflictos de horario

**Archivo:** `dify/api/controllers/console/myownclone/booking.py` — endpoint POST (no existe aún para bookings)
**Fix:** Antes de crear un `Booking`, verificar que no haya solapamiento con bookings existentes para el mismo `meeting_type_id` en la misma fecha y franja horaria.

### C.5 — Endpoint inbound-email funcional en replica

**Archivo:** `replica/src/app/api/inbound-email/route.ts` — actualmente es un stub que solo devuelve `{received: true}`.
**Fix:** Implementar procesamiento real:
- Parsear multipart/form-data de SendGrid
- Reenviar al backend Dify (`POST /api/myownclone/public/inbound-email`)
- O implementar localmente usando `lib/email.ts`

### C.6 — Webhook Stripe en replica: completar stubs

**Archivo:** `replica/src/app/api/stripe/webhook/route.ts`
**Bug:** `subscription.updated` y `subscription.deleted` son stubs vacíos.
**Fix:** Implementar actualización de tenant status para esos eventos, igual que en el backend Python.

### C.7 — Registrar `custom_domain` correctamente

**Migración necesaria:** Añadir `custom_domain VARCHAR(255)` a la tabla `clone_configs` (y al modelo `CloneConfig`). Actualmente solo existe en `tenants`.
**Fix:** Nueva migración + actualizar modelo `clone.py`.

---

## FASE D: UNIFICACIÓN ARQUITECTÓNICA

### D.1 — Eliminar RAG pipeline duplicado en replica

**Situación:** Existen DOS pipelines RAG paralelos:
1. `replica/src/lib/rag/pipeline.ts` → usa Drizzle + Claude, habla directo a PostgreSQL
2. `dify/api/core/myownclone/retrieval.py` → usa SQLAlchemy + RetrievalService de Dify

**Decisión:** Mantener solo el backend Dify (`retrieval.py`). El `lib/rag/pipeline.ts` es código muerto que diverge del plan maestro (el plan dice claramente "extender Dify, no reescribir"). El SSE proxy (`ChatPanel → /api/clone/[slug]/chat → Dify backend`) ya funciona correctamente.
**Acción:** Eliminar `replica/src/lib/rag/` o marcarlo como `@deprecated`. El único punto de RAG debe ser `dify/api/core/myownclone/retrieval.py`.

### D.2 — Unificar implementaciones Stripe

**Situación:** Existen DOS implementaciones Stripe:
1. `replica/src/app/api/stripe/route.ts` (+ webhook) → usa Stripe SDK desde Next.js, habla directo a Drizzle DB
2. `dify/api/controllers/console/myownclone/stripe_ctrl.py` (+ `stripe_webhook.py`) → usa Stripe SDK desde Python, habla a SQLAlchemy DB

**Decisión:** Consolidar en el backend Python (Dify). Eliminar las rutas Stripe del frontend Next.js (`/api/stripe/` y `/api/stripe/webhook/`) y usar solo las proxied (`/api/clone/stripe/checkout`, `/api/clone/billing`). El webhook se registra en `dify/api/app_factory.py:224`.
**Acción:** 
- Verificar que `stripe_webhook.py` funcione correctamente
- Eliminar `replica/src/app/api/stripe/route.ts` y `replica/src/app/api/stripe/webhook/route.ts`
- Actualizar `facturacion/page.tsx` para que use solo los endpoints proxy

### D.3 — Integrar retrieval con `DatasetRetrieval` de Dify (no solo `RetrievalService`)

**Estado actual:** `retrieve_from_silo()` llama a `RetrievalService.retrieve()` directamente, saltándose `DatasetRetrieval` que es la capa de orquestación de Dify (maneja metadata filtering, multi-dataset, re-ranking).
**Fix (futuro):** Construir un `KnowledgeRetrievalRequest` y pasar por `DatasetRetrieval.knowledge_retrieval()`. Esto da acceso a filtrado por metadata nativo de Dify (en vez del post-filtro manual de `filter_segments_by_context`). **Prioridad media — el enfoque actual funciona para MVP.**

---

## FASE E: TESTS

### E.1 — Tests unitarios Python (dify/api/tests/myownclone/)

**Estructura objetivo:**
```
tests/unit_tests/myownclone/
├── __init__.py
├── conftest.py                          # Fixtures: app, db_session, test_tenant, test_clone
├── test_models.py                       # Creación de CloneConfig, CreatorMemory, EmailInbound
├── test_silos.py                        # dataset_name_for_silo, filter_segments_by_context
├── test_retrieval.py                    # retrieve_from_silo (mock RetrievalService)
├── test_email_processor.py              # parse_inbound_email (con email de prueba)
├── test_email_ai.py                     # classify_email, generate_draft (mock LLM callable)
├── test_controllers/
│   ├── __init__.py
│   ├── test_clone.py                    # CRUD clone + mode prompts
│   ├── test_creator_memory.py           # CRUD memories
│   ├── test_inbox.py                    # List, detail, draft generation
│   ├── test_booking.py                  # CRUD + tenant verification
│   ├── test_analytics.py                # Tenant-scoped queries
│   └── test_admin_platform.py           # Admin auth + impersonation
```

**Patrón a seguir:** `tests/unit_tests/controllers/web/test_completion.py` (usa `app.test_request_context`, `@patch`, `MagicMock`, fixtures en `conftest.py`).

**Cobertura mínima objetivo:**
- Modelos: creación y validación (80%)
- Core/myownclone: lógica de silos, retrieval, email (90%)
- Controllers: todos los endpoints CRUD (90%)
- Verificaciones de tenant en todos los controllers (100%)

### E.2 — Tests de integración (opcional, Fase E.2)

- `test_chat_flow.py`: End-to-end: crear clon → ingestar documento → chat con silo → verificar respuesta
- `test_inbox_flow.py`: Recibir email → clasificar → generar draft → revisar → enviar
- `test_stripe_flow.py`: Checkout → webhook → actualización de tenant

### E.3 — Tests frontend (replica)

**Estructura:**
```
replica/src/__tests__/
├── components/
│   ├── ChatPanel.test.tsx              # Renderizado, envío, streaming, estados
│   ├── SiloToggle.test.tsx             # Cambio de silo
│   └── MessageBubble.test.tsx          # Markdown, confidence bar
└── pages/
    ├── dashboard-resumen.test.tsx       # Carga de stats
    └── inbox.test.tsx                  # CRUD de emails
```

**Framework:** Vitest + React Testing Library (añadir a `package.json`).

---

## FASE F: INTEGRACIÓN END-TO-END

### F.1 — Verificación de conectividad replica ↔ Dify

| Componente | Replica endpoint | Dify backend endpoint | Estado |
|-----------|-----------------|----------------------|--------|
| Chat SSE | `/api/clone/[slug]/chat` | `/api/myownclone/public/clones/{slug}/chat` | Implementado, necesita confidence/sources |
| Clone info | Página `[slug]` → fetch | `/api/myownclone/public/clones/{slug}` | Implementado |
| Dashboard CRUD | `/api/clone/[...path]` | `/console/api/myownclone/*` | Implementado (proxy genérico) |
| Inbox | `/api/clone/inbox/*` | `/console/api/myownclone/inbox/*` | Implementado |
| Analytics | `/api/clone/analytics/*` | Dentro de `[...path]` proxy | Implementado |
| Stripe checkout | `/api/clone/stripe/checkout` | `/console/api/myownclone/stripe/checkout` | Implementado |
| Plans | `/api/clone/plans` | `/console/api/myownclone/plans` | Implementado |
| Billing | `/api/clone/billing` | `/console/api/myownclone/stripe/billing` | Bug: cookies no enviados |
| Inbound email | `/api/inbound-email` | `/api/myownclone/public/inbound-email` | Stub → necesita implementación |
| Admin | `/api/admin/[...path]` | `/console/api/myownclone/admin/*` | Implementado |

### F.2 — Prueba de humo manual

1. Levantar Dify backend: `cd dify && docker compose -f docker/docker-compose.yaml up -d`
2. Ejecutar migraciones: `cd api && flask db upgrade`
3. Levantar replica: `cd replica && pnpm dev`
4. Crear tenant + clon desde el onboarding
5. Verificar chat público en `[slug].localhost:3000`
6. Verificar dashboard en `localhost:3000/dashboard`

---

## ORDEN DE EJECUCIÓN RECOMENDADO

| # | Fase | Tiempo estimado | Dependencias |
|---|------|----------------|-------------|
| 1 | A.1 — Fix CloneModePrompt | 5 min | Ninguna |
| 2 | A.2 — Fix `_get_clone_context` import | 10 min | Ninguna |
| 3 | A.3 — Fix custom_domain | 15 min | Ninguna |
| 4 | A.4 — Fix booking tenant verification | 15 min | Ninguna |
| 5 | A.5 — Fix `_is_platform_admin` | 10 min | Ninguna |
| 6 | B.1 — Eliminar duplicación CloneSilo | 10 min | A.1 |
| 7 | B.2 — Eliminar duplicación dataclasses | 5 min | A.2 |
| 8 | B.3 — Fix N+1 context filter | 15 min | Ninguna |
| 9 | B.4 — Fix analytics tenant scoping | 10 min | Ninguna |
| 10 | B.5 — Fix Stripe config | 5 min | Ninguna |
| 11 | B.6 — Fix billing cookie | 5 min | Ninguna |
| 12 | C.1 — Dashboard pages funcionales | 2h | Fase A+B |
| 13 | C.2 — Chat confidence/sources | 30 min | Ninguna |
| 14 | C.3 — Impersonation real | 1h | A.5 |
| 15 | C.4 — Booking conflict detection | 30 min | A.4 |
| 16 | C.5 — Inbound email funcional | 30 min | A.2, A.3 |
| 17 | C.6 — Stripe webhook stubs | 20 min | B.5 |
| 18 | C.7 — custom_domain migration | 10 min | A.3 |
| 19 | D.1 — Eliminar RAG duplicado | 5 min | Ninguna |
| 20 | D.2 — Unificar Stripe | 30 min | C.6 |
| 21 | E.1 — Tests unitarios Python | 4h | Fase A+B |
| 22 | E.3 — Tests frontend | 2h | Fase C |
| 23 | F.1 — Verificación conectividad | 1h | Todo lo anterior |
| **TOTAL** | | **~14h** | |

---

## MÉTRICAS DE SALIDA

Al completar este plan, el proyecto debe cumplir:

- [ ] 0 bugs críticos (runtime errors)
- [ ] 0 bugs de seguridad (tenant isolation verificada en todos los controllers)
- [ ] 100% de páginas dashboard funcionales (no shells)
- [ ] 1 solo pipeline RAG (backend Dify)
- [ ] 1 sola implementación Stripe (backend Dify)
- [ ] Tests unitarios con >80% cobertura en módulos `core/myownclone/`
- [ ] Tests unitarios con >90% cobertura en controllers Clonify
- [ ] Chat SSE devuelve confidence_score y sources
- [ ] Inbound email pipeline end-to-end funcional
- [ ] Impersonation funcional (login real como otro tenant)
