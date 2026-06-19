# AUDIT_REPORT_VPS.md

Fecha de auditoria: 2026-06-19
Alcance: VPS de produccion `myownclone-vps` (212.227.169.99 / Tailscale 100.125.128.116)
Metodo: inspeccion por SSH (`ssh myownclone-vps`) sobre host, kernel, red, Docker, app, PostgreSQL, nginx/TLS, backups y observabilidad.
Secretos: NO se exfiltraron valores; las claves se reportan solo por presencia/longitud o, cuando estaban en texto plano en config, se marcan para rotacion sin reproducirlas.

---

## 1. Resumen ejecutivo

El VPS mantiene la aplicacion MyOwnClone funcional y atendiendo trafico HTTPS: frontend Next.js 16 detras de nginx, backend Flask/Gunicorn en Docker, PostgreSQL 15 + pgvector, Redis. Los healthchecks principales responden (`/healthz`, `/readyz`, frontend HTTP 200) y la base de datos esta en la migracion head esperada (`c3d4e5f6a7c1`).

Sin embargo, la auditoria detecta **6 hallazgos criticos de seguridad** que deben cerrarse antes de considerar el entorno endurecido para produccion publica. El mas urgente es un **servidor de archivos Python ejecutandose como root y abierto a internet en el puerto 9999** que esta sirviendo el contenido de `/tmp`, incluyendo scripts con patrones de credenciales (`inject_token.py`) y cabeceras de autenticacion capturadas (`moc-login-headers.txt`). A esto se suman: ausencia total de firewall y fail2ban, SSH con login root y password habilitados, una **API key en texto plano dentro de la config de nginx**, inyeccion fija de `X-User-Role: owner` para el area admin, ausencia de security headers y **ningun backup programado**.

Estado estimado de **endurecimiento/higiene**: ~55%. La aplicacion corre, pero la superficie de ataque es amplia y hay secretos expuestos que conviene rotar.

---

## 2. Inventario del host

| Item | Valor |
|---|---|
| Hostname / SO | `ubuntu` / Ubuntu 26.04 LTS (resolute) |
| Kernel / arch | Linux 7.0.0-22-generic / x86_64 |
| Virtualizacion | KVM (VPS cloud) |
| CPU | 2 vCPU AMD EPYC-Milan |
| Memoria | 3.8 GiB (uso ~1.3 Gi, swap 2 Gi con ~280 Mi usados) |
| Disco | 116 Gi en `/` (36% usado, 75 Gi libres) |
| TZ / NTP | Etc/UTC / sincronizado, NTP activo |
| Uptime | 3 dias, 20 h (load avg 0.41/0.33/0.34) |
| Docker | 29.1.3, root dir `/var/lib/docker` (962 Mi), driver overlayfs |
| Usuarios shell | `root` (uid 0), `myownclone` (uid 997, **sin sudo**) |
| Sudoers | grupo `sudo` vacio, grupo `admin` vacio |
| Unattended upgrades | habilitadas |

Usuarios con acceso real: solo `root` (vía SSH por llave). No hay cuentas compartidas con sudo adicionales.

---

## 3. Superficie de red (puertos a la escucha)

| Puerto | Bind | Proceso | Exposicion | Riesgo |
|---|---|---|---|---|
| 22 | 0.0.0.0 / [::] | sshd | **Publico** | Alto (root+password ON, ver SEC-04) |
| 80 | 0.0.0.0 / [::] | nginx | Publico (redirect HTTPS) | OK |
| 443 | 0.0.0.0 / [::] | nginx | Publico | OK |
| 3000 | **0.0.0.0** | next-server (Next 16.2.9) | **Publico directo** | Medio (byassable de nginx) |
| 9999 | **0.0.0.0** | python3 `-m http.server` (root) | **Publico directo** | **Critico** (SEC-01) |
| 5432 | 127.0.0.1 | postgres (docker-proxy) | Loopback | OK |
| 6379 | 127.0.0.1 | redis (docker-proxy) | Loopback | OK |
| 5001 | 127.0.0.1 | gunicorn API (docker-proxy) | Loopback | OK |
| 8080 | 127.0.0.1 | weaviate (docker-proxy) | Loopback | OK |
| 36735 | 100.125.128.116 | tailscaled | Tailscale | OK |

---

## 4. Hallazgos criticos (P0)

### SEC-01 | Critica | Servidor de archivos Python como root, abierto a internet
- **Ubicacion**: proceso `python3 -m http.server 9999` (PID 1579263, ppid=1/systemd, huérfano).
- **CWD servido**: `/tmp` — listado de directorio publico, sin auth, solo lectura.
- **Exposicion**: escucha en `0.0.0.0:9999` (sin firewall → alcanzable desde internet/Tailscale).
- **Inicio**: 2026-06-18 10:38, sin unidad systemd (lanzado a mano, probablemente por herramienta de automatizacion).
- **Contenido sensible servido** (deteccion por patrones, valores no extraidos):
  - `inject_token.py` — 9 coincidencias de patrones tipo secret/token/password/api_key.
  - `moc-login-headers.txt` — 2 coincidencias authorization/set-cookie/token.
  - `cookies.txt` (131 B), `audit-fix.py`, mockups de login HTML.
- **Impacto**: fuga de credenciales/scripts internos → pivot a admin (combinable con SEC-02/SEC-03).
- **Remediacion**: matar el proceso `kill 1579263`; verificar que no quede reiniciandose; limpiar `/tmp` de scripts y mocks; nunca volver a exponer `http.server` a `0.0.0.0`.

### SEC-02 | Critica | API key de servicio en texto plano en config de nginx
- **Ubicacion**: `/etc/nginx/sites-enabled/myownclone`, bloque `location /api/admin/`.
- **Detalle**: cabecera fija `proxy_set_header X-API-Key "<valor_en_claro>"`. El valor coincide en longitud con un `SERVICE_API_KEY` (48 chars) definido en `/opt/myownclone/shared/backend.env.production`.
- **Impacto**: el archivo es legible por root y queda en backups/config versionable; si se filtra (p.ej. via SEC-01), habilita llamadas admin al backend.
- **Remediacion**: mover la clave a una variable del env de nginx (`/etc/nginx/myownclone.env`, permisos 0600) cargada con `envsubst`/`include`, o inyectarla desde el backend; **rotar** el valor tras corregir.

### SEC-03 | Critica | nginx inyecta identidad de admin fija (`X-User-Role: owner`)
- **Ubicacion**: mismo bloque `location /api/admin/`.
- **Detalle**: nginx fija `X-User-Id`, `X-User-Role: owner`, `X-User-Email` para **todas** las peticiones a `/api/admin/`. El backend confía en esas cabeceras (combinado con `X-API-Key`).
- **Impacto**: cualquier poseedor de la API key (SEC-02) opera como owner de plataforma sin autenticacion de usuario real. Falta un factor de identidad verificable (sesion/JWT firmado validado por el backend).
- **Remediacion**: que el backend derive identidad del JWT/cookie de sesion (NextAuth), no de cabeceras inyectadas por nginx; conservar `X-API-Key` solo como secreto de servicio mutuo, no como portador de identidad.

### SEC-04 | Critica | SSH debil + sin firewall + sin fail2ban
- **sshd efectivo**: `PermitRootLogin yes`, `PasswordAuthentication yes`, `MaxAuthTries 6`, `X11Forwarding yes`, puerto 22.
- **Firewall**: UFW `inactive`, firewalld ausente, iptables con policy por defecto ACCEPT (36 reglas -A, mayormente docker).
- **IPS**: fail2ban no instalado.
- **Impacto**: superficie de fuerza bruta sobre root a internet, y ningun servicio de los escuchando en `0.0.0.0` (22, 3000, 9999) tiene filtrado.
- **Remediacion**:
  1. `PermitRootLogin prohibit-password` (o `no` + login por usuario con llave), `PasswordAuthentication no`.
  2. Habilitar UFW: permitir 22, 80, 443 (y Tailscale); **negar** 3000 y 9999 al exterior.
  3. Instalar fail2ban con jail `sshd`.

### SEC-05 | Critica | Sin backups programados
- **Estado**: ningun cron (root ni usuario), ningun script en `/etc/cron.*`. Unico dump existente: `/root/myownclone/backups/myownclone_before_alembic_stamp.dump` (manual, puntual).
- **`pg_dump`** disponible en el contenedor postgres.
- **Impacto**: perdida irrecuperable ante borrado/corrupcion/ransomware.
- **Remediacion**: cron diario `pg_dump` (comprimido, rotado), copia offsite (S3/B2/restic) y test de restauracion.

### SEC-06 | Alta | Ausencia de security headers HTTP
- **Estado**: `https://212.22.169.99/` no devuelve HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy ni Permissions-Policy.
- **Remediacion**: anadirlos en el `server` 443 de nginx (`add_header ... always`).

---

## 5. Hallazgos altos/medios (P1/P2)

### APP-01 | Alta | Drift entre repos local, bootstrap del VPS y release actual
- **Repo local** (rama `audit/vps-sync-and-docs`): HEAD `a1df523`.
- **VPS `/opt/myownclone/bootstrap`** (mismo remote `github.com:Teokoaaly/MyOwnClone.git`, misma rama): HEAD `c0808ce` “feat: resource limits, Redis TLS, network isolation, Weaviate healthcheck”.
- **Release en curso** (`current` → `20260617185014-frontend-landing-restore`): anterior al HEAD del bootstrap; **sin `.git`** dentro (copia, no checkout).
- **Impacto**: imposible auditar drift commit a commit contra lo que corre; riesgo de desplegar estados no versionados.
- **Remediacion**: estandarizar deploy por commit/tag; que cada release lleve su `.git` o un fichero `REVISION`.

### APP-02 | Alta | Integraciones de pago/IA/email sin configurar (env vacios)
Valores vacios en `backend.env.production`: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `SENDGRID_INBOUND_WEBHOOK_SECRET`, `WHEREBY_API_KEY`, `TOGETHER_API_KEY`, `RESEND_*`(solo frontend con valor), Google OAuth, PostHog, Sentry, Supabase. Y en frontend: `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`, price IDs.
- Configurados: MiniMax (LLM), Resend (frontend), DB/Redis/Weaviate/JWT.
- **Impacto**: billing, OAuth y varios canales no operativos en produccion.
- **Remediacion**: completar con valores de sandbox primero, validar flujos, rotar todo lo expuesto via SEC-01/SEC-02.

### OPS-01 | Media | 27 releases acumulados (~24 GiB) + 2 GiB de build cache
- `/opt/myownclone/releases` = 24 GiB de 116 GiB. Varias releases de >1 GiB.
- `docker builder` cache: 2.03 GiB reclaimable.
- **Remediacion**: retener solo las ultimas 3-5 releases; `docker builder prune`; cron de limpieza.

### OPS-02 | Media | Weaviate marcado unhealthy e imagen obsoleta
- Contenedor `myownclone_weaviate`: `unhealthy`, imagen `weaviate:1.24.0` (de hace ~2 anios). Arranca y atiende `/ready` (vacio), pero el healthcheck del compose falla.
- **Remediacion**: revisar el comando `healthcheck` (probablemente `PING`/ready endpoint); planear upgrade de version mayor con prueba de schema.

### OPS-03 | Media | Logging de contenedores sin limite
- Driver `json-file` sin `max-size`/`max-file` → los logs crecen sin bound. Hoy pequeños (max 508 Ki) pero sin proteccion.
- **Remediacion**: `/etc/docker/daemon.json` con `log-opts` globales o por servicio en el compose.

### OPS-04 | Media | Observabilidad ausente
- Sin `node_exporter`/Prometheus; Sentry/PostHog mencionados en el frontend env pero con valor vacio (no enviarian telemetria).
- `journalctl` ocupa 96 MiB.
- **Remediacion**: definir metricas minimas (CPU/disco/p95) y captura de errores; rotar journald (`SystemMaxUse=200M`).

### OPS-05 | Baja | 2 actualizaciones pendientes
- `update-notifier-common`, `nodejs` (revisar changelog de nodejs por CVEs).
- **Remediacion**: `apt update && apt upgrade` en ventana de mantenimiento.

### OPS-06 | Baja | server_name incluye la IP cruda
- nginx responde a `212.227.169.99 myownclone.com www.myownclone.com`; acceder por IP genera mismatch de cert.
- **Remediacion**: dejar solo los dominios; redirigir IP a un host canónico si hace falta.

---

## 6. Lo que esta correcto

- Aplicacion sirviendo HTTPS con certificado Let's Encrypt valido (vence 2026-09-13, 86 dias; renovacion via certbot presente).
- Redirect HTTP → HTTPS correcto; `nginx -t` pasa.
- Backend `/healthz` ok y `/readyz` ok (database + redis).
- Frontend responde 200; gestionado por **systemd** (`myownclone-frontend.service`, `npm run start`).
- Backend en Docker compose `ops` con `restart: unless-stopped`, 0 reinicios, contenedores healthy (api/postgres/redis).
- PostgreSQL 15.18 con **pgvector 0.8.2** y **uuid-ossp 1.1**, en head `c3d4e5f6a7c1` (consistente con el repo).
- DB pequeña (9 MiB, datos seed), 8 conexiones, sin saturacion.
- Servicios de datos (postgres/redis/weaviate/api) **solo en loopback**.
- `unattended-upgrades` activo; `PermitEmptyPasswords no`, `PermitUserEnvironment no`, `PubkeyAuthentication yes`.
- Esquema de deploy tipo capistrano (`releases/current/shared`) correcto en concepto; `current` es symlink.

---

## 7. Plan de remediacion priorizado

**Inmediato (hoy, antes de cualquier otra cosa):**
1. Cerrar SEC-01: `kill 1579263`, confirmar que no reaparece, limpiar `/tmp`.
2. Bloquear 9999 y 3000 al exterior (UFW) — esto contiene SEC-01 aunque se relance.
3. Rotar el `SERVICE_API_KEY` expuesto en nginx (SEC-02) y el `X-User-Id`/`SERVICE_API_KEY` del backend.

**Corto plazo (esta semana):**
4. SEC-04: hardening SSH (`prohibit-password`, `PasswordAuthentication no`) + UFW + fail2ban.
5. SEC-03: mover la identidad de admin del header inyectado al JWT/cookie firmado.
6. SEC-05: backups diarios de postgres + copia offsite + test de restore.
7. SEC-06: security headers en nginx.

**Medio plazo:**
8. APP-01: deploy por commit/tag con `REVISION` por release.
9. APP-02: completar integraciones en sandbox y validar.
10. OPS-01..04: retencion de releases, prune de Docker, limite de logs, metricas minimas, upgrade de Weaviate.

---

## 8. Estado global

| Dimension | Estado | Notas |
|---|---|---|
| Disponibilidad app | OK | HTTPS funcional, healthchecks verdes |
| Base de datos | OK | Migracion head correcta, pgvector activo |
| Seguridad perimeter | **Critica** | Sin firewall, SSH debil, 9999 expuesto |
| Gestion de secretos | **Critica** | API key en claro en nginx |
| Backups | **Critica** | Ninguno programado |
| Hardening HTTP | Deficiente | Sin security headers |
| Observabilidad | Deficiente | Sin metricas/errores |
| Higiene de deploy | Media | Drift + 27 releases acumuladas |

**Recomendacion**: cerrar los 6 P0 (SEC-01 a SEC-06) antes de seguir agregando funcionalidad o dar por buena la instancia como produccion publica.
