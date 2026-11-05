---
id: 2026-1027-github-search-temp-mail-api-temp-mail-websites
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-temp-mail-api.md]
links: ["[[2026-1027-github-search-temp-mail-api-result]]", "[[2026-1027-github-search-temp-mail-api-python-wrappers]]"]
---

## Claim

Los repositorios de temp-mail web identificados en la búsqueda de GitHub incluyen implementaciones de interfaz web para generar y ver correos temporales, siendo el caso más notable `mehmetkahya0/temp-mail` (181 estrellas, JavaScript) que provee una aplicación web completa para recibir correos electrónicos desechables.

## Why It Matters

Mientras que los wrappers Python (como `saippuakauppias/temp-mail` y `bertigert/temp-mails`) se enfocan en acceso programático a APIs de temp-mail, las implementaciones web satisfacen el caso de uso de verificación manual, pruebas rápidas y escenarios donde no hay integración de código disponible. La existencia de ambos tipos (web y Python API) refleja la dualidad de necesidades en el ecosistema de correo temporal: acceso humano directo vs integración automatizada.

## [FRICTION]

> [[2026-1027-github-search-temp-mail-api-python-wrappers]] lista tres wrappers Python principales con diferentes enfoques de cobertura de proveedores, mientras que [[2026-1027-github-search-temp-mail-api-temp-mail-websites]] se enfoca en la interfaz web. Ambas pueden ser ciertas: los wrappers dan acceso programático, mientras que las webs dan acceso directo. Sin embargo, la captura no documenta si los usuarios prefieren uno u otro, si hay superposición de funcionalidad entre wrappers y webs, o si una clase de usuario tiende a usar uno sobre el otro para casos de uso específicos.

## Nota de verificación

Los metadatos del repositorio `mehmetkahya0/temp-mail` (`stargazers_count: 181`, `language: JavaScript`, `description: "TempMail is a simple web application that allows you to generate temporary email addresses and view the emails received by these addresses."`) son **transcripción literal** de los campos `items[2]` (índice 0-based, el tercero en orden de clasificación) en la respuesta de la API de GitHub. No se verificó la capacidad real de la web para recibir y mostrar correos, la retención de mensajes, ni si la interfaz sigue operativa o ha sido tomadaDown desde la captura.