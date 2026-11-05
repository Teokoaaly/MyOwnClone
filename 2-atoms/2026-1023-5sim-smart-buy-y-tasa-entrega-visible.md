---
id: 2026-1023-5sim-smart-buy-y-tasa-entrega-visible
type: atom
certainty: tentative
sources: [sources/2026-10-22-5sim-home.md, sources/2026-10-22-5sim-openai-chatgpt-pricing.md]
links: ["[[2026-1023-5sim-catalogo-servicios-precios-y-stock]]", "[[2026-1023-5sim-reembolso-instantaneo-si-no-llega-sms]]", "[[2026-1022-dashboard-de-insights]]", "[[2026-1023-5sim-openai-tasa-entrega-65-de-100]]", "[[2026-1023-5sim-openai-tasa-entrega-techo-56]]"]
---

## Claim
5sim presenta tres funcionalidades de reducir la tasa de fallo, todas declaradas en su home: **Smart Buy**, que "automatically picks the number with the highest SMS delivery success rate, based on live statistics for every country and operator"; **estadísticas de éxito transparentes**, "live SMS delivery statistics for every country and operator, so you buy numbers that actually work"; y la página de precios con su CSV de stock y tasa por fila (ver [[2026-1023-5sim-catalogo-servicios-precios-y-stock]]). La home afirma además que **no hace falta registrarse para navegar**: se puede consultar cada país, servicio, precio y tasa de éxito antes de crear cuenta.

## Why It Matters
El producto compite por **tasa de entrega**, no por precio: si el número no recibe el SMS, el coste real es el reintento. Exponer la tasa de entrega por país y operador antes del pago es un movimiento de transparencia que convierte una métrica de proveedor en un dato de mercado — el mismo tipo de lectura operativa que el desglose de costes por proveedor en [[2026-1022-costes-por-categoria-tenant]], y que en el panel de plataforma se expone como desglose "chat vs. ops" ([[2026-1022-dashboard-de-insights]]).
El "browse sin registro" es además el patrón opuesto al funnel de [[myownclone]], donde el alta exige cuenta ([[2026-1022-live-verify-alta-y-precios-ya-publicos]]).

## Extensión (página de producto OpenAI, 2026-10-22)
La guía del servicio OpenAI describe Smart Buy con un matiz que la home no da: no solo elige automáticamente "the country and operator with the best SMS delivery rate", sino que **admite fijar un precio máximo** ("You can also set a maximum price to stay within your budget") y, si hay empate de precio, la propia guía recomienda quedarse con la tasa más alta ("When the prices are close, the higher-rate option is usually the stronger choice"). Es decir, el automatismo de 5sim es en realidad una **regla de desempate sobre precio y tasa**, no un óptimo de tasa absoluto. Y la guía define la métrica que el automatismo consume: la tasa es la frecuencia histórica de SMS recibidos sobre pedidos recientes para ese par exacto ([[2026-1023-5sim-openai-tasa-entrega-65-de-100]]), cuyo techo para OpenAI es del 56% ([[2026-1023-5sim-openai-tasa-entrega-techo-56]]).


## Nota de extensión 2026-10-26
A partir de `sources/2026-10-25-onlinesim-virtual-sms.md`. Este átomo describe el "Smart Buy" de 5sim (elegir automáticamente el par país-operador con mejor tasa de entrega, con opción de fijar precio máximo) y lo describe como "una **regla de desempate** sobre precio y tasa, no un óptimo de tasa absoluto".

OnlineSim es el extremo opuesto del corpus en materia de auditabilidad de la entrega: **no publica ninguna tasa de entrega**, ni tabla por par (país, operador), ni contador de stock, ni CSV. Su bloque de tarifas solo dice "To see exact prices, **please select your country**" y los CTA apuntan a `onlinesim.io/auth/register?redirect=/v2/numbers/` y `/v2/rent/` ([[2026-1026-onlinesim-precios-ocultos-tras-seleccionar-pais-y-cta-de-registro]]).

Lo que sí publica OnlineSim como prueba de vida es un carrusel de SMS de ejemplo que **repite códigos entre marcas** (AliExpress y Taobao comparten "561318"; Instagram y Facebook comparten "645 829"), con un texto de OkCupid bajo la etiqueta Tinder y el bloque entero repetido ([[2026-1026-onlinesim-codigos-de-ejemplo-duplicados-entre-marcas]]). Es una demostración de marketing, no tráfico real ni evidencia de cobertura.

La consecuencia metodológica: en la jerarquía de evidencia del corpus, **OnlineSim es el proveedor con menos dato verificable de los tres, no el más grande**. Su único dato duro es el pie de 107 países enumerados y el módulo gratuito de 132 páginas, ambos contables.
