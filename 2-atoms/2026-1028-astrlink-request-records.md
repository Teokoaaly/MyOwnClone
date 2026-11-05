---
id: 2026-1028-astrlink-request-records
type: atom
certainty: solid
sources: [sources/2026-10-28-astrlink-github.md]
links: ["[[2026-1028-astrlink-on-device-privacy]]", "[[2026-1028-astrlink-model-routing]]"]
---

## Claim

AstrLink provides request records and usage tracking that inspect requests, session traces, upstream attempts, and errors, with estimated costs tracked by provider, model, and access token.

## Why It Matters

Agents and operators can inspect what happened at each step of a request: which provider was attempted, which models were tried, where errors occurred, and the estimated cost based on usage tokens. This enables debugging, cost optimization, and auditing of agent behavior over time.

## [FRICTION]

> [[2026-1024-gptgrok2api-285-estrellas-y-24-commits-con-12-tags-y-3-mes-sin-movimiento]] describe un repositorio sin actividad de commits desde julio de 2026, con 285 estrellas y 145 forks generados sobre una ventana de 12 días, y donde el ratio forks/estrellas se ha vuelto no monótono (de 0.5088 a 0.5035 en dos días sin actividad de código). Este átomo presiona la creencia de que el tracking de uso de AstrLink proporciona estimaciones de costo precisas: AstrLink reporta usage tokens solo cuando finaliza una llamada y extiende los output tokens de llamadas finalizadas de manera uniforme sobre su ventana de un minuto, mientras que repositorios sin actividad reciente pueden reportar usage de manera distinta o no reportarlo en calls que se detuvieron antes de su uso final. Las dos lecturas no se contradicen directamente —AstrLink's model se aplica a calls entrantes through the gateway, mientras que el repositorio GPTGrok2API es un proyecto independiente sin relación con el pipeline de request tracking— pero la creencia de que los patterns de usage tracking son universales ignora que AstrLink's control API returns output_tokens solo para calls finalizados y deja out counts parciales para streams que se detuvieron prematuremente. No hay inconsistencia lógica, pero sí fricción en la suposición de que el model de tracking de AstrLink se aplica sin modificaciones a todos los sistemas de inference.