---
id: 2026-1026-new-api-tokens-de-acceso-con-scope-y-vencimiento
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]", "[[2026-1022-myclone-auth-jwt-account-type-creator]]", "[[2026-1022-myclone-auth-jwt-account-type-creator]]"]
---

## Claim
**v1.0.0-rc.41** sustituye el **único token de acceso del panel** por **hasta 20 tokens de acceso nombrados** en *Security & Access*. El token **se muestra una sola vez al crearlo**, **expira a los 30 días por defecto**, y sus **Scopes se quedan dentro de lo que su propietario ya puede hacer**. El **token legacy sigue funcionando 30 días** tras el upgrade, y **después se rechaza y no se puede regenerar**. Además, la gestión de usuarios por parte del admin **exige una verificación de un solo uso** para borrar, cambiar estado o rol, poner contraseña o permisos, crear admin, resetear un passkey, desactivar 2FA o limpiar un binding; **no la exige** para ajustes de cuota ni para cambiar nombre visible, grupo o nota.

## Why It Matters
Es un **cambio de modelo de credencial**, no una mejora cosmética: el token deja de ser **una credencial de administrador de larga vida** y pasa a ser **un boleto de un solo uso con caducidad por defecto y scopes derivados de los permisos reales del dueño**. El patrón "**scopes que no superan lo que el owner puede hacer**" evita la escalada de privilegios por delegación — es exactamente el punto que el vault tiene abierto en su propio modelo de sesión, donde el rol del creador y el de la cuenta conviven ([[2026-1022-myclone-auth-jwt-account-type-creator]]).
La parte que más importa al vault es el **período de gracia de 30 días** para el token legacy y el hecho de que **no se pueda regenerar**: es una **migración con fecha de caducidad irreversible**, y el release note avisa explícitamente de cambiarla antes. Un self-hoster que no lea las notas se queda sin acceso a su panel — un incidente de disponibilidad creado por un default de seguridad. Y es un punto que el vault ya tiene marcado: el modelo de sesión del gateway **no distingue por diseño entre el operador y el usuario final** ([[2026-1023-new-api-seguridad-env-vars-y-rate-limit-por-nodo]]), y sin esa distinción el único freno posible es la credencial revocable y con caducidad.
Y la verificación de un solo uso para las operaciones destructivas de administración es un control que el producto del vault **no tiene hoy**: es una **frontera explícita entre lo que es reversible (quota, nombre, grupo) y lo que no lo es (borrar, rol, 2FA, passkey)**.
