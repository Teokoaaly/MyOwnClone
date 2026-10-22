---
id: 2026-1022-gap-custom-domains-campo-inactivo
type: atom
certainty: solid
sources: [raw/articles/myownclone-osint-implementation-plan-2026-06-24.md]
links: ["[[2026-1022-myclone-custom-domains-whitelabel]]", "[[2026-1022-gap-voz-en-vivo-myownclone]]", "[[2026-1022-plan-replicacion-myclone-fases-prioridad]]", "[[2026-1022-modulo-brain-cerebro-memorias-plantillas]]"]
---
## Claim
[[myownclone]] tiene ya un campo `custom_domain` en `CloneConfig`, pero **existe y no se usa activamente**: no hay flujo de verificación DNS, ni SSL, ni resolución del dominio en el serving del clon. MyClone.is sí tiene `POST /custom-domains`, `GET /custom-domains/lookup/{domain}` (verificación DNS), `POST /custom-domains/{id}/verify` y un límite de dominios por tier (pro: 10, business: 10, enterprise: -1).

## Why It Matters
El campo ya está en el esquema, así que el gap no es de datos sino de **infraestructura**: falta el plano de control (lookup DNS, verificación de propiedad, emisión de certificado con Let's Encrypt) y falta decidir que el dominio propio se sirve en `clon.micreador.com` en lugar de `[slug].myownclone.com`.
El límite por tier de MyClone.is es la pista de que los dominios son un recurso **cuotable y vendible**, no un extra gratis: 10 en planes medios e ilimitado solo en enterprise ([[2026-1022-myclone-custom-domains-whitelabel]]).
El plan lo sitúa en Fase 4 (semana 7+) con prioridad 🟢 BAJA, junto a voz, porque es una mejora de marca y no de conversión inmediata.
El campo ya presente en el esquema es la diferencia entre "no existe" y "existe pero inactivo", un matiz que el vault ya registra en otros módulos (ver [[2026-1022-modulo-brain-cerebro-memorias-plantillas]]).
