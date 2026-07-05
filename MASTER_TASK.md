# MASTER_TASK.md

> Version: 1.0
> Fecha: 2026-07-05
> Para: MiniMax M2.7 (modelo base autonomo)
> Estado: PROHIBIDO tocar la landing (BUILD_ID s4Hs00UH)

---

## OBJETIVO

Ejecutar autonomamente las tareas pendientes del PLAN_MAESTRO.md sin intervencion del usuario.
**NO se debe tocar la landing** (s4Hs00UHv6esTNBt7xcUp). Todo cambio debe ser
reversible y documentado.

---

## REGLAS INQUEBRANTABLES

1. La landing `s4Hs00UH` es INTOCABLE
2. Cada cambio se documenta en `MASTER_LOG.md`
3. El estado actual se refleja en `MASTER_STATE.md`
4. Si un comando falla, revertir inmediatamente
5. NO usar `git push --force`
6. NO borrar archivos sin backup

---

## ESTRUCTURA DEL VPS

```
/opt/myownclone/
  current -> /opt/myownclone/releases/20260704222310-frontend-codex-admin
  releases/
    20260704222310-frontend-codex-admin (ACTIVO)
    20260703190910-landing-cleanup-restore (Landing buena s4Hs00UH)
    20260701150141-backend-codex-deploy
    20260630081811-dashboard-route-fix -> 20260629144355
    20260629144355-frontend-i18n-selector
    20260629141926-i18n-manual-selector
    20260620070304-frontend-dashboard-fix (Aqui esta el backup_postgres.sh original)
  shared/ (configuracion)
  backups/ (backups de DB)
```

---

## TAREAS AUTOMATIZADAS

### TASK-A02: cron de backups

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Accion**: Configurar crontab con el script de backup que ya existe.

**Pasos**:
1. Verificar que el script `backup_postgres.sh` existe y es ejecutable:
   ```bash
   ls -la /opt/myownclone/current/ops/backup_postgres.sh
   chmod +x /opt/myownclone/current/ops/backup_postgres.sh
   ```

2. Anadir entrada al crontab (como root):
   ```bash
   echo '0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1' | crontab -
   ```

3. Crear log file:
   ```bash
   touch /var/log/myownclone-backup.log
   chmod 644 /var/log/myownclone-backup.log
   ```

4. Verificar:
   ```bash
   crontab -l
   ```

**Validacion**:
- [ ] crontab -l muestra la entrada
- [ ] log file existe y es escribible
- [ ] script de backup es ejecutable

---

### TASK-B05: AdminSwitch build + deploy + test

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Advertencia**: ESTA TAREA REQUIERE REBUILD DEL FRONTEND.
Solo ejecutar si el usuario aprueba explicitamente.

**Cambios en stash** (NO commiteados):
- `MyOwnClone/src/components/dashboard/AdminSwitch.tsx` (nuevo)
- `MyOwnClone/src/app/(dashboard)/layout.tsx` (modificado)
- `MyOwnClone/src/app/admin/layout.tsx` (modificado)

**Pasos**:
1. `git stash list` (verificar que esta el stash)
2. `git stash pop` (traer cambios al working tree)
3. Verificar que `s4Hs00UH` es la version que se va a construir
4. `cd /opt/myownclone/current/MyOwnClone`
5. `rm -rf .next node_modules/.cache`
6. `npm run build` (tarda 2-5 min)
7. Verificar que `s4Hs00UH` se mantiene y que el build NO cambia la landing
8. Reiniciar frontend: `systemctl restart myownclone-frontend`
9. Test E2E: login admin y verificar AdminSwitch en dashboard
10. Si todo funciona, commit y push

**Validacion**:
- [ ] BUILD_ID se mantiene en `s4Hs00UH`
- [ ] Landing visible sin animaciones, sin precios
- [ ] AdminSwitch visible solo para platform_admin
- [ ] Login funciona con `MocAdmin!2026-06-24`

---

### TASK-C02: /healthz detallada

**Estado**: PENDIENTE
**Prioridad**: MEDIO
**Accion**: Modificar el endpoint /healthz para devolver los checks detallados.

**Cambio en el codigo**: `/opt/myownclone/current/api/app_factory.py`

**Localizar la funcion healthz** (probablemente similar a `return jsonify({"status": "ok"})`).

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
        checks["database"] = f"error: {exc}"
        all_ok = False
    # Redis (mTLS)
    try:
        client = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", "6379")),
            password=os.getenv("REDIS_PASSWORD") or None,
            socket_connect_timeout=1.0,
            socket_timeout=1.0,
            ssl=os.getenv("REDIS_TLS", "false").lower() == "true",
            ssl_cert_reqs="required",
            ssl_ca_certs="/etc/redis/tls/ca.crt",
            ssl_certfile="/etc/redis/tls/redis.crt",
            ssl_keyfile="/etc/redis/tls/redis.key",
        )
        client.ping()
        checks["redis"] = "ok"
    except Exception as exc:
        checks["redis"] = f"error: {exc}"
        all_ok = False
    # Ollama
    try:
        import requests
        r = requests.get("http://ollama:11434/api/tags", timeout=2)
        checks["ollama"] = "ok" if r.status_code == 200 else f"error: HTTP {r.status_code}"
    except Exception as exc:
        checks["ollama"] = f"error: {exc}"
    return jsonify({"status": "ready" if all_ok else "degraded", "checks": checks}), 200 if all_ok else 503
```

**Validacion**:
- [ ] `curl /healthz` devuelve JSON con checks detallados
- [ ] Reiniciar API: `docker compose -f docker-compose.backend.prod.yml restart api`
- [ ] Probar el endpoint

---

### TASK-C03: healthcheck automatico (TASK-A02 + C02 combinados)

**Estado**: PENDIENTE
**Prioridad**: ALTO
**Accion**: Crear script de healthcheck automatico que verifica el sistema cada 5 minutos.

**Crear**: `/opt/myownclone/current/ops/healthcheck.sh`

```bash
#!/bin/bash
LOG=/var/log/myownclone-healthcheck.log
ST=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001/readyz)
NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "$ST" != "200" ]; then
    echo "$NOW ALERT readyz=$ST" >> $LOG
    # Aqui iria notificacion a Sentry/Slack si se configura
fi
```

**Anadir al crontab**:
```bash
echo '*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh' | crontab -
```

**Validacion**:
- [ ] script creado y ejecutable
- [ ] crontab configurado
- [ ] log file existe

---

### TASK-D01: Sentry (preparar)

**Estado**: PENDIENTE (espera DSN del usuario)
**Prioridad**: BAJA
**Accion**: Solo preparar el codigo, sin activar.

**Verificar** que `/opt/myownclone/current/api/app_factory.py` tenga:
```python
if sentry_dsn:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration
    # ... init Sentry
```

**Validacion**:
- [ ] Codigo de Sentry presente
- [ ] NO activar (espera DSN del usuario)

---

### TASK-D02: PostHog (preparar)

**Estado**: PENDIENTE (espera API key)
**Prioridad**: BAJA
**Accion**: Solo verificar que el codigo soporta PostHog.

**Verificar**:
```bash
grep -r 'posthog\|PostHogProvider' /opt/myownclone/current/MyOwnClone/src/lib/auth.ts
```

**Validacion**:
- [ ] PostHog esta en la configuracion de NextAuth
- [ ] NO activar (espera key del usuario)

---

## SCRIPT MAESTRO DE EJECUCION

Para que MiniMax M2.7 ejecute todo automaticamente, este es el orden:

```bash
# PASO 1: Confirmar estado del VPS
ssh root@212.227.169.99 "
  readlink /opt/myownclone/current
  cat /opt/myownclone/current/MyOwnClone/.next/BUILD_ID
  curl -sI https://myownclone.com | head -1
"

# PASO 2: TASK-A02 - Configurar cron de backups
ssh root@212.227.169.99 "
  chmod +x /opt/myownclone/current/ops/backup_postgres.sh
  (crontab -l 2>/dev/null | grep -v backup_postgres; echo '0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1') | crontab -
  touch /var/log/myownclone-backup.log
  chmod 644 /var/log/myownclone-backup.log
  crontab -l
"

# PASO 3: TASK-C03 - Healthcheck automatico
ssh root@212.227.169.99 '
  cat > /opt/myownclone/current/ops/healthcheck.sh << "SCRIPT"
#!/bin/bash
LOG=/var/log/myownclone-healthcheck.log
ST=\$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5001/readyz)
NOW=\$(date -u +%Y-%m-%dT%H:%M:%SZ)
if [ "\$ST" != "200" ]; then
    echo "\$NOW ALERT readyz=\$ST" >> \$LOG
fi
SCRIPT
  chmod +x /opt/myownclone/current/ops/healthcheck.sh
  (crontab -l 2>/dev/null | grep -v healthcheck.sh; echo "*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh") | crontab -
  echo "Healthcheck cron configurado"
'

# PASO 4: TASK-C02 - /healthz detallada
ssh root@212.227.169.99 "
  # Backup del codigo actual
  cp /opt/myownclone/current/api/app_factory.py /tmp/app_factory.py.backup
  # Editar el endpoint /healthz (ver seccion TASK-C02 de este doc)
  # Reiniciar API
  cd /opt/myownclone/current/ops
  docker compose -f docker-compose.backend.prod.yml restart api
"

# PASO 5: TASK-B05 - Solo si el usuario aprueba explicitamente
# NO ejecutar sin aprobacion!

# PASO 6: TASK-D01/D02 - Solo verificar
ssh root@212.227.169.99 "
  grep -E 'sentry|posthog' /opt/myownclone/current/api/app_factory.py | head -5
  grep -E 'posthog|PostHog' /opt/myownclone/current/MyOwnClone/src/lib/auth.ts | head -5
"
```

---

## CHECKLIST DE VALIDACION FINAL

Despues de ejecutar todos los pasos:

- [ ] crontab -l muestra las entradas de backup y healthcheck
- [ ] /var/log/myownclone-backup.log existe
- [ ] /var/log/myownclone-healthcheck.log existe
- [ ] /healthz devuelve JSON con checks detallados
- [ ] Backup manual funciona: /opt/myownclone/current/ops/backup_postgres.sh 7
- [ ] Frontend sigue con BUILD_ID s4Hs00UH
- [ ] Landing NO se ha tocado (verificar con `ls` de los archivos protegidos)
- [ ] AdminSwitch NO se ha activado (queda en stash)
- [ ] Sentry y PostHog siguen sin activar (espera credenciales)

---

## ARCHIVOS DE REFERENCIA

- `MASTER_STATE.md` - Estado actual del sistema
- `MASTER_LOG.md` - Trazabilidad de cambios
- `PLAN_MAESTRO.md` - Plan completo de 16 tareas
- `DOCS_PREVENTIVOS.md` - Procedimientos y señales de alerta
- `LANDING_APROBADA.md` - Confirmacion de la landing s4Hs00UH

---

## COMUNICACION

Cada cambio debe documentarse en MASTER_LOG.md con formato:
```
## [YYYY-MM-DD HH:MM UTC] - [TASK-ID]
**Tarea**: [descripcion]
**Accion**: [que se hizo]
**Verificacion**: [como se confirmo]
**Rollback**: [como deshacer]
```

---

## PROHIBIDO

- Tocar `src/app/page.tsx` (landing)
- Tocar `src/components/landing/*` (componentes landing)
- Tocar `src/app/(public)/*` (rutas publicas)
- Tocar `src/app/login/page.tsx` y `registro` (auth pages)
- Hacer `git push --force`
- Borrar archivos sin backup
- Tocar el .next del release bueno (s4Hs00UH)

---

## RESULTADO ESPERADO

Despues de ejecutar este MASTER_TASK.md con MiniMax M2.7:

1. Sistema con backups automaticos a las 3 AM UTC
2. Healthcheck cada 5 minutos con alertas
3. /healthz devuelve checks detallados
4. Landing s4Hs00UH INTACTA
5. AdminSwitch en stash (NO activado)
6. Sentry y PostHog preparados (espera credenciales)
7. Trazabilidad completa en MASTER_LOG.md
8. Estado actualizado en MASTER_STATE.md

---

**Version**: 1.0
**MiniMax M2.7 compatible**: SI
**Sin tocar la landing**: CONFIRMADO
**Reversible**: SI
