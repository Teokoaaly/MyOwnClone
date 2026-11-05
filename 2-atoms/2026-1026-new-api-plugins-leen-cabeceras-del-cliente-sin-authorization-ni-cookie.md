---
id: 2026-1026-new-api-plugins-leen-cabeceras-del-cliente-sin-authorization-ni-cookie
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]", "[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1026-new-api-utils-fetch-y-dominios-declarados]]"]
---

## Claim
**v1.0.0-rc.47** amplía lo que ve un **plugin de tarea**: ahora puede **leer las cabeceras de la petición del cliente**, pero **Authorization y Cookie no se le pasan**. La misma versión añade **subida de ficheros en las rutas nativas del plugin** y la posibilidad de que el plugin use las cabeceras del cliente.

## Why It Matters
Define una **frontera de credenciales explícita dentro del sandbox**: el plugin ve metadatos de la petición del cliente (por ejemplo cabeceras de proveedor que el gateway reenvía), pero **nunca la credencial del cliente ni su cookie de sesión**. Eso es una decisión de diseño transferible —un tercero con acceso a tráfico de usuario no debe poder suplantar al usuario— y encaja con el modelo de plugin que ya documenta el vault, donde el plugin no decide cuánto cobra pero tampoco puede declarar cifras arbitrarias ([[2026-1023-new-api-plugins-de-tareas-js-en-sandbox]]).
Para el vault que evalúa este software como capa de inferencia, la lección es de **superficie de confianza por componente**: el gateway ya era un punto de concentración de secretos (`SESSION_SECRET`, `CRYPTO_SECRET`, claves upstream) ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]); que el plugin de tareas sea un **tercer actor con código de terceros** que además puede **salir a la red** ([[2026-1026-new-api-utils-fetch-y-dominios-declarados]]) convierte el sandbox en la parte más sensible del sistema, y por tanto la que más conviene auditar antes de auto-hospedar.
