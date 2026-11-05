---
id: 2026-1104-clerk-retencion-de-logs-1-7-y-30-dias-y-admin-logs-solo-business
type: atom
certainty: solid
sources: [sources/2026-11-04-clerk-pricing.md]
links: ["[[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]]", "[[2026-1101-clerk-enterprise-precio-custom-y-sla-9999]]", "[[2026-1101-clerk-gating-por-plan-contradice-atom-1031]]"]
---

## Claim
La retención de logs de Clerk es una **escalera de tres escalones por plan** — Application Logs con **1 día** en Hobby, **7 días** en Pro y **30 días** en Business, con **retención custom en Enterprise**— y los **Admin Logs** (auditoría de acciones de admin del workspace: cambios de configuración de instancia, edición de roles y permisos, rotación de secretos) son **"Not included" en Hobby y Pro** y solo existen en **Business con 30 días de retención**.

## Why It Matters
Es la línea de **trazabilidad** del stack de identidad, y su forma es reveladora: no es "cuánto se guarda" sino "**dónde empieza a existir la auditoría**". En el tramo gratuito de Clerk hay **retención de 1 día y nada de Admin Logs**, es decir, **un incidente de seguridad en Hobby es prácticamente no investigable**: se ve el evento del día y nada más, y no existe registro de quién cambió una configuración o rotó un secreto. Para un producto multi-tenant que va a vender a empresas —donde el cliente corporate querrá ver quién accede a su workspace— esa ausencia es un argumento de venta en contra del competidor, no un detalle de plan. Y el escalón que lo desbloquea es **Business, a $300/mes o $250/mes anual**, con protecciones avanzadas y SOC2 ([[2026-1101-clerk-enterprise-precio-custom-y-sla-9999]]): es decir, **la observabilidad y la compliance de Clerk live exactamente en el mismo plan**, el Enterprise de precio custom — lo que cierra el patrón de los tres proveedores de identidad del vault, en el que el tramo superior nunca es solo "más usuarios" sino "auditoría, SLA y contrato".

## Nota de verificación
Filas "Application Logs" y "Admin Logs" de la tabla "Full price breakdown", y bullets "Application Logs / 1 day retention", "Application and Admin Logs / 30 day retention" (Business) y "Custom retention" (Enterprise) de las tarjetas de plan de `sources/2026-11-04-clerk-pricing.md`, verbatim. El átomo [[2026-1101-clerk-plan-gratuito-50000-mru-y-3-asientos]] ya recogía el dato de 1 día en Hobby; este átomo añade la escalera completa y la exclusión de Admin Logs en Pro, que no estaban atomizadas.
