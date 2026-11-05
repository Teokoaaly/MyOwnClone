---
id: 2026-1026-patchright-command-flags-automation-controlled-y-habilitacion-de-funciones
type: atom
certainty: solid
sources: [sources/2026-10-25-patchright-playwright.md]
links: ["[[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]"]
---

## Claim
La sección "Command Flags Leaks" describe cómo se ajustan los flags por defecto de Playwright: **"Patchright tweaks the Playwright Default Args to avoid detection by Command Flag Leaks."** La lista es literal y va en dos direcciones. **Añadido**: `--disable-blink-features=AutomationControlled` — *"to avoid navigator.webdriver detection"*. **Eliminados**: `--enable-automation` (también *"to avoid navigator.webdriver detection"*), `--disable-popup-blocking` (*"to avoid popup crashing"*), `--disable-component-update` (*"to avoid detection as a Stealth Driver"*), `--disable-default-apps` (*"to enable default apps"*) y `--disable-extensions` (*"to enable extensions"*).

## Why It Matters
El parche es pequeño pero revelador: **cinco de los seis cambios no son para parecer más humano, sino para recuperar capacidades que la automatización por defecto desactiva**. Extensiones, aplicaciones por defecto y popups son functionality de navegador real que Playwright apaga por defecto y que un usuario humano sí tiene. Es el mismo tipo de razonamiento que ya está en el vault sobre captchas —elegir por el tipo de señal del destino— aplicado a la superficie del navegador: **la automatización no se delata solo por lo que hace, también por lo que no puede hacer**.
Y hay un detalle de diseño que importa para quien integrate: la detección de `navigator.webdriver` se ataca por **dos vías redundantes** —añadir `--disable-blink-features=AutomationControlled` y quitar `--enable-automation`. Es una señal de que el autor trata estas cosas como **superficie de detección conocida y enumerable**, no como un problema aislado.
Para el vault, la conclusión es de comparabilidad de capas: este parche vive en la **capa de flags del proceso de navegador**, mientras que el `chatgpt-creator` imita la **capa de transporte HTTP** ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]). Son dos capas distintas y no intercambiables.

## [FRICTION]
> [[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]] afirma que **la capa dominante de un flujo de alta es una construcción, no una compra**, porque la huella del cliente "no está en ningún catálogo", y de ahí la conclusión de que con ≤ €4/mes esa ingeniería no se resuelve comprando.
> Este átomo presiona esa conclusión en un punto: **la ingeniería de elusión de navegador sí está disponible, gratis y en abierto**, con licencia Apache 2.0 y mantenimiento activo — y su coste no es monetario, es de integración y de dependencia de un parche sobre un proyecto tercero. Si esa capa es la dominante, el cuello de botella del modelo de coste del thread no es "no existe catálogo": es que **el catálogo que importa no es de pago**. La fricción real que queda por juzgar es si una capa de elusión **gratis y open source** es sustainable frente a un antibot que también puede actualizarse, y eso la captura no puede resolver: el README no publica fecha de última verificación ni tasa de éxito.
> Marcado para juicio humano, no auto-resuelto.

## Nota de verificación
Los seis flags y sus motivos están transcritos literalmente del README. La captura **no** incluye el diff del parche, ni la versión de Chromium sobre la que se aplican, ni evidencia de que `navigator.webdriver` deje de estar definido. La lectura de "recuperar capacidades de usuario humano" es interpretación del vault sobre las frases "to enable default apps" / "to enable extensions".
