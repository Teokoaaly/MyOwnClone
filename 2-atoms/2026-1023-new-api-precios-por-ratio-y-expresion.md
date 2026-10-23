---
id: 2026-1023-new-api-precios-por-ratio-y-expresion
type: atom
certainty: solid
sources: [sources/2026-10-22-new-api-github.md]
links: ["[[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]", "[[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]", "[[2026-1023-new-api-routing-por-grupo-prioridad-y-afinidad]]"]
---

## Claim
El README declara en la fila "Usage and costs" de la tabla de capacidades: *"Manage quotas, subscriptions, usage logs, cache accounting, and **expression-based pricing** for different usage tiers"*. El historial de commits visible en la propia página añade el segundo motor de precios: **"Ratio pricing bills 12-hour writes at twice the cache write ratio, the same way Claude 1-hour writes use 6/3.75"** y **"GPT models with a cache write ratio convert to expressions with cc12h"**. Es decir, conviven **un sistema de precios por ratio (倍率) y uno por expresiones**, y las expresiones admiten precios propios para cache write: `cc` (cache corto), `cc1h` (Claude 1 hora) y `cc12h` (OpenAI 12 horas). El mismo historial documenta **precios built-in con expresión pico/valle** (*"Built-in prices: peak/off-peak expressions"*) y precios por número de peticiones (*"$0.75 per 1,000 requests"* para `deepseek-search` y `deepseek-fetch`).

## Why It Matters
Este es el **mecanismo interno que produce el multiplicador que PriceAI tabula**: el vault ya sabía que el multiplicador compuesto es *coeficiente de recarga × multiplicador de modelo* ([[2026-1023-priceai-transit-formula-del-multiplicador-compuesto]]) pero no tenía evidencia del lado del software. Aquí aparece: el precio se define **por modelo (ratio) y por nivel de uso (expresión)**, y el grupo es la palanca de asignación ([[2026-1023-new-api-grupos-como-eje-de-precio-del-relay]]).
El hallazgo colateral relevante para el vault es que **el precio depende del modo de caché**: una escritura de cache de 12 h cuesta 2,5× el precio de entrada en OpenAI y el sistema lo refleja con `cc12h`. Un relay que no differentiate caché está regalando margen o regalando service.
Y aparece una **unidad de cuota no basada en tokens**: `$0.75 per 1,000 requests` para búsqueda/fetch serverside. Es el mismo problema de unidades heterogéneas que el vault ya DOCUMENTÓ en las suscripciones oficiales ([[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]).
