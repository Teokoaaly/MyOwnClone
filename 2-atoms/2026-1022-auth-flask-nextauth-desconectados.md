---
id: 2026-1022-auth-flask-nextauth-desconectados
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[myownclone]]", "[[2026-1022-auth-otp-impersonacion-30min]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]"]
---
## Claim
Los dos sistemas de [[myownclone]] están **desconectados en autenticación**: el backend Flask usa decorators `@login_required`, `@account_initialization_required` y `@setup_required`, mientras que el frontend Next.js usa `auth()` de NextAuth (`@/lib/auth`). Como el frontend escribe directo a Drizzle (`/api/clone/memories`) y solo proxya algunas rutas a Flask, la sesión del frontend no gobierna el acceso al backend Flask y viceversa: hay dos sistemas de identidad conviviendo sobre el mismo modelo de datos.

## Why It Matters
El handoff lo afirma como estado actual ("los dos systems están desconectados actualmente"), y es la costura que ya produce bugs reales en este repositorio (drift de schema entre SQLAlchemy y Drizzle, ver [[2026-1022-drift-schema-drizzle-sqlalchemy]]). Un único modelo de auth cortaría de raíz la mitad de esos fallos: el mismo token validado por ambos lados.
En el vault, [[2026-1022-auth-otp-impersonacion-30min]] ya documenta la pieza de impersonación con OTP del lado NextAuth; este átomo añade que el lado Flask no participa de ese control, es decir, la impersonación no cubre toda la superficie.
Consecuencia para el modo multi-tenant: [[multi-tenant-saas]] exige aislamiento por tenant, y con dos sistemas de sesión independientes el aislamiento solo puede garantizarse en la capa de datos (filtros por tenant_id), nunca en la capa de sesión.
