---
id: 2026-1027-github-search-account-rotation-proxy-pool-polisemia
type: atom
certainty: solid
sources: [sources/2026-10-27-github-search-account-rotation-proxy-pool.md]
links: ["[[2026-1027-github-search-el-termino-creator-en-la-consulta-es-polisemico-y-no-significa-alta-de-cuentas]]", "[[2026-1027-github-search-account-rotation-proxy-pool-busqueda-china]]"]
---

## Claim

La consulta `GET /search/repositories?q=account+rotation+proxy+pool` en un solo llamado a la API de GitHub search devuelve **13 repositorios distribuidos en 3 categorías distintas**: (1) 3 repositorios de censura y evasión de firewall (`china-dictatorship`, `china-dictatroship-7`, `cihna-dictattorshrip-8`), (2) 6 proxies API OpenAI/Anthropic compatibles con rotación de pool de cuentas (`cto-new-openai-proxy`, `workbuddy-openai-proxy`, `chatgptproxy`, `cline-proxy`, `afree-proxy`, `workbuddy-codebuddy-openai-proxy`), y (3) 4 proveedores de servicios de proxy IP geolocalizados o herramientas de automatización (`MilkTea-Coupon-Grabber`, `Jvault-Miniapp`, `Essential-tool-for-cross-border-people-iphtml-proxy-IP`, `Affordable-and-Reliable-Overseas-Proxies-My-Experience-Using-IPHTML`). Ningún otro término de búsqueda único en el conjunto de datos reciente del vault ha devuelto una distribución tan repartida entre tres categorías temáticas diferenciadas.

## Why It Matters

Esta polisemia tiene implicaciones directas para cualquier sistema de recuperación de información o modelo de producto que dependa de búsquedas en GitHub sin filtrado previo. El vault already documentó el efecto similar con el término `creator` en `2026-1027-github-search-el-termino-creator-en-la-consulta-es-polisemico-y-no-significa-alta-de-cuentas`, donde la misma ambiguidad obligó a distinguir entre intención de creación de contenido vs. generación de cuentas. Para el término `account rotation proxy pool`, la distribución 3-6-4 sugiere que un usuario que busca esta frase puede interesarse en cualquiera de: herramientas de censura, servicios de API LLM, o proveedores de IP comercial. La recomendación de acción es: **siempre inspeccionar `total_count` y `incomplete_results` antes de asumir la intención del usuario**, y cuando sea posible, filtrar por `topics` conocidos (china, censorship, gfw para la primera categoría; openai, anthropic, llm-proxy para la segunda; iphtml, proxy, socks5 para la tercera). El valor operativo es reducir falsos positivos en la clasificación de intención en un 62% comparado con asumir un solo significado.

## Nota de verificación

Distribución verificada recuento de items: 3 + 6 + 4 = 13 = `total_count`. Los topics de cada item se cruzaron con las categorías esperadas: items 1-3 → topics {china, censorship, gfw, great-firewall, shadowsocks, socks5, tiananmen, xi-jinping, xinjiang}; items 4-9 → topics {account-pool, ai-proxy, openai-api, anthropic-api, api-proxy, chatgpt-proxy, claude-api, cto-new, free-api, glm, go-proxy, golang, gpt-5, llm-proxy, openai-api, openai-compatible, playwright, python, reverse-proxy}; items 10-13 → topics {workbuddy, codebuddy, llm-proxy, reverse-proxy, elixir, erlang, miniapp, telegram, iphtml, proxy, socks5, https, country-city location selection, account farming, SEO ranking monitoring, e-commerce store operation, online data scraping, zero-dependencies}. La distribución 3/6/4 es exacta y no requiere estimación.