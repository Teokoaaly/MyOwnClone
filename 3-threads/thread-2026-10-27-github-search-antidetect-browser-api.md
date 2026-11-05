## 10github-search-antidetect-browser-api Atoms — 2026-10-27

Created 3 atomic notes from capture `2026-10-27-github-search-antidetect-browser-api.md` (sources/2026-10-27-github-search-antidetect-browser-api.md): GitHub search for "antidetect browser api" returning 21 repositories across 3 thematic categories.

### Atoms created:

1. **2026-1027-github-search-antidetect-browser-api-result-structure** — La consulta `GET /search/repositories?q=antidetect+browser+api` devuelve `total_count: 21` y `incomplete_results: false`, lo que significa que el índice de GitHub no truncó los resultados y se exhibieron los 21 repositorios completos en la captura del 2026-10-27. Datos operativos: población indexada completa, sin paginación necesaria.

2. **2026-1027-github-search-antidetect-browser-api-mcp-pattern** — Dos repositorios en la captura (`foxprofile` y `undetectable-browser-MCP`) exponen un servidor MCP (Model Context Protocol) para la gestión de perfiles y navegadores antidetect. El patrón sugiere que el modelo de agente para herramientas antidetest está desplazándose hacia APIs estandarizadas (MCP) en lugar de endpoints propietarios, con al menos 3 repositorios teniendo `"mcp"` en topics (foxprofile, undetectable-browser-MCP, browser-proxies-sx).

3. **2026-1027-github-search-antidetect-browser-api-categories** — Los repositorios de la búsqueda se organizan en dos categorías funcionales distintas: (1) herramientas de gestión de perfiles y navegadores antidetect con APIs/MCP integrados (`foxprofile`, `vesper-antidetect-browser`, `undetectable-browser-MCP`), y (2) frameworks de automatización y bypass de detección (`invisible_selenium`, `invisible_puppeteer`, `antibrow`, `Undetectable-profile-creation-Selenium`, `undetectable-selenium-connection`). La categoría 1 expone REST API o MCP para control de perfiles, mientras que la categoría 2 se enfoca en bibliotecas/frames para controlar navegadores con stealth.

### Cross-atom tensions:

- **Perfil vs. automatización**: La búsqueda revela una división clara entre herramientas de gestión de perfiles (necesitan MCP/REST API) y frameworks de automatización (necesitan bibliotecas Selenium/Puppeteer/Playwright con stealth). Asumir que un solo tipo satisface ambos casos de uso conduce a diseños de integración incompletos. Los flujos de trabajo típicos probablemente combinen ambos tipos: un gestor de perfiles más un framework de automatización.

- **Intención de búsqueda vs. distribución de resultados**: El término `antidetect browser api` devuelve una mezcla de perfiles, frameworks y herramientas MCP. La distribución 21-items across dos categorías funcionales significa que la intención del usuario puede estar en cualquier subconjunto dependiendo del caso de uso específico.

- **Estandarización de protocolo**: La aparición de MCP en múltiples repositorios (foxprofile, undetectable-browser-MCP, browser-proxies-sx) contrasta con la variedad de endpoints propietarios y patches de stealth en el resto del corpus. Esto sugiere un posible camino de convergencia hacia APIs estandarizadas para la gestión de antidetect browsers.

### Follow-up needed:

- Verificar la distribución de topics a lo largo del tiempo para el término `antidetect browser api`: si las categorías de perfil y automatización mantienen sus proporciones o si nuevas subcategorías aparecen.

- Seguir si `incomplete_results: false` se mantiene en capturas posteriores: cambios en `per_page` o en la política de indexación de GitHub afectarían la validez de los análisis sobre los 21 items.

- Monitorear si algún nuevo repositorio con topics relacionados (`antidetect-browser`, `mcp`, `browser-automation`) aparece en búsquedas futuras y cómo se categoriza en relación con los 3 atoms actuales.

- Evaluar whether the [FRICTION] block is needed between any pair of these 3 atoms when cross-referencing with existing atoms on browser automation, proxy pools, or MCP integration. especialmente entre `2026-1027-github-search-antidetect-browser-api-mcp-pattern.md` y atoms existentes sobre MCP workflows.

### Additional notes:

- Fuente única: `sources/2026-10-27-github-search-antidetect-browser-api.md` (captura de la API de búsqueda de repositorios de GitHub con query `antidetect browser api`, 21 items, capture date 2026-10-27).
- Cierto `certainty` varía: `result-structure` (solid, datos literales del JSON MCP `tentative`, `categories` `tentative` por juicios de clasificación del vault sobre descripciones de repositorios.