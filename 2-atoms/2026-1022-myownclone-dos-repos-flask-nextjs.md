---
id: 2026-1022-myownclone-dos-repos-flask-nextjs
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[myownclone]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[multi-tenant-saas]]"]
---
## Claim
[[myownclone]] no es un monorepo: son **dos bases de código independientes** con procesos de arranque separados. El backend Flask/SQLAlchemy vive en `/home/haxth3/myownclone_local/api/` (`api/controllers/myownclone_public.py`, `api/controllers/console/myownclone/{clone,creator_memory,inbox}.py`, `api/models/{clone,analytics}.py`, `api/core/retrieval.py`, `api/core/myownclone/{email_ai,silos}.py`) y arranca con `python -m api.app_factory` en el puerto 5001. El frontend Next.js vive en `/home/haxth3/MyOwnClone/MyOwnClone/` (`src/app/(dashboard)/{cerebro,resumen,biblioteca}/page.tsx`, `src/lib/db/schema/{clones,analytics,conversations}.ts` con Drizzle) y arranca con `npm run dev` en el 3000. El frontend además tiene su propia ruta de API a Drizzle directo (`src/app/api/clone/memories/route.ts`) que **no pasa por Flask**.

## Why It Matters
Cada feature nueva tiene dos puntos de contacto y una frontera de datos: si el frontend escribe directo a la base y Flask también, entonces cualquier campo nuevo hay que añadirlo en los dos schemas (SQLAlchemy y Drizzle) — que es exactamente la raíz de los bugs de drift que documenta este mismo handoff (ver [[2026-1022-drift-schema-drizzle-sqlalchemy]]). El proxy `src/proxy.ts` es el único mapa de rutas entre ambos (`/api/clones` → `/console/api/myownclone/clones`, `/api/feedback`, `/api/inbox`).
Consecuencia operativa: el handoff advierte explícitamente de que "NO copies el prompt system de MyClone tal cual — adapta las variables a los campos existentes de CloneConfig", es decir, MyClone y MyOwnClone no comparten dominio de datos, solo patrones. Ver [[multi-tenant-saas]] para el modelo de aislamiento por tenant que debe mantener esta separación.

## [FRICTION]
> `entities/myownclone.md` describe el stack de [[myownclone]] como una sola línea — Frontend Next.js 14 + Hosting Vercel + Base de datos Neon + Auth NextAuth.js — sin mencionar ningún backend Flask ni SQLAlchemy.
> Este átomo presiona esa creencia porque el código real tiene un backend Flask con modelos SQLAlchemy propios (`clone_configs`, `clone_mode_prompts`, `memories`, `analytics`) y una API de consola separada, con un frontend que escribe en la base por Drizzle directo.
> Ambas no pueden ser completamente correctas: o el entity resume solo la capa pública visible y omite el backend por ser interno, o el stack "Next.js + Neon" describe solo el frontend y no el producto completo. Marcado para juicio humano, no auto-resuelto.
