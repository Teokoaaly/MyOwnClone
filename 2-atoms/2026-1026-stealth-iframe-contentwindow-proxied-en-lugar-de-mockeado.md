---
id: 2026-1026-stealth-iframe-contentwindow-proxied-en-lugar-de-mockeado
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-stealth.md]
links: ["[[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]", "[[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]]", "[[2026-1026-stealth-navigator-webdriver-con-proxies-es6-para-pasar-instanceof]]", "[[2026-1026-puppeteer-extra-stealth-y-extract-stealth-evasions-como-paquetes-separados]]"]
---

## Claim
Dos entradas del changelog describen la misma corrección en `iframe.contentWindow`. En `v2.4.0`: "New & improved: `iframe.contentWindow` — Found a way to fix `srcdoc` frame based detection without breaking recaptcha inline popup & other iframes (please report any issues)". En `v2.4.2`/`v2.4.1`: "Improved: `iframe.contentWindow` — We now proxy the original window object and smartly redirect calls that might reveal it's true identity, as opposed to mocking it like peasants :)". Y `v2.4.0` añade además "All evasions now have a specific before and after test to make make this whole topic less voodoo".

## Why It Matters
Es el único punto de la captura donde el README **reconoce una dependencia con otro producto**: la detección por frames `srcdoc` se arregla **sin romper el popup inline de reCAPTCHA**. Es decir: la capa de elusión de navegador y la capa de resolución de captcha **se tocan y se condicionan** —no son dos módulos ortogonales que se instalan en paralelo—.
La segunda mitad del átomo es la que más valor tiene para el método: **"as opposed to mocking it like peasants"** es el autor del propio framework reconociendo que el enfoque anterior —sustituir el objeto por una imitación— era detectable, y que la técnica correcta es **interceptar el objeto real en lugar de fabricarlo**. Es una ingeniería de **proxy transparente**, no de suplantación, y es el mismo fundamento sobre el que trabajan las herramientas que capturan el contexto ([[2026-1026-rebrowser-parchea-el-codigo-fuente-porque-no-hay-configuracion-que-lo-arregle]]).
Y la tercera pieza es la que da la regla de higiene del proyecto: **cada evasión tiene un test "before and after"**. Eso significa que la eficacia de cada pieza es verificable de forma aislada, y por tanto que la lista de evasiones funciona como una **lista de hipótesis comprobables** y no como un manto protector. Es el patrón que el vault ya tenía registrado en el sector ([[2026-1026-stealth-navigator-webdriver-con-proxies-es6-para-pasar-instanceof]]), y es también lo que el otro sector del vault hace con su propio instrumento: **un banco de pruebas público con tabla de antes/después**, solo que allí el detector es un servicio externo y aquí es un directorio versionado en el mismo paquete ([[2026-1026-rebrowser-bot-detector-como-banco-de-pruebas-publico]]).

Nota de verificación: las tres citas son literales del changelog. La captura **no** publica los tests ni su resultado; el "before and after test" es una **declaración del autor** sobre su propio proceso.
