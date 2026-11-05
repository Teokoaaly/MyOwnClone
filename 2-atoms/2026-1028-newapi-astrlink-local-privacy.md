---
id: 2026-1028-newapi-astrlink-local-privacy
type: atom
certainty: solid
sources: [sources/2026-10-28-newapi-docs-home.md]
links: ["[[2026-1028-astrlink-api-protocols]]", "[[2026-1028-astrlink-on-device-privacy]]"]
---

## Claim

AstrLink ensures that secrets, phone numbers, and names are swapped for placeholders on the user's machine and restored when the reply arrives, keeping sensitive data local and never transmitting it upstream. This local-first privacy model enables agents to work with confidential data without external exposure.

## Why It Matters

The "Secrets stay local. Agents keep working." principle means that API keys, phone numbers, and personal names are never sent in cleartext to the AstrLink gateway or any external service. Placeholder substitution occurs on the client machine, and restoration happens when the reply returns. This enables compliance with data protection regulations and protects user privacy in agentic workflows where sensitive information must be processed but not exposed. The New API documentation home reinforces this model as foundational to the platform's philosophy of connecting AI providers while keeping data under user control.

## [FRICTION]

> La creencia de que el sustitución de placeholders resuelve todos los riesgos de privacidad ignora los vectores de side-channel y las fugas en la capa de aplicación. Aunque secrets son swappeados en la máquina del usuario, la lógica de restauración y el contexto de sesión pueden aún contener metadata sensible que los proveedores upstream puedan inferir. El modelo "agents keep working" presume que la disponibilidad local de datos es suficiente, pero en flujos de trabajo multi-step que cruzan múltiples proveedores, el tracking de qué placeholders fueron restaurados y cuáles no puede volverse ambiguous. Además, la creencia de que "secrets stay local" se extiende automáticamente a todo el pipeline de agentes ignora que agentes third-party o plugins pueden manejar datos de forma distinta, introduciendo puntos de exposición que el gateway AstrLink no controle. No hay contradicción técnica, pero sí fricción en la suposición de que la privacidad en la capa de gateway garantiza privacidad en todo el flujo de trabajo del agente. Marcado para juicio humano, no auto-resuelto.