---
id: 2026-1024-hostkey-apps-preinstaladas-n8n-cpanel-fastpanel-plane-jitsi
type: atom
certainty: solid
sources: [sources/2026-10-23-hostkey-bitcoin-vps.md]
links: ["[[2026-1022-gap-workflows-myownclone]]", "[[2026-1022-plan-workflows-nuestro]]", "[[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]"]
---
## Claim
La página de Bitcoin VPS lista como **aplicaciones preinstaladas**: n8n Community Edition ("Extendable workflow automation tool. With a fair-code distribution model"), ispmanager, cPanel, MySQL, Fastpanel, Plane ("Open-source project management tool for sprint planning, task-tracking, and work roadmapping") y Jitsi ("Free and open-source multiplatform voice, video conferencing and instant messaging applications for Web & Mobile").

## Why It Matters
n8n y Plane son las dos piezas que el vault tiene anotadas como **hueco conocido del producto**: el flujo de trabajo interno como capa de orquestación (con su plan propio en [[2026-1022-plan-workflows-nuestro]] y su hueco documentado en [[2026-1022-gap-workflows-myownclone]]) y la gestión de sprints que MyOwnClone no resuelve por sí mismo. Descubrir que un proveedor de hosting paga la instalación de n8n CE **no es una solución al hueco**: n8n Community Edition es la versión de fair-code, sin el nivel de control ni de aislamiento multi-tenant que un SaaS de clones necesita, y además arrastraría datos de tenants hacia un panel del proveedor de hosting. La lectura útil es otra: es la señal de que el proveedor **compite por el workload de automatización en el borde**, no por el de clones de IA. Y contrasta con Hetzner, donde las apps de un clic también están documentadas ([[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]).
