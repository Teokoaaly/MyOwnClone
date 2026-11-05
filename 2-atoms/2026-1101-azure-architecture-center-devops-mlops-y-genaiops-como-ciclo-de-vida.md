---
id: 2026-1101-azure-architecture-center-devops-mlops-y-genaiops-como-ciclo-de-vida
type: atom
certainty: solid
sources: [sources/2026-11-01-azure-architecture-center.md]
links: ["[[2026-1101-azure-architecture-center-arboles-de-decision-para-elegir-servicios]]", "[[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]", "[[2026-1022-myclone-langfuse-observabilidad]]"]
---

## Claim
El area "Operationalize application and AI workloads" define tres disciplinas encadenadas —**DevOps, MLOps y GenAIOps**— con entradas propias: `guide/devops/devops-get-started`, `ai-ml/guide/mlops-maturity-model` ("Assess your MLOps maturity") y `ai-ml/guide/genaiops-for-mlops` ("Extend MLOps with GenAIOps").

## Why It Matters
El vault tiene un hueco declarado en observabilidad: la verificación en vivo se hizo **sin instrumentación** de Sentry ni PostHog ([[2026-1023-live-verify-sin-instrumentacion-sentry-posthog]]), y la observabilidad de LLM quedó en Langfuse ([[2026-1022-myclone-langfuse-observabilidad]]). El *MLOps maturity model* ofrece la escala que falta: no "¿tengo métricas?" sino "¿en qué nivel estoy y cuál es el siguiente?", lo que convierte la ausencia de instrumentación en una posición en una escalera en vez de un vacío. Y **GenAIOps** (GenAI operations aplicado sobre MLOps) es directamente el dominio de MyOwnClone: los clones son el producto, así que el ciclo de vida del prompt, la evaluación de salidas y el despliegue de modelos *son* el ciclo de vida de la aplicación, no un adorno de IA encima.
