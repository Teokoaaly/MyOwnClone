# DEPLOYMENT.md

Guia de despliegue para MyOwnClone.

## Estado actual

El repo incluye scripts en `ops/` y ejemplos de variables de entorno. Los bloqueantes P0 de auditoria inicial quedaron mitigados, pero antes de produccion real falta un ensayo de staging con datos/secretos reales:

- `npm audit` debe mantenerse en 0 vulnerabilidades.
- `ops/docker-compose.backend.prod.yml` usa PostgreSQL con pgvector.
- CI y runtime usan URLs `postgresql://` compatibles con `psycopg2-binary`.
- E2E pasa local con 35 passed / 2 skipped; staging debe seedear sesion/clones para eliminar skips.
- Secretos reales rotados y `ALLOW_DEV_SERVICE_KEY=false`.

## Backend VPS

Archivos relevantes:

- `ops/docker-compose.backend.prod.yml`
- `ops/backend.env.production.example`
- `ops/deploy-backend.sh`

Pasos:

1. Copiar `ops/backend.env.production.example` a `backend.env.production`.
2. Sustituir todos los placeholders `change-me`.
3. Asegurar:
   - `FLASK_ENV=production`
   - `ALLOWED_ORIGINS=https://dominio-real`
   - `SERVICE_API_KEY` fuerte
   - `ALLOW_DEV_SERVICE_KEY=false`
   - `JWT_SECRET_KEY` fuerte
   - `IMPERSONATION_TOKEN_PEPPER` fuerte
   - Al menos un proveedor LLM configurado (`OPENAI_API_KEY`,
     `ANTHROPIC_API_KEY`, `MINIMAX_API_KEY` o `TOGETHER_API_KEY`)
4. Verificar que DB usa imagen con pgvector y que la migracion `c3d4e5f6a7c1` crea la extension.
5. Ejecutar migraciones antes de abrir trafico.
6. Configurar reverse proxy HTTPS.

Comando esperado:

```bash
bash ops/deploy-backend.sh
```

### LLM / DeepSeek

El runtime del backend usa `api/core/model_manager.py`. Para OpenAI real:

```bash
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

Para DeepSeek u otro proveedor compatible con la API de OpenAI:

```bash
OPENAI_API_KEY=...
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
```

`OPENAI_API_BASE` se acepta como alias legacy, pero `OPENAI_BASE_URL` es el
nombre preferido porque coincide con el SDK oficial de OpenAI.

## Frontend VPS

Archivos relevantes:

- `ops/frontend.env.production.example`
- `ops/deploy-frontend.sh`
- `ops/myownclone-frontend.service`

Pasos:

1. Copiar ejemplo a `frontend.env.production`.
2. Configurar:
   - `NODE_ENV=production`
   - `DATABASE_URL`
   - `MYOWNCLONE_API_URL`
   - `AUTH_URL`
   - `NEXTAUTH_URL`
   - `AUTH_SECRET`
   - `NEXTAUTH_SECRET`
   - `SERVICE_API_KEY` igual al backend
3. Ejecutar build y levantar servicio systemd.

Comando esperado:

```bash
bash ops/deploy-frontend.sh
```

El deploy copia `shared/frontend.env.production` a
`current/MyOwnClone/.env.production` con propietario `myownclone` y permisos
`0600`. Esto evita errores `EACCES` durante `next start` cuando existe un env
antiguo creado por `root`.

## Checklist pre-produccion

- `npm run lint`
- `npm run typecheck`
- `npm run build`
- `npm run test`
- `pytest -q`
- `npm audit --omit=dev`
- `npm run test:e2e`
- `flask --app app_factory db upgrade` sobre DB staging vacia; validado localmente en DB temporal pgvector
- Para bases preexistentes sin `alembic_version`, hacer backup antes de cualquier `flask db stamp`.
- smoke test login/dashboard/chat/billing/webhook

## ⚠️ Regla de migraciones de schema (ver SCHEMA_OWNERSHIP.md)

**Alembic es el único dueño del esquema en producción.**

- ✅ `flask --app app_factory db upgrade` — comando seguro, aplicar siempre.
- ❌ `npm run db:push` — **PROHIBIDO en producción**. Drizzle Kit `push` aplica
  ALTER/CREATE automáticos sin archivo SQL revisable; puede recrear tablas y
  perder datos. Solo usar `db:migrate` con archivos SQL revisados en dev local.
- Para sincronizar el schema Drizzle tras un cambio Alembic: `npm run db:generate`
  (regenera el snapshot, no toca la DB).

## Activar embeddings semánticos (pipeline RAG estándar)

Si despliegas la rama `feature/standard-rag-pipeline`, tras el deploy:

1. Asegura `OPENAI_API_KEY` (o `MINIMAX_API_KEY` si te basta con léxico) en
   `ops/backend.env.production`.
2. Aplica migración: `docker exec myownclone_api flask --app app_factory db upgrade`
3. Reinicia: `docker compose -f ops/docker-compose.backend.prod.yml restart api`
4. **Backup antes de reindexar**: `bash ops/backup_postgres.sh`
5. Reindexa contenido existente (los chunks viejos tienen hash léxico):
   ```bash
   docker exec myownclone_api flask --app app_factory reindex
   ```
6. Verifica: `curl http://127.0.0.1:5001/api/myownclone/internal/embed/status -H "X-API-Key: $SERVICE_API_KEY"`

Nuevas deps Python (ya en `requirements.txt`): `openai`, `anthropic`, `pypdf`,
`youtube-transcript-api`, `trafilatura`. El contenedor las instala en build.

## Rollback

- Mantener backup de DB antes de migraciones.
- Mantener release anterior de frontend/backend.
- Deploy backend y frontend deben registrar commit SHA.
- Si falla readiness, revertir servicio y restaurar env anterior.

## Observabilidad minima

- Sentry frontend y backend.
- Logs con request ID.
- Alertas por 5xx, latencia p95 y cola/webhook failures.
- `/healthz` para liveness.
- `/readyz` para DB/Redis/migraciones.
