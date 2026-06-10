# AUTH SOURCE OF TRUTH — Decisión arquitectónica

> Fecha: 2026-06-10 · Estado: **propuesta pendiente de confirmación**

## Contexto

El repo contiene **dos implementaciones de autenticación paralelas**:

1. **NextAuth v5** (frontend, `MyOwnClone/src/lib/auth.ts`) — usa `DrizzleAdapter` sobre
   las tablas `users` / `nextauth_accounts` / `verificationTokens` definidas en
   `MyOwnClone/src/lib/db/schema/users.ts`. Estrategia JWT. Soporta Credentials,
   Google OAuth y Resend magic link.
2. **Flask JWT** (backend, `api/controllers/console/auth.py`) — endpoint
   `POST /console/api/auth/login` que consulta `accounts` (tabla SQLAlchemy
   en `api/models/account.py`) y emite un JWT HS256 firmado con
   `JWT_SECRET_KEY`. Decorado con `login_required` en `api/libs/login.py`.

El middleware de Next.js (`MyOwnClone/src/middleware.ts`) **no usa** la ruta
`/api/auth/login`; las llamadas autenticadas van a través del proxy con la
cabecera `X-API-Key: SERVICE_API_KEY` (ver Fase 1). En la práctica, **el flujo
de login real vive en NextAuth**, y el endpoint Flask sólo se conserva
para compatibilidad hacia atrás (por ejemplo, integraciones externas o
scripts que aún lo consumen).

## Problema

- Riesgo de drift: `users.passwordHash` (Drizzle) ≠ `accounts.password` (SQLAlchemy).
  Si un usuario se registra vía NextAuth, su fila vive en `users` pero **no**
  en `accounts`; el endpoint Flask no lo encuentra.
- Doble superficie a mantener: cualquier cambio de password, MFA, recuperación,
  etc. debe aplicarse a ambos lados.
- Las migraciones Drizzle y Alembic gestionan dominios solapados y pueden
  entrar en conflicto.

## Recomendación

**Consolidar todo en NextAuth** (Drizzle `users` como única tabla de cuentas).

### Pasos

1. **Dejar de generar filas en `accounts`**: eliminar el seed Flask que crea
   cuentas demo; el seed de Drizzle pasa a ser la única fuente.
2. **Eliminar `auth_bp`** del backend y de `app_factory.py`.
3. **Migrar `accounts` → `users`**: una migración Alembic+Drizzle que renombre
   la tabla y las columnas (`password` → `password_hash`) y traslade los datos.
4. **Sustituir `login_required`** en `api/libs/login.py` por una variante que
   valide únicamente tokens emitidos por NextAuth (mismo `AUTH_SECRET`).
5. **Eliminar la entrada `/api/auth/login`** del `ROUTE_MAP` del middleware.
6. **Documentar** que cualquier consumer externo (si existe) debe migrar a
   NextAuth.

### Riesgos

- Si hay integraciones externas (webhooks, scripts, integraciones de terceros)
  que aún llaman a `/console/api/auth/login`, dejarán de funcionar. Hay que
  identificarlas antes de eliminar.
- La migración `accounts` → `users` debe coordinarse con un deploy sin
  downtime (dual-write corto + cutover + drop).

## Estado actual (Fase 2)

✅ Resend magic link **crea fila en `users` (Drizzle)** vía NextAuth.
✅ `/es/verificar` consume el token y lo marca como usado.
✅ Forgot/reset password fluyen sobre `users` y `verificationTokens`.
🟡 `auth_bp` sigue activo en Flask pero **no es la ruta de login de facto**
   para usuarios web. Se conserva temporalmente hasta confirmar que no hay
   consumers externos.
🟡 El proxy de middleware usa `SERVICE_API_KEY` (Fase 1), no JWT, así que
   el endpoint Flask no recibe tráfico de usuarios web.

## Acción

Antes de eliminar `auth_bp` se requiere:

1. Confirmar que no hay tráfico de producción hacia `/console/api/auth/login`
   (revisar logs de Nginx / observabilidad).
2. Listar integraciones externas que lo usen (si las hay).
3. Diseñar la ventana de migración dual-write.

Hasta entonces, **se mantiene la coexistencia** documentada en este archivo.
