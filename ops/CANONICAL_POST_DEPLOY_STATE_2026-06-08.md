# MyOwnClone — estado canónico post-deploy (2026-06-08)

Objetivo: una sola referencia operativa para paths, servicios y recovery sin mezclar rutas viejas.

## 1) Paths canónicos hoy

Repositorio local de trabajo
- raíz: `/home/haxth3/MyOwnClone`
- backend Flask real: `/home/haxth3/MyOwnClone/api`
- frontend Next.js real: `/home/haxth3/MyOwnClone/MyOwnClone`
  - nota: el `package.json` todavía se llama `"replica"`, pero el directorio real ya no es `replica/`

Producción esperada según los artefactos vigentes de `ops/`
- release root: `/opt/myownclone/current`
- frontend real: `/opt/myownclone/current/MyOwnClone`
- backend real: `/opt/myownclone/current/api`
- backend ops: `/opt/myownclone/current/ops`
- env compartidos:
  - frontend: `/opt/myownclone/shared/frontend.env.production`
  - backend: `/opt/myownclone/shared/backend.env.production`

## 2) Servicios canónicos en producción

Frontend
- unit file de referencia: `myownclone-frontend.service`
- `WorkingDirectory=/opt/myownclone/current/MyOwnClone`
- `EnvironmentFile=/opt/myownclone/shared/frontend.env.production`
- `ExecStart=/usr/bin/npm run start -- --hostname 127.0.0.1 --port 3000`

Backend
- compose de referencia: `/opt/myownclone/current/ops/docker-compose.backend.prod.yml`
- contenedores esperados:
  - `myownclone_api`
  - `myownclone_postgres`
  - `myownclone_redis`
  - `myownclone_weaviate`

Reverse proxy público
- el smoke público devolvió `Server: nginx/1.24.0 (Ubuntu)`
- URLs verificadas desde esta sesión:
  - `https://myownclone.com` -> `200 OK`
  - `https://myownclone.com/console/api/` -> `200 OK`
  - `https://myownclone.com/api/auth/session` -> `200 OK`
  - `https://myownclone.com/api/clone/plans` -> `401 Unauthorized`
  - `https://myownclone.com/console/api/myownclone/clones` -> `401 Unauthorized`

## 3) Inventario de rutas viejas/obsoletas mencionadas

Estas rutas NO deben volver a usarse como referencia canónica:

1. `/root/MyOwnClone/replica`
- estado: obsoleta
- evidencia: commit `507737f` renombró `replica/` -> `MyOwnClone/`
- reemplazo: `/opt/myownclone/current/MyOwnClone` en producción; `/home/haxth3/MyOwnClone/MyOwnClone` en local

2. `/root/MyOwnClone/api`
- estado: referencia histórica, superada por el layout release-based
- evidencia: `ops/deploy-backend.sh` despliega a `/opt/myownclone/releases/...` y apunta `current` a `/opt/myownclone/current`
- reemplazo: `/opt/myownclone/current/api`

3. `/root/MyOwnClone`
- estado: referencia histórica de handoffs viejos, no canónica
- evidencia: docs nuevas de `ops/` usan `/opt/myownclone/...`; el frontend systemd ya no apunta a `/root/...`
- reemplazo: `/opt/myownclone/current`

4. `/root/MyOwnClone-clean`
5. `/root/MyOwnClone-new`
6. `/root/MyOwnClone_new`
7. `/root/myownclone-api`
- estado: candidatas obsoletas/no canónicas
- evidencia: sólo aparecen en handoffs antiguos y pedidos de cleanup; no aparecen en `ops/deploy-backend.sh`, `ops/myownclone-frontend.service` ni `ops/docker-compose.backend.prod.yml`
- acción tomada: NO borradas en esta sesión porque no pude verificar por SSH el filesystem del VPS real (desde este host: `ssh root@100.99.222.101` -> `connection refused`)

## 4) Recovery canónico

Frontend
```bash
sudo systemctl daemon-reload
sudo systemctl restart myownclone-frontend
sudo systemctl status myownclone-frontend --no-pager
curl -I --max-time 15 https://myownclone.com
```

Backend
```bash
cd /opt/myownclone/current/ops
cp /opt/myownclone/shared/backend.env.production ./backend.env.production
docker compose -f docker-compose.backend.prod.yml up -d --build --remove-orphans
docker compose -f docker-compose.backend.prod.yml ps
curl -fsS http://127.0.0.1:5001/console/api/ >/dev/null
```

Deploy backend desde una máquina con el repo
```bash
cd /home/haxth3/MyOwnClone
SSH_PASSWORD='***' BACKEND_ENV_FILE=/ruta/backend.env.production ./ops/deploy-backend.sh
```

## 5) Comando exacto para cleanup seguro de rutas viejas en el VPS

No ejecutar a ciegas. Primero validar que ningún servicio activo referencia esas rutas:

```bash
for p in \
  /root/MyOwnClone \
  /root/MyOwnClone/replica \
  /root/MyOwnClone-clean \
  /root/MyOwnClone-new \
  /root/MyOwnClone_new \
  /root/myownclone-api
  do
  echo "=== $p ==="
  test -e "$p" && stat "$p" || echo "missing"
  systemctl cat myownclone-frontend.service 2>/dev/null | grep -F "$p" || true
  grep -R -F "$p" /opt/myownclone/current/ops /etc/systemd /etc/nginx 2>/dev/null || true
 ***REMOVED***
```

Si el path existe y las búsquedas salen vacías, recién entonces:

```bash
rm -rf /ruta/confirmada-como-no-usada
```

## 6) Qué NO es canónico

- cualquier instrucción que diga `cd replica`
- cualquier referencia a `api/api/` como árbol vivo
- cualquier recovery que use `/root/MyOwnClone/...` como source of truth
- cualquier idea de frontend en Docker: el commit `eef15f6` revirtió ese camino y dejó frontend nativo con systemd

## 7) Evidencia base usada para esta canonización

- `ops/myownclone-frontend.service`
- `ops/deploy-backend.sh`
- `ops/docker-compose.backend.prod.yml`
- `git log` con commits:
  - `507737f feat(deploy): rename replica/ → MyOwnClone/ + Dockerfile + compose frontend service`
  - `eef15f6 revert(deploy): remove frontend Docker service — run Next.js natively on VPS with s6/systemd`
- smoke HTTP público ejecutado en esta sesión
- intento de SSH al VPS fallido: `connection refused`, por eso no hubo borrado remoto
