---
title: Retrieval Augmented Cognition (RAC)
created: 2026-05-25
updated: 2026-05-25
type: concept
tags: [llm, rag, database, ai]
sources: [raw/articles/myownclone-founder-transcript.md, raw/articles/myownclone-technical-research.md]
confidence: high
---

# Retrieval Augmented Cognition (RAC)

"RAC" es el término que usa [[eugenio-oller]] para describir la arquitectura core de [[myownclone]]. Es una variante de RAG (Retrieval Augmented Generation) aplicada a clones de IA.

## Mecanismo

1. **Base de datos vectorizada**: el conocimiento del creador se almacena como embeddings
2. **Retrieval pre-respuesta**: antes de que el LLM genere texto, se recupera la información relevante de la base vectorial ^[raw/articles/myownclone-founder-transcript.md]
3. **Inyección de contexto**: los fragmentos recuperados se inyectan en el prompt del LLM
4. **Umbral de similitud**: si ningún fragmento supera el coeficiente de comparación, el clon responde "no tengo conocimiento sobre eso" ^[raw/articles/myownclone-founder-transcript.md]

## Diferenciación de myownclone

- **Tres retrieval paths separados**: aprendizaje, soporte, ventas — cada uno busca en su propio namespace vectorial ^[raw/articles/myownclone-founder-transcript.md]
- **Separación de hablantes**: en entrevistas, solo indexa la voz del creador, no la del entrevistador ^[raw/articles/myownclone-founder-transcript.md]
- **Contexto por instancia**: el retrieval puede limitarse al contenido de un vídeo/curso específico según el enlace de entrada ^[raw/articles/myownclone-founder-transcript.md]

## vs RAG Tradicional

| Aspecto | RAG estándar | RAC (myownclone) |
|---------|-------------|---------------|
| Fuente | Documentos genéricos | Solo contenido del creador |
| Personalidad | Neutra | Estilo y voz del creador |
| Fallback | Puede alucinar | "No tengo conocimiento" |
| Multi-namespace | No | 3 paths separados |
| Cost tracking | No | Por tenant y categoría |

## Ver también

- [[ai-clones]]
- [[myownclone]]
- [[context-aware-instances]]
