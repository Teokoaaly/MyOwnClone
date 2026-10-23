---
id: 2026-1023-ai-security-tools-promptfoo-adquisicion-openai-marzo-2026
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1023-ai-security-tools-guardarrail-de-retrieval-no-es-guardarrail-de-seguridad]]", "[[2026-1022-myclone-langfuse-observabilidad]]", "[[2026-1022-genesis-software-con-ia]]"]
---

## Claim
El listado anota que **OpenAI anunció un acuerdo de adquisición de `promptfoo` en marzo de 2026**, y que el proyecto **sigue con licencia MIT** — con la recomendación explícita del propio README: "remains MIT-licensed — track governance". `promptfoo` es, con 25.956 ★, la entrada más popular de la sección de red-teaming de LLM: una CLI de evaluación y red-teaming/pentesting con más de 50 plugins de ataque. Es también la casa de `ModelAudit`, el escáner de artefactos de modelo con parsers estáticos y un compañero de análisis de pickles en Rust. En el mismo listado, `garak` (NVIDIA) aparece como "The LLM vulnerability scanner" con 9.548 ★, y `PyRIT` (Microsoft) como "battle-tested across 100+ GenAI red-team operations" — es decir, la categoría de la que habla esta adquisición es la de herramientas de entrada y salida de modelos, la misma que el vault distingue del guardarrail de retrieval ([[2026-1023-ai-security-tools-guardarrail-de-retrieval-no-es-guardarrail-de-seguridad]]).

## Why It Matters
Es una señal de consolidación en la capa de **evaluación y red-teaming de LLM**: el mayor estándar de facto de la categoría pasa a estar bajo control de un proveedor de modelos. El README no editorializa —solo pide "track governance"— pero para un vault que piensa en qué dependencias construir, el dato relevante es que el gobierno de esa dependencia puede cambiar aunque la licencia no.

Dos consecuencias concretas: (a) cualquier pipeline que dependa de `promptfoo` para evals hereda una dependencia con un único mantenedor corporativo detrás, con el riesgo de deprecación de formatos o de cambio de política de telemetría; (b) el propio README marca `ModelAudit` con telemetría activada por defecto, lo que en un producto con datos de clientes es un punto a decidir antes de instalar, no después.

La conexión con el competidor del vault es directa: MyClone.is usa `llm-judge` y `llm-rag` como evals en su capa de observabilidad ([[2026-1022-myclone-langfuse-observabilidad]]), es decir, ya usa el patrón que la industria implementa con `promptfoo`. Y [[2026-1022-genesis-software-con-ia]] explica por qué el vault acumula decisiones técnicas como activos: elegir dependencias de evaluación es una de esas decisiones con fecha de caducidad.
