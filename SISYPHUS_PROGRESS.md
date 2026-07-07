# Rebase Sisyphus → VPS — Progress Log

> Rama: `rebase/sisyphus-vps`  
> Base: `deploy/maint-mode-plus-wip` (24e966a)  
> Inicio: 2026-07-07  
> Estado: ✅ Código completo, build en prueba

---

## Commits

| SHA | Contenido |
|-----|-----------|
| `7a0f983` | Plan pricing alignment |
| `18d6c01` | Backend fixes: trial_ends_at, tenant detail, Redis TLS |
| `dfa2401` | 11 módulos Sisyphus + migración + 4 modelos |

## Archivos añadidos (17 nuevos)

### Módulos core (11)
- cost_recording.py, feedback_collector.py, ingestion_pipeline.py
- metrics_collector.py, moderation.py, reranking.py
- security_types.py, smart_router.py, rate_limit.py
- retrieval.py, admin_ia_models.py

### Modelos SQLAlchemy (4)
- embedding_outbox.py, response_feedback.py
- routing_log.py, moderation_log.py

### Migración (1)
- 2026_07_07_sisyphus_m10_m20.py
  - 4 tablas: embedding_outbox, response_feedback, routing_log, moderation_log
  - 2 columnas: ai_invocations.cost_cents, ai_invocations.response_hash

### Fixes import (2)
- feedback_collector.py: ai_invocation → ai_models
- smart_router.py: RoutingDecision desde routing_log.py

## Preservado del VPS (NO tocado)
- model_manager.py: 567 líneas (VPS > Sisyphus 571)
- model_registry.py: 376 líneas (VPS > Sisyphus 214)
- providers/: 10 adapters (VPS > Sisyphus 5)
- embeddings.py, stt.py: intactos

## Pendiente
- [ ] Build Docker exitoso
- [ ] Test smoke: /healthz, /readyz
- [ ] Test /admin/ia-modelos endpoints
- [ ] Deploy controlado con rollback
