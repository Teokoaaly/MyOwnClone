---
id: 2026-1026-patchright-declara-pasar-catorce-detectores-publicados
type: atom
certainty: tentative
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]]", "[[2026-1024-brightdata-web-unlocker-resuelve-captcha-y-no-requiere-kyc]]"]
---

## Claim
La sección "Stealth" es una lista explícita de **catorce detectores superados**, cada uno con su marca de verificación ✅: **Brotector** (que exige además las CDP-Patches, un repositorio aparte del autor), **Cloudflare**, **Kasada**, **Akamai** (bot manager), **Shape/F5**, **Bet365**, **Datadome**, **Fingerprint.com**, **CreepJS**, **Sannysoft**, **Incolumitas**, **IPHey**, **Browserscan** y **Pixelscan**. La condición es explícita: **"With the right setup, Patchright currently is considered undetectable."**

## Why It Matters
La lista es lo más valioso de la fuente por su **composición**, no por su contenido. Repartida entre detectores de automatización genéricos (Brotector, CreepJS, Sannysoft, Incolumitas, IPHey, Browserscan, Pixelscan), detectores de bot de grandes empresas (Cloudflare, Kasada, Akamai, Datadome, Fingerprint.com), un proveedor de e-commerce con betas (Bet365) y un proveedor de WAF (Shape/F5). Es decir: **cubre la cadena completa, desde el fingerprint de navegador hasta el bot manager comercial**, y eso es una afirmación de cobertura, no de un caso aislado.
Para el vault, el dato relevante es de **modelo de coste**: si una sola herramienta open source declara pasar los catorce, entonces la partida "captcha" —que el thread cotiza con tanto detalle, de $0.5 a $2.99 por mil en los tipos estándar ([[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]])— es en muchos casos **evitable en la capa anterior**: no se resuelve el captcha, se evita que el destino lo plantee. Es la diferencia entre pagar por mil captchas y pagar por el mantenimiento de un parche.

## [FRICTION]
> [[2026-1024-2captcha-precios-por-1000-por-tipo-de-captcha]] y el resto de la tabla de coste del thread tratan la resolución de captchas como una **partida cotizable y barata**: el captcha es "una partida de céntimos por mil" y el cuello de botella caro es el SMS.
> Este átomo presiona ese modelo en un punto que no estaba visto: **hay una capa entera de elusión que no está en la tabla de coste porque no se compra — se mantiene**. Patchright declara pasar Cloudflare, Kasada, Akamai y Datadome sin resolver captcha, lo que significa que el captcha es evitable para una parte de los destinos, mientras que el parche que lo evita tiene un coste que la tabla no puede representar (dependencia de un proyecto de terceros, re-parche en cada release de Playwright, y una ventana de ruptura cuando cambia el codebase upstream).
> Ambas cosas no pueden ser la misma partida a la vez: o el captcha es una partida de coste marginal por unidad, o es un **síntoma** de una señal más profunda —el perfil del cliente— que se puede atacar antes y más barato. Marcado para juicio humano, no auto-resuelto: la lista de catorce detectores es una **declaración del propio autor, sin evidencia adjunta ni fecha**, y la captura no publica ninguna tasa de éxito ni ningún registro de las pruebas.

## Nota de verificación
Los catorce nombres y sus marcas ✅ están transcritos literalmente. La captura **no** contiene capturas de pantalla, logs, fecha de la última ejecución ni el método de la prueba. La frase "currently is considered undetectable" está explícitamente condicionada a *"with the right setup"*, setup que la captura no define. El vault no ha ejecutado ninguna de estas pruebas.


## Nota de extensión 2026-10-26
La captura de `sources/2026-10-25-rebrowser-patches.md` ofrece un **contraste de auditabilidad dentro de la misma familia de proyectos**. Patchright declara pasar catorce detectores nombrados, **sin publicar ni una captura ni una fecha de ejecución**. `rebrowser/patches` publica en cambio **la herramienta con la que se comprueba**: `bot-detector.rebrowser.net`, con el código fuente en `github.com/rebrowser/rebrowser-bot-detector`, y una tabla de comparación **"Before the patches 👎 / After the patches 👍"** con dos capturas de la misma prueba. El README sitúa además el listón: *"It doesn't matter how good your proxies, fingerprints, and behaviour scripts, if you don't have it patched, you're just a big red flag for any major website."* Añadir al *Why It Matters*: **un claim de catorce detectores sin evidencia y un detector público con su código no son la misma clase de prueba**, y el vault no puede ponderarlos igual. Ver [[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]].
