---
id: 2026-1024-veridrop-home-la-disponibilidad-se-mide-por-par-sitio-y-modelo
type: atom
certainty: solid
sources: [sources/2026-10-24-veridrop-home-leaderboard.md]
links: ["[[2026-1024-veridrop-leaderboard-home-paga-la-posicion-pero-no-el-verdict]]", "[[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]", "[[2026-1024-veridrop-home-top10-con-sitios-repetidos-y-no-diez-distintos]]"]
---

## Claim
Las dos únicas columnas de medición de la home —**disponibilidad** y **latencia de respuesta**— están tabuladas **por par (sitio, modelo)**, y ese par no es constante para un mismo sitio. `shushutoken.com` aparece con **100 % en Opus 4.8, 100 % en GPT 5.6 y 100 % en Opus 5, pero 67 % en Fable 5**; `88api.ai` con **96 % en Opus 4.8, 87 % en GPT 5.6 y 96 % en Opus 5**; `mintpop.ai` con **78 %, 80 %, 84 % y 78 %** en los cuatro tableros; `www.hejuapi.com` con **98 %, 89 % y 96 %** en Opus 4.8, GPT 5.6 y Fable 5. La latencia también se mueve con el modelo para el mismo sitio: `routerra.ai` registra **3,3 s en Opus 4.8 y 5,9 s en GPT 5.6**; `88api.ai`, **2,2 s / 4,7 s / 2,5 s**. La columna de latencia además tiene un **tercer valor no numérico**: en las cuatro filas de `shushutoken.com` del tablero Fable 5 aparece **"muestra acumulándose"** en lugar de un tiempo. Los extremos de la tabla son `api.zhaomoxing.com` con **54 %** (el mínimo) y `routerra.ai` con **5,9 s** (la latencia máxima).

## Why It Matters
Es la **medición que la home sí ofrece** y su forma correcta de lectura es la que el vault ha venido corrigiendo en el resto del sector: **la disponibilidad de un relay no es una propiedad del relay, es una propiedad del par relay-modelo**. Un `shushutoken.com` al 100 % en Opus 5 no es un relay al 100 %, y comprarlo para Fable 5 significa comprar un 67 % con muestra insuficiente —el propio sitio lo dice en la celda de latencia ([[2026-1024-veridrop-leaderboard-home-paga-la-posicion-pero-no-el-verdict]]). Esto refuerza lo que el thread ya sabía sobre el otro agregador: **precio y estabilidad son ejes desacoplados**, y aquí se añade un tercero, **el modelo**, que multiplica la granularidad de la tabla sin que ninguna página declare el denominador.
Para el vault la consecuencia es de **modelo de datos, no de ranking**: si alguna vez se construye la lista de proveedores de `OPENAI_API_BASE`, la clave primaria no puede ser el dominio sino el par (dominio, modelo), porque es la única granularidad en la que la cifra es válida. Y hay un segundo apunte: la celda "muestra acumulándose" es un **estado de madurez del dato publicado como texto**, no como número, lo que significa que la home no solo carece de denominador sino que **marca explícitamente cuándo no tiene suficiente muestra** —algo que ni PriceAI ni el directorio de VeriDrop hacen de forma visible.

## Nota de verificación
Cifras transcritas literalmente de las 35 filas. La captura **no** publica: el número de sondeos que sustentan cada porcentaje de disponibilidad, la ventana temporal, ni el criterio que decide cuándo una latencia pasa a mostrarse como "muestra acumulándose" en lugar de un tiempo. Ningún porcentaje de esta tabla es comparable con la columna de disponibilidad de 7 días de PriceAI sin conocer el denominador ([[2026-1023-priceai-transit-precio-y-estabilidad-desacoplados]]).
