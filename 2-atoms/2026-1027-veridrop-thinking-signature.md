---
id: 2026-1027-veridrop-thinking-signature
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-que-es-relay]]", "[[2026-1027-veridrop-diferencia-protocolo-oficial]]"]
---

## Claim

**thinking signature** es el artefacto de firma de cifrado que retorna el campo `signature` en la respuesta de Claude cuando el pensamiento extendido está habilitado. Tiene una longitud de 500-2000 caracteres y es generado por el servidor de Anthropic, con verificación de cifrado que, en teoría, ningún relay puede falsificar. Veridrop asigna un peso del 25% a esta señal como indicador central de autenticidad para el modelo Claude.

## Why It Matters

Es el estándar de oro para la verificación de autenticidad en el ecosistema Claude: a diferencia de afirmar «soy Claude» (que cualquier modelo entrenado sabe responder), la thinking signature es un indicador técnico criptográficamente fuerte. Si un relay no devuelve thinking signature, Veridrop asigna 0 puntos en esta categoría, señalando inmediatamente que el relay no está proporcionando el modelo auténtico de Claude, independientemente de qué modelo se anuncie en el campo `model`.

## Nota de verificación

La definición y peso (25%) son literales de la sección «thinking signature es qué?» y la cobertura de detectores de la FAQ. La captura no especifica la longitud exacta en todos los casos (puede variar según la versión de Claude ni el contexto de la solicitud), pero el rango 500-2000 caracteres es el especificado en la FAQ.