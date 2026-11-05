---
id: 2026-1026-brightdata-llms-txt-como-indice-de-documentacion-para-agentes
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-docs-intro.md]
links: ["[[2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente]]", "[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1024-dataimpulse-uso-de-ips-en-agentes-y-visibilidad-en-ia]]"]
---

## Claim
El bloque superior de la documentación ofrece a los agentes un índice propio: **"Fetch the complete documentation index at: `/llms.txt`"** con la instrucción *"Use this file to discover all available pages before exploring further."* La home incluye además un panel **"You're an agent? Start here"** que apunta a `llms.txt`, **skills** y **MCP tools** para lectores de IA, y un botón de **"Copy prompt"** cuyo texto es *"Read https://docs.brightdata.com/llms.txt and get me set up with Bright Data"*.

## Why It Matters
Es la señal más directa de que **el canal de distribución de la documentación es un agente, no un humano**. El vault ya tenía dos casos del mismo patrón: 2Captcha publica repositorio MCP para agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]) y DataImpulse declara explícitamente el uso de sus IPs por "Claude, Claude Code, Codex y Gemini" ([[2026-1024-dataimpulse-uso-de-ips-en-agentes-y-visibilidad-en-ia]]). Lo que aporta esta captura es el **tercer eslabón**: el índice `llms.txt` como formato de descubrimiento, más un **prompt de arranque copiable** que literalmente dice "read this and set me up".
Para el vault esto tiene una consecuencia operativa concreta: **el propio `llms.txt` es una superficie de confianza que el vault debe auditar antes de seguir sus enlaces**. Un índice que un agente consume para decidir qué páginas leer es un canal de inyección de instrucciones con los mismos privilegios que la documentación que señale, y el vault ya tiene el marco para esa lectura: el objetivo manipulable deja de ser el prompt y pasa a ser **la definición de la herramienta** ([[2026-1026-brightdata-mcp-un-solo-comando-por-cliente-de-agente]]).

## Nota de verificación
Textos transcritos literalmente. La captura **no publica**: el contenido de `llms.txt` (solo el enlace), qué "skills" concretos se publican, ni si el índice distingue páginas de producto de páginas de precio.
