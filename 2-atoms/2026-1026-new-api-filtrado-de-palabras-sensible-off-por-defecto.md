---
id: 2026-1026-new-api-filtrado-de-palabras-sensible-off-por-defecto
type: atom
certainty: solid
sources: [sources/2026-10-25-new-api-releases.md]
links: ["[[2026-1023-new-api-aviso-legal-para-reventa-publica]]", "[[2026-1023-new-api-una-sola-api-multiproto]]", "[[2026-1022-superficie-legal-publica-dpa-clon-terms]]"]
---

## Claim
**v1.0.0-rc.45** cambia el default del **filtrado de palabras sensibles**: pasa a estar **desactivado por defecto** y, si además se había rellenado una lista pero **nunca se guardó el interruptor**, esa lista **se borra**. Para reactivarlo hay que ir a **"Request checks"** y encenderlo tras el upgrade. El commit es *"disable sensitive word filtering by default and clear list"* (PR #7814, `seefs001`).

## Why It Matters
Es un default de seguridad y de cumplimiento que se invierte **sin migración de configuración**: el operador que tenía una lista escrita pero no guardada **pierde el filtro** al actualizar, y tiene que saber que existe para reencenderlo.
Para un vault que documenta la reventa de API como sector con obligaciones de **seguridad de contenido**, esto es un hecho de configuración, no un detalle ([[2026-1023-new-api-aviso-legal-para-reventa-publica]]): el software de gateway más desplegado del sector **no filtra palabras sensibles por defecto**, y quien opera un servicio público tiene que activarlo él mismo o asumir que no lo hace.
Y hay un matiz de superficie que no conviene perder: el interruptor vive en **"Request checks"**, es decir, en la **capa de petición del gateway**, no en el modelo. Es el único mecanismo de moderación de contenido de la pieza que decide **qué modelo sirve a qué grupo de usuarios** ([[2026-1023-new-api-una-sola-api-multiproto]]) — el punto exacto donde el producto del vault tiene su propia superficie legal y de terminación de cuentas ([[2026-1022-superficie-legal-publica-dpa-clon-terms]]).

## [FRICTION]
> [[2026-1023-new-api-aviso-legal-para-reventa-publica]] recoge la advertencia del README: quien opere el proyecto como **servicio público de IA generativa o servicio de reventa de API** debe cumplir **registro, licencias, seguridad de contenido, verificación de identidad real, retención de logs, impuestos y autorización upstream**, y el propio README declara esas obligaciones como **condición previa**.
> Este átomo presiona esa creencia en un punto de cumplimiento concreto: el software que implementa ese servicio público **deja el filtrado de palabras sensibles apagado por defecto** y **borra** la lista de quien la tenía escrita sin guardar el interruptor. Es decir, **la postura por defecto del stack es la de "no moderar"**, mientras que la documentación dice que la moderación de contenido es una obligación regulatoria del operador.
> Ambas no pueden ser completamente correctas en su lectura general: o el default apagado es correcto porque la obligación de seguridad de contenido del README se refiere a **identificación, licencias y registro** (y la moderación de vocabulario no es un estándar regulatorio), o la documentación presenta la seguridad de contenido como condición y el default del producto **desprecia esa condición**, con lo que el README estaría describiendo un estándar que el propio software no ayuda a cumplir. Marcado para juicio humano, no auto-resuelto: el release note **no explica el motivo** del cambio de default (¿coste de CPU? falsos positivos? retirada de la funcionalidad?) y el README no define qué "content safety" exige en la práctica.

