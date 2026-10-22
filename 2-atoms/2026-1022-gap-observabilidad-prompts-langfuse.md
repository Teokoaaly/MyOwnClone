---
id: 2026-1022-gap-observabilidad-prompts-langfuse
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-langfuse-observabilidad]]", "[[2026-1022-gap-prompt-versioning-clonemodeprompt]]", "[[2026-1022-myclone-prompt-template-sistema]]"]
---
## Claim
[[myownclone]] no tiene **observabilidad de prompts**: sin integración con Langfuse, sin evaluación de calidad de las respuestas y sin tracking de tokens por prompt. MyClone.is expone `/langfuse/prompts/compile` (compila el prompt con variables), `/prompts/create`, `/prompts/list`, `/prompts/update/{name}`, más métricas a nivel de prompt (latencia, uso de tokens, quality scores) y evals custom tipo `llm-rag` y `llm-judge`.

## Why It Matters
El versionado de prompt ([[2026-1022-gap-prompt-versioning-clonemodeprompt]]) sin observabilidad es solo un historial: no dice si el cambio ayudó. Los evals `llm-judge` y las métricas por prompt son el ciclo cerrado —cambiar, medir, comparar— que convierte el tuning en ingeniería en vez de en prueba y error.
El plan lo sitúa en **Fase 4 (semana 7+)**, con impacto medio y effort medio, justo detrás de workflows y monetización: es la capa que hace escalable el trabajo manual de los otros pasos.
El `compile` de Langfuse tiene además un equivalente natural en el stack propio: la compilación de variables `{name}`, `{role}` que MyOwnClone ya necesita para sus plantillas de prompt ([[2026-1022-myclone-prompt-template-sistema]]).
