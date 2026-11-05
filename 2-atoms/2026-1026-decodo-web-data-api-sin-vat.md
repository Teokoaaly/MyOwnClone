---
id: 2026-1026-decodo-web-data-api-sin-vat
type: atom
certainty: solid
sources: [0-raw/2026-10-26-decodo-web-data-api-pricing.md]
links: ["[[2026-1026-decodo-titular-de-2-por-gb-y-entrada-real-de-375]]", "[[2026-1026-decodo-escalera-mensual-de-375-a-275-por-gb]]"]
---

## Claim

La página de precios de la **Web Data API** de Decodo publica ocho planes ($0, $19, $49, $99, $249, $499, $999 y $1499) **sin ninguna marca "+ VAT"**. El bloque de pago muestra "SSL Secure Payment", "Your information is protected by 256-bit SSL" y el icono de PayPal, **sin mención alguna a Paddle ni a "Merchant of Record"**. En contraste, la línea residencial del mismo proveedor (captura del 2026-10-25) sí marca "+ VAT" y explica en el FAQ que las órdenes pasan por Paddle como Merchant of Record.

## Why It Matters

Todo comparación entre la línea de proxies y la línea de scraping de Decodo está **incompleta por el lado fiscal**: el vault debe leer el "+ VAT" como un atributo de la página, no del proveedor. El patrón es consistente dentro de cada línea pero **diferente entre líneas** — la página de API no cobra VAT ni usa Paddle, mientras que la página de proxies sí lo hace. Esto afecta cualquier modelo de coste que intente normalizar precios entre las dos líneas de negocio de Decodo.

## [FRICTION]

> [[2026-1024-brightdata-cupon-50-off-y-match-del-primer-deposito]] (escrita hace semanas) afirma que el precio nominal de Bright Data solo se alcanza con cupón `RESIGB50`. Esta nota presiona eso porque la Web Data API de Decodo **no requiere cupón** para publicar su precio nominal: el precio de lista es el precio real. Ambas no pueden ser completamente correctas en el mismo sentido —en uno el precio nominal es condicional, en el otro es incondicional. Marcado para juicio humano, no auto-resuelto.