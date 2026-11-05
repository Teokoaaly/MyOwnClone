---
id: 2026-1024-brightdata-ancho-de-banda-contado-en-dos-sentidos-con-cabeceras
type: atom
certainty: solid
sources: [sources/2026-10-24-brightdata-proxy-pricing.md]
links: ["[[2026-1024-skhron-trafico-contado-en-dos-sentidos]]", "[[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]", "[[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]"]
---

## Claim
Bright Data define el ancho de banda facturable **como la suma de los datos transmitidos hacia y desde el sitio objetivo**, y lo desglosa en cuatro componentes: *"request headers + request data (POST) + response headers + response data"*. Además: *"traffic used during your trial will be listed on your dashboard but will not be counted towards your bill"*.

## Why It Matters
Es el mismo criterio de doble conteo que ya registró Skhron para el tráfico de red ([[2026-1024-skhron-trafico-contado-en-dos-sentidos]]) y el contrario del de Hetzner, donde los 20 TB son de salida y el excedente se cobra a €1,00/TB ([[2026-1023-hetzner-trafico-20-tb-inclusivos-y-1-euro-por-tb-extra]]). Pero aquí el desglose añade algo que ningún otro átomo del vault tenía: **las cabeceras HTTP se facturan como tráfico**. Es un coste invisible en cualquier estimación hecha "a ojo" del tamaño de una respuesta, y en un flujo de scraping con muchas peticiones pequeñas —el patrón real de un pipeline de altas— las cabeceras son una fracción sustancial del total facturable por petición. La unidad de precio, $4/GB en PAYG ([[2026-1024-brightdata-payg-a-4-por-gb-sin-compromiso]]), se aplica por tanto a un volumen inflado respecto del payload real.
La segunda precisión útil es la del trial: el tráfico de prueba **se ve en el panel pero no se factura**, lo que hace del trial una forma de medir el tamaño real de la respuesta antes de comprar compromiso.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: si el cómputo de cabeceras es exacto o una estimación, ni si hay exenciones (por ejemplo, tráfico de conexión o TLS).


## Nota de extensión 2026-10-26
La documentación de billing del 2026-10-25 ofrece por primera vez una **cifra de tráfico gratuito**, que es la que faltaba para poder medir el tamaño real de una respuesta antes de comprar compromiso: el **Browser API consume 5 créditos por MB**, y la cuota completa de 5.000 créditos equivale a **1.000 MB, "nearly 1 GB"** de tráfico mensual gratis ([[2026-1026-brightdata-un-credito-por-request-y-cinco-por-mb-en-browser-api]]). Eso **cuantifica por fin el "traffic used during your trial will be listed on your dashboard but will not be counted towards your bill"** que este átomo registraba: el free tier es un medidor de volumen con 1 GB de precisíon mensual. La conclusión del átomo —que las cabeceras HTTP se facturan como tráfico y que por tanto el $/GB se aplica a un volumen inflado respecto del payload— **sigue sin confirmarse ni desmentirse**: la captura de billing **no** publica el desglose de componentes del ancho de banda, solo el MB total. Se le añade un dato nuevo de orden práctico: con **5 créditos por MB**, el Browser API es **5 veces más caro por megabyte** que la petición simple del pool, de modo que medir en navegador cloud es la forma más cara de gastar la cuota.
