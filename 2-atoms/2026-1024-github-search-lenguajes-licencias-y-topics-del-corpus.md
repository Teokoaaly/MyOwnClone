---
id: 2026-1024-github-search-lenguajes-licencias-y-topics-del-corpus
type: atom
certainty: solid
sources: [sources/2026-10-24-github-search-chatgpt-account-creator.md]
links: ["[[2026-1024-github-search-catorce-resultados-y-el-universo-indexado-de-la-consulta]]", "[[2026-1024-github-search-tres-de-catorce-son-falsos-positivos-de-la-consulta]]", "[[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]]"]
---

## Claim
El perfil técnico del corpus de 14 repositorios es **plano y sin higiene**: los lenguajes declarados son JavaScript (5), Python (4), Go (1), TypeScript (1) y **3 sin lenguaje declarado** (`VAggarwal97/AutoReelUpload`, `zbaxstore/chatgpt-account-creator`, `dameyosegoi-glitch/chatgpt-creator-standalone`). **8 repositorios declaran licencia MIT y 6 no declaran ninguna** (`license: null`): `BHPT-VIP/ChatGPTAccountCreator`, `VAggarwal97/AutoReelUpload`, `Nilsber/CookieProfileCreator`, `theheiszt/Gumroad-AI-MCP-Server`, `Khontol54/chatgpt-account-creator` y `pharaohanjay-gif/chatgpt-account-creator`. **11 de los 14 no tienen ningún topic**; solo tres los publican, y con perfiles radicalmente distintos: `AuuCoder/gptGrok2api` con 9 (`ai-gateway`, `chatgpt`, `docker-compose`, `gpt-image`, `grok`, `grok-api`, `oauth`, `openai-api`, `vue3-typescript`), `opeinime/ChatGPT-Account-Creator` con 5 (`account-create`, `automation`, `chatgpt`, `nodejs`, `openai`) y `VAggarwal97/AutoReelUpload` con 9 (los de Instagram). Cuatro repositorios tienen `description: null`. Solo **3 de los 14 publican `homepage`**: `AuuCoder/gptGrok2api` (`https://muyuai.top`), `VAggarwal97/AutoReelUpload` (una URL de imagen de Vecteezy) y `ashleymccourt88-hub/chatgpt-account-creator` (`https://chatgpt-account-creator.vercel.app`).

## Why It Matters
Tres lecturas, y la tercera es la que más importa para el vault.
La primera es de **heterogeneidad de stack**: el mismo problema —registrar cuentas de ChatGPT— está resuelto en Go, Python, JavaScript y TypeScript. Que el vault ya tuviera dos de esos ([[2026-1024-chatgpt-creator-bot-go-de-registro-masivo-de-cuentas-de-chatgpt]] en Go y el gateway en Python/TypeScript) no es casualidad: **no hay un lenguaje canónico de esta categoría**, porque estos repositorios no son un proyecto con historia, son implementaciones independientes que resolvió cada autor por su cuenta.
La segunda es de **higiene legal**: 6 de 14 sin licencia declarada y 11 sin topics significan que la categoría es, en términos de metadatos, **invisible para cualquier búsqueda por tema** y legalmente ambigua para quien quiera reutilizarla. El contraste con el corpus del vault sobre herramientas de seguridad, donde el índice es CC0 y cada entrada conserva su licencia, es directo.
La tercera es la comercial: **solo tres repositorios del corpus tienen un sitio web, y el único con un homepage de negocio real es `gptGrok2api` (`muyuai.top`)**, el segundo por estrellas y el primero por forks. Es la señal de que **esta categoría tiene un escalón comercial encima del código abierto**, igual que lo tenía Midjourney-Proxy con su edición plus.

## Nota de verificación
Recuentos de `language`, `license.spdx_id`, `topics`, `description` y `homepage` sobre los 14 `items` del JSON capturado el 2026-10-24. Los `topics` de `gptGrok2api` y `opeinime` se transcriben literalmente de la respuesta; el listado de `VAggarwal97/AutoReelUpload` incluye `selenuim`, con la ortografía del propio repositorio.
