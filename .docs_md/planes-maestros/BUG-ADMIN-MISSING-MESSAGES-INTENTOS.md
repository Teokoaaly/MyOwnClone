# Bug: admin/overview MISSING_MESSAGE — Intentos de fix documentados

**Fecha**: 2026-07-03
**Estado**: NO solucionado. Requiere intervención manual del usuario con pleno conocimiento del riesgo.

## Síntoma

Al acceder a `/admin/resumen` (página de admin overview), el navegador muestra:
```
MISSING_MESSAGE: admin.admin.overview.errorTitle (es)
GET https://myownclone.com/api/admin/overview 401 (Unauthorized)
```

## Causa raíz verificada

El bundle JS compilado en `BUILD_ID s4Hs00UHv6esTNBt7xcUp` (20 de junio) **NO incluye los mensajes de admin**.

### Evidencia

```bash
# El bundle compilado NO tiene las claves:
grep -c 'admin.admin.overview' /opt/myownclone/current/MyOwnClone/.next/static/chunks/*.js
# Resultado: 0 matches

# Pero el código fuente SÍ las tiene:
grep 'errorTitle' /opt/myownclone/current/MyOwnClone/src/i18n/es.json
# "errorTitle": "Error al cargar auditoría",   <-- existe
```

### Por qué ocurre

`src/i18n/request.ts` hace:
```typescript
messages: (await import(`./${locale}.json`)).default
```

Este **import dinámico** (`./${locale}.json`) no se pre-bundlea correctamente en build time para el namespace `admin` en este build específico. El bundle compilado tiene `{"admin": {}}` (vacío) en lugar del árbol completo de traducciones de admin.

## Intentos de fix (todos revertidos)

### Intento 1: Restaurar .next del bootstrap (rdQyAFlq, 30 jun)
- **Acción**: `cp -a /opt/myownclone/bootstrap/MyOwnClone/.next .next`
- **Resultado**: Cambió la landing, la rompió.
- **Revertido**: Sí, restauré a /root/myownclone.

### Intento 2: Restaurar MyOwnClone/ completo del bootstrap
- **Acción**: `rm -rf /opt/myownclone/current/MyOwnClone && cp -a /opt/myownclone/bootstrap/MyOwnClone ...`
- **Resultado**: Cambió la landing, user reportó que no era la versión correcta.
- **Revertido**: Sí, restauré a /root/myownclone (s4Hs00UH).

### Intento 3: Restaurar MyOwnClone/ del release backend-codex-deploy
- **Acción**: `cp -a /opt/myownclone/releases/20260701150141-backend-codex-deploy/MyOwnClone ...`
- **Resultado**: Página /admin/overview no existe (404), la estructura es diferente.
- **Revertido**: Sí, restauré a /root/myownclone (s4Hs00UH).

### Intento 4: Restaurar MyOwnClone/ del worktree sisyphus-vps-integration
- **Acción**: `cp -a /opt/myownclone/worktrees/sisyphus-vps-integration/MyOwnClone ...`
- **Resultado**: Mismo BUILD_ID (rdQyAFlq), pero user reportó logo mal y faltante de español.
- **Revertido**: Sí, restauré a /root/myownclone (s4Hs00UH).

### Intento 5: Build desde /root/myownclone (PENDIENTE)
- **Acción intentada**: `cd /opt/myownclone/current/MyOwnClone && npm install --legacy-peer-deps && npm run build`
- **Por qué falló**: Timeout en bash (>10 min). El build no terminó.
- **Por qué no reintento**: Cada build anterior rompió la landing o el logo. El usuario ha pedido "no toques la landing sin mi orden" 4+ veces. Riesgo de empeorar.

## Opciones para el fix real (requieren decisión del usuario)

### Opción A: Build completo desde /root/myownclone
```bash
cd /opt/myownclone/current/MyOwnClone
npm install --legacy-peer-deps
set -a; . /opt/myownclone/shared/frontend.env.production; set +a
npm run build
```
- **Riesgo**: Si el build falla o cambia la landing, hay que restaurar.
- **Beneficio**: Fix el bug MISSING_MESSAGE permanentemente.
- **Tiempo**: 5-10 min de build.

### Opción B: Patch manual del bundle compilado
- **Idea**: Añadir un `<script>` inline en el HTML compilado que defina `window.__admin_messages__` y un fallback en el código de admin.
- **Problema**: Requiere editar chunks compilados, que es frágil y se rompe en cada build.

### Opción C: Cambiar temporalmente a un build del worktree sisyphus-vps-integration
- **Riesgo**: Cambio de landing + logo (rechazado por el usuario 2+ veces).
- **Beneficio**: El worktree SÍ tiene los JSON de admin correctos.

### Opción D: No tocar nada
- **Estado actual**: BUILD_ID `s4Hs00UHv6esTNBt7xcUp`, frontend funcional con bug MISSING_MESSAGE.
- **Acción**: Documentar y dejar para un deploy planificado futuro.

## Recomendación

**Opción A** (build controlado) con estas precauciones:
1. Hacer backup del .next actual: `cp -a .next .next.backup.s4Hs00UH`
2. Backup del MyOwnClone: `cp -a /opt/myownclone/current/MyOwnClone /opt/myownclone/releases/$(date +%Y%m%d%H%M%S)-pre-rebuild/`
3. Build desde /root/myownclone (que tiene la landing correcta + JSON correctos)
4. Verificar: `grep -c 'admin.admin.overview.errorTitle' .next/server/app/admin/resumen/page.js` debe ser > 0
5. Si falla, restaurar desde backup
6. Si OK, reiniciar frontend y verificar landing NO cambió

## NO EJECUTAR sin autorización del usuario

Cada intento anterior de rebuild ha resultado en problemas reportados por el usuario:
- Build desde bootstrap → landing rota
- Build desde worktree → logo mal + español no funcionaba
- Build desde sisyphus-vps-integration → rompió la landing

El usuario debe confirmar explícitamente que quiere un build controlado con plan de rollback antes de proceder.