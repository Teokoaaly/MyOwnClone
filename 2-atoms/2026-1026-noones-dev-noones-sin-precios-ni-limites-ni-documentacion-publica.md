---
id: 2026-1026-noones-dev-noones-sin-precios-ni-limites-ni-documentacion-publica
type: atom
certainty: solid
sources: [sources/2026-10-25-noones-developer-api.md]
links: ["[[2026-1026-noones-api-dos-formatos-directo-y-delegado]]", "[[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]", "[[2026-1024-noones-tabla-de-limites-por-nivel]]", "[[2026-1022-sin-pagina-precios-ni-docs]]"]
---

## Claim
La captura completa de `https://dev.noones.com/` son **547 palabras** y **no contiene ni un endpoint, ni un ejemplo de request o response, ni un esquema de autenticación, ni un rate limit, ni un precio, ni un SLA, ni una política de datos**. Es una landing de marketing: cuatro bullets, cuatro bloques de caso de uso con su "Read more", y el selector "Choose Your Format" con dos enlaces a `dev.noones.com/dashboard/direct-access` y `dev.noones.com/dashboard/delegated-access`. La captura **sí** contradice lo que la propia página sugiere: el botón de entrada es `Get Started` → `https://dev.noones.com/#chooseYourFormat`, es decir, un ancla a la **misma página**, no a un panel de documentación.

## Why It Matters
El vault ya tenía anotado que la superficie pública de NoOnes enlaza "API documentation" a `dev.noones.com` ([[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]]), lo que sugería un modelo de integradores serio. **La captura corrige esa lectura**: `dev.noones.com` no es un repositorio de documentación, es el escaparate de los dos formatos de acceso, y la documentación real está detrás de un dashboard autenticado. El resultado práctico es el mismo patrón que el vault ya marcó en varios proveedores del corpus ([[2026-1022-sin-pagina-precios-ni-docs]]): **todo lo auditable de esta API es la foto de su marketing, y todo lo auditable de verdad (límites, precios, scopes) está detrás del login** — justo lo que un integrador necesita para presupuestar ([[2026-1024-noones-tabla-de-limites-por-nivel]]).

## [FRICTION]
> [[2026-1024-noones-superficie-publica-productos-y-dominios-espejo]] afirma que en NoOnes "**API documentada** + partner program" es, frente a HeroSMS ("API sin documentación y socios cuyo producto es el registro automatizado"), "la diferencia con un intermediario opaco" y que apunta "a un modelo de integradores serio y no a un intermediario opaco".
> Este átomo presiona esa creencia en un punto medible: la página que esa etiqueta llama "documentación" son **547 palabras sin un solo endpoint, sin un esquema de autenticación, sin un rate limit, sin un precio y sin un SLA**, y su botón "Get Started" apunta a un ancla de la misma página (`#chooseYourFormat`), no a un panel de referencia.
> Ambas no pueden ser completamente correctas a la vez: o "API documentada" es true en sentido material —documentación técnica accesible sin cuenta— y esta captura la desmiente, o el descriptor se refiere solo a "hay un sitio propio para desarrolladores" y entonces **la diferencia con HeroSMS es de marketing, no de auditabilidad**: los dos esconden lo técnico, y NoOnes además separa el alta en dos dashboards.
> Marcado para juicio humano, no auto-resuelto: la captura es la home pública; la documentación tras login no se ha podido leer y podría existir y ser completa.

