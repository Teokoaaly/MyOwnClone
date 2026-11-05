---
id: 2026-1026-noones-api-de-analitica-del-historial-para-cuentas-propias-y-de-usuarios-de-tu-app
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-acceso-delegado-app-instalada-por-el-usuario]]", "[[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]", "[[2026-1024-extravm-registro-contable-sin-vinculo-a-wallets]]", "[[2026-1024-noones-tabla-de-limites-por-nivel]]"]
---

## Claim
El cuarto caso de uso de la API es el único que **cruza la frontera entre cuentas**: *"Get access to the trading history with our NoOnes API for reporting and audit. This API allows to retrieve analytics data for you own account and other users of your app."* (con el typo literal *you own account* en el texto de origen). Su caso de uso enlazado es `https://dev.noones.com/case-studies/siwp_example/`. Es decir: la API expone el **historial de trading de la cuenta propia y de los usuarios de tu app**, con los fines declarados *reporting* y *audit*.

## Why It Matters
Es la pieza que convierte a Delegated Access en un **negocio de gestión de portfolios ajenos**: la app instalada ve el historial de trades de cada usuario y puede construir sobre él informes y auditoría. Es el mismo movimiento que hace un producto de contabilidad que registra operaciones de terceros sin custodiar los fondos ([[2026-1024-extravm-registro-contable-sin-vinculo-a-wallets]]), y explica por qué el proveedor menciona *keeping track of accounting* entre los usos de Delegated Access. Dos avisos: (1) **la captura no publica qué campos ni qué granularidad** devuelve ese historial (¿trades, ofertas, pagos, countermeasures?) — nada más que "analytics data"; (2) como el historial es la memoria operativa del usuario, delegarlo es delegar **el activo más difícil de reponer tras un incidente**, así que la superficie de permisos que se importa es justamente la que no se publica ([[2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica]]).
