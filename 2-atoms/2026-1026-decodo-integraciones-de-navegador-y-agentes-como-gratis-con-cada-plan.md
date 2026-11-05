---
id: 2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan
type: atom
certainty: solid
sources: [sources/2026-10-25-decodo-residential-pricing.md]
links: ["[[2026-1024-dataimpulse-gateway-unico-y-protocolos]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1026-decodo-targeting-a-nivel-de-asn-y-zip-incluido-gratis]]"]
---

## Claim
Cada suscripción de proxies residenciales incluye **add-ons gratuitos**, enumerados: **"Chrome Proxy Extension"** y **"Firefox Add-on"** ("Unlock extra tools, like Chrome Proxy Extension and Firefox Add-on with every residential proxies subscription"). La página de integraciones lista **Chrome, Safari, Firefox, Edge**, las extensiones **Decodo Chrome Extension**, **Decodo Firefox Extension**, **FoxyProxy**, **SwitchyOmega**, los navegadores con huella **Insomniac** y **Ghost Browser**, y las apps móviles **iPhone** y **Android**.

## Why It Matters
Es el mismo movimiento de producto que el vault ya registró en 2Captcha: **el proveedor de insumo añade una capa de automatización propia** —allí fueron Browser API, Scraper API, Web Unlocker y cuatro servidores MCP para agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]); aquí son **extensiones de navegador y perfiles con huella**. La diferencia es que Decodo **incluye la capa gratis en cualquier suscripción**, incluso en la de $11.25/mes, mientras que 2Captcha la vende como producto aparte.
Para el vault esto importa en un punto concreto: **Insomniac y Ghost Browser son navegadores con huella**, y la huella es exactamente la partida que el bot de registro masivo del corpus **construye a mano** con TLS fingerprinting de perfiles Chrome aleatorizados y cabeceras de traza con formato Datadog ([[2026-1024-chatgpt-creator-tls-fingerprinting-con-perfiles-chrome-aleatorios]]) — una ingeniería que en el corpus aparece como la capa dominante de un flujo de alta, no como una compra. Aquí esa misma capa **está catalogada como add-on gratuito** de un proveedor de $2–$3.75/GB. Es la primera vez que el vault ve la imitación de huella **como commodity de catálogo** y no como construcción interna.
El matiz técnico: la integración se resuelve **por el lado del navegador o del cliente**, no por el gateway. DataImpulse resuelve todo por un único endpoint `gw.dataimpulse.com:823` con credenciales embebidas y siete lenguajes ([[2026-1024-dataimpulse-gateway-unico-y-protocolos]]); Decodo publica **HTTP(S) y SOCKS5** pero su superficie visible es de **extensiones y perfiles**, no de endpoint único documentado en la captura.

## Nota de verificación
Listas transcritas literalmente. La captura **no** publica: la URL o el nombre del endpoint de conexión, si las extensiones requieren cuenta o clave, ni si Insomniac y Ghost Browser requieren pago aparte.
