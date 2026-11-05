---
id: 2026-1101-auth0-b2c-essentials-escala-por-mau
type: atom
certainty: solid
sources: [sources/2026-11-01-auth0-pricing.md, sources/2026-11-03-auth0-pricing.md, sources/2026-11-04-auth0-pricing.md]
links: ["[[2026-1101-auth0-precios-por-mau-no-por-evento]]", "[[2026-1101-auth0-b2b-essentials-escala-por-mau]]", "[[2026-1022-precio-99-mensual]]", "[[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]", "[[2026-1103-auth0-log-streaming-a-siem-incluido-en-essentials]]", "[[2026-1103-auth0-entornos-produccion-y-desarrollo-separados-en-essentials]]"]
---

## Claim
Auth0 Essentials B2C cuesta **$35/mes hasta 500 MAU** y escala por escalones de MAU: $70 (1.000), $175 (2.500), $350 (5.000), $525 (7.500), $700 (10.000), $1.400 (20.000), $2.100 (30.000), $2.800 (40.000) y $3.500 (50.000 MAU). En yearly son 11× el mensual ($385/año en 500 MAU). Professional B2C parte de $240/mes en 500 MAU, sube a $545 en 2.500 y $1.000 en 5.000, y desde 30.000 MAU pasa a "Contact us".

## Why It Matters
El coste unitario por MAU en B2C **decrece** con la escala: $35/500 = **$0,07 por MAU/mes** en el escalón de entrada, y $3.500/50.000 = **$0,07** en el más alto — prácticamente plano, sin descuento por volumen. Eso significa que en Auth0 B2C **no hay economía de escala por tamaño**: el coste de identidad crece linealmente con los usuarios. Para un producto con precio base de 99/mes ([[2026-1022-precio-99-mensual]]) y un presupuesto de infraestructura total de ≤ 4 EUR/mes, esto importa: cualquier MAU de cliente que se autentique en el mes es ya un coste recurrente que el founder paga de su bolsillo, y a partir de 500 MAU el primer escalón de pago ($35/mes) **supera por sí solo todo el presupuesto de infra del vault**, antes de contar el VPS. Es el dato que obliga a comparar Auth0 con la alternativa de coste cero (plan Free hasta 25.000 MAU) antes de asumir cualquier plan de pago.

## Nota de verificación
Cifras leídas literalmente de las tablas "B2C Base Price by MAUs (monthly)" y "(yearly)". El ratio de $0,07 por MAU es una división de este átomo sobre las cifras de la fuente.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-auth0-pricing.md` (render reducido de 540 palabras de auth0.com/pricing).

El render del 2026-11-03 vuelve a imprimir **Essentials $35/mes** y **Professional $240/mes**, ambos con "Up to 500 monthly active users" — los mismos dos precios de entrada que este átomo fija para B2C. Confirma el Claim en sus dos cifras de referencia.

Advertencia añadida: en esta captura esos importes aparecen **bajo el encabezado "B2B BILLING"**, no bajo B2C, lo que deja abierta la posibilidad de que el extractor no esté separando las columnas (ver [[2026-1103-auth0-precios-35-y-240-bajo-el-encabezado-b2b-billing]]). Esta captura además enumera el contenido de la tarjeta Essentials, que este átomo no recogía: Higher Auth/API/Feature limits, Pro MFA, RBAC per Organization, 10 Organizations, streaming de Audit Logs a Datadog/Splunk/AWS/Azure, Separate Production & Development Environments y Standard Support (ver [[2026-1103-auth0-log-streaming-a-siem-incluido-en-essentials]] y [[2026-1103-auth0-entornos-produccion-y-desarrollo-separados-en-essentials]]).

## Actualización 2026-11-04
Fuente: `sources/2026-11-04-auth0-pricing.md` (render completo restaurado de auth0.com/pricing, byte a byte idéntico al del 2026-11-01 — ver [[2026-1104-auth0-render-completo-restaurado-tras-el-reducido-del-11-03]]).

Dos precisiones sobre el **techo de la tabla B2C** que este átomo no recogía:

- El escalón de **30.000 MAU** en Professional B2C es "**Contact us**", pero los escalones de **40.000 y 50.000 MAU** en la misma columna figuran como "**Not available**" — no "Contact us". La distinción importa: "Not available" significa que el plan no existe para ese tamaño, mientras que "Contact us" significa que existe y hay que cotizarlo. En cambio, **Essentials B2C sí tiene precio publicado hasta 50.000 MAU** ($2.800 y $3.500/mes), o sea que el plan se degrada en Professional pero se mantiene en Essentials.
- La tabla **B2B** no publica ningún precio por encima de 20.000 MAU: su última fila es "**30,000+ | Contact us | Contact us**". El techo de escalones con precio publicado es por tanto **50.000 MAU en B2C** y **30.000 MAU en B2B**, frente al "user 1 to 1,000,000+" del encabezado comercial (ver [[2026-1103-auth0-header-precios-flexibles-hasta-millon-de-usuarios]]).
- Re-verificación aritmética: la tabla yearly B2C es exactamente **11× la mensual en los 10 escalones** (500 → $385; 20.000 → $15.400; 50.000 → $38.500), sin excepciones.
