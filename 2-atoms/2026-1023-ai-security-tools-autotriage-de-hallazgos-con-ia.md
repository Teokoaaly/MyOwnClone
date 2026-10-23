---
id: 2026-1023-ai-security-tools-autotriage-de-hallazgos-con-ia
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-gap-observabilidad-prompts-langfuse]]", "[[2026-1022-sin-rate-limiting]]", "[[2026-1023-ai-security-tools-taxonomia-15-categorias]]"]
---

## Claim
La primera categoría del listado —**"Autotriage of Security Findings"**, 7 entradas— cubre el problema de que los escáneres producen ruido que nadie filtra: herramientas que triagean, deduplican, priorizan o validan la salida de otros escáneres. Casos literales: `Metis` (Arm, 877 ★) — triaje de hallazgos SARIF con navegación al código fuente, grafo de código C/C++ opcional y decisiones LLM estructuradas, con la advertencia de que "model verdicts are not proof of exploitability"; `nuclei-autotriage` (CyberOK) — triage en dos etapas de hallazgos Nuclei (falsificador + pasada red-team) contra endpoints OpenAI-compatible; `seclab-taskflow-agent` (GitHub Security Lab, 268 ★) — agente YAML para triagear alertas de CodeQL/SAST y filtrar falsos positivos; `honeyslop` — señuelos "code-canary" para triagear reportes de vulnerabilidad **alucinados por IA** que inundan los programas de bug bounty; `SigmaOptimizer` — genera, prueba y refina reglas Sigma desde logs reales con comprobación de falsos positivos.

## Why It Matters
Es la categoría que más directamente se parece a lo que el vault ya hace: auditar una superficie y quedarse con lo que importa. La diferencia es que aquí la lógica de triaje es **un LLM que lee el hallazgo y el código y decide**, no un criterio explícito. Eso tiene un coste conocido y documentado en la propia ficha de `Metis`: el proveedor alojado recibe código y evidencia, requiere credenciales, y los trazas de depuración pueden contener contenido sensible. Es decir, **filtrar hallazgos con IA mueve datos sensibles a un tercero**.

La conexión con el resto de la taxonomía es que esta es la categoría más pequeña de herramientas pero la primera del listado ([[2026-1023-ai-security-tools-taxonomia-15-categorias]]): el campo la ha colocado primero por dificultad, no por volumen. Y el paralelismo con lo que ya registró el vault es directo: auditar una superficie y quedarse con lo que importa es la misma disciplina que [[2026-1022-sin-rate-limiting]] describe al exigir rate limiting en vez de confiar en el buen uso. La entrada `honeyslop` es la más transferible: un señuelo que delata reportes generados sin evidencia filtra ruido sin necesidad de modelo ni de enviar código. Y `SigmaOptimizer`/los optimizadores de reglas son el patrón generalizable: la dedupe y priorización deterministas (hash, regla, cobertura) cuestan menos y son auditables que el juicio de un LLM.

## [FRICTION]
> [[2026-1022-gap-observabilidad-prompts-langfuse]] afirma que [[myownclone]] no tiene observabilidad de prompts, sin evaluación de calidad de las respuestas ni tracking de tokens por prompt.
> Este átomo presiona esa brecha desde el lado del campo: la industria ha construido una capa entera de herramientas cuyo propósito es **filtrar y verificar la salida de un detector antes de que llegue a un humano**, y esa capa es justamente la que necesita instrumentación para saber cuánto filtro aplica y con qué tasa de error.
> Ambas no pueden ser completamente correctas: o la ausencia de observabilidad es un gap menor porque el producto no genera volumen de hallazgos que filtrar (y entonces no hace falta la capa), o es exactamente el hueco que impide auditar el propio pipeline de calidad. Marcado para juicio humano, no auto-resuelto.
