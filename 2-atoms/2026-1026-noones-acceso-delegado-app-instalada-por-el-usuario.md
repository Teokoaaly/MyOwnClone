---
id: 2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta]]", "[[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]", "[[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]"]
---

## Claim
Delegated Access es el formato de negocio: *"Delegated Access allows you to create an app that other users can install and grant permission to manage their account—from automating trading on their behalf to keeping track of accounting."* La app se instala en el flujo del usuario final y **es el usuario quien concede el permiso**; el CTA es `https://dev.noones.com/dashboard/delegated-access`. Los dos usos nombrados son *automatizar trading en nombre del usuario* y *llevar la contabilidad de sus trades*. La captura **no enumera los permisos concretos** que se pueden delegar, ni publica tarifas, ni exige consentimiento granular.

## Why It Matters
Es el modelo de **marketplace de apps con autorización del titular**: el proveedor de la plataforma deja de ser el que opera la cuenta y pasa a ser el que **subordina su propia interfaz al tercero instalado por el usuario**. Para el vault esto se parece a lo que ya se registró con el ecosistema de aplicaciones que consumen Midjourney Proxy ([[2026-1023-midjourney-proxy-ecosistema-de-aplicaciones-que-lo-consumen]]): el valor capturable está en el **tercero que se instala encima**, no en la API. Y aquí hay una asimetría que la captura no cierra: la API promete gestionar la cuenta de un tercero, pero NoOnes ata a la identidad las funciones de **publicar ofertas** y **emitir Visa virtual** ([[2026-1024-noones-publicar-ofertas-y-visa-virtual-exigen-id]]), y la captura no dice si esos permisos heredan el nivel de verificación del usuario delegante o el de la app.
