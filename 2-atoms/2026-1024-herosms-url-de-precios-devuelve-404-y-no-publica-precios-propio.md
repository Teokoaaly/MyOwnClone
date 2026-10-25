---
id: 2026-1024-herosms-url-de-precios-devuelve-404-y-no-publica-precios-propio
type: atom
certainty: solid
sources: [sources/2026-10-24-hero-sms-pricing.md]
links: ["[[2026-1023-hero-sms-pagina-de-chatgpt-sin-precio-ni-stock-propio]]", "[[2026-1023-hero-sms-marketing-seo-por-servicio-en-vez-de-catalogo]]", "[[2026-1024-herosms-los-contadores-de-stock-siguen-vivos-dos-dias-despues]]"]
---

## Claim
**HeroSMS no tiene página de precios.** La URL `https://hero-sms.com/pricing` responde renderizando la home con un bloque final de **"404 / Page not found / To the main page"**, es decir, la ruta de precios es un 404 catchall: el selector "1. Choice service" que aparece en la captura es el **selector de la home incrustado en la página de error**, no una tabla de precios. La captura completa son 125 palabras y termina literalmente en el mensaje de error. No hay ni una sola fila de precio por servicio, país u operador: solo los cinco "from" del selector de home, que ya se habían transcrito en [[2026-1023-herosms-precios-escapate-entre-0059-y-08551]].

## Why It Matters
Confirma y precisa el diagnóstico de opacidad del proveedor: el intento más directo de auditar precios —pedir la página `/pricing`— falla estructuralmente, no por ocultación activa sino porque **la ruta no existe**. El precio unitario de un número solo es obtenible entrando al panel con saldo ([[2026-1023-hero-sms-pagina-de-chatgpt-sin-precio-ni-stock-propio]]), de modo que la página pública de HeroSMS no ofrece ningún dato transaccionable que la home no ofrezca ya.
Para el vault esto reinforce la asimetría ya registrada frente a 5sim: comparar coste de aprovisionamiento entre los dos proveedores sobre páginas públicas es incomparable por construcción, porque uno publica un CSV de 175 combinaciones país-operador y el otro no publica ni la tabla de precios de su propia ruta de precios. La única forma de obtener el precio real de HeroSMS es comprar saldo y abrir el panel.

## Nota de verificación
El bloque "404 / Page not found / To the main page" está transcrito literalmente de las últimas líneas de la captura, y la coincidencia de los cinco precios con los de la home del 2026-10-22 está comprobada servicio a servicio. La captura no indica si el 404 es del router SPA o un error de servidor, y no permite saber si existen rutas de precios por servicio más allá de la home.
