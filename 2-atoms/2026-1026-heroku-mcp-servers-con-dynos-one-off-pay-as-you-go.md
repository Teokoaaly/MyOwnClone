---
id: 2026-1026-heroku-mcp-servers-con-dynos-one-off-pay-as-you-go
type: atom
certainty: solid
sources: [sources/2026-10-25-heroku-pricing.md]
links: ["[[2026-1026-heroku-inference-claude-opus-4-8-a-5-50-y-27-50-por-millon]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-gap-dify-como-capa-inferencia-prompts]]"]
---

## Claim
El texto introductorio de la sección **"Artificial Intelligence _new_ — Heroku Managed Inference and Agents"** describe un componente de categoría propia: *"developers can use **MCP servers (powered by one-off dynos that follow a pay-as-you-go model)** to extend AI model capabilities, enabling AI-powered automation and tool execution within Heroku's trusted environment"*. La página **no publica ninguna tabla de precios** para los MCP servers; su modelo de coste se describe solo como **one-off dynos** con **pay-as-you-go**, y se presenta la sección entera como la parte **"new"** del catálogo.

## Why It Matters
Es la **unica parte del catálogo de Heroku que se presenta explícitamente como novedad** ("_new_"), y su modelo de cobro es un tercero que el vault no tenía: **ni suscripción mensual, ni precio por 1M tokens, ni precio por 1000 consultas, sino dynos de un solo uso facturados por uso**. Eso conecta directamente con la decisión de arquitectura que el vault tiene abierta: su API expone **227 endpoints** ([[2026-1022-myclone-api-superficie-227-endpoints]]) y su capa de inferencia de prompts es **Dify** ([[2026-1022-gap-dify-como-capa-inferencia-prompts]]) — un clon con herramientas necesita un **MCP server** que exponga esas capacidades del producto como herramientas invocables por un modelo, y Heroku ofrece ese intermediario ya empaquetado en la plataforma.
El dato de por qué importa el cobro "pay-as-you-go": un MCP server **solo se paga cuando se invoca**, lo que lo hace compatible con un producto cuyo coste variable debe escala con el uso del cliente y no con el número de tenants. Es la misma propiedad que el vault busca en la inferencia por token, pero resuelta en la capa de orquestación en vez de en la de inferencia.
Y el límite honesto: **la captura no cuantifica nada de esto**. No hay precio de los MCP servers, ni de los one-off dynos, ni su relación con el precio de un dyno Cedar de $5. El vault no puede, con esta fuente, poner un número a la orquestación de herramientas; solo puede registrar que existe una **tercera forma de facturar** en la plataforma, y que es la que corresponde a la parte "Agents" del producto de Heroku.

## Nota de verificación
"one-off dynos" y "pay-as-you-go" son la formulación literal de la página; **no hay tabla de precios asociada a los MCP servers** en la captura, y el término "one-off" no aparece en ningún otro sitio del catálogo de dynos (que solo define Eco, Basic, Standard, Performance, Private, Shield y las familias Fir).
