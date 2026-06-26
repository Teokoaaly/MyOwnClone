---
title: AI Clones
created: 2026-05-25
updated: 2026-05-25
type: concept
tags: [llm, saas, agent, automation]
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-technical-research.md]
confidence: high
---

# AI Clones

Clones de IA: modelos de lenguaje personalizados con el conocimiento, voz y estilo de una persona específica (normalmente un creador de contenido). El usuario interactúa con el clon como si hablara con la persona real.

## Cómo Funcionan

La arquitectura típica es **RAC (Retrieval Augmented Cognition)**:

1. **Ingestión**: el contenido del creador (vídeos, cursos, textos, entrevistas) se vectoriza y almacena en una base de datos vectorial
2. **Retrieval**: cuando un usuario hace una pregunta, el sistema busca los fragmentos más relevantes del conocimiento del creador
3. **Generación**: un LLM (OpenAI/Anthropic) genera la respuesta usando solo el contenido recuperado + instrucciones de personalidad
4. **Guardrails**: si el retrieval no supera un umbral de similitud, el clon admite que no sabe

## Modos de Operación

[[myownclone]] implementa tres modos con retrieval paths separados:

| Modo | Función | Retrieval Path |
|------|---------|---------------|
| Pedagogía | Enseñar con el contenido del creador | Conocimiento del curso |
| Ventas | Recomendar productos, convertir | Info de productos, ofertas |
| Soporte | Resolver dudas, escalar a humano | Base de conocimiento de soporte |

^[raw/articles/myownclone-founder-transcript.md]

## Aplicaciones de Negocio

- **Conversión de low-ticket a high-ticket**: curso pregrabado (pirateable) → curso + clon personalizado (no pirateable, mayor valor)
- **Captación de leads**: el clon pide email antes de interactuar → base de datos exportable a CRM
- **Soporte 24/7**: respuestas automatizadas con escalado a humano
- **Insights de audiencia**: preguntas frecuentes, gaps de conocimiento, perfil de avatar

## Desafíos Técnicos

- **Alucinación**: evitar que el LLM invente fuera del conocimiento del creador
- **Separación de hablantes**: en entrevistas, solo usar la voz del creador, no del entrevistador
- **Contexto por instancia**: el clon debe saber desde qué vídeo/curso/clase viene el usuario
- **Coste**: tracking de costes por tenant (respuestas, ingestion, platform ops)

## Ver también

- [[myownclone]] — implementación comercial
- [[delfi]] — competidor pionero
- [[retrieval-augmented-cognition]] — la tecnología core
- [[context-aware-instances]] — instancias contextuales
