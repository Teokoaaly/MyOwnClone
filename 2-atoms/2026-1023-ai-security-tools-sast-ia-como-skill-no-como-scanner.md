---
id: 2026-1023-ai-security-tools-sast-ia-como-skill-no-como-scanner
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1023-ai-security-tools-agente-como-categoria-dominante]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]", "[[2026-1022-gap-observabilidad-prompts-langfuse]]"]
---

## Claim
La categoría **"AI-Powered SAST & Secure Code Review"** (22 entradas) está dominada por **workflows/skills para agentes de código**, no por escáneres deterministas: `Cloudflare Security Audit Skill` (28.989 ★), `Anthropic-Cybersecurity-Skills` (34.338 ★), `Trail of Bits Skills` (7.502 ★), `sast-skills` (1.335 ★), `Claude-BugHunter` (5.057 ★), `defending-code-reference-harness` de Anthropic (7.570 ★), `Mantis` de Google, `deepsec` de Vercel Labs, `VulnHunter` de Capital One, `Codex Security` de OpenAI. El propio README lo dice sin rodeos sobre el más popular: "workflow skill, not a standalone scanner; it requires a capable coding agent with parallel subagents and an OS-enforced sandbox. Results are nondeterministic, and Cloudflare reports that one run finds only about half of the vulnerabilities found across repeated runs."

## Why It Matters
El dato duro —"una ejecución encuentra solo la mitad de las vulnerabilidades que aparecen entre ejecuciones repetidas"— invalida cualquier lectura de "el análisis de seguridad de código ya está resuelto" y define la forma correcta de usar estas herramientas: **como generador de candidatos con falsos positivos alto, no como veredicto**. Eso reordena prioridades: si cada pasada encuentra la mitad, el presupuesto de seguridad se decide por cuántas pasadas se pagan, no por si la herramienta pasa o falla.

El patrón encaja con la taxonomía del campo: la seguridad de agentes de código es la categoría dominante del listado ([[2026-1023-ai-security-tools-agente-como-categoria-dominante]]), y dentro de ella el runtime de 61 entradas es donde se concentra la contención ([[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]). Es decir: la industria responde a "el análisis con IA es no determinista" construyendo más aislamiento, no más confianza en el veredicto.

Para el vault la lectura es doble. Por un lado, es la versión de código del mismo patrón que ya afecta al producto: la IA puede encontrar, pero la validación la hace un humano. Por otro, encaja con la ausencia de instrumentación: sin trazas, no se puede medir si el pipeline de análisis del producto se está degradando, igual que sin observabilidad de prompts no se puede medir la calidad de las respuestas ([[2026-1022-gap-observabilidad-prompts-langfuse]]). Y contrasta con la superficie de escritura del producto, que es Server Actions ([[2026-1022-mutaciones-rsc-sin-api-rest]]): un único canal de mutación es auditable con una regla determinista, que es más barato que un pipeline de agentes.

En la misma categoría, `VulnHunter` (Capital One) es explícito sobre el orden de operaciones: "forward analysis from exposed entry points, a finding-falsification pass, evidence-backed remediation, and a separate fix-verification flow" — falsificar antes de remediar, y verificar el arreglo por separado. Ese es el ciclo que el listado impone sobre cualquier hallazgo de IA: candidato → falsación → evidencia → arreglo → verificación.
