---
id: 2026-1102-brightdata-doce-logos-de-clientes-enterprise-tras-los-50000
type: atom
certainty: solid
sources: [sources/2026-11-02-brightdata-pricing.md, sources/2026-11-01-brightdata-pricing.md]
links: ["[[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]", "[[2026-1026-decodo-135k-clientes-y-cinco-años-de-premio-proxyway-como-escala]]", "[[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]]"]
---

## Claim
En la página de precios, bajo el titular **"Trusted by 50,000+ customers worldwide"**, la captura del 2026-11-02 resuelve los logotipos de cliente a doce marcas nombradas: **Club Med, Deloitte, eToro, McDonald's, Moody's, NBC Universal, Nokia, Oxford, Pfizer, Shopee, Taboola y United Nations** (`media.brightdata.com/2025/07/logo_<marca>.svg`). La captura del 2026-11-01 del mismo URL mostraba esos trece huecos (doce de cliente más el propio logo de Bright Data) como **SVG inline vacío** (`viewBox='0 0 190 30'`…`'0 0 98 40'`), sin nombre ni marca; solo la del 11-02 conserva las URLs de origen.

## Why It Matters
Es la primera vez que el vault puede **auditar la escala de clientes del proveedor en vez de citarla**: "50.000+ clientes" era hasta ahora una cadena publicitaria sin un solo nombre detrás ([[2026-1024-brightdata-400m-de-ips-en-195-paises-con-targeting-gratis]]); ahora hay doce nombres concretos detrás. Y son nombres con peso en un sentido concreto: **Nokia, Pfizer, McDonald's, NBC Universal, Moody's, Oxford y United Nations** son organizaciones donde la compra de infraestructura de datos pasa por comité de compras, no por tarjeta de crédito — lo que es coherente con el único modelo de venta con persona asignada del catálogo (la suscripción de Datasets con *dedicated account manager*).
La comparación con el resto del corpus es la parte útil. Decodo publica la cifra más alta del sector (**135.000+ clientes**, [[2026-1026-decodo-135k-clientes-y-cinco-años-de-premio-proxyway-como-escala]]) pero **sin un solo logo de cliente nombrable**; Bright Data publica menos clientes pero **doce identificables**, entre ellos un organismo supranacional. Para el agregador de precios del vault la conclusión práctica es que **el número de clientes no es comparable entre proveedores** —el primero es una cifra de marketing, el segundo una lista de testigos verificables— y que el activo realmente vendible de este proveedor es la **percepción de fiabilidad**, no el recuento. Es la misma lógica que ya dejó registrado el átomo de los distintivos de IPRoyal: un logo no es un SLA ([[2026-1024-iproyal-premios-y-distintivos-como-sustituto-de-sla]]).

## Nota de verificación
El hecho de que la captura del 2026-11-01 perdiera los nombres de cliente (SVG inline vacío) mientras la del 2026-11-02 los conserva es en sí mismo un dato de fiabilidad del pipeline de captura: **dos capturas consecutivas de la misma URL, un día de diferencia, difieren en el número de hechos extraíbles**. La lista de doce marcas solo es recuperable desde la captura del 11-02.
Marcas transcritas de los nombres de archivo (`logo_club_med.svg`, `logo_deloitte.svg`, `logo_etoro.svg`, `logo_mcdonalds.svg`, `logo_moodys.svg`, `logo_nbc_universal.svg`, `logo_nokia.svg`, `logo_oxford.svg`, `logo_pfizer.svg`, `logo_shopee.svg`, `logo_taboola.svg`, `logo_united_nations.svg`). La captura **no** publica: qué producto consume cada cliente, su volumen, su condición de cliente de pago ni su fecha.
