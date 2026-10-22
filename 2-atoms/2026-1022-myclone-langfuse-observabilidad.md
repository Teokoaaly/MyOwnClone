---
id: 2026-1022-myclone-langfuse-observabilidad
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-versioning]]", "[[2026-1022-myclone-prompt-template-sistema]]", "[[2026-1022-myclone-verticalizacion-y-transparencia]]", "[[2026-1022-gap-observabilidad-prompts-langfuse]]"]
---
## Claim
MyClone.is integra **Langfuse** como capa de gestión y observabilidad de prompts, con endpoints propios bajo `/api/v1/langfuse/`: `POST /prompts/compile`, `POST /prompts/create`, `GET /prompts/get/{prompt_name}`, `GET /prompts/list`, `PUT /prompts/update/{prompt_name}`. La API revela además que Langfuse se usa internamente para versionado de prompts, A/B testing, evaluación de LLM (evals tipo `llm-judge`, `llm-rag`), creación de datasets a partir de traces y compilación de prompts.

## Why It Matters
Es la infraestructura de un **equipo de producto que itera sobre prompts como código**: compilar, versionar, comparar, evaluar y construir datasets desde trazas reales es un ciclo de mejora medible, no un ajuste a mano. El eval `llm-judge` implica que el output del clon se califica automáticamente contra un criterio — es el ancestor directo de los guardrails anti-alucinación que [[myownclone]] describe como su diferenciador, pero resuelto en la capa de evaluación offline y no en la de runtime.
El hecho de que conviva con un versionado propio ([[2026-1022-myclone-prompt-versioning]]) sugiere que Langfuse es la fuente de verdad y el versionado la capa de producto.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación añade el detalle fino de que MyClone.is **compila el prompt antes de enviarlo** (`/langfuse/prompts/compile` con variables), lo que implica que la interpolación ocurre en una capa propia y no en el motor de plantillas. Y confirma que [[myownclone]] no tiene nada de esto: sin observabilidad de prompts, sin evaluación de calidad de respuestas y sin tracking de tokens por prompt. Ver [[2026-1022-gap-observabilidad-prompts-langfuse]] y [[2026-1022-gap-dify-como-capa-inferencia-prompts]].
