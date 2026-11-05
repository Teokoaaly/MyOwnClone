---
id: 2026-1028-astrlink-tool-connection
type: atom
certainty: solid
sources: [0-raw/2026-10-28-astrlink-home.md]
links: ["[[2026-1028-astrlink-unified-subscriptions]]", "[[2026-1028-astrlink-api-protocols]]"]
---

## Claim

AstrLink centralizes the connection of AI tools such as Codex, Claude, and Grok through a single access token, eliminating the need for individual API keys and scattered subscription management across multiple dashboards.

## Why It Matters

The "03 — Connect your tools" section of the AstrLink home page describes how agents can add subscriptions or APIs in AstrLink and then connect their AI tools. Accounts, keys, and model settings are all managed in one place. An agent no longer needs to manage individual API keys; a single access token per agent connects to the local gateway, which handles credential rotation, provider selection, and usage tracking across all configured models and providers. This reduces operational overhead and prevents credential sprawl.

## [FRICTION]

> [[2026-1028-astrlink-unified-subscriptions]] afirma que una sola gateway local puede gestionar suscripciones de Codex, Claude y Grok junto a proveedores mayores. Este átomo presiona la creencia de que un solo gateway puede sustituir completamente la gestión de suscripciones institucionales: AstrLink's unified interface agrega y normaliza proveedores, pero las cuotas, los modelos disponibles y las licencias siguen dependiendo del proveedor subyacente. Un gateway unificado no elimina las restricciones específicas de cada provedor; solo las centraliza. Ambas afirmaciones pueden ser ciertas en dominios diferentes —gestión interna vs. acceso al proveedor— pero la suposición de que la unificación resuelve todos los problemas de proveedor es una simplificación que requiere juicio humano. No hay contradicción lógica, pero sí fricción en la expectativa de valor. Además, [[2026-1028-astrlink-api-protocols]] documenta la conversión de protocolos entre proveedores, y la creencia de que todos los clientes pueden enrutarse a través de cualquier protocolo convertido ignora que algunos clients tienen requisitos de formato de request y response que el gateway puede no normalizar completamente. Ambas no pueden ser completamente correctas: la conversión de protocolos cubre los casos estándar, pero los clientes con esquemas de request personalizados pueden encontrar límites en la compatibilidad del gateway. Marcado para juicio humano, no auto-resuelto.