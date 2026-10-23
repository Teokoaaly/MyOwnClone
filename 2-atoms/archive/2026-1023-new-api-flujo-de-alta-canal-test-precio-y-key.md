---
id: 2026-1023-new-api-flujo-de-alta-canal-test-precio-y-key
type: atom
certainty: retired
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1023-new-api-precios-por-ratio-y-expresion]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]"]
---

## Claim
El README describe el **procedimiento exacto para poner un canal en servicio**, en cuatro pasos: (1) **añadir un canal** con la clave API upstream, los modelos disponibles y la **asignación de grupo**, y **ejecutar un test de canal**; (2) **configurar el precio del modelo** y asegurar que el usuario tenga **cuota o una suscripción válida**; (3) **crear una API key** en la consola con acceso **al mismo grupo y a los mismos modelos**; (4) apuntar el cliente a `http://localhost:3000/v1` (compatible con OpenAI) y usar **la key emitida por New API**, no la del upstream. La verificación se hace con `GET /v1/models` y luego `POST /v1/responses`.

## Why It Matters
Este es el **runbook de un relay**, y es exactamente lo que distingue a un canal real de una listing: precio configurado, quota o suscripción, key por grupo, y **un test de canal** como paso previo. Un operador que publica "0.05x" en un ranking como PriceAI ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]) ha pasado por estos cuatro pasos con su propio upstream.
El orden de los pasos también revela la **dependencia entre precio y cuota**: sin precio configurado, no hay forma de validar la cuota; sin cuota, no hay suscripción que vender. Es el estado mínimo de un gateway de reventa, y por eso el producto del vault —que aún no tiene ni API de consumo ni precios públicos ([[2026-1022-myclone-tier-plans-usage-api]])— está a un nivel de madurez de considerably menor en este eje.
Y el detalle de "usar **la key de New API**, no la del upstream" es la frontera de seguridad del producto: el cliente nunca ve la clave real del proveedor, solo una credencial emitida y revocable por el gateway.


## [RETIRED]
Contenido fusionado dentro de [[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]] por regla de una idea por átomo. Fuente: [[2026-1023-new-api-gateway-unificado-de-modelos]].
