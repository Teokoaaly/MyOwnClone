---
id: 2026-1023-ai-security-tools-mcp-como-superficie-de-ataque
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]", "[[2026-1022-ia-y-auth-totalmente-servidor]]"]
---

## Claim
El listado dedica una capa entera al **MCP como superficie de ataque**, con al menos tres familias distinguibles: (a) **escáneres de skills y servidores MCP** (`SkillSpector` de NVIDIA con YARA/AST/taint y chequeos MCP de mínimo privilegio, `mcp-scanner` y `skill-scanner` de Cisco AI Defense, `aguara` en Go sin LLM, `mcp-armor` con detección de rug-pull y tool-poisoning, `Ramparts` en Rust con mapeo al OWASP MCP Top 10, `A2A Security Scanner`); (b) **proxies/gateways que median el tráfico MCP** (`ToolHive`, `Pipelock`, `mcp-context-protector`, `MCP Gateway` de Lasso, `MCP Defender` —desktop app que proxya tool-calls de Cursor, Claude, VS Code y Windsurf— y `MCP Observatory`); y (c) **reglas de detección tipo Sigma** (`agent-threat-rules`, "768 rules across 10 categories", autodenominado "Sigma for agents", con integraciones para Microsoft AGT, Cisco AI Defense, MISP, OWASP, FINOS y SigmaHQ).

## Why It Matters
MCP es, en el listado, la señal de que la industria ha dejado de tratar el prompt como el único objeto manipulable: el objetivo pasa a ser **la definición de la herramienta** que el agente va a invocar. La respuesta de la industria es doble —estática (analizar el manifiesto y la descripción de la herramienta) y dinámica (interceptar la llamada en un proxy)—, y la segunda implica que el proxy pasa a ser un punto de control con permisos de escritura sobre lo que el agente ve y hace.

Para el vault esto es un espejo de una decisión ya registrada: en [[myownclone]] el único canal de escritura son Server Actions (ver [[2026-1022-mutaciones-rsc-sin-api-rest]]), lo que equivale a un contrato de herramienta en miniatura. La lección extrapolable es que un canal de invocación único y bien definido es una superficie de ataque más pequeña que un conjunto heterogéneo de skills y servidores MCP, y que el control aplicable es la política sobre ese canal, no el escaneo del prompt ([[2026-1022-ia-y-auth-totalmente-servidor]]). Y la respuesta de la industria a esa superficie no es solo defensa: hay una subsección entera de runtime (61 entradas, [[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]) dedicada a aislar al agente y a mediar sus llamadas.

Con un matiz que conviene no perder: el "ataque a la definición de la herramienta" es un problema de los agentes que cargan herramientas externas. El producto del vault no carga herramientas de terceros, pero sí procesa documentos de la biblioteca que el usuario controla, que es la misma categoría de "datos no fiables" que las skills de un agente.
