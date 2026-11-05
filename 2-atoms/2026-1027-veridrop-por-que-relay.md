---
id: 2026-1027-veridrop-por-que-relay
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-que-es-relay]]", "[[2026-1027-veridrop-protocolo-diferencias-official-vs-relay]]"]
---

## Claim

Tres son las razones principales por las que usuarios recurren a las **AI API 中转站**: (1) el acceso directo a dominios como anthropic.com / openai.com requiere ciencia de red desde muchos territorios; (2) algunos relay aglutinan el excedente de múltiples proveedores y los venden al por menor, con precios 30-70% más bajos que los oficiales; (3) ciertos relay unifican Claude / GPT / Gemini en una sola interfaz OpenAI compatible, reduciendo la carga de mantenimiento de código. Sin embargo, cada razón conlleva compromisos de transparencia y riesgo.

## Why It Matters

El vault decide sobre el uso de relay basándose en este balance: si la prioridad es costo bajo y se acepta la pérdida de transparencia operativa, un relay bien evaluado con Veridrop es aceptable. Para escenarios de producción crítica o manejos de secretos comerciales, la recomendación es conectar directamente al proveedor oficial, ya que el riesgo de modificaciones ocultas en el flujo de respuesta (system prompt injection, model substitution, token inflation) es unacceptable.

## Nota de verificación

Los tres motivos son literales de la sección «中转站基础» de la FAQ. La captura no enumera las variantes de negocio específicas de cada proveedor, que serían materia de investigación independiente o del líderboard de Veridrop.