---
id: 2026-1026-noones-dev-noones-devuelve-contenido-mientras-la-home-bloquea-por-ip
type: atom
certainty: tentative
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]", "[[2026-1024-noones-prohibicion-explicita-de-circular-restricciones-por-ip-y-ubicacion]]", "[[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]", "[[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]"]
---

## Claim
La captura de `https://dev.noones.com/` del **2026-10-25** devuelve **contenido completo** —547 palabras de copy, cuatro casos de uso, cuatro URLs de caso de uso y dos enlaces de alta— sin ningún mensaje de jurisdicción restringida, mientras que la captura de `https://noones.com/` del **2026-10-23** devolvía exclusivamente *"You are accessing NoOnes from a restricted jurisdiction"* con la detección de IP en Estados Unidos ([[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]]). La captura **no registra desde qué IP se hizo cada una**, así que el dato duro es la asimetría entre dos subdominios del mismo operador, no la causa.

## Why It Matters
Si el bloqueo por IP se aplicara al conjunto del dominio, el portal de developers sería **inaccesible justo para quien necesita integrarse** — lo que apuntaría a un bloqueo de la tienda (donde se ve el producto y el precio) más que de la plataforma. La diferencia importa operativamente: un proveedor que expone la API pero no el producto sigue siendo **auditable en su estructura pero no en sus precios**, y eso reordena qué se puede verificar desde fuera ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]). `certainty: tentative` porque la captura no documenta la IP de origen: no se puede distinguir "el subdominio de developers no está bloqueado" de "las dos capturas se hicieron desde IPs distintas".

## [FRICTION]
> [[2026-1024-noones-bloquea-ip-estadounidense-con-mensaje-explicito]] afirma que el bloqueo de NoOnes decide **por IP, antes de cualquier cuenta o navegador**, y [[2026-1024-noones-prohibicion-explicita-de-circular-restricciones-por-ip-y-ubicacion]] añade que el proveedor advierte de no eludir las restricciones "such as by obscuring your IP address".
> Este átomo presiona esa creencia en un punto concreto: **`dev.noones.com` no devolvió muro** el 2026-10-25, con contenido real y enlaces a dos dashboards de alta.
> Ambas no pueden ser completamente correctas a la vez: o el filtro de jurisdicción es **por subdominio/ruta** (la home se bloquea, el portal de developers no), o las dos capturas se hicieron desde IPs distintas y el filtro es uniforme.
> Marcado para juicio humano, no auto-resuelto: la captura no incluye la IP de origen ni un segundo intento desde otra geolocalización.
