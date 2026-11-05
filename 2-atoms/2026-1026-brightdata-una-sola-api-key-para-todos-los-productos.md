---
id: 2026-1026-brightdata-una-sola-api-key-para-todos-los-productos
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]", "[[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]]"]
---

## Claim
La documentación define la autenticación como **una sola credencial para todo el catálogo**: el titular es **"Scrape any site, buy ready-made datasets. Thousands of pre-built scrapers, one API key."** El bloque "Send your first request" lo confirma: *"Each example scrapes a LinkedIn profile with the Scraper API and works as-is after you replace `YOUR_API_KEY` with a key from your account settings. See authentication for how API keys work across all products."* El transporte es `Authorization: Bearer ***` en `cURL`, `"Authorization": "Bearer YOUR_API_KEY"` en Python y Node.js, con la cabecera `Content-Type: application/json`.

## Why It Matters
Es la misma propiedad que el vault registró en el lado proxy de DataImpulse —**un único gateway y un único par de credenciales para los cuatro tipos de pool**, de modo que cambiar de pool no obliga a tocar el código ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]])— pero aquí es aún más fuerte porque **abarca las dos capas**: la misma clave sirve para el proxy, para el Scraper API, para el Dataset Marketplace y para el MCP. Es decir, **una sola credencial abre el acceso a los datos y a la red**, lo que elimina la costura de configuración entre "cómo me conecto" y "desde dónde me conecto".
La asimetría del vault se mantiene intacta, y por eso la clave hay que leerla con su límite: **una clave no es un acceso**. La misma página de precios que da la clave explica que el pool residencial y el móvil exigen KYC con videollamada ([[2026-1024-brightdata-kyc-para-residencial-y-movil-pero-web-unlocker-no]]), y el free tier de 5.000 créditos se activa sin tarjeta ([[2026-1026-brightdata-free-tier-de-5000-creditos-sin-tarjeta]]). La unificación de la credencial **no unifica los gates**: hay una clave y varios filtros.

## Nota de verificación
Textos transcritos literalmente. La captura **no publica**: si la misma clave da acceso a todas las redes o solo a los productos de datos, cuántos tokens/secretos emite la cuenta, ni si hay rotación de claves.
