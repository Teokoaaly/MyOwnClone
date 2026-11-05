---
id: 2026-1027-github-search-account-rotation-proxy-pool-busqueda-china
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-account-rotation-proxy-pool.md]
links: ["[[2026-1027-github-search-el-termino-creator-en-la-consulta-es-polisemico-y-no-significa-alta-de-cuentas]]", "[[2026-1027-github-search-openai-account-creator-api-cuatro-resultados-y-tres-de-ruido]]"]
---

## Claim

La consulta `GET /search/repositories?q=account+rotation+proxy+pool` (captura `sources/2026-10-27-github-search-account-rotation-proxy-pool.md`, 2026-10-27) devuelve `total_count: 13`, `incomplete_results: false` y **13 `items`**, de los cuales los **primeros 3 resultados** (`china-dictatorship`, `china-dictatroship-7`, `cihna-dictattorshrip-8`) son repositorios de propaganda anti-gobierno chino con descripciones centradas en la censura y la evasión del Great Firewall de China. Los siguientes 6 resultados (`cto-new-openai-proxy`, `workbuddy-openai-proxy`, `chatgptproxy`, `cline-proxy`, `afree-proxy`, `workbuddy-codebuddy-openai-proxy`) son proxies API OpenAI/Anthropic compatibles con rotación de pool de cuentas documented. Los últimos 4 resultados (`MilkTea-Coupon-Grabber`, `Jvault-Miniapp`, `Essential-tool-for-cross-border-people-iphtml-proxy-IP`, `Affordable-and-Reliable-Overseas-Proxies-My-Experience-Using-IPHTML`) son herramientas de grabador de cupones, automatizadores de minería y proveedores de proxies IP con énfasis en rotación por país/ciudad.

## Why It Matters

El índice de búsqueda de GitHub para este término no está truncado (`total_count: 13` cabe completamente en `per_page=20`), lo que significa que la población indexada de 13 repositorios es completa para esta consulta. La consecuencia estructural es que el término `account rotation proxy pool` es **polisémico**: mapea a tres categorías distintas —(1) censura y evasión de firewall, (2) proxies API con rotación de cuentas, y (3) proxies residenciales/cómodos para scraping y cuenta farming. Para el vault, esto significa que cualquier modelo de producto o análisis de riesgo que asuma un significado único para esta consulta **fallará**, pues los 13 resultados abarcan desde herramientas de código abierto para investigación hasta servicios comerciales de proxy y herramientas de automatización de marketing. La implicación práctica es que las búsquedas futuras para este término deben filtrar por `topics` o `language` si se quiere un subconjunto coherente.

## Nota de verificación

Cifras transcritas del JSON de la captura: `total_count: 13`, `incomplete_results: false`. Los campos `stargazers_count`, `forks_count`, `language`, `license.spdx_id`, `size` y las tres marcas temporales (`created_at`, `updated_at`, `pushed_at`) se leyeron de cada `item`. La clasificación de los primeros 3 items como repositorios de censura se basa en el campo `description` publicado y los `topics` asociados (china, censorship, gfw, great-firewall, shadowsocks, socks5, tiananmen, xi-jinping, xinjiang). Ningún repositorio fuera de los 3 primeros tiene topics relacionados con China o censura.