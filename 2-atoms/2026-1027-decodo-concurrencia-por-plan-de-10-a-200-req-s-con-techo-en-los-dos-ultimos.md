---
id: 2026-1027-decodo-concurrencia-por-plan-de-10-a-200-req-s-con-techo-en-los-dos-ultimos
type: atom
certainty: tentative
sources: [sources/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]]", "[[2026-1026-brightdata-limite-de-1000-requests-por-minuto-en-cuenta-sin-fondos]]", "[[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]"]
---

## Claim
La escalera de la Web Data API publica un eje de **concurrencia** que no es el precio: **10 req/s** en los dos primeros planes (el gratuito y el de $19), **25 req/s** a $49, **50 req/s** a $99, **100 req/s** a $249, **150 req/s** a $499 y **200 req/s** en los dos últimos planes (**$999** y **$1499**). Es decir: los dos planes más caros **comparten el mismo techo de 200 req/s** y solo se diferencian en la cuota (1.8M/6.2M frente a 2.9M/9.9M crawls/páginas).

## Why It Matters
El vault ya tiene registrado que **el límite que decide el coste de una operación de scraping no es el volumen, es la concurrencia**: Bright Data corta a **1.000 requests por minuto** en cuenta sin fondos y lo publica como un número duro ([[2026-1026-brightdata-limite-de-1000-requests-por-minuto-en-cuenta-sin-fondos]]), y DataImpulse obliga a medir el coste por **número de sesiones sticky**, no por GB ([[2026-1024-dataimpulse-sesiones-rotating-y-sticky]]). Aquí el proveedor hace lo contrario de lo habitual: **publica el techo de concurrencia como característica comercial de cada plan**, algo que ningún otro del corpus hace en su página de precios.
La lectura operativa que impone la escalera es notable: **pasar de $499 a $1499 multiplica por 3 la cuota y no mueve ni un req/s el techo**. Es decir, el comprador del último plan está pagando **capacidad de volumen con concurrencia ya saturada** — y un pipeline cuyo cuello de botella es el paralelismo (no el total) no gana nada subiendo de plan, sino cambiando de arquitectura. Eso convierte a la API en un producto que **se puede auto-optimizar antes de subir de precio**: bajar el paralelismo de 200 a 50 req/s es gratis si el trabajo total cabe en la cuota.
El matiz honesto: la captura **no publica** el significado de "req/s" (¿peticiones concurrentes en curso, o peticiones por segundo servidas con cola?), ni si el límite es por clave, por cuenta o por IP de origen. De ahí que el átomo sea `tentative`: las cifras son literales, la lectura de "techo" es interpretación.

## Nota de verificación
Cifras de req/s transcritas literalmente, emparejadas con su plan por la posición en la tabla. La captura **no** publica: definición de req/s, si el límite aplica a `/crawl` igual que a `/scrape`, si hay soft limit, ni el número de claves API por cuenta.
