---
id: 2026-1026-new-api-playground-por-cuenta-y-busqueda-por-grupo
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]", "[[2026-1026-new-api-canales-y-plugins-competen-por-prioridad-y-peso]]"]
---

## Claim
**v1.0.0-rc.44** cambia el almacenamiento del **playground**: pasa a ser **por cuenta**, y **el historial anterior se borra una vez** tras el upgrade. En **rc.42** los usuarios **se pueden filtrar por grupo de usuario** ("Users can be filtered by User Group"). En **rc.45** los tokens de acceso ganan el interruptor **"Allow querying user quota"** ("允许查询用户额度"): **los tokens nuevos lo traen activado y los antiguos siguen desactivados**.

## Why It Matters
El **playground por cuenta** es una corrección de **aislamiento de datos**: si el historial era compartido, un usuario podía ver las conversaciones de otro en la misma instancia. Es un cambio de modelo de datos, no de UI, y tiene un coste explícito — **se borra el historial** — que es exactamente el tipo de precio que hay que pagar al cambiar la granularidad del aislamiento ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]).
El **filtro por grupo** conecta directamente con el modelo de routing: si el **grupo** decide a qué canales y a qué precio accede un usuario, la consola de administración **debe poder segmentar por grupo**, porque es la unidad de la decisión comercial. Sin ese filtro, el operador no puede ni medir ni auditar por segmento ([[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]).
Y el interruptor **"Allow querying user quota"** es una **decisión de default con historia**: *nuevos activados, antiguos desactivados*. Es un cambio de default que solo afecta a las credenciales nuevas — una convención de seguridad conservative y sensata, muy distinta del de la **filtración de palabras sensibles**, que se invirtió para todos ([[2026-1026-new-api-filtrado-de-palabras-sensible-off-por-defecto]]). La comparación es útil: **el mismo producto elige defaults opuestos en dos casos** — uno por What's Changed (nuevos sí, antiguos no), otro por interruptor apagado — y el vault debería registrar esa inconsistencia como **dato de diseño, no como error**.
