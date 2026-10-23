---
id: 2026-1023-ai-security-tools-honeypots-llm-y-decepcion-6-entradas
type: atom
certainty: solid
sources: [sources/2026-10-22-awesome-ai-security-tools.md]
links: ["[[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]", "[[2026-1022-dns-superficie-publica-myownclone]]", "[[2026-1023-ai-security-tools-taxonomia-15-categorias]]"]
---

## Claim
El listado incluye una categoría pequeña y específica —**"LLM Honeypots & Deception"**, 6 entradas— donde la defensa es actively engañar al atacante: `Beelzebub` (2.194 ★, honeypot low-code en Go que simula servicios SSH/HTTP/**MCP** con LLMs), `DECEIVE` (Cisco Talos, honeypot SSH con LLM que evalúa cada sesión como benigna, sospechosa o maliciosa), `TRAP` (ACL 2024, "Targeted Random Adversarial Prompt": identifica uso black-box de LLM mediante sufijos de prompt específicos de modelo), `shelLM` y `VelLMes` (Stratosphere, honeypots SSH multi-protocolo) y `llm-honeypot` (Cowrie extendido con trampas de prompt injection para detectar agentes LLM hackers).

## Why It Matters
Es la categoría donde el campo invierte el objetivo: en vez de bloquear al atacante, se le da un señuelo creíble para que revele su método. Dos consecuencias para el vault. Primera: **el MCP aparece como protocolo honeypot**, no solo como superficie de ataque a defender ([[2026-1023-ai-security-tools-mcp-como-superficie-de-ataque]]) — un servicio MCP falso es un honeypot natural, porque el atacante que lo encuentra ejecuta sus herramientas contra un señuelo y escribe un informe que delata su arsenal. Segunda: la categoría es un recordatorio de que **cualquier endpoint público de un producto con IA es un objetivo automatizable**, y que un despliegue propio expone la superficie DNS y HTTP que el vault ya tiene catalogada ([[2026-1022-dns-superficie-publica-myownclone]]).

Y hay un matiz de escalado que el listado documenta: `TRAP` demuestra que el uso de un LLM se puede detectar por la huella del prompt. Un producto con IA en servidor que responde a peticiones arbitrarias está, por construcción, exponiendo ese mismo rasgo — el detector existe para ambos lados de la frontera. Con solo 6 entradas, esta es la categoría más pequeña del listado ([[2026-1023-ai-security-tools-taxonomia-15-categorias]]), y también la más barata de replicar: cada entrada es un servicio de señuelo, no una dependencia que instalar en producción.
