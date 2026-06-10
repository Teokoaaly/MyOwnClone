# Auditoria — Testing, CI/CD, performance y pre-produccion (TASK-360-07)

## Resumen
- **Estado:** Amarillo — CI pipeline configurado con 3 jobs; 71 vitest + ~15 pytest + 10 E2E; gaps criticos en CI e2e job (sin Postgres), lint no bloqueante, y cobertura muy delgada
- **Riesgo principal:** E2E job roto en CI (falta servicio Postgres); tenant isolation no testeado; deploy sin rollback
- **Veredicto prod:** CI funciona para frontend unit tests. Backend y E2E requieren fixes antes de confiar en el pipeline

## Mapa de estado actual

| Componente | Existe | Completo | Evidencia |
|---|---|---|---|
| Vitest unit tests | ✅ | ~60% | 10 archivos, 71 tests, todos pasan |
| Pytest backend tests | ✅ | ~40% | 3 archivos en `api/tests/`, tests skipped |
| Playwright E2E | ✅ | ~30% | 2 archivos, 10 tests (solo structural) |
| CI pipeline | ✅ | ~65% | 3 jobs: backend, frontend, e2e |
| Deploy scripts | ✅ | ~70% | `ops/deploy-*.sh` con health checks |
| Docker | ✅ | ~75% | `api/Dockerfile` (prod), root `Dockerfile` (dev) |
| Smoke tests | ✅ | ~50% | `ops/smoke-prod.sh` — 5 HTTP checks |
| Coverage | ❌ | ~0% | Sin thresholds, sin upload, output truncado |

## Hallazgos priorizados

| ID | Prioridad | Hallazgo | Impacto | Evidencia | Recomendacion |
|---|---|---|---|---|---|
| TEST-001 | P0 | E2E job en CI roto — falta servicio Postgres | Playwright tests nunca pasan en CI; se da falsa sensacion de seguridad | `.github/workflows/ci.yml:53-80` — job `e2e` no tiene bloque `services: postgres:` | Anadir `services: postgres:` igual que en job `backend` |
| TEST-002 | P0 | Tenant isolation sin test automatizado | No hay garantia de que tenant A no vea datos de tenant B | `api/tests/test_tenant_scoping.py:94` — `test_endpoint_scopes_by_tenant` permanently skipped | Crear fixture `tenant_a`/`tenant_b` y des-skip el test |
| TEST-003 | P1 | Lint no bloqueante en CI | Errores de linting nunca fallan CI | `.github/workflows/ci.yml:28` — `ruff check . --select=E,F,W --exit-zero` | Cambiar a `--exit-non-zero-on-fix` o eliminar `--exit-zero` |
| TEST-004 | P1 | pytest testpaths desalineado con api/tests/ | Running `pytest` from root no descubre tests de `api/tests/` | `pytest.ini:3` — `testpaths = tests` apunta a `tests/` root, no `api/tests/` | Crear `api/pytest.ini` con `testpaths = tests` o mover tests |
| TEST-005 | P1 | requirements-dev.txt no se usa en CI | Dependencias de dev declaradas pero CI instala manualmente | `ci.yml:26` — `pip install ruff pytest` en vez de `pip install -r requirements-dev.txt` | Usar `pip install -r requirements-dev.txt` en CI |
| TEST-006 | P1 | Coverage output truncado y sin upload | No hay visibilidad real de cobertura | `ci.yml:51` — `2>&1 | tail -20` trunca reporte; sin Codecov/Coveralls | Quitar `tail -20`; considerar upload a Codecov |
| TEST-007 | P2 | E2E tests solo verifican estructura | 10 tests solo confirman que paginas cargan, no flujos funcionales | `e2e/auth.spec.ts` — solo verifica elementos de form; `e2e/navigation.spec.ts` — "body is visible" | Anadir tests de login real, creacion de clone, envio de chat |
| TEST-008 | P2 | 2/3 admin smoke tests永久 skipped | Tests de seguridad (403, 200) nunca ejecutan | `api/tests/test_admin_smoke.py:34,46` — `@pytest.mark.skip` | Crear fixture JWT valido para admin y des-skip |
| TEST-009 | P2 | Sin rollback en deploy scripts | Si health check falla, symlink ya apunta al release roto | `ops/deploy-backend.sh` — symlink actualizado antes del health check | Implementar rollback: solo actualizar symlink despues de health check exitoso |
| TEST-010 | P2 | Root Dockerfile inseguro | Corre como root, usa Flask dev server, sin healthcheck | `Dockerfile:1-16` — `CMD ["flask", "run"]`, sin USER | Eliminar root Dockerfile; usar solo `api/Dockerfile` |
| TEST-011 | P2 | Sin coverage thresholds | No hay minimo de cobertura que falle CI | `vitest.config.ts` — sin bloque `coverage` | Anadir `coverage.lines: 50` como minimo inicial |
| TEST-012 | P3 | requirements.txt duplicado con stripe repetido | Archivos root y api/ casi identicos pero divergentes | Root `requirements.txt` tiene `stripe` duplicado (lineas 13-14) | Consolidar en un solo archivo; eliminar duplicados |
| TEST-013 | P3 | Playwright solo Chromium | Sin cobertura Firefox/WebKit | `playwright.config.ts` — solo proyecto `chromium` | Aceptar para MVP; documentar como limitacion conocida |

## Matriz de interconexion

### Flujo: CI pipeline

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| CI | Backend job | `ci.yml:8-37` | ✅ Funcional | Lint no bloqueante (`--exit-zero`) |
| CI | Frontend job | `ci.yml:39-51` | ✅ Funcional | Coverage truncado |
| CI | E2E job | `ci.yml:53-80` | ❌ Roto | Sin servicio Postgres; `flask db upgrade` fallara |
| Config | pytest.ini | `pytest.ini` | ⚠️ Desalineado | `testpaths = tests` no apunta a `api/tests/` |
| Config | vitest.config.ts | `vitest.config.ts` | ✅ Funcional | Sin coverage thresholds |
| Config | playwright.config.ts | `playwright.config.ts` | ✅ Funcional | Solo Chromium |

### Flujo: Testing

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Frontend unit | Vitest | `src/__tests__/` (10 files) | ✅ 71/71 pass | Sin tests de dashboard, hooks, middleware |
| Backend unit | Pytest | `tests/test_smoke.py` | ✅ 15 pass | Solo smoke tests |
| Backend API | Pytest | `api/tests/` (3 files) | ⚠️ ~15 tests, many skipped | Tenant isolation skipped; admin auth skipped |
| E2E | Playwright | `e2e/` (2 files) | ⚠️ 10 tests | Solo structural; sin flujos autenticados |
| Production | smoke-prod.sh | `ops/smoke-prod.sh` | ✅ 5 checks | Solo HTTP checks; sin auth flows |

### Flujo: Deploy

| Capa | Componente | Archivo | Estado | Gaps |
|---|---|---|---|---|
| Backend deploy | deploy-backend.sh | `ops/deploy-backend.sh` | ✅ Funcional | Sin rollback; sin `flask db upgrade` |
| Frontend deploy | deploy-frontend.sh | `ops/deploy-frontend.sh` | ✅ Funcional | Sin rollback |
| Docker backend | api/Dockerfile | `api/Dockerfile` | ✅ Multi-stage, non-root | Sin test stage |
| Docker dev | Dockerfile (root) | `Dockerfile` | ⚠️ Inseguro | Root user, dev server, sin healthcheck |
| Compose prod | docker-compose.backend.prod.yml | `ops/` | ✅ Existe | No verificado |

## Tareas propuestas

| ID | Prioridad | Tarea | Owner sugerido | Estimacion | Depende de |
|---|---|---|---|---|---|
| T-701 | P0 | Fix e2e job: anadir `services: postgres:` + Redis | Agent QA / DevOps | 1 dia | — |
| T-702 | P0 | Des-skip tenant isolation test con fixtures reales | Agent QA + Agent DB | 2 dias | T-701 |
| T-703 | P1 | Hacer lint bloqueante en CI (eliminar `--exit-zero`) | Agent QA / DevOps | 0.5 dias | — |
| T-704 | P1 | Crear `api/pytest.ini` o consolidar testpaths | Agent QA / DevOps | 0.5 dias | — |
| T-705 | P1 | Usar `requirements-dev.txt` en CI en vez de install manual | Agent QA / DevOps | 0.5 dias | — |
| T-706 | P1 | Quitar `tail -20` de vitest output; subir coverage | Agent QA / DevOps | 0.5 dias | — |
| T-707 | P2 | Anadir E2E tests de login real y creacion de clone | Agent QA + Agent Frontend | 2 dias | T-701 |
| T-708 | P2 | Des-skip admin auth tests con JWT fixture | Agent QA + Agent Security | 1 dia | — |
| T-709 | P2 | Implementar rollback en deploy scripts | Agent QA / DevOps | 1 dia | — |
| T-710 | P2 | Eliminar root Dockerfile; documentar `api/Dockerfile` como unico | Agent QA / DevOps | 0.5 dias | — |
| T-711 | P2 | Anadir coverage thresholds en vitest.config.ts | Agent QA / DevOps | 0.5 dias | — |
| T-713 | P3 | Consolidar requirements.txt duplicados | Agent QA / DevOps | 0.5 dias | — |

## Open Questions

1. **E2E roto**: Se confirma que el job `e2e` en CI esta fallando? Si nadie lo ha visto pasar, puede que nunca haya funcionado.
2. **Coverage target**: Cual es el minimo aceptable para MVP? Sugiero 50% lines para frontend, 30% para backend.
3. **Deploy rollback**: Se necesita rollback automatico o suficiente con health check + notificacion?
4. **Playwright browsers**: Se necesita soporte multi-browser o Chromium es suficiente para el MVP?
5. **Smoke test de produccion**: `smoke-prod.sh` solo tests HTTP. Se necesita smoke con autenticacion?
