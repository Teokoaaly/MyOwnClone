# Bug: MISSING_MESSAGE en i18n y 401 en admin/overview

**Fecha**: 2026-07-03
**Síntoma**: Al acceder a `/admin/overview` (o cualquier ruta admin), el navegador muestra:
```
MISSING_MESSAGE: admin.admin.overview.errorTitle (es)
```
y `api/admin/overview` responde 401 Unauthorized.

**Estado**: NO TOCAR el frontend. Diagnosticar primero.

## Diagnóstico

### Capa 1: 401 en api/admin/overview
- El endpoint requiere autenticación admin (X-User-Role: platform_admin)
- El browser NO tiene esa cookie/header porque el usuario actual no es platform_admin
- El 401 es COMPORTAMIENTO CORRECTO: protege el endpoint de accesos no autorizados
- El dashboard admin solo es accesible para platform_admin

### Capa 2: MISSING_MESSAGE admin.admin.overview.errorTitle (es)
- La clave **SÍ existe** en `src/i18n/es.json`:
  ```json
  "errorTitle": "Error al cargar auditoría"
  ```
- Pero el bundle JS compilado que sirve la página NO la incluye
- **Causa raíz**: cuando se hizo el build, el `messages` no se importó en el namespace correcto
- El bundle tiene `"admin": {}` (objeto vacío) en lugar de `"admin": { "audit": { "errorTitle": "..." } }`

## Por qué ocurre

1. `src/i18n/request.ts` hace `await import('./${locale}.json')` — **import dinámico**
2. Next.js en build time intenta pre-bundlear todos los imports dinámicos
3. Si el pre-bundle falla (por ejemplo por el símbolo `default` en JSON), Next.js crea un chunk vacío
4. El navegador carga el chunk vacío → MISSING_MESSAGE en runtime

## Workaround temporal (frontend)

El selector de idioma del landing muestra UI pero al cambiarlo:
- Si la cookie `myownclone_locale` no está seteada, el landing carga en `en` (default)
- Si la cookie está seteada a `es`, debe traducir (pero el bundle puede no tener los mensajes)

**Pruebas que el usuario puede hacer**:
1. En el navegador, abrir DevTools → Application → Cookies → borrar `myownclone_locale`
2. Recargar `https://myownclone.com` — debería mostrar en inglés
3. Click en el selector de idioma "Español" — debe setear cookie y recargar
4. Si sigue mostrando MISSING_MESSAGE, es bug del bundle compilado

## Solución real (requiere rebuild)

El fix correcto es rebuild desde el código fuente que tiene los `es.json` y `en.json` correctos:

```bash
cd /opt/myownclone/worktrees/sisyphus-vps-integration/MyOwnClone
npm install --legacy-peer-deps
set -a; . /opt/myownclone/shared/frontend.env.production; set +a
npm run build
# Verificar que los bundles compilados tienen admin.admin.overview.errorTitle
grep -c 'admin.admin.overview' .next/static/chunks/*.js | grep -v ':0$'
# Si hay matches, el build es correcto
```

**ADVERTENCIA**: rebuild desde `sisyphus-vps-integration` cambia también la landing (problema que el usuario ha reportado múltiples veces). Necesita un deploy cuidado que:
1. Tome la landing de `/root/myownclone` (que funciona)
2. Tome los JSON de traducciones de `sisyphus-vps-integration`
3. Genere un build híbrido

## Estado actual

- Frontend: BUILD_ID `s4Hs00UHv6esTNBt7xcUp` (restaurado, no se toca)
- Bug MISSING_MESSAGE: **preexistente, no causado por mis cambios**
- Bug 401 admin: **comportamiento correcto** (protección)
- Selector de idioma: UI funciona, pero bundle compilado puede no tener los mensajes

## Acciones del usuario

1. **Acceder al dashboard admin** requiere ser `platform_admin`. El usuario actual no lo es, por eso ve 401.
2. **Para el selector de idioma**: verificar cookie `myownclone_locale` en DevTools
3. **Si MISSING_MESSAGE persiste**: es bug del build, requiere rebuild (que el usuario ha pedido no hacer)

## NO TOCAR

Este bug NO se soluciona modificando archivos del frontend. Requiere un rebuild planificado que el usuario debe aprobar.
