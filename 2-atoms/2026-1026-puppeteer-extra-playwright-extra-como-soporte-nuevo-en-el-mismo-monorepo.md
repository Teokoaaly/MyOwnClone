---
id: 2026-1026-puppeteer-extra-playwright-extra-como-soporte-nuevo-en-el-mismo-monorepo
type: atom
certainty: solid
sources: [sources/2026-10-25-puppeteer-extra-repo.md]
links: ["[[2026-1026-capsolver-mcp-y-agentes-como-primera-superficie-comercial]]", "[[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]"]
---

## Claim
El README declara: "We've also recently introduced support for Playwright, if you're interested in that head over to [`playwright-extra`](https://github.com/berstend/puppeteer-extra/blob/master/packages/playwright-extra)". Es decir, el mismo monorepo mantiene **dos líneas de framework** —Puppeteer y Playwright— bajo una misma API de plugins, y la segunda está señalada como añadida "recently".

## Why It Matters
Playwright aparece en el corpus del vault en dos papeles distintos y ambos son comerciales: como **superficie de integración de agente** en la home de CapSolver ("01 AGENTS — AI agent automation" con MCP, Browser Use, LangChain, OpenAI SDK y **Playwright**) ([[2026-1026-capsolver-mcp-y-agentes-como-primera-superficie-comercial]]) y como integración incluida en cada plan del proveedor de proxy Decodo ([[2026-1026-decodo-integraciones-de-navegador-y-agentes-como-gratis-con-cada-plan]]). Aquí Playwright es además el **segundo lenguaje de un framework de evasión de código abierto**, con su propio paquete dentro del mismo repositorio: es decir, la superficie comercial de evasión y la superficie de código abierto de evasión **coinciden en el mismo nombre de framework**.
La consecuencia práctica para el vault es una alternativa que no tenía registrada: si la elusión hay que construirla (no comprarla), el punto de partida más barato no es un captcha de $0.001 sino un framework MIT ya publicado con la misma interfaz en ambos navegadores.
Nota de verificación: la captura **no fecha** la incorporación ("recently" es la única marca temporal), no documenta la API de `playwright-extra` y no enumera qué paquetes existen bajo `packages/`.
