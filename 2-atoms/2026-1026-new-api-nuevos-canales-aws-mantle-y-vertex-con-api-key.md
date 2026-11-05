---
id: 2026-1026-new-api-nuevos-canales-aws-mantle-y-vertex-con-api-key
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
**v1.0.0-rc.45** añade dos formas de hablar con proveedores grandes:

1. **AWS**: los canales **AWS soportan Mantle (Messages API)**, mientras que **los que ya están en uso siguen en InvokeModel** (PR #6330, `xiaoyuyu6420`).
2. **Vertex**: en **modo API Key** hay un **campo nuevo para el project ID**, que evita un **404 en los endpoints oficiales** (PR #6330).

Además, en **rc.46** se corrige que **el sondeo de tareas arrastrara la clave a otra dirección** cuando la URL de sondeo redirigía, y en **rc.42** se **aislan las configuraciones TLS entre transportes HTTP** (PR #7627, `seefs001`).

## Why It Matters
El patrón de **compatibilidad hacia atrás en el proveedor** es la nota de producto: AWS no cambia el canal existente, **añade un modo nuevo** (Mantle), y los que ya funcionaban se quedan en InvokeModel. Es la diferencia entre **migrar a un proveedor grande** y **poder elegir entre dos protocolos del mismo proveedor** — que es justo lo que necesita un agregador que ofrece "la misma capacidad, dos precios".
El **project ID en modo API Key de Vertex** parece un detalle, pero es la diferencia entre que el canal **funcione** y que devuelva 404. Y aplica a una de las rutas de **API key** que el vault ya tiene como eje de su propio producto ([[2026-1023-new-api-una-sola-api-multiproto]]).
Los dos arreglos de seguridad son los que más pesan: **la clave no debe seguir a una redirección** (un redirect a un host del atacante se llevaba la credencial) y **aislar las configuraciones TLS entre transportes** evita que un transporte herede la tolerancia de otro — un punto crítico **justo ahora**, con el switch "Skip Upstream TLS Verification" recién introducido en rc.43 ([[2026-1026-new-api-skip-upstream-tls-verification-por-canal]]). Si los transportes comparten configuración TLS, un canal con la verificación desactivada puede **relajar la validación de otro** que no la tenía.
Para el modelo de canal del vault ([[2026-1023-priceai-transit-canal-tipo-sub2api-vs-new-api]]) esto significa que **el tipo de canal ya no se define solo por el proveedor, sino por el protocolo concreto dentro del proveedor** — y por tanto que un precio no se puede comparar solo por proveedor.
