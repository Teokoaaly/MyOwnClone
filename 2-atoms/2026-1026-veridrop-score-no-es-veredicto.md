---
id: 2026-1026-veridrop-score-no-es-veredicto
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-profundidades-deteccion]]", "[[2026-1026-veridrop-firma-usage-field]]"]
---

## Claim
En Veridrop, una puntuación alta no garantiza un veredicto verde. Si existe siquiera un problema grave (por ejemplo, campos de Anthropic "filtrados" en la respuesta), el veredicto general se degrada a amarillo "cuidado", independientemente de la puntuación total. La puntuación y el veredicto son dimensiones independientes.

## Why It Matters
Los usuarios pueden interpretar mal la puntuación numérica como una garantía de calidad. Este átomo aclara que la puntuación mide la conformidad protocolar, mientras que el veredicto (círculo de color) también considera la presencia de problemas graves. Un relay puede tener buena puntuación técnica pero aún así presentar riesgos operativos si hay filtración de campos de otro proveedor. La distinción es crucial para decisiones de uso serio (código, tareas importantes) vs. uso casual (chats cotidianos).

## [FRICTION]
> [[2026-1027-veridrop-una-desviacion-grave-baja-el-veredicto-a-amarillo]] (escrita hace ~5 semanas) sostiene que dos criterios (llegada a 100 de firma criptográfica y CV < 0.10) definen una spec de calidad mínima, y que una desviación grave baja el veredicto a amarillo aunque el score alcance 70. Este átomo (2026-1026) coincide en el fenómeno (score alta + veredicto amarillo) pero llega a la conclusión operativa diferente: la nota de 2026-1027 se enfoca en los umbrales binarios de firma CV y calidad, mientras que este átomo (2026-1026) se enfoca en la independencia conceptual entre score y veredicto, que es una propiedad del diseño de Veridrop independientemente de los umbrales específicos. Ambas pueden ser correctas: los umbrales definen los límites numéricos, pero la independencia de score vs. veredicto es una propiedad de diseño del sistema. No hay contradicción auto-resuelta: son capas diferentes de la misma especificación.