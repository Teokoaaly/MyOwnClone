# DOCUMENTACIÓN PREVENTIVA — MyOwnClone

> Versión: 1.0
> Fecha: 2026-07-05
> Mantenido por: LLM agente (auditoría continua)

---

## 1. CAUSA ORIGEN DE LOS PROBLEMAS

### 1.1 ¿Por qué el login NextAuth daba `?error=Configuration`?

**Causa raíz**: El regex de validación de bcrypt en `platform-admin.ts` esperaba hashes que terminaran en `$` literal. Pero bcrypt genera hashes que terminan en `.`. **Ningún hash bcrypt estándar** podía pasar el regex. **El login NextAuth nunca funcionó de forma robusta** desde el inicio — solo funcionaba el path de DB (consulta tabla `users` con `bcrypt.compare`).

**Señales tempranas que lo habrían detectado**:
- Tests E2E del login fallando desde la primera implementación
- Mensaje de error en logs: `isPlatformAdminEnvMisconfigured`

**Fix**: El regex debe aceptar `.` o `$` al final. Lo correcto es `^\$2[aby]\$\d{2}\$[./A-Za-z0-9]{53}\.?$`.

### 1.2 ¿Por qué la `myownclone_api` salía como UNHEALTHY?

**Causa raíz**: El healthcheck de Docker corría `curl /readyz`. El endpoint `/readyz` requería que la conexión a Redis estuviera viva. Redis estaba configurado con TLS en puerto 6380, pero el compose del release activo (creado con un compose anterior) tenía Redis sin TLS en puerto 6379. Las versiones del compose y del contenedor Redis no coincidían.

**Señales tempranas**:
- `docker ps` muestra `(unhealthy)` junto al nombre del contenedor
- `/readyz` devuelve 503 con `redis: error: Connection reset by peer`

**Fix aplicado**: Recrear Redis desde el compose actual para que coincida con la configuración. Después `/readyz` da 200 con `redis: ok`.

### 1.3 ¿Por qué faltaba el cron de backups?

**Causa raíz**: `crontab -l` está vacío. No hay backup automático programado. La documentación menciona `ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1` pero nunca se añadió al cron.

**Fix**: Añadir `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1` al crontab.

### 1.4 ¿Por qué el BUILD_ID cambiaba entre despliegues?

**Causa raíz**: El sistema de release (`/opt/myownclone/current` symlink) apuntaba a un release diferente cada vez que un agente o un script hacía `docker compose up`. El BUILD_ID del bundle servido dependía de qué release estuviera activo. No había pinning del release.

**Fix**: El release activo ahora es `20260704222310-frontend-codex-admin` (verificado). Pero cualquier agente puede cambiar el symlink. Es importante **no tocar el symlink** sin confirmar.

---

## 2. SEÑALES TEMPRANAS DE DETECCIÓN

| Señal | Comando | Causa probable |
|---|---|---|
| Login da `Configuration` | `curl /readyz` y revisar logs del frontend | Regex de bcrypt incompatible |
| Container UNHEALTHY | `docker ps` | Healthcheck falla (DB/Redis no accesibles) |
| Login da 401 inesperado | `curl /readyz` | DB connection rota |
| Backend lento | `docker stats` | Recursos saturados (CPU/RAM) |
| Disco lleno | `df -h` | Backups sin retention o logs sin rotación |
| Cron no ejecuta | `crontab -l` | Cron vacío o comando no existe |
| `?error=Configuration` | `journalctl -u myownclone-frontend` | Config admin env incorrecta |

---

## 3. CHECKLIST PRE-DEPLOY

Antes de CUALQUIER deploy (incluyendo AdminSwitch):

- [ ] `git status` limpio
- [ ] `git log` confirma que NO se modificó `src/app/page.tsx` ni `src/components/landing/*`
- [ ] `.next/` del release anterior guardado en `/tmp/next-backup-*`
- [ ] `backend.env.production` tiene `DB_USER=myownclone_app` (no `postgres`)
- [ ] `backend.env.production` tiene `OLLAMA_BASE_URL=http://ollama:11434`
- [ ] `frontend.env.production` tiene `DATABASE_URL` con `myownclone_app`
- [ ] `frontend.env.production` NO tiene `PLATFORM_ADMIN_EMAIL/PASSWORD` (si los tiene, regex falla)
- [ ] Healthcheck antes: `curl /readyz` debe dar 200
- [ ] Backup reciente: `ls -la /opt/myownclone/backups/ | tail -5`

## 4. CHECKLIST POST-DEPLOY

Después de CUALQUIER deploy:

- [ ] `docker ps` — todos los contenedores `Up X (healthy)`
- [ ] `curl https://myownclone.com/api/healthz` — devuelve 200 con `{checks, status:"ready"}`
- [ ] `curl https://myownclone.com/api/readyz` — 200 con `{database, redis, ollama}` todos ok
- [ ] `curl -I https://myownclone.com` — 200 OK (landing)
- [ ] `curl -I https://myownclone.com/login` — 200 OK
- [ ] Login admin funciona con `MocAdmin!2026-06-24`
- [ ] AdminSwitch visible solo para platform_admin
- [ ] MASTER_LOG.md actualizado con el deploy
- [ ] `git log` confirma solo cambios esperados

---

## 5. CONTROLES AUTOMÁTICOS RECOMENDADOS

### 5.1 Healthcheck automático
Crear un cron que verifica cada 5 minutos:
```bash
*/5 * * * * /opt/myownclone/current/ops/healthcheck.sh >> /var/log/healthcheck.log 2>&1
```

`healthcheck.sh`:
```bash
#!/bin/bash
STATUS=$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:5001/readyz)
if [ "$STATUS" != "200" ]; then
    echo "$(date): ALERT: /readyz returned $STATUS"
    # Aquí se podría integrar con Sentry/PagerDuty
fi
```

### 5.2 Backup automático (si no está ya)
```bash
0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1
```

### 5.3 Watchdog del symlink
El release activo puede cambiar silenciosamente. Script de verificación:
```bash
*/30 * * * * if [ ! -L /opt/myownclone/current ]; then echo "ALERT: symlink current lost"; fi
```

---

## 6. PROCEDIMIENTO DE ROLLBACK

### Rollback de AdminSwitch
```bash
cd /opt/myownclone
# Ver el commit antes de AdminSwitch
git log --oneline | head -5
# Revertir al commit anterior
git checkout HEAD~1 -- MyOwnClone/src/components/dashboard/AdminSwitch.tsx MyOwnClone/src/app/\(dashboard\)/layout.tsx MyOwnClone/src/app/admin/layout.tsx
# Rebuild
cd /opt/myownclone/current/MyOwnClone
rm -rf .next && npm run build
# Deploy
cp -a .next /opt/myownclone/releases/$(date +%Y%m%d%H%M%S)-admin-switch-revert
# Restart
systemctl restart myownclone-frontend
```

### Rollback de Redis (compose)
```bash
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml up -d --force-recreate redis
# Verificar
docker exec myownclone_redis redis-cli ping
```

### Rollback de Correcciones de config
```bash
# Restaurar el .env de antes
git checkout HEAD~1 -- /opt/myownclone/shared/backend.env.production
# O restaurar el compose
git checkout HEAD~1 -- /opt/myownclone/current/ops/docker-compose.backend.prod.yml
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml up -d --force-recreate
```

---

## 7. PROCEDIMIENTO DE RECUPERACIÓN DE ACCESO

### Si el login admin falla (olvidé la contraseña)
```bash
# Conectar al VPS
ssh root@212.227.169.99

# Resetear la password de admin@myownclone.com
NEW_PASSWORD="TuPasswordNuevo!"
HASH=$(docker exec myownclone_api python3 -c "
import bcrypt
print(bcrypt.hashpw('$NEW_PASSWORD'.encode(), bcrypt.gensalt(rounds=12)).decode())
")

# Crear archivo SQL
echo "UPDATE accounts SET password = '$HASH' WHERE email = 'admin@myownclone.com';" > /tmp/reset.sql
echo "UPDATE users SET password_hash = '$HASH' WHERE email = 'admin@myownclone.com';" >> /tmp/reset.sql

# Aplicar
docker cp /tmp/reset.sql myownclone_postgres:/tmp/reset.sql
docker exec myownclone_postgres psql -U postgres -d myownclone -f /tmp/reset.sql
```

### Si el frontend no responde
```bash
ssh root@212.227.169.99
systemctl status myownclone-frontend
journalctl -u myownclone-frontend -n 50 --no-pager

# Si el .next está corrupto, restaurar del backup
rm -rf /opt/myownclone/current/MyOwnClone/.next
cp -a /tmp/next-backup-* /opt/myownclone/current/MyOwnClone/.next
chown -R myownclone:myownclone /opt/myownclone/current/MyOwnClone/.next
systemctl restart myownclone-frontend
```

### Si el backend no arranca
```bash
ssh root@212.227.169.99
docker logs --tail 50 myownclone_api

# Recrear contenedor
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml up -d --force-recreate api
```

---

## 8. ADMINSWITCH — USO Y EXTENSIÓN

### Uso actual
- **Para quién**: Solo visible para `role === 'platform_admin'`
- **Desde dashboard**: Click "Vista Backend" → navega a `/admin/resumen`
- **Desde admin**: Click "Vista Dashboard" → navega a `/resumen`
- **Sin reauth**: La sesión se mantiene
- **Sin recargar**: El state se preserva

### Extensión a nuevos roles (futuro)
Si se quiere añadir el switch a un nuevo rol (ej. `tenant_owner`):

```typescript
// En AdminSwitch.tsx
const isAdminView = pathname?.startsWith("/admin") ?? false;

// En el layout
{isPlatformAdminSession(session) && <AdminSwitch target="admin" />}
```

### Revocación (si se quiere quitar)
1. Borrar el componente: `rm MyOwnClone/src/components/dashboard/AdminSwitch.tsx`
2. Revertir los imports en los layouts
3. Rebuild + deploy

### Auditoría
Para añadir log de auditoría (cuándo un admin entra al backend), se puede hacer:
```typescript
// En un useEffect del AdminSwitch
useEffect(() => {
    fetch("/api/admin/audit", {
        method: "POST",
        body: JSON.stringify({ event: "view_switch", from: pathname, to: href })
    });
}, [pathname]);
```

---

## 9. REGLA PERMANENTE: FRONTEND/LANDING NUNCA SE TOCA

Esta regla es **innegociable**. Razones:

1. **El diseño está aprobado** y validado por el usuario
2. **Cambiar la landing puede romper** el flujo de conversión
3. **El test de regresión** del frontend es costoso
4. **El release activo** tiene un frontend validado
5. **Otros agentes** pueden hacer deploys concurrentes

### Archivos que NUNCA se deben tocar (sin aprobación explícita)
- `MyOwnClone/src/app/page.tsx` (landing principal)
- `MyOwnClone/src/components/landing/*` (componentes de landing)
- `MyOwnClone/src/app/(public)/*` (rutas públicas)
- `MyOwnClone/src/app/login/page.tsx` y `registro` (páginas de auth)
- Archivos en `MyOwnClone/.next/` (build artifacts)
- `MyOwnClone/public/*` (assets estáticos)

### Excepciones
Solo si el usuario lo autoriza explícitamente. En ese caso:
1. Documentar el cambio en MASTER_LOG.md
2. Hacer backup del estado anterior
3. Probar en staging primero
4. Tener un plan de rollback

---

## 10. SINCRONIZACIÓN CORRECTA DE RAMAS

### Estado actual de ramas
- `master`: documentación
- `docs/planes-maestros`: planes de las 3 fases (FASE 1, 2, 3) + AdminSwitch
- `sisyphus/anti-forget-layer`: rama de features de Sisyphus (no en uso activo)
- `i18n/exec-en-es`: rama i18n (NO en uso, hubo un revert en mayo)

### Procedimiento para merge a master
1. Verificar que el release está estable 48h
2. Actualizar `MASTER_STATE.md` con el cambio
3. PR a `master` con descripción detallada
4. NO force-push
5. Verificar CI/CD pasa
6. Merge solo después de review explícito

### Procedimiento para crear nueva rama
1. Branch desde `master` actualizado
2. NUNCA desde un release desactualizado
3. Nombre descriptivo (`feat/admin-switch`, `fix/redis-tls`, etc.)
4. Push al fork del VPS (no al repo principal del usuario)

---

## 11. CHECKLIST DE EMERGENCIA

Si el VPS se rompe completamente:

1. **Snapshot del estado actual**: `cp -a /opt/myownclone /tmp/snapshot-$(date +%s)`
2. **Verificar backups**: `ls -la /opt/myownclone/backups/`
3. **Restaurar último release conocido funcional**: `20260704222310-frontend-codex-admin` (AdminSwitch)
4. **Si necesitas restaurar DB**: `gunzip -c /opt/myownclone/backups/<file>.sql.gz | docker exec -i myownclone_postgres psql -U postgres -d myownclone`
5. **Reiniciar todo**: `systemctl restart myownclone-frontend && cd /opt/myownclone/current/ops && docker compose up -d`
6. **Verificar**: `curl https://myownclone.com/api/readyz` debe dar 200

---

## 12. PROCEDIMIENTO DE BACKUP Y RESTAURACIÓN

### Backup actual
- Cron: `0 3 * * * /opt/myownclone/current/ops/backup_postgres.sh 7 >> /var/log/myownclone-backup.log 2>&1`
- Ubicación: `/opt/myownclone/backups/`
- Retention: 7 días
- Local: `/var/backups/myownclone/` (script `backup_dual.sh`)

### Backup off-site (futuro)
- Recomendado: rclone + S3 / B2
- Cron: `0 4 * * * rclone copy /var/backups/myownclone/ myownclone:backups/`
- Cuando se configure el credential, seguir pasos en TASK-D01 de PLAN_MAESTRO.md

### Restauración
```bash
# 1. Listar backups
ls -la /opt/myownclone/backups/ /var/backups/myownclone/

# 2. Verificar integridad (tamaño, fecha)
LATEST=$(ls -t /opt/myownclone/backups/myownclone_*.sql.gz | head -1)
echo "Restaurando: $LATEST"

# 3. Detener el backend para evitar conflictos
cd /opt/myownclone/current/ops
docker compose -f docker-compose.backend.prod.yml stop api

# 4. Restaurar
gunzip -c $LATEST | docker exec -i myownclone_postgres psql -U postgres -d myownclone

# 5. Reiniciar backend
docker compose -f docker-compose.backend.prod.yml up -d api
```

---

## 13. FIRMA DIGITAL DE CAMBIOS

Para cada cambio importante, agregar a MASTER_LOG.md:

```
## [YYYY-MM-DD HH:MM UTC] — [TASK-ID] [STATUS]
**Tarea**: [descripción corta]
**Cambio**: [qué se hizo exactamente]
**Archivos**: [lista de archivos modificados]
**Verificación**: [cómo se confirmó que funciona]
**Rollback**: [cómo deshacer si es necesario]
**Riesgo**: [BAJO/MEDIO/ALTO] + razón
**Tiempo**: [X min]
```

---

## 14. CONTACTOS Y RUTAS CRÍTICAS

| Servicio | URL | Estado |
|---|---|---|
| Landing | https://myownclone.com | ✅ INTACTA |
| Login | https://myownclone.com/login | ✅ |
| Dashboard | https://myownclone.com/resumen | ✅ |
| Admin | https://myownclone.com/admin/resumen | ✅ |
| API healthcheck | https://myownclone.com/api/readyz | ✅ |
| VPS SSH | ssh root@212.227.169.99 | ✅ |
| Repo | git@github.com:Teokoaaly/MyOwnClone.git | ✅ |
| Release activo | /opt/myownclone/releases/20260704222310-frontend-codex-admin | ✅ |

---

## 15. RESUMEN FINAL

- **Total tareas pendientes**: 9 (de 16)
- **Tareas críticas**: 3 (verificaciones de AdminSwitch, backups, deploy)
- **Tiempo total**: 4-6 horas
- **Riesgos**: BAJOS (cambios mínimos, todos reversibles)
- **Frontend/landing**: PROTEGIDO — no se tocó
- **AdminSwitch**: IMPLEMENTADO, falta verificación E2E
- **Correcciones**: Redis arreglado, faltan /healthz y cron
- **Documentación**: PLAN_MAESTRO.md y este archivo

---

**Última actualización**: 2026-07-05
**Mantenedor**: LLM agente (auditoría continua)
**Próxima revisión recomendada**: tras cualquier deploy o incidente
