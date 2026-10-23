---
id: 2026-1023-priceai-opencode-go-10-usd-y-60-usd-al-mes
type: atom
certainty: solid
sources: [sources/2026-10-22-priceai-official-api.md]
links: ["[[2026-1023-priceai-alibaba-coding-plan-50-usd]]", "[[2026-1023-priceai-codificacion-por-requests-vs-prompts-vs-creditos]]", "[[2026-1023-priceai-suscripcion-no-es-api-token]]", "[[2026-1022-pgvector-embeddings-openai-inferidos]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---

## Claim
**OpenCode Go** es un Coding Plan de **$10/mes** con ventanas de cuota **valoradas en dólares**: **$12/5h · $30/week · $60/month**. Cubre **12 modelos**, entre ellos **DeepSeek V4 Flash, DeepSeek V4 Pro, Qwen3.7 Plus, Qwen3.7 Max, Qwen3.6 Plus, Kimi K2.6**. Es el plan más barato de toda la tabla y a la vez el de mayor cobertura de modelos.

## Why It Matters
Con $10/mes y 12 modelos —incluidos los dos flagship de DeepSeek V4—, OpenCode Go es el punto de referencia de "codo barato" para cualquier producto del vault que necesite inferencia de codificación sin pagar consumo por token ([[2026-1023-priceai-alibaba-coding-plan-50-usd]] ofrece lo mismo con 5 modelos a $50; el plan de Tencent con 3 modelos a 40 元).
La estructura de cuota es idéntica a la de ChatGPT y Claude: valor en dólares por ventana 5h/semana/mes, no tokens ni requests ([[2026-1023-priceai-chatgpt-plus-y-pro-precios-y-ventanas]]). Es un cuarto ejemplo de que la industria converge en **cuota valorada en dinero de uso**, lo que la hace no comparable con un presupuesto de API por token ([[2026-1023-priceai-suscripcion-no-es-api-token]]).

## [FRICTION]
> [[2026-1022-pgvector-embeddings-openai-inferidos]] afirma que el stack de [[myownclone]] usa **Anthropic Claude + OpenAI** como LLM, con Neon + PGvector y `text-embedding-3` de OpenAI, y que el coste por proveedor (Anthropic + OpenAI) del panel de [[2026-1022-costes-por-categoria-tenant]] se explica por ese consumo.
> Este átomo presiona esa creencia: por **$10 al mes** una suscripción da acceso a 12 modelos, incluidos **DeepSeek V4 Flash y DeepSeek V4 Pro** — modelos de frontera chinos que la tabla de PriceAI no lista en ningún plan de OpenAI, Anthropic o Gemini. Si la inferencia del vault se realiza vía Dify ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]), que abstrae el proveedor, la elección de "Anthropic + OpenAI" ya no es una consecuencia de la arquitectura sino una preferencia de precio mal cuantificada.
> Ambas no pueden ser completamente correctas: o la inferencia del vault es realmente sensible a modelos de frontera occidentales y no es sustituible por DeepSeek/Qwen/Kimi, o la atribución "Anthropic + OpenAI" de las fuentes previas refleja el proveedor *inferido* de un bundle (el propio átomo lo marca como *inferido*) y no una decisión de arquitectura. Marcado para juicio humano, no auto-resuelto.
