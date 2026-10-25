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
