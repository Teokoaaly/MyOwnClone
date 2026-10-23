---
id: 2026-1023-ai-security-tools-aviso-de-no-es-un-escanner-como-patron-editorial
type: atom
certainty: tentative
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1023-ai-security-tools-sast-ia-como-skill-no-como-scanner]]", "[[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]", "[[2026-1023-ai-security-tools-telemetria-activa-por-defecto]]"]
---

## Claim
*tentative* — El README aplica un patrón editorial consistente: cada entrada lleva una advertencia de **qué no es** la herramienta. Casos literales: `lintlang` — "heuristic static instruction/config review only; not runtime enforcement, prompt-injection detection, semantic-correctness proof, or a security guarantee"; `Guardana` — "Not a general SAST scanner or compliance certification"; `open-appsec` — "detection claims are not a security guarantee"; `RAMPART` — "test framework built on PyRIT, not a runtime protection layer"; `owasp/AISVS` — "security standard and checklist, not an executable scanner"; `OWASP Agent Security Regression Harness` — "not a scanner, leaderboard, general benchmark, or guarantee of agent security"; `Agent Memory Guard` — "published benchmark numbers are project-reported and should be independently reproduced"; `Metis` — "Model verdicts are not proof of exploitability or grounds for automatic suppression"; `AgentLock` — "the published results include a suite where the defense costs more utility than the attack it prevents"; `CaMeL` — "maintainers explicitly warn that the interpreter may contain bugs and may not be fully secure".

## Why It Matters
La inferencia es del lector, pero es sólida: la lista está escrita por alguien que **rechaza sistemáticamente el marketing de "protección"**. Prácticamente cada entrada que podría leerse como un escudo lleva su contrapeso explícito. Para el vault esto es un patrón de lectura, no solo de la fuente: cuando el listado describa una herramienta como protección, la pregunta correcta es qué es exactamente lo que esa protección no cubre.

Dos consecuencias operativas: (a) el valor de esta fuente no está en las herramientas sino en el **vocabulario de límites** que aporta —"heuristic", "not a guarantee", "project-reported", "not independently reproduced"— que es directamente reutilizable al documentar cualquier control propio; (b) conecta con la evidencia de que el vault trabaja con un listón parecido: ya [[2026-1022-sin-rate-limiting]] y [[2026-1022-ausencia-csp-xss-sin-mitigacion]] están redactados en ese registro de "lo que falta, medido", sin marcar la ausencia como si existiera un marco de referencia omitido. La lista funciona como calibración: 80 de las 422 entradas mencionan explícitamente su licencia y 79 llevan la marca ⚠️ de verificación adicional, así que una entrada sin ninguna advertencia es la excepción, no la norma.

Los tres casos donde el patrón se ve con más claridad son los que atacan de frente la idea de "protección": el más popular de la lista de SAST con IA se autodescribe como skill, no como escáner ([[2026-1023-ai-security-tools-sast-ia-como-skill-no-como-scanner]]); las herramientas de runtime que se quedan en monitor por defecto y dejan pasar los fallos ([[2026-1023-ai-security-tools-fail-open-y-monitor-por-defecto]]); y las que abren su telemetría por defecto con un opt-out documentado ([[2026-1023-ai-security-tools-telemetria-activa-por-defecto]]).

Nota de método: el recuento de "entradas con advertencia de no-es-X" no se publica en el README; es una lectura del documento.
