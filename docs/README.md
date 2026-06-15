# Documentación MyOwnClone

Índice maestro tipo wiki para operación, auditoría y soporte.

## Sitios HTML

- [Manual público de usuario](./index.html)
- [Wiki técnica interna](./admin/index.html)
- [Plan de capturas y evidencias](./screenshots/README.md)

## 📋 Auditoría técnica

- [00 - Resumen ejecutivo](./auditoria/00-resumen-ejecutivo.md)
- [01 - Diferencias VPS vs GitHub](./auditoria/01-diferencias-vps-github.md)
- [02 - Cambios sincronizados](./auditoria/02-cambios-sincronizados.md)
- [03 - Auditoría técnica completa](./auditoria/03-auditoria-tecnica-completa.md)
- [04 - Plan de mejoras priorizado](./auditoria/04-plan-mejoras-priorizado.md)
- [05 - Remediaciones aplicadas](./auditoria/05-remediaciones-aplicadas.md)
- [Auditoría VPS previa 2026-06-14](./VPS_AUDIT_2026-06-14.md)

## 🛠️ Manual técnico y administración

- [Manual técnico](./manual-tecnico/README.md)
- [Guía de despliegue raíz](../DEPLOYMENT.md)
- [Arquitectura raíz](../ARCHITECTURE.md)
- [Setup raíz](../SETUP.md)

## 👤 Manual de usuario

- [Manual de usuario](./manual-usuario/README.md)

## 🏗️ Arquitectura y diagramas

- [Auditoría técnica - arquitectura](./auditoria/03-auditoria-tecnica-completa.md#1-arquitectura)
- [Manual técnico - arquitectura](./manual-tecnico/README.md#2-arquitectura-técnica)
- [Modelo de datos](./auditoria/03-auditoria-tecnica-completa.md#5-base-de-datos)

## 🚀 Despliegue

- [DEPLOYMENT.md](../DEPLOYMENT.md)
- [Frontend deploy script](../ops/deploy-frontend.sh)
- [Backend deploy script](../ops/deploy-backend.sh)
- [Nginx vhost example](../ops/nginx.myownclone.conf.example)
- [Smoke production script](../ops/smoke-prod.sh)

## 🔧 Troubleshooting

- [Manual técnico - Troubleshooting](./manual-tecnico/README.md#15-troubleshooting)
- [Manual de usuario - Solución de problemas](./manual-usuario/README.md#10-problemas-comunes)

## 📊 Decisiones técnicas

- Next.js actúa como proxy autenticado para rutas frontend API.
- Flask es la API canónica de negocio.
- `accounts` es la tabla canónica backend; `users` se conserva como fallback legacy.
- `/planes` es selección/upgrade; `/facturacion` es billing, portal e historial.
- `PLATFORM_ADMIN_*` se carga desde systemd EnvironmentFile, no desde `.env.production` de Next.

## Estado operativo conocido

- Última release VPS verificada previamente: `/opt/myownclone/releases/20260614162441-codex-plans-page`.
- El 2026-06-15 no había acceso SSH no interactivo disponible; ejecutar revalidación VPS al restaurar acceso.
