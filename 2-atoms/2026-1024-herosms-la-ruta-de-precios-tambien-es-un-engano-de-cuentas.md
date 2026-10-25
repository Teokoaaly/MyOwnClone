---
id: 2026-1024-herosms-la-ruta-de-precios-tambien-es-un-engano-de-cuentas
type: atom
certainty: tentative
sources: [sources/2026-10-24-hero-sms-pricing.md]
links: ["[[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]", "[[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]", "[[2026-1023-hero-sms-pagina-de-chatgpt-sin-precio-ni-stock-propio]]"]
---

## Claim
La ruta `/pricing` de HeroSMS, además de terminar en 404, renderiza en su parte alta un cromo de **cuentapersonal**: pestañas `Numbers`, `Emails` y `Favorites`, con los avisos "To see your favorites, log into your account" y "To see your latest activations, log into your account", ambos con su boton `Log in`. Es decir, la página coloca, delante de un selector de precios que se presenta como público, **dos bloques que exigen cuenta** (favoritos e historial de activaciones). La captura no aclara si el selector se mostraría sin sesión iniciada; solo deja constancia de que el "Log in" está presente en la misma pantalla que los precios.

## Why It Matters
Es la misma frontera que ya delimita el modelo de HeroSMS: el precio se presenta como dato público de escaparate, pero el estado de uso —qué activó el usuario, qué favoritó— es datos de cuenta ([[2026-1023-hero-sms-modelo-pay-per-use-y-tabla-real-vs-virtual]]). Y el hecho de que la página que promete ser la de precios sea en realidad un 404 con cromo de panel hace sospechar que **cualquier scraping futuro de precios de HeroSMS terminado en `/pricing` está leyendo la home, no un catálogo** — que es el error que la captura documenta ([[2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio]]).
La existencia de la pestaña `Emails` junto a `Numbers` es, además, la única pista de que HeroSMS vende también **email** y no solo SMS; la captura no muestra ningún producto de email ni su precio, así que queda como indicio, no como dato.

## Nota de verificación
Los tres avisos y los dos "Log in" están transcritos literalmente de las líneas 8-22 de la captura. `certainty: tentative` porque la captura no permite distinguir qué bloques son visibles sin sesión y cuáles son placeholders de servidor, y la pestaña `Emails` no va acompañada de ningún producto observable en el material.
