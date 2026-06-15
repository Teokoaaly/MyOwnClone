# 06 - Restauracion VPS 2026-06-15

## Resumen

El 2026-06-15 se restauro el stack de MyOwnClone en el VPS `212.227.169.99` y se dejo operativo con:

- Frontend Next.js en `127.0.0.1:3000`
- Backend Flask en `127.0.0.1:5001`
- PostgreSQL expuesto solo en loopback `127.0.0.1:5432`
- Redis activo
- Weaviate activo en `127.0.0.1:8080`
- Nginx sirviendo `http://212.227.169.99` y `https://myownclone.com`

## Infra y acceso

- Se creo acceso SSH por clave para `root` y alias local `myownclone-vps`.
- Se instalo base de sistema:
  - `git`
  - `curl`
  - `docker.io`
  - `docker-compose-plugin`
  - `nginx`
  - `certbot`
  - `python3-certbot-nginx`
  - `nodejs`
- Se dejo `/opt/myownclone/bootstrap` como repositorio Git real en rama `audit/vps-sync-and-docs`.
- Se creo `/opt/myownclone/shared` para secretos y configuracion persistente.

## Env y secretos

Se generaron y guardaron en `/opt/myownclone/shared`:

- `frontend.env.production`
- `backend.env.production`
- `admin-bootstrap.txt`

Notas:

- Los secretos fuertes se generaron en el VPS.
- No se versionaron secretos en GitHub.
- `admin-bootstrap.txt` contiene la credencial bootstrap actual del admin y debe protegerse o rotarse despues.

## Despliegue ejecutado

Se ejecuto `ops/restore-from-github-on-vps.sh` sobre la rama `audit/vps-sync-and-docs`.

Durante la restauracion se corrigieron estos bloqueos reales:

1. `myownclone-frontend.service` seguia atado a la IP antigua `100.99.222.101`.
2. `sudo -u myownclone npm` no encontraba `node/npm` porque el runtime previo vivia bajo `/root/.hermes`.
3. Las migraciones de Flask buscaban `migrations/` en una ruta incorrecta dentro del contenedor.
4. Nginx quedo contaminado por una configuracion previa de Certbot que devolvia `404` en puerto `80`.
5. El proxy de NextAuth forzaba `secureCookie: true`, lo que rompia sesiones en HTTP mientras se validaba por IP.
6. Next.js necesitaba Postgres accesible en loopback para leer `accounts` durante auth.

## Cambios aplicados en codigo

### Commits realizados en la rama `audit/vps-sync-and-docs`

- `c0c70f6` `fix(ops): bind frontend service from env`
- `7541377` `fix(auth): support http proxy sessions during restore`
- `fd5431f` `fix(ops): expose postgres on loopback for frontend auth`

### Efecto de cada cambio

- `ops/myownclone-frontend.service`
  - Deja de usar una IP hardcodeada antigua.
  - Usa `HOSTNAME` y `PORT` desde `frontend.env.production`.

- `MyOwnClone/src/proxy.ts`
  - Usa cookie segura solo cuando la request llega por HTTPS.
  - Permite validar sesiones reales durante restauracion por IP/HTTP sin romper el proxy autenticado.

- `MyOwnClone/src/lib/auth.ts`
  - Prioriza autenticacion por tabla `accounts` antes del fallback `PLATFORM_ADMIN_*`.
  - Mantiene el fallback bootstrap si la DB aun no esta lista.

- `ops/docker-compose.backend.prod.yml`
  - Publica Postgres unicamente en `127.0.0.1:5432`.
  - Permite a NextAuth consultar `accounts` desde el frontend systemd sin exponer la DB a Internet.

## Migraciones y datos

- Se aplicaron migraciones Alembic con:
  - `flask --app api.app_factory:app db --directory /app/api/migrations upgrade`
- Quedaron creadas las tablas principales:
  - `tenants`
  - `accounts`
  - `clone_configs`
  - `myownclone_plans`
  - `bookings`
  - `email_inbound`
  - `impersonation_tokens`
  - y el resto del esquema MyOwnClone
- Se creo una cuenta admin persistente en `accounts`.
- `myownclone_plans` quedo sembrada con 4 planes.

## Validaciones realizadas

### Servicios internos

- `myownclone-frontend.service`: activo
- `nginx`: activo
- `myownclone_api`: healthy
- `myownclone_postgres`: healthy
- `myownclone_redis`: healthy
- `myownclone_weaviate`: activo

### Smoke checks

- `http://127.0.0.1:3000/` -> `200`
- `http://127.0.0.1:5001/healthz` -> `200`
- `http://127.0.0.1:5001/readyz` -> `200`
- `http://212.227.169.99/` -> `200`
- `http://212.227.169.99/login` -> `200`
- `http://212.227.169.99/planes` -> `307` sin sesion
- `http://212.227.169.99/api/clone/plans` -> `401` sin sesion

### Login

Con la cuenta bootstrap/admin:

- `/admin/resumen` -> `200`
- `/api/admin/overview` -> `200`
- `/api/admin/tenants` -> `200`
- `/api/clone/plans` -> `200` con cookie de sesion

## Dominio

Estado verificado el `2026-06-15`:

- `myownclone.com` resuelve a `212.227.169.99`
- `https://myownclone.com/` responde `200`
- La respuesta publica ya sirve la landing actual de MyOwnClone
- Existen certificados en `/etc/letsencrypt/live/myownclone.com/`

## Riesgos y pendientes

- Faltan credenciales reales de integraciones:
  - `OPENAI_API_KEY`
  - `STRIPE_SECRET_KEY`
  - `STRIPE_WEBHOOK_SECRET`
  - `RESEND_API_KEY`
  - `SENDGRID_INBOUND_WEBHOOK_SECRET`
- El backend avisa que `SENDGRID_INBOUND_WEBHOOK_SECRET` no esta configurado.
- Conviene rotar o eliminar la credencial bootstrap una vez validado el acceso normal.
- Queda pendiente convertir el vhost temporal en configuracion final HTTPS limpia si se quiere endurecer del todo Nginx/Certbot.
