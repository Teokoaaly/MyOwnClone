# PLAN MAESTRO EJECUTABLE — MyOwnClone VPS

> Versión: 1.0
> Fecha: 2026-07-05
> Generado por: LLM agente (auditoría + AdminSwitch + correcciones)

---

## RESUMEN EJECUTIVO

| Total tareas | Críticas | Requieren confirmación | Tiempo total |
|---|---|---|---|
| 16 | 5 | 1 | 4-6 horas |

---

## ESTADO ACTUAL DEL SISTEMA

- **Frontend**: BUILD_ID actual en VPS (sigue siendo del release `20260704222310-frontend-codex-admin`)
- **Landing**: INTACTA, NO se tocó
- **Backend**: Healthy, 5 contenedores (api + worker + postgres + redis + weaviate + ollama)
- **DB**: 32 tablas, alembic `2026_07_03_0001`
- **Login**: Funcional con `admin@myownclone.com` / `MocAdmin!2026-06-24`
- **AuthSwitch**: Implementado (TASK-010, TASK-011, TASK-012 completados)

---

## FASE A — TAREAS DE ADMINISTRACIÓN

### TASK-A01 — Auditoría completa del VPS
- **Área**: VPS / Repo / DB
- **Prioridad**: CRÍTICO
- **Dependencias**: NINGUNA
- **Problema**: Necesidad de tener visibilidad completa del estado del sistema
- **Causa raíz**: Falta de documentación operativa
- **Acción**: Ejecutar los comandos de auditoría (ya hecho en este plan, verificar contra el sistema)
- **Archivos**: `MASTER_STATE.md`, `MASTER_LOG.md`
- **Verificación**: Los archivos reflejan el estado real del sistema
- **Rollback**: N/A (solo lectura)
- **Restricción**: NINGUNA
- **Riesgo**: NINGUNO
- **Tiempo**: 5 min

### TASK-A02 — Verificar acceso SSH y backups
- **Área**: VPS
- **Prioridad**: ALTO
- **Dependencias**: TASK-A01
- **Problema**: No se sabe si el cron de backup funciona
- **Causa raíz**: La auditoría mostró cron vacío
- **Acción**: `crontab -l` para verificar; si está vacío, añadir el backup con `ops/backup_postgres.sh`
- **Archivos**: crontab
- **Verificación**: `ls -la /opt/myownclone/backups/` muestra archivos nuevos
- **Rollback**: `crontab -r`
- **Restricción**: NO añadir tareas que no sean backup
- **Riesgo**: BAJO
- **Tiempo**: 10 min

---

## FASE B — TAREAS DE ADMIN SWITCH

### TASK-B01 — Crear componente AdminSwitch
- **Área**: Frontend / Componentes
- **Prioridad**: ALTO
- **Dependencias**: NINGUNA
- **Problema**: Admin no puede alternar dashboard ↔ backend sin reauth
- **Causa raíz**: Solo hay un link "Back to dashboard" en admin layout, sin botón dashboard→admin
- **Acción**: Crear `MyOwnClone/src/components/dashboard/AdminSwitch.tsx` con useRouter para navegar
- **Archivos**: `MyOwnClone/src/components/dashboard/AdminSwitch.tsx` (NUEVO)
- **Verificación**: El componente renderiza solo para `platform_admin`
- **Rollback**: Borrar el archivo
- **Restricción**: NO usar `force-motion` o props incompatibles con la interface
- **Riesgo**: BAJO
- **Tiempo**: 5 min
- **Estado**: ✅ COMPLETADA (commit actual)

### TASK-B02 — Integrar AdminSwitch en dashboard layout
- **Área**: Frontend / Layouts
- **Prioridad**: ALTO
- **Dependencias**: TASK-B01
- **Problema**: Botón no aparece en dashboard
- **Causa raíz**: El layout no lo importa
- **Acción**: En `MyOwnClone/src/app/(dashboard)/layout.tsx`, añadir import y footer prop condicional
- **Archivos**: `MyOwnClone/src/app/(dashboard)/layout.tsx`
- **Verificación**: Admin logueado ve el botón en dashboard sidebar
- **Rollback**: Quitar el import y el footer prop
- **Restricción**: NO alterar la landing
- **Riesgo**: BAJO (cambio aditivo)
- **Tiempo**: 5 min
- **Estado**: ✅ COMPLETADA

### TASK-B03 — Integrar AdminSwitch en admin layout
- **Área**: Frontend / Layouts
- **Prioridad**: ALTO
- **Dependencias**: TASK-B01
- **Problema**: Botón no aparece en admin
- **Causa raíz**: El layout usa un link, no el componente
- **Acción**: En `MyOwnClone/src/app/admin/layout.tsx`, reemplazar el Link por AdminSwitch
- **Archivos**: `MyOwnClone/src/app/admin/layout.tsx`
- **Verificación**: Admin ve el botón de vuelta al dashboard
- **Rollback**: Restaurar el Link original
- **Restricción**: NO tocar la landing
- **Riesgo**: BAJO
- **Tiempo**: 5 min
- **Estado**: ✅ COMPLETADA

### TASK-B04 — Verificar protección backend
- **Área**: Frontend / Auth
- **Prioridad**: CRÍTICO
- **Dependencias**: NINGUNA
- **Problema**: Verificar que no-admin no puede acceder a /admin/*
- **Causa raíz**: Necesidad de validación
- **Acción**: En el navegador, login con `ia.hacchi@gmail.com` (owner) y verificar que NO ve AdminSwitch
- **Verificación**: Login con owner → AdminSwitch invisible; URL directa /admin → redirect
- **Rollback**: N/A (ya existe `isPlatformAdminSession` guard)
- **Restricción**: NINGUNA
- **Riesgo**: NINGUNO (ya implementado)
- **Tiempo**: 5 min

### TASK-B05 — Verificación completa AdminSwitch
- **Área**: Frontend / Verificación
- **Prioridad**: CRÍTICO
- **Dependencias**: TASK-B01, TASK-B02, TASK-B03
- **Problema**: Verificar todos los casos de uso
- **Causa raíz**: Necesidad de validación E2E
- **Acción**: Build + deploy + test manual en navegador
- **Archivos**: N/A (solo verificación)
- **Verificación**:
  1. Login admin → switch visible
  2. Login no-admin → switch invisible
  3. Switch dashboard → admin funciona
  4. Switch admin → dashboard funciona
  5. URL directa sin admin → redirect
- **Rollback**: Revertir TASK-B01, TASK-B02, TASK-B03
- **Restricción**: PROHIBIDO tocar la landing
- **Riesgo**: MEDIO
- **Tiempo**: 30 min (incluye build + deploy)

---

## FASE C — CORRECCIONES DE PRODUCCIÓN

### TASK-C01 — Recrear Redis sin TLS
- **Área**: Docker / Backend
- **Prioridad**: CRÍTICO
- **Dependencias**: NINGUNA
- **Problema**: Redis estaba configurado con TLS (puerto 6380) pero el compose del release activo no incluye TLS, causando error 503 en /readyz
- **Causa raíz**: Inconsistencia entre compose (6379 sin TLS) y contenedor Redis en ejecución (6380 con TLS)
- **Acción**: `docker compose up -d --force-recreate redis` para recrear Redis con la config del compose
- **Archivos**: N/A
- **Verificación**: `curl /readyz` da 200 con `redis:ok`
- **Rollback**: N/A (recrear contenedor)
- **Restricción**: NO cambiar otras configs
- **Riesgo**: BAJO (Redis no tiene datos críticos, solo rate limit + cache)
- **Tiempo**: 5 min
- **Estado**: ✅ COMPLETADA (Redis ya recreado)

### TASK-C02 — Arreglar /healthz detallado
- **Área**: Backend
- **Prioridad**: MEDIO
- **Dependencias**: NINGUNA
- **Problema**: `/healthz` solo devuelve `{"status":"ok"}` sin detalles
- **Causa raíz**: La ruta /healthz está duplicada y la del api solo devuelve status simple
- **Acción**: En `api/app_factory.py`, cambiar la ruta /healthz para que devuelva lo mismo que /readyz
- **Archivos**: `api/app_factory.py`
- **Verificación**: `curl /healthz` devuelve `{"checks":{...},"status":"ready"}`
- **Rollback**: Restaurar la versión simple
- **Restricción**: NO cambiar otras rutas
- **Riesgo**: BAJO
- **Tiempo**: 5 min

### TASK-C03 — Verificar cron de backups
- **Área**: VPS / Sistema
- **Prioridad**: ALTO
- **Dependencias**: TASK-A02
- **Problema**: Cron vacío, no se sabe si backups automáticos funcionan
- **Causa raíz**: La auditoría mostró `crontab -l` sin contenido
- **Acción**: Añadir `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1`
- **Archivos**: crontab
- **Verificación**: `ls -la /opt/myownclone/backups/` después de 24h muestra nuevo archivo
- **Rollback**: `crontab -r`
- **Restricción**: NO añadir tareas que no sean backup
- **Riesgo**: BAJO
- **Tiempo**: 5 min

---

## FASE D — MEJORAS OPCIONALES

### TASK-D01 — Aumentar monitorización con Sentry
- **Área**: Backend / Observabilidad
- **Prioridad**: MEDIO
- **Dependencias**: Ninguna (Sentry ya inicializado en app_factory)
- **Problema**: Sentry no se activa porque no hay SENTRY_DSN
- **Causa raíz**: Falta configurar DSN
- **Acción**: Crear cuenta Sentry, obtener DSN, añadir a `backend.env.production`
- **Verificación**: Producir un error 500 y ver que aparece en Sentry
- **Rollback**: Quitar SENTRY_DSN
- **Restricción**: NO cambiar el código de Sentry
- **Riesgo**: BAJO
- **Tiempo**: 15 min

### TASK-D02 — PostHog analytics
- **Área**: Frontend / Observabilidad
- **Prioridad**: BAJO
- **Dependencias**: Ninguna
- **Problema**: PostHog no configurado
- **Causa raíz**: NEXT_PUBLIC_POSTHOG_KEY vacía
- **Acción**: Crear cuenta PostHog, añadir key, inicializar PostHogProvider en NextAuth
- **Verificación**: Ver eventos en dashboard PostHog
- **Rollback**: Quitar variables
- **Restricción**: NO agregar scripts de tracking invasivos
- **Riesgo**: BAJO
- **Tiempo**: 20 min

---

## ORDEN DE EJECUCIÓN

```
FASE A (auditoría):
  TASK-A01 ✅ COMPLETADA (este plan)
  TASK-A02 ⚠️ PENDIENTE (verificar backups)

FASE B (AdminSwitch):
  TASK-B01 ✅ COMPLETADA
  TASK-B02 ✅ COMPLETADA
  TASK-B03 ✅ COMPLETADA
  TASK-B04 ⚠️ PENDIENTE (verificación)
  TASK-B05 ⚠️ PENDIENTE (build + deploy + test E2E)

FASE C (correcciones):
  TASK-C01 ✅ COMPLETADA (Redis sin TLS)
  TASK-C02 ⚠️ PENDIENTE (/healthz detallado)
  TASK-C03 ⚠️ PENDIENTE (cron backups)

FASE D (mejoras):
  TASK-D01 ⚠️ PENDIENTE (Sentry)
  TASK-D02 ⚠️ PENDIENTE (PostHog)
```

## RIESGOS GLOBALES

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Build del frontend rompe landing | MEDIA | ALTO | NO hacer rebuild sin aprobación. Probar en staging primero. |
| Pérdida de Redis al recrear | BAJA | BAJO | Redis no tiene datos críticos (rate limit + cache) |
| Pérdida de DB al restaurar | MUY BAJA | CRÍTICO | Backups en /var/backups/. Verificar antes de cualquier acción destructiva. |
| Sentry/PostHog consumen recursos | BAJA | BAJO | Solo activar si hay RAM libre > 1GB |

## RESTRICCIONES INNEGOCIABLES

1. **PROHIBIDO tocar frontend/landing** (`src/app/page.tsx`, `src/components/landing/*`, `src/app/(public)/*`)
2. **NO hacer rebuild del frontend** sin aprobación explícita
3. **NO borrar nada** sin confirmar
4. **NO asumir** que algo funciona sin verificarlo
5. **AdminSwitch SOLO para platform_admin**
6. **Correcciones mínimas** y reversibles
7. **Documentar cada cambio** en MASTER_LOG.md

## CHECKLIST DE VALIDACIÓN FINAL

- [ ] Login admin funciona con `MocAdmin!2026-06-24`
- [ ] Login no-admin funciona con sus credenciales
- [ ] AdminSwitch visible solo para platform_admin
- [ ] Switch dashboard → admin funciona
- [ ] Switch admin → dashboard funciona
- [ ] URL directa /admin sin admin → redirect
- [ ] /readyz devuelve 200 con checks
- [ ] /healthz responde correctamente
- [ ] Landing INTACTA (no se cambió)
- [ ] MASTER_STATE.md actualizado
- [ ] MASTER_LOG.md actualizado

## VALIDACIÓN FINAL

Para confirmar que todo está correcto:
1. `curl https://myownclone.com/api/auth/session` con cookie de admin → devuelve user con role platform_admin
2. `curl https://myownclone.com/api/admin/overview` con headers de admin → devuelve métricas
3. `curl https://myownclone.com/admin/resumen` con sesión de admin → 200
4. `curl https://myownclone.com/admin/resumen` sin sesión → 307 a /login
5. La landing `https://myownclone.com` sigue mostrando el contenido original (no se cambió)
