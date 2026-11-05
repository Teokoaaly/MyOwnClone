---
id: 2026-1101-assemblyai-dictation-api-062-hora-y-120s
type: atom
certainty: solid
sources: [sources/2026-11-01-assemblyai-pricing.md]
links: ["[[2026-1101-assemblyai-sync-api-030-hora-y-134ms]]", "[[2026-1022-myclone-voice-clone]]", "[[2026-1022-myclone-limites-plan-free]]"]
---

## Claim
El Dictation API de AssemblyAI ("New") cobra **$0.62/hr** con las tres features **incluidas** en la misma tarifa: Keyterms Prompting, Prompting y Output Instruction, todos "Included". Cubre "Built on Universal-3.5 Pro across 32 languages, with clips up to 120 seconds per request. The verbatim transcript comes back alongside it" y la página cierra con: "Every feature is included in the $0.62/hr rate. One line on your bill covers the whole request — there is no second rate to model and no token math to do."

## Why It Matters
Es el endpoint que más se parece a la función "dictado" que describe el producto competidor en [[2026-1022-myclone-voice-clone]] — una utterances hablada que vuelve como texto listo para enviar, con el verbatim al lado — y por tanto el candidato natural para el input de voz del clon. Pero el precio es **el más alto de todo el catálogo de audio de AssemblyAI**: $0.62/hr frente a $0.15/hr de Universal-2, es decir 4,1× más caro por minuto. Y con el límite de 120 segundos por request, un tenant que dicta 2 minutos al día durante 30 días consume 1 hora/mes: $0,62. Barato en términos absolutos, pero con el resto del modelo de coste del vault ([[2026-1022-costes-por-categoria-tenant]]) la lección operativa es la frase literal de la página: **una sola línea de factura, sin segunda tasa que modelar** — un add-on por uso ("Output Instruction", que permite pedir la forma del texto: lista de tareas, nota clínica, mensaje de chat) no genera un coste variable adicional, lo que es unusually cleanly compatible con un modelo de precio por asiento donde lo que se factura al tenant es el uso de audio, no cada feature.
