# Cambio de embedding: MiniMax → Ollama local

**Fecha**: 2026-07-03
**Cambio**: Embedding primario global cambiado de MiniMax a Ollama local (mxbai-embed-large)

## Contexto

Antes del cambio, todos los embeddings se generaban vía API externa MiniMax (`embo-01`):
- Coste: ~$0.013 USD / 1K tokens
- Dependencia de API China (riesgo regulatorio)
- Latencia de red externa

Después del cambio:
- Coste: **$0**
- 100% local (VPS en `212.227.169.99`)
- Latencia: ~50-200ms (vs 500ms+ de API externa)
- Sin dependencia de API externa

## Cambios aplicados

### 1. Actualización de la DB
```sql
UPDATE ai_model_assignments
SET model_id = '019f12f1-adaf-7e64-8d69-e11e39ee19f6'  -- local/mxbai-embed-large
WHERE task = 'embedding'
  AND tenant_id IS NULL
  AND is_active = true;
-- Query result: UPDATE 1
```

### 2. Verificación con Flask app context
```python
from api.app_factory import create_app
from api.core.model_registry import ModelRegistry
from api.models.ai_models import AITask

app = create_app()
with app.app_context():
    reg = ModelRegistry()
    m = reg.get_model_for_task(tenant_id=None, task=AITask.EMBEDDING)
    # Provider: local
    # Model: mxbai-embed-large
    # Dimensions: 1024
    # Source: database
    # Base URL: http://ollama:11434/v1
```

### 3. Healthcheck sigue verde
```
{"checks":{"database":"ok","ollama":"ok","redis":"ok"},"status":"ready"}
```

## Coste estimado por volumen

| Escenario | Antes (MiniMax) | Después (Ollama local) |
|---|---|---|
| Beta (3 usuarios) | $0.02/mes | **$0** |
| Crecimiento (50 usuarios) | $0.98/mes | **$0** |
| Escala (500 usuarios) | $9.75/mes | **$0** + ~1 GB RAM fija |

## Compatibilidad

- **pgvector**: embeddings de 1024 dims caben perfectamente en `chunks.embedding vector(1024)`
- **API**: el cliente OpenAI-compatible en `embeddings.py` ya soporta `provider="local"` desde M8
- **Fallback**: MiniMax sigue configurado como legacy_env fallback si Ollama se cae

## Rollback

Si Ollama local da problemas:
```sql
UPDATE ai_model_assignments
SET model_id = '019f1263-24f8-7d01-bbb4-2a42343bbc4c'  -- minimax/embo-01
WHERE task = 'embedding' AND tenant_id IS NULL AND is_active = true;
```

(Esperar 60s para que el cache TTL del ModelRegistry expire)

## Notas técnicas

- El **ModelRegistry** tiene TTL de 60s en caché → cambios tardan hasta 1 minuto en aplicarse
- El `create_app()` SIEMPRE carga el contexto Flask → el test directo en shell sin contexto no refleja el flujo real
- La validación de `capabilities=["embedding"]` en `_select_assignment_row` funciona correctamente