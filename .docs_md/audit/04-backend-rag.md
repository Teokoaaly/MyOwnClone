# Auditoria — Backend, RAG y Logica de Negocio (TASK-360-04)

## Resumen
- **Estado:** Verde — Backend Flask funcional con blueprints registrados, pipeline RAG operativo, model manager con fallback
- **Riesgo principal:** Faltan algunos endpoints de public chat; silos de conocimiento dependen de configuracion de dataset externo; ingestion.py no verificado en profundidad
- **Veredicto prod:** Funcional para MVP. RAG pipeline usa pgvector correctamente. Model manager tiene fallback entre OpenAI/Anthropic

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| Application factory | ✅ | ~90% | `api/app_factory.py` — blueprints, extensions, seed command |
| Console blueprint (10 modulos) | ✅ | ~85% | 10 modulos: admin, analytics, booking, clone, memories, feedback, inbox, stripe |
| Public blueprint | ✅ | ~70% | `controllers/myownclone_public.py` — chat public, inbound email |
| Auth blueprint | ✅ | Funcional | `controllers/console/auth.py` — login JWT, rate limiting Redis |
| Deploy blueprint | ✅ | Existe | `controllers/deploy.py` |
| RAG pipeline (silo-aware) | ✅ | ~80% | `core/retrieval.py` — pgvector, silo filtering, structured results |
| Model manager (LLM facade) | ✅ | ~85% | `core/model_manager.py` — OpenAI/Anthropic fallback, streaming, cost tracking |
| Ingestion | ⚠️ | No verificado | `core/ingestion.py` — existe pero no se audito en profundidad |
| Email processor | ✅ | Existe | `core/myownclone/email_processor.py` + `email_ai.py` |
| Silo management | ✅ | Existe | `core/myownclone/silos.py` |
| Weaviate remnants | ⚠️ | Parcial | `core/rag/` incluye datasource/retrieval_service.py que referencia Weaviate |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| B04-001 | P1 | Endpoint public chat (/{slug}) no encontrado o incompleto | El chat publico del clon puede no estar operativo | `myownclone_public.py:126` solo tiene GET para obtener config del clon, no POST para chat | Verificar que el endpoint POST chat publico existe y funciona |
| B04-002 | P1 | Weaviate remnants en codigo | El datasource/retrieval_service.py referencia Weaviate, pero el proyecto migro a pgvector | `core/rag/datasource/retrieval_service.py` — depende de weaviate-client en requirements | Limpiar o renombrar para reflejar que ya no se usa Weaviate |
| B04-003 | P1 | Ingestion no auditable en esta ronda | No se pudo verificar manejo de estados processing/ready/error ni timeouts LLM | `core/ingestion.py` — no revisado por limite de alcance | Incluir en proxima ronda de auditoria o asignar tarea especifica |
| B04-004 | P2 | Model manager sin tracking de coste por tenant | Las llamadas LLM no se facturan por tenant individual | `core/model_manager.py` — no hay registro de coste por invocation | Integrar CostTracking para facturacion por uso |
| B04-005 | P2 | Silo resolution depende de dataset externo | `get_dataset_id_for_silo()` puede fallar si el dataset no esta configurado | `core/myownclone/silos.py` — logica de resolucion de dataset | Documentar dependencia o implementar fallback a busqueda sin silo |
| B04-006 | P2 | Sin health check endpoint | No hay forma de verificar que el backend esta operativo desde monitoreo | No existe ruta `/health` o `/ping` en ningun blueprint | Anyadir endpoint `/health` que verifique DB, Redis y LLM keys |
| B04-007 | P3 | Feedback endpoint sin validacion de contenido | Cualquier string se acepta como feedback | `feedback.py:29` — POST sin validacion de payload | Anyadir validacion basica (longitud, caracteres) |
| B04-008 | P3 | Deploy blueprint sin auth robusta | Endpoint de deploy deberia estar protegido con API key fuerte | `controllers/deploy.py` — no se audito, pero usa DEPLOY_SECRET segun middleware | Verificar que DEPLOY_SECRET se valida correctamente |

## Matriz de interconexion

### Endpoints del Backend Flask

| Endpoint | Blueprint | Metodo | Auth | Payload validation | Estado |
|---|---|---|---|---|---|
| /console/api/auth/login | Auth | POST | No | Pydantic | ✅ |
| /console/api/myownclone/admin/overview | Console | GET | login_required | — | ✅ |
| /console/api/myownclone/admin/tenants | Console | GET/POST | login_required | Pydantic (POST) | ✅ |
| /console/api/myownclone/admin/impersonate | Console | POST | login_required | Pydantic | ✅ |
| /console/api/myownclone/clones | Console | GET/POST | login_required | Pydantic (POST) | ✅ |
| /console/api/myownclone/clones/{id} | Console | GET/PUT/DELETE | login_required | Pydantic (PUT) | ✅ |
| /console/api/myownclone/clones/{id}/analytics/* | Console | GET | login_required | — | ✅ |
| /console/api/myownclone/clones/{id}/inbox | Console | GET | login_required | — | ✅ |
| /console/api/myownclone/inbox/{id}/generate-draft | Console | PUT | login_required | — | ✅ |
| /console/api/myownclone/clones/{id}/memories | Console | GET/POST | login_required | Pydantic (POST) | ✅ |
| /console/api/myownclone/clones/{id}/meeting-types | Console | GET/POST | login_required | — | ⚠️ No verificado |
| /console/api/myownclone/clones/{id}/bookings | Console | GET/POST | login_required | — | ⚠️ No verificado |
| /console/api/myownclone/plans | Console | GET | login_required | — | ✅ |
| /console/api/myownclone/stripe/checkout | Console | POST | login_required | — | ⚠️ No verificado |
| /console/api/myownclone/stripe/billing | Console | POST | login_required | — | ⚠️ No verificado |
| /console/api/myownclone/feedback | Console | GET/POST | login_required | — | ⚠️ Sin validacion |
| /inbound-email | Public | POST | Webhook secret | — | ✅ Firma validada |
| /clones/{slug} | Public | GET | No | — | Solo GET, falta POST chat |

### RAG Pipeline Flow

```
Cliente → Next.js middleware → Flask retrieval.py → RetrievalService
                                                       │
                                          ┌────────────┴────────────┐
                                          ▼                        ▼
                                    pgvector search           LLM call
                                    (silo-filtered)      (OpenAI/Anthropic)
                                          │                        │
                                          ▼                        ▼
                                    Chunks + scores          Response text
                                          │                        │
                                          └────────┬───────────────┘
                                                   ▼
                                            SiloRetrievalResult
                                                   │
                                                   ▼
                                            Confidence scoring
                                                   │
                                              Gap detection?
```

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| B04-A | P1 | Verificar endpoint POST chat public y anyadirlo si falta | Agent Backend | 0.5d | — |
| B04-B | P1 | Limpiar/renombrar Weaviate remnants en core/rag/ | Agent Backend | 0.5d | — |
| B04-C | P1 | Auditar ingestion.py (estados, timeouts, errores) | Agent Backend | 1d | — |
| B04-D | P2 | Integrar cost tracking por tenant en model_manager | Agent Backend | 1d | — |
| B04-E | P2 | Documentar dependencia de dataset externo en silos | Agent Backend | 0.3d | — |
| B04-F | P2 | Anyadir endpoint /health con checks DB, Redis, LLM | Agent Backend | 0.5d | — |
| B04-G | P3 | Anyadir validacion de payload en POST feedback | Agent Backend | 0.3d | — |

## Open Questions

1. **Public chat endpoint**: Existe un endpoint POST para chat publico en `myownclone_public.py`? La ruta GET /clones/{slug} esta, pero no se encontro POST.
2. **Weaviate**: Se mantiene el codigo de Weaviate como referencia o se elimina definitivamente? Si ya no se usa, pesa en el codigo base.
3. **Ingestion.py**: No se audito por limite de alcance. Tiene manejo de estados `processing`/`ready`/`error`? Timeouts en llamadas LLM?
