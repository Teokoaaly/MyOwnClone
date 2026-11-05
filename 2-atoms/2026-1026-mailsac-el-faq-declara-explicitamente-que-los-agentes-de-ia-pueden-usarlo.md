---
id: 2026-1026-mailsac-el-faq-declara-explicitamente-que-los-agentes-de-ia-pueden-usarlo
type: atom
certainty: solid
sources: [sources/2026-10-25-mailsac-test-email.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]", "[[2026-1023-5sim-asistente-ia-integrado]]"]
---

## Claim
El FAQ de MailS.ac incluye una pregunta y una respuesta dedicadas a los agentes: "**Can AI agents use Mailsac for email testing?** Yes. An agent that can make HTTP requests can use Mailsac's REST API to list received messages and read their contents. Use a **private address** or **private custom domain** for sensitive test emails. Start with the REST API quickstart". Es la **única mención a agentes en toda la página**, y aparece como caso de uso de primer nivel con su propia entrada de FAQ y su enlace a la documentación (`docs.mailsac.com/en/latest/services/private_addresses/...` y `.../custom_domains/...`).

## Why It Matters
El corpus del vault ya tenía dos proveedores que **giran hacia agentes**: 2Captcha, que publica cuatro servidores MCP y una línea de scraping ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]), y 5sim, que vende un chat de IA que además **compra** ([[2026-1023-5sim-asistente-ia-integrado]]). MailS.ac es un **tercero con un modelo distinto**: no vende un agente ni un MCP, declara **compatibilidad** con cualquier agente que sepa hacer peticiones HTTP y pone el punto de diseño en la **privacidad del buzón** ("use a private address or private custom domain for sensitive test emails").

Eso importa para la lectura del producto propio: un agente que lee correo de prueba es, estructuralmente, un agente que lee credenciales. El proveedor que documenta esto resuelve la tensión de forma explícita y **en dos niveles** (dirección privada en el plan gratuito, dominio privado en los de pago), mientras que el bot de registro masivo que el vault sí tiene documentado **recoge el OTP automáticamente** sin declarar el régimen de privacidad de su buzón ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]).

## [FRICTION]
> [[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]] describe el giro a agentes como una **línea de producto explícita** —Browser API, Scraper API, fingerprints, Web Unlocker y cuatro servidores MCP publicados en `github.com/2captcha/2captcha-mcp`— y lo lee como "infraestructura de acceso a web para agentes de IA" con precio por resultado útil.
> Este átomo presiona esa lectura en un punto: **MailS.ac llega al mismo público de agentes sin ninguna de esas piezas**, y lo resuelve con una frase de FAQ. Es decir, o "girar hacia agentes" es **una línea de producto que exige superficie propia** (MCP, navegador, proxy, scraping), o es **una declaración de compatibilidad** que basta con exponer REST y documentar la privacidad del buzón. Ambas no pueden ser la regla general: un proveedor con una sola FAQ puede plugarse en agentes sin construir nada.
> Marcado para juicio humano, no auto-resuelto: la captura de 2Captcha no publica los precios de su línea de agentes, así que no hay comparación de coste posible entre "comprar superficie para agentes" y "usar REST".

Nota de verificación: la captura **no** publica ninguna cifra de precio de MailS.ac más allá del piso de $18/mes, ni ningún detalle sobre el uso real de agentes por parte de clientes.
