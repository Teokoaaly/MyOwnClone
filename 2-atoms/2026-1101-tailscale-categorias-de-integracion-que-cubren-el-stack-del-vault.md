---
id: 2026-1101-tailscale-categorias-de-integracion-que-cubren-el-stack-del-vault
type: atom
certainty: solid
sources: [sources/2026-11-01-tailscale-docs.md]
links: ["[[2026-1031-tailscale-docs]]", "[[2026-1022-myclone-stack-tecnologico]]", "[[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]"]
---

## Claim
La sección "Integrations" de la documentación de Tailscale enumera **diez categorías de integración**, y varias cubren el stack del vault una a una: **"Containers and virtualization"**, **"Databases"** (`/docs/database`), **"Firewalls"**, **"Web servers"**, **"Cloud servers"**, **"Serverless apps"**, **"Kubernetes Operator"**, **"Remote environments"**, "Developer tools", "NAS". En la sección "Route Traffic" del índice aparece además "Set up an app connector", cuya descripción no está en la captura.

## Why It Matters
Confirma que la documentación de Tailscale **no es solo una VPN de hosts**: hay categorías específicas de bases de datos, contenedores y firewalls, que es lo que necesita un despliegue donde Postgres, Redis y el api corren en contenedores y solo nginx tiene salida pública. Que exista una categoría "Firewalls" y otra "Cloud servers" sugiere —sin que la captura lo diga— coexistencia documentada con UFW/iptables y con los proveedores donde vive el VPS barato del vault ([[2026-1023-hetzner-presupuesto-4-euros-no-alcanza]]). El "app connector" sería la vía documentada para que el worker alcance servicios de terceros (LLM, email) sin abrirlos. Límite honesto: la captura da **solo los títulos de las categorías** —ninguna descripción, ningún ejemplo—, así que no permite afirmar qué se hace en cada una.
