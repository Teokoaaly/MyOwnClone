---
id: 2026-1027-github-search-antidetect-browser-api-categories
type: atom
certainty: tentative
sources: [sources/2026-10-27-github-search-antidetect-browser-api.md]
links: ["[[2026-1026-github-search-playwright-stealth-dos-de-ocho-no-son-herramientas-de-evasion.md]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos.md]]"]
---

## Claim

Los repositorios de la búsqueda se organizan en dos categorías funcionales distintas: (1) herramientas de gestión de perfiles y navegadores antidetect con APIs/MCP integrados (`foxprofile`, `vesper-antidetect-browser`, `undetectable-browser-MCP`), y (2) frameworks de automatización y bypass de detección (`invisible_selenium`, `invisible_puppeteer`, `antibrow`, `Undetectable-profile-creation-Selenium`, `undetectable-selenium-connection`). La categoría 1 expone REST API o MCP para control de perfiles, while the categoría 2 se enfoca en bibliotecas/frames para controlar navegadores con stealth.

## Why It Matters

Para el vault, esta separación estructural significa que las perguntas de producto sobre "antidetect browsers" deben distinguir si el caso de uso es gestión de múltiples perfiles (necesita MCP/REST API para crear/importar perfiles) vs. automatización de navegación con evasión (necesita bibliotecas como Selenium/Puppeteer/Playwright con patches de stealth). La búsqueda demuestra que estos dos propósitos convergen raramente en un mismo repositorio, lo que sugiere que los flujos de trabajo típicos combinan ambos tipos: un gestor de perfiles más un framework de automatización.

## Nota de verificación

Lectura de campos `description` y `topics` del JSON en `sources/2026-10-27-github-search-antidetect-browser-api.md`. Por ejemplo: `foxprofile` description menciona "per-profile fingerprint, cookies and proxy, Camoufox and Chrome engines, desktop app, REST API and MCP server"; `undetectable-browser-MCP` description dice "Manage profiles, proxies, cookies, fingerprints, import/export, cloud sync"; `invisible_selenium` description dice "Selenium that anti-bots cannot see"; `antibrow` description dice "Kernel-level antidetect browser with the Playwright API". Estas clasificaciones son juicios del vault sobre la descripción publicada, no auditorías de código. `certainty: tentative` por esta razón.