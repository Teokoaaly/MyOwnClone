# MASTER_PLAN_I18N_EXECUTION.md — Plan Maestro i18n Ejecutable

> **Generado:** 2026-06-16
> **Estado del repo (verificado live):** `100.125.128.116:/root/myownclone`
> **Reemplaza/supera:** `MASTER_PLAN_LANGUAGE_SWITCH_EN_ES.md` (estratégico) + `I18N_50_LANGUAGES_PLAN.md` (ambicioso). Este es el plan **operativo y basado en datos reales**.

---

## 0. AUDITORÍA EN VIVO (snapshot 2026-06-16)

Comandos ejecutados y resultados:

| Métrica | Valor | Comando |
|---|---|---|
| Archivos `.tsx` totales en `src/` | **80** | `find src -name '*.tsx' \| wc -l` |
| Archivos con strings UI hardcodeados | **52** (65%) | `grep -rEc '<UI words>' src/ --include='*.tsx'` |
| Archivos que usan `useTranslations` | **0** | `grep -rl 'useTranslations' src/` |
| Strings UI hardcodeados (matches) | **~1,041** | `grep -rE 'Sign in\|Create\|Welcome\|...' src/ --include='*.tsx'` |
| Locales configurados en `routing.ts` | `['es', 'en']` | `cat src/i18n/routing.ts` |
| `next-intl` plugin en `next.config.ts` | ✅ Sí (vía `createNextIntlPlugin`) | `cat next.config.ts` |
| `middleware.ts` para detección de locale | ❌ **No existe** | `find . -name middleware.ts` |
| Segmento `[locale]/` en app router | ❌ **No existe** | `find src/app -type d -name '[locale]'` |
| Archivos de mensajes | `en.json` (2.8KB), `es.json` (2.9KB) | parcial: solo meta+nav+auth+onboarding+dashboard+clone+errors+plans |
| Provider (`NextIntlClientProvider`) wired | ✅ Sí en `app/providers.tsx` | `cat src/app/providers.tsx` |
| Detección de locale actual | Header custom `x-locale` (set por infra) | `src/i18n/request.ts` + `src/app/layout.tsx` |
| Rutas legacy con español hardcodeado | `src/app/es/onboarding`, `src/app/es/verificar` | dead-code (2 archivos) |

### Diagnóstico resumido

- **El scaffolding de `next-intl` está montado** (config, provider, JSONs, routing, navigation helpers) — eso es el ~30% del trabajo.
- **Falta el 70% restante**: cambiar las ~1,041 strings hardcodeadas por `useTranslations('namespace')`, traducir los JSONs con namespaces nuevos, decidir arquitectura de routing (`/[locale]/` vs cookie/header), y construir un selector visible.
- **Los 2 planes previos en `.docs_md/` son correctos en visión pero ninguno se ejecutó**. `I18N_50_LANGUAGES_PLAN.md` apunta a 50 idiomas con auto-traducción IA — eso es **escalable a futuro, NO el primer hito**. El usuario pidió EN/ES primero.
- **No hay middleware**, así que cambiar idioma hoy requiere recargar con header custom. Inaceptable para usuarios reales.

### Top 15 archivos con más strings hardcodeados

| # | Archivo | Matches aprox. |
|---|---|---|
| 1 | `src/app/admin/tenants/page.tsx` | ~49 |
| 2 | `src/app/(dashboard)/reuniones/page.tsx` | ~40 |
| 3 | `src/app/(dashboard)/settings/page.tsx` | ~35 |
| 4 | `src/app/(dashboard)/cerebro/page.tsx` | ~26 |
| 5 | `src/app/admin/tenants/[id]/page.tsx` | ~26 |
| 6 | `src/app/(dashboard)/inbox/page.tsx` | ~25 |
| 7 | `src/app/(dashboard)/productos/page.tsx` | ~25 |
| 8 | `src/components/ui/SearchCommandBar.tsx` | ~23 |
| 9 | `src/app/(dashboard)/onboarding/page.tsx` | ~18 |
| 10 | `src/app/(dashboard)/biblioteca/nuevo/page.tsx` | ~18 |
| 11 | `src/app/(dashboard)/resumen/page.tsx` | ~15 |
| 12 | `src/components/chat/ChatPanel.tsx` | ~15 |
| 13 | `src/app/registro/register-form.tsx` | ~13 |
| 14 | `src/app/login/login-form.tsx` | ~12 |
| 15 | `src/components/admin/CourtesyButton.tsx` | ~12 |

---

## 1. OBJETIVO Y ALCANCE

**Hito 1 (esta iteración):** MyOwnClone 100% traducible entre **inglés (default)** y **español**, con selector visible, persistencia, y arquitectura limpia que permita añadir más idiomas sin re-arquitectura.

**Hito 2 (futuro, no en este plan):** añadir 3-5 idiomas adicionales (fr, de, pt, it, ca) reutilizando el mismo pipeline + script de auto-traducción IA. Documentado aparte, no aquí.

**Out of scope:**
- Traducción de contenido generado por usuarios (mensajes de chat, nombres de clones, knowledge uploads).
- Localización de moneda/fechas en analytics (Hito 2).
- 50 idiomas simultáneos (overhead no justificado).

---

## 2. DECISIONES DE ARQUITECTURA

### 2.1 Routing: cookie + header, NO segmento `[locale]/`

**Por qué no `[locale]/`:**
- 33 archivos de páginas + 30 componentes reescritos en paths.
- Rutas legacy `src/app/es/onboarding` y `src/app/es/verificar` colisionan.
- SEO no es crítico en SaaS dashboard (autenticado).
- Doble mantenimiento si el usuario guarda bookmark en `/en/dashboard` y mañana queremos renombrar.

**Decisión:** mantener arquitectura actual (header/cookie) y **añadir `middleware.ts`** que:
1. Lee cookie `myownclone_locale`.
2. Si no, lee `Accept-Language`.
3. Si no, usa `en` (default).
4. Inyecta header `x-locale` para que el `layout.tsx` actual lo recoja sin cambios.
5. Persiste cookie con `SameSite=Lax`, `Max-Age=1y`.

**Beneficio:** 1 archivo nuevo (`middleware.ts`) + ajustes en `request.ts`. Cero cambios en paths.

### 2.2 Namespaces de traducción

Partir de los 8 namespaces existentes y añadir los que faltan:

| Namespace | Estado actual | Áreas |
|---|---|---|
| `meta` | ✅ existe | HTML title/description |
| `nav` | ✅ existe | Header público |
| `auth` | ✅ existe | Login, registro, magic link |
| `onboarding` | ✅ existe | Wizard inicial |
| `dashboard` | ✅ existe (mínimo, faltan strings reales) | Sidebar items |
| `clone` | ✅ existe | Chat widget público |
| `errors` | ✅ existe | Errores genéricos |
| `plans` | ✅ existe | Pricing |
| **`common`** | ❌ falta | Botones genéricos (Save, Cancel, Delete, Edit, etc.) |
| **`sidebar`** | ❌ falta | Tooltips y labels completos de sidebar |
| **`search`** | ❌ falta | `SearchCommandBar` (23 strings) |
| **`chat`** | ❌ falta | `ChatPanel`, `MessageBubble` (panel interno) |
| **`library`** | ❌ falta | Biblioteca, Brain, Productos |
| **`meetings`** | ❌ falta | Reuniones |
| **`inbox`** | ❌ falta | Inbox |
| **`analytics`** | ❌ falta | Analíticas + charts |
| **`billing`** | ❌ falta | Facturación, planes, Stripe |
| **`settings`** | ❌ falta | Configuración + Settings (legacy) |
| **`admin`** | ❌ falta | AdminShell, tenants, audit, feedback, impersonation |
| **`onboarding_dashboard`** | ❌ falta | Onboarding interno post-registro |
| **`landing`** | ❌ falta | Página pública `/` |
| **`legal`** | ❌ falta | `/legal` |
| **`validation`** | ❌ falta | Errores de form (Zod, server actions) |

**Total: 22 namespaces** (8 actuales + 14 nuevos).

### 2.3 Tipado estricto

Usar `next-intl` con TypeScript en modo estricto: definir `GlobalConfig` y `Messages` types para que **keys faltantes sean error de compilación**, no warning runtime.

---

## 3. FASES DE EJECUCIÓN

### FASE 0 — Setup (sin tocar UI)

| # | Tarea | Esfuerzo | Riesgo |
|---|---|---|---|
| 0.1 | Crear `middleware.ts` con detección cookie→Accept-Language→default | S | bajo |
| 0.2 | Mover `src/app/es/` (legacy) a `src/app/_legacy_es/` para evitar colisión con namespace | S | bajo |
| 0.3 | Activar typed translations en `next-intl` (declarar `Messages` global) | S | bajo |
| 0.4 | Crear `scripts/i18n/audit.ts` (cuenta strings por namespace, falla CI si >0 hardcoded) | M | medio |
| 0.5 | Crear `scripts/i18n/check-keys.ts` (compara `en.json` vs `es.json`, falla si keys faltan) | S | bajo |
| 0.6 | Crear `LanguageSwitcher` componente client (dropdown EN/ES, escribe cookie) | S | bajo |
| 0.7 | Hookear `LanguageSwitcher` en `Sidebar` footer + `SettingsPage` | S | bajo |

**Verificación Fase 0:** `curl -H "Cookie: myownclone_locale=es" https://app/resumen` → refleja español en next-intl context. `curl -H "Accept-Language: es-ES"` → idem.

---

### FASE 1 — Componentes compartidos y dashboard (orden: hojas → raíz)

Orden importa: traducir hojas primero, porque varios componentes hoja los consume el layout.

| # | Archivo | Strings aprox. | Namespace destino |
|---|---|---|---|
| 1.1 | `components/ui/EmptyState.tsx` | 4 | `common` |
| 1.2 | `components/ui/LoadingState.tsx` | 3 | `common` |
| 1.3 | `components/ui/ErrorState.tsx` | 2 | `common` |
| 1.4 | `components/ui/Modal.tsx` | 4 | `common` |
| 1.5 | `components/ui/Sheet.tsx` | 4 | `common` |
| 1.6 | `components/ui/StatusBadge.tsx` | 3 | `common` |
| 1.7 | `components/ui/BarChart.tsx` | 1 | `analytics` |
| 1.8 | `components/ui/ThemeToggle.tsx` | 2 | `common` |
| 1.9 | `components/ui/MobileNav.tsx` | 5 | `sidebar` |
| 1.10 | `components/ui/SearchCommandBar.tsx` | ~23 | `search` |
| 1.11 | `components/dashboard/Sidebar.tsx` | ~8 (navItems vienen de config) | `sidebar` |
| 1.12 | `components/dashboard/StatsCard.tsx` | 3 | `common` |
| 1.13 | `components/dashboard/QuickActionCard.tsx` | 1 | `common` |
| 1.14 | `components/dashboard/HeaderBreadcrumb.tsx` | 1 | `common` |
| 1.15 | `components/dashboard/DashboardTopbarSearch.tsx` | ~6 | `search` |
| 1.16 | `components/dashboard/OnboardingBanner.tsx` | 3 | `onboarding_dashboard` |
| 1.17 | `components/dashboard/ChatOrb.tsx` | 2 | `chat` |
| 1.18 | `components/dashboard/EndpointCard.tsx` | 2 | `common` |
| 1.19 | `components/dashboard/CloneIdResolver.tsx` | 2 | `clone` |
| 1.20 | `components/chat/ChatPanel.tsx` | ~15 | `chat` |
| 1.21 | `components/chat/MessageBubble.tsx` | 3 | `chat` |
| 1.22 | `components/chat/SiloToggle.tsx` | 3 | `chat` |
| 1.23 | `components/auth/SignOutButton.tsx` | 2 | `auth` |

**Subtotal Fase 1: ~97 strings en 23 archivos.**

---

### FASE 2 — Páginas dashboard (grupo `(dashboard)/*`)

| # | Archivo | Strings aprox. | Namespace destino |
|---|---|---|---|
| 2.1 | `(dashboard)/layout.tsx` | 2 | `sidebar` |
| 2.2 | `(dashboard)/resumen/page.tsx` | ~15 | `dashboard`, `analytics` |
| 2.3 | `(dashboard)/biblioteca/page.tsx` | ~12 | `library` |
| 2.4 | `(dashboard)/biblioteca/nuevo/page.tsx` | ~18 | `library` |
| 2.5 | `(dashboard)/cerebro/page.tsx` | ~26 | `library` |
| 2.6 | `(dashboard)/productos/page.tsx` | ~25 | `library` |
| 2.7 | `(dashboard)/inbox/page.tsx` | ~25 | `inbox` |
| 2.8 | `(dashboard)/reuniones/page.tsx` | ~40 | `meetings` |
| 2.9 | `(dashboard)/analiticas/page.tsx` | ~7 | `analytics` |
| 2.10 | `(dashboard)/facturacion/page.tsx` | ~13 | `billing` |
| 2.11 | `(dashboard)/configuracion/page.tsx` | ~3 | `settings` |
| 2.12 | `(dashboard)/settings/page.tsx` | ~35 | `settings` |
| 2.13 | `(dashboard)/onboarding/page.tsx` | ~18 | `onboarding_dashboard` |

**Subtotal Fase 2: ~237 strings en 13 archivos.**

---

### FASE 3 — Auth y páginas públicas

| # | Archivo | Strings aprox. | Namespace destino |
|---|---|---|---|
| 3.1 | `app/layout.tsx` (metadata) | 2 | `meta` |
| 3.2 | `app/page.tsx` (landing) | ~15 | `landing` |
| 3.3 | `app/login/page.tsx` | 1 | `auth` |
| 3.4 | `app/login/login-form.tsx` | ~12 | `auth` |
| 3.5 | `app/registro/page.tsx` | 1 | `auth` |
| 3.6 | `app/registro/register-form.tsx` | ~13 | `auth` |
| 3.7 | `app/forgot-password/page.tsx` | ~7 | `auth` |
| 3.8 | `app/reset-password/page.tsx` | ~9 | `auth` |
| 3.9 | `app/legal/page.tsx` | ~7 | `legal` |
| 3.10 | `(public)/layout.tsx` | 1 | `landing` |
| 3.11 | `(public)/[slug]/page.tsx` (clone público) | ~10 | `clone` |
| 3.12 | Eliminar `app/es/verificar` y `app/es/onboarding` legacy | — | — |

**Subtotal Fase 3: ~78 strings en 12 archivos (2 archivos a eliminar).**

---

### FASE 4 — Admin panel

| # | Archivo | Strings aprox. | Namespace destino |
|---|---|---|---|
| 4.1 | `admin/layout.tsx` | 1 | `admin` |
| 4.2 | `admin/resumen/page.tsx` | ~4 | `admin` |
| 4.3 | `admin/tenants/page.tsx` | ~49 | `admin` |
| 4.4 | `admin/tenants/[id]/page.tsx` | ~26 | `admin` |
| 4.5 | `admin/audit/page.tsx` | ~5 | `admin` |
| 4.6 | `admin/courtesy/page.tsx` | ~5 | `admin` |
| 4.7 | `admin/feedback/page.tsx` | ~5 | `admin` |
| 4.8 | `admin/impersonation/page.tsx` | ~5 | `admin` |
| 4.9 | `components/admin/AdminShell.tsx` | 2 | `admin` |
| 4.10 | `components/admin/AdminTopbar.tsx` | 2 | `admin` |
| 4.11 | `components/admin/PageHeader.tsx` | 2 | `admin` |
| 4.12 | `components/admin/Field.tsx` | 6 | `admin` |
| 4.13 | `components/admin/FilterBar.tsx` | 2 | `admin` |
| 4.14 | `components/admin/Pagination.tsx` | 5 | `admin` |
| 4.15 | `components/admin/CourtesyButton.tsx` | ~12 | `admin` |
| 4.16 | `components/admin/ImpersonateButton.tsx` | ~9 | `admin` |

**Subtotal Fase 4: ~140 strings en 16 archivos.**

---

### FASE 5 — Validación de strings y QA

| # | Tarea |
|---|---|
| 5.1 | Ejecutar `scripts/i18n/audit.ts` → debe dar 0 hardcoded |
| 5.2 | Ejecutar `scripts/i18n/check-keys.ts` → `en` y `es` con mismas keys |
| 5.3 | `npm run typecheck` (modo estricto next-intl) |
| 5.4 | `npm run lint` |
| 5.5 | `npm run build` |
| 5.6 | QA manual matrix (login, dashboard, chat, billing, admin, settings, mobile) |
| 5.7 | Test E2E Playwright: switcher cambia UI, cookie persiste, refresh mantiene idioma |
| 5.8 | Verificar que `/[slug]` público (clone widget) detecta idioma del navegador |

**Total esfuerzo: 5 fases, ~64 archivos a tocar, ~552 strings únicos a traducir (1,041 matches con duplicados inter-archivo).**

Estimación realista: 3-4 días de trabajo concentrado de un dev senior, o ~10-15 horas con paralelización vía delegate_task (3 workers en paralelo, uno por fase/área).

---

## 4. ENTREGABLES (artefactos a producir)

1. `src/middleware.ts` — detección de locale.
2. `src/i18n/en.json` y `src/i18n/es.json` — completos, 22 namespaces, tipados.
3. `src/components/LanguageSwitcher.tsx` — selector visible.
4. `scripts/i18n/audit.ts` — CI guard.
5. `scripts/i18n/check-keys.ts` — CI guard.
6. `src/app/_legacy_es/` — archivo de las 2 rutas legacy.
7. `src/types/i18n.d.ts` — declaración global de `Messages`.
8. PR con cambio en `.github/workflows/ci.yml` para correr los 2 scripts.
9. Handoff doc en `.docs_md/HANDOFF_I18N_ES_EN.md` con lo ejecutado y pendientes Hito 2.

---

## 5. RIESGOS Y MITIGACIÓN

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Rotos de hydration por `useTranslations` en client component | Alta | Medio | Convertir strings a props server→client, mantener client components tontos |
| Placeholders de formato rotos (`{days}`, `{name}`) en traducción | Media | Bajo | `scripts/i18n/check-keys.ts` valida placeholders con regex |
| Rutas legacy `/es/...` siguen activas y duplican contenido | Alta | Medio | Mover a `_legacy_es/` o eliminar en Fase 0.2 |
| Cambiar namespace rompe otras páginas que lo importan | Media | Alto | Cambiar en orden hoja→raíz, correr typecheck después de cada fase |
| `next-intl` v4 API cambia entre minor versions | Baja | Medio | Pin en `4.13.0`, no actualizar hasta cerrar Hito 1 |
| Cookie no persiste si nginx no la propaga | Baja | Bajo | Verificar `proxy_pass` con `Cookie` header; añadir a `next.config.ts` si hace falta |
| Build size aumenta ~30% con i18n completo | Alta | Bajo | Aceptable para SaaS interno; code-split por namespace en Hito 2 |

---

## 6. CRITERIOS DE ACEPTACIÓN (Hito 1 done)

- [ ] `grep -rE '<UI words>' src/ --include='*.tsx'` → 0 matches.
- [ ] `npm run typecheck` pasa con tipos i18n estrictos.
- [ ] `npm run build` pasa.
- [ ] `npm run lint` pasa.
- [ ] `scripts/i18n/check-keys.ts` pasa (mismas keys en `en.json` y `es.json`).
- [ ] Selector de idioma visible en `Sidebar` footer y en `Settings`.
- [ ] Cookie `myownclone_locale` persiste 1 año.
- [ ] `Accept-Language: es` → usuario anónimo ve UI en español.
- [ ] QA matrix manual pasada en desktop + mobile.
- [ ] Test E2E Playwright cubre: switcher funciona, cookie persiste, refresh mantiene.
- [ ] Documento de handoff escrito.

---

## 7. ORDEN DE EJECUCIÓN RECOMENDADO

1. **Auditoría extendida** (no se pidió explícitamente pero la acabo de hacer en sección 0). HECHO ✅
2. **Decidir con el usuario** si ejecuta Fase 0+1+2+3+4 enteras, o por hitos (ej. solo auth+landing en sprint 1).
3. **Si sí**: ejecutar Fases 0 → 1 → 2 → 3 → 4 → 5 en orden, con PR por fase.
4. **Si no**: priorizar Fase 3 (auth + landing) por ser user-facing y Fase 0 (middleware + switcher) por ser prerequisito.

**Sugerencia práctica:** empezar por **Fase 0** completa + **Fase 3** (auth + landing) como primer sprint, porque son prerequisito de toda la app (sin middleware no se puede probar el switcher; sin auth traducido el resto no importa). Eso son ~6 archivos tocados y desbloquea todo lo demás.

---

## 8. PRÓXIMOS PASOS (lo que necesita tu input)

1. **¿Ejecuto Fase 0 ahora?** (middleware + switcher + scripts i18n + setup). 0 strings traducidos, 0 UI tocado, ~2-3 horas.
2. **¿Ejecuto Fase 0 + Fase 3 ahora?** (auth + landing en español). 12 archivos, ~78 strings, desbloquea el resto.
3. **¿Ejecuto todo el plan ahora vía delegate_task en paralelo?** (3 workers: auth, dashboard, admin). 64 archivos, ~552 strings, ~10-15h.
4. **¿Solo quieres este plan y ejecutas tú otro día?** (no toco código).

---

*Documento vivo: actualizar contadores de strings por fase al cerrar cada PR.*
