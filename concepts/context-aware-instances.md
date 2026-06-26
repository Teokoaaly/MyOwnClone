---
title: Context-Aware Instances
created: 2026-05-25
updated: 2026-05-25
type: concept
tags: [llm, saas, architecture]
sources: [raw/articles/myownclone-founder-transcript.md]
confidence: medium
---

# Context-Aware Instances

Sistema de [[myownclone]] que permite que cada enlace compartido del clon tenga un contexto específico asociado.

## Cómo Funciona

1. El creador sube un vídeo de YouTube sobre un tema (ej: "fitness")
2. El clon entrena específicamente sobre ese vídeo
3. El enlace generado para compartir lleva el contexto del vídeo
4. Cuando un usuario llega desde ese enlace, el clon sabe de qué vídeo viene y limita el retrieval a ese contexto

^[raw/articles/myownclone-founder-transcript.md]

## Casos de Uso

- **Vídeos de YouTube**: "si queréis seguir charlando sobre este tema, hablad con mi clon" → el clon ya sabe el contexto
- **Landing pages**: cada página de venta puede tener su propia instancia del clon con contexto de ese producto
- **Cursos por módulos**: cada módulo tiene su instancia, el clon solo responde sobre ese módulo

## Ventajas

- Experiencia personalizada por punto de entrada
- Evita que el clon mezcle contenidos de distintos cursos/productos
- El creador controla qué conocimiento está disponible en cada contexto
- El clon puede pedir email antes de hablar → funciona como lead magnet contextual

## Ver también

- [[myownclone]]
- [[ai-clones]]
- [[retrieval-augmented-cognition]]
