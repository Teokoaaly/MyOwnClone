# SETUP.md

Guia de configuracion local para MyOwnClone.

## Requisitos

- Node.js 20 LTS recomendado.
- Python 3.11 recomendado para backend. La auditoria local corrio pytest con Python 3.13.2, pero produccion/CI declaran 3.11.
- Docker Desktop con Compose.
- PostgreSQL con pgvector via Docker.
- Redis via Docker.

## 1. Backend e infraestructura

```powershell
cd C:\Users\Usuari\Documents\hacchi\MyOwnClone\api
Copy-Item .env.example .env
```

Edita `api/.env` y define al menos:

- `FLASK_ENV=development`
- `DB_PASSWORD`
- `REDIS_PASSWORD`
- `JWT_SECRET_KEY`
- `IMPERSONATION_TOKEN_PEPPER`
- `SERVICE_API_KEY` o deja fallback dev solo en local
- `WEAVIATE_API_KEY` si levantas Weaviate con auth

Levanta servicios:

```powershell
docker compose up -d db_postgres redis weaviate
```

Instala backend:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Aplica migraciones:

```powershell
flask --app app_factory db upgrade
```

Arranca API:

```powershell
flask --app app_factory run --host=0.0.0.0 --port=5001
```

## 2. Frontend

```powershell
cd C:\Users\Usuari\Documents\hacchi\MyOwnClone\MyOwnClone
Copy-Item .env.example .env.local
npm ci
```

Edita `MyOwnClone/.env.local`:

- `DATABASE_URL`
- `NEXTAUTH_URL=http://localhost:3000`
- `AUTH_SECRET` y `NEXTAUTH_SECRET`
- `MYOWNCLONE_API_URL=http://127.0.0.1:5001`
- `SERVICE_API_KEY`, mismo valor que backend si desactivas fallback dev
- `DEFAULT_CLONE_ID` despues de crear/sembrar un clon
- claves OpenAI/Anthropic/Stripe/Resend/SendGrid/Whereby si pruebas integraciones

Arranca:

```powershell
npm run dev
```

Abre `http://localhost:3000`.

## 3. Checks locales

Desde `MyOwnClone/`:

```powershell
npm run lint
npm run typecheck
npm run build
npm run test
npm audit --omit=dev
```

Desde la raiz:

```powershell
pytest -q
```

E2E:

```powershell
cd C:\Users\Usuari\Documents\hacchi\MyOwnClone\MyOwnClone
npm run test:e2e
```

## 4. Problemas conocidos de setup

- `npm audit` y `npm audit --omit=dev` deben devolver `found 0 vulnerabilities`.
- El backend acepta `DATABASE_URL` y normaliza `postgresql+psycopg://` a `postgresql://`; el driver estandar sigue siendo `psycopg2-binary`.
- Produccion usa PostgreSQL con pgvector mediante `pgvector/pgvector:pg15`.
- `flask --app app_factory db upgrade` fue validado sobre una DB limpia `pgvector/pgvector:pg15`.
- La DB local existente fue respaldada en `backups/myownclone_before_alembic_stamp.dump` y marcada en Alembic head (`c3d4e5f6a7c1`).
- Si otra DB falla con `relation "tenants" already exists`, esa DB ya contiene tablas fuera del estado Alembic; crea backup antes de estampar/reconciliar.
- No uses `dev-api-key-for-proxy` fuera de local.
