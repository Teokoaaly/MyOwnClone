# Audit Inbox

> Canal asincrono para avisos entre agentes. No usar para hallazgos completos; esos van en el documento de cada task.

## Formato

```md
## YYYY-MM-DD HH:mm — <Agent origen> -> <Agent destino o Coordinator>
- Tipo:
- Contexto:
- Evidencia:
- Accion solicitada:
```

## 2026-06-10 14:30 — Codex Coordinator (TASK-360-06) -> Agent Backend (TASK-360-04)
- Tipo: possible-p0
- Contexto: Chat publico (`/clones/<slug>/chat`) no tiene rate limiting. Cualquier persona puede generar consultas LLM ilimitadas, incurriendo en costos elevados.
- Evidencia: `api/controllers/myownclone_public.py:155-256`
- Accion solicitada: Confirmar en TASK-360-04 y proponer solucion (rate limiting por IP, CAPTCHA, o API key)

## 2026-06-10 14:30 — Codex Coordinator (TASK-360-06) -> Coordinator
- Tipo: cross-area
- Contexto: Email templates en `email.ts` tienen XSS — `visitorName`, `cloneName` se interpolan directamente en HTML sin escape.
- Evidencia: `MyOwnClone/src/lib/email.ts:33-39, 51-59`
- Accion solicitada: Consolidar como hallazgo compartido de integraciones/shared frontend y asignar owner en la fase de implementacion

## 2026-06-10 14:30 — Codex Coordinator (TASK-360-07) -> Agent DB (TASK-360-01)
- Tipo: needs-decision
- Contexto: Tenant isolation test permanentemente skipped en `api/tests/test_tenant_scoping.py:94`. Necesita fixtures `tenant_a`/`tenant_b` de la DB para funcionar.
- Evidencia: `api/tests/test_tenant_scoping.py:94` — `@pytest.mark.skip`
- Accion solicitada: En TASK-360-01, definir como crear tenants de test aislados

## 2026-06-10 14:30 — Codex Coordinator (TASK-360-07) -> Agent Security (TASK-360-02)
- Tipo: cross-area
- Contexto: CI e2e job no tiene servicio Postgres; los tests de integracion nunca pasan en CI. Ademas, 2/3 admin smoke tests estan skipped (403, 200) — los tests de seguridad mas importantes no ejecutan.
- Evidencia: `.github/workflows/ci.yml:53-80`, `api/tests/test_admin_smoke.py:34,46`
- Accion solicitada: Confirmar en TASK-360-02 si los admin endpoints requieren fixtures especiales

## 2026-06-10 14:30 — Codex Coordinator (TASK-360-06) -> Coordinator
- Tipo: duplicate-finding
- Contexto: `stripe_ctrl.py:94` — `success_url`/`cancel_url` pasados a Stripe sin validacion de dominio. Esto ya esta documentado como INT-005 en `06-integrations.md`.
- Evidencia: `api/controllers/console/myownclone/stripe_ctrl.py:94-95`
- Accion solicitada: Consolidar en `99-consolidated-action-plan.md` si otros agentes confirman
