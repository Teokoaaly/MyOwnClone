---
id: 2026-1023-hetzner-api-cli-e-integraciones-iac
type: atom
certainty: solid
sources: [sources/2026-10-22-hetzner-cloud.md, sources/2026-11-03-hetzner-cloud.md]
links: ["[[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]", "[[2026-1022-myclone-api-rest]]", "[[2026-1022-mutaciones-rsc-sin-api-rest]]"]
---

## Claim
Hetzner expone **toda la gestión de la infraestructura cloud vía una REST API developer-friendly y una CLI**, y publica integraciones para lenguajes de programación (**Python**, **Go**) y frameworks de gestión (**Ansible, Terraform, Kubernetes**), con el fin explícito de permitir un alto grado de automatización e integración, "por ejemplo, en pipelines de CI/CD". La página describe además las **Networks** (comunicación entre servidores por red privada, topologías complejas, casos como un clúster Kubernetes o una base de datos no accesible públicamente) e **Images** (Ubuntu, Debian, Fedora y otras distribuciones Linux).

## Why It Matters
La diferencia clave con el stack serverless del vault: [[2026-1022-mutaciones-rsc-sin-api-rest]] documenta que el producto no expone API REST y que las mutaciones viajan por Server Actions/RSC — es decir, **no hay superficie de API propia que un script externo pueda llamar**, salvo la de autenticación ([[2026-1022-myclone-api-rest]]). Un VPS con Terraform o Ansible invierte eso: da una API de gestión del servidor que sí es consumible por CI/CD, y una red privada que permite mantener la base de datos (Neon u otra) no expuesta públicamente. Es la pieza que hace posible un pipeline de despliegue propio — el mismo objetivo que persiguen las apps de un clic ([[2026-1023-hetzner-apps-un-clic-gratuitas-incluidas]]) y el siguiente paso tras el VPS nginx ya existente ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]).

## Nota de verificación
La captura no publica precios de API, límites de rate, costes de las imágenes personalizadas, ni si el uso de Terraform/Ansible tiene coste adicional. No se afirma ninguno de esos datos.

## Nota de extensión 2026-11-03
Fuente: `sources/2026-10-31-hetzner-cloud.md`, `sources/2026-11-01-hetzner-cloud.md`, `sources/2026-11-02-hetzner-cloud.md`. El bloque de features se repite **literalmente** en las tres capturas: **API REST + CLI**, integraciones para **Python y Go** y frameworks **Ansible, Terraform, Kubernetes** con mención explícita a pipelines de CI/CD, **Networks** (red privada, clústeres Kubernetes, bases de datos no públicas), **Firewalls** stateful sin coste adicional e **Images** (Ubuntu, Debian, Fedora y otras distribuciones). Sin cambios en el periodo.

La captura del 2026-11-01 añade, en el menú del sitio, que el acceso a la infraestructura se hace desde **Console**, **Robot** y **konsoleh** (tres interfaces distintas de Hetzner), y que la sección Resources incluye **Status** (system and service status) y **API** con enlace a `docs.hetzner.cloud`. Ninguna de las tres capturas publica **precios de API, límites de rate ni coste de las imágenes personalizadas**: la ausencia que este átomo ya señalaba sigue vigente, y por tanto la automatización vía Terraform/Ansible sigue siendo **gratuita pero no cuantificada** —lo que la hace sospechosa de coste de tiempo propio en el despliegue del vault, no de licencia.

## 2026-11-03 — re-verificación
Fuente: `sources/2026-11-03-hetzner-cloud.md`. El bloque "Everything you need, included" se repite **literalmente**: **API** REST developer-friendly + CLI, integraciones para **Python y Go** y frameworks **Ansible, Terraform, Kubernetes** con la mención explícita a pipelines de CI/CD, **Networks** (red privada entre servidores, topologías complejas, clúster Kubernetes o base de datos no accesible públicamente), **Firewalls** stateful sin costes adicionales y asignables a tantos servidores como se quiera, e **Images** (Ubuntu, Debian, Fedora y otras distribuciones Linux). Sin cambios. La captura **no publica** precios de API, límites de rate, coste de imágenes personalizadas ni coste de las redes privadas: la automatización vía Terraform/Ansible sigue siendo **gratuita pero no cuantificada**, que era la conclusión de este átomo. Ver [[2026-1103-hetzner-cinco-capturas-estabilidad-catalogo-vs-widgets-dinamicos]].
