---
id: 2026-1024-flokinet-consola-ipmi-virtual-y-panel-novnc
type: atom
certainty: solid
sources: [sources/2026-10-24-flokinet-vps-pricing.md]
links: ["[[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]", "[[2026-1024-buyvm-plantillas-os-100-y-panel-stallion-compatible-solusvm]]", "[[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]]", "[[2026-1024-flokinet-upgrade-de-storage-exige-ajustar-particiones-a-mano]]"]
---

## Claim
FlokiNET incluye en **los siete planes** una **"Virtual IPMI Console"** y describe un **panel de control remoto** que permite *"control over your VPS even while it is offline. There you can reboot, install Linux, access the remote console"*. La FAQ precisa que se trata de una **consola noVNC** en el área de cliente ("client area → My services → select your VPS → noVNC console"), útil *"particularly for troubleshooting network issues or eventful crashes and the server is not reachable through other protocols such as SSH or other management platforms such as CPanel/WHM"*. El panel es además el punto de **recuperación de backups** y de **creación manual de backups**.

## Why It Matters
Es el quinto modelo de panel del thread y el **único que publica su recuperación en dos pasos dentro del propio VPS**: acceso por consola **aunque el servidor esté apagado o no arranque**, lo que cubre el fallo que ninguna otra painel del vault cubre explícitamente (comparar con el Rescue Mode de Evoxt, [[2026-1024-evoxt-api-y-rescue-mode-para-gestion-de-vms]], y el Out-of-Band de HostBrr, [[2026-1024-hostbrr-virtfusion-panel-rebuild-os-vnc-y-telemetria]]). Para el stack del vault, donde el punto de fallo más probable no es el rendimiento sino **la configuración de red que impide entrar por SSH** —el escenario que la propia FAQ describe—, esto convierte la consola en la diferencia operativa entre "servidor caído" y "servidor recuperable". Y hay un segundo efecto: la consola **es el único camino para activar la autenticación por contraseña** si el despliegue se hizo solo con clave SSH, porque el VPS se aprovisiona con autenticación por clave y el cambio requiere editar `/etc/ssh/sshd_config` — un cambio que solo se puede hacer desde dentro.

## Nota de verificación
La captura **no** publica: nombre del software de panel, si existe API documentada, si hay plantillas de SO, telemetría de CPU/IO/red, ni si la consola IPMI virtual tiene coste. "Virtual IPMI Console" aparece como línea de spec en los siete planes sin más detalle.
