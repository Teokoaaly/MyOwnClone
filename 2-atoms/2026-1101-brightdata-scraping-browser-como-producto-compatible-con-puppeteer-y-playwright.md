---
id: 2026-1101-brightdata-scraping-browser-como-producto-compatible-con-puppeteer-y-playwright
type: atom
certainty: solid
sources: [sources/2026-11-01-brightdata-pricing.md, sources/2026-11-02-brightdata-pricing.md, sources/2026-10-31-brightdata-pricing.md]
links: ["[[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]]", "[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1026-puppeteer-extra-playwright-extra-como-soporte-nuevo-en-el-mismo-monorepo]]"]
---

## Claim
La ficha **"Scraping Browser Pricing"** del catálogo vende el navegador como **sustituto drop-in de las librerías de automatización del cliente**: *"Access our Scraping Browser, compatible with leading web automation tools"*, con los bullets **"Built-In Website Unlocking"**, **"Save Time & Resources"** y **"Puppeteer & Playwright Compatible"**. Su subpágina de precio es `/pricing/scraping-browser`. Es un producto **distinto** del "Browser API" de la documentación y de la red: es la misma categoría que el vault ya registra como navegador remoto ([[2026-1026-brightdata-browser-api-navegadores-remotos-para-automatizar]]), pero soldada como compatibilidad explícita con **Puppeteer y Playwright**, los dos frameworks que el resto del corpus trata como código a mantener.

## Why It Matters
Esta es la pieza que cierra el triángulo del vault sobre la capa de automatización. En el corpus, Puppeteer y Playwright aparecen de tres formas distintas: como **framework a parchear** (`rebrowser/patches` los parchea porque la configuración no basta, [[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]), como **línea de plugins** mantenida por un tercero (puppeteer-extra/playwright-extra, [[2026-1026-puppeteer-extra-playwright-extra-como-soporte-nuevo-en-el-mismo-monorepo]]) y ahora como **API de un proveedor de proxies** cuyo argumento de venta es que no hay que escribir código nuevo: se conecta al browser que ya se usa.
La consecuencia para el producto del vault es de arquitectura, no de precio: si el scraping browser del proveedor es compatible con Puppeteer y Playwright, **el coste de migrar un pipeline propio a esa infraestructura es el del cambio de configuración de conexión, no el de reescribir los extractores**. Y el "Built-In Website Unlocking" añade el desbloqueo de sitio dentro del propio navegador, que es exactamente lo que el vault ahora tiene que comprar por separado (Web Unlocker como API aparte) o construir con parches. La lectura honesta es que **Bright Data está vendiendo la categoría que en el resto del corpus es ingeniería**, no un producto nuevo — por eso el átomo de la capa de servicio ya decía que el punto donde el proveedor mueve el coste de "tráfico" a "proyecto" es precisamente esta zona.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: el precio del Scraping Browser, el número de navegadores concurrentes incluidos, la versión de Puppeteer/Playwright soportada, ni si el navegador remoto es el mismo producto que el "Browser API" de la documentación o una implementación distinta de la misma familia.
