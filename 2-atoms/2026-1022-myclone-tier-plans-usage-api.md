---
id: 2026-1022-myclone-tier-plans-usage-api
type: atom
certainty: solid
sources: [raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-limites-plan-free]]", "[[2026-1022-myclone-stripe-connect-monetizacion]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]"]
---
## Claim
La API de tiers de MyClone.is es **manipulable por el creator, no solo de lectura**: `GET /tier/plans` es público, mientras que `GET,POST /tier/plans`, `PUT,DELETE /tier/plans/{tier_id}` requieren auth — es decir, un creator puede **crear, editar y borrar planes** dentro de su cuenta. El consumo se expone vía `GET /tier/subscription`, `GET /tier/usage`, `GET /tier/usage/{user_id}` y `POST /tier/usage/{user_id}/refresh`. El plan Free verificado por API muestra: 5 raw text (50MB), 3 documentos (150MB), 3 multimedia (500MB, 1h), 5 vídeos YouTube (2h), 500 mensajes/mes, 10 min de voz/mes (reset 2026-07-01), 2 personas.

## Why It Matters
Que el creator pueda **definir sus propios planes** es un modelo de negocio distinto del SaaS por niveles: MyClone.is no solo cobra por plan, habilita al creator a revender su clon como producto ([[2026-1022-myclone-stripe-connect-monetizacion]]). Es la misma estrategia de "marketplace de planes" que documenta [[multi-tenant-saas]].
El `POST /tier/usage/{user_id}/refresh` es un refresco forzado de contadores, útil para soporte: el creator no espera al ciclo mensual si un cliente se quejó del consumo.
Ver [[2026-1022-myclone-limites-plan-free]] para la lectura de los límites como palanca de conversión.

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff añade la **matriz completa de límites por plan** verificada contra `GET /tier/plans` (endpoint público): `free` → 2 personas y 0 dominios propios; `pro` → 3 personas y 10 dominios; `business` → 30 personas y 10 dominios; `enterprise` → `-1` personas y `-1` dominios (sin límite). Y los contadores del plan Free tal como los ve la API: 1 persona usada de 2, `messages_limit` 500 para texto y `minutes_limit` 10 para voz.
La matriz explica por qué [[2026-1022-plan-workflows-nuestro]] propone `minimum_plan_tier_id` en sus plantillas de workflow: los workflows son la función premium (ver [[2026-1022-myclone-workflows-beta-dominio]]), y `pro` con solo 3 personas es donde tiene sentido empaquetarlos. Nótese que `pro` permite 10 dominios propios mientras `business` con 30 personas también: el límite de dominios no escala con el tamaño del plan, lo que sugiere que el custom domain es un add-on de [[2026-1022-myclone-custom-domains-whitelabel]] más que un escalón de precio.
