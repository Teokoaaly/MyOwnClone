---
id: 2026-1027-github-search-antidetect-browser-api-mcp-pattern
type: atom
certainty: tentative
sources: [sources/2026-10-27-github-search-antidetect-browser-api.md]
links: ["[[2026-1026-github-search-playwright-stealth-dos-de-ocho-no-son-herramientas-de-evasion.md]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos.md]]"]
---

## Claim

Dos de los repositorios en la captura (`foxprofile` y `undetectable-browser-MCP`) exponen un servidor MCP (Model Context Protocol) para la gestión de perfiles y navegadores antidetect: `foxprofile` lo hace como parte de su arquitectura FastAPI+MCP para agentes de IA, y `undetectable-browser-MCP` está dedicado exclusivamente al protocolo MCP con operaciones batch via Promise.all para gestión de perfiles, proxies, cookies y fingerprints.

## Why It Matters

La aparición de MCP como patrón de integración en múltiples repositorios sugiere que el modelo de agente para herramientas antidetect está desplazándose hacia APIs estandarizadas (MCP) en lugar de endpoints propietarios. Esto tiene implicaciones para el vault: los skills de Hermes diseñados para agentes MCP-first pueden reutilizarse en este ecosistema sin adaptadores personalizados, y la categoría "mcp" aparece como topic en al menos 3 repositorios de la búsqueda (foxprofile, undetectable-browser-MCP, browser-proxies-sx), lo que indica adopción creciente.

## Nota de verificación

Datos literales del JSON: `foxprofile` tiene `topics` que incluyen `"mcp"` y `fastapi`; `undetectable-browser-MCP` tiene `topics` que incluyen `"mcp"`, `"stdio"` y `"mode-context-protocol"`. `browser-proxies-sx` también tiene `"mcp"` en topics. La descripción de `undetectable-browser-MCP` menciona explícitamente "Concurrent batch ops via Promise.all". Ciertas de estas lecturas son datos de campo del JSON fuente.