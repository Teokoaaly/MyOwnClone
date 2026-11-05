---
id: 2026-1026-noones-acceso-directo-limitado-a-tu-propia-cuenta
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]", "[[2026-1022-api-privada-sin-documentacion]]", "[[2026-1026-noones-bot-de-saludo-al-iniciar-el-trade]]", "[[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]"]
---

## Claim
Direct Access está definido por su techo: *"Use NoOnes's APIs to create an app that can only access and automate your own NoOnes account."* Es decir, la app que se construye bajo este formato **no puede tocar la cuenta de nadie más** — opera exclusivamente sobre la cuenta de quien la instala. La captura no publica para este formato ningún endpoint, precio, rate limit ni SLA; el único enlace es `https://dev.noones.com/dashboard/direct-access`.

## Why It Matters
Es el formato **trivialmente seguro y trivialmente limited**: no hay superficie de permisos, no hay autorización delegada, no hay responsabilidad sobre cuentas ajenas — y por tanto **tampoco hay negocio por sí solo**. Todo el valor que el proveedor quiere capturar está en el otro formato ([[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]): Direct Access sirve para que un operador automatice su propia operativa y para que el proveedor documente un camino de entrada sin fricción, pero **el modelo de ingresos solo puede estar en Delegated** (tarifa por app instalada, por transacción, por cuenta gestionada) — y ninguno de esos importes aparece en la captura. Es también el patrón que el vault ya vio en la API privada de MyOwnClone: la superficie existe pero el contrato comercial no ([[2026-1022-api-privada-sin-documentacion]]), y es el mismo camino de una sola vía que ya se registró en NoOnes con el catálogo de países no enumerable ([[2026-1024-noones-catalogo-de-paises-soportados-y-150-mas]]).
