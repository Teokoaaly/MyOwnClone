# 02 - Cambios sincronizados

Fecha: 2026-06-15  
Rama: `audit/vps-sync-and-docs`

## Cambios válidos incorporados desde la operación VPS

| Cambio | Estado | Commit/archivo | Evidencia |
|---|---|---|---|
| Hardening del deploy frontend para `.env.production` legible por `myownclone` y compatible con bcrypt (`$`) | Sincronizado | `ops/deploy-frontend.sh` | Hotfix aplicado en VPS; script ahora genera `.env.production` desde shared env excluyendo `PLATFORM_ADMIN_*`. |
| Autenticación frontend contra tabla backend `accounts` | Sincronizado | `MyOwnClone/src/lib/auth.ts` | Corrige login de cuentas canónicas de Flask/Alembic. |
| Proxy NextAuth para rutas protegidas | Sincronizado | `MyOwnClone/src/proxy.ts` | Lee cookie segura `__Secure-authjs.session-token` y añade headers de identidad al backend. |
| Separación `/planes` y `/facturacion` | Sincronizado | `MyOwnClone/src/app/(dashboard)/planes/page.tsx`, `facturacion/page.tsx` | `/planes` usa diseño de landing; `/facturacion` queda para billing/portal/historial. |
| Prevención de bucle en admin fetch | Sincronizado | `MyOwnClone/src/components/admin/useAdminFetch.ts` | Usa `credentials: "include"` y evita redirecciones repetidas. |
| Plantilla Nginx correcta | Añadido en esta rama | `ops/nginx.myownclone.conf.example` | Documenta que `/api/admin`, `/api/clone` y `/api/*` deben ir a Next.js, no directo a Flask. |
| Auditoría/manuales | Añadido en esta rama | `docs/auditoria/*`, `docs/manual-*/*`, `docs/README.md` | Nueva documentación operativa y técnica. |

## Cambios NO sincronizados por seguridad

| Elemento | Motivo | Acción |
|---|---|---|
| `/opt/myownclone/shared/*.env.production` | Contiene secretos reales. | Documentar nombres de variables; gestionar con secret manager o archivos 0600 en VPS. |
| Logs de `journalctl`, Nginx y Docker | Pueden contener trazas, IPs, tokens o payloads. | Guardar solo extractos redaccionados si son necesarios. |
| Backups del VPS | Pueden contener datos de producción. | Mantener fuera de Git; definir retención y cifrado. |
| `.env`, `__pycache__`, `.pyc` locales | Artefactos no fuente. | Ignorados por `.gitignore`. |

## Evidencia de validación local

```bash
cd MyOwnClone
npm run typecheck
npm test -- --run src/__tests__/app/facturacion.test.tsx
```

Ejecución previa: `typecheck` OK; test de facturación/planes OK con 8 tests.

