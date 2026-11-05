---
id: 2026-1026-veridrop-profundidades-deteccion
type: atom
certainty: solid
sources: [sources/2026-10-26-veridrop-openai-detection.md]
links: ["[[2026-1026-veridrop-ocho-checks-protocol-chatcompletions]]", "[[2026-1026-veridrop-firma-usage-field]]"]
---

## Claim
Veridrop ofrece tres niveles de profundidad de detección: profundidad (~15 segundos, 3 verificaciones), estándar (~40 segundos, 6 verificaciones) y completa (~70 segundos, todas las 6 categorías). El nivel determina cuántos protocolos y campos se inspeccionan, no la rigurosidad de cada una individualmente.

## Why It Matters
El usuario puede elegir el equilibrio entre velocidad y exhaustividad. En un entorno de producción, el modo profundidad puede servir como filtro rápido; el modo estándar es suficiente para la mayoría de los casos de uso; y el modo completa es necesario cuando la integridad del modelo es crítica (por ejemplo, al ejecutar código o tareas que dependen de capacidades específicas del modelo). Conocer los límites de tiempo y verificación ayuda a planificar el uso del detector en flujos de trabajo automatizados.

## [FRICTION]
> [[2026-1027-veridrop-los-tres-modos-de-deteccion-y-sus-conteos-no-coinciden-entre-paginas]] (escrita hace ~5 semanas) enumera los mismos tres modos pero atribuye conteos diferentes de detectores a cada uno. Este átomo (2026-1026) coincide en la existencia de tres modos pero discrepa en la numeración: la nota de 2026-1027 dice "el modo rápido incluye igualmente el detector de firma criptográfica", mientras que la fuente original (capture 2026-10-26) describe los tres modos como "rápido (~15s, 3 items)", "estándar (~40s, 6 items)" y "completo (~70s, full 6 items)" sin mención de firma criptográfica en el rápido. La captura original de 2026-10-26 no menciona firma criptográfica en los modos rápidos, mientras que la nota de 2026-1027 lo añade. Dado que la fuente original (capture) no lo incluye, esta nota (2026-1026) mantiene lealtad al texto capturado y la de 2026-1027 extiende con información posterior. No hay contradicción auto-resuelta: son versiones distintas del mismo esquema, una basada puramente en la captura, la otra en la evolución documentada.