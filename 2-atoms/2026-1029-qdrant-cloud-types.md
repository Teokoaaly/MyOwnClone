---
id: 2026-1029-qdrant-cloud-types
type: atom
certainty: solid
sources: [0-raw/2026-10-29-qdrant-cloud-pricing.md]
links: ["[[2026-1029-qdrant-hybrid-cloud]]", "[[2026-1029-qdrant-private-cloud]]"]
---

## Claim

Las tres modalidades de Qdrant Cloud —Managed, Hybrid y Private— difieren en quién provee la infraestructura, el nivel de isolation, los SLAs y el modelo de compliance, siendo Managed el fully managed, Hybrid el bring-your-own-infrastructure y Private el on-premise dedicated deployment.

## Why It Matters

Entender las diferencias entre Managed, Hybrid y Private Cloud es esencial para elegir el modelo correcto según requisitos de residencia de datos, compliance, budget y nivel de control operativo. Cada modelo tradea off entre comodidad, control y responsibility de manera distinta, y la elección incorrecta puede implicar costos innecesarios o riesgo de compliance.

## [FRICTION]

> [[2026-1029-hybrid-cloud]] (escrita hace ~21 semanas) describe el Hybrid Cloud como "run managed Qdrant clusters on your own infrastructure using your compute, network and storage", mientras que [[2026-1029-private-cloud]] afirma que el Private Cloud es "dedicated, isolated deployment for strict security or compliance needs" con "full isolation" —la fricción es que ambos usan la infraestructura del usuario pero el nivel de isolation y responsibility difiere: en Hybrid, Qdrant gestiona el plano de control sobre la infraestructura del usuario, mientras que en Private, el usuario tiene control total tanto del plano de control como de datos, lo que cambia radicalmente el modelo de trust, access y compliance. Ambas satisfacen necesidades de datos locales pero con perfiles de risk y operational responsibility fundamentally diferentes. Marcado para juicio humano, no auto-resuelto.