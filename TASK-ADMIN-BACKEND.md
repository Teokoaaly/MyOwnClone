# Plan maestro: Backend Admin de MyOwnClone

## Objetivo

Implementar y endurecer el backend de administracion de **MyOwnClone** para que el panel `/admin` tenga una API estable, segura y verificable. Este plan esta escrito para que otro modelo mas sencillo pueda ejecutarlo paso a paso sin improvisar.

Prioridad absoluta: **no introducir errores de autenticacion, multi-tenancy, imports, modelos ni contratos frontend-backend**.

## Resumen del repositorio revisado

El proyecto tiene dos areas principales:

- Backend Python/Flask:
  - `api/api/app_factory.py`
  - `api/api/controllers/console/myownclone/admin_platform.py`
  - `api/api/controllers/console/auth.py`
  - `api/api/libs/login.py`
  - `api/api/models/*`
  - `api/api/migrations/versions/*`
- Frontend/Admin Next:
  - `replica/src/app/admin/layout.tsx`
  - `replica/src/app/admin/resumen/page.tsx`
  - `replica/src/app/admin/tenants/page.tsx`
  - `replica/src/app/admin/feedback/page.tsx`
  - `replica/src/app/api/admin/[...path]/route.ts`
  - `replica/src/app/api/admin/route.ts`
  - `replica/src/lib/db/schema/*`

Stack detectado:

- Frontend: Next `16.2.6`, React `19.2.4`, Tailwind `4`, TypeScript, Vitest.
- Backend: Flask, Flask-RESTX, SQLAlchemy, Alembic, JWT propio en `/console/api/auth`.
- Base de datos: PostgreSQL, con esquemas duplicados/paralelos entre SQLAlchemy y Drizzle.

## Diagnostico tecnico actual

### Backend admin existente

Archivo principal:

```text
api/api/controllers/console/myownclone/admin_platform.py
```

Endpoints existentes:

- `GET /console/api/myownclone/admin/overview`
- `GET /console/api/myownclone/admin/tenants`
- `POST /console/api/myownclone/admin/impersonate`
- `POST /console/api/myownclone/admin/impersonate/stop`

Pantallas frontend que consumen admin:

- `GET /api/admin/overview`
- `GET /api/admin/tenants`
- `GET /api/admin/feedback`

Proxy Next:

```text
replica/src/app/api/admin/[...path]/route.ts
```

Actualmente reenvia peticiones a:

```text
{MYOWNCLONE_API_URL}/console/api/myownclone/admin/{endpoint}
```

### Riesgos detectados

Estos riesgos deben resolverse antes de ampliar funcionalidad:

1. **Import sospechoso en `_is_platform_admin`**

   En `admin_platform.py`:

   ```py
   from models.account import Account
   ```

   Debe revisarse porque el patron usado en el resto del backend es `api.models...`. Ademas, `api/api/models/account.py` contiene stubs, no modelos SQLAlchemy completos.

2. **Modelos `Tenant` y `Account` incompletos en Python**

   `api/api/models/account.py` define clases simples/stub:

   ```py
   class Tenant:
       id: str
       name: str
       status: str
   ```

   Pero `admin_platform.py` hace queries SQLAlchemy:

   ```py
   select(func.count(Tenant.id))
   select(Tenant).order_by(Tenant.created_at.desc())
   ```

   Si ese `Tenant` no es un modelo SQLAlchemy real, las rutas pueden fallar en runtime.

3. **Doble arbol `api/` y `api/api/`**

   Existen archivos parecidos en:

   - `api/controllers/...`
   - `api/api/controllers/...`
   - `api/models/...`
   - `api/api/models/...`

   Hay riesgo alto de editar el archivo equivocado. Para este plan, la fuente principal debe ser `api/api/*`, porque `api/api/app_factory.py` registra esos controladores.

4. **Auth inconsistente entre Next y Flask**

   El backend Flask espera:

   ```http
   Authorization: Bearer <jwt>
   ```

   Pero el proxy Next actual reenvia solo:

   ```ts
   Cookie: request.headers.get("cookie") || ""
   ```

   Tambien existe:

   ```ts
   const ADMIN_TOKEN = process.env.PLATFORM_ADMIN_TOKEN || ""
   ```

   pero no se usa. Esto indica que el panel admin puede no autenticar correctamente contra Flask.

5. **Fuente de verdad mezclada**

   `replica/src/app/api/admin/route.ts` lee tenants directamente con Drizzle.

   `replica/src/app/api/admin/[...path]/route.ts` proxya a Flask.

   El plan debe unificar la fuente de verdad: para administracion de plataforma, preferir backend Flask o definir explicitamente que datos quedan locales en Next. Recomendacion: **Flask como API admin canonica** y Next solo como BFF/proxy con auth.

6. **Contrato `feedback` incompleto**

   La pagina `replica/src/app/admin/feedback/page.tsx` llama:

   ```text
   /api/admin/feedback
   ```

   Pero `admin_platform.py` no define `GET /myownclone/admin/feedback`.

   Existe controlador separado:

   ```text
   api/api/controllers/console/myownclone/feedback.py
   ```

   pero debe confirmarse si sirve datos de plataforma o solo tenant/clone.

7. **Inconsistencia de nombres de planes y estados**

   Backend admin usa planes:

   ```py
   {"básico", "pro", "escala", "enterprise"}
   ```

   Drizzle usa:

   ```ts
   "basic", "pro", "scale", "enterprise", "trial"
   ```

   Backend admin usa `Tenant.status == "normal"`, Drizzle usa:

   ```ts
   "active", "suspended", "cancelled", "trial"
   ```

   Esto puede producir metricas incorrectas aunque no falle el build.

## Principios de arquitectura

### Fuente de verdad

Para administracion de plataforma:

- Flask debe exponer la API canonica.
- Next debe autenticar la sesion web y reenviar al backend de forma controlada.
- Drizzle puede seguir existiendo para auth/web app, pero no debe duplicar logica admin critica salvo que se documente.

### Seguridad

Toda ruta admin debe cumplir:

- Usuario autenticado.
- Rol `platform_admin`.
- Auditoria en acciones sensibles.
- Validacion estricta de payload con Pydantic o schema equivalente.
- No filtrar tokens completos en logs.
- No devolver secretos al frontend salvo que sea estrictamente necesario.

### Multi-tenancy

Toda query debe:

- Ser explicita sobre si es global de plataforma o scoped por tenant.
- Evitar modificar datos de tenants sin auditoria.
- No permitir que un tenant normal acceda a endpoints de plataforma.

### Contratos estables

Cada endpoint debe devolver JSON con forma estable:

- Para listas: `{ "items": [], "pagination": {...} }`
- Para errores: `{ "error": "code", "message": "Human readable message" }`
- Para fechas: ISO 8601 en nuevas APIs; mantener compatibilidad si una pantalla espera timestamp Unix.

## Contrato admin propuesto

### `GET /console/api/myownclone/admin/overview`

Debe devolver:

```json
{
  "total_tenants": 0,
  "active_tenants": 0,
  "total_clones": 0,
  "mrr_cents": 0,
  "mrr_display": "0.00€",
  "total_costs_cents": 0,
  "total_costs_display": "0.00€",
  "margin_cents": 0,
  "margin_display": "0.00€",
  "plan_breakdown": {
    "trial": 0,
    "basic": 0,
    "pro": 0,
    "scale": 0,
    "enterprise": 0
  },
  "generated_at": "2026-06-04T00:00:00Z"
}
```

Reglas:

- Usar nombres canonicos de plan en ingles: `trial`, `basic`, `pro`, `scale`, `enterprise`.
- Si hace falta compatibilidad visual en espanol, traducir en frontend.
- `active_tenants` debe usar el estado real disponible en DB. No asumir `normal` si el schema usa `active`.

### `GET /console/api/myownclone/admin/tenants`

Parametros:

```text
page=1
limit=20
search=
status=
plan=
sort=created_at
direction=desc
```

Respuesta:

```json
{
  "items": [
    {
      "id": "tenant_id",
      "slug": "tenant-slug",
      "name": "Tenant name",
      "plan": "pro",
      "status": "active",
      "subscription_status": "active",
      "clone_count": 1,
      "monthly_cost_cents": 0,
      "created_at": "2026-06-04T00:00:00Z",
      "updated_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}
```

Reglas:

- Aplicar `limit <= 50`.
- Buscar por `name`, `slug` y opcionalmente email del owner si existe relacion.
- No devolver datos sensibles.

### `GET /console/api/myownclone/admin/tenants/<tenant_id>`

Nuevo endpoint recomendado.

Debe devolver detalle operativo:

```json
{
  "tenant": {
    "id": "tenant_id",
    "slug": "tenant-slug",
    "name": "Tenant name",
    "plan": "pro",
    "status": "active",
    "subscription_status": "active",
    "created_at": "2026-06-04T00:00:00Z"
  },
  "usage": {
    "clone_count": 0,
    "cost_cents_30d": 0,
    "tokens_in_30d": 0,
    "tokens_out_30d": 0,
    "questions_30d": 0,
    "gaps_open": 0
  },
  "clones": []
}
```

### `PATCH /console/api/myownclone/admin/tenants/<tenant_id>`

Nuevo endpoint recomendado para acciones controladas.

Payload permitido:

```json
{
  "plan": "pro",
  "status": "active"
}
```

Reglas:

- Solo permitir campos allowlist.
- Registrar auditoria.
- No modificar billing externo sin endpoint dedicado.

### `GET /console/api/myownclone/admin/feedback`

Nuevo endpoint necesario para la pantalla actual.

Parametros:

```text
page=1
limit=20
search=
rating=
clone_id=
tenant_id=
```

Respuesta:

```json
{
  "items": [
    {
      "id": "feedback_id",
      "clone_id": "clone_id",
      "tenant_id": "tenant_id",
      "tenant_name": "Tenant name",
      "rating": "up",
      "comment": "Texto",
      "created_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}
```

### `POST /console/api/myownclone/admin/impersonate`

Mantener, pero endurecer.

Payload:

```json
{
  "tenant_id": "tenant_id",
  "reason": "Necesario para soporte"
}
```

Reglas:

- `reason` obligatorio con minimo 10 caracteres.
- Confirmar que tenant existe antes de crear token.
- Expiracion maxima: 30 minutos.
- Token debe guardarse hasheado si se va a persistir mas alla del retorno inmediato.
- Log sin token completo.
- Registrar `started_at`.

Respuesta:

```json
{
  "impersonation_id": "id",
  "token": "one_time_token",
  "tenant_id": "tenant_id",
  "tenant_name": "Tenant name",
  "expires_at": "2026-06-04T00:30:00Z"
}
```

### `POST /console/api/myownclone/admin/impersonate/stop`

Reglas:

- Debe cerrar el log correcto, no solo el ultimo log abierto del admin.
- Si no existe token activo, devolver 404 o 400 claro.
- Debe borrar/revocar token.

### `GET /console/api/myownclone/admin/audit-log`

Nuevo endpoint recomendado.

Debe listar:

- Impersonaciones.
- Cambios de plan/status.
- Acciones admin sensibles.

Respuesta:

```json
{
  "items": [
    {
      "id": "log_id",
      "actor_id": "admin_id",
      "action": "impersonation_started",
      "tenant_id": "tenant_id",
      "reason": "Texto",
      "created_at": "2026-06-04T00:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 0,
    "pages": 0
  }
}
```

## Plan de implementacion por fases

### Fase 0: Congelar mapa real de archivos

Antes de editar, ejecutar:

```bash
rg --files
git status --short
```

Confirmar que se editaran estos archivos principales:

```text
api/api/controllers/console/myownclone/admin_platform.py
api/api/models/account.py
api/api/models/analytics.py
api/api/migrations/versions/*
replica/src/app/api/admin/[...path]/route.ts
replica/src/app/admin/resumen/page.tsx
replica/src/app/admin/tenants/page.tsx
replica/src/app/admin/feedback/page.tsx
```

No editar los duplicados en `api/controllers/*` o `api/models/*` salvo que se confirme que el runtime los usa.

Criterio de aceptacion:

- El implementador sabe cual arbol usa Flask.
- No hay cambios accidentales en archivos duplicados.

### Fase 1: Corregir modelos e imports backend

Objetivo: que las rutas admin puedan consultar `accounts` y `tenants` con SQLAlchemy real.

Tareas:

1. Revisar tablas reales `accounts` y `tenants` en migraciones/base.
2. Convertir `api/api/models/account.py` en modelos SQLAlchemy reales o importar los modelos correctos si ya existen en otro modulo.
3. Incluir al menos:

   ```py
   class Tenant(TypeBase):
       __tablename__ = "tenants"
       id
       slug
       name
       plan
       status
       subscription_status si existe
       stripe_customer_id
       stripe_subscription_id
       created_at
       updated_at
   ```

   ```py
   class Account(TypeBase):
       __tablename__ = "accounts"
       id
       tenant_id
       email
       name
       role
       is_platform_admin si existe o propiedad derivada de role
   ```

4. Cambiar en `admin_platform.py`:

   ```py
   from api.models.account import Account, Tenant
   ```

5. Corregir `_is_platform_admin` para usar `role == "platform_admin"` o el campo real.

Implementacion recomendada:

```py
def _is_platform_admin(account_id: str) -> bool:
    account = db.session.execute(
        select(Account).where(Account.id == account_id)
    ).scalar_one_or_none()
    return bool(account and account.role == "platform_admin")
```

Si existe `is_platform_admin`, soportar ambos:

```py
return bool(
    account
    and (
        getattr(account, "is_platform_admin", False)
        or getattr(account, "role", None) == "platform_admin"
    )
)
```

Criterio de aceptacion:

- `GET /console/api/myownclone/admin/overview` no falla por modelos stub.
- `_is_platform_admin` no importa desde `models.account`.
- El rol usado coincide con login JWT y DB.

### Fase 2: Normalizar auth entre Next y Flask

Objetivo: que `/admin` web pueda llamar al backend Flask sin bypass ni falso positivo.

Tareas:

1. Decidir mecanismo oficial:
   - Opcion recomendada: Next valida `next-auth`, comprueba `platform_admin`, y el proxy llama a Flask con un token backend de servicio.
   - Alternativa: Next obtiene/almacena JWT Flask por usuario y reenvia `Authorization: Bearer`.

2. Si se usa token de servicio:
   - Definir variable:

     ```text
     PLATFORM_ADMIN_TOKEN
     ```

   - En Flask, aceptar token de servicio solo en endpoints admin y mapearlo a una identidad admin auditada.
   - No usar el token como reemplazo invisible de usuario si se pierde auditoria.

3. Si se usa JWT Flask:
   - Guardar token en cookie segura o sesion.
   - Reenviar:

     ```ts
     Authorization: `Bearer ${token}`
     ```

4. En `replica/src/app/api/admin/[...path]/route.ts`:
   - Validar sesion con `auth()`.
   - Consultar usuario en Drizzle.
   - Rechazar si no es `platform_admin`.
   - Reenviar auth correcta a Flask.
   - Eliminar `ADMIN_TOKEN` si no se usa o usarlo realmente.

5. Mantener manejo de timeout 30s.

Criterio de aceptacion:

- Usuario no autenticado recibe 401.
- Usuario no admin recibe 403.
- Usuario `platform_admin` puede consultar overview/tenants.
- Flask recibe credencial esperada.
- No queda variable `ADMIN_TOKEN` muerta.

### Fase 3: Endurecer `overview`

Objetivo: metricas correctas, sin estados/planes mal contados.

Tareas:

1. Sustituir planes espanoles por canonicos:

   ```py
   plan_counts = {
       "trial": 0,
       "basic": 0,
       "pro": 0,
       "scale": 0,
       "enterprise": 0,
   }
   ```

2. Definir precios en cents:

   ```py
   plan_prices = {
       "trial": 0,
       "basic": 4900,
       "pro": 9900,
       "scale": 19900,
       "enterprise": 49900,
   }
   ```

3. Contar activos usando estados reales:

   ```py
   active_statuses = ("active", "trial")
   ```

4. Calcular costes por ventana temporal, preferiblemente ultimos 30 dias:

   ```py
   CostTracking.created_at >= now - timedelta(days=30)
   ```

5. Anadir `generated_at`.
6. Cubrir valores nulos.

Criterio de aceptacion:

- `plan_breakdown` no mezcla `básico/escala` con `basic/scale`.
- MRR no cuenta tenants suspendidos/cancelados.
- Costes indican ventana temporal.

### Fase 4: Rehacer endpoint `tenants`

Objetivo: lista paginada, filtrable y estable.

Tareas:

1. Cambiar respuesta de array plano a:

   ```json
   { "items": [], "pagination": {} }
   ```

2. Agregar filtros `status`, `plan`.
3. Agregar busqueda por `name` y `slug`.
4. Agregar `total` con query separada.
5. Agregar `clone_count` via subquery sobre `CloneConfig`.
6. Agregar `monthly_cost_cents` via subquery sobre `CostTracking`.
7. Mantener compatibilidad frontend actual actualizando `replica/src/app/admin/tenants/page.tsx`.

Criterio de aceptacion:

- Search no dispara errores con strings vacios.
- `limit` maximo 50.
- Frontend no asume array directo.

### Fase 5: Crear detalle de tenant

Objetivo: permitir inspeccion admin sin impersonar innecesariamente.

Tareas:

1. Crear clase Flask:

   ```py
   @console_ns.route("/myownclone/admin/tenants/<tenant_id>")
   class AdminTenantDetailApi(Resource):
       ...
   ```

2. Devolver:
   - Datos tenant.
   - Clones.
   - Costes 30d.
   - Gaps abiertos.
   - Preguntas top.
   - Ultima actividad si existe.

3. Crear pagina frontend futura:

   ```text
   replica/src/app/admin/tenants/[id]/page.tsx
   ```

Criterio de aceptacion:

- No hace falta impersonar para ver estado general de un tenant.
- Si tenant no existe, 404 claro.

### Fase 6: Crear endpoint admin feedback

Objetivo: que `replica/src/app/admin/feedback/page.tsx` tenga backend real.

Tareas:

1. En `admin_platform.py`, agregar:

   ```py
   @console_ns.route("/myownclone/admin/feedback")
   class AdminFeedbackApi(Resource):
       ...
   ```

2. Usar modelo:

   ```py
   Feedback
   ```

3. Hacer join con `CloneConfig` para obtener `tenant_id`.
4. Si es posible, join con `Tenant` para `tenant_name`.
5. Responder `{ items, pagination }`.
6. Actualizar frontend para aceptar el contrato nuevo.

Criterio de aceptacion:

- `/api/admin/feedback` deja de depender de datos mock o rutas inexistentes.
- Estado vacio funciona.
- Search se puede hacer server-side o client-side, pero el contrato es claro.

### Fase 7: Endurecer impersonacion

Objetivo: soporte tecnico seguro y auditable.

Tareas:

1. Validar `reason`:

   ```py
   reason: str = Field(min_length=10, max_length=1000)
   ```

2. Comprobar que `tenant_id` existe antes de crear token.
3. Asociar token y log de forma trazable.
4. Corregir `stop` para cerrar el log del token especifico.
5. No loguear token completo.
6. Considerar guardar hash del token:
   - `sha256(token + secret_pepper)`
   - comparar hashes en stop.

Criterio de aceptacion:

- No se crea impersonacion para tenant inexistente.
- Stop no cierra una sesion equivocada.
- Logs permiten auditoria.

### Fase 8: Auditoria admin

Objetivo: trazabilidad de acciones sensibles.

Tareas:

1. Si no existe tabla generica, crear migracion:

   ```text
   admin_audit_log
   ```

   Campos:

   ```text
   id
   actor_id
   action
   tenant_id
   target_type
   target_id
   reason
   metadata_json
   ip_address
   user_agent
   created_at
   ```

2. Registrar:
   - `impersonation_started`
   - `impersonation_stopped`
   - `tenant_plan_updated`
   - `tenant_status_updated`

3. Exponer:

   ```text
   GET /console/api/myownclone/admin/audit-log
   ```

Criterio de aceptacion:

- Cada accion sensible deja rastro.
- El panel puede mostrar auditoria sin consultar DB manualmente.

### Fase 9: Actualizar frontend admin para nuevo contrato

Objetivo: que el panel consuma la API endurecida.

Archivos:

```text
replica/src/app/admin/resumen/page.tsx
replica/src/app/admin/tenants/page.tsx
replica/src/app/admin/feedback/page.tsx
replica/src/app/api/admin/[...path]/route.ts
```

Tareas:

1. Adaptar `resumen` a `generated_at` y planes canonicos.
2. Adaptar `tenants` a `{ items, pagination }`.
3. Adaptar `feedback` a `{ items, pagination }`.
4. Mostrar errores reales:
   - 401
   - 403
   - 502 backend unreachable
   - 504 timeout
5. No mezclar lectura directa de Drizzle en `/api/admin/route.ts` con admin Flask salvo que se mantenga como endpoint interno separado y documentado.

Criterio de aceptacion:

- El frontend no rompe si backend devuelve lista vacia.
- El frontend no asume array plano.
- Los errores son accionables para el admin.

### Fase 10: Tests y verificacion

Backend:

1. Agregar tests para:
   - Usuario sin token: 401.
   - Usuario no admin: 403.
   - Admin: 200.
   - Overview con DB vacia.
   - Tenants paginado.
   - Feedback vacio.
   - Impersonate tenant inexistente: 404.
   - Impersonate reason corta: 400.

2. Comandos esperados:

```bash
cd api
python -m pytest
```

Si no existe pytest configurado, crear pruebas minimas o documentar el bloqueo.

Frontend:

```bash
cd replica
npm run lint
npm run typecheck
npm run test
npm run build
```

Criterio de aceptacion:

- Lint pasa.
- Typecheck pasa.
- Build pasa.
- Tests existentes pasan.
- Si algo falla por deuda preexistente, documentar archivo y error exacto.

## Pseudocodigo recomendado

### Decorador reusable para admin

Crear helper en `admin_platform.py` o modulo dedicado:

```py
def require_platform_admin():
    account, _ = current_account_with_tenant()
    if not account or not _is_platform_admin(account.id):
        return None, ({"error": "platform_admin_required"}, 403)
    return account, None
```

Uso:

```py
account, error = require_platform_admin()
if error:
    return error
```

Importante: confirmar primero como funciona `_AccountProxy`, porque `current_account_with_tenant()` devuelve proxy con atributos desde `flask.g`.

### Paginacion reusable

```py
def _pagination_args():
    page = max(int(request.args.get("page", 1)), 1)
    limit = min(max(int(request.args.get("limit", 20)), 1), 50)
    return page, limit
```

### Formato de moneda

```py
def _format_eur(cents: int) -> str:
    return f"{(cents or 0) / 100:.2f}€"
```

### Formato fecha

```py
def _iso(dt):
    return dt.isoformat() + "Z" if dt else None
```

Si `dt` ya incluye timezone, no anadir `Z` manualmente; normalizar a UTC.

## Buenas practicas obligatorias

- No usar SQL string manual salvo que sea imprescindible.
- Preferir SQLAlchemy `select`.
- No hacer `select(Tenant).all()` para calculos grandes si se puede agregacion SQL.
- No devolver tokens completos en logs.
- No capturar excepciones genericas ocultando errores sin `logger.exception`.
- No mezclar nombres de planes espanoles e ingleses en backend.
- No introducir dependencias nuevas para tareas simples.
- No modificar migraciones antiguas ya aplicadas; crear una nueva migracion.
- No cambiar contratos frontend sin actualizar TypeScript.
- No dejar variables env declaradas y sin uso.
- No confiar en cookies como auth Flask si Flask espera Bearer token.

## Checklist final de aceptacion

Backend:

- [ ] `api/api/models/account.py` tiene modelos reales o imports correctos.
- [ ] `_is_platform_admin` usa `api.models.account.Account`.
- [ ] Auth admin esta unificada entre Next y Flask.
- [ ] `overview` usa planes/estados canonicos.
- [ ] `tenants` devuelve `{ items, pagination }`.
- [ ] Existe `GET admin/feedback`.
- [ ] Impersonacion valida tenant y reason.
- [ ] Stop impersonation cierra el log correcto.
- [ ] Hay auditoria para acciones sensibles.

Frontend:

- [ ] Proxy `/api/admin/[...path]` valida `platform_admin`.
- [ ] Proxy reenvia credencial correcta a Flask.
- [ ] `resumen` consume contrato actualizado.
- [ ] `tenants` consume paginacion.
- [ ] `feedback` consume paginacion.
- [ ] Estados loading/error/empty funcionan.

Verificacion:

- [ ] `cd replica && npm run lint`
- [ ] `cd replica && npm run typecheck`
- [ ] `cd replica && npm run test`
- [ ] `cd replica && npm run build`
- [ ] Backend tests pasan o bloqueo documentado.
- [ ] Se probaron manualmente 401, 403, 200 y backend caido.

## Orden recomendado para otro modelo

1. No tocar UI todavia.
2. Arreglar modelos/imports backend.
3. Arreglar auth proxy Next -> Flask.
4. Hacer pasar `overview`.
5. Cambiar `tenants` a contrato paginado.
6. Crear `feedback`.
7. Endurecer impersonacion.
8. Agregar auditoria.
9. Actualizar pantallas admin.
10. Ejecutar lint/typecheck/test/build.

## Resultado esperado

Al terminar, MyOwnClone debe tener un backend admin que permita:

- Ver resumen real de plataforma.
- Ver tenants con busqueda, filtros y paginacion.
- Consultar detalle operativo de tenants.
- Revisar feedback de plataforma.
- Impersonar tenants de forma segura y auditable.
- Auditar acciones sensibles.
- Usar el panel Next `/admin` sin inconsistencias entre Drizzle, NextAuth y Flask.

El trabajo no se considera terminado hasta que build, typecheck y rutas admin criticas funcionen con contratos estables.

