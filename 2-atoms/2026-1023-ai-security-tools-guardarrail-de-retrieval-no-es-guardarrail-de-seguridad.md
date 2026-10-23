---
id: 2026-1023-ai-security-tools-guardarrail-de-retrieval-no-es-guardarrail-de-seguridad
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-guardarrail-no-alucinar]]", "[[2026-1022-gap-observabilidad-prompts-langfuse]]", "[[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]"]
---

## Claim
El listado separa explícitamente dos cosas que el vault usa con el mismo nombre. El guardarrail que el listado monitoriza como **"LLM Red-Teaming & Guardrails"** (68 entradas) es defenses contra prompt injection, jailbreak, fuga de datos y tool misuse en la frontera del modelo: `garak` (NVIDIA), `promptfoo` (25.956 ★), `PyRIT` (Microsoft), `NeMo Guardrails`, `Guardrails AI`, `PurpleLlama`, `LLM Guard` (archivado por el mantenedor) y `Rebuff` (también archivado), más cinco modelos clasificadores de prompt injection en Hugging Face (Wolf Defender, DeBERTa v3 v2, PromptGuard, Prompt Guard 86M y `prompt-injection-sentinel`). En cambio, el control que el vault llama "guardarrail" —el umbral de comparación del retrieval que hace que el clon responda "De esto no sé" ([[2026-1022-guardarrail-no-alucinar]])— **no aparece en el listado**: no hay ninguna entrada que evalúe honestidad de recuperación o abstain-por-falta-de-evidencia.

## Why It Matters
Es una precisión que evita un error de categoría al construir el producto: la industria ya tiene un ecosistema maduro para "el modelo no debe obedecer instrucciones incrustadas", y ese ecosistema **no cubre** "el modelo no debe inventar cuando el corpus no dice". Son dos threats distintos con dos capas distintas —frontera del modelo vs. grounding del retrieval—, y confundirlos lleva a comprar (o construir) un guardarrail que no protege del problema que se quiere resolver.

También da una señal sobre la maturity del campo: las dos herramientas de referencia del guardarrail de entrada/salida más citadas por el listado (`LLM Guard` y `Rebuff`) están **archivadas por sus propios mantenedores**, y el propio README marca `LLM Guard` como "retained as a historical reference". Y como ya se vio en [[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]], el veredicto de un modelo no es prueba: en `Metis` el README advierte "model verdicts are not proof of exploitability", y en `ZeroLeaks` "model-graded results are not proof of exploitation". Sin observabilidad ([[2026-1022-gap-observabilidad-prompts-langfuse]]), un guardarrail no se puede ni medir ni afinar.
