---
id: 2026-1024-notletters-captura-minima-sin-dominios-ni-limites-ni-condiciones
type: atom
certainty: tentative
sources: [sources/2026-10-23-notletters-mail.md]
links: ["[[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]", "[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]"]
---
## Claim
La captura de `notletters.com` es una **home de marketing de 172 palabras** y, leída entera, **no publica** ningún catálogo operativo: no hay formato ni lista de dominios de los buzones, no hay patrón de las direcciones, no hay límite de buzones por cuenta ni por compra, no hay plazo de retención ni de expiración, no hay precios por volumen (solo la afirmación de que "la mayoría de los clientes" recibe descuentos), no hay forma de pago, ni reembolso, ni condiciones, ni SLA. Lo único cuantificado son las cuatro cifras de la sección de estadísticas ([[2026-1024-notletters-precio-005-rubles-por-correo-y-contadores-de-escala]]).

## Why It Matters
Es una ausencia, y por eso va con `certainty: tentative` — lo verificable es que la captura no lo trae, no que el servicio no lo tenga. Pero la ausencia tiene valor de por sí, porque delimita qué se puede afirmar: del proveedor de correo masivo más explícitamente orientado a registros que ha caído en la captura, **el vault solo puede afirmar precio nominal, orden de magnitud y superficies de acceso**. No puede afirmar coste real de un alta, ni rendimiento, ni tasa de rechazo, ni nada que sirva para construir un modelo de costes.
El precedente ya está en el vault: la captura de lzt.market era también un render parcial sin un solo precio, y su consecuencia fue dejar el precio fuera del modelo ([[2026-1023-lzt-captura-parcial-sin-precios-ni-stock]]). La diferencia es que aquí el precio sí aparece (0.05 ₽), y precisamente por eso es peligroso: **una cifra de precio sin catálogo al lado se lee como un precio de mercado**, y no lo es — no se sabe por cuánto correo, con qué dominio ni con qué retención. El mismo取证 que el vault aplicó al catálogo de 5sim (desglose por país y operador, 175 filas auditables, [[2026-1023-5sim-catalogo-servicios-precios-y-stock]]) o a la tabla de 53 filas del 卡网 ([[2026-1023-priceai-channels-correo-y-jianma-a-centimos-como-insumo-de-alta]]) no es posible aquí: no hay nada que auditar.
La consecuencia operativa para el vault: **NotLetters no es una fuente de coste utilizable tal como está**. Es una fuente de *categoría* —la pierna de correo de la cadena de registro masivo— y su valor documental está en el tipo de producto y en las tres superficies de consumo ([[2026-1024-notletters-tres-vias-de-consumo-api-http-imap-y-web]]), no en su aritmética.

## Nota de verificación
La ausencia se ha comprobado sobre el texto completo de la captura (172 palabras, seis encabezados de sección). Ningún dato de este átomo procede de la web del proveedor: las páginas `/email` y `/user` enlazadas no se han visitado.
