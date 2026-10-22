---
id: 2026-1022-pipeline-chat-actual-myownclone
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-arquitectura-rac-tres-modos-por-clon]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[retrieval-augmented-cognition]]"]
---
## Claim
El pipeline de chat real de [[myownclone]] (Flask) es: `POST /api/myownclone/public/clones/{slug}/chat` → busca `CloneConfig` por slug → busca `CloneModePrompt` por `clone_id` + modo activo → `_add_memories_to_prompt()` (concatena memorias al system prompt) → `retrieve_from_silo()` (búsqueda RAG sobre dataset de Dify) → construye `full_prompt = system_prompt + CONTEXT + user_message` → `model_instance.invoke_llm_stream()` → SSE `data: {content: chunk}` hasta `data: [DONE]`. El `CloneModePrompt` almacena **solo el prompt actual, sin historial**.

## Why It Matters
Describe el mecanismo real detrás de [[2026-1022-arquitectura-rac-tres-modos-por-clon]]: el modo no es un campo de config abstracto sino una fila de `clone_mode_prompts` que se resuelve en cada request. La ausencia de historial de prompts es exactamente el gap que cubre el versionado de MyClone.is (ver [[2026-1022-myclone-prompt-versioning]]): hoy no se puede ni recuperar ni comparar una versión anterior de un clon.
El RAG se apoya en **Dify** como dataset externo, no en una base vectorial propia — lo que significa que la fuente de verdad de los retrievals está fuera del repo, un punto de dependencia que la nota de arquitectura [[retrieval-augmented-cognition]] no explicita para este caso.
Los "silos" de los que habla el founder (aprendizaje/soporte/ventas) se resuelven en runtime por `clone_id + modo`, no por corpus separado en la tabla: los modos comparten el mismo `clone_mode_prompts` con filas distintas.
