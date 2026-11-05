---
id: 2026-1101-tailscale-logging-audit-y-flow-logs-para-observar-el-plano-de-red
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1101-tailscale-ssh-integrado-con-grabacion-de-sesion]]", "[[2026-1022-myclone-stack-tecnologico]]"]
---

## Claim
La sección **"Logging, Streaming, and Events"** (`/docs/reference/logging-streaming-events`) de la documentación de Tailscale enumera: "Logging overview", "Configuration audit logging", "Network flow logs", "Log streaming", "SSH session recording", "Client metrics" y "Webhooks". Además, el índice principal incluye la entrada con descripción explícita *"Logging overview — Understand Tailscale's logging infrastructure."* Es la única señal del corpus de que Tailscale tiene **una infraestructura de logging propia**, del plano de red, y no solo logs de aplicación.

## Why It Matters
El stack de MyOwnClone tiene observabilidad de aplicación (Langfuse para trazas de IA, Sentry para errores) pero **nada que observe el plano de red**, que es donde se manifestaría un acceso no autorizado al tailnet o un nodo inesperado ([[2026-1022-myclone-stack-tecnologico]]). "Configuration audit logging" y "Network flow logs" son, por título, la respuesta documental a dos preguntas que el vault tiene abiertas: *¿quién cambió la política del tailnet?* y *¿qué tráfico ha pasado entre nodos?*. "Log streaming" y "Webhooks" encajan con el patrón de Automations ya identificado, es decir, eventos del tailnet disparables hacia la automatización. La combinación con "SSH session recording" ([[2026-1101-tailscale-ssh-integrado-con-grabacion-de-sesion]]) cierra el ciclo de trazabilidad: acceso administrativo registrado, cambios de configuración registrados, flujos de red registrados. Límite honesto: son **solo títulos**; la captura no dice qué eventos se emiten, con qué retención, ni si el streaming de logs tiene coste. No hay ninguna cifra que verificar aquí.
