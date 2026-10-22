---
id: 2026-1022-myclone-prompt-template-sistema
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-prompt-versioning]]", "[[2026-1022-myclone-langfuse-observabilidad]]", "[[myownclone]]", "[[2026-1022-gap-campos-cloneconfig-vs-variables-myclone]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---
## Claim
MyClone.is implementa un **sistema de plantillas de prompt parametrizadas**: la plantilla por defecto ("Expert Digital Persona System Instructions") se construye con placeholders `{name}`, `{role}`, `{company}`, `{description}`, `{introduction}`, `{area_of_expertise}`, `{chat_objective}` e impone un marco de 5 fases de respuesta (Assessment → Information Gathering → Solution Reasoning → Recommendation Delivery → Experience Integration), límites de alcance ("Expertise Boundaries"), estilo de comunicación y la instrucción explícita **"NO markdown formatting in responses"**. La API lo expone vía `POST /prompt/create-advanced-prompt`, `POST /prompt/create-prompt-for-persona`, `POST /prompt-templates/` y `PATCH /prompt-templates/update-parameter`.

## Why It Matters
Es el mecanismo por el que MyClone.is convierte "una persona" en un agente: identidad, rol, empresa, objetivo de conversación y expertise se rellenan como campos, no se escriben a mano. La fase de Assessment inicial (preguntar antes de responder) es exactamente las "preguntas de activación" que en [[myownclone]] se resuelven con un interview agent: mismo objetivo, distinta implementación — aquí es una plantilla reutilizable con parámetro.
La prohibición de markdown y el tono "expert directness + casual" son detalles de contrato de output que afectan directamente a la percepción de "habla como el creador": es un mecanismo barato y replicable de "voz" sin tocar el modelo.

## Extensión (Plan de implementación 2026-06-24)
El plan de replicación fija un detalle de sintaxis que el vault no tenía: MyClone.is usa **`{{variable}}`** (doble llave) en sus prompts, mientras [[myownclone]] usa placeholders de una sola llave (`{name}`, `{role}`). Adoptar la sintaxis del competidor es una normalización barata. Y como MyOwnClone infiere vía **Dify**, la interpolación de variables debe resolverse **antes** de enviar al modelo, no en el motor de plantillas: ver [[2026-1022-gap-dify-como-capa-inferencia-prompts]].

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff **extrae la plantilla completa** y confirma 10 variables (las 7 del átomo más `thinking_style`, `objective_response` y `example_responses`), con el marco de comportamiento explícito: *Stateful Interaction* (usa el historial completo de conversación), *Progressive Disclosure* (empieza con preguntas de evaluación), *Solution Reasoning* (recolecta datos antes de recomendar) y *Evidence-Based Responses*. El handoff reitera la instrucción "NO markdown formatting in responses" y el tono "human-like, friendly, casual".
El contraste con [[myownclone]] es directo: sus prompts por modo (`DEFAULT_PROMPTS` en Flask) son **textos monolíticos** ("Eres un asistente pedagógico amable y paciente… Basa tus respuestas ÚNICAMENTE en el contenido proporcionado"), no plantillas parametrizadas. El handoff recomienda explícitamente **no** copiar el prompt de MyClone tal cual, sino adaptar sus variables a los campos existentes de `CloneConfig` — ver [[2026-1022-gap-campos-cloneconfig-vs-variables-myclone]] para el desglose de los 5 campos que faltarían.
