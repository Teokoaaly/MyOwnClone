# 01 - Diferencias VPS vs GitHub

Fecha: 2026-06-15  
Rama de trabajo: `audit/vps-sync-and-docs`  
Repositorio: `https://github.com/Teokoaaly/MyOwnClone`

## Alcance y estado de acceso

El 2026-06-15 el acceso SSH no interactivo al VPS `212.227.169.99` no estuvo disponible (`Permission denied (publickey,password)`). Esta tabla combina:

- Evidencia inspeccionada en el VPS durante la intervención operativa del 2026-06-14.
- Comparación contra la rama local `codex/vps-deploy-audit-fixes`, usada como base porque contiene los hotfixes ya desplegados.
- Pendientes que requieren reconexión SSH para cierre definitivo.

No se copian secretos, hashes, tokens, logs completos ni `.env` reales.

## Diferencias identificadas

| Archivo/Config | Tipo cambio | Origen | Impacto | Acción recomendada |
|---|---|---|---|---|
| `/etc/nginx/sites-enabled/myownclone` | Hotfix de configuración | VPS | `/api/admin/*`, `/api/clone/*` y `/api/*` deben pasar por Next.js para que `proxy.ts` añada `X-API-Key` y valide sesión. Antes iban directo a Flask y devolvían `401`. | Versionado como plantilla en `ops/nginx.myownclone.conf.example`; revalidar con `nginx -T` cuando vuelva SSH. |
| `/opt/myownclone/shared/frontend.env.production` | Config runtime | VPS | Contiene secretos y variables reales. `PLATFORM_ADMIN_PASSWORD_HASH` debe cargarse vía systemd, no desde `.env.production`, para evitar expansión de `$` por dotenv. | No versionar. Mantener como secreto del VPS o secret manager. Documentado en manual técnico. |
| `/opt/myownclone/current/MyOwnClone/.env.production` | Hotfix runtime | VPS | Debe ser legible por usuario `myownclone`; no debe incluir `PLATFORM_ADMIN_*` con bcrypt escapado. | Script `ops/deploy-frontend.sh` ya genera este archivo excluyendo `PLATFORM_ADMIN_*`. |
| `/opt/myownclone/current -> /opt/myownclone/releases/20260614162441-codex-plans-page` | Release activa | VPS | Producción ejecuta release de frontend con `/planes` separado de `/facturacion`. | Revalidar con SSH; registrar SHA desplegado en cada release. |
| `/opt/myownclone/shared/backend.env.production` | Config runtime | VPS | Variables reales del backend, DB, Redis, JWT, LLM, Stripe. | No versionar. Comparar solo nombres, no valores, durante próxima ventana SSH. |
| `myownclone-frontend.service` | Servicio systemd | VPS + repo | Ejecuta Next.js como usuario `myownclone` en `100.99.222.101:3000` con `EnvironmentFile=/opt/myownclone/shared/frontend.env.production`. | Mantener en `ops/myownclone-frontend.service`; revisar hardening si cambia hostname. |
| Docker backend (`myownclone_api`, `myownclone_postgres`, `myownclone_redis`, `myownclone_weaviate`) | Servicios activos | VPS | Backend Flask y dependencias corren en Docker Compose. | Mantener `ops/docker-compose.backend.prod.yml`; añadir backups automatizados. |
| `package-lock.json` | Desincronización | GitHub/repo | `npm ci` falla; despliegue usa `npm install --legacy-peer-deps`, menos reproducible. | Alta prioridad: regenerar lockfile en PR separado y volver a `npm ci`. |
| `api/.env`, `__pycache__`, `.pyc` en workspace local principal | Archivos locales no versionables | Local | Riesgo de commit accidental si se trabaja fuera del worktree limpio. | `.gitignore` ya cubre; mantener commits desde worktree limpio. |
| `/root/nginx-backups/` | Backup temporal | VPS | Backup de vhost previo durante hotfix Nginx. | Mantener fuera de sites-enabled; limpiar según política de retención. |

## Comandos de revalidación pendientes

Ejecutar cuando haya acceso SSH:

```bash
ssh root@212.227.169.99 'hostname; date -Is; readlink -f /opt/myownclone/current'
ssh root@212.227.169.99 'systemctl status myownclone-frontend --no-pager'
ssh root@212.227.169.99 'docker ps --format "{{.Names}} {{.Image}} {{.Status}}"'
ssh root@212.227.169.99 'nginx -T | sed -n "/server_name myownclone.com/,/}/p"'
ssh root@212.227.169.99 'find /etc/cron* /var/spool/cron -maxdepth 2 -type f -print 2>/dev/null'
```

