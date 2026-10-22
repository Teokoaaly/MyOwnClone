---
id: 2026-1022-plan-langfuse-instrumentacion-nuestra
type: atom
certainty: tentative
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-langfuse-observabilidad]]", "[[2026-1022-pipeline-chat-actual-myownclone]]", "[[2026-1022-plan-orden-implementacion-myownclone]]"]
---
## Claim
El paso 5 del handoff propone integrar **Langfuse** en [[myownclone]] para observar prompts en producción: `pip install langfuse`, cliente con `LANGFUSE_PUBLIC_KEY`/`LANGFUSE_SECRET_KEY` y host `cloud.langfuse.com` o self-hosted, y tracing del pipeline de chat con `langfuse.trace(name="clone-chat", metadata={"clone_id":..., "mode":...})` y un span `llm-inference` alrededor de `model_instance.invoke_llm()`,strumentado en `api/core/myownclone/email_ai.py` y `api/core/retrieval.py`. Es el último paso de la roadmap, "producción / observabilidad".

## Why It Matters
MyClone.is usa Langfuse como capa de gestión **y** observabilidad de prompts, con eval types `llm-judge` y `llm-rag` (ver [[2026-1022-myclone-langfuse-observabilidad]]). Adopción equivalente convierte el prompt de [[myownclone]] en un artefacto medible: hoy el `system_prompt` es una cadena opaca en `clone_mode_prompts` (ver [[2026-1022-pipeline-chat-actual-myownclone]]) sin historial ni trazabilidad, lo que hace imposible responder "¿por qué el clon dijo eso?".
El handoff coloca Langfuse el último por una razón de orden: sin versionado de prompts (Step 1) ni instrumentación de datos, el tracing da información pero no un ciclo de mejora; con la observabilidad primero, se invierte la dependencia.
Matiz: instrumentar `email_ai.py` y `retrieval.py` además del chat sugiere que la intención es medir coste y calidad de la generación de borradores de email, no solo del chat. `tentative`: es plan.
