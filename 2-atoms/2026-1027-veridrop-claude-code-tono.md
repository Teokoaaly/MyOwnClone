---
id: 2026-1027-veridrop-claude-code-tonto
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-faq.md]
links: ["[[2026-1027-veridrop-thinking-signature]]", "[[2026-1027-veridrop-detectar-agua]]"]
---

## Claim

Si **Claude Code** parece "más tonto" de repente, es necesario distinguir entre dos situaciones: (1) si el relay cambió de modelo o usó un channel de reemplazo (como Kiro o Amazon Q), entonces la thinking signature no estará disponible y Veridrop marcará ese item con 0 puntos; (2) si la thinking signature es normal, la disminución de capacidades es más probable por contexto truncado o por system prompt inyectado adicional. La forma de diferenciarlas es ejecutar Veridrop con la misma configuración (mismo base_url y key) en la página de detección de Claude: si el signature falla, es problema de modelo; si pasa, el problema es de contexto o prompts adicionales.

## Why It Matters

Este razonamiento evita acusaciones erróneas contra un relay por "bajada de calidad" cuando en realidad la thinking signature es válida y el problema reside en la gestión de contexto o prompts del usuario. El vault puede usar este criterio como parte de su contrato de aceptación de proveedores: cero problemas graves en los detectores de Veridrop, coherencia stream/no-stream, identidad de modelo, y varianza de contador por debajo del 10%.

## Nota de verificación

El criterio de dos situaciones y la metodología de diferenciación son literales de la sección «Claude Code 变笨了,是中转站换了模型吗?» de la FAQ. La captura no publica umbrales específicos de truncamiento de contexto ni las señales exactas de system prompt inyección, que requieren análisis de detalles por detector individual.