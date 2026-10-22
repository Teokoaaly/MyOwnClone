---
id: thread-myownclone-vs-myclone-is
type: thread
updated: 2026-10-22
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md, raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[myownclone]]", "[[myownclone-vs-delfi]]", "[[ai-clones-market]]"]
---

# Thread — MyOwnClone vs MyClone.is

Síntesis del material atomizado el 2026-10-22. Fuentes: 10 documentos OSINT en `raw/articles/` (Mayo–Junio 2026), atomizados en 107 notas de `2-atoms/`.

## Tesis del thread

MyClone.is es el competidor más dangerous y el más documentado del mapa. No compite por ser el clon más parecido a una persona famous: compite por **operationalizar** la clonificación — 227 endpoints REST, versionado de prompts, workflows, Stripe Connect para el creador, observabilidad Langfuse, voz con tres proveedores y dominios propios. Our product tiene la arquitectura más limpia (tres silos explícitos, modos, memorias) pero **apenas expone superficie de API**: es un back-office RSC-first sin contrato público.

Esto invierte la lectura del mapa de competencia heredado (`[[2026-1022-solo-personify-compite-de-verdad]]`): el mapa de mayo decía "solo Personify compite de verdad" y no mencionaba MyClone.is. Ese atom ahora lleva la fricción correspondiente.

## Ejes de comparación

| Eje | MyClone.is (verificado) | MyOwnClone (verificado en código) | Átomos |
|---|---|---|---|
| Superficie API | 227 endpoints, OpenAPI v1/v2, envoltura `{data, error}` | RSC + Server Actions; sin REST público | [[2026-1022-myclone-api-superficie-227-endpoints]], [[2026-1022-mutaciones-rsc-sin-api-rest]], [[2026-1022-api-privada-sin-documentacion]] |
| Versionado de prompts | Objetos `PromptVersion` con `change_summary`, `created_by`, timeline y diff | `CloneModePrompt` es un único campo sobrescribible; sin historial | [[2026-1022-myclone-prompt-versioning]], [[2026-1022-gap-prompt-versioning-clonemodeprompt]] |
| Memoria / modos | Los modos no aparecen en su API | Tres silos (knowledge/terms/personality) + modos + memorias | [[2026-1022-myclone-carece-modos-memories-ni-visitors]], [[2026-1022-arquitectura-rac-tres-modos-por-clon]], [[2026-1022-modulo-brain-cerebro-memorias-plantillas]] |
| Workflows | `Workflow` con ciclo de vida, `output_template`, scoring de leads | Cero: solo chat libre | [[2026-1022-myclone-workflows-beta-dominio]], [[2026-1022-gap-workflows-myownclone]] |
| Monetización del creador | Stripe Connect | El creador no cobra; solo planes de plataforma | [[2026-1022-myclone-stripe-connect-monetizacion]], [[2026-1022-gap-monetizacion-creador-stripe-connect]] |
| Voz | 3 orígenes × 2 proveedores (Cartesia/ElevenLabs) + LiveKit | Sin voz; LiveKit también ausente | [[2026-1022-myclone-voice-providers-cartesia-elevenlabs]], [[2026-1022-myclone-voice-clone]], [[2026-1022-gap-voz-en-vivo-myownclone]] |
| Observabilidad | Langfuse + evals + tracking de tokens | Ninguna | [[2026-1022-myclone-langfuse-observabilidad]], [[2026-1022-gap-observabilidad-prompts-langfuse]] |
| Captura de leads | `/personas/{id}/visitors` + `capture-lead` | No existe tabla de visitantes; solo `Feedback` con rating | [[2026-1022-myownclone-ventajas-sobre-myclone]], [[2026-1022-gap-lead-capture-visitors]] |
| Streaming | SSE + LiveKit | SSE sobre Dify RAG, sin historial en el prompt | [[2026-1022-myclone-chat-streaming-sse]], [[2026-1022-pipeline-chat-actual-myownclone]] |
| Dominios propios | Custom domains + whitelabel | Campo `custom_domain` existe pero inactivo | [[2026-1022-myclone-custom-domains-whitelabel]], [[2026-1022-gap-custom-domains-campo-inactivo]] |

## El gap estructural de our platform

El handoff de junio documenta que nuestro producto son **dos repos independientes** (Flask/SQLAlchemy en 5001 + Next.js/Drizzle en 3000) donde el frontend escribe Drizzle directamente y bypasea Flask, con dos sistemas de auth desconectados y cuatro bugs de drift de schema. Eso no es una nota de OSINT del competidor: es una descripción de our own code, verificada contra `api/api/models/clone.py`. Es el hallazgo más accionable de todo el lote y no aparece en ninguna nota legacy.

Ver [[2026-1022-myownclone-dos-repos-flask-nextjs]], [[2026-1022-auth-flask-nextauth-desconectados]], [[2026-1022-drift-schema-drizzle-sqlalchemy]], [[2026-1022-bug-enum-modos-teach-vs-pedagogy]].

## Fricciones que quedan para juicio humano

1. **Mapa de competencia desactualizado** — [[2026-1022-solo-personify-compite-de-verdad]] vs [[2026-1022-myclone-verticalizacion-y-transparencia]]: el mapa de `comparisons/myownclone-competitors.md` no menciona a MyClone.is.
2. **Onboarding contradictorio** — el código tiene un funnel de 4 pasos y signup público ([[2026-1022-onboarding-cuatro-pasos-encuestas]]) pero `/registro` redirige a `/contacto` ([[2026-1022-onboarding-manual-sin-self-service]]). Ambos son ciertos en momentos distintos; el estado real del alta no está verificado.
3. **"Ventaja" que puede no ser ventaja** — [[2026-1022-myclone-carece-modos-memories-ni-visitors]] afirma que MyClone.is no tiene modos/memorias, pero su propia lista de endpoints incluye `visitors` y `capture-lead`. El handoff se contradice sobre el alcance de la ventaja.
4. **Prioridad de roadmap en conflicto** — el founder dice MVP primero ([[2026-1022-mvp-salir-al-mercado-pronto]]); el handoff interno marca el versionado de prompts como 🔴 ALTA y primero ([[2026-1022-plan-orden-implementacion-myownclone]]).
5. **Delfi** — el transcript solo sostiene que Delfi "no solamente te responda con lo que tú ya le has puesto de conocimiento"; la nota legacy [[myownclone-vs-delfi]] va más lejos al atribuirle alucinación.

## Certezas

- `solid` (81 átomos): hechos observados directamente (conteos de endpoints, headers HTTP, versiones de framework, código de our own repo).
- `tentative` (27 átomos): inferencias, rutas deducidas de bundles JS, afirmaciones del founder y planes de trabajo.

La línea entre ambos es real y no se ha difuminado: los endpoints "inferidos de JS" del deep-dive de junio están marcados `tentative`; la superficie de 227 endpoints confirmada por OpenAPI está marcada `solid`.
