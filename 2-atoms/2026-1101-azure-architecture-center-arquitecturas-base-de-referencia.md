---
id: 2026-1101-azure-architecture-center-arquitecturas-base-de-referencia
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-cinco-tipos-de-artefacto]]", "[[2026-1022-myownclone-dos-repos-flask-nextjs]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]"]
---

## Claim
El center publica **arquitecturas base (baseline architectures)** por tipo de carga, no solo patrones: `virtual-machines/baseline` ("Azure VM baseline architecture"), `ai-ml/architecture/baseline-microsoft-foundry-chat` ("Microsoft Foundry chat baseline architecture") y `example-scenario/data/greenfield-lakehouse-fabric` ("Greenfield lakehouse on Microsoft Fabric"). La palabra *baseline* aparece como categoría explícita del catálogo.

## Why It Matters
Una *baseline architecture* es la respuesta de Microsoft a la pregunta "¿qué minimally necesita mi app para no estar mal hecha?" — una lista de piezas obligatorias antes de añadir extras. Es el formato exacto que falta en el vault: MyOwnClone tiene una topología de hecho (dos repos, Flask en 5001, Next.js en 3000, proxy `src/proxy.ts` como único mapa de rutas — ver [[2026-1022-myownclone-dos-repos-flask-nextjs]]), y un despliegue vivo ya endurecido con nginx ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]), pero **ningún documento declara qué es el mínimo**. Sin baseline escrita, cada nueva función (Weaviate, analítica, pasarelas de pago) se decide por inercia del stack, y el eje de coste del vault —que separa coste por asiento de coste de infraestructura— no tiene contra qué medir qué es "imprescindible" frente a "añadido por]].
