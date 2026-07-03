# T2.2 — Fallback LLM (OpenAI) — PREPARADO, FALTA API KEY

**Fecha**: 2026-07-03
**Estado**: Infraestructura lista, **falta el API key real de OpenAI del usuario**

## Estado actual

- ✅ OpenAI `gpt-4o-mini` catalogado en `ai_models`
- ✅ Asignación `chat_fallback` con priority 100
- ⚠️ `api_key_encrypted = 'PLACEHOLDER'` — debe ser reemplazado con la key real cifrada

## Pasos para activar (cuando el usuario dé la API key)

### 1. Generar el ciphertext con SecretCipher

```bash
# En el VPS:
docker exec -it myownclone_api bash

# Dentro del contenedor:
flask --app api.app_factory generate-encrypted-key
# Te pide: OPENAI_API_KEY
# Salida: el ciphertext cifrado con AES-256-GCM
```

### 2. Actualizar la DB

```sql
-- Reemplazar el placeholder con el ciphertext generado
UPDATE ai_models
SET api_key_encrypted = '<ciphertext_de_paso_1>'
WHERE id = '019f2000-0000-0000-0000-000000000001';

-- Verificar
SELECT name, provider, LENGTH(api_key_encrypted) as key_len
FROM ai_models
WHERE provider = 'openai';
```

### 3. Verificar que el fallback funciona

```bash
# Comprobar que el registry ahora ve OpenAI como opción
docker exec myownclone_api python3 << 'EOF'
from api.app_factory import create_app
app = create_app()
with app.app_context():
    from api.core.model_registry import ModelRegistry
    from api.models.ai_models import AITask
    reg = ModelRegistry()
    # Invalidar cache para forzar recarga
    reg.invalidate()
    m = reg.get_model_for_task(tenant_id=None, task='chat_fallback')
    print(f'Provider: {m.provider}, Model: {m.model_id}')
EOF
```

## Costes estimados de OpenAI gpt-4o-mini

| Tipo | Coste |
|---|---|
| Input | $0.15 / 1M tokens |
| Output | $0.60 / 1M tokens |

A 50 usuarios: ~$2-3/mes (solo cuando MiniMax falle como fallback)

## Por qué gpt-4o-mini

- 10x más barato que `gpt-4o`
- Calidad suficiente como fallback (8B parámetros efectivos)
- Latencia baja (~500ms primer token)
- Cumple GDPR (datos en US, contrato DPA disponible)

## Asignaciones actuales de chat

| task | provider | priority | estado |
|---|---|---|---|
| chat | minimax/abab6.5s-chat | 100 | activo |
| chat_fallback | openai/gpt-4o-mini | 100 | preparado, falta key |

## Comportamiento esperado (con key)

1. Chat intenta primero MiniMax (priority 100)
2. Si MiniMax falla (circuit breaker), intenta OpenAI (chat_fallback)
3. Si ambos fallan → error al usuario

Esto ya está implementado en `api/core/retry_client.py` (T5 del Sisyphus). Solo falta la key.