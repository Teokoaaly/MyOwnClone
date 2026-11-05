---
id: 2026-1027-proton-business-workspace-la-capacidad-se-amplia-anadiendo-usuarios
type: atom
certainty: solid
sources: [sources/2026-10-26-proton-business-plans.md]
links: ["[[2026-1027-proton-business-mail-limites-por-usuario-almacenamiento-y-direcciones-y-dominios]]", "[[2026-1022-costes-por-categoria-tenant]]", "[[2026-1027-proton-business-mail-escalera-por-usuario-6-99-12-99-19-99]]"]
---

## Claim
La FAQ "What if I reach my plan's storage limit?" da la vía de escalado explícita: "simply **add more users and reallocate that storage** or upgrade to a plan that offers more storage. For large organizations, you can customize your storage with a Proton Enterprise plan by contacting our Sales team". Es decir, **el almacenamiento crece con el número de asientos**: añadir usuarios compra capacidad, y la reasignación se hace desde el panel de administración. La FAQ "What is a user?" define el asiento: "Users are **accounts in your organization that aren't administrators**... They can't view or manage any details at the organization level", y el administrador puede "add or remove users, as well as **allocate storage and VPN connections**, from your admin panel".

## Why It Matters
Es la **regla de escalado del modelo de producto multi-tenant escrita por el proveedor**, y es la pieza que faltaba en la thread: **capacidad = función del número de asientos**, con un panel de administración que reparte almacenamiento y conexiones entre usuarios sin que estos vean nada del nivel organizativo. La consecuencia para un producto como el del vault es directa: la lógica "coste por tenant" que separa `categoryCloneResponses`, `categoryIngestion` y `categoryPlatformOps` ([[2026-1022-costes-por-categoria-tenant]]) tiene un precedente externo de **capacidad asignable por asiento** — el mismo patrón de "plataforma que reparte recursos entre tenants" que ya es la arquitectura de MyOwnClone. Y hay una segunda lectura, más incómoda: **añadir usuarios como vía de compra de almacenamiento significa que el coste marginal de la capacidad es un precio por asiento, no un precio por gigabyte**, lo que hace que el número de usuarios del cliente sea la variable de coste dominante en vez del volumen de datos.
