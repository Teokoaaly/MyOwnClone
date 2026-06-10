---
name: bootstrap-local-completado
description: MyOwnClone bootstrap local finalizado — MVP mínimo verificable operativo
metadata:
  type: project
  status: verified
---

El bootstrap local de MyOwnClone se completó con éxito el 2026-06-09.

**Qué se logró:**
- PostgreSQL nativo (PID 7444, puerto 5432) + Docker Redis (puerto 6379) operativos
- 19 tablas en BD con Alembic en head (`b1c2d3e4f5a6`)
- Login admin funcional: `admin@myownclone.com` / `admin123`
- Backend Flask arranca en `localhost:5001` sin errores
- Frontend Next.js 16 arranca en `localhost:3000` sin errores
- Flujo E2E: login → JWT → admin overview → list clones → frontend landing
- Seed data: tenant demo, admin account, clone config, meeting type, availability

**Fixes de último momento:**
- Password hash cambiado de scrypt (werkzeug) a bcrypt
- Decorador `account_initialization_required` parcheado para standalone (usa `g.account_id`)
- `setup_required` convertido en no-op en standalone
- UUID serialization: flask-restx Resources necesitan `str(uuid)` explícito

**Pendientes inmediatos:**
- Falta API key LLM (OpenAI/Anthropic) para chat funcional → `model_unavailable`
- [[dualidad-drizzle-alembic]] sigue sin resolver
- [[pgvector-no-disponible]] en PostgreSQL nativo del host

**Why:** Completar bootstrap era requisito para cualquier trabajo posterior significativo.
**How to apply:** Para arrancar entorno, ejecutar `docker compose up -d redis` (solo Redis), luego `python run_dev.py` en `api/` y `npm run dev` en `MyOwnClone/`.
