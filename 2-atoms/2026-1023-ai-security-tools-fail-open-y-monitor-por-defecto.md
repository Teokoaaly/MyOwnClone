---
id: 2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto
type: atom
certainty: tentative
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1022-gap-observabilidad-prompts-langfuse]]", "[[2026-1022-myclone-langfuse-observabilidad]]", "[[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]"]
---

## Claim
En las fichas de runtime del listado, la **postura por defecto es monitor-only y fail-open**, no bloqueo. Casos literales: *Numbat* — "monitoring is the default posture; blocking is opt-in, limited to supported synchronous pre-action hooks, and the shipped rules are monitor-only until operators explicitly configure enforcement"; *Norviq* — "ships in audit mode … all shipped policy presets default to allow"; *xaidr* — "monitor mode is the default and unexpected scan failures fail open"; *StackOne Defender* — "blocking high-risk results is opt-in by default; missing Tier-2 dependencies can fall back to simpler Tier-1 detection unless strict mode is enabled"; *sofagent* — "the default setup is not fail-closed and Git hooks can be bypassed"; *Crust* — "parse failures can pass the original body through"; *agentsh* — "the shell shim bypasses policy for non-TTY stdin unless `--force` is used, which is critical for headless agents and CI"; *Future AGI* — "Gateway guardrails are disabled by default, and scanner timeout/panic handling defaults to fail-open".

## Why It Matters
*tentative* — la inferencia es del lector, no del repo: el patrón dominante en el campo es **visibilidad primero, enforcement después de configurar**. Eso conecta con la brecha de observabilidad del vault ([[2026-1022-gap-observabilidad-prompts-langfuse]]): sin trazas no hay ni alerta ni bloqueo posible, y el propio competidor que sí tiene esa capa ([[2026-1022-myclone-langfuse-observabilidad]]) la usa en modo evaluación offline (`llm-judge`, `llm-rag`) antes que como control de runtime. La consecuencia práctica es que un producto que copia un "guardarrail" de esta lista sin instrumentación está copiando la parte fail-open sin la parte fail-closed.

El patrón no es accidental: la misma subsección de runtime que agrupa estas 61 entradas es la que concentra las herramientas de contención ([[2026-1023-ai-security-tools-runtime-61-entradas-aislamiento-no-deteccion]]). El campo construyó primero la capa de "ver y avisar" y dejó el bloqueo como configuración explícita del operador, no como comportamiento por defecto.

Nota de método: la enumeración de casos sale de leer las fichas del README; el README no afirma esta generalización de forma explícita.
