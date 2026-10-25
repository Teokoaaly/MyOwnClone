---
id: 2026-1024-internet-bs-buscador-de-dominios-con-premiums-preorder-y-filtros-idn
type: atom
certainty: solid
sources: [sources/2026-10-24-internet-bs-domains.md]
links: ["[[2026-1024-internet-bs-com-a-6-99-y-cinco-servicios-gratis-de-por-vida]]", "[[2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte]]", "[[2026-1024-internet-bs-tracker-de-dominios-externos-y-renovaciones]]"]
---

## Claim
El buscador de dominios de Internet.bs expone una **máquina de estados de disponibilidad** más rica que un simple disponible/no disponible: los estados de la interfaz son **Available, Unknown, Pending, Invalid, Not available, Taken, Reserved, Preorder, Not supported** — este último aplicado a configuraciones concretas. El buscador ofrece filtros de **TLD, "Include Premiums", "Available Only" y "Exact Match"**, y un panel de sugerencias con **"Include Numbers", "Include IDNS", "Include Dashes", "Max Characters / Less characters / 25 / More characters"**. El catálogo que la home muestra incluye **decenas de TLD de segundo nivel por país** (.ac, .com.au, .co.uk, .com.mx, .com.pl, .co.in, .com.br, .eu, .edu.pl, .net.au, .org.uk, .jp, .za, .us) y **TLD punycode** (xn--qxa6a, xn--e1a4c, xn--5tzm5g, xn--6frz82g, xn--c1avg, xn--q9jyb4c, xn--t60b56a, xn--tckwe, xn--unup4y, xn--vhquv, xn--nqv7f, xn--ngbc5azd, xn--czrs0t, xn--fjq720a, xn--i1b6b1a6a, xn--mk1bu44c, xn--80asehdb, xn--80aswg, xn--9dbq2ay).

## Why It Matters
El estado **"Reserved"** y el estado **"Preorder"** son los que importan: un nombre "reservado" o "en preorder" **no está disponible aunque el buscador lo muestre**, y ese es exactamente el punto ciego de un agente de dominio automatizada. El vault ya registró el patrón opuesto en VeriDrop: dominios de TLD barato donde la barrera no es el precio sino que el nombre **ya está tomado por un actor anónimo** ([[2026-1024-veridrop-relays-con-dominios-efimeros-y-riesgo-de-contraparte]]). Aquí está la herramienta de disponibilidad que faltaba: distingue tomado, reservado, en preorder y no soportado, que para una compra automatizada son cuatro respuestas distintas.

El catálogo de TLD de segundo nivel es la otra mitad del dato: la home muestra que el precio de $6.99 es **solo para .com**, y que la oferta real es una matriz de casi mil sufijos con precios distintos —los ccTLD de país suelen ser más caros y sus reglas de elegibilidad también. Y la presencia de punycode en la lista confirma que **IDN está soportado de serie**, coherente con el filtro "Include IDNS" del buscador. La captura **no** publica ningún precio que no sea el del .com de bienvenida, así que el resto de la matriz queda como superficie, no como dato.

## Nota de verificación
Recuento y literales transcritos de la captura: la lista de TLD es la concatenación de la home, sin estructura de precios asociada (los tokens de plantilla `tld`, `price` y `renewalPrice` aparecen sin resolver, es decir la tabla de resultados no llegó a renderizarse en la captura). El precio de $6.99 corresponde únicamente a .com; **ningún otro TLD tiene precio capturado**.
