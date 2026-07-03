# T3.2 — IA local para chat (llama3.2:3b)

**Fecha**: 2026-07-03
**Estado**: Modelo descargado y catalogado, NO activado por defecto

## Lo que se hizo

- Descargado `llama3.2:3b` (2 GB) en Ollama del VPS
- Catalogado en `ai_models` con id `019f2000-0000-0000-0000-000000000010`
- Test de inferencia: "La capital de Francia es París" (verificado)

## NO activado por defecto

Sigue siendo **opcional** porque:
- VPS tiene solo 2.4 GB RAM libres
- Cargar el modelo usa 1.5-2 GB adicionales
- Si MiniMax está caído, podemos activarlo en caliente

## Cómo activarlo en producción

```sql
-- Cambiar la asignación de chat global de MiniMax a local
UPDATE ai_model_assignments
SET model_id = '019f2000-0000-0000-0000-000000000010'
WHERE task = 'chat' AND tenant_id IS NULL;
```

Después esperar 60s (cache TTL del ModelRegistry).

## Tiempos esperados

- Latencia: 1-5 segundos para respuestas cortas
- Tokens/seg: 30-50 (CPU-only)
- Calidad: ~80% de GPT-4o-mini (suficiente para FAQs y soporte básico)

## Consideraciones

- **NO usar** para conversaciones largas (>500 tokens) por latencia
- **SÍ usar** para soporte simple, FAQs, navegación
- **Escalable**: si subimos a VPS 8 GB, podemos usar `qwen2.5:7b` (más capaz)
