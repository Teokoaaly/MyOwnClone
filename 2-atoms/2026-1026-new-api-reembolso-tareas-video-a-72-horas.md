---
id: 2026-1026-new-api-reembolso-tareas-video-a-72-horas
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]"]
---

## Claim
**v1.0.0-rc.47** cambia el plazo de **reembolso de las tareas de vídeo**: antes se devolvía el saldo si la tarea pasaba de **24 horas**, ahora **por defecto se espera a 72 horas**. Si el operador ya había configurado `TASK_TIMEOUT_MINUTES`, **ese valor se respeta** y no se sobrescribe.

## Why It Matters
El plazo de reembolso es una **política de caja**, no un detalle de implementación: un gateway que reembolsa a las 24 h está liberando saldo mientras el proveedor todavía puede entregar el vídeo y, por tanto, **cobrándolo al gateway**. Pasar a 72 h duplica y media el dinero en riesgo por tarea de vídeo en curso.
Para un operador de reventa esto interactúa con la lógica de grupos y quotas ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]): la reserva de saldo de una tarea de vídeo bloquea cuota durante días, y el umbral decide si una tarea entra o se rechaza por falta de saldo.
El matiz operativo importante es el del `TASK_TIMEOUT_MINUTES` respetado: **rc.47 cambia un default, no una configuración existente**. Es un patrón de migración conservador que conviene documentar en el vault, porque significa que un despliegue upgraded y uno nuevo tienen **políticas de caja distintas** sin que nada en su configuración lo delate — el mismo tipo de divergencia invisible entre canales que aparece en la comparación de estabilidad y precio ([[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]).
Y encaja con el modelo de tareas asíncronas por plugin del gateway ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]): aquí lo que se decide es **cuánto tiempo vive una reserva de cuota sin consumo**.
