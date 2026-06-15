# 05 - Remediaciones aplicadas

## Remediaciones de alta prioridad y bajo riesgo

| Remediación | Archivos | Riesgo | Resultado |
|---|---|---|---|
| Versionar plantilla Nginx correcta | `ops/nginx.myownclone.conf.example` | Bajo | Evita que `/api/admin/*` y `/api/clone/*` salten el proxy de Next y fallen con `401`. |
| Documentar separación de planes/billing | `docs/manual-*`, `docs/auditoria/*` | Bajo | Reduce ambigüedad operativa: `/planes` es selección/upgrade; `/facturacion` es portal/historial/balance. |
| Documentar manejo seguro de bcrypt en env frontend | `docs/manual-tecnico/README.md`, `docs/auditoria/01-*` | Bajo | Evita repetir incidente donde dotenv rompe hashes con `$`. |
| Crear índice maestro navegable | `docs/README.md` | Bajo | Facilita onboarding y soporte. |

## Remediaciones ya existentes en la rama base

| Remediación | Estado |
|---|---|
| `ops/deploy-frontend.sh` escapa `$` para dotenv y excluye `PLATFORM_ADMIN_*` de `.env.production`. | Aplicado. |
| NextAuth consulta tabla canónica `accounts` antes del fallback legacy `users`. | Aplicado. |
| Proxy NextAuth valida cookie segura y añade headers `X-User-*` + `X-API-Key`. | Aplicado. |
| `useAdminFetch` evita bucles de redirección. | Aplicado. |
| `ops/myownclone-frontend.service` deja de usar la IP antigua y toma `HOSTNAME`/`PORT` del env compartido. | Aplicado el 2026-06-15. |
| `ops/docker-compose.backend.prod.yml` publica Postgres en `127.0.0.1:5432` para auth del frontend sin exponer la DB a Internet. | Aplicado el 2026-06-15. |
| `proxy.ts` usa cookie segura solo en HTTPS para no romper restauraciones por IP/HTTP. | Aplicado el 2026-06-15. |

## Pendientes no aplicados por riesgo o falta de acceso

| Pendiente | Motivo |
|---|---|
| Regenerar `package-lock.json` | Requiere PR dedicado y revisión de cambios masivos de dependencias. |
| Automatizar backups en VPS | Requiere decisión de destino/cifrado y política de retención. |
| Completar claves reales de Stripe, Resend, OpenAI y SendGrid inbound webhook. | La restauración quedó operativa sin esas integraciones, pero no completa para producción funcional total. |
