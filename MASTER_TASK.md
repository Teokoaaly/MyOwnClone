# MASTER_TASK.md

> **Version**: 2.0
> **Fecha**: 2026-07-06
> **Para**: MiniMax M2.7 (modelo base autonomo)
> **Auditoria basada en**: comparacion repo vs VPS 2026-07-06
> **Estado**: PROHIBIDO tocar la landing (BUILD_ID s4Hs00UHv6esTNBt7xcUp)

---

## OBJETIVO

Ejecutar autonomamente las tareas pendientes identificadas en la auditoria repo-vs-VPS del 2026-07-06.
**NO se debe tocar la landing** (`s4Hs00UHv6esTNBt7xcUp`). Todo cambio debe ser reversible y documentado.

---

## ESTADO ACTUAL VERIFICADO (auditoria 2026-07-06)

| Componente | Estado | Evidencia |
|---|---|---|
| **Release activo** | `20260703190910-landing-cleanup-restore` | `readlink /opt/myownclone/current` |
| **BUILD_ID frontend** | `s4Hs00UHv6esTNBt7xcUp` ✅ INTACTO | `.next/BUILD_ID` |
| **Backend admin** | ✅ Desplegado (HTTP 401 en endpoints = existe + requiere auth) | `/console/api/myownclone/admin/overview` |
| **Migrations BD** | ✅ Aplicada hasta `2026_07_03_0001` | `alembic_version` |
| **Tablas BD** | ✅ 32 tablas | `psql \dt` |
| **Bug encontrado** | ❌ `maintenance.py` NO registrado en `__init__.py` → 404 | Ver TASK-001 |
| **Frontend admin** | ⚠️ Codigo fuente existe, NO compilado en build actual | Ver TASK-002 |
| **LanguageSelector** | ❌ Ausente (revert autorizado 30 jun `bceee0a`) | `git log` |
| **Contenedores** | ✅ 6 healthy (api, postgres, redis, weaviate, worker, ollama) | `docker ps` |

---

## REGLAS INQUEBRANTABLES

1. La landing `s4Hs00UHv6esTNBt7xcUp` es INTOCABLE
2. NO rebuilds de frontend sin autorizacion explicita del usuario (cambia BUILD_ID)
3. NO tocar `src/app/page.tsx`, `src/app/login/*`, `src/app/registro/*`, `src/app/(public)/*`, `src/components/landing/*`
4. Cada cambio se documenta en `MASTER_LOG.md`
5. El estado actual se refleja en `MASTER_STATE.md`
6. Si un comando falla, revertir inmediatamente
7. NO usar `git push --force`
8. NO borrar archivos sin backup
9. Antes de CUALQUIER cambio: hacer snapshot de seguridad (TASK-004)

---

## ESTRUCTURA DEL VPS (verificada 2026-07-06)

```
/opt/myownclone/
  current -> /opt/myownclone/releases/20260703190910-landing-cleanup-restore (BUILD_ID s4Hs00UH)
  releases/
    20260703190910-landing-cleanup-restore (ACTIVO - landing aprobada)
    20260704222310-frontend-codex-admin (anterior codex, sin BUILD_ID)
    20260701150141-backend-codex-deploy
    20260629144355-frontend-i18n-selector
    20260629141926-i18n-manual-selector
    20260620070304-frontend-dashboard-fix
  snapshots/ (aqui iran los backups pre-cambio)
  backups/
  shared/
```

---

## ORDEN DE EJECUCION DE TASKS

```
TASK-004 (snapshot) → TASK-001 (fix maintenance) → TASK-A02 (cron backup) → TASK-C03 (healthcheck) → TASK-002 (verificar) → TASK-C02 (healthz) → TASK-D01 (verificar) → TASK-D02 (verificar)
```

**TASK-B05 (AdminSwitch) y re-deploy LanguageSelector**: REQUIEREN AUTORIZACION EXPLICITA del usuario. NO ejecutar.

---

## TASK-004: Snapshot de seguridad pre-cambios

**Estado**: PENDIENTE
**Prioridad**: CRITICA (hacer ANTES de cualquier otra cosa)
**Objetivo**: Permitir rollback completo al estado actual si algo falla

**Pasos**:
```bash
ssh root@212.227.169.99 "
  mkdir -p /opt/myownclone/snapshots
  tar czf /opt/myownclone/snapshots/pre-audit-2026-07-06-\$(date +%s).tar.gz \\
    -C /opt/myownclone/releases/20260703190910-landing-cleanup-restore \\
    --exclude='.next/cache' .
  ls -la /opt/myownclone/snapshots/
"
```

**Validacion**:
- [ ] Archivo tar.gz creado en `/opt/myownclone/snapshots/`
- [ ] Tamaño coherente (debe ser >100MB)

**Rollback**: `ssh root@212.227.169.99 "rm /opt/myownclone/current && ln -s /opt/myownclone/releases/20260703190910-landing-cleanup-restore /opt/myownclone/current && systemctl restart myownclone-frontend && cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml restart api"`

---

## TASK-001: Fix bug maintenance (registro en __init__.py)

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Objetivo**: Activar endpoints `/console/api/myownclone/maintenance/{status,toggle}` que actualmente dan 404

**Evidencia del bug**:
```
$ docker exec myownclone_api cat /app/api/controllers/console/myownclone/__init__.py
from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, runtime, stripe_ctrl
# maintenance NO esta en la lista
```

**Archivo a modificar**: `/opt/myownclone/current/api/controllers/console/myownclone/__init__.py`

**Cambio exacto** (1 linea):
```diff
- from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, runtime, stripe_ctrl
+ from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, maintenance, runtime, stripe_ctrl
```

**Pasos**:
```bash
ssh root@212.227.169.99 "
  # Backup
  cp /opt/myownclone/current/api/controllers/console/myownclone/__init__.py /tmp/init_backup_\$(date +%s).py
  # Aplicar fix
  sed -i 's/from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, runtime, stripe_ctrl/from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, maintenance, runtime, stripe_ctrl/' \\
    /opt/myownclone/current/api/controllers/console/myownclone/__init__.py
  # Verificar cambio
  grep 'maintenance' /opt/myownclone/current/api/controllers/console/myownclone/__init__.py
  # Reiniciar API
  cd /opt/myownclone/current/ops
  docker compose -f docker-compose.backend.prod.yml restart api
  sleep 10
  # Verificar endpoint
  curl -s -o /dev/null -w 'maintenance/status HTTP %{http_code}\\n' http://127.0.0.1:5001/console/api/myownclone/maintenance/status
"
```

**Validacion**:
- [ ] `maintenance` aparece en el `__init__.py`
- [ ] `/console/api/myownclone/maintenance/status` devuelve HTTP 401 (no 404)
- [ ] `/console/api/myownclone/maintenance/toggle` devuelve HTTP 401 (no 404)
- [ ] Otros endpoints admin siguen funcionando (HTTP 401)

**Rollback**:
```bash
ssh root@212.227.169.99 "
  cp /tmp/init_backup_*.py /opt/myownclone/current/api/controllers/console/myownclone/__init__.py
  cd /opt/myownclone/current/ops
  docker compose -f docker-compose.backend.prod.yml restart api
"
```

---

## TASK-A02: Cron de backups PostgreSQL

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Objetivo**: Configurar backup automatico diario a las 3 AM UTC

**Pasos**:
```bash
ssh root@212.227.169.99 "
  # Verificar script
  ls -la /opt/myownclone/current/ops/backup_postgres.sh
  chmod +x /opt/myownclone/current/ops/backup_postgres.sh
  # Crear log file
  touch /var/log/myownclone-backup.log
  chmod 644 /var/log/myownclone-backup.log
  # Anadir al crontab (sin duplicar)
  (crontab -l 2>/dev/null | grep -v 'backup_postgres.sh'; \\
   echo '0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1') | crontab -
  crontab -l | grep backup
"
```

**Validacion**:
- [ ] crontab -l muestra: `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1`
- [ ] /var/log/myownclone-backup.log existe y es escribible

**Rollback**:
```bash
ssh root@212.227.169.99 "(crontab -l 2>/dev/null | grep -v 'backup_postgres.sh') | crontab -"
```

---

## TASK-C03: Healthcheck automatico cada 5 min

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Objetivo**: Detectar caidas del API y registrarlas

**Pasos**:
```bash
ssh root@212.227.169.99 '
  cat > /opt/myownclone/current/ops/healthcheck.sh << "SCRIPT"
#!/bin/bash
LOG=/var/log/myownclone-healthcheck.log
ST=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001/readyz)
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "$ST" != "200" ]; then
    echo "$NOW ALERT readyz=$ST" >> $LOG
fi
SCRIPT
  chmod +x /opt/myownclone/current/ops/healthcheck.sh
  touch /var/log/myownclone-healthcheck.log
  chmod 644 /var/log/myownclone-healthcheck.log
  (crontab -l 2>/dev/null | grep -v "healthcheck.sh"; echo "*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh") | crontab -
  crontab -l | grep healthcheck
'
```

**Validacion**:
- [ ] script existe y es ejecutable
- [ ] crontab muestra: `*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh`
- [ ] log file existe

**Rollback**:
```bash
ssh root@212.227.169.99 "(crontab -l 2>/dev/null | grep -v 'healthcheck.sh') | crontab -"
```

---

## TASK-002: Verificar gap frontend admin

**Estado**: PENDIENTE
**Prioridad**: BAJA (solo lectura)
**Objetivo**: Confirmar si las paginas `/admin/*` estan compiladas en `.next/` del release actual

**Pasos**:
```bash
ssh root@212.227.169.99 "
  echo '=== DIRECTORIOS ADMIN EN BUILD ==='
  find /opt/myownclone/current/MyOwnClone/.next/server/app -type d -name 'admin' 2>/dev/null
  echo
  echo '=== TEST /admin/resumen ==='
  curl -s -o /dev/null -w 'HTTP %{http_code}\\n' http://127.0.0.1:3000/admin/resumen
  echo
  echo '=== TEST /admin/tenants ==='
  curl -s -o /dev/null -w 'HTTP %{http_code}\\n' http://127.0.0.1:3000/admin/tenants
  echo
  echo '=== BUILD_ID ==='
  cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID
"
```

**Validacion - Reportar**:
- [ ] Si HTTP 200 con HTML admin UI → admin frontend compilado y servido
- [ ] Si HTTP 404 o HTML contiene "404: This page" → admin frontend NO compilado (requiere rebuild que cambiara BUILD_ID)

**Accion posterior** (solo si admin frontend NO compilado):
- Documentar hallazgo en MASTER_LOG.md
- NO hacer rebuild sin autorizacion explicita

**Rollback**: N/A (solo lectura)

---

## TASK-C02: /healthz detallada (checks DB+Redis+Ollama)

**Estado**: PENDIENTE
**Prioridad**: MEDIO
**Objetivo**: Endpoint /healthz con verificacion real de componentes

**Archivo a modificar**: `/opt/myownclone/current/api/app_factory.py`

**Localizar** la funcion healthz actual (probablemente `return jsonify({"status": "ok"})`).

**Reemplazar con**:
```python
@app.route("/healthz")
def healthz():
    checks = {}
    all_ok = True
    # Database
    try:
        db.session.execute(text("SELECT 1"))
        checks["database"] = "ok"
    except Exception as exc:
        checks["database"] = f"error: {str(exc)[:100]}"
        all_ok = False
    # Redis (sin TLS, compose actual usa puerto 6379)
    try:
        import redis as redis_lib
        client = redis_lib.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            password=os.getenv("REDIS_PASSWORD") or None,
            socket_connect_timeout=2.0,
            socket_timeout=2.0,
        )
        client.ping()
        checks["redis"] = "ok"
    except Exception as exc:
        checks["redis"] = f"error: {str(exc)[:100]}"
        all_ok = False
    # Ollama
    try:
        import requests
        r = requests.get("http://ollama:11434/api/tags", timeout=2)
        checks["ollama"] = "ok" if r.status_code == 200 else f"error: HTTP {r.status_code}"
    except Exception as exc:
        checks["ollama"] = f"error: {str(exc)[:100]}"
    status_code = 200 if all_ok else 503
    return jsonify({"status": "ready" if all_ok else "degraded", "checks": checks}), status_code
```

**Pasos**:
```bash
ssh root@212.227.169.99 "
  # Backup
  cp /opt/myownclone/current/api/app_factory.py /tmp/app_factory.py.backup.\$(date +%s)
  # Localizar y reemplazar (usar sed o editor)
  # El comando exacto depende de la implementacion actual
  # Sugerencia: usar python para hacer el edit de forma segura
  
  python3 << 'PYEOF'
import re
path = '/opt/myownclone/current/api/app_factory.py'
with open(path) as f:
    content = f.read()

new_func = '''@app.route(\"/healthz\")
def healthz():
    checks = {}
    all_ok = True
    try:
        db.session.execute(text(\"SELECT 1\"))
        checks[\"database\"] = \"ok\"
    except Exception as exc:
        checks[\"database\"] = f\"error: {str(exc)[:100]}\"
        all_ok = False
    try:
        import redis as redis_lib
        client = redis_lib.Redis(
            host=os.getenv(\"REDIS_HOST\", \"redis\"),
            port=int(os.getenv(\"REDIS_PORT\", \"6379\")),
            password=os.getenv(\"REDIS_PASSWORD\") or None,
            socket_connect_timeout=2.0,
            socket_timeout=2.0,
        )
        client.ping()
        checks[\"redis\"] = \"ok\"
    except Exception as exc:
        checks[\"redis\"] = f\"error: {str(exc)[:100]}\"
        all_ok = False
    try:
        import requests
        r = requests.get(\"http://ollama:11434/api/tags\", timeout=2)
        checks[\"ollama\"] = \"ok\" if r.status_code == 200 else f\"error: HTTP {r.status_code}\"
    except Exception as exc:
        checks[\"ollama\"] = f\"error: {str(exc)[:100]}\"
    status_code = 200 if all_ok else 503
    return jsonify({\"status\": \"ready\" if all_ok else \"degraded\", \"checks\": checks}), status_code'''

# Reemplazar funcion existente
pattern = r'@app.route\\(\"/healthz\"\\)[^@]*?return jsonify\\(\\{\"status\":\\s*\"ok\"\\}\\)[^\\n]*'
new_content = re.sub(pattern, new_func, content, count=1, flags=re.DOTALL)

if new_content != content:
    with open(path, 'w') as f:
        f.write(new_content)
    print('OK: healthz actualizado')
else:
    print('WARN: no se encontro patron exacto, requiere edit manual')
PYEOF
  
  # Reiniciar API
  cd /opt/myownclone/current/ops
  docker compose -f docker-compose.backend.prod.yml restart api
  sleep 10
  # Verificar
  curl -s http://127.0.0.1:5001/healthz | python3 -m json.tool
"
```

**Validacion**:
- [ ] /healthz devuelve JSON con keys `database`, `redis`, `ollama`
- [ ] Status code 200 si todo OK, 503 si falla algo
- [ ] /readyz sigue funcionando (no se toco)

**Rollback**:
```bash
ssh root@212.227.169.99 "
  cp /tmp/app_factory.py.backup.* /opt/myownclone/current/api/app_factory.py
  cd /opt/myownclone/current/ops
  docker compose -f docker-compose.backend.prod.yml restart api
"
```

---

## TASK-D01: Verificar Sentry (NO activar)

**Estado**: PENDIENTE (espera DSN del usuario)
**Prioridad**: BAJA
**Objetivo**: Confirmar que el codigo de Sentry esta preparado

**Pasos**:
```bash
ssh root@212.227.169.99 "
  echo '=== SENTRY EN BACKEND ==='
  grep -rE 'sentry|SENTRY' /opt/myownclone/current/api/app_factory.py 2>/dev/null | head -10
  echo
  echo '=== SENTRY EN REQUIREMENTS ==='
  grep -i sentry /opt/myownclone/current/api/requirements.txt 2>/dev/null
"
```

**Validacion**:
- [ ] Si aparece codigo de Sentry → esta preparado
- [ ] Si NO aparece → falta (no es critico, espera DSN del usuario)
- [ ] NO activar (sin DSN no funciona)

**Rollback**: N/A

---

## TASK-D02: Verificar PostHog (NO activar)

**Estado**: PENDIENTE (espera API key)
**Prioridad**: BAJA
**Objetivo**: Confirmar que el codigo de PostHog esta preparado

**Pasos**:
```bash
ssh root@212.227.169.99 "
  echo '=== POSTHOG EN FRONTEND ==='
  grep -rE 'posthog|PostHog' /opt/myownclone/current/MyOwnClone/src/lib/auth.ts 2>/dev/null | head -10
  echo
  echo '=== POSTHOG EN PACKAGE.JSON ==='
  grep -i posthog /opt/myownclone/current/MyOwnClone/package.json 2>/dev/null
"
```

**Validacion**:
- [ ] Si aparece codigo de PostHog → esta preparado
- [ ] Si NO aparece → falta (no es critico, espera key del usuario)
- [ ] NO activar (sin key no funciona)

**Rollback**: N/A

---

## TASKS QUE REQUIEREN AUTORIZACION EXPLICITA (NO EJECUTAR)

### TASK-B05: AdminSwitch build + deploy + test
- **Estado**: BLOQUEADO por regla "no tocar landing"
- **Razon**: Requiere rebuild de frontend, cambia BUILD_ID
- **Prereq**: Autorizacion explicita del usuario

### TASK-RE-i18n: Re-deploy LanguageSelector
- **Estado**: BLOQUEADO por regla "no tocar landing"
- **Razon**: Requiere rebuild de frontend, cambia BUILD_ID
- **Prereq**: Autorizacion explicita del usuario

### TASK-REBUILD-ADMIN-FRONTEND: Compilar paginas /admin/*
- **Estado**: BLOQUEADO por regla "no tocar landing"
- **Razon**: Requiere rebuild de frontend, cambia BUILD_ID
- **Prereq**: Autorizacion explicita del usuario

---

## SCRIPT MAESTRO DE EJECUCION (orden estricto)

```bash
#!/bin/bash
# Ejecutar como MiniMax M2.7

set -e

VPS="root@212.227.169.99"

echo "=== TASK-004: Snapshot de seguridad ==="
ssh $VPS "
  mkdir -p /opt/myownclone/snapshots
  tar czf /opt/myownclone/snapshots/pre-audit-2026-07-06-\$(date +%s).tar.gz \\
    -C /opt/myownclone/releases/20260703190910-landing-cleanup-restore \\
    --exclude='.next/cache' .
  ls -la /opt/myownclone/snapshots/
"
echo "Snapshot creado OK"
echo

echo "=== TASK-001: Fix bug maintenance ==="
ssh $VPS "
  cp /opt/myownclone/current/api/controllers/console/myownclone/__init__.py /tmp/init_backup_\$(date +%s).py
  sed -i 's/from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, runtime, stripe_ctrl/from . import admin_platform, ai_models, analytics, booking, clone, creator_memory, feedback, inbox, locale, maintenance, runtime, stripe_ctrl/' \\
    /opt/myownclone/current/api/controllers/console/myownclone/__init__.py
  grep 'maintenance' /opt/myownclone/current/api/controllers/console/myownclone/__init__.py
  cd /opt/myownclone/current/ops && docker compose -f docker-compose.backend.prod.yml restart api
  sleep 10
  curl -s -o /dev/null -w 'maintenance/status HTTP %{http_code}\\n' http://127.0.0.1:5001/console/api/myownclone/maintenance/status
"
echo

echo "=== TASK-A02: Cron de backups ==="
ssh $VPS "
  chmod +x /opt/myownclone/current/ops/backup_postgres.sh
  touch /var/log/myownclone-backup.log
  chmod 644 /var/log/myownclone-backup.log
  (crontab -l 2>/dev/null | grep -v 'backup_postgres.sh'; echo '0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1') | crontab -
  crontab -l | grep backup
"
echo

echo "=== TASK-C03: Healthcheck automatico ==="
ssh $VPS '
  cat > /opt/myownclone/current/ops/healthcheck.sh << "SCRIPT"
#!/bin/bash
LOG=/var/log/myownclone-healthcheck.log
ST=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001/readyz)
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "$ST" != "200" ]; then
    echo "$NOW ALERT readyz=$ST" >> $LOG
fi
SCRIPT
  chmod +x /opt/myownclone/current/ops/healthcheck.sh
  touch /var/log/myownclone-healthcheck.log
  chmod 644 /var/log/myownclone-healthcheck.log
  (crontab -l 2>/dev/null | grep -v "healthcheck.sh"; echo "*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh") | crontab -
  crontab -l | grep healthcheck
'
echo

echo "=== TASK-002: Verificar gap admin frontend ==="
ssh $VPS "
  find /opt/myownclone/current/MyOwnClone/.next/server/app -type d -name 'admin' 2>/dev/null
  curl -s -o /dev/null -w '/admin/resumen HTTP %{http_code}\\n' http://127.0.0.1:3000/admin/resumen
  cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID
"
echo

echo "=== TASK-C02: /healthz detallada ==="
# Requiere edit manual del app_factory.py - usar la logica de la seccion TASK-C02
# Saltar si no es seguro hacerlo automaticamente

echo

echo "=== TASK-D01/D02: Verificar Sentry/PostHog ==="
ssh $VPS "
  echo '--- Sentry ---'
  grep -rE 'sentry|SENTRY' /opt/myownclone/current/api/app_factory.py 2>/dev/null | head -5
  echo '--- PostHog ---'
  grep -rE 'posthog|PostHog' /opt/myownclone/current/MyOwnClone/src/lib/auth.ts 2>/dev/null | head -5
"
echo

echo "=== VALIDACION FINAL ==="
ssh $VPS "
  echo 'BUILD_ID:' \$(cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID)
  echo 'Release:' \$(readlink /opt/myownclone/current)
  echo 'Frontend:' \$(systemctl is-active myownclone-frontend)
  echo 'API health:' \$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:5001/readyz)
  echo 'Landing:' \$(curl -s -o /dev/null -w '%{http_code}' https://myownclone.com/)
  echo 'Cron entries:'
  crontab -l
"
```

---

## CHECKLIST DE VALIDACION FINAL

Despues de ejecutar todos los pasos:

- [ ] Snapshot de seguridad creado en `/opt/myownclone/snapshots/`
- [ ] `maintenance` aparece en `__init__.py` y endpoint devuelve 401 (no 404)
- [ ] crontab -l muestra entradas de backup y healthcheck
- [ ] /var/log/myownclone-backup.log existe
- [ ] /var/log/myownclone-healthcheck.log existe
- [ ] /healthz devuelve JSON con checks detallados (o se reporto que no se pudo hacer)
- [ ] Frontend sigue con BUILD_ID `s4Hs00UHv6esTNBt7xcUp`
- [ ] Landing NO se ha tocado (verificar con `cat .next/BUILD_ID`)
- [ ] AdminSwitch NO se ha activado (sigue en stash)
- [ ] Sentry y PostHog verificados (siguen sin activar)
- [ ] Sentry y PostHog: codigo presente o ausente (documentado)
- [ ] MASTER_LOG.md actualizado con cada cambio
- [ ] MASTER_STATE.md refleja estado final

---

## ARCHIVOS DE REFERENCIA

- `MASTER_STATE.md` - Estado actual del sistema
- `MASTER_LOG.md` - Trazabilidad de cambios
- `PLAN_MAESTRO.md` - Plan completo de 16 tareas
- `DOCS_PREVENTIVOS.md` - Procedimientos y señales de alerta
- `LANDING_APROBADA.md` - Confirmacion de la landing s4Hs00UH

---

## COMUNICACION (formato obligatorio en MASTER_LOG.md)

```
## [YYYY-MM-DD HH:MM UTC] - [TASK-ID] [OK/FAIL]
**Tarea**: [descripcion corta]
**Accion**: [que se hizo exactamente]
**Verificacion**: [como se confirmo]
**Rollback aplicado**: [si/no, y como]
**Riesgo**: [BAJO/MEDIO/ALTO]
```

---

## PROHIBIDO (extension del v1.0)

- Tocar `src/app/page.tsx` (landing)
- Tocar `src/components/landing/*` (componentes landing)
- Tocar `src/app/(public)/*` (rutas publicas)
- Tocar `src/app/login/page.tsx` y `registro` (auth pages)
- Hacer `git push --force`
- Borrar archivos sin backup
- Tocar el `.next/` del release bueno (s4Hs00UH)
- **Hacer rebuild del frontend (cambia BUILD_ID)**
- **Re-deployar LanguageSelector (cambia BUILD_ID)**
- **Activar AdminSwitch del stash (cambia BUILD_ID)**
- **Activar Sentry/PostHog sin credenciales del usuario**

---

## RESULTADO ESPERADO (version 2.0)

Despues de ejecutar este MASTER_TASK.md con MiniMax M2.7:

1. ✅ Snapshot de seguridad pre-cambios
2. ✅ Sistema con backups automaticos a las 3 AM UTC
3. ✅ Healthcheck cada 5 minutos con alertas
4. ✅ Bug maintenance corregido (endpoints funcionan)
5. ✅ /healthz devuelve checks detallados (DB+Redis+Ollama)
6. ✅ Gap admin frontend documentado
7. ✅ Sentry y PostHog verificados (siguen sin activar)
8. ✅ Landing `s4Hs00UHv6esTNBt7xcUp` INTACTA
9. ✅ AdminSwitch en stash (NO activado)
10. ✅ Trazabilidad completa en MASTER_LOG.md
11. ✅ Estado actualizado en MASTER_STATE.md

---

**Version**: 2.0
**MiniMax M2.7 compatible**: SI
**Sin tocar la landing**: CONFIRMADO (BUILD_ID se mantiene)
**Reversible**: SI (cada task tiene rollback explicito)
**Auditado**: 2026-07-06 contra repo y VPS real