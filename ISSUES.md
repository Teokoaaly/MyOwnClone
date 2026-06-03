# MyOwnClone — Issues Report

Generated: 2026-05-30

---

## CRÍTICO

### 1. `myownclone_public_bp` NO registrado — endpoints públicos no funcionan

**Archivo:** `api/controllers/myownclone_public.py`
**Línea:** Blueprint definido en línea 30 pero nunca registrado en la app Flask.

```python
myownclone_public_bp = Blueprint("myownclone_public", __name__, url_prefix="/api/myownclone/public")
```

Este blueprint existe pero no se importa ni se registra en:
- `api/app_factory.py`
- `api/extensions/ext_blueprints.py`
- `api/controllers/__init__.py`

**Impacto:** Los endpoints `/api/myownclone/public/clones/<slug>/chat`, `/api/myownclone/public/inbound-email`, etc. NO responden — 404.

**Fix:** Importar y registrar en `app_factory.py` o en `ext_blueprints.py`:
```python
from controllers.myownclone_public import myownclone_public_bp
app.register_blueprint(myownclone_public_bp)
```

---

### 2. `_add_memories_to_prompt` no retorna — memorias del creador nunca se injectan

**Archivo:** `api/controllers/myownclone_public.py`
**Líneas:** 273-283

```python
def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> None:
    memories = db.session.execute(select(CreatorMemory).where(...)).scalars().all()
    if memories:
        mem_text = "\n".join(f"- {m.content}" for m in memories)
        base_prompt += f"\n\nInformación importante que debes recordar:\n{mem_text}"
    # NO RETURN — base_prompt se modifica localmente pero se pierde
```

**Impacto:** El contexto de memorias del creador nunca llega al modelo IA.

**Fix:**
```python
def _add_memories_to_prompt(clone_id: str, base_prompt: str) -> str:
    # ... mismo código ...
    return base_prompt  # RETORNAR el string modificado
```

---

## ALTO

### 3. `admin_platform.py` devuelve `tenant_id` como nombre de tenant

**Archivo:** `api/controllers/console/myownclone/admin_platform.py`
**Línea:** ~169

```python
"tenant_name": data.tenant_id,  # debería ser data.tenant.name
```

---

### 4. `_is_platform_admin` demasiado permisivo

**Archivo:** `api/controllers/console/myownclone/admin_platform.py`
**Línea:** ~50-55

```python
def _is_platform_admin(account) -> bool:
    return account.role == TenantAccountRole.OWNER
```

Cualquier usuario OWNER de cualquier tenant es considerado admin de plataforma.

---

### 5. `clone.py` línea 119: iteración sobre `CloneSilo` enum

```python
for silo in CloneSilo:  # Esto itera sobre el Enum class, no sobre sus valores
```

Para iterar sobre valores usar `CloneSilo.__members__.values()`.

---

## MEDIA

### 6. `custom_domain` duplicado en `tenants` y `clone_configs`

### 7. `impersonation_tokens` usa `String(36)` en vez de `UUID`

### 8. Componentes UI vacíos

### 9. Sin SDK Supabase

### 10. `widget.js/route.ts` estructura no estándar