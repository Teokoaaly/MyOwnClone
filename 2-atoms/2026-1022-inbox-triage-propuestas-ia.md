---
id: 2026-1022-inbox-triage-propuestas-ia
type: atom
certainty: solid
sources: [raw/articles/myownclone-frontend-recon.md, raw/articles/myownclone-new-findings-may-2026.md]
links: ["[[myownclone]]", "[[2026-1022-soporte-al-cliente-separado-y-escalado]]", "[[2026-1022-dashboard-de-insights]]"]
---
## Claim
El "Triage Mode" del inbox de [[myownclone]] no envía correos automáticamente sino que genera un conjunto de *propuestas* de IA que el humano acepta: borrador de respuesta enviable, propuestas de memoria (crear o actualizar), propuestas de plantilla reutilizable y propuestas de label para auto-clasificar por intención; además ofrece historial del hilo, notas de voz con transcripción y una salida "procesar sin respuesta" (dismiss).

## Why It Matters
El diseño de "human-in-the-loop por propuestas" es lo que separa una función de soporte de una función de marketing no consentida: la IA clasifica, propone y redacta, pero el envío exige acción humana. Es la pieza operativa que sostiene el modo soporte descrito en [[2026-1022-soporte-al-cliente-separado-y-escalado]]. Las propuestas de memoria y de templates conectan el inbox con el loop de mejora del clon — cada interacción aprobada alimenta la memoria, y por tanto los gaps y preguntas que [[2026-1022-dashboard-de-insights]] agrega como intelligence de producto.

## Extensión (nuevos hallazgos, mayo 2026)
El bundle nombra el módulo como `Triage` y describe el flujo completo: la IA **lee el inbox, propone drafts en la voz del creador**, incluye **voice-to-text** y un **envío en un clic** (one-click send). El matiz relevante es que el draft sale ya con la identidad vocal del creator y que la única fricción restante es el clic — la propuesta no es un texto genérico que el humano reescribe, sino un mensaje listo para enviar. Ver [[2026-1022-mapa-modulos-internos-desde-bundles-js]] y [[2026-1022-modulo-brain-cerebro-memorias-plantillas]] (de donde salen las plantillas y las memorias que alimentan esos drafts).
