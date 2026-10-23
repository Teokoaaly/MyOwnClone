---
id: 2026-1023-lzt-venta-individual-y-masiva-por-categoria
type: atom
certainty: solid
sources: [sources/2026-10-22-lzt-market-home.md]
links: ["[[2026-1023-lzt-categorias-gaming-y-social-network]]", "[[2026-1023-lzt-categoria-llm-accounts-para-reventa]]", "[[2026-1023-herosms-api-y-partners-de-registro-masivo]]"]
---

## Claim
El lado **vendedor** de lzt.market tiene dos superficies distintas y no equivalentes: (a) alta de una cuenta individual con `/{categoria}/item/add` — **23 categorías** —, y (b) carga masiva con `/mass-upload/{categoria}/start` — **19 categorías**. Cuatro categorías solo tienen vía individual y no masiva: **Epic Games, Valorant and League Of Legends, Social Club y Battle.net**. Las 23 categorías con vía individual incluyen, además de las de juego y redes, **LLM Accounts, VPN, Hytale y OnlyFans**; las 19 con vía masiva incluyen las mismas cuatro (LLM Accounts, VPN, Hytale, OnlyFans).

## Why It Matters
La existencia de una API de carga masiva por categoría (`/mass-upload/{categoria}/start`) es la señal de que el mercado no solo revende cuentas sueltas: tiene **oferta industrializada por lotes**. Eso conecta directamente con lo que dice el sector de números: HeroSMS ofrece "**Register thousands of accounts daily with our partners**" y lista revendedores cuyo producto es el registro masivo ([[2026-1023-herosms-api-y-partners-de-registro-masivo]]); lzt.market es el destino de exchange donde ese output se vende por lotes. La cadena completa queda así: proveedor de números → registro masivo → mercado de cuentas.
La asimetría de 23 frente a 19 también dice algo operativo: cuatro categorías están deliberadamente fuera del canal masivo, probablemente por el riesgo de bloqueo o el volumen de soporte. Es un dato de control de calidad del propio mercado, y no una omisión del HTML.
Para el vault, la lectura de flujo es: si el producto propio ([[2026-1022-instancia-como-captador-de-leads]]) quisiera identidades verificadas en volumen, el mecanismo sectorial existente no es comprar un número ([[2026-1023-5sim-sms-verificacion-como-coste-marginal-de-alta]]) sino el de este mercado, que ya tiene lote built-in ([[2026-1023-lzt-categorias-gaming-y-social-network]]).

## Nota de verificación
Las dos listas de enlaces y sus rutas están transcritas literalmente. La captura **no** publica: formatos de archivo aceptados, máximo de cuentas por carga, comisión por venta, ni tiempos de verificación de las cuentas.
