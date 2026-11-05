---
id: 2026-1031-proton-business-workspace-standard-12-99
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-vpn-pricing.md]
links: ["[[2026-1027-proton-business-vpn-pass-professional-anade-pass-integrado-alias-y-un-cli]]", "[[2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas]]"]
---

## Claim
Workspace Standard es el plan B2B todo-incluido a $12.99/user por mes que combina VPN, Pass, Mail, Calendar, Drive, Docs, Sheets y Meet con **1 TB de almacenamiento por usuario**, 15 dominios de correo personalizables y todas las funciones de los planes inferiores, añadiendo almacenamiento en la nube, calendario privado, videoconferencias y un asistente AI Lumo.

## Why It Matters
Es el **plan que cambia la regla de escalado de capacidad**: a diferencia de los planes VPN puros donde el precio es fijo por usuario, Workspace Standard ofrece 1 TB de almacenamiento por usuario con la vía explícita de "añadir más usuarios y reasignar ese almacenamiento" (ver [[2026-1024-proton-limites-de-capacidad-por-plan-500-gb-15-correos-y-50-bovedas]]). Esto significa que el coste marginal de la capacidad de almacenamiento es un precio por asiento, no por gigabyte — la variable de coste dominante pasa a ser el número de usuarios en lugar del volumen de datos. Para el vault, este plan valida la lógica de la thread `costes-por-categoria-tenant`: en un modelo multi-tenant, **la capacidad es una función del número de asientos** con panel de administración que reparte recursos, y el precio por usuario refleja ese patrón a escala completa. Además, al incluir Pass, Mail y Calendar en un solo asiento, Workspace resuelve el problema "una identidad por tenant sin dominios por tenant" de manera completa, a diferencia de VPN Essentials/Professional que solo gestionan conexiones de red.

## [FRICTION]
> [[2026-1027-proton-business-workspace-la-capacidad-se-amplia-anadiendo-usuarios]] afirma que "el almacenamiento crece con el número de asientos: añadir usuarios compra capacidad, y la reasignación se hace desde el panel de administración". Sin embargo, [[2026-1031-proton-business-workspace-standard-12-99]] claima que el modelo es "coste marginal de la capacidad es un precio por asiento, no un precio por gigabyte, haciendo que el número de usuarios sea la variable de coste dominante". Ambas pueden ser ciertas describe el mismo mecanismo desde perspectivas diferentes (capacidad vs. coste), pero el énfasis distinto — uno en la mecánica de reasignación, otro en la implicación de coste — podría generar confusión en lectores que no siguen la thread de costes-por-categoria-tenant. No hay contradicción técnica, solo diferencial de enfoque. Evaluar si merece FRICTION o puede dejarse como observación complementaria.