# Operativa de deploy y smoke test — MyOwnClone

Objetivo: dejar un camino reproducible para desplegar backend Docker + frontend Next.js con systemd en el VPS `100.99.222.101`, y validar humo de producción con `curl`.

## Artefactos creados

- `ops/docker-compose.backend.prod.yml`
- `ops/backend.env.production.example`
- `ops/frontend.env.production.example`
- `ops/myownclone-frontend.service`
- `ops/deploy-backend.sh`
- `ops/deploy-frontend.sh`
- `ops/smoke-prod.sh`

## Layout esperado en el VPS

```text
/opt/myownclone/
  current -> /opt/myownclone/releases/<release-id>
  releases/
  shared/
    backend.env.production
    frontend.env.production
```

Los scripts crean el layout anterior automáticamente.

## Backend Docker de producción

`ops/docker-compose.backend.prod.yml` hace lo siguiente:

- usa `../api/Dockerfile`
- deja Postgres/Redis/Weaviate con `restart: unless-stopped`
- publica Flask sólo en loopback: `127.0.0.1:5001:5001`
- fuerza `FLASK_ENV=production`
- añade aliases de variables DB (`DB_NAME`/`DB_DATABASE`, `DB_USER`/`DB_USERNAME`) para tolerar el código actual
- define healthcheck real contra `http://127.0.0.1:5001/console/api/`

Preparar secretos:

```bash
cp /home/haxth3/MyOwnClone/ops/backend.env.production.example /tmp/backend.env.production
# editar /tmp/backend.env.production
```

Deploy:

```bash
cd /home/haxth3/MyOwnClone
chmod +x ops/deploy-backend.sh
SSH_PASSWORD='***' BACKEND_ENV_FILE=/tmp/backend.env.production ./ops/deploy-backend.sh
```

Si el fichero ya existe en el VPS y no quieres volver a subirlo:

```bash
cd /home/haxth3/MyOwnClone
SSH_PASSWORD='***' ./ops/deploy-backend.sh
```

## Frontend Next.js nativo con systemd

El servicio `ops/myownclone-frontend.service`:

- ejecuta `npm run start -- --hostname 127.0.0.1 --port 3000`
- usa `EnvironmentFile=/opt/myownclone/shared/frontend.env.production`
- corre como usuario dedicado `myownclone`
- aplica hardening base: `NoNewPrivileges=true`, `PrivateTmp=true`, `ProtectHome=read-only`, restricciones de kernel/control groups/address families

Preparar env del frontend:

```bash
cp /home/haxth3/MyOwnClone/ops/frontend.env.production.example /tmp/frontend.env.production
# editar /tmp/frontend.env.production
```

Deploy:

```bash
cd /home/haxth3/MyOwnClone
chmod +x ops/deploy-frontend.sh
SSH_PASSWORD='***' FRONTEND_ENV_FILE=/tmp/frontend.env.production ./ops/deploy-frontend.sh
```

Notas del script:

- crea usuario `myownclone` si no existe
- sincroniza `MyOwnClone/` y `ops/`
- ejecuta `npm ci`
- compila con `npm run build`
- instala `/etc/systemd/system/myownclone-frontend.service`
- habilita/reinicia el servicio y muestra `systemctl status`

## Variables auth/frontend que deben quedar bien en producción

Estas son las claves operativas mínimas a revisar en `frontend.env.production`:

- `AUTH_URL`: URL pública canónica del frontend
- `NEXTAUTH_URL`: misma URL que `AUTH_URL`
- `AUTH_TRUST_HOST=true`: necesario detrás de reverse proxy
- `AUTH_SECRET`: secreto largo y aleatorio
- `NEXTAUTH_SECRET`: mismo valor que `AUTH_SECRET`
- `DATABASE_URL`: DB usada por Drizzle/NextAuth
- `MYOWNCLONE_API_URL`: backend Flask que usa SSR/API routes; en VPS local puede ser `http://127.0.0.1:5001`
- `PLATFORM_ADMIN_EMAIL`: email del admin bootstrap mientras el frontend no dependa de tabla `users`
- `PLATFORM_ADMIN_PASSWORD_HASH`: hash bcrypt del password del admin bootstrap

Comando recomendado para generar secreto:

```bash
openssl rand -hex 32
```

Observación importante: el frontend actual referencia además `AUTH_GOOGLE_ID`, `AUTH_GOOGLE_SECRET`, `RESEND_API_KEY` y `RESEND_FROM_EMAIL` en `MyOwnClone/src/lib/auth.ts`. Si esos proveedores siguen activos en runtime, hay que rellenarlos con valores válidos.

## Smoke test de producción

`ops/smoke-prod.sh` valida con `curl`:

1. frontend `/` => `200`
2. auth session route `/api/auth/session` => `200`
3. backend `/console/api/` => `200`
4. ruta protegida frontend `/api/clone/plans` => `401`
5. ruta protegida backend `/console/api/myownclone/clones` => `401`

Uso por defecto:

```bash
cd /home/haxth3/MyOwnClone
chmod +x ops/smoke-prod.sh
./ops/smoke-prod.sh
```

Si el backend no está expuesto públicamente porque queda sólo en loopback, ejecutar el smoke desde el VPS o sobreescribir la URL:

```bash
BACKEND_URL=http://127.0.0.1:5001 FRONTEND_URL=http://100.99.222.101 ./ops/smoke-prod.sh
```

## Requisitos previos en el VPS

Backend:

- Docker Engine + Docker Compose plugin
- acceso SSH para el operador que lanza deploy

Frontend:

- Node.js y npm instalados en el VPS
- systemd operativo

## Verificaciones locales hechas sobre estos artefactos

- sintaxis shell con `bash -n` para los scripts de `ops/`
- `docker compose config` sobre `ops/docker-compose.backend.prod.yml`
- `systemd-analyze verify` sobre `ops/myownclone-frontend.service` si la herramienta está disponible en el host local

## Gaps pendientes / no cubiertos aquí

- no se ejecutó deploy real contra `100.99.222.101` porque `22/tcp` estaba cerrado en esta sesión
- no se validó humo contra producción real por la misma razón
- no se tocó lógica de auth de la app; sólo envs, servicio systemd y scripts operativos
- si existe reverse proxy (nginx/caddy/traefik), su configuración queda fuera de estos artefactos
