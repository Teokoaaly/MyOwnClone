---
id: 2026-1026-decodo-todos-los-precios-mas-vat-no-incluido
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]", "[[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]", "[[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]"]
---

## Claim
**Los ocho precios de la página están marcados "+ VAT"**, sin excepción: los cinco planes mensuales lo llevan en el bloque de total ("Total: $11.25 **+ VAT** billed monthly", $35, $81.25, $150, $275), el PAYG dice "Total: $4 **+ VAT**" y los dos planes Enterprise ("$625 **+ VAT** billed monthly", "$2.000 **+ VAT** billed monthly"). El único texto sobre el tratamiento fiscal es el FAQ: las órdenes se procesan a través de **Paddle**, que es "Merchant of Record" y "the complete payments, **tax**, and subscriptions solution for SaaS".

## Why It Matters
Convierte la tabla de precios de Decodo en **precios sin impuesto**, que es una forma distinta de la que usa el resto del corpus. Hetzner publica "excl. VAT" de forma explícita y Mullvad publica precio **con IVA incluido** —las dos prácticas son opuestas y el thread ya lo registra ([[2026-1024-mullvad-precio-plano-5-euros-iva-incluido-sin-cambio-desde-2009]]). Para los proveedores de proxy, en cambio, **ninguno publica el tratamiento fiscal**: Bright Data no dice si sus $499/$999/$1.999 incluyen o excluyen impuesto ([[2026-1024-brightdata-escalera-de-volumen-141-a-798-gb]]), e IPRoyal publica cinco "from" sin ninguna nota fiscal ni mínimo ([[2026-1024-iproyal-cinco-lineas-y-cinco-unidades-de-precio]]).
La consecuencia aritmética es concreta: **el precio unitario que el vault puede citar para Decodo es un precio neto**, y cualquier comparación de $/GB entre proveedores está incompleta hasta aplicar un IVA que **ningún proveedor del sector publica**. Con un IVA del 21 %, el $2/GB de 1 TB pasa a **$2,42/GB** y el $3,75/GB de 3 GB a **$4,54/GB** — lo que deja el plan de entrada de Decodo por encima del PAYG de $4/GB de Bright Data. Es decir: **el ranking de entrada puede cambiar según el tratamiento fiscal, y ninguna de las dos páginas comparable lo dice**.
El matiz de fondo: al ser Paddle el Merchant of Record, **quien factura es un tercero**, y eso también implica que el titular de la relación comercial con el fisco es Paddle, no Decodo.

## Nota de verificación
Marca "+ VAT" transcrita literalmente en los ocho precios. La captura **no** publica: el porcentaje de IVA aplicado, el país que determina el tipo, ni el desglose de lo que cubre el Merchant of Record (IVA, IVA reversal, dutías).


## Nota de extensión 2026-10-27
La página de precios de la **Web Data API** (`decodo.com/web-data-api/pricing`) rompe el patrón que este átomo establece para la línea residencial: sus ocho precios —**$0, $19, $49, $99, $249, $499, $999 y $1499**— **no llevan ninguna marca "+ VAT"**, y el bloque de pago de la página muestra **"SSL Secure Payment"**, **"Your information is protected by 256-bit SSL"** y el icono de **PayPal**, sin mención alguna a **Paddle** ni a "Merchant of Record".

Es decir: **la fiscalidad no es una propiedad de la marca, es una propiedad de cada página**. La página de proxies de Decodo (captura del 2026-10-25) marca los ocho precios "+ VAT" y explica en el FAQ que las órdenes pasan por Paddle como Merchant of Record; la página de la API, del mismo proveedor y del mismo mes, **no marca fiscalidad y no menciona Paddle**. Con un IVA del 21 %, el plan de entrada de $19/mes de la API pasa a **$22,99** si el precio es neto, o se queda en $19 si es bruto — y **la captura no permite decidirlo**, porque no hay nota fiscal que lo diga.

Consecuencia para el modelo de coste: **toda comparación entre la línea de proxies y la línea de scraping de Decodo está incompleta por el lado fiscal**, y el vault tiene que leer el "+ VAT" como un atributo de la página, no del proveedor. Ver [[2026-1027-decodo-web-data-api-ocho-planes-mensuales-con-limite-de-crawls-y-paginas]] y [[2026-1026-decodo-paddle-como-merchant-of-record-y-cripto-excepto-isp-y-datacenter]].
