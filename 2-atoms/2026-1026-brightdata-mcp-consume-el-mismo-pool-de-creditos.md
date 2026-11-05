---
id: 2026-1026-brightdata-mcp-consume-el-mismo-pool-de-creditos
type: atom
certainty: solid
sources: [sources/2026-10-25-brightdata-free-tier.md]
links: ["[[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]]", "[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1026-brightdata-pool-unico-de-creditos-cinco-productos]]"]
---

## Claim
Las peticiones al **servidor MCP de Bright Data** consumen el mismo pool: *"Bright Data MCP server requests also draw from this pool. The MCP free tier of **5,000 requests per month** is the same shared allowance, because the MCP server runs on the Web Unlocker API."* Es decir, el "free tier de 5.000 requests/mes" del MCP **no es una cuota adicional**, es la misma bolsa de 5.000 créditos, y la equivalencia técnica es que el MCP corre sobre Web Unlocker.

## Why It Matters
Convierte el MCP de **interfaz** en **puerta de entrada al presupuesto**: una llamada de un agente vía MCP consume el mismo crédito que una llamada HTTP directa, porque el MCP es un cliente del Web Unlocker. Es el mismo movimiento de categoría que el vault ya registró en 2Captcha —proveedor de elusión que publica servidores MCP para agentes ([[2026-1024-2captcha-giro-hacia-scraping-y-mcp-para-agentes]])— pero aquí con la dato nuevo del **coste**: el MCP tiene un free tier, y ese free tier **no multiplica la cuota**.
La lectura de riesgo es la que conecta con la superficie de ataque que el vault ya tenía anotada: el MCP como vector ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]) se materializa aquí en un punto muy concreto —**cualquier agente que use el MCP de Bright Data consume un presupuesto compartido, medido y sin techo de ratio**; la única protección es el límite de 1.000 requests/minuto y el saldo de créditos.
Y hay una consecuencia de diseño para el agregador del vault: si el MCP y el Web Unlocker cobran igual por llamada, **el MCP no es una unidad de coste nueva**, sino una forma de gastar la misma. Eso hace que la decisión "llamar por MCP o por HTTP" sea una decisión de ergonomía, no de coste — lo cual es un dato útil porque elimina una variable del modelo.

## Nota de verificación
Texto transcrito literalmente. La captura **no** publica: si las peticiones MCP fallidas consumen crédito, el precio del MCP en PAYG, ni el nombre del repositorio del servidor MCP.
