---
id: 2026-1026-new-api-redaccion-de-secretos-en-errores-y-en-el-log-de-acceso
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]", "[[2026-1022-live-verify-csp-y-headers-ahora-presentes]]"]
---

## Claim
Dos versiones cierran fugas de credenciales en la superficie de observabilidad del gateway:

- **rc.47**: el **log de acceso** ya no guarda las **claves que venían en la URL** (PR #7972, primera contribución de `ceezyyy`).
- **rc.45**: en un **error de upstream**, el **gateway oculta la dirección, la IP y la clave** que el operadorintrodujo, mientras que **los enlaces de documentación y las direcciones de correo siguen visibles**; y si el cuerpo de la petición es demasiado grande, la respuesta es **413** en lugar de un error genérico.

La misma versión rc.46 añade un tercer arreglo del mismo tipo: el **polling de una tarea ya no arrastra la clave a otra dirección** cuando la URL de polling redirige a otro host.

## Why It Matters
El patrón de fondo es **redacción de secretos en todo lo que sale del proceso**: logs, mensajes de error y redirecciones. Y el criterio de la redacción es fino: **se oculta lo que el operador introdujo (dirección, IP, clave) y se conserva lo que el usuario necesita para diagnosticar (docs, correo)**. Ese es exactamente el criterio que un producto del vault necesita cuando su superficie pública devuelve errores de un proveedor ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]).
El caso del log de acceso es el más grave del lote: un log que guarda claves de la URL **escribe la credencial en disco**, y ese disco es lo que un operador entrega al cliente o a un auditor. Es la diferencia entre un error visible y una credencial filtrada de forma persistente.
Y es una lista de verificación aplicable directamente al vault, que hoy tiene una superficie de headers y CSP en revisión ([[2026-1022-live-verify-csp-y-headers-ahora-presentes]]) y una arquitectura donde el mismo proceso tiene secretos de sesión ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]): **la pregunta correcta no es "qué errores devuelvo" sino "qué sobrevive en mis logs"**.
