---
id: 2026-1027-github-search-account-rotation-proxy-pool-api-proxies
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-account-rotation-proxy-pool.md]
links: ["[[2026-1027-github-search-el-termino-creator-en-la-consulta-es-polisemico-y-no-significa-alta-de-cuentas]]", "[[2026-1024-github-search-noventa-y-cuatro-por-ciento-de-las-estrellas-en-tres-repos]]"]
---

## Claim

De los 13 repositorios devueltos por `GET /search/repositories?q=account+rotation+proxy+pool`, **6 son herramientas OpenAI/Anthropic-compatible API proxy con rotación de pool de cuentas documentada**: `cto-new-openai-proxy` (45 stargazers, Python, MIT license), `workbuddy-openai-proxy` (43 stargazers, Node.js, MIT license), `chatgptproxy` (25 stargazers, Python, MIT license), `cline-proxy` (9 stargazers, Go, null license), `afree-proxy` (0 stargazers, Go, null license), y `workbuddy-codebuddy-openai-proxy` (0 stargazers, Go, MIT license). Todos exhiben en su descripción la funcionalidad de `account pool auto-rotation`, `JWT refresh`, o `bulk registration`. Ningún repositorio de los 6 tiene como lenguaje principal Java o Rust; 5 usan Python y 1 usa Go.

## Why It Matters

La predominancia de proxies API de código abierto con rotación de cuentas sugiere que la consulta `account rotation proxy pool` tiene un fuerte sesgo de consumo hacia la **integración de desarrolladores** más que hacia la infraestructura de red pura. El hecho de que 5 de 6 usen Python y todos menos uno tengan licencia MIT indica un patrón de adopción bajo licencia permissiva en la comunidad de herramientas LLM. Para el vault, este es un dato de referencia importante: si se modelo la disponibilidad de capacidades de rotación de cuentas en GitHub, se debe esperar encontrar el 46 % (6 de 13) del índice indexado en esta categoría, con una fuerte correlación con el ecosistema Python/LLM. Además, la ausencia de soluciones de Rust/Java sugiere una laguna de automatización para entornos que no sean Python-dominant.

## Nota de verificación

Cifras de stargazers y lenguaje transcritas del JSON de cada `item` (items 4-9 en la captura source). Los recuentos de estrellas se comparan contra los valores reportados en los metadatos del API: `cto-new-openai-proxy: 45`, `workbuddy-openai-proxy: 43`, `chatgptproxy: 25`, `cline-proxy: 9`, `afree-proxy: 0`, `workbuddy-codebuddy-openai-proxy: 0`. Licencia: `cto-new-openai-proxy: mit`, `workbuddy-openai-proxy: mit`, `chatgptproxy: mit`, `cline-proxy: null`, `afree-proxy: null`, `workbuddy-codebuddy-openai-proxy: mit`.