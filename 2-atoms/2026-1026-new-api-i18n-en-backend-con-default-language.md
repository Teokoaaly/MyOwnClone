---
id: 2026-1026-new-api-i18n-en-backend-con-default-language
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-escala-adopcion-y-traduccion]]", "[[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]]", "[[2026-1023-new-api-una-sola-api-multiproto]]"]
---

## Claim
**v1.0.0-rc.43** completa la internacionalización: la consola web, **los mensajes de la API**, **los correos**, **las notificaciones** y **los logs del servidor** pasan a ser multilingüe. El backend traduce los errores para clientes de IA, correos y notificaciones **al inglés, chino simplificado o chino tradicional**, usando **primero el idioma de la cuenta** y después la cabecera **`Accept-Language`** de la petición. El idioma por defecto se fija con la variable de entorno **`DEFAULT_LANGUAGE`** (`en`, `zh-CN` o `zh-TW`), y **por defecto es `en`**. Los **logs escritos antes de esta versión conservan su texto original**.

## Why It Matters
El vault tiene una **fricción abierta y sin cerrar** sobre el idioma de los errores del propio producto ([[2026-1022-live-verify-fuga-admin-cerrada-pero-queda-i18n]]), y aquí el gateway de referencia muestra **el patrón completo de una i18n de backend**: el idioma no es un ajuste de UI, es un **atributo de la cuenta que además condiciona la respuesta que recibe un cliente programático**, con un fallback documentado (cabecera `Accept-Language`).
El detalle que más importa para el producto del vault es que **un error de API es parte del contrato**: si el error va en el idioma de la cuenta del cliente final y ese cliente es una IA, la traducción **miente sobre el contenido técnico** — y sin embargo es exactamente lo que un gateway de reventa necesita para que su error sea legible por un usuario chino.
La regla de "**los logs antiguos conservan su texto**" es la lección operativa: cambiar el idioma de los logs rompe los parsers y las búsquedas de historial, así que la migración se hace **hacia adelante, no hacia atrás**. Y el hecho de que el idioma por defecto sea `en` mientras el producto se usa masivamente en chino [[2026-1023-new-api-escala-adopcion-y-traduccion]] dice algo sobre **quién es el usuario real de este software**: no el operador occidental del vault, sino el operador chino que revende en yuanes.
