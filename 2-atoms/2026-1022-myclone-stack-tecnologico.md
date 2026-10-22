---
id: 2026-1022-myclone-stack-tecnologico
type: atom
certainty: solid
sources: [raw/articles/myownclone-technical-deep-dive-2026-06-23.md, raw/articles/myclone-deep-api-osint-2026-06-24.md, raw/articles/myownclone-osint-implementation-handoff-2026-06-24.md]
links: ["[[2026-1022-myclone-competidor-arquitectura]]", "[[2026-1022-frontend-nextjs-vercel-sentry-posthog]]", "[[myownclone]]", "[[myownclone-competitors]]", "[[2026-1022-myclone-api-superficie-227-endpoints]]", "[[2026-1022-plan-langfuse-instrumentacion-nuestra]]"]
---
## Claim
MyClone.is opera con un stack confirmado por evidencia directa: dashboard en Next.js 13+ (App Router, rutas `/dashboard/*` y chunks en `_next/static/chunks/`), landing en Astro v5.16.11 (chunks en `/astro_chunks/`), hosting en Vercel (headers de respuesta y despliegues en edge), autenticación con NextAuth.js (Credentials + OAuth, rutas `/api/auth/*`), monitorización con Sentry, analítica con PostHog (`phc_zXjWGA3SNsR5sFCowUgXOXro4tWY7or485lpQzNQtzh`) y Google Tag Manager (`G-PHZWY08HCV`), y una base de datos descrita como "superset de PostgreSQL" que el autor marca explícitamente como **inferida**, no observada.

## Why It Matters
Es la línea base técnica contra la que comparar la arquitectura de [[myownclone]] (cuyo stack —Next.js v14, Vercel, NextAuth, PostHog, Sentry, Neon PostgreSQL— ya está desglosado en [[2026-1022-frontend-nextjs-vercel-sentry-posthog]] y [[2026-1022-neon-postgres-serverless]]): ambas compiten con Next.js + Vercel + NextAuth + PostHog + Sentry, así que el stack no es el diferencial — el diferencial está en la UX, el widget y la voz. La coincidencia exacta de proveedores de instrumentación (PostHog, Sentry) sugiere que el equipo sigue un stack compartido o un andamiaje conocido, lo que hace barato replicar cualquier mejora de instrumentación en [[myownclone]]. La inferencia de PostgreSQL queda marcada como no verificada: no debe tratarse como hecho.

## Extensión (API OSINT 2026-06-24)
El OpenAPI 1.0.0 de `api.myclone.is` añade la capa de **backend**: **Python + Uvicorn (ASGI)** sobre **AWS** (54.208.x.x / 3.86.x.x, certificado Amazon RSA 2048 M01). Es decir, MyClone.is es una app **híbrida**: frontend JS/Next en Vercel, backend de dominio en Python autoalojado en AWS. Ver [[2026-1022-myclone-api-superficie-227-endpoints]].

## Extensión (Handoff OSINT+Implementación 2026-06-24)
El handoff añade la tabla de **servicios internos** del backend, cada uno visible por sus prefijos de ruta en la API: Voyage AI (`/embeddings/*`, 96.891 embeddings), Langfuse (`/langfuse/*`), Cartesia AI (`/cartesia/*`), ElevenLabs (`/eleven_labs/*`), LiveKit (`/livekit/*`), Stripe Connect (`/stripe/*`) y **Vercel AI SDK** como motor del streaming SSE de `stream-chat`. Es decir, el stack de dominio de MyClone.is es un patchwork de proveedores SaaS de IA (embeddings, voz x2, voz en tiempo real, pagos, observabilidad de prompts) orquestado por un backend Python propio.
Para [[myownclone]], la lectura relevante es qué **no** hay que replicar: [[2026-1022-plan-langfuse-instrumentacion-nuestra]] propone adoptar Langfuse como capa de observabilidad, pero nada del stack de voz ni de LiveKit está en el roadmap propio, lo que confirma que la wager del vault (chat de texto + RAG) es un subconjunto acotado del competidor.
