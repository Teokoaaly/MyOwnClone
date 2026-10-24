---
id: 2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms
type: atom
certainty: solid
sources: [sources/2026-10-23-evoxt-vms.md, sources/2026-10-23-evoxt-vps-pricing.md]
links: ["[[2026-1023-hetzner-api-cli-e-integraciones-iac]]", "[[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]", "[[2026-1024-evoxt-kvm-aislamiento-y-hardware-enterprise]]", "[[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]"]
---

## Claim
La home de Evoxt añade dos funciones de gestión que **no aparecen en la página de precios** de la misma web: **API** ("controla, edita y configura tus máquinas virtuales sin necesidad de iniciar sesión en Evoxt"), documentada en `https://api.evoxt.com/`, y **Rescue Mode** ("¿tu VM se quedó atascada en el arranque? un clic para arrancar en modo rescate y realizar reparaciones o migraciones de datos"). La home las lista dentro de la barra de nueve funciones de gestión (Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups, VNC, API) y, en la lista de funciones adicionales, **Rescue Mode** aparte.

## Why It Matters
La **API documentada** sitúa a Evoxt en el mismo eje que la API/CLI de Hetzner y sus integraciones de IaC ([[2026-1023-hetzner-api-cli-e-integraciones-iac]]): sin API no hay aprovisionamiento programático, y el aprovisionamiento manual es la razón por la que un proveedor de low-cost se queda en pocos tenants — relevante cuando el objetivo es que el alta de un clon nuevo sea un clic. Y el **Rescue Mode** es la respuesta al peor incidente posible en un VPS autoalojado: repair o migración de datos cuando la VM no arranca, que es exactamente el punto ciego del despliegue vivo, un nginx autoalojado en una sola IP sin SLA ([[2026-1022-live-verify-deployment-migrada-a-vps-nginx]]). En conjunto, las dos son las piezas que convierten "hosting barato" en "hosting operable".

## Nota de verificación
La captura **no** publica el contenido de la documentación de api.evoxt.com (endpoints, autenticación, esquema, límites de rate), ni el nombre del mecanismo de rescate (initrd, ISO, kernel panic), ni si el Rescue Mode requiere reinicio. Solo se afirma la existencia de la API con su URL de documentación y la del Rescue Mode con su copy literal.

## [NOTA 2026-10-24]
La página de precios (`sources/2026-10-23-evoxt-vps-pricing.md`) cierra el inventario del panel: la barra de gestión de esa página enumera **siete funciones** — Monitoring, IP Management, Firewall, Cloning, Sub Accounts, Backups, VNC — **sin API ni Rescue Mode**, lo que confirma que API y Rescue Mode son exclusivos de la home. Ninguna de las siete tiene línea de precio: el catálogo solo publica el precio del plan (desde $2.99 en [[2026-1024-evoxt-plan-de-entrada-vm-0-5-a-2-99-dolar]]). La página de precios es además la única del vault con cifras de benchmark de Evoxt (GeekBench 5 multi-core, 1073 → 5265), es decir, la fuente del dato de rendimiento y no la home.
