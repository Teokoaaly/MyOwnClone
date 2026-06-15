# Capturas y evidencias visuales

## Estado actual

Las capturas reales del VPS anterior no se pueden generar porque el VPS fue eliminado y ya no hay servidor de producción accesible.

No se han fabricado capturas ni mockups para sustituir evidencias reales. Esto evita documentar un estado que no existe.

## Capturas obligatorias al restaurar VPS

| Pantalla | Ruta | Estado |
| --- | --- | --- |
| Landing pública | `/` | Pendiente de VPS nuevo |
| Login | `/login` | Pendiente de VPS nuevo |
| Dashboard usuario | `/resumen` | Pendiente de VPS nuevo |
| Setup / onboarding clon | ruta de setup activa | Pendiente de VPS nuevo |
| Plans / Upgrade | `/planes` | Pendiente de VPS nuevo |
| Billing | `/facturacion` | Pendiente de VPS nuevo |
| Admin overview | `/admin/resumen` | Pendiente de VPS nuevo |
| API plans | `/api/clone/plans` | Pendiente de VPS nuevo |
| API billing | `/api/clone/billing` | Pendiente de VPS nuevo |

## Convención de nombres

Guardar futuras capturas en esta carpeta con nombres estables:

```text
01-landing.png
02-login.png
03-dashboard-resumen.png
04-setup-clone.png
05-planes.png
06-facturacion.png
07-admin-resumen.png
08-api-plans.png
09-api-billing.png
```

## Comandos sugeridos

Cuando exista VPS nuevo:

```bash
curl -I https://myownclone.com/
curl -I https://myownclone.com/planes
curl -I https://myownclone.com/facturacion
bash ops/smoke-prod.sh https://myownclone.com
```

Para capturas visuales, usar navegador autenticado y no capturar secretos, cookies ni datos personales.
