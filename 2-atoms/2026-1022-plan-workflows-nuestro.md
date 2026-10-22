---
id: 2026-1022-plan-workflows-nuestro
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-workflows-beta-dominio]]", "[[2026-1022-plan-lead-capture-visitors]]", "[[2026-1022-arquitectura-rac-tres-modos-por-clon]]"]
---
## Claim
El paso 3 del handoff (prioridad 🟡 MEDIA, esfuerzo **alto**) propone replicar en [[myownclone]] el módulo Workflows de MyClone.is con **cuatro tablas**: `workflow_templates` (predefinidos por industria, con `template_key`, `workflow_type`, `minimum_plan_tier_id` y `workflow_config JSONB`), `persona_workflows` (workflow activo por clon, con `is_customized`, `published_at`, `synced_version`), `workflow_sessions` (con `visitor_id`, `status` active/completed/abandoned, `current_step`) y `workflow_answers` (respuesta por paso). La estructura de config replica la de MyClone: `objectives` (pasos `type: question` encadenados por `next_step_on_answer`, con un `type: advice` final) y un `output_template` de tipo `lead_summary` con secciones `profile`, `situation`, `need`, `score`, `follow_up_questions`.

## Why It Matters
El `output_template` con `score` y `follow_up_questions` revela el objetivo real de los workflows de MyClone: son un **cuestionario de cualificación que produce un lead scored**, no un simple guion conversacional. Eso es coherente con la monetización por persona vía Stripe Connect ([[2026-1022-myclone-stripe-connect-monetizacion]]): el workflow identifica al lead scored y el pago cierra.
El handoff lo coloca **último** en la roadmap ("solo si hay demanda de usuarios"), lo que es coherente con la lección del vault sobre no sobreconstruir ([[2026-1022-error-fase-3-sobreconstruir]]) y con el hecho de que [[2026-1022-arquitectura-rac-tres-modos-por-clon]] ya cubre el caso de uso de rol variable con tres modos, más barato.
Es el gap más caro de replicar (alto esfuerzo, cuatro tablas, sesiones con estado), y el que más sentido comercial tiene. `tentative`: es diseño, no código existente.
