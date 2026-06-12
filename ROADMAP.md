# ROADMAP.md

Objetivo: llevar MyOwnClone del estado actual a 100% operativo en 7 semanas.

## Criterios de 100% operativo

- Funcionalidad core completa: auth, tenant, clones, chat RAG, fuentes, inbox, reuniones, billing, admin y widget.
- Estabilidad: 0 bugs criticos, menos de 5 bugs menores abiertos.
- Tests: unit/contract/E2E pasando, coverage minimo 80% en modulos core.
- Seguridad: 0 vulnerabilidades criticas/altas, secretos fuertes, dev fallbacks desactivados en prod.
- Performance: landing/dashboard <2s LCP en target, API p95 <200ms para endpoints no IA, chat/RAG p95 medido.
- Documentacion: setup, deploy, arquitectura, contributing y runbooks actualizados.
- CI/CD: pipeline reproducible con migraciones, tests, build, E2E y artefactos.
- Monitoreo: logs estructurados, Sentry/PostHog, health/readiness y alertas.

## Milestone 1: Fundamentos (Semana 1)

Objetivo: cerrar bloqueantes de produccion y CI.

Tareas:

- T1.1: Corregir vulnerabilidades `npm audit`. COMPLETADO.
  - Upgrade controlado de `drizzle-orm`.
  - Resolver PostCSS/Next con upgrade u override compatible.
  - Criterio: `npm audit --omit=dev` sin vulnerabilidades altas.
- T1.2: Normalizar driver PostgreSQL. COMPLETADO.
  - Decidir `psycopg2` vs `psycopg`.
  - Alinear `requirements`, `DATABASE_URL`, `app_factory.py`, CI y docs.
  - Criterio: `flask db upgrade` pasa en CI y local.
- T1.3: Corregir pgvector en produccion. COMPLETADO.
  - Cambiar compose prod a imagen con pgvector.
  - Agregar verificacion `CREATE EXTENSION IF NOT EXISTS vector`.
  - Criterio: migraciones limpias contra DB nueva.
- T1.4: Matriz de envs. PARCIAL.
  - Definir variables obligatorias por dev/staging/prod.
  - Criterio: `.env.example` y `ops/*.example` no se contradicen.

Responsable: DevOps + Backend.

Milestone 1 queda cerrado a nivel local: `flask db upgrade` fue validado sobre una DB limpia temporal con pgvector y la DB local existente fue respaldada, estampada en `c3d4e5f6a7c1`, y verificada con `flask db upgrade`.

## Milestone 2: Funcionalidad core validada (Semana 2-3)

Objetivo: probar flujos reales con datos y servicios sandbox.

Tareas:

- T2.1: Validar onboarding completo: registro, verificacion, creacion tenant/clone.
- T2.2: Validar biblioteca: upload/text/web source, chunking, embeddings y retrieval.
- T2.3: Validar chat publico y dashboard con persistencia.
- T2.4: Validar inbox: SendGrid inbound, clasificacion, draft y respuesta.
- T2.5: Validar reuniones: disponibilidad, booking, Whereby y email de confirmacion.
- T2.6: Validar billing: checkout, portal, webhook y cambio de plan en Stripe sandbox.

Responsable: Backend + Frontend + QA.

## Milestone 3: Calidad y testing (Semana 4)

Objetivo: convertir el estado verificado en red de seguridad permanente.

Tareas:

- T3.1: Coverage frontend/backend con umbral minimo 80% en core.
- T3.2: Playwright E2E para auth, billing, fuentes, chat, reuniones y admin. PARCIAL: suite pasa con 35 tests y 2 skips por falta de sesion/clones seedeados.
- T3.3: Tests de tenant scoping y permisos admin.
- T3.4: Tests de migraciones desde DB vacia y desde snapshot anterior.
- T3.5: Eliminar warnings de lint y warnings React relevantes. COMPLETADO.

Responsable: QA + Frontend + Backend.

## Milestone 4: Seguridad y performance (Semana 5)

Objetivo: endurecer superficie publica.

Tareas:

- T4.1: Threat model corto por superficie: public chat, widget, auth, admin, webhooks.
- T4.2: Rate limiting centralizado con Redis/Upstash y pruebas negativas.
- T4.3: Headers de seguridad, CSP y limites de payload.
- T4.4: Sanitizacion y validacion de inputs en endpoints publicos/admin.
- T4.5: Benchmarks p95: endpoints API, dashboard y RAG.
- T4.6: Indices DB para consultas frecuentes.

Responsable: Security + Backend + Frontend.

## Milestone 5: Observabilidad y operaciones (Semana 6)

Objetivo: operar el sistema sin volar a ciegas.

Tareas:

- T5.1: `/healthz` y `/readyz`. COMPLETADO base; pendiente version/migration readiness.
- T5.2: Logs estructurados con request ID, tenant ID y clone ID cuando aplique.
- T5.3: Sentry para frontend/backend.
- T5.4: PostHog/product analytics con eventos core.
- T5.5: Runbooks: rollback, rotacion secretos, webhook failures, migracion DB.

Responsable: DevOps + Backend.

## Milestone 6: Documentacion y release candidate (Semana 7)

Objetivo: dejar el proyecto listo para handoff y despliegue.

Tareas:

- T6.1: Revisar `SETUP.md`, `DEPLOYMENT.md`, `ARCHITECTURE.md`.
- T6.2: Ensayo de despliegue staging desde cero.
- T6.3: Smoke test post-deploy automatizado.
- T6.4: Checklist final de seguridad y producto.
- T6.5: Release candidate con changelog.

Responsable: Tech Lead + todos los agentes.
