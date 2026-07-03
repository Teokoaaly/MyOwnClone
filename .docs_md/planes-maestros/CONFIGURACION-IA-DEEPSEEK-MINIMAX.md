# Configuración IA — DeepSeek + MiniMax (2026-07-03)

**Fecha**: 2026-07-03
**Acción**: Cambio de modelo primario de MiniMax y nuevo fallback con DeepSeek

## Contexto

MiniMax renombró sus modelos. El `model_id="abab6.5s-chat"` que teniamos en la DB **ya no existe** en la API de MiniMax (devolvia 400: "unknown model 'abab6.5s-chat'"). El chat del VPS estaba técnicamente roto.

Modelos disponibles en MiniMax ahora: `MiniMax-M3`, `MiniMax-M2.7`, `MiniMax-M2.5`, etc.

## Cambios aplicados en la DB

### 1. MiniMax actualizado

```sql
-- model_id actualizado de 'abab6.5s-chat' a 'MiniMax-M2.7' (con API key nueva)
UPDATE ai_models
SET model_id = 'MiniMax-M2.7',
    api_key_encrypted = '<nueva key cifrada con SecretCipher>',
    base_url = 'https://api.minimax.io/v1',
    updated_at = CURRENT_TIMESTAMP
WHERE id = '<id del modelo MiniMax>';
```

### 2. DeepSeek añadido como chat_fallback

```sql
INSERT INTO ai_models (
  id, name, provider, model_id, api_key_encrypted, base_url,
  capabilities, input_price_cents_per_mtok, output_price_cents_per_mtok,
  priority, is_active
) VALUES (
  '019f2000-0000-0000-0000-000000000002',
  'deepseek/deepseek-chat',
  'openai_compatible',  -- API compatible OpenAI
  'deepseek-chat',
  '<key DeepSeek cifrada>',
  'https://api.deepseek.com/v1',
  '["llm"]'::jsonb,
  14, 28, 100, true
);

-- Asignar como chat_fallback
UPDATE ai_model_assignments
SET model_id = '019f2000-0000-0000-0000-000000000002'
WHERE task = 'chat_fallback' AND tenant_id IS NULL AND is_active = true;
```

### 3. OpenAI gpt-4o-mini desactivado

```sql
UPDATE ai_models SET is_active = false
WHERE id = '019f2000-0000-0000-0000-000000000001';
```

## Estado del catálogo

| Modelo | Provider | Estado | Uso |
|---|---|---|---|
| `MiniMax-M2.7` | minimax | ✅ Activo | chat, email_classification, email_draft |
| `deepseek-chat` | openai_compatible | ✅ Activo | chat_fallback |
| `mxbai-embed-large` | local (Ollama) | ✅ Activo | embedding |
| `embo-01` | minimax | Disponible | (no asignado) |
| `llama3.2:3b` | local (Ollama) | Disponible | (no asignado) |
| `gpt-4o-mini` | openai | ❌ Inactivo | (ya no se necesita) |

## Flujo de failover

```
Request de chat
  → ModelRegistry.get_model_for_task(task=CHAT)
  → Asignación: minimax/MiniMax-M2.7 (primario)
  → Si MiniMax falla: circuit breaker abre
  → Asignación: deepseek/deepseek-chat (chat_fallback, priority 200)
  → Si DeepSeek falla: error al usuario
```

## Coste estimado

| Provider | Modelo | Coste (input) | Coste (output) |
|---|---|---|---|
| MiniMax | M2.7 | ~$0.01/1K tokens | ~$0.01/1K tokens |
| DeepSeek | chat | $0.14/MTok | $0.28/MTok |
| OpenAI | gpt-4o-mini | $0.15/MTok | $0.60/MTok |

**A 50 usuarios activos**: ~$2-4/mes con MiniMax primario + DeepSeek fallback.

## ⚠️ SEGURIDAD — Acción requerida del usuario

Las dos API keys fueron compartidas en el chat. **Rotar antes de producción**:

1. **DeepSeek**: https://platform.deepseek.com/api_keys → revocar `sk-39f3f67653754f91bd19e05174879cc5`
2. **MiniMax**: https://api.minimax.io/user-center/basic-information/interface-key → revocar `sk-cp-uH28IYHerovNI_5jI6J6UMCq-q-WTEfuhd9nlEiXQaOrJ9k0O_u0yQ0wJQXNgQZw2du9I0QADEVeh6oZDVxIp-24kRnJS17XyDhlIrvcFVGxVbbI9_NGSRs`

Después, pásame las nuevas para recifrarlas.

## Verificación de no-regresión

```bash
# 1. Healthcheck sigue verde
curl https://myownclone.com/api/admin/health  # (via nginx -> Flask)

# 2. Chat test (con usuario logueado)
# Cualquier mensaje en /resumen debe funcionar

# 3. Test de fallback (simular caída MiniMax):
docker exec myownclone_postgres psql -U postgres -d myownclone -c \
  "UPDATE ai_models SET is_active = false WHERE provider = 'minimax' AND model_id = 'MiniMax-M2.7';"
# Hacer un chat → debe usar DeepSeek automáticamente
# Reactivar:
docker exec myownclone_postgres psql -U postgres -d myownclone -c \
  "UPDATE ai_models SET is_active = true WHERE provider = 'minimax' AND model_id = 'MiniMax-M2.7';"
```