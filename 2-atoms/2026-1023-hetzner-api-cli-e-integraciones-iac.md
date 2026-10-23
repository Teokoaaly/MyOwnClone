---
id: 2026-1023-hetzner-api-cli-e-integraciones-iac
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]", "[[2026-1022-myclone-api-rest]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---

## Claim
Hetzner expone **toda la gestión de la infraestructura cloud vía una REST API developer-friendly y una CLI**, y publica integraciones para lenguajes de programación (**Python**, **Go**) y frameworks de gestión (**Ansible, Terraform, Kubernetes**), con el fin explícito de permitir un alto grado de automatización e integración, "por ejemplo, en pipelines de CI/CD". La página describe además las **Networks** (comunicación entre servidores por red privada, topologías complejas, casos como un clúster Kubernetes o una base de datos no accesible públicamente) e **Images** (Ubuntu, Debian, Fedora y otras distribuciones Linux).

## Why It Matters
La diferencia clave con el stack serverless del vault: [[2026-1022-mutaciones-rsc-sin-api-rest]] documenta que el producto no expone API REST y que las mutaciones viajan por Server Actions/RSC — es decir, **no hay superficie de API propia que un script externo pueda llamar**, salvo la de autenticación ([[2026-1022-myclone-api-rest]]). Un VPS con Terraform o Ansible invierte eso: da una API de gestión del servidor que sí es consumible por CI/CD, y una red privada que permite mantener la base de datos (Neon u otra) no expuesta públicamente. Es la pieza que hace posible un pipeline de despliegue propio — el mismo objetivo que persiguen las apps de un clic ([[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]) y el siguiente paso tras el VPS nginx ya existente ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]).

## Nota de verificación
La captura no publica precios de API, límites de rate, costes de las imágenes personalizadas, ni si el uso de Terraform/Ansible tiene coste adicional. No se afirma ninguno de esos datos.
