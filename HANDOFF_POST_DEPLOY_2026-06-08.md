# Handoff — MyOwnClone post-deploy canon (2026-06-08)

Resumen corto
- Ya quedó escrita la referencia operativa canónica en `ops/CANONICAL_POST_DEPLOY_STATE_2026-06-08.md`.
- El layout vigente dejó de ser `/root/MyOwnClone/...` y pasó a releases bajo `/opt/myownclone/current/...`.
- Frontend canónico en prod: `/opt/myownclone/current/MyOwnClone` con `myownclone-frontend.service`.
- Backend canónico en prod: `/opt/myownclone/current/api` levantado desde `/opt/myownclone/current/ops/docker-compose.backend.prod.yml`.
- No se borró nada en producción porque no hubo verificación remota suficiente: `ssh root@100.99.222.101` devolvió `connection refused`.

Estado verificado en esta sesión
- repo local: `/home/haxth3/MyOwnClone`
- backend local real: `/home/haxth3/MyOwnClone/api/app_factory.py`
- frontend local real: `/home/haxth3/MyOwnClone/MyOwnClone/package.json`
- public smoke:
  - `https://myownclone.com` -> `200 OK`
  - `https://myownclone.com/console/api/` -> `200 OK`
  - `https://myownclone.com/api/auth/session` -> `200 OK`
  - `https://myownclone.com/api/clone/plans` -> `401 Unauthorized`
  - `https://myownclone.com/console/api/myownclone/clones` -> `401 Unauthorized`
- reverse proxy público observado: `nginx/1.24.0 (Ubuntu)`

Confusión resuelta
- `replica/` ya no es un path real del repo; hoy el frontend vive en `MyOwnClone/`.
- `api/api/` ya no debe tratarse como árbol vivo.
- `/root/MyOwnClone*` quedó como legado de handoffs viejos; la referencia nueva es `/opt/myownclone/current`.

Archivos tocados en esta sesión
- creado: `/home/haxth3/MyOwnClone/ops/CANONICAL_POST_DEPLOY_STATE_2026-06-08.md`
- creado: `/home/haxth3/MyOwnClone/HANDOFF_POST_DEPLOY_2026-06-08.md`

Qué queda si se retoma después
1. Entrar al VPS por un camino que sí funcione (SSH/Tailscale o consola).
2. Ejecutar el bloque de verificación de paths viejos del doc canónico.
3. Si `/root/MyOwnClone-clean`, `/root/MyOwnClone-new`, `/root/MyOwnClone_new`, `/root/myownclone-api` existen y no están referenciados, borrarlos uno por uno con evidencia.
4. Confirmar si el backend env real vive en `/opt/myownclone/shared/backend.env.production` como ya asume `ops/deploy-backend.sh`.
5. Si se quiere cerrar el loop, copiar esta verdad operativa a cualquier README/ops doc adicional que todavía hable de `replica/` o `/root/MyOwnClone`.

Comandos de arranque rápido
```bash
# frontend
sudo systemctl restart myownclone-frontend
sudo systemctl status myownclone-frontend --no-pager
curl -I --max-time 15 https://myownclone.com

# backend
cd /opt/myownclone/current/ops
cp /opt/myownclone/shared/backend.env.production ./backend.env.production
docker compose -f docker-compose.backend.prod.yml up -d --build --remove-orphans
docker compose -f docker-compose.backend.prod.yml ps
curl -fsS http://127.0.0.1:5001/console/api/ >/dev/null
```

Bloqueador encontrado
- Sin acceso SSH usable al VPS no es responsable borrar rutas legacy ni confirmar el filesystem remoto real. En esta sesión el nodo respondió por web/Tailscale, pero `22/tcp` estaba cerrado; por eso el cleanup quedó documentado, no ejecutado.
- Además, el fix de admin web quedó validado localmente pero no desplegado aún por el mismo bloqueo de acceso remoto.
