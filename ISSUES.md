# Clonify — Issues Report

Generated: 2026-05-30
Source: Auditoría completa del repositorio (dify + replica + migrations)

---

## CRÍTICO

### 1. `clonify_public_bp` NO registrado — endpoints públicos no funcionan

**Archivo:** `dify/api/controllers/clonify_public.py`
**Línea:** Blueprint definido en línea 30 pero nunca registrado en la app Flask.

```python
clonify_public_bp = Blueprint("clonify_public", __name__, url_prefix="/api/clonify/public")
```

Este blueprint existe pero no se importa ni se registra en:
- `dify/api/app_factory.py`
- `dify/extensions/ext_blueprints.py`
- `dify/api/controllers/__init__.py`

**Impacto:** Los endpoints `/api/clonify/public/clones/<slug>/chat`, `/api/clonify/public/inbound-email`, etc. NO responden — 404.

**Fix:** Importar y registrar en `app_factory.py` o en `ext_blueprints.py`:
```python
from controllers.clonify_public import clonify_public_bp
app.register_blueprint(clonify_public_bp)
```

---

### 2. `_add_memories_to_prompt` no retorna — memorias del creador nunca se injectan

**Archivo:** `dify/api/controllers/clonify_public.py`
**Líneas:** 273-283

```python
def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> None:
    memories = db.session.execute(select(CreatorMemory).where(...)).scalars().all()
    if memories:
        mem_text = "\n".join(f"- {m.content}" for m in memories)
        base_prompt += f"\n\nInformación importante que debes recordar:\n{mem_text}"
    # NO RETURN — base_prompt se modifica localmente pero se pierde
```

Python strings son inmutables. `base_prompt += ...` crea una nueva variable local que se destruye al salir de la función. El caller en línea 166 llama `system_prompt = _add_memories_to_prompt(clone.id, system_prompt)` pero ignora el return (que es None).

**Impacto:** El contexto de memorias del creador nunca llega al modelo IA — el clone no recuerda información personalizada.

**Fix:**
```python
def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> str:
    # ... mismo código ...
    return base_prompt  # RETORNAR el string modificado
```

---

## ALTO

### 3. `admin_platform.py` devuelve `tenant_id` como nombre de tenant

**Archivo:** `dify/api/controllers/console/clonify/admin_platform.py`
**Línea:** ~169

```python
"tenant_name": data.tenant_id,  # debería ser data.tenant.name
```

El nombre del tenant se muestra como UUID en el dashboard admin en lugar del nombre real.

---

### 4. `_is_platform_admin` demasiado permisivo

**Archivo:** `dify/api/controllers/console/clonify/admin_platform.py`
**Línea:** ~50-55

```python
def _is_platform_admin(account) -> bool:
    return account.role == TenantAccountRole.OWNER
```

Cualquier usuario OWNER de cualquier tenant es considerado admin de plataforma. Un owner de un plan Básico puede ver el MRR, impersonar tenants, etc.

---

### 5. `clone.py` línea 119: iteración sobre `CloneSilo` enum

```python
for silo in CloneSilo:  # Esto itera sobre el Enum class, no sobre sus valores
```

En Python, `for silo in CloneSilo` itera sobre los miembros del Enum (miembros con nombres como TEACH, SUPPORT, SALES), no sobre los valores. Para iterar sobre valores usar `CloneSilo.__members__.values()` o `[s for s in CloneSilo]`.

---

## MEDIA

### 6. `custom_domain` duplicado en `tenants` y `clone_configs`

**Migrations:**
- `b2c3d4e5f6a7` añade `custom_domain` a `tenants`
- `d4e5f6a7b8c9` añade `custom_domain` a `clone_configs`

El mismo concepto en dos sitios diferentes. Posible inconsistencia si un tenant tiene múltiples clones con diferentes domains.

---

### 7. `impersonation_tokens` usa `String(36)` en vez de `UUID`

**Migration:** `e5f6a7b8c9d0`

Todas las demás tablas Clonify usan UUID como PK/FK. Esta tabla usa `String(36)` para `id`, `admin_id`, `tenant_id`. Inconsistente.

---

### 8. Componentes UI vacíos

**Directorios:** `replica/src/components/admin/`, `components/booking/`, `components/clone/`, `components/dashboard/`, `components/inbox/`, `components/ui/`

Todos estos directorios están vacíos (solo `.` y `..`). Los componentes reales probablemente están inline en las páginas o en otros lugares.

---

### 9. Sin SDK Supabase

**Archivo:** `replica/package.json`

`.env.example` referencia variables de Supabase (`SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`) pero no hay `@supabase/supabase-js` en dependencies. El código usa `pg` raw para conexiones PostgreSQL.

---

### 10. `widget.js/route.ts` estructura no estándar

**Archivo:** `replica/src/app/widget.js/route.ts`

Los route handlers de Next.js App Router son `.ts`/`.tsx`, no `.js`. Este archivo debería renombrarse a `route.ts`.

---

## NOTES

- SMB access bloqueado (`NT_STATUS_ACCOUNT_LOCKED_OUT`) durante auditoría. Parte del código no pudo ser recuperada para revisión directa.
- `clonify_public.py` auditado completamente — 447 líneas, 7 endpoints, bug confirmado.
- Migrations verificadas — 5 archivos, 15 tablas, cadena correcta.
- API controllers verificados — 36 endpoints totales.
- Frontend auditado — 19 páginas, 18 API routes, i18n es/es, NextAuth 5.