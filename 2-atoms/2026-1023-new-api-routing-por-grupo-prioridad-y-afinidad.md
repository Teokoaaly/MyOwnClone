---
id: 2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-gateway-unificado-de-modelos]]", "[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]"]
---

## Claim
La tabla de capacidades de New API define el **modelo de canal y de routing**: un canal es una **clave upstream con los modelos disponibles y una asignación de grupo**, y el routing se decide por **mapeos de modelo, prioridades y pesos de canal, reintentos, afinidad de canal y múltiples claves upstream**. Los grupos son la unidad de asignación transversal: un canal se crea con su `group assignment`, y **una API key creada en la consola debe tener acceso al mismo grupo y a los mismos modelos** que el canal. El propio historial de commits del repositorio confirma el vocabulary: *"the usual **group, priority, weight, affinity and channel-pin** rules"*.

## Why It Matters
Este es el **mecanismo exacto** que convierte "un proveedor" en "una piscina de proveedores con reglas de reparto": prioridad, peso, afinidad y pin. Es la maquinaria de la que habla la dispersión de multiplicadores del ranking de relays ([[2026-1023-priceai-transit-dispersion-de-multiplicadores]]) — el operador decide qué canal sirve a qué grupo y con qué prioridad, y eso a su vez es lo que le permite vender **el mismo modelo a precios distintos** a distintos grupos ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]).
El dato duro y reutilizable es la **fricción operativa** de la asignación grupo↔canal↔key: no basta con añadir un canal, la key del cliente tiene que arrastrar el grupo correcto o la request no se enruta. Para el vault, cualquier diseño de "un solo gateway, varias marcas" hereda exactamente esta regla.

## Extensión (runbook de alta de un canal)
El README describe el **procedimiento exacto para poner un canal en servicio**, en cuatro pasos: (1) **añadir un canal** con la clave API upstream, los modelos disponibles y la **asignación de grupo**, y **ejecutar un test de canal**; (2) **configurar el precio del modelo** y asegurar que el usuario tenga **cuota o una suscripción válida**; (3) **crear una API key** en la consola con acceso **al mismo grupo y a los mismos modelos**; (4) apuntar el cliente a `http://localhost:3000/v1` (compatible con OpenAI) y usar **la key emitida por New API**, no la del upstream. Verificación con `GET /v1/models` y luego `POST /v1/responses`.
Es el **runbook de un relay**, y distingue un canal real de una listing: precio configurado, quota o suscripción, key por grupo y **test de canal** como paso previo. Un operador que publica "0.05x" en un ranking como PriceAI ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]) ha pasado por estos cuatro pasos con su propio upstream. El orden también revela la **dependencia entre precio y cuota**: sin precio no se valida la cuota; sin cuota no hay suscripción que vender — el estado mínimo de un gateway de reventa, frente a un producto que aún no tiene ni API de consumo ni precios públicos ([[2026-1022-myclone-tier-plans-usage-api]]). Y el detalle "usar **la key de New API**, no la del upstream" marca la frontera de seguridad: el cliente nunca ve la clave real del proveedor, solo una credencial emitida y revocable por el gateway.
