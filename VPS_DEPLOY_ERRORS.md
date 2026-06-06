# MyOwnClone — Errores de Despliegue en VPS

Registro de problemas encontrados durante el despliegue en VPS, con sus causas y soluciones.

## Entorno

- **Repo:** https://github.com/Teokoaaly/MyOwnClone
- **VPS IP pública:** `85.87.120.247`
- **VPS Tailscale:** `100.111.27.123`
- **Puerto SSH (original):** 22/tcp — bloqueado por firewall en algunos momentos
- **Puertos accesibles:** 3001 (FreeLLMAPI), 80, 443, 8080
- **Contraseña root VPS:** `killer`

---

## Error 1 — SSH sin contraseña

**Síntoma:** `ssh root@100.99.222.101` pedía password interactivo o fallaba.

**Causa:** Sin clave SSH configurada, el servidor pedía password.

**Solución:** Usar `sshpass -p 'killer' ssh -o StrictHostKeyChecking=no root@100.99.222.101`.

```bash
sshpass -p 'killer' ssh -o StrictHostKeyChecking=no root@100.99.222.101 "comando"
```

---

## Error 2 — ModuleNotFoundError: No module named 'models.myownclone'

**Síntoma:** La API fallaba al iniciar con:

```
ModuleNotFoundError: No module named 'models.myownclone'
```

**Causa:** El `PYTHONPATH` en docker-compose no incluía `/app`, que es donde el código de la aplicación reside dentro del contenedor.

**Solución:** Añadir `PYTHONPATH: /app` en el servicio `api` del docker-compose.yml y rebuild:

```yaml
services:
  api:
    environment:
      - PYTHONPATH=/app
```

```bash
docker compose up -d --build api
```

---

## Error 3 — Dos directorios `models/` en el contenedor

**Síntoma:** Imports ambiguos, algunos resolved a un `models/` vacío y otros al correcto.

**Causa:** Existían dos rutas:
- `/app/models/` — stub vacío (solo account)
- `/app/api/models/` — el código real

**Solución:** Asegurar que todos los imports usen la ruta absoluta desde `/app/api/`, ej:
```python
from api.models.myownclone import CloneConfig
```
No usar imports relativos que puedan resolver al `models/` incorrecto.

---

## Error 4 — SyntaxError en models/base.py (docstring sin comillas)

**Síntoma:** La API entraba en crash loop con:

```
SyntaxError: invalid syntax ... models/base.py line 24
```

**Causa:** La clase `DefaultFieldsDCMixin` tenía un docstring con `#` en lugar de triple-quotes `"""`:

```python
# Incorrecto:
class DefaultFieldsDCMixin:
    # Mixin that adds created_at, updated_at, created_by to a model.
    created_at: Mapped[datetime] = mapped_column(

# Correcto:
class DefaultFieldsDCMixin:
    """Mixin that adds created_at, updated_at, created_by to a model."""
    created_at: Mapped[datetime] = mapped_column(
```

**Solución:** Fix manual dentro del contenedor:

```bash
docker cp /tmp/base_fix.py myownclone_api:/tmp/base_fix.py
docker exec myownclone_api cp /tmp/base_fix.py /app/api/models/base.py
docker restart myownclone_api
```

---

## Error 5 — Import path incorrecto: `from core.myownclone.email_ai`

**Síntoma:** `ImportError: attempted relative import beyond top-level package`

**Causa:** Archivos en `api/controllers/console/myownclone/` usaban:
```python
from core.myownclone.email_ai import ...
```

**Solución:** Corregir a la ruta absoluta desde `/app`:

```python
from api.core.myownclone.email_ai import ...
```

Aplicar con sed en todos los archivos:

```bash
sed -i 's/from core.myownclone.email_ai/from api.core.myownclone.email_ai/g' \
  api/controllers/console/myownclone/inbox.py
```

---

## Error 6 — ImportError en migrations: relative import beyond top-level package

**Síntoma:**

```
ImportError: attempted relative import beyond top-level package
  models/analytics.py:12 → from ..base import DefaultFieldsDCMixin, TypeBase
```

**Causa:** El archivo de migración usaba imports relativos que no funcionan cuando Flask-Migrate ejecuta las migraciones fuera del contexto del paquete de la aplicación.

**Solución:** Modificar el archivo de migración para usar imports absolutos desde `api.models`:

```python
# En el archivo de migración, cambiar:
from ..base import DefaultFieldsDCMixin, TypeBase
# Por:
from api.models.base import DefaultFieldsDCMixin, TypeBase
```

---

## Error 7 — Base de datos vacía (0 tablas)

**Síntoma:** `docker exec myownclone_postgres psql -U postgres -d myownclone -c "\dt"` devolvía 0 tablas.

**Causa:** Las migraciones nunca se ejecutaron exitosamente debido al Error 6.

**Solución:** Después de arreglar los imports en las migraciones:

```bash
docker exec myownclone_api flask db upgrade
# o
docker exec myownclone_api python -m flask db upgrade
```

---

## Error 8 — Swagger 500: CloneConfigResponse no registrado

**Síntoma:** `GET /console/api/` devolvía 500 con `Model cls CloneConfigResponse not registered`.

**Causa:** `CloneConfigResponse` nunca se registró en el API namespace con `register_response_schema_models`.

**Solución:** Registrar el modelo en el helper de schema. Añadir esta línea después de cada `namespace.schema_model()`:

```python
namespace.schema_model(
    schema_to_register.get("title", name),
    schema_to_register
)
# También registrar con el nombre completo del modelo para resolución cruzada
namespace.schema_model(name, schema_to_register)
```

---

## Error 9 — Puerto incorrecto en Dockerfile (5001 vs 5000)

**Síntoma:** La API respondía en el puerto incorrecto según la configuración esperada.

**Causa:** El Dockerfile tenía `EXPOSE 5001` y `CMD flask run --port 5001`, pero el docker-compose esperaba 5000.

**Solución:**

```bash
sed -i 's/5001/5000/g' api/Dockerfile
```

---

## Error 10 — Puerto SSH 22 bloqueado por firewall en VPS

**Síntoma:** `ssh root@100.99.222.101` → `Connection refused`

**Causa:** El firewall del VPS solo tenía abiertos los puertos 80, 443, 3001, 8080. El 22 estaba bloqueado.

**Detalle:** Los servicios en el VPS seguían funcionando (FreeLLMAPI en 3001 respondía), solo SSH estaba bloqueado.

**Solución alternativa:** Usar los endpoints HTTP disponibles para verificar el estado del VPS, o abrir el puerto 22 desde la consola de proveedor cloud.

---

## Error 11 — VIP VPS: IP cambió durante el despliegue

**Síntoma:** La IP `100.99.222.101` dejó de responder en SSH, los servicios seguían en otros puertos.

**Causa:** La IP pública del VPS cambió.

**Solución:** Verificar la IP pública actual desde la consola del proveedor cloud. En el momento del despliegue:
- IP pública: `85.87.120.247`
- Tailscale: `100.111.27.123`

---

## Servicios en el VPS (estado actual)

| Servicio | Puerto | Estado |
|----------|--------|--------|
| FreeLLMAPI | 3001 | UP |
| Nginx | 80, 443 | UP |
| Weaviate | 8080 | UP |
| SSH | 22 | BLOQUEADO |

---

## Comandos de diagnóstico en VPS

```bash
# Estado de contenedores
docker ps -a

# Logs de la API
docker logs myownclone_api --tail 50

# Ver tablas en DB
docker exec myownclone_postgres psql -U postgres -d myownclone -c "\dt"

# Verificar estado de servicios
curl -s http://localhost:3001/v1/models | python3 -m json.tool | head -5

# Reiniciar API
docker restart myownclone_api

# Verificar puertos abiertos
nc -zv -w 3 85.87.120.247 3001
```

---

## Checklist antes de desplegar

- [ ] Verificar IP actual del VPS
- [ ] Confirmar que SSH (22) está accesible O tener plan alternativo (HTTP check)
- [ ] Asegurar que todas las clases con docstrings usan triple-quotes `"""`, no `#`
- [ ] Verificar que PYTHONPATH=/app está configurado en docker-compose
- [ ]确认 imports usan rutas absolutas desde `/app/api/` (no relativos con `..`)
- [ ] Ejecutar `flask db upgrade` después de cada cambio de modelo
- [ ] Verificar 0 tablas en DB antes de asumir que las migraciones funcionaron