# VPS Hardening Runbook (2026-06-19)

Guía operativa de los parches de seguridad aplicados al VPS de producción
`myownclone-vps` (212.227.169.99). Aplicada tras la auditoría registrada en
`AUDIT_REPORT_VPS.md`.

Cada sección describe **qué se cambió**, **dónde**, y **cómo revertirlo**.

---

## P0-1 · Cierre del servidor de archivos en :9999

**Problema**: `python3 -m http.server 9999` corría como root en `0.0.0.0:9999`
sirviendo `/tmp` (scripts con credenciales, cabeceras de auth capturadas).

**Acción**:
- `kill` del proceso (PID huérfano, ppid=1).
- Limpieza de `/tmp/inject_token.py`, `moc-login-headers.txt`, `cookies.txt`, etc.
- Snapshot seguro de los scripts en `/root/audit-tmp-snapshot/` (permisos 600).
- El puerto 9999 queda además bloqueado por UFW (P0-2).

**Revertir**: no procede (era un riesgo activo).

---

## P0-2 · Hardening SSH + UFW + fail2ban

**SSH** — drop-in `/etc/ssh/sshd_config.d/40-audit-hardening.conf` (prefijo `40-`
para que cargue **antes** que `50-cloud-init.conf`, que fijaba
`PasswordAuthentication yes` por first-match-wins):

```
PermitRootLogin prohibit-password
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
X11Forwarding no
AllowAgentForwarding no
AllowTcpForwarding no
```

**UFW** — activado con default deny incoming, permite solo 22/80/443.
Los puertos 3000 (Next.js) y 9999 ya no son alcanzables desde internet.

**fail2ban** — instalado, jail `sshd` activa (bantime 1h, maxretry 5).

**Backups**: `/root/audit-backups/sshd-YYYYMMDD/`.

**Revertir UFW**: `sudo ufw disable`.
**Revertir SSH**: `sudo rm /etc/ssh/sshd_config.d/40-audit-hardening.conf && sudo systemctl reload ssh`.

---

## P0-3+04 · nginx: rotación de API key, fin del bypass de admin, security headers

**Problema**: el `location /api/admin/` de nginx inyectaba un `X-API-Key`
hardcodeado en claro y `X-User-Role: owner` fijo, saltándose la validación
NextAuth que hace `src/proxy.ts`. Eso permitía a quien tuviera la API key
operar como admin sin sesión real.

**Acción**:
- **Rotada** `SERVICE_API_KEY` (48 chars) en:
  - `/opt/myownclone/shared/backend.env.production`
  - `/opt/myownclone/shared/frontend.env.production` (`SERVICE_API_KEY` + `MYOWNCLONE_SERVICE_API_KEY`)
  - `/opt/myownclone/current/ops/backend.env.production` (copia que lee el compose)
- **nginx reescrito** (`ops/nginx.myownclone.conf.example` es la referencia):
  - Eliminados los bloques que inyectaban identidad: `/api/admin/`, `/api/auth/login`, `/api/myownclone/`, `/console/`.
  - Todo el tráfico va a Next.js (3000), cuyo `proxy.ts` valida NextAuth JWT e inyecta identidad real.
  - Se conservan **dos webhooks server-to-server** directos al backend (no mapeados en `proxy.ts`):
    - `/api/myownclone/public/inbound-email` (SendGrid, multipart)
    - `/api/deploy` (CI/CD)
- **Security headers** añadidos: HSTS, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, Permissions-Policy.
- Reiniciados: contenedor API (`docker compose up -d` con `--env-file`), frontend (systemd), nginx reload.

**Revertir nginx**: restaurar desde `/root/audit-backups/nginx-*/myownclone.conf.bak`.
**Revertir clave**: restaurar desde `/root/audit-backups/envs-*/`.

> ⚠️ **Importante**: la `SERVICE_API_KEY` vieja quedó registrada en logs de esta
> sesión y en backups. **Debe considerarse comprometida** y no reutilizarse.

---

## P0-5 · Backups de PostgreSQL

**Acción**:
- Script `ops/backup_postgres.sh` (pg_dump vía `docker exec`, gzip, rotación).
- Instalado en `/opt/myownclone/current/ops/backup_postgres.sh`.
- Cron diario root: `0 3 * * * .../backup_postgres.sh 7 >> /var/log/myownclone-backup.log`.
- Conserva 7 días en `/opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz`.

**Restore** (ejemplo):
```
gunzip < /opt/myownclone/backups/myownclone_YYYYMMDD_HHMMSS.sql.gz | \
  docker exec -i myownclone_postgres psql -U postgres -d myownclone
```

---

## P1 · Higiene

- **Limpieza de releases**: 27 → 5 releases retenidas (current + 4 previas). ~16 GiB liberados.
- **Docker**: `daemon.json` con `log-opts` (max-size 50m, max-file 3).
- **journald**: `/etc/systemd/journald.conf.d/size.conf` (SystemMaxUse 200M).
- **Weaviate**: healthcheck corregido de `curl` a `wget` (la imagen 1.24.0 no incluye `curl`). Ahora healthy.

---

## Verificación post-parche (2026-06-19)

| Check | Estado |
|---|---|
| HTTPS `https://myownclone.com/` | HTTP 200 |
| Backend `/healthz`, `/readyz` | ok / ready (db+redis) |
| Contenedores | 4/4 healthy |
| Security headers | HSTS, X-Frame, X-Content-Type, Referrer, Permissions |
| Puerto 9999 | cerrado |
| Puerto 3000 | bloqueado al exterior por UFW |
| SSH | prohibit-password, PasswordAuth no |
| fail2ban | activo (ya baneó IPs de fuerza bruta) |
| Backups | cron diario + dump verificado |

---

## Pendiente (fuera del alcance de estos parches)

- Completar integraciones vacías en envs (Stripe, OpenAI, SendGrid inbound secret, Google OAuth, etc.).
- Estabilizar deploy por commit/tag (el release en curso no lleva `.git`).
- Ajustar duplicado de `Strict-Transport-Security` (cosmético: el redirect HTTP y el server HTTPS ambos lo emiten vía `map`).
- Upgrade mayor de Weaviate (1.24.0 es de hace ~2 años) con prueba de schema.
